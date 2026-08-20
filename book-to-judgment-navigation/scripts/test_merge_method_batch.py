import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).with_name("merge_method_batch.py")
SPEC = importlib.util.spec_from_file_location("merge_method_batch", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


RECIPE_VALUE = {
    "methods": [
        {"method": "m", "steps": [{"step_id": "m.step-001", "step_hash": "hash-001"}]}
    ],
    "generation": {"high_risk_terms": {}},
}


def audit_value(
    verdict: str = "PASS",
    finding_status: str = "本轮未找到问题",
    step_hash: str = "hash-001",
    schema_version: str = "independent-semantic-audit/v3",
    confirmations: dict | None = None,
) -> dict:
    return {
        "schema_version": schema_version,
        "batch_id": "batch-1",
        "identity": {"participated_in_production": False},
        "review_mode": "full",
        "reviewed_step_ids": ["m.step-001"],
        "entries": [
            {
                "step_id": "m.step-001",
                "verdict": verdict,
                "step_hash": step_hash,
                "high_risk_confirmations": confirmations or {},
            }
        ],
        "finding_status": finding_status,
    }


class MergeMethodBatchTests(unittest.TestCase):
    def write_json(self, path: Path, value: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def test_full_audit_bound_to_current_recipe_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary)
            recipe = batch / "references/navigation/method-recipes.json"
            self.write_json(recipe, RECIPE_VALUE)
            state = {
                "batch_id": "batch-1",
                "review_mode": "full",
                "audit_step_ids": ["m.step-001"],
            }
            self.write_json(batch / "validation/independent-semantic-audit.json", audit_value())
            report = MODULE.verify_audit(batch, state, recipe)
            self.assertEqual(report["finding_status"], "本轮未找到问题")

    def test_audit_v2_whole_file_binding_format_is_retired(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary)
            recipe = batch / "references/navigation/method-recipes.json"
            self.write_json(recipe, RECIPE_VALUE)
            state = {"batch_id": "batch-1", "review_mode": "full", "audit_step_ids": ["m.step-001"]}
            self.write_json(
                batch / "validation/independent-semantic-audit.json",
                audit_value(schema_version="independent-semantic-audit/v2"),
            )
            with self.assertRaisesRegex(MODULE.MergeError, "不是 v3"):
                MODULE.verify_audit(batch, state, recipe)

    def test_audit_entry_with_stale_step_hash_is_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary)
            recipe = batch / "references/navigation/method-recipes.json"
            self.write_json(recipe, RECIPE_VALUE)
            state = {"batch_id": "batch-1", "review_mode": "full", "audit_step_ids": ["m.step-001"]}
            self.write_json(
                batch / "validation/independent-semantic-audit.json",
                audit_value(step_hash="stale-hash"),
            )
            with self.assertRaisesRegex(MODULE.MergeError, "步骤内容指纹"):
                MODULE.verify_audit(batch, state, recipe)

    def test_unconfirmed_high_risk_term_is_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary)
            recipe = batch / "references/navigation/method-recipes.json"
            value = json.loads(json.dumps(RECIPE_VALUE))
            value["generation"]["high_risk_terms"] = {
                "m.step-001": [
                    {"term": "saturn", "term_class": "proper_noun", "mapped_quote": "Saturn", "mapped_claim": "土星"}
                ]
            }
            self.write_json(recipe, value)
            state = {"batch_id": "batch-1", "review_mode": "full", "audit_step_ids": ["m.step-001"]}
            self.write_json(batch / "validation/independent-semantic-audit.json", audit_value())
            with self.assertRaisesRegex(MODULE.MergeError, "高风险词确认"):
                MODULE.verify_audit(batch, state, recipe)

    def test_high_risk_reject_choice_requires_reject_verdict(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary)
            recipe = batch / "references/navigation/method-recipes.json"
            value = json.loads(json.dumps(RECIPE_VALUE))
            value["generation"]["high_risk_terms"] = {
                "m.step-001": [
                    {"term": "saturn", "term_class": "proper_noun", "mapped_quote": "Saturn", "mapped_claim": "土星"}
                ]
            }
            self.write_json(recipe, value)
            state = {"batch_id": "batch-1", "review_mode": "full", "audit_step_ids": ["m.step-001"]}
            self.write_json(
                batch / "validation/independent-semantic-audit.json",
                audit_value(confirmations={"saturn": "reject"}),
            )
            with self.assertRaisesRegex(MODULE.MergeError, "必须判 REJECT"):
                MODULE.verify_audit(batch, state, recipe)

    def test_audit_missing_required_step_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary)
            recipe = batch / "references/navigation/method-recipes.json"
            self.write_json(recipe, RECIPE_VALUE)
            state = {
                "batch_id": "batch-1",
                "review_mode": "full",
                "audit_step_ids": ["m.step-001"],
            }
            value = audit_value()
            value["reviewed_step_ids"] = []
            value["entries"] = []
            self.write_json(batch / "validation/independent-semantic-audit.json", value)
            with self.assertRaisesRegex(MODULE.MergeError, "没有覆盖"):
                MODULE.verify_audit(batch, state, recipe)

    def test_audit_reject_is_a_terminal_signal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary)
            recipe = batch / "references/navigation/method-recipes.json"
            self.write_json(recipe, RECIPE_VALUE)
            state = {
                "batch_id": "batch-1",
                "review_mode": "full",
                "audit_step_ids": ["m.step-001"],
            }
            self.write_json(
                batch / "validation/independent-semantic-audit.json",
                audit_value(verdict="REJECT", finding_status="本轮找到问题"),
            )
            with self.assertRaises(MODULE.AuditRejected) as context:
                MODULE.verify_audit(batch, state, recipe)
            self.assertEqual(context.exception.rejected_step_ids, ["m.step-001"])

    def test_invalid_audit_verdict_is_not_a_terminal_rejection(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary)
            recipe = batch / "references/navigation/method-recipes.json"
            self.write_json(recipe, RECIPE_VALUE)
            state = {
                "batch_id": "batch-1",
                "review_mode": "full",
                "audit_step_ids": ["m.step-001"],
            }
            self.write_json(
                batch / "validation/independent-semantic-audit.json",
                audit_value(verdict="UNKNOWN", finding_status="本轮找到问题"),
            )
            with self.assertRaisesRegex(MODULE.MergeError, "非法判定"):
                MODULE.verify_audit(batch, state, recipe)

    def test_merge_main_marks_valid_reject_as_terminal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            batch = Path(temporary)
            recipe = batch / "references/navigation/method-recipes.json"
            self.write_json(recipe, RECIPE_VALUE)
            state_path = batch / "validation/batch-state.json"
            self.write_json(
                state_path,
                {
                    "batch_id": "batch-1",
                    "current_state": "audit_in_progress",
                    "review_mode": "full",
                    "audit_step_ids": ["m.step-001"],
                    "method_recipes_sha256": MODULE.sha256(recipe),
                    "history": [],
                },
            )
            self.write_json(
                batch / "validation/independent-semantic-audit.json",
                audit_value(verdict="REJECT", finding_status="本轮找到问题"),
            )
            with patch.object(sys, "argv", ["merge_method_batch.py", "--batch", str(batch), "--target", str(batch)]):
                self.assertEqual(MODULE.main(), 1)
            saved = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["current_state"], "rejected")

    def test_rejected_audit_ends_the_batch(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            state_path = Path(temporary) / "batch-state.json"
            state = {"current_state": "audit_in_progress", "history": []}
            evidence = Path(temporary) / "independent-semantic-audit.json"
            MODULE.reject_state(state_path, state, "独立检查发现问题", evidence)
            saved = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["current_state"], "rejected")
            self.assertEqual(saved["history"][-1]["evidence"], str(evidence))

    def test_project_status_updates_from_merge_counts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            status_path = root / "JUDGMENT_PIPELINE_STATUS.json"
            evidence = root / "merge-receipt.json"
            self.write_json(
                status_path,
                {
                    "updated_on": "old",
                    "current_phase_cn": "机器账显示剩余候选 5 条",
                    "only_next_action": "当前剩余候选 5 条；继续生产",
                    "verified_currently": {"full_book_source_manifest": "旧"},
                    "evidence": [],
                },
            )
            MODULE.update_project_status(
                status_path,
                {"remaining_candidates_after": 4},
                "2026-08-19T22:00:00+00:00",
                evidence,
            )
            saved = json.loads(status_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["updated_on"], "2026-08-19")
            self.assertIn("剩余候选 4 条", saved["current_phase_cn"])
            self.assertIn("当前剩余候选 4 条", saved["only_next_action"])
            self.assertIn("2024 条唯一原文；4 条待生产候选", saved["verified_currently"]["full_book_source_manifest"])
            self.assertEqual(saved["evidence"], [str(evidence)])

    def test_intermediate_full_validation_allows_only_remaining_candidates(self) -> None:
        remaining = {"bphs-97:santhanam:ch51:v1", "bphs-97:santhanam:ch52:v2"}
        report = {
            "passed": False,
            "errors": [
                "方法候选尚未完成方法生产，不能通过：bphs-97:santhanam:ch52:v2",
                "方法候选尚未完成方法生产，不能通过：bphs-97:santhanam:ch51:v1",
            ],
        }
        accepted = MODULE.validate_full_book_result(report, 1, remaining)
        self.assertIs(accepted, report)

    def test_intermediate_full_validation_rejects_any_other_error(self) -> None:
        remaining = {"bphs-97:santhanam:ch51:v1"}
        report = {
            "passed": False,
            "errors": [
                "方法候选尚未完成方法生产，不能通过：bphs-97:santhanam:ch51:v1",
                "派生文件与机器真相不一致，请运行 --render-derived：methods/verified.md",
            ],
        }
        with self.assertRaisesRegex(MODULE.MergeError, "剩余候选错误之外"):
            MODULE.validate_full_book_result(report, 1, remaining)

    def test_terminal_validation_failure_is_rejected(self) -> None:
        report = {
            "passed": False,
            "errors": ["方法候选尚未完成方法生产，不能通过：bphs-97:santhanam:ch51:v1"],
        }
        with self.assertRaisesRegex(MODULE.MergeError, "候选已清零但全书验证仍失败"):
            MODULE.validate_full_book_result(report, 1, set())

    def test_terminal_full_validation_requires_exit_zero(self) -> None:
        report = {"passed": True, "errors": []}
        accepted = MODULE.validate_full_book_result(report, 0, set())
        self.assertIs(accepted, report)

    def test_pipeline_state_records_merge_counts(self) -> None:
        counts = {
            "added_methods": 8,
            "consumed_sources": 84,
            "remaining_candidates_after": 1671,
        }
        text = MODULE.pipeline_state_with_merge_counts("# 状态\n", counts, "2026-08-19T00:00:00+00:00")
        self.assertIn("本批新增方法数：8", text)
        self.assertIn("本批消化原文数：84", text)
        self.assertIn("合并后剩余候选数：1671", text)

    def test_pipeline_state_replaces_previous_merge_counts(self) -> None:
        counts = {
            "added_methods": 2,
            "consumed_sources": 10,
            "remaining_candidates_after": 100,
        }
        old = "# 状态\n\n" + "\n".join(
            [
                MODULE.PIPELINE_STATE_START,
                "- 本批新增方法数：9",
                "- 本批消化原文数：90",
                "- 合并后剩余候选数：110",
                MODULE.PIPELINE_STATE_END,
            ]
        ) + "\n"
        updated = MODULE.pipeline_state_with_merge_counts(old, counts, "now")
        self.assertEqual(updated.count(MODULE.PIPELINE_STATE_START), 1)
        self.assertIn("本批新增方法数：2", updated)
        self.assertNotIn("本批新增方法数：9", updated)

    def test_merge_ignores_frozen_knowledge_maps_and_merges_machine_truth(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            batch = root / "batch"
            target = root / "target"
            batch_recipe = {
                "methods": [
                    {"method": "ch25-method", "publishable": False, "executable_in_pilot": False}
                ]
            }
            batch_query = {"topics": {"ch25-topic": {"title": "批次主题"}}}
            batch_scan = {
                "atom_dispositions": [
                    {"evidence_atom_id": "atom-1", "disposition": "method_step"}
                ]
            }
            target_recipe = {"methods": []}
            target_query = {"topics": {}}
            target_scan = {
                "atom_dispositions": [
                    {"evidence_atom_id": "atom-1", "disposition": "method_candidate"}
                ]
            }
            self.write_json(batch / "references/navigation/method-recipes.json", batch_recipe)
            self.write_json(batch / "references/navigation/query-recipes.json", batch_query)
            self.write_json(batch / "validation/method-source-scan.json", batch_scan)
            self.write_json(target / "references/navigation/method-recipes.json", target_recipe)
            self.write_json(target / "references/navigation/query-recipes.json", target_query)
            self.write_json(target / "validation/method-source-scan.json", target_scan)

            frozen_topic = target / "references/knowledge/topic-map.json"
            batch_topic = batch / "references/knowledge/topic-map.json"
            frozen_glossary = target / "references/knowledge/glossary.json"
            batch_glossary = batch / "references/knowledge/glossary.json"
            self.write_json(frozen_topic, {"topics": {"frozen": "canonical"}})
            self.write_json(batch_topic, {"topics": {"frozen": "different"}})
            self.write_json(frozen_glossary, {"terms": [{"term": "frozen", "definition": "canonical"}]})
            self.write_json(batch_glossary, {"terms": [{"term": "frozen", "definition": "different"}]})
            topic_bytes = frozen_topic.read_bytes()
            glossary_bytes = frozen_glossary.read_bytes()

            merged, counts = MODULE.merge_data(batch, target)

            self.assertEqual(
                set(merged),
                {
                    Path("references/navigation/method-recipes.json"),
                    Path("references/navigation/query-recipes.json"),
                    Path("validation/method-source-scan.json"),
                },
            )
            self.assertEqual(merged[Path("references/navigation/method-recipes.json")]["methods"], batch_recipe["methods"])
            self.assertEqual(merged[Path("references/navigation/query-recipes.json")]["topics"], batch_query["topics"])
            self.assertEqual(
                merged[Path("validation/method-source-scan.json")]["atom_dispositions"],
                batch_scan["atom_dispositions"],
            )
            self.assertEqual(counts["consumed_sources"], 1)
            self.assertEqual(frozen_topic.read_bytes(), topic_bytes)
            self.assertEqual(frozen_glossary.read_bytes(), glossary_bytes)

    def test_receipt_write_failure_restores_book_and_batch_state(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            batch = root / "batch"
            target = root / "target"
            for relative in MODULE.MACHINE_PATHS:
                self.write_json(batch / relative, {"batch": True})
                self.write_json(target / relative, {"target": True})
            state = {
                "batch_id": "batch-1",
                "current_state": "audit_in_progress",
                "method_recipes_sha256": MODULE.sha256(batch / MODULE.MACHINE_PATHS[0]),
                "history": [],
            }
            self.write_json(batch / "validation/batch-state.json", state)
            self.write_json(batch / "validation/independent-semantic-audit.json", {})
            (target / MODULE.PIPELINE_STATE_NAME).write_text("# original\n", encoding="utf-8")
            project_status = target.parent / MODULE.PROJECT_STATUS_NAME
            self.write_json(project_status, {"verified_currently": {}, "evidence": []})
            original_target = (target / MODULE.MACHINE_PATHS[0]).read_bytes()
            original_pipeline = (target / MODULE.PIPELINE_STATE_NAME).read_bytes()
            original_status = project_status.read_bytes()
            rendered_once = {"value": False}

            merged = {
                MODULE.MACHINE_PATHS[0]: {"methods": [{"method": "new"}]},
                MODULE.MACHINE_PATHS[1]: {"topics": {"new": {}}},
                MODULE.MACHINE_PATHS[2]: {"atom_dispositions": []},
            }
            counts = {
                "added_methods": 1,
                "consumed_sources": 1,
                "remaining_candidates_before": 1,
                "remaining_candidates_after": 0,
            }
            original_atomic_write = MODULE.atomic_write
            failed = {"value": False}

            def fail_first_receipt(path: Path, value: dict) -> None:
                if path == batch / "validation/merge-receipt.json" and not failed["value"]:
                    failed["value"] = True
                    raise OSError("模拟合入凭证写入失败")
                original_atomic_write(path, value)

            def fake_run_validator(target_path: Path, require_v2: bool, **kwargs: object) -> dict:
                if not require_v2 and not rendered_once["value"]:
                    rendered_once["value"] = True
                    generated = target_path / "methods/families/new-method.md"
                    generated.parent.mkdir(parents=True, exist_ok=True)
                    generated.write_text("temporary derived output", encoding="utf-8")
                return {"passed": True, "errors": []}

            with patch.object(MODULE, "verify_audit", return_value={"finding_status": "本轮未找到问题"}), patch.object(
                MODULE, "merge_data", return_value=(merged, counts)
            ), patch.object(MODULE, "run_validator", side_effect=fake_run_validator), patch.object(
                MODULE, "atomic_write", side_effect=fail_first_receipt
            ), patch.object(
                sys,
                "argv",
                ["merge_method_batch.py", "--batch", str(batch), "--target", str(target)],
            ):
                self.assertEqual(MODULE.main(), 1)

            self.assertEqual((target / MODULE.MACHINE_PATHS[0]).read_bytes(), original_target)
            self.assertEqual((target / MODULE.PIPELINE_STATE_NAME).read_bytes(), original_pipeline)
            self.assertEqual(project_status.read_bytes(), original_status)
            restored_state = json.loads((batch / "validation/batch-state.json").read_text(encoding="utf-8"))
            self.assertEqual(restored_state["current_state"], "audit_in_progress")
            self.assertFalse((batch / "validation/merge-receipt.json").exists())
            self.assertFalse((target / "methods/families/new-method.md").exists())


if __name__ == "__main__":
    unittest.main()
