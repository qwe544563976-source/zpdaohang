import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("backfill_step_hash.py")
SPEC = importlib.util.spec_from_file_location("backfill_step_hash", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

SHARED = MODULE.shared_constants


def ledger() -> dict:
    return {
        "schema_version": "judgment-method-recipes/v2",
        "generation": {"generator": "cangjie-skill/scripts/build_methods.py"},
        "methods": [
            {
                "method": "m1",
                "steps": [
                    {"step_id": "m1.step-001", "action": "第一步"},
                    {"step_id": "m1.step-002", "action": "第二步"},
                ],
            }
        ],
    }


class BackfillTests(unittest.TestCase):
    def test_backfill_adds_hash_hint_and_generator(self) -> None:
        data = ledger()
        counts = MODULE.backfill(data)
        self.assertEqual(counts["steps_backfilled"], 2)
        self.assertEqual(counts["spine_slot_hints_added"], 1)
        self.assertTrue(counts["generator_updated"])
        self.assertEqual(data["generation"]["generator"], SHARED.GENERATOR_ID)
        step = data["methods"][0]["steps"][0]
        self.assertEqual(step["step_hash"], SHARED.compute_step_hash(step))
        self.assertIsNone(data["methods"][0]["spine_slot_hint"])

    def test_backfill_is_idempotent(self) -> None:
        data = ledger()
        MODULE.backfill(data)
        counts = MODULE.backfill(data)
        self.assertEqual(counts["steps_backfilled"], 0)
        self.assertEqual(counts["steps_already_correct"], 2)
        self.assertEqual(counts["spine_slot_hints_added"], 0)
        self.assertFalse(counts["generator_updated"])

    def test_backfill_does_not_touch_step_content(self) -> None:
        data = ledger()
        before = json.loads(json.dumps(data["methods"][0]["steps"][0]))
        MODULE.backfill(data)
        after = {k: v for k, v in data["methods"][0]["steps"][0].items() if k != "step_hash"}
        self.assertEqual(before, after)

    def test_cli_writes_backup_and_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "method-recipes.json"
            path.write_text(json.dumps(ledger(), ensure_ascii=False), encoding="utf-8")
            first = subprocess.run(
                [sys.executable, str(SCRIPT), str(path)],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
            report = json.loads(first.stdout)
            self.assertTrue(report["written"])
            self.assertTrue(Path(report["backup"]).is_file())
            second = subprocess.run(
                [sys.executable, str(SCRIPT), str(path)],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            report2 = json.loads(second.stdout)
            self.assertFalse(report2["changed"])
            self.assertFalse(report2["written"])

    def test_cli_check_mode_never_writes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "method-recipes.json"
            original = json.dumps(ledger(), ensure_ascii=False)
            path.write_text(original, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(path), "--check"],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            report = json.loads(result.stdout)
            self.assertTrue(report["changed"])
            self.assertFalse(report["written"])
            self.assertEqual(path.read_text(encoding="utf-8"), original)


if __name__ == "__main__":
    unittest.main()
