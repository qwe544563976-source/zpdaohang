#!/usr/bin/env python3
"""为整本书批量准备下一批（或下几批）的输入：导出分组、派生批次编号与主题。

输出可直接作为 extract_workflow.js 的 args.batches——**组状态由本程序从目录实况
生成，不许手写**。真实教训（2026-08-21 两连踩）：工单手写"g1 已抽完只补 g2"，
目录实况正好相反，一批装配白跑、一批 agent 靠自己看目录才没被带偏。
凡手写状态必然出错，和"手写章名错位一章"同病。

用法：
    python distillation/prepare_batches.py --next 3        # 取接下来未完成的 3 批
    python distillation/prepare_batches.py ch19-20 ch21-22
    python distillation/prepare_batches.py --status
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLAN = REPO / "distillation" / "BATCH_PLAN.json"
BATCH_ROOT = REPO / "distillation" / "bphs-97" / "batches"
LOCAL_BATCHES = REPO / "distillation" / "_local" / "batches"
ATOMS = REPO / "distillation" / "_local" / "evidence_atoms.jsonl"
RUN_DATE = "20260821"


def load_chapter_titles() -> dict[int, str]:
    titles: dict[int, str] = {}
    for line in ATOMS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            atom = json.loads(line)
            titles.setdefault(atom["chapter_number"], atom["chapter_title"])
    return titles


def slugify(text: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")


def done_labels() -> set[str]:
    """已经装配出批次目录的批次标签（目录名里带 _<label>_）。"""
    done = set()
    if BATCH_ROOT.is_dir():
        for path in BATCH_ROOT.iterdir():
            parts = path.name.split("_")
            if len(parts) > 1:
                done.add(parts[1])
    return done


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("labels", nargs="*")
    parser.add_argument("--next", type=int, help="自动取计划表里接下来未开工的 N 批")
    parser.add_argument("--groups", type=int, help="强制每批分几组")
    parser.add_argument("--status", action="store_true", help="只看全书进度")
    args = parser.parse_args()

    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    finished = done_labels()

    if args.status:
        total = sum(item["atom_count"] for item in plan)
        done_atoms = sum(item["atom_count"] for item in plan if item["batch_label"] in finished)
        print(json.dumps({
            "batches_total": len(plan),
            "batches_done": len([i for i in plan if i["batch_label"] in finished]),
            "atoms_total": total,
            "atoms_done": done_atoms,
            "percent": round(done_atoms / total * 100, 1),
            "next": [i["batch_label"] for i in plan if i["batch_label"] not in finished][:6],
        }, ensure_ascii=False, indent=2))
        return 0

    if args.next:
        labels = [i["batch_label"] for i in plan if i["batch_label"] not in finished][:args.next]
    else:
        labels = args.labels
    if not labels:
        print(json.dumps({"passed": False, "errors": ["没有要准备的批次"]}, ensure_ascii=False))
        return 1

    titles = load_chapter_titles()
    prepared = []
    for label in labels:
        batch = next((i for i in plan if i["batch_label"] == label), None)
        if batch is None:
            print(json.dumps({"passed": False, "errors": [f"计划表里没有：{label}"]}, ensure_ascii=False))
            return 1

        command = [sys.executable, str(REPO / "distillation" / "export_batch.py"), label]
        if args.groups:
            command += ["--groups", str(args.groups)]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", cwd=REPO)
        if result.returncode != 0:
            print(result.stdout or result.stderr)
            return 1
        exported = json.loads(result.stdout)

        # 批次编号里的主题串一律由原子自带章名派生；手写章名已经错位过一次。
        chapters = sorted(exported["chapter_titles"], key=int)
        slug = "-".join(slugify(chapter_term(titles[int(n)])) for n in chapters)[:60].strip("-")
        groups = [g["group"] for g in exported["groups"]]
        # 组状态：机器看目录，谁也不许手写
        fragments_dir = LOCAL_BATCHES / label / "fragments"
        have = sorted(f.stem for f in fragments_dir.glob("*.json")) if fragments_dir.is_dir() else []
        missing = [g for g in groups if g not in have]
        note = (
            f"目录实况（机器生成，勿手写勿转述记忆）：已有片段 {'、'.join(have) or '无'}；"
            f"缺 {'、'.join(missing) or '无'}。已存在的组文件跳过不动，只补缺的组。"
        )
        prepared.append({
            "label": label,
            "batch_id": f"BPHS97_{label}_{slug}_{RUN_DATE}_run01",
            "groups": groups,
            "topic": exported["topic_from_atoms"],
            "note": note,
            "atoms": exported["atom_count"],
            "high_risk": exported["high_risk"],
            "fully_extracted": not missing and bool(have),
        })

    print(json.dumps({"passed": True, "batches": prepared}, ensure_ascii=False, indent=2))
    return 0


TITLE_PREFIXES = (
    "Effects of the ", "Effects of ", "Remedies from the ", "Remedies from ",
    "Remedies for ", "Combinations for ", "Evaluation of the ", "Evaluation Of ",
    "Evaluation of ", "Determination of ", "Working out of ", "Judgement of ",
)


def chapter_term(title: str) -> str:
    for prefix in TITLE_PREFIXES:
        if title.lower().startswith(prefix.lower()):
            return title[len(prefix):].strip(" .")
    return title.strip(" .")


if __name__ == "__main__":
    raise SystemExit(main())
