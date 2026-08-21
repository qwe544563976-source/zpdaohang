#!/usr/bin/env python3
"""按批次计划导出某一批的原文分组，供抽取窗口读取。

批量生产时每批开工的第一步。它只读 `BATCH_PLAN.json` 和冻结原子，
把该批原文切成若干组写到 `_local/batches/<批次标签>/groups/`，
并写一份 `scope.json`（该批全部原子编号，供 make_batch 使用）。

分组只为并行方便，不改变证据边界：同一条原文永远整条进同一组，
组内保留 context_before/after 和 prev/next 编号，代词承接不会被切断。

用法：
    python distillation/export_batch.py ch17-18
    python distillation/export_batch.py ch17-18 --groups 4
    python distillation/export_batch.py --list
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLAN = REPO / "distillation" / "BATCH_PLAN.json"
ATOMS = REPO / "distillation" / "_local" / "evidence_atoms.jsonl"
OUT_ROOT = REPO / "distillation" / "_local" / "batches"

KEEP_FIELDS = (
    "evidence_atom_id", "chapter_number", "chapter_title", "content_role", "verse_label",
    "exact_text", "pdf_pages", "citation", "previous_atom_id", "next_atom_id",
    "context_before", "context_after", "suspected_annotations", "content_missing",
)
# 一组的目标条数：太大 agent 抽不完，太小则跨组重复断语的风险上升。
TARGET_PER_GROUP = 12


def load_atoms() -> dict[str, dict]:
    atoms = {}
    for line in ATOMS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            atom = json.loads(line)
            atoms[atom["evidence_atom_id"]] = atom
    return atoms


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_label", nargs="?")
    parser.add_argument("--groups", type=int, help="强制分成几组；默认按每组约 12 条自动定")
    parser.add_argument("--list", action="store_true", help="列出全部批次标签")
    args = parser.parse_args()

    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    if args.list or not args.batch_label:
        for batch in plan:
            flag = "高风险" if batch["high_risk"] else "     "
            print(f"{batch['batch_label']:<14}{flag}  {batch['atom_count']:>4} 条  {batch['topic']}")
        print(f"\n共 {len(plan)} 批。用法：python distillation/export_batch.py <批次标签>")
        return 0

    batch = next((item for item in plan if item["batch_label"] == args.batch_label), None)
    if batch is None:
        print(json.dumps({"passed": False, "errors": [f"批次计划里没有：{args.batch_label}"]}, ensure_ascii=False))
        return 1

    atoms = load_atoms()
    missing = [atom_id for atom_id in batch["evidence_atom_ids"] if atom_id not in atoms]
    if missing:
        print(json.dumps({"passed": False, "errors": [f"批次引用了不存在的原子：{missing[:5]}"]}, ensure_ascii=False))
        return 1
    selected = [atoms[atom_id] for atom_id in batch["evidence_atom_ids"]]

    group_count = args.groups or max(1, -(-len(selected) // TARGET_PER_GROUP))
    size = -(-len(selected) // group_count)
    blocks = [selected[i:i + size] for i in range(0, len(selected), size)]

    out = OUT_ROOT / batch["batch_label"]
    (out / "groups").mkdir(parents=True, exist_ok=True)
    (out / "fragments").mkdir(parents=True, exist_ok=True)
    group_files = []
    for index, block in enumerate(blocks, 1):
        slim = [{key: atom.get(key) for key in KEEP_FIELDS} for atom in block]
        path = out / "groups" / f"g{index}.json"
        path.write_text(json.dumps(slim, ensure_ascii=False, indent=2), encoding="utf-8")
        group_files.append({
            "group": f"g{index}",
            "path": str(path),
            "atoms": len(block),
            "chars": sum(len(atom["exact_text"]) for atom in block),
            "first": block[0]["evidence_atom_id"],
            "last": block[-1]["evidence_atom_id"],
        })
    (out / "scope.json").write_text(
        json.dumps(batch["evidence_atom_ids"], ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # 章名必须取自原子自带的 chapter_title：计划表里的主题是按目录范围粗分的，
    # 手写具体章名会错位（实测 ch17 是 Ari 六宫、不是七宫），抽取窗口会拿到错的章号。
    chapter_titles = {}
    for atom in selected:
        chapter_titles.setdefault(atom["chapter_number"], atom["chapter_title"])
    topic_line = "；".join(
        f"第{num}章 {title}" for num, title in sorted(chapter_titles.items())
    )
    print(json.dumps({
        "passed": True,
        "batch_label": batch["batch_label"],
        "chapters": batch["chapters"],
        "topic": batch["topic"],
        "topic_from_atoms": topic_line,
        "chapter_titles": {str(k): v for k, v in sorted(chapter_titles.items())},
        "high_risk": batch["high_risk"],
        "atom_count": batch["atom_count"],
        "groups": group_files,
        "scope_file": str(out / "scope.json"),
        "fragments_dir": str(out / "fragments"),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
