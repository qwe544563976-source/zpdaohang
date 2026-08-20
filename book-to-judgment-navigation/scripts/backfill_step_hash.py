#!/usr/bin/env python3
"""一次性回填脚本（拆网定案·四·5）：给已并入总账的方法补 step_hash。

只做三件纯计算的事，不改任何经文内容、原文编号、页码或引用：
1. 每个方法步骤按当前内容计算并写入 step_hash（已正确的跳过）；
2. 方法缺 spine_slot_hint 时补 null（Q17 留插座，不猜值）；
3. generation.generator 从退役地址 cangjie-skill/scripts/build_methods.py
   更新为本技能地址（Q19 搬家后的身份，同一生成器）。

幂等：重复运行不再产生任何变化。写入前先做时间戳备份。
用法：
    python scripts/backfill_step_hash.py <method-recipes.json 路径>          # 回填
    python scripts/backfill_step_hash.py <method-recipes.json 路径> --check  # 只检查不写
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

_SHARED_SPEC = importlib.util.spec_from_file_location(
    "b2jn_shared_constants", Path(__file__).resolve().with_name("shared_constants.py")
)
assert _SHARED_SPEC and _SHARED_SPEC.loader
shared_constants = importlib.util.module_from_spec(_SHARED_SPEC)
_SHARED_SPEC.loader.exec_module(shared_constants)

RETIRED_GENERATOR_ID = "cangjie-skill/scripts/build_methods.py"


def backfill(data: dict) -> dict:
    counts = {
        "methods": 0,
        "steps_backfilled": 0,
        "steps_already_correct": 0,
        "spine_slot_hints_added": 0,
        "generator_updated": False,
    }
    generation = data.get("generation")
    if isinstance(generation, dict) and generation.get("generator") == RETIRED_GENERATOR_ID:
        generation["generator"] = shared_constants.GENERATOR_ID
        counts["generator_updated"] = True
    for method in data.get("methods", []):
        if not isinstance(method, dict):
            continue
        counts["methods"] += 1
        if "spine_slot_hint" not in method:
            method["spine_slot_hint"] = None
            counts["spine_slot_hints_added"] += 1
        for step in method.get("steps", []):
            if not isinstance(step, dict):
                continue
            expected = shared_constants.compute_step_hash(step)
            if step.get("step_hash") == expected:
                counts["steps_already_correct"] += 1
            else:
                step["step_hash"] = expected
                counts["steps_backfilled"] += 1
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description="给已并入的方法配方一次性回填 step_hash")
    parser.add_argument("recipes", type=Path, help="method-recipes.json 路径（总账或批次）")
    parser.add_argument("--check", action="store_true", help="只检查并输出报告，不写文件")
    args = parser.parse_args()
    path = args.recipes.resolve()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("methods"), list):
            raise ValueError("不是方法配方文件：缺少 methods 数组")
        counts = backfill(data)
        changed = bool(
            counts["steps_backfilled"] or counts["spine_slot_hints_added"] or counts["generator_updated"]
        )
        if changed and not args.check:
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
            backup = path.with_name(f"{path.name}.{stamp}.before-step-hash-backfill")
            shutil.copy2(path, backup)
            path.write_text(
                json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
            counts["backup"] = str(backup)
        counts["passed"] = True
        counts["changed"] = changed
        counts["written"] = changed and not args.check
        print(json.dumps(counts, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"passed": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
