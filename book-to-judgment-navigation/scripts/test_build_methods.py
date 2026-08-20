#!/usr/bin/env python3
"""Code-level regression tests for the only formal method generator."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("build_methods.py")
SPEC = importlib.util.spec_from_file_location("build_methods", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


ATOM_ID = "book:edition:ch1:v1"
CONTEXT_ID = "book:edition:ch1:v0"
ATOMS = {
    ATOM_ID: {
        "evidence_atom_id": ATOM_ID,
        "content_role": "verse",
        "exact_text": (
            "If Saturn is weak, loss occurs. Either branch A or branch B also causes loss. "
            "Even if a benefic is present, loss occurs. A mantra mitigates loss."
        ),
        "pdf_pages": [1],
    },
    CONTEXT_ID: {
        "evidence_atom_id": CONTEXT_ID,
        "content_role": "verse",
        "exact_text": "The following statement concerns Saturn.",
        "pdf_pages": [1],
    },
}


def extraction() -> dict:
    return {
        "schema_version": "judgment-method-extraction/v2",
        "batch": {
            "batch_id": "test-batch",
            "book_id": "book",
            "edition_id": "edition",
            "artifact_scope": "FORMAL",
            "pilot_only": False,
            "publishable": False,
            "book_strategy": "rule_book",
            "chapter_features": ["other"],
            "requested_review": "full",
            "consecutive_clean_batches": 0,
            "review_cycle_position": 1,
        },
        "source_scope": [CONTEXT_ID, ATOM_ID],
        "source_records": [
            {"evidence_atom_id": CONTEXT_ID, "semantic_class": "condition_result", "risk_flags": []},
            {"evidence_atom_id": ATOM_ID, "semantic_class": "condition_result", "risk_flags": []},
        ],
        "methods": [
            {
                "method": "saturn-loss",
                "title": "土星条件结果",
                "generalization_scope": "general_rule",
                "source_status": "single_explicit_source",
                "fact_binding_status": "unmapped",
                "upstream_issue_ids": [],
                "user_intents": ["核对土星条件"],
                "facts": [
                    {"key": "base", "availability": "always", "role": "context"},
                    {"key": "branch-a", "availability": "conditional", "role": "risk_condition"},
                    {"key": "branch-b", "availability": "conditional", "role": "risk_condition"},
                    {"key": "phase-start", "availability": "always", "role": "phase_condition"},
                    {"key": "remedy", "availability": "conditional", "role": "remedy_condition"},
                    {"key": "benefic-present", "availability": "conditional", "role": "evidence_condition"},
                ],
                "dependencies": [],
                "steps": [
                    {
                        "action": "核对土星条件与结果。",
                        "applicability_scope": "仅限本条原文。",
                        "minimum_supported_claim": "土星弱时会发生损失。",
                        "claim_terms": {
                            "conditions": [{"quote": "Saturn is weak", "claim": "土星弱"}],
                            "results": [{"quote": "loss occurs", "claim": "损失"}],
                        },
                        "time_scope": {"kind": "none", "label": "原文没有时间限定", "fact_keys": []},
                        "produced_fact_keys": ["saturn-loss-result"],
                        "required_fact_keys": ["base"],
                        "condition_logic": {"fact_key": "base"},
                        "conditional_requirements": [],
                        "alternative_groups": [],
                        "concession_conditions": [],
                        "context_reference": False,
                        "context_bindings": [],
                        "source_status": "single_explicit_source",
                        "evidence": [
                            {"evidence_atom_id": CONTEXT_ID, "quote": "The following statement concerns Saturn."},
                            {"evidence_atom_id": ATOM_ID, "quote": "If Saturn is weak, loss occurs."}
                        ],
                        "exception_relations": [],
                        "forbidden_extensions": ["不得扩大成终身结论。"],
                    }
                ],
                "retrieval_plan": {
                    "support_queries": ["土星弱"],
                    "counter_queries": ["取消条件"],
                    "boundary_queries": ["适用范围"],
                    "method_queries": ["判断顺序"],
                },
                "stop_conditions": ["缺少 base 时停止。"],
                "spine_slot_hint": None,
            }
        ],
    }


class GeneratorRuleTests(unittest.TestCase):
    def build(self, data: dict) -> dict:
        MODULE.validate_schema(data)
        return MODULE.assemble(data, ATOMS)[0]

    def assert_build_error(self, data: dict, text: str) -> None:
        MODULE.validate_schema(data)
        with self.assertRaisesRegex(MODULE.BuildError, text):
            MODULE.assemble(data, ATOMS)

    def test_or_positive_is_assembled_as_selection_group(self) -> None:
        data = extraction()
        step = data["methods"][0]["steps"][0]
        step["alternative_groups"] = [{
            "group_id": "primary",
            "branches": [
                {"branch_id": "a", "condition_logic": {"fact_key": "branch-a"}, "required_fact_keys": ["branch-a"]},
                {"branch_id": "b", "condition_logic": {"fact_key": "branch-b"}, "required_fact_keys": ["branch-b"]},
            ],
        }]
        output = self.build(data)
        groups = output["methods"][0]["steps"][0]["conditional_fact_requirements"]
        self.assertEqual({item["selection_group"] for item in groups}, {"saturn-loss.step-001:primary"})

    def test_or_negative_rejects_raw_or_in_main_logic(self) -> None:
        data = extraction()
        data["methods"][0]["steps"][0]["condition_logic"] = {
            "operator": "OR", "operands": [{"fact_key": "base"}, {"fact_key": "branch-a"}]
        }
        self.assert_build_error(data, "OR 必须写进 alternative_groups")

    def test_minimum_claim_positive_has_condition_and_result_pairs(self) -> None:
        output = self.build(extraction())
        self.assertEqual(output["methods"][0]["steps"][0]["minimum_supported_claim"], "土星弱时会发生损失。")

    def test_minimum_claim_negative_rejects_empty_template(self) -> None:
        data = extraction()
        step = data["methods"][0]["steps"][0]
        step["minimum_supported_claim"] = "按原文判断。"
        step["claim_terms"]["conditions"][0]["claim"] = "按原文"
        step["claim_terms"]["results"][0]["claim"] = "判断"
        self.assert_build_error(data, "空话模板")

    def test_placeholder_source_fact_is_rejected(self) -> None:
        data = extraction()
        method = data["methods"][0]
        method["facts"][0]["key"] = "source_condition_v21"
        step = method["steps"][0]
        step["required_fact_keys"] = ["source_condition_v21"]
        step["condition_logic"] = {"fact_key": "source_condition_v21"}
        self.assert_build_error(data, "占位事实")

    def test_placeholder_chinese_fact_is_rejected(self) -> None:
        data = extraction()
        method = data["methods"][0]
        method["facts"][0]["key"] = "原文事实已取得"
        step = method["steps"][0]
        step["required_fact_keys"] = ["原文事实已取得"]
        step["condition_logic"] = {"fact_key": "原文事实已取得"}
        self.assert_build_error(data, "占位事实")

    def test_target_house_positive_is_copied_to_recipe(self) -> None:
        data = extraction()
        data["methods"][0]["target_house"] = 7
        output = self.build(data)
        self.assertEqual(output["methods"][0]["target_house"], 7)

    def test_target_house_is_optional_and_not_invented(self) -> None:
        output = self.build(extraction())
        self.assertNotIn("target_house", output["methods"][0])

    def test_target_house_negative_rejects_non_integer_or_out_of_range(self) -> None:
        for value in (True, False, 0, 13, -1, 7.5, "7"):
            data = extraction()
            data["methods"][0]["target_house"] = value
            with self.subTest(value=value):
                with self.assertRaisesRegex(MODULE.BuildError, "不符合严格 Schema"):
                    MODULE.validate_schema(data)

    def test_phase_positive_requires_exact_phase_fact(self) -> None:
        data = extraction()
        step = data["methods"][0]["steps"][0]
        step["required_fact_keys"] = ["base", "phase-start"]
        step["condition_logic"] = {"operator": "AND", "operands": [{"fact_key": "base"}, {"fact_key": "phase-start"}]}
        step["time_scope"] = {"kind": "phase", "label": "仅限开始阶段", "fact_keys": ["phase-start"]}
        self.build(data)

    def test_phase_negative_rejects_unwired_phase_fact(self) -> None:
        data = extraction()
        step = data["methods"][0]["steps"][0]
        step["time_scope"] = {"kind": "phase", "label": "仅限开始阶段", "fact_keys": ["phase-start"]}
        self.assert_build_error(data, "阶段事实没有挂到对应条件分支")

    def test_remedy_positive_is_kept_in_mitigation_relation(self) -> None:
        data = extraction()
        data["methods"][0]["steps"][0]["exception_relations"] = [{
            "type": "mitigation", "evidence_atom_ids": [ATOM_ID], "condition_logic": {"fact_key": "remedy"}
        }]
        self.build(data)

    def test_remedy_negative_rejects_remedy_as_risk_condition(self) -> None:
        data = extraction()
        step = data["methods"][0]["steps"][0]
        step["required_fact_keys"] = ["base", "remedy"]
        step["condition_logic"] = {"operator": "AND", "operands": [{"fact_key": "base"}, {"fact_key": "remedy"}]}
        data["methods"][0]["facts"][4]["availability"] = "always"
        self.assert_build_error(data, "把补救事实混入了风险成立条件")

    def test_even_if_positive_is_separate_from_risk_gate(self) -> None:
        data = extraction()
        data["methods"][0]["steps"][0]["concession_conditions"] = [{"fact_key": "benefic-present"}]
        self.build(data)

    def test_even_if_negative_rejects_concession_as_required_gate(self) -> None:
        data = extraction()
        step = data["methods"][0]["steps"][0]
        step["concession_conditions"] = [{"fact_key": "benefic-present"}]
        step["required_fact_keys"] = ["base", "benefic-present"]
        step["condition_logic"] = {"operator": "AND", "operands": [{"fact_key": "base"}, {"fact_key": "benefic-present"}]}
        data["methods"][0]["facts"][5]["availability"] = "always"
        self.assert_build_error(data, "把 even if 让步条件写成了成立前提")

    def test_context_positive_binds_previous_atom(self) -> None:
        data = extraction()
        step = data["methods"][0]["steps"][0]
        step["context_reference"] = True
        step["context_bindings"] = [CONTEXT_ID]
        self.build(data)

    def test_context_negative_rejects_missing_binding(self) -> None:
        data = extraction()
        data["methods"][0]["steps"][0]["context_reference"] = True
        self.assert_build_error(data, "没有绑定前置原文")

    def test_dasha_batch_cannot_request_sampling(self) -> None:
        data = extraction()
        data["batch"].update({
            "chapter_features": ["dasha_or_transit"],
            "requested_review": "sample",
            "consecutive_clean_batches": 9,
        })
        report = MODULE.assemble(data, ATOMS)[1]
        self.assertEqual(report["review_mode"], "full")

    def test_simple_batch_sample_is_seeded_and_exactly_twenty_percent(self) -> None:
        data = extraction()
        data["batch"].update({
            "chapter_features": ["simple_house_placement"],
            "requested_review": "sample",
            "consecutive_clean_batches": 3,
            "review_cycle_position": 1,
        })
        first = MODULE.assemble(copy.deepcopy(data), ATOMS)[1]
        second = MODULE.assemble(copy.deepcopy(data), ATOMS)[1]
        self.assertEqual(first["review_mode"], "sample")
        self.assertEqual(first["audit_step_ids"], second["audit_step_ids"])

    def test_full_audit_step_ids_are_sorted(self) -> None:
        data = extraction()
        second = copy.deepcopy(data["methods"][0])
        second["method"] = "alpha-loss"
        second["title"] = "另一条土星条件结果"
        data["methods"].append(second)
        output, report = MODULE.assemble(data, ATOMS)
        self.assertEqual(report["audit_step_ids"], sorted(report["audit_step_ids"]))
        self.assertEqual(output["generation"]["audit_step_ids"], report["audit_step_ids"])

    def test_schema_rejects_unknown_ai_output_field(self) -> None:
        data = extraction()
        data["methods"][0]["steps"][0]["free_form_answer"] = "模型擅自输出的散文"
        with self.assertRaisesRegex(MODULE.BuildError, "不符合严格 Schema"):
            MODULE.validate_schema(data)

    def test_generator_derives_query_scan_and_mechanical_state(self) -> None:
        data = extraction()
        methods, report = MODULE.assemble(data, ATOMS)
        queries = MODULE.build_query_recipes(methods)
        scan = MODULE.build_source_scan(data, methods)
        state = MODULE.batch_state(data["batch"], report, "recipe-hash")
        self.assertEqual(set(queries["topics"]), {"saturn-loss"})
        self.assertFalse(scan["pilot_only"])
        self.assertTrue(all(item["disposition"] == "method_step" for item in scan["atom_dispositions"]))
        self.assertEqual(state["current_state"], "mechanical_testing")

    def test_source_scan_carries_batch_pilot_only_flag(self) -> None:
        data = extraction()
        data["batch"]["pilot_only"] = True
        methods, _ = MODULE.assemble(data, ATOMS)
        scan = MODULE.build_source_scan(data, methods)
        self.assertTrue(scan["pilot_only"])

    def test_cli_writes_all_v2_machine_outputs_once(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            atom_path = root / "evidence_atoms.jsonl"
            atom_text = "\n".join(json.dumps(item, ensure_ascii=False) for item in ATOMS.values()) + "\n"
            atom_path.write_text(atom_text, encoding="utf-8")
            package_path = root / "accepted-package.json"
            package_path.write_text(
                json.dumps(
                    {
                        "artifact_scope": "FORMAL",
                        "distillation_allowed": True,
                        "book": {"book_id": "book", "edition_id": "edition"},
                        "evidence_atoms": {
                            "path": str(atom_path),
                            "content_sha256": hashlib.sha256(atom_path.read_bytes()).hexdigest(),
                        },
                        "upstream_gates": {
                            "source_text_bidirectional": "pass",
                            "chunking_validation": "pass",
                            "accepted": "pass",
                        },
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            extraction_path = root / "extraction.json"
            extraction_path.write_text(json.dumps(extraction(), ensure_ascii=False), encoding="utf-8")
            output = root / "delivery/references/navigation/method-recipes.json"
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--extraction",
                    str(extraction_path),
                    "--accepted-package",
                    str(package_path),
                    "--output",
                    str(output),
                ],
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue(output.is_file())
            self.assertTrue(output.with_name("query-recipes.json").is_file())
            self.assertTrue((root / "delivery/validation/method-source-scan.json").is_file())
            state = json.loads((root / "delivery/validation/batch-state.json").read_text(encoding="utf-8"))
            self.assertEqual(state["current_state"], "mechanical_testing")


class StepHashTests(unittest.TestCase):
    def test_step_hash_is_computed_and_verifiable(self) -> None:
        output = MODULE.assemble(extraction(), ATOMS)[0]
        step = output["methods"][0]["steps"][0]
        self.assertEqual(step["step_hash"], MODULE.compute_step_hash(step))

    def test_step_hash_changes_only_for_changed_step(self) -> None:
        data = copy.deepcopy(extraction())
        first = MODULE.assemble(copy.deepcopy(data), ATOMS)[0]["methods"][0]["steps"][0]["step_hash"]
        data["methods"][0]["steps"][0]["action"] = "改写后的动作说明。"
        second = MODULE.assemble(data, ATOMS)[0]["methods"][0]["steps"][0]["step_hash"]
        self.assertNotEqual(first, second)

    def test_step_hash_is_stable_for_identical_content(self) -> None:
        first = MODULE.assemble(copy.deepcopy(extraction()), ATOMS)[0]
        second = MODULE.assemble(copy.deepcopy(extraction()), ATOMS)[0]
        self.assertEqual(
            first["methods"][0]["steps"][0]["step_hash"],
            second["methods"][0]["steps"][0]["step_hash"],
        )


class SpineSlotHintTests(unittest.TestCase):
    def test_spine_slot_hint_null_is_copied_to_recipe(self) -> None:
        output = MODULE.assemble(extraction(), ATOMS)[0]
        method = output["methods"][0]
        self.assertIn("spine_slot_hint", method)
        self.assertIsNone(method["spine_slot_hint"])

    def test_spine_slot_hint_non_null_is_rejected_by_schema(self) -> None:
        data = extraction()
        data["methods"][0]["spine_slot_hint"] = "guessed-slot"
        with self.assertRaisesRegex(MODULE.BuildError, "spine_slot_hint"):
            MODULE.validate_schema(data)


class HighRiskTermTests(unittest.TestCase):
    def test_unmapped_high_risk_number_is_rejected(self) -> None:
        data = extraction()
        step = data["methods"][0]["steps"][0]
        step["evidence"][1]["quote"] = "If Saturn is weak, loss occurs."
        ATOMS_LOCAL = copy.deepcopy(ATOMS)
        ATOMS_LOCAL[ATOM_ID]["exact_text"] = "If Saturn is weak in the 7th, loss occurs. " + ATOMS_LOCAL[ATOM_ID]["exact_text"]
        step["evidence"][1]["quote"] = "If Saturn is weak in the 7th, loss occurs."
        MODULE.validate_schema(data)
        with self.assertRaisesRegex(MODULE.BuildError, "未映射的高风险词"):
            MODULE.assemble(data, ATOMS_LOCAL)

    def test_mapped_high_risk_terms_pass_and_enter_report(self) -> None:
        data = extraction()
        step = data["methods"][0]["steps"][0]
        ATOMS_LOCAL = copy.deepcopy(ATOMS)
        ATOMS_LOCAL[ATOM_ID]["exact_text"] = "If Saturn is weak in the 7th, loss occurs. " + ATOMS_LOCAL[ATOM_ID]["exact_text"]
        step["evidence"][1]["quote"] = "If Saturn is weak in the 7th, loss occurs."
        step["claim_terms"]["conditions"].append({"quote": "in the 7th", "claim": "第7宫"})
        step["minimum_supported_claim"] = "土星弱、落在第7宫时会发生损失。"
        MODULE.validate_schema(data)
        output, report = MODULE.assemble(data, ATOMS_LOCAL)
        table = output["generation"]["high_risk_terms"]
        self.assertIn("saturn-loss.step-001", table)
        detected = {item["term"] for item in table["saturn-loss.step-001"]}
        self.assertIn("7th", detected)
        self.assertIn("saturn", detected)
        self.assertEqual(report["high_risk_terms"], table)

    def test_detection_ignores_diacritics_and_case(self) -> None:
        detected = {item["term"] for item in MODULE.detect_high_risk_terms("Śani in Dhana causes loss")}
        self.assertIn("dhana", detected)
        self.assertIn("sani", detected)


class NonMethodDispositionTests(unittest.TestCase):
    """书里确有没有判断规则的正文（章节过渡句、引言、收尾语）。

    真实样本：BPHS97 ch15 v1「三宫结果已述，现在听四宫」、ch14 v15「估量强弱之后再宣布结果」。
    不给它们一个合法去向，抽取员就只能把过渡句硬做成方法——97 章会累积上百条假方法。
    """

    def transition_extraction(self) -> dict:
        data = extraction()
        data["source_records"][0]["semantic_class"] = "foundational_knowledge"
        data["source_records"][0]["disposition"] = "knowledge_only"
        step = data["methods"][0]["steps"][0]
        step["evidence"] = [item for item in step["evidence"] if item["evidence_atom_id"] != CONTEXT_ID]
        return data

    def test_knowledge_only_atom_is_not_required_to_have_a_method(self) -> None:
        data = self.transition_extraction()
        MODULE.validate_schema(data)
        output, _report = MODULE.assemble(data, ATOMS)
        self.assertEqual(len(output["methods"]), 1)

    def test_knowledge_only_atom_is_recorded_with_no_method_ids(self) -> None:
        data = self.transition_extraction()
        MODULE.validate_schema(data)
        output, _ = MODULE.assemble(data, ATOMS)
        scan = MODULE.build_source_scan(data, output)
        row = next(item for item in scan["atom_dispositions"] if item["evidence_atom_id"] == CONTEXT_ID)
        self.assertEqual(row["disposition"], "knowledge_only")
        self.assertEqual(row["method_ids"], [])

    def test_knowledge_only_atom_must_not_be_cited_by_a_step(self) -> None:
        data = extraction()
        data["source_records"][0]["semantic_class"] = "foundational_knowledge"
        data["source_records"][0]["disposition"] = "knowledge_only"
        MODULE.validate_schema(data)
        with self.assertRaisesRegex(MODULE.BuildError, "非方法去向的原文却被方法步骤引用"):
            MODULE.assemble(data, ATOMS)

    def test_default_disposition_still_requires_every_atom_to_be_used(self) -> None:
        data = extraction()
        step = data["methods"][0]["steps"][0]
        step["evidence"] = [item for item in step["evidence"] if item["evidence_atom_id"] != CONTEXT_ID]
        MODULE.validate_schema(data)
        with self.assertRaisesRegex(MODULE.BuildError, "没有进入任何方法步骤"):
            MODULE.assemble(data, ATOMS)


class RealBphsTermCoverageTests(unittest.TestCase):
    """真实 BPHS 97（Santhanam）原文驱动的高风险词回归。

    每条样本都来自正式书包 ch14~16 的 exact_text；这些词曾整体漏检，
    漏检即等于数值或行星写错也能通过装配。
    """

    def detected(self, text: str) -> set[str]:
        return {item["term"] for item in MODULE.detect_high_risk_terms(text)}

    def test_cardinal_numbers_in_child_and_sibling_counts(self) -> None:
        self.assertIn("three", self.detected("the native will be brought up by three mothers, or two fathers"))
        self.assertIn("six", self.detected("if Putr is tenanted by six Grahas"))
        self.assertIn("nine", self.detected("Nine will be the number of sons"))

    def test_santhanam_short_forms_are_detected(self) -> None:
        self.assertIn("putr", self.detected("Should Putr’s Lord be in Ari Bhava"))
        self.assertIn("shukr", self.detected("while its Lord is with Shukr"))
        self.assertIn("lagn", self.detected("Lagn’s Lord is in fall"))
        self.assertIn("mandi", self.detected("Should Mandi be in Lagna"))

    def test_divisional_chart_names_are_detected(self) -> None:
        self.assertIn("navans", self.detected("or in own Navāńś, or in exaltation"))

    def test_pronoun_one_is_deliberately_not_a_number_term(self) -> None:
        self.assertNotIn("one", self.detected("one will beget a child at the age of 30"))

    def test_coverage_requires_whole_word_not_substring(self) -> None:
        self.assertFalse(MODULE.shared_constants.high_risk_term_covered("10", ["100 sons"]))
        self.assertTrue(MODULE.shared_constants.high_risk_term_covered("10", ["10 sons"]))


if __name__ == "__main__":
    unittest.main()
