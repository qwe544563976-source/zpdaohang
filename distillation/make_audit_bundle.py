#!/usr/bin/env python3
"""给每个审计分片预切一份"该看的东西"，省掉审计员自己翻找的开销。

实测第 2 批第一轮：每个分片 agent 头 4~5 次工具调用都花在同一件事上——
从 method-recipes.json 里挑出分给自己的步骤、再去 3.45MB 的冻结原子里捞对应原文、
再去生成报告里找自己那几步的高风险词差异表。5 个分片 × 67 批，重复 300 多次。

本工具把这三样按分片预切成一个文件。审计员读一个文件就齐了，直接开始比对。

**不改变证据边界**：原文一律逐字复制 `exact_text`，不摘要、不截断；
并记下冻结文件的 sha256，审计员可随时回冻结文件核对，冻结文件仍是唯一真相。

用法：
    python distillation/make_audit_bundle.py <批次目录> --shards 5
    python distillation/make_audit_bundle.py <批次目录> --shards 5 --step-ids steps.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ATOMS = REPO / "distillation" / "_local" / "evidence_atoms.jsonl"

# 审计要看的原文字段：正文一字不改，外加定位与承接线索。
ATOM_FIELDS = (
    "evidence_atom_id", "chapter_number", "chapter_title", "verse_label",
    "content_role", "exact_text", "pdf_pages", "citation",
    "previous_atom_id", "next_atom_id", "context_before", "context_after",
    "content_missing",
)
# 步骤所属方法的哪些信息对判"有没有多说、范围诚不诚实"有用。
METHOD_FIELDS = (
    "method", "title", "target_house", "generalization_scope", "user_intents",
    "facts", "dependencies", "retrieval_plan", "stop_conditions",
)


def load_atoms(wanted: set[str]) -> dict[str, dict]:
    atoms: dict[str, dict] = {}
    for line in ATOMS.read_text(encoding="utf-8").splitlines():
        if not line.strip() or not any(atom_id in line for atom_id in wanted):
            continue
        atom = json.loads(line)
        if atom["evidence_atom_id"] in wanted:
            atoms[atom["evidence_atom_id"]] = {key: atom.get(key) for key in ATOM_FIELDS}
    return atoms


def step_atom_ids(step: dict) -> set[str]:
    found = {ref["evidence_atom_id"] for ref in step.get("evidence_refs", [])}
    found |= set(step.get("context_bindings") or [])
    for relation in step.get("exception_relations") or []:
        found |= set(relation.get("evidence_atom_ids") or [])
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument("--shards", type=int, default=5)
    parser.add_argument("--step-ids", type=Path, help="只切这些步骤；默认全批")
    args = parser.parse_args()

    recipes = json.loads(
        (args.target / "references" / "navigation" / "method-recipes.json").read_text(encoding="utf-8")
    )
    report = json.loads(
        (args.target / "validation" / "build-methods-report.json").read_text(encoding="utf-8")
    )
    terms_by_step: dict[str, list] = {}
    for entry in report.get("generation", {}).get("high_risk_terms", []) or []:
        terms_by_step.setdefault(entry.get("step_id"), []).append(entry)

    owned = {step["step_id"]: (method, step) for method in recipes["methods"] for step in method["steps"]}
    order = (
        json.loads(args.step_ids.read_text(encoding="utf-8")) if args.step_ids
        else [step["step_id"] for method in recipes["methods"] for step in method["steps"]]
    )
    unknown = [step_id for step_id in order if step_id not in owned]
    if unknown:
        print(json.dumps({"passed": False, "errors": [f"配方里没有这些步骤：{unknown[:5]}"]}, ensure_ascii=False))
        return 1

    out_dir = args.target / "validation" / "audit-bundles"
    out_dir.mkdir(parents=True, exist_ok=True)
    for stale in out_dir.glob("shard-*.json"):
        stale.unlink()

    size = -(-len(order) // args.shards)
    blocks = [order[i:i + size] for i in range(0, len(order), size)]
    frozen_sha = hashlib.sha256(ATOMS.read_bytes()).hexdigest()
    written = []
    for index, block in enumerate(blocks, 1):
        steps = []
        wanted: set[str] = set()
        for step_id in block:
            method, step = owned[step_id]
            wanted |= step_atom_ids(step)
            steps.append({
                "step_id": step_id,
                "method": {key: method.get(key) for key in METHOD_FIELDS},
                "step": step,
                "high_risk_terms": terms_by_step.get(step_id, []),
            })
        bundle = {
            "shard": index,
            "step_count": len(block),
            "frozen_atoms_path": str(ATOMS),
            "frozen_atoms_sha256": frozen_sha,
            "note": (
                "原文一律逐字复制自冻结文件的 exact_text，未摘要未截断。"
                "冻结文件仍是唯一真相，随时可回去核对。"
            ),
            "steps": steps,
            "atoms": load_atoms(wanted),
        }
        path = out_dir / f"shard-{index}.json"
        path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
        written.append({"shard": index, "path": str(path), "steps": len(block),
                        "atoms": len(bundle["atoms"]), "kb": path.stat().st_size // 1024})

    print(json.dumps({"passed": True, "shards": written}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
