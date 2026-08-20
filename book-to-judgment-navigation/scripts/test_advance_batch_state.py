import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


SCRIPT = Path(__file__).with_name("advance_batch_state.py")
SPEC = importlib.util.spec_from_file_location("advance_batch_state", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class AdvanceBatchStateTests(unittest.TestCase):
    def valid_receipt(self, root: Path, recipe: Path) -> dict:
        source = {"source_path": "source.json", "source_fingerprint": "source-fingerprint"}
        bindings = [{"path": str(recipe), "sha256": MODULE.sha256(recipe)}]
        record_paths = {}
        for label in ("positive", "negative", "baseline"):
            path = root / f"{label}-run.json"
            path.write_text("{}\n", encoding="utf-8")
            record_paths[label] = str(path)
        return {
            "schema_version": "anti-false-green-run-v1",
            "status": "completed",
            "source": source,
            "artifact_bindings": bindings,
            "runs": {
                "positive": {"exit_code": 0, "validator_report": {"passed": True, "errors": []}, "record_path": record_paths["positive"], "parse_error": ""},
                "negative": {"exit_code": 1, "validator_report": {"passed": False, "errors": ["bad"]}, "record_path": record_paths["negative"], "parse_error": ""},
                "baseline": {"exit_code": 1, "validator_report": {"passed": False, "errors": ["blank"]}, "record_path": record_paths["baseline"], "parse_error": ""},
            },
        }

    def test_valid_three_controls_bind_current_recipe(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            recipe = root / "method-recipes.json"
            receipt = root / "run-receipt.json"
            recipe.write_text("{}\n", encoding="utf-8")
            receipt_data = self.valid_receipt(root, recipe)
            receipt.write_text(json.dumps(receipt_data), encoding="utf-8")
            report = {
                "controls": {"positive": "pass", "negative": "fail", "baseline": "fail"},
                "status": "machine_check_pass",
                "unresolved_blockers": [],
                "artifact_bindings": [{"path": str(recipe), "sha256": MODULE.sha256(recipe)}],
                "source": receipt_data["source"],
                "run_receipt": str(receipt),
            }
            with patch.object(MODULE, "run_gate_report_validator", return_value={"passed": True}):
                MODULE.validate_controls(root, report, recipe, receipt)

    def test_wrong_blank_baseline_cannot_enter_audit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            recipe = root / "method-recipes.json"
            receipt = root / "run-receipt.json"
            recipe.write_text("{}\n", encoding="utf-8")
            receipt_data = self.valid_receipt(root, recipe)
            receipt.write_text(json.dumps(receipt_data), encoding="utf-8")
            report = {
                "controls": {"positive": "pass", "negative": "fail", "baseline": "pass"},
                "status": "machine_check_pass",
                "unresolved_blockers": [],
                "artifact_bindings": [{"path": str(recipe), "sha256": MODULE.sha256(recipe)}],
                "source": receipt_data["source"],
                "run_receipt": str(receipt),
            }
            with patch.object(MODULE, "run_gate_report_validator", return_value={"passed": True}):
                with self.assertRaisesRegex(MODULE.BatchRejected, "正确／错误／空白"):
                    MODULE.validate_controls(root, report, recipe, receipt)

    def test_failed_machine_check_ends_the_batch(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            state_path = Path(temporary) / "batch-state.json"
            state = {"current_state": "mechanical_testing", "history": []}
            MODULE.reject_state(state_path, state, "机器交付检查失败", ["真实错误"])
            saved = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["current_state"], "rejected")
            self.assertEqual(saved["history"][-1]["details"], ["真实错误"])

    def test_wrong_gate_binding_is_not_a_batch_rejection(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            recipe = root / "method-recipes.json"
            receipt = root / "run-receipt.json"
            other_recipe = root / "other-method-recipes.json"
            recipe.write_text("{}\n", encoding="utf-8")
            other_recipe.write_text("other\n", encoding="utf-8")
            receipt.write_text("{}\n", encoding="utf-8")
            report = {
                "controls": {"positive": "fail", "negative": "fail", "baseline": "fail"},
                "status": "machine_check_failed",
                "artifact_bindings": [{"path": str(other_recipe), "sha256": MODULE.sha256(other_recipe)}],
                "run_receipt": str(receipt),
            }
            with self.assertRaises(MODULE.StateError):
                MODULE.validate_controls(root, report, recipe, receipt)

    def test_empty_receipt_is_not_a_valid_machine_check(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            recipe = root / "method-recipes.json"
            receipt = root / "run-receipt.json"
            recipe.write_text("{}\n", encoding="utf-8")
            receipt.write_text("{}\n", encoding="utf-8")
            report = {
                "controls": {"positive": "pass", "negative": "fail", "baseline": "fail"},
                "status": "machine_check_pass",
                "unresolved_blockers": [],
                "artifact_bindings": [{"path": str(recipe), "sha256": MODULE.sha256(recipe)}],
                "run_receipt": str(receipt),
            }
            with patch.object(
                MODULE,
                "run_gate_report_validator",
                side_effect=MODULE.StateError("反假绿报告检查器未通过：run_receipt 不是已完成记录"),
            ):
                with self.assertRaisesRegex(MODULE.StateError, "不是已完成记录"):
                    MODULE.validate_controls(root, report, recipe, receipt)

    def test_main_keeps_state_when_validator_output_is_unreadable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "validation").mkdir()
            (root / "references/navigation").mkdir(parents=True)
            recipe = root / "references/navigation/method-recipes.json"
            recipe.write_text("{}\n", encoding="utf-8")
            state_path = root / "validation/batch-state.json"
            state_path.write_text(
                json.dumps(
                    {
                        "schema_version": "judgment-batch-state/v2",
                        "current_state": "mechanical_testing",
                        "method_recipes_sha256": MODULE.sha256(recipe),
                        "history": [],
                    }
                ),
                encoding="utf-8",
            )
            fake = SimpleNamespace(returncode=1, stdout="", stderr="validator crashed")
            with patch.object(sys, "argv", ["advance_batch_state.py", str(root)]), patch.object(
                MODULE.subprocess, "run", return_value=fake
            ):
                self.assertEqual(MODULE.main(), 1)
            saved = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["current_state"], "mechanical_testing")

    def test_main_enters_audit_with_complete_real_controls(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "validation").mkdir()
            (root / "references/navigation").mkdir(parents=True)
            recipe = root / "references/navigation/method-recipes.json"
            recipe.write_text("{}\n", encoding="utf-8")
            state_path = root / "validation/batch-state.json"
            state_path.write_text(
                json.dumps(
                    {
                        "schema_version": "judgment-batch-state/v2",
                        "current_state": "mechanical_testing",
                        "method_recipes_sha256": MODULE.sha256(recipe),
                        "history": [],
                    }
                ),
                encoding="utf-8",
            )
            receipt_data = self.valid_receipt(root, recipe)
            receipt = root / "validation/run-receipt.json"
            receipt.write_text(json.dumps(receipt_data), encoding="utf-8")
            gate = root / "validation/gate-report.json"
            gate.write_text(
                json.dumps(
                    {
                        "controls": {"positive": "pass", "negative": "fail", "baseline": "fail"},
                        "status": "machine_check_pass",
                        "unresolved_blockers": [],
                        "source": receipt_data["source"],
                        "artifact_bindings": receipt_data["artifact_bindings"],
                        "run_receipt": str(receipt),
                    }
                ),
                encoding="utf-8",
            )
            fake = SimpleNamespace(returncode=0, stdout=json.dumps({"passed": True, "errors": []}), stderr="")
            with patch.object(
                sys,
                "argv",
                ["advance_batch_state.py", str(root), "--gate-report", str(gate)],
            ), patch.object(MODULE.subprocess, "run", return_value=fake), patch.object(
                MODULE, "run_gate_report_validator", return_value={"passed": True}
            ):
                self.assertEqual(MODULE.main(), 0)
            saved = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(saved["current_state"], "audit_in_progress")


if __name__ == "__main__":
    unittest.main()
