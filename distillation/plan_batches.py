#!/usr/bin/env python3
"""全书批次规划：把 2024 条原子切成可执行的生产批次。

规则来自必读卡：
- 一批 = 一个专题或一组直接依赖专题，40~120 个审查步骤为宜；
- 不得按单条原文拆批；专题本身太小就与相邻专题合并；
- 大运流年、多星同聚、复杂瑜伽永远全审，单独成批不与简单落宫混装；
- 章内原文不跨批打散（除非一章本身超过上限，此时按偈号顺序切块）。

步骤数无法在生产前精确知道，用实测比例估算：
第一批（ch14~16，41 条原子）实际产出 ~2 步/条，故以"条数 × 2"估步数。

用法：
    python distillation/plan_batches.py                 # 打印计划摘要
    python distillation/plan_batches.py --json out.json # 导出机器可读计划
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ATOMS = REPO / "distillation" / "_local" / "evidence_atoms.jsonl"

STEPS_PER_ATOM = 2.0
MIN_STEPS, MAX_STEPS = 40, 120
MIN_ATOMS = int(MIN_STEPS / STEPS_PER_ATOM)   # 20
MAX_ATOMS = int(MAX_STEPS / STEPS_PER_ATOM)   # 60

# 需要强制全审、且不与简单落宫章节混装的高风险区。
# 章号依据 BPHS 97 章版目录：45 行星状态、46~65 运期体系、66~72 八分法。
HIGH_RISK_CHAPTERS = set(range(43, 46)) | set(range(46, 66)) | set(range(66, 73))

TOPIC_HINTS = {
    (1, 10): "基础：创世、行星、星座、分盘、相位",
    (11, 11): "判断入口：各宫应看何事",
    (12, 24): "十二宫效果与宫主效果",
    (25, 33): "行星与宫主的组合效果",
    (34, 42): "功能吉凶、瑜伽组合、财富与贫困",
    (43, 45): "寿命与行星状态",
    (46, 65): "运期体系与运期效果",
    (66, 72): "八分法量化",
    (73, 83): "其他专题",
    (84, 97): "化解方法与全书总结",
}


def topic_for(chapter: int) -> str:
    for (low, high), label in TOPIC_HINTS.items():
        if low <= chapter <= high:
            return label
    return "未分类"


def load() -> dict[int, list[dict]]:
    chapters: dict[int, list[dict]] = {}
    for line in ATOMS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            atom = json.loads(line)
            chapters.setdefault(atom["chapter_number"], []).append(atom)
    for atoms in chapters.values():
        atoms.sort(key=lambda item: item.get("chapter_position", 0))
    return chapters


def chunk_chapter(atoms: list[dict]) -> list[list[dict]]:
    """一章超过上限时按偈号顺序切块，尽量均分而不是切出一个零头。"""
    if len(atoms) <= MAX_ATOMS:
        return [atoms]
    parts = -(-len(atoms) // MAX_ATOMS)
    size = -(-len(atoms) // parts)
    return [atoms[i:i + size] for i in range(0, len(atoms), size)]


def plan() -> list[dict]:
    chapters = load()
    batches: list[dict] = []
    pending: list[dict] = []
    pending_chapters: list[int] = []

    def flush() -> None:
        nonlocal pending, pending_chapters
        if pending:
            batches.append(make_batch(pending, pending_chapters))
            pending, pending_chapters = [], []

    def make_batch(atoms: list[dict], chapter_numbers: list[int], part: tuple[int, int] | None = None) -> dict:
        low, high = min(chapter_numbers), max(chapter_numbers)
        high_risk = any(ch in HIGH_RISK_CHAPTERS for ch in chapter_numbers)
        label = f"ch{low:02d}" if low == high else f"ch{low:02d}-{high:02d}"
        # 一章切成多块时必须带块号：批次编号是合并总账时的唯一键，重名会撞车。
        if part:
            label = f"{label}-p{part[0]}of{part[1]}"
        return {
            "batch_label": label,
            "chapters": sorted(set(chapter_numbers)),
            "topic": topic_for(low),
            "atom_count": len(atoms),
            "estimated_steps": int(len(atoms) * STEPS_PER_ATOM),
            "review_mode": "full",
            "high_risk": high_risk,
            "reason": "高风险区（寿命/运期/八分法）强制全审且不与落宫章混装" if high_risk
                      else "结构较单一，仍按新工具首批规则全审",
            "evidence_atom_ids": [atom["evidence_atom_id"] for atom in atoms],
        }

    for chapter in sorted(chapters):
        atoms = chapters[chapter]
        high_risk = chapter in HIGH_RISK_CHAPTERS
        # 高风险章不与其他章混装：先把攒着的放出去
        if high_risk or len(atoms) > MAX_ATOMS:
            flush()
            blocks = chunk_chapter(atoms)
            for index, block in enumerate(blocks, 1):
                part = (index, len(blocks)) if len(blocks) > 1 else None
                batches.append(make_batch(block, [chapter], part))
            continue
        # 攒够下限就出一批；攒到上限也出
        if pending and len(pending) + len(atoms) > MAX_ATOMS:
            flush()
        pending.extend(atoms)
        pending_chapters.append(chapter)
        if len(pending) >= MIN_ATOMS:
            flush()
    flush()
    return batches


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, help="导出机器可读计划")
    args = parser.parse_args()
    batches = plan()
    total_atoms = sum(b["atom_count"] for b in batches)
    total_steps = sum(b["estimated_steps"] for b in batches)

    print(f"全书 {total_atoms} 条原子 → {len(batches)} 批，预计 {total_steps} 个审查步骤\n")
    print(f"{'批次':<12}{'章节':<14}{'条数':>5}{'预计步数':>9}  {'高风险':<7}主题")
    print("-" * 96)
    for batch in batches:
        chapters = ",".join(str(c) for c in batch["chapters"])
        if len(chapters) > 12:
            chapters = chapters[:11] + "…"
        print(f"{batch['batch_label']:<12}{chapters:<14}{batch['atom_count']:>5}"
              f"{batch['estimated_steps']:>9}  {'是' if batch['high_risk'] else '否':<7}{batch['topic']}")
    print("-" * 96)
    oversized = [b for b in batches if b["estimated_steps"] > MAX_STEPS]
    undersized = [b for b in batches if b["estimated_steps"] < MIN_STEPS]
    print(f"超上限批次：{len(oversized)}  低于下限批次：{len(undersized)}（末批或单章不足时允许）")
    if args.json:
        args.json.write_text(json.dumps(batches, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"已导出：{args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
