#!/usr/bin/env python3
"""路标演示：拿一句用户问题，走一遍判断导航，看它给出什么。

演示的是"路标"本身，不是答案：
匹配主题 → 列出必查命盘事实 → 给出四路查书计划 → 因为 JH8 事实未接通而停判。
停判正是设计要的结果——没有真实命盘事实时，系统必须说缺什么，不许猜。

用法：
    python distillation/demo_navigation.py "我会有几个孩子"
    python distillation/demo_navigation.py --list          # 看这批覆盖了哪些问法
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = REPO / "distillation" / "bphs-97" / "batches" / "BPHS97_ch14-16_siblings-home-children_20260820_run01"


def tokenize(text: str) -> set[str]:
    """粗切词：中文按字，英文按单词。演示用，正式匹配由 RAG 负责。"""
    words = set(re.findall(r"[a-zA-Z]+", text.lower()))
    words.update(ch for ch in text if "一" <= ch <= "鿿")
    return words


def score(question: str, topic: dict) -> int:
    asked = tokenize(question)
    best = 0
    for intent in topic.get("user_intents", []):
        best = max(best, len(asked & tokenize(intent)))
    return best


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("question", nargs="?", default="我会有几个孩子")
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--list", action="store_true", help="列出本批覆盖的全部用户问法")
    parser.add_argument("--top", type=int, default=2, help="展示前几个最相关主题")
    args = parser.parse_args()

    queries = json.loads((args.batch / "references" / "navigation" / "query-recipes.json").read_text(encoding="utf-8"))
    recipes = json.loads((args.batch / "references" / "navigation" / "method-recipes.json").read_text(encoding="utf-8"))
    methods = {item["method"]: item for item in recipes.get("methods", [])}
    topics = queries.get("topics", {})

    if args.list:
        for name, topic in topics.items():
            print(f"\n[{name}] {topic.get('title')}")
            for intent in topic.get("user_intents", []):
                print(f"   · {intent}")
        print(f"\n共 {len(topics)} 个主题。范围外的问题本批没有方法，必须回答“暂无已发布方法”。")
        return 0

    ranked = sorted(topics.items(), key=lambda item: score(args.question, item[1]), reverse=True)
    hits = [(name, topic) for name, topic in ranked if score(args.question, topic) > 0][: args.top]

    print(f"用户问题：{args.question}\n")
    if not hits:
        print("没有匹配到本批任何主题。")
        print("正确反应：回答“这一题目前没有已发布方法”，不许拿别的主题硬套。")
        return 0

    for name, topic in hits:
        print("=" * 72)
        print(f"命中主题：{topic.get('title')}  [{name}]")
        print(f"  用户问法：{'、'.join(topic.get('user_intents', []))}")
        print(f"\n  必查命盘事实（缺一即停）：")
        for fact in topic.get("required_facts", []):
            print(f"    · {fact}")
        for fact in topic.get("conditional_facts", []):
            print(f"    · （按分支）{fact}")
        print(f"\n  四路查书计划（交给 RAG）：")
        for lane, label in (
            ("support_queries", "支持路"),
            ("counter_queries", "反例路"),
            ("boundary_queries", "边界路"),
            ("method_queries", "方法路"),
        ):
            for query in topic.get(lane, []):
                print(f"    [{label}] {query}")

        for method_id in topic.get("candidate_method_ids", []) + topic.get("method_ids", []):
            method = methods.get(method_id)
            if not method:
                continue
            print(f"\n  方法 {method_id} 的执行步骤：")
            for index, step in enumerate(method.get("steps", []), 1):
                print(f"    {index}. {step.get('action')}")
                print(f"       原文最多支持到：{step.get('minimum_supported_claim')}")
                for evidence in step.get("evidence_refs", []):
                    print(f"       回指原文：{evidence['evidence_atom_id']}（PDF {evidence['pdf_pages']}）")
                    print(f"                 “{evidence['quote'][:90]}”")
                print(f"       停判：{step.get('stop_condition')}")

        print(f"\n  当前执行许可：execution_allowed={topic.get('execution_allowed')}"
              f"  排盘事实接入={topic.get('fact_binding_status')}")
        print("  → 停判输出：JH8 排盘事实尚未交付，本主题只能给出查书计划，不得给用户下结论。")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
