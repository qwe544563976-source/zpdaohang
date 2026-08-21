#!/usr/bin/env python3
"""译名漂移检查：同一个英文术语在本批被译成了几个中文词？

补的是 `审计有效性对照表.md` 第五节记的第一个机器闸门盲区。
第 1 批实测：`exalted` 被译成「入旺」8 次、「入庙旺」3 次，`trine` 37 次「三角宫」
夹 1 次「三分宫」——而「三分盘」正是同批 Decanate/D3 的译名，只差一个字。
这类漂移一条条看方法看不出来，必须全批统计才现形，正好是机器该干的活。

判据：只盯「译错等于换一张盘、换一种状态」的词。不做全批译名统一
（那一版拿真实批次跑出过几十条假阳性：同一个 yuti 在不同句子里本来就该有不同说法）。

用法：
    python distillation/check_term_drift.py <批次目录>
    python distillation/check_term_drift.py <批次目录> --json
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

# 英文词 → 该词在本书里可能出现的中文译法。同一个英文词命中两种以上就告警。
# 每组里的词必须是**真正互斥**的译法，不是近义词，否则又会变成假阳性机器。
WATCHED_TERMS: dict[str, tuple[str, ...]] = {
    r"exalted|exaltation": ("入旺", "入庙", "庙旺"),
    r"debilitat": ("入陷", "落陷", "失势"),
    r"\btrine|trinal": ("三角宫", "三分宫", "拱宫"),
    r"decanate|drekkana": ("三分盘", "十分盘", "十度盘"),
    r"nav[aā][mń][sś]": ("九分盘", "九分宫"),
    r"dasamsa|dashamsa": ("十分盘", "十度盘"),
    r"\bmalefic": ("凶星", "恶星", "煞星"),
    r"\bbenefic": ("吉星", "善星"),
}


def chinese_text(step: dict) -> str:
    return " ".join([
        step.get("minimum_supported_claim", ""),
        step.get("action", ""),
        json.dumps(step.get("claim_terms", {}), ensure_ascii=False),
    ])


def scan(recipes: dict) -> dict:
    counts: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    where: dict[str, dict[str, list[str]]] = collections.defaultdict(lambda: collections.defaultdict(list))
    for method in recipes.get("methods", []):
        for step in method.get("steps", []):
            source = " ".join(ref.get("quote", "") for ref in step.get("evidence_refs", []))
            target = chinese_text(step)
            for pattern, renderings in WATCHED_TERMS.items():
                if not re.search(pattern, source, re.I):
                    continue
                for rendering in renderings:
                    if rendering in target:
                        counts[pattern][rendering] += 1
                        where[pattern][rendering].append(step["step_id"])
    drifts = []
    for pattern, counter in counts.items():
        if len(counter) > 1:
            ranked = counter.most_common()
            minority = ranked[1:]
            drifts.append({
                "term": pattern,
                "renderings": dict(ranked),
                # 少数派最可能是漂移的那一个，先让人看它
                "suspect_steps": [sid for rendering, _ in minority for sid in where[pattern][rendering]],
            })
    return {
        "passed": not drifts,
        "checked_terms": len(counts),
        "renderings": {p: dict(c) for p, c in sorted(counts.items())},
        "drifts": drifts,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    path = args.target / "references" / "navigation" / "method-recipes.json"
    report = scan(json.loads(path.read_text(encoding="utf-8")))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"本批命中 {report['checked_terms']} 个受控术语")
        for pattern, renderings in report["renderings"].items():
            flag = "  ← 同词异译" if len(renderings) > 1 else ""
            print(f"  {pattern:<24}{renderings}{flag}")
        for drift in report["drifts"]:
            print(f"\n[漂移] {drift['term']} 有 {len(drift['renderings'])} 种译法，先看少数派这些步骤：")
            for step_id in drift["suspect_steps"]:
                print(f"    {step_id}")
        if report["passed"]:
            print("\n译名一致：每个受控术语在本批只有一种译法。")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
