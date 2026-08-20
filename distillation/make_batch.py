#!/usr/bin/env python3
"""把已通过自验的抽取片段合成正式批次目录，跑完整生产线到机器验收。

顺序（对应必读卡的固定工作链）：
1. 合并 fragments/*.json → 完整 extraction（source_scope = 本批全部原子）；
2. 唯一入口 build_methods.py 装配 method-recipes.json / query-recipes.json / method-source-scan.json；
3. 生成知识地图（章节/主题/术语，只记位置，不是证据）、工作单、蒸馏来源清单、上游问题记录；
4. validate_delivery.py --render-derived 生成人读派生文件；
5. validate_delivery.py --require-v2 机械验收。

用法：python distillation/make_batch.py [--batch-id ...] [--target ...]
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "book-to-judgment-navigation"
BUILDER = SKILL / "scripts" / "build_methods.py"
VALIDATOR = SKILL / "scripts" / "validate_delivery.py"
LOCAL = REPO / "distillation" / "_local"
FRAGMENTS = LOCAL / "fragments"
LOCAL_PACKAGE = LOCAL / "accepted-package.local.json"
ATOMS = LOCAL / "evidence_atoms.jsonl"
SCOPE_FILE = LOCAL / "groups" / "all-scope.json"

DEFAULT_BATCH_ID = "BPHS97_ch14-16_siblings-home-children_20260820_run01"
DEFAULT_TARGET = REPO / "distillation" / "bphs-97" / "batches" / DEFAULT_BATCH_ID


def load_atoms() -> dict[str, dict]:
    atoms = {}
    for line in ATOMS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            atom = json.loads(line)
            atoms[atom["evidence_atom_id"]] = atom
    return atoms


def build_extraction(batch_id: str, scope: list[str], atoms: dict[str, dict], fragments: Path) -> dict:
    methods: list[dict] = []
    for path in sorted(fragments.glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        methods.extend(raw["methods"] if isinstance(raw, dict) else raw)
    if not methods:
        raise SystemExit("没有可合并的抽取片段")
    ids = [item["method"] for item in methods]
    duplicates = sorted({value for value in ids if ids.count(value) > 1})
    if duplicates:
        raise SystemExit(f"方法编号跨组重复：{duplicates}")
    return {
        "schema_version": "judgment-method-extraction/v2",
        "batch": {
            "batch_id": batch_id,
            "book_id": "bphs-97",
            "edition_id": "santhanam",
            "artifact_scope": "FORMAL",
            "pilot_only": False,
            "publishable": False,
            "book_strategy": "rule_book",
            # 本批是三、四、五宫的落宫与宫主断语，无大运流年、无多星复杂瑜伽。
            "chapter_features": ["simple_house_placement"],
            # 首批用新工具，强制逐步全审（定案：新工具首批不许抽审）。
            "requested_review": "full",
            "consecutive_clean_batches": 0,
            "review_cycle_position": 1,
        },
        "source_scope": scope,
        "source_records": [
            {
                "evidence_atom_id": atom_id,
                "semantic_class": "condition_result",
                "risk_flags": [],
            }
            for atom_id in scope
        ],
        "methods": methods,
    }


def knowledge_maps(target: Path, scope: list[str], atoms: dict[str, dict]) -> None:
    chapters: dict[int, dict] = {}
    for atom_id in scope:
        atom = atoms[atom_id]
        entry = chapters.setdefault(
            atom["chapter_number"],
            {
                "chapter_number": atom["chapter_number"],
                "title": atom["chapter_title"],
                "pdf_pages": [],
                "evidence_atom_ids": [],
            },
        )
        entry["evidence_atom_ids"].append(atom_id)
        for page in atom.get("pdf_pages", []):
            if page not in entry["pdf_pages"]:
                entry["pdf_pages"].append(page)

    # 主题与术语只在本批真有原文时才生成：知识地图里不允许出现没有原文编号的空条目。
    TOPIC_SPECS = (
        ("sahaj-bhava-co-born", "三宫：兄弟姐妹", 14),
        ("bandhu-bhava-home-mother-vehicle", "四宫：住房、母亲、车乘", 15),
        ("putr-bhava-children", "五宫：子女", 16),
    )
    TERM_SPECS = (
        ("Sahaj Bhava", "三宫；兄弟姐妹、勇气等事项。", 14),
        ("Bandhu Bhava", "四宫；住房、母亲、车乘等事项。", 15),
        ("Putr Bhava", "五宫；子女、智力等事项。", 16),
    )

    def scoped(chapter: int) -> list[str]:
        return [atom_id for atom_id in scope if atoms[atom_id]["chapter_number"] == chapter]

    topics = {
        name: {"title": title, "chapter_numbers": [chapter], "evidence_atom_ids": scoped(chapter)}
        for name, title, chapter in TOPIC_SPECS
        if scoped(chapter)
    }
    glossary = [
        {"term": term, "explanation": explanation, "evidence_atom_ids": scoped(chapter)[:3]}
        for term, explanation, chapter in TERM_SPECS
        if scoped(chapter)
    ]
    if not topics or not glossary:
        raise SystemExit("本批范围内没有可建主题或术语的原文")

    write_json(target / "references" / "knowledge" / "chapter-map.json", {
        "schema_version": "knowledge-chapter-map/v1",
        "book_id": "bphs-97",
        "edition_id": "santhanam",
        "pilot_only": False,
        "publishable": False,
        "chapters": [chapters[key] for key in sorted(chapters)],
    })
    write_json(target / "references" / "knowledge" / "topic-map.json", {
        "schema_version": "knowledge-topic-map/v1",
        "book_id": "bphs-97",
        "edition_id": "santhanam",
        "pilot_only": False,
        "publishable": False,
        "topics": topics,
    })
    write_json(target / "references" / "knowledge" / "glossary.json", {
        "schema_version": "knowledge-glossary/v1",
        "book_id": "bphs-97",
        "edition_id": "santhanam",
        "pilot_only": False,
        "publishable": False,
        "terms": glossary,
    })


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run(command: list[str], label: str) -> dict:
    result = subprocess.run(command, check=False, capture_output=True, text=True, encoding="utf-8")
    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError:
        raise SystemExit(f"{label} 没有输出可读 JSON：\n{result.stdout}\n{result.stderr}")
    return {"returncode": result.returncode, "report": report}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-id", default=DEFAULT_BATCH_ID)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--keep", action="store_true", help="不清空目标目录（默认重建）")
    parser.add_argument("--scope", type=Path, default=SCOPE_FILE, help="本批原文编号清单")
    parser.add_argument("--fragments", type=Path, default=FRAGMENTS, help="抽取片段目录")
    args = parser.parse_args()

    target = args.target.resolve()
    if target.exists() and not args.keep:
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)

    atoms = load_atoms()
    scope = json.loads(args.scope.read_text(encoding="utf-8"))
    package = json.loads(LOCAL_PACKAGE.read_text(encoding="utf-8"))

    # 工作单的允许范围必须与本批实际原文严格相等：
    # 整章都在本批的写进 chapter_scope；只取了一章里一部分的，逐条写进 evidence_atom_scope。
    # 否则验证器会按整章加载原子，把没生产的原文算成"遗漏"。
    scope_set = set(scope)
    chapters_touched = sorted({atoms[atom_id]["chapter_number"] for atom_id in scope})
    chapter_scope: list[int] = []
    atom_scope: list[str] = []
    for chapter in chapters_touched:
        whole = {
            atom_id for atom_id, atom in atoms.items() if atom["chapter_number"] == chapter
        }
        if whole <= scope_set:
            chapter_scope.append(chapter)
        else:
            atom_scope.extend(atom_id for atom_id in scope if atoms[atom_id]["chapter_number"] == chapter)
    extraction = build_extraction(args.batch_id, scope, atoms, args.fragments.resolve())
    extraction_path = target / "validation" / "stage-a-extraction.json"
    write_json(extraction_path, extraction)

    build = run(
        [
            sys.executable, str(BUILDER),
            "--extraction", str(extraction_path),
            "--accepted-package", str(LOCAL_PACKAGE),
            "--output", str(target / "references" / "navigation" / "method-recipes.json"),
        ],
        "build_methods.py",
    )
    if build["returncode"] != 0:
        print(json.dumps({"stage": "build", **build}, ensure_ascii=False, indent=2))
        return 1

    knowledge_maps(target, scope, atoms)

    write_json(target / "WORK_ORDER.json", {
        "job_name": args.batch_id,
        "operation": "formal",
        "pilot_only": False,
        "publishable": False,
        "artifact_scope": "FORMAL",
        "formal_migration": "ALLOWED_AFTER_AUDIT",
        "accepted_package": package.get("package_id"),
        "mechanical_gate_status": "not_run",
        "book": {
            "title": "Brihat Parashara Hora Shastra",
            "author": "Maharshi Parashara",
            "edition": "Santhanam 97-chapter edition",
        },
        "book_class": "A",
        "distillation_strategy": "rule_book",
        "input": {
            "accepted_package_path": str(LOCAL_PACKAGE),
            "chapter_scope": chapter_scope,
            "evidence_atom_scope": atom_scope,
        },
        "target_dir": str(target),
        "topic_order": ["三宫兄弟姐妹", "四宫住房母亲车乘", "五宫子女"],
        "review_requirement": "首批使用 v2 新工具，逐步全审，不得抽审",
    })

    write_json(target / "DISTILLATION_SOURCE.json", {
        "distillation_run_id": args.batch_id,
        "artifact_scope": "FORMAL",
        "pilot_only": False,
        "publishable": False,
        "book_id": package["book"]["book_id"],
        "edition_id": package["book"]["edition_id"],
        "source_artifact_id": package["book"]["source_artifact_id"],
        "accepted_package_id": package["package_id"],
        "accepted_package_path": str(LOCAL_PACKAGE),
        "evidence_contract_version": package["evidence_atoms"]["contract_version"],
        "evidence_atoms_path": str(ATOMS.resolve()),
        "evidence_atoms_sha256": package["evidence_atoms"]["content_sha256"],
        "chapter_scope": chapter_scope,
        "created_at": "2026-08-20T00:00:00Z",
    })

    write_json(target / "UPSTREAM_ISSUES.json", {
        "schema_version": "upstream-issues/v1",
        "pilot_only": False,
        "publishable": False,
        "issues": [],
    })

    (target / "references" / "navigation" / "version-routing.md").write_text(
        "# 版本路由\n\n本批只使用 BPHS 97 章版（R. Santhanam 英译，`bphs-97:santhanam`）。\n"
        "100 章版是独立版本，原文与引用永不混写；本批不引用、不比对、不合并。\n",
        encoding="utf-8",
    )
    (target / "SKILL.md").write_text(
        f"# {args.batch_id}\n\n"
        "BPHS 97 章版第 14~16 章（三宫兄弟姐妹、四宫住房母亲车乘、五宫子女）正式方法批次。\n\n"
        "- 唯一方法真相：`references/navigation/method-recipes.json`\n"
        "- 唯一主题真相：`references/navigation/query-recipes.json`\n"
        "- 人读文件全部由验证器 `--render-derived` 生成，手改即判失败。\n"
        "- 本批全部方法 `executable_in_pilot=false`：JH8 排盘事实尚未接通，只做证据绑定，不进执行主路。\n",
        encoding="utf-8",
    )
    (target / "PIPELINE_STATE.md").write_text(
        f"# {args.batch_id} 进度\n\n"
        "- 已完成：正式书包复核、四组并行抽取并各自通过生成器强校验、合并装配、知识地图、机器验收。\n"
        "- 待办：独立语义审计（未参与生成的窗口）→ 并入用户本机全书总账。\n"
        "- 本批不含大运流年、多星同聚或复杂瑜伽，但按新工具首批规则逐步全审。\n",
        encoding="utf-8",
    )

    render = run([sys.executable, str(VALIDATOR), str(target), "--render-derived"], "render-derived")
    rendered_files = render["report"].get("rendered_files")
    if rendered_files is None:
        print(json.dumps({"stage": "render", **render}, ensure_ascii=False, indent=2))
        return 1
    validate = run([sys.executable, str(VALIDATOR), str(target), "--require-v2"], "validate --require-v2")

    recipes = json.loads((target / "references" / "navigation" / "method-recipes.json").read_text(encoding="utf-8"))
    print(json.dumps({
        "batch_id": args.batch_id,
        "target": str(target),
        "build": build["report"],
        "rendered_files": rendered_files,
        "validate_returncode": validate["returncode"],
        "validate": validate["report"],
        "methods": len(recipes.get("methods", [])),
        "steps": sum(len(m.get("steps", [])) for m in recipes.get("methods", [])),
    }, ensure_ascii=False, indent=2))
    return 0 if validate["returncode"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
