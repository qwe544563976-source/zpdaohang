#!/usr/bin/env python3
"""抽取片段自验工具：把一个分组的 methods 片段包成完整 extraction，跑生成器强校验。

抽取窗口每产出一组 methods 就用它自验，直到 passed=true 才交回。
它不写任何产物，只调用唯一正式生成器 build_methods.py 的 --check-only。

用法：
    python distillation/check_fragment.py <片段.json> [--scope <原子编号列表.json>]

片段格式（只需 methods 数组，或 {"methods": [...]}）：
    [ {method 对象}, ... ]

默认 scope 取片段里实际引用到的原子编号；传 --scope 可强制指定必须全部用上的集合。
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BUILDER = REPO / "book-to-judgment-navigation" / "scripts" / "build_methods.py"
LOCAL_PACKAGE = REPO / "distillation" / "_local" / "accepted-package.local.json"
ATOMS = REPO / "distillation" / "_local" / "evidence_atoms.jsonl"

BATCH_TEMPLATE = {
    "batch_id": "fragment-self-check",
    "book_id": "bphs-97",
    "edition_id": "santhanam",
    "artifact_scope": "FORMAL",
    "pilot_only": False,
    "publishable": False,
    "book_strategy": "rule_book",
    "chapter_features": ["simple_house_placement"],
    "requested_review": "full",
    "consecutive_clean_batches": 0,
    "review_cycle_position": 1,
}


def referenced_atom_ids(methods: list[dict]) -> list[str]:
    found: list[str] = []
    for method in methods:
        for step in method.get("steps", []):
            for evidence in step.get("evidence", []):
                atom_id = evidence.get("evidence_atom_id")
                if isinstance(atom_id, str) and atom_id not in found:
                    found.append(atom_id)
            for atom_id in step.get("context_bindings", []) or []:
                if isinstance(atom_id, str) and atom_id not in found:
                    found.append(atom_id)
            for relation in step.get("exception_relations", []) or []:
                for atom_id in relation.get("evidence_atom_ids", []) or []:
                    if isinstance(atom_id, str) and atom_id not in found:
                        found.append(atom_id)
    return found


def semantic_class_for(atom_id: str, atoms: dict[str, dict]) -> str:
    role = atoms.get(atom_id, {}).get("content_role")
    return "condition_result" if role == "verse" else "foundational_knowledge"


def load_validator():
    import importlib.util

    path = REPO / "book-to-judgment-navigation" / "scripts" / "validate_delivery.py"
    spec = importlib.util.spec_from_file_location("delivery_validator_or_precheck", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def or_gate_problems(methods: list[dict]) -> list[str]:
    """用交付验证器的同一套判据预检 OR 闸门。"""
    validator = load_validator()
    problems: list[str] = []
    for method in methods:
        for number, step in enumerate(method.get("steps", []), 1):
            has_group = bool(step.get("alternative_groups"))
            source_text = "\n".join(
                [item.get("quote", "") for item in step.get("evidence", [])]
                + [step.get("minimum_supported_claim", "")]
            )
            if not has_group and validator.or_outside_results(source_text, step):
                problems.append(
                    f"方法 {method.get('method')} 步骤 {number}："
                    "条件侧含明确 OR／任选分支，必须写进 alternative_groups"
                )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fragment", type=Path)
    parser.add_argument("--scope", type=Path, help="必须全部被引用的原子编号列表 JSON")
    args = parser.parse_args()
    try:
        raw = json.loads(args.fragment.read_text(encoding="utf-8"))
        methods = raw["methods"] if isinstance(raw, dict) else raw
        if not isinstance(methods, list) or not methods:
            raise ValueError("片段里没有 methods 数组")
        # 抽取员会反复自验，每次全量解析 2024 条原子（3.45MB）纯属浪费；
        # 只解析本片段真正引用到的那几条。
        wanted = set(json.loads(args.scope.read_text(encoding="utf-8"))) if args.scope else set()
        wanted |= set(referenced_atom_ids(methods))
        atoms = {}
        for line in ATOMS.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            # 先按编号子串粗筛，避开对无关行做完整 JSON 解析
            if not any(atom_id in line for atom_id in wanted):
                continue
            atom = json.loads(line)
            if atom["evidence_atom_id"] in wanted:
                atoms[atom["evidence_atom_id"]] = atom

        scope = json.loads(args.scope.read_text(encoding="utf-8")) if args.scope else referenced_atom_ids(methods)
        unknown = [atom_id for atom_id in scope if atom_id not in atoms]
        if unknown:
            raise ValueError(f"scope 里有不存在的原文编号：{unknown}")

        extraction = {
            "schema_version": "judgment-method-extraction/v2",
            "batch": BATCH_TEMPLATE,
            "source_scope": scope,
            "source_records": [
                {
                    "evidence_atom_id": atom_id,
                    "semantic_class": semantic_class_for(atom_id, atoms),
                    "risk_flags": [],
                }
                for atom_id in scope
            ],
            "methods": methods,
        }
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "extraction.json"
            path.write_text(json.dumps(extraction, ensure_ascii=False), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, str(BUILDER),
                    "--extraction", str(path),
                    "--accepted-package", str(LOCAL_PACKAGE),
                    "--output", str(Path(temporary) / "method-recipes.json"),
                    "--check-only",
                ],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
        if result.returncode != 0:
            print(result.stdout or result.stderr)
            return result.returncode

        # 生成器不查 OR 闸门（那是交付验证的活），但等到最后才发现太晚：
        # 这里先用验证器的同一套判据预检，让抽取当场看到"条件里的或没拆分支"。
        or_problems = or_gate_problems(methods)
        report = json.loads(result.stdout)
        if or_problems:
            report["passed"] = False
            report["errors"] = or_problems
            print(json.dumps(report, ensure_ascii=False, indent=2))
            return 1
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"passed": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
