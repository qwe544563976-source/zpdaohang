import importlib.util
import os
import unittest
from datetime import date
from pathlib import Path


SCRIPT = Path(__file__).with_name("adapt_jh8_facts.py")
JH8_CHART = Path(
    os.environ.get(
        "JUDGMENT_NAV_JH8_CHART",
        "F:/JH8-Full-20260816-FactsGate-Handoff/runs/LML_true_lahiri",
    )
)
SPEC = importlib.util.spec_from_file_location("adapt_jh8_facts", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class FactGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.method = {
            "method": "demo-method",
            "required_facts": ["已提供事实", "布尔值为假", "空数组"],
            "conditional_facts": ["可选事实"],
            "fact_binding_status": "mapped",
            "executable_in_pilot": True,
            "upstream_issue_ids": [],
            "dependencies": [],
        }

    def test_positive_complete_facts_open_request(self) -> None:
        facts = {
            "已提供事实": MODULE.record("available", "有值"),
            "布尔值为假": MODULE.record("available", False),
            "空数组": MODULE.record("available", []),
            "可选事实": MODULE.record("unavailable", reason="未触发该条件"),
        }
        gate = MODULE.build_method_gate(self.method, facts, {"demo-method": self.method})
        self.assertTrue(gate["allowed"])
        self.assertEqual(gate["blocking_facts"], [])
        self.assertIsNotNone(MODULE.build_judgment_request("demo-method", facts, gate))

    def test_known_bad_missing_fact_closes_gate(self) -> None:
        facts = {
            "已提供事实": MODULE.record("available", "有值"),
            "布尔值为假": MODULE.record("available", False),
            "空数组": MODULE.record("unavailable", reason="故意抽掉"),
        }
        gate = MODULE.build_method_gate(self.method, facts, {"demo-method": self.method})
        self.assertFalse(gate["allowed"])
        self.assertEqual(gate["blocking_facts"][0]["fact"], "空数组")
        self.assertIsNone(MODULE.build_judgment_request("demo-method", facts, gate))

    def test_caller_required_is_unknown_not_false(self) -> None:
        facts = {
            "已提供事实": MODULE.record("available", "有值"),
            "布尔值为假": MODULE.record("caller_required", reason="等待用户问题分类"),
            "空数组": MODULE.record("available", []),
        }
        gate = MODULE.build_method_gate(self.method, facts, {"demo-method": self.method})
        self.assertFalse(gate["allowed"])
        self.assertEqual(gate["blocking_facts"][0]["fact_state"], "unknown")

    def test_blank_baseline_closes_gate_and_reports_all_missing(self) -> None:
        gate = MODULE.build_method_gate(self.method, {}, {"demo-method": self.method})
        self.assertFalse(gate["allowed"])
        self.assertEqual(
            {item["fact"] for item in gate["blocking_facts"]},
            {"已提供事实", "布尔值为假", "空数组"},
        )

    def test_stop_output_contains_no_judgment(self) -> None:
        facts = {"已提供事实": MODULE.record("available", "有值")}
        gate = MODULE.build_method_gate(self.method, facts, {"demo-method": self.method})
        output = MODULE.build_stop_output(facts, gate)
        self.assertTrue(output["missing_key_facts"])
        self.assertIn("不得判断吉凶", output["prohibited_conclusions"])
        self.assertNotIn("判断请求", output)

    def _dual_lord_method(self) -> dict:
        return {
            **self.method,
            "required_facts": ["目标宫主是否主管两个宫位"],
            "conditional_facts": ["双重宫主两项原文证据"],
            "steps": [
                {
                    "conditional_fact_requirements": [
                        {
                            "when": {"fact_key": "目标宫主是否主管两个宫位"},
                            "required_fact_keys": ["双重宫主两项原文证据"],
                            "stop_condition": "缺少两项原文证据就停。",
                        }
                    ]
                }
            ],
        }

    def _selection_group_method(self) -> dict:
        return {
            **self.method,
            "method": "selection-group-method",
            "required_facts": ["前置条件"],
            "conditional_facts": ["分支A事实", "分支B事实"],
            "steps": [
                {
                    "conditional_fact_requirements": [
                        {
                            "when": {"fact_key": "前置条件"},
                            "required_fact_keys": ["分支A事实"],
                            "selection_group": "fixture:multi_match",
                            "branch_condition_logic": {"fact_key": "分支A事实"},
                            "stop_condition": "分支 A 命中但缺事实时停止。",
                        },
                        {
                            "when": {"fact_key": "前置条件"},
                            "required_fact_keys": ["分支B事实"],
                            "selection_group": "fixture:multi_match",
                            "branch_condition_logic": {"fact_key": "分支B事实"},
                            "stop_condition": "分支 B 命中但缺事实时停止。",
                        },
                    ]
                }
            ],
        }

    def _selection_group_gate(self, a: dict, b: dict) -> dict:
        method = self._selection_group_method()
        facts = {
            "前置条件": MODULE.record("available", True),
            "分支A事实": a,
            "分支B事实": b,
        }
        return MODULE.build_method_gate(
            method, facts, {method["method"]: method}
        )

    def _crossed_selection_group_method(self) -> dict:
        return {
            **self.method,
            "method": "crossed-selection-group-method",
            "required_facts": ["前置A", "前置B"],
            "conditional_facts": ["选择A", "选择B", "分支A事实", "分支B事实"],
            "steps": [
                {
                    "conditional_fact_requirements": [
                        {
                            "when": {"fact_key": "前置A"},
                            "required_fact_keys": ["分支A事实"],
                            "selection_group": "fixture:crossed",
                            "branch_condition_logic": {"fact_key": "选择A"},
                            "stop_condition": "分支 A 命中但缺事实时停止。",
                        },
                        {
                            "when": {"fact_key": "前置B"},
                            "required_fact_keys": ["分支B事实"],
                            "selection_group": "fixture:crossed",
                            "branch_condition_logic": {"fact_key": "选择B"},
                            "stop_condition": "分支 B 命中但缺事实时停止。",
                        },
                    ]
                }
            ],
        }

    def test_selection_group_only_a_active_allows_with_b_unavailable(self) -> None:
        gate = self._selection_group_gate(
            MODULE.record("available", True),
            MODULE.record("unavailable", reason="未命中分支 A"),
        )
        self.assertTrue(gate["allowed"])

    def test_selection_group_only_b_active_allows_with_a_unavailable(self) -> None:
        gate = self._selection_group_gate(
            MODULE.record("unavailable", reason="未命中分支 B"),
            MODULE.record("available", True),
        )
        self.assertTrue(gate["allowed"])

    def test_selection_group_allows_both_branches_active(self) -> None:
        gate = self._selection_group_gate(
            MODULE.record("available", True),
            MODULE.record("available", True),
        )
        self.assertTrue(gate["allowed"])

    def test_selection_group_stops_when_all_branches_false(self) -> None:
        gate = self._selection_group_gate(
            MODULE.record("available", False),
            MODULE.record("available", False),
        )
        self.assertFalse(gate["allowed"])
        self.assertTrue(
            any(item["fact"] == "<selection_group:fixture:multi_match>" for item in gate["blocking_facts"])
        )

    def test_selection_group_crossed_when_and_logic_stops(self) -> None:
        method = self._crossed_selection_group_method()
        facts = {
            "前置A": MODULE.record("available", True),
            "前置B": MODULE.record("available", False),
            "选择A": MODULE.record("available", False),
            "选择B": MODULE.record("available", True),
            "分支A事实": MODULE.record("unavailable", reason="未命中分支 A"),
            "分支B事实": MODULE.record("available", True),
        }
        gate = MODULE.build_method_gate(method, facts, {method["method"]: method})
        self.assertFalse(gate["allowed"])
        self.assertTrue(
            any(item["fact"] == "<selection_group:fixture:crossed>" for item in gate["blocking_facts"])
        )

    def test_single_lord_skips_dual_lord_evidence(self) -> None:
        method = self._dual_lord_method()
        facts = {
            "目标宫主是否主管两个宫位": MODULE.record("available", False),
            "双重宫主两项原文证据": MODULE.record(
                "method_or_rag_required", reason="等待原文"
            ),
        }
        gate = MODULE.build_method_gate(method, facts, {"demo-method": method})
        self.assertTrue(gate["allowed"])
        self.assertNotIn(
            "双重宫主两项原文证据",
            {item["fact"] for item in gate["blocking_facts"]},
        )

    def test_dual_lord_blocks_without_two_source_evidence(self) -> None:
        method = self._dual_lord_method()
        facts = {
            "目标宫主是否主管两个宫位": MODULE.record("available", True),
            "双重宫主两项原文证据": MODULE.record(
                "method_or_rag_required", reason="等待原文"
            ),
        }
        gate = MODULE.build_method_gate(method, facts, {"demo-method": method})
        self.assertFalse(gate["allowed"])
        blocker = next(
            item
            for item in gate["blocking_facts"]
            if item["fact"] == "双重宫主两项原文证据"
        )
        self.assertEqual(blocker["status"], "method_or_rag_required")

    def test_unknown_when_condition_stops(self) -> None:
        method = self._dual_lord_method()
        facts = {
            "目标宫主是否主管两个宫位": MODULE.record(
                "method_or_rag_required", reason="等待 JH8 宫主表"
            ),
            "双重宫主两项原文证据": MODULE.record(
                "method_or_rag_required", reason="等待原文"
            ),
        }
        gate = MODULE.build_method_gate(method, facts, {"demo-method": method})
        self.assertFalse(gate["allowed"])
        self.assertIn(
            "目标宫主是否主管两个宫位",
            {item["fact"] for item in gate["blocking_facts"]},
        )

    def test_shadbala_percent_does_not_create_bphs_strength_tier(self) -> None:
        method = {
            **self.method,
            "required_facts": ["目标宫主强弱档位（原书三档）"],
        }
        facts = {
            "目标宫主六力百分比": MODULE.record("available", 128.5),
            "目标宫主强弱档位（原书三档）": MODULE.record(
                "method_or_rag_required",
                reason="六力百分比没有原书三档阈值",
            ),
        }
        gate = MODULE.build_method_gate(method, facts, {"demo-method": method})
        self.assertFalse(gate["allowed"])
        self.assertEqual(
            gate["blocking_facts"][0]["fact"], "目标宫主强弱档位（原书三档）"
        )

    @unittest.skipUnless(
        JH8_CHART.is_dir(),
        "JH8 样例命盘目录不存在；设 JUDGMENT_NAV_JH8_CHART 指向样例包后运行",
    )
    def test_formal_jh8_emits_all_lordship_fact_key(self) -> None:
        result = MODULE.adapt(JH8_CHART, 7, date(2026, 8, 16))
        self.assertIn("目标宫主的全部宫主身份", result["facts"])
        self.assertNotIn("目标宫主的双重宫主身份", result["facts"])

    def test_declared_target_house_7_matches_cli_house_7(self) -> None:
        method = {**self.method, "target_house": 7}
        facts = {
            "已提供事实": MODULE.record("available", "有值"),
            "布尔值为假": MODULE.record("available", False),
            "空数组": MODULE.record("available", []),
        }
        gate = MODULE.build_method_gate(
            method, facts, {"demo-method": method}, target_house=7
        )
        self.assertTrue(gate["allowed"])
        self.assertNotIn(
            "target_house_mismatch",
            {item["type"] for item in gate["authorization_blockers"]},
        )

    def test_declared_target_house_7_rejects_cli_house_2(self) -> None:
        method = {**self.method, "target_house": 7}
        facts = {
            "已提供事实": MODULE.record("available", "有值"),
            "布尔值为假": MODULE.record("available", False),
            "空数组": MODULE.record("available", []),
        }
        gate = MODULE.build_method_gate(
            method, facts, {"demo-method": method}, target_house=2
        )
        self.assertFalse(gate["allowed"])
        blocker = next(
            item
            for item in gate["authorization_blockers"]
            if item["type"] == "target_house_mismatch"
        )
        self.assertIn("target_house=7", blocker["reason"])
        self.assertIn("target_house=2", blocker["reason"])


if __name__ == "__main__":
    unittest.main()
