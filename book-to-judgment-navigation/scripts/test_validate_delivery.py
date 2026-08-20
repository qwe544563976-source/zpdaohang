#!/usr/bin/env python3
"""Regression checks for the judgment-navigation delivery gate."""

from __future__ import annotations

import json
import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


SCRIPT = Path(__file__).with_name("validate_delivery.py")
LEGACY_FIXTURE = Path(
    "C:/Users/aa/Documents/ChatGPT/洗书/"
    "_judgment_distillation_pilot_bphs97_ch11_20260814"
)


def _resolve_fixture() -> Path:
    """夹具解析顺序：环境变量 → 本机历史夹具（默认行为不变）→ 现场自举。"""
    env = os.environ.get("JUDGMENT_NAV_PILOT_FIXTURE")
    if env:
        return Path(env)
    if LEGACY_FIXTURE.is_dir():
        return LEGACY_FIXTURE
    builder = Path(__file__).resolve().parents[1] / "tests" / "make_pilot_fixture.py"
    parent = Path(tempfile.mkdtemp(prefix="judgment-nav-pilot-fixture-"))
    result = subprocess.run(
        [sys.executable, str(builder), str(parent)],
        check=False, capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode != 0:
        raise RuntimeError(f"试点夹具自举失败：{result.stdout}\n{result.stderr}")
    return parent / "_judgment_distillation_pilot_fixture"


FIXTURE = _resolve_fixture()
VALIDATOR_SPEC = importlib.util.spec_from_file_location(
    "validate_delivery_cross_regression",
    SCRIPT,
)
VALIDATOR = importlib.util.module_from_spec(VALIDATOR_SPEC)
assert VALIDATOR_SPEC and VALIDATOR_SPEC.loader
VALIDATOR_SPEC.loader.exec_module(VALIDATOR)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class DeliveryGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "delivery"
        shutil.copytree(FIXTURE, self.root)
        method_path = self.root / "references" / "navigation" / "method-recipes.json"
        methods = read_json(method_path)
        for method in methods.get("methods", []):
            for step in method.get("steps", []):
                step.setdefault("produced_fact_keys", [])
                step.setdefault("conditional_fact_requirements", [])
        write_json(method_path, methods)
        self.render_derived()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def validate(self, require_v2: bool = False) -> dict:
        command = [sys.executable, str(SCRIPT), str(self.root)]
        if require_v2:
            command.append("--require-v2")
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertTrue(result.stdout, result.stderr)
        return json.loads(result.stdout)

    def assert_error(self, text: str) -> None:
        report = self.validate()
        self.assertFalse(report["passed"])
        self.assertTrue(any(text in error for error in report["errors"]), report["errors"])

    def render_derived(self) -> None:
        subprocess.run(
            [sys.executable, str(SCRIPT), str(self.root), "--render-derived"],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )

    def method_data(self) -> tuple[Path, dict]:
        path = self.root / "references" / "navigation" / "method-recipes.json"
        return path, read_json(path)

    def add_valid_selection_group(self) -> tuple[Path, dict, dict]:
        path, data = self.method_data()
        method = data["methods"][0]
        step = method["steps"][0]
        base_logic = step["condition_logic"]
        base_key = step["required_fact_keys"][0]
        method["conditional_facts"].extend(["选择分支A", "选择分支B"])
        step["condition_logic"] = {
            "operator": "AND",
            "operands": [
                base_logic,
                {
                    "operator": "OR",
                    "operands": [
                        {"fact_key": "选择分支A"},
                        {"fact_key": "选择分支B"},
                    ],
                },
            ],
        }
        step["conditional_fact_requirements"] = [
            {
                "when": {"fact_key": base_key},
                "required_fact_keys": ["选择分支A"],
                "branch_condition_logic": {"fact_key": "选择分支A"},
                "selection_group": "fixture:primary_or",
                "stop_condition": "选中分支A后缺少事实时停止。",
            },
            {
                "when": {"fact_key": base_key},
                "required_fact_keys": ["选择分支B"],
                "branch_condition_logic": {"fact_key": "选择分支B"},
                "selection_group": "fixture:primary_or",
                "stop_condition": "选中分支B后缺少事实时停止。",
            },
        ]
        return path, data, step

    def replace_atom_content_role(self, atom_id: str, content_role: str) -> None:
        work_path = self.root / "WORK_ORDER.json"
        work = read_json(work_path)
        source = Path(work["input"]["evidence_atoms_path"])
        source_copy = Path(self.temp.name) / "evidence_atoms.jsonl"
        found = False
        output = []
        for line in source.read_text(encoding="utf-8").splitlines():
            atom = json.loads(line)
            if atom.get("evidence_atom_id") == atom_id:
                atom["content_role"] = content_role
                found = True
            output.append(json.dumps(atom, ensure_ascii=False, separators=(",", ":")))
        self.assertTrue(found, atom_id)
        source_copy.write_text("\n".join(output) + "\n", encoding="utf-8")
        digest = hashlib.sha256(source_copy.read_bytes()).hexdigest()
        stat = source_copy.stat()
        work["input"]["evidence_atoms_path"] = str(source_copy)
        work["input"]["source_snapshot"] = {
            "size_bytes": stat.st_size,
            "mtime_ns": stat.st_mtime_ns,
            "content_sha256": digest,
        }
        write_json(work_path, work)
        manifest_path = self.root / "DISTILLATION_SOURCE.json"
        manifest = read_json(manifest_path)
        manifest["evidence_atoms_path"] = str(source_copy)
        manifest["evidence_atoms_sha256"] = digest
        write_json(manifest_path, manifest)

    def replace_atom_text(self, atom_id: str, exact_text: str) -> None:
        work_path = self.root / "WORK_ORDER.json"
        work = read_json(work_path)
        source = Path(work["input"]["evidence_atoms_path"])
        source_copy = Path(self.temp.name) / "evidence_atoms.jsonl"
        found = False
        output = []
        for line in source.read_text(encoding="utf-8").splitlines():
            atom = json.loads(line)
            if atom.get("evidence_atom_id") == atom_id:
                atom["exact_text"] = exact_text
                found = True
            output.append(json.dumps(atom, ensure_ascii=False, separators=(",", ":")))
        self.assertTrue(found, atom_id)
        source_copy.write_text("\n".join(output) + "\n", encoding="utf-8")
        digest = hashlib.sha256(source_copy.read_bytes()).hexdigest()
        stat = source_copy.stat()
        work["input"]["evidence_atoms_path"] = str(source_copy)
        work["input"]["source_snapshot"] = {
            "size_bytes": stat.st_size,
            "mtime_ns": stat.st_mtime_ns,
            "content_sha256": digest,
        }
        write_json(work_path, work)
        manifest_path = self.root / "DISTILLATION_SOURCE.json"
        manifest = read_json(manifest_path)
        manifest["evidence_atoms_path"] = str(source_copy)
        manifest["evidence_atoms_sha256"] = digest
        write_json(manifest_path, manifest)

    def test_clean_pilot_fixture_passes_but_executes_nothing(self) -> None:
        report = self.validate()
        self.assertTrue(report["passed"], report["errors"])
        self.assertEqual(report["executable_methods"], 0)

    def test_generated_backup_files_are_not_formal_delivery_inputs(self) -> None:
        root = Path(self.temp.name) / "backup-scope"
        root.mkdir()
        write_json(root / "formal.json", {"pilot_only": False, "publishable": False})
        backup = root / "backups" / "old-run"
        backup.mkdir(parents=True)
        write_json(backup / "old-status.json", {"pilot_only": True, "publishable": True})
        errors: list[str] = []
        VALIDATOR.check_json_flags(root, False, False, errors)
        self.assertEqual(errors, [])

    def test_validator_can_be_loaded_by_upstream_package_checker(self) -> None:
        spec = importlib.util.spec_from_file_location("delivery_validator_import_probe", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        spec.loader.exec_module(module)
        self.assertTrue(callable(module.validate))

    def test_require_v2_rejects_legacy_generator_recipe(self) -> None:
        report = self.validate(require_v2=True)
        self.assertFalse(report["passed"])
        self.assertTrue(any("不是由唯一正式生成器重新生成" in error for error in report["errors"]))

    def test_rejects_knowledge_map_without_atom_anchors(self) -> None:
        path = self.root / "references" / "knowledge" / "chapter-map.json"
        data = read_json(path)
        data["chapters"][0]["evidence_atom_ids"] = []
        write_json(path, data)
        self.assert_error("缺少原文编号")

    def test_rejects_knowledge_map_missing_one_scoped_atom(self) -> None:
        path = self.root / "references" / "knowledge" / "chapter-map.json"
        data = read_json(path)
        data["chapters"][0]["evidence_atom_ids"].pop()
        write_json(path, data)
        self.assert_error("章节地图遗漏允许范围内的原文编号")

    def test_rejects_duplicate_atom_hiding_a_missing_atom(self) -> None:
        path = self.root / "references" / "knowledge" / "chapter-map.json"
        data = read_json(path)
        atom_ids = data["chapters"][0]["evidence_atom_ids"]
        atom_ids[-1] = atom_ids[0]
        write_json(path, data)
        report = self.validate()
        self.assertFalse(report["passed"])
        self.assertTrue(any("遗漏允许范围内的原文编号" in error for error in report["errors"]))
        self.assertTrue(any("重复收录原文编号" in error for error in report["errors"]))

    def test_rejects_method_scan_without_final_disposition(self) -> None:
        path = self.root / "validation" / "method-source-scan.json"
        data = read_json(path)
        data["atom_dispositions"].pop()
        write_json(path, data)
        self.assert_error("方法审查清单遗漏允许范围内的原文编号")

    def test_rejects_method_scan_with_pending_review(self) -> None:
        path = self.root / "validation" / "method-source-scan.json"
        data = read_json(path)
        record = data["atom_dispositions"][0]
        record["disposition"] = "review_pending"
        record["method_ids"] = []
        write_json(path, data)
        self.assert_error("原文尚未完成方法语义审查")

    def test_rejects_complete_classification_without_semantic_fields(self) -> None:
        path = self.root / "validation" / "method-source-scan.json"
        data = read_json(path)
        data["review_status"] = "complete"
        data["atom_dispositions"][0].pop("semantic_class", None)
        write_json(path, data)
        self.assert_error("原文缺少 semantic_class")

    def test_rejects_in_progress_classification_without_both_required_fields(self) -> None:
        path = self.root / "validation" / "method-source-scan.json"
        data = read_json(path)
        data["review_status"] = "in_progress"
        record = data["atom_dispositions"][0]
        record.pop("semantic_class", None)
        record.pop("risk_flags", None)
        write_json(path, data)
        report = self.validate()
        self.assertFalse(report["passed"], report["errors"])
        self.assertTrue(any("原文缺少 semantic_class" in error for error in report["errors"]))
        self.assertTrue(any("原文缺少 risk_flags" in error for error in report["errors"]))

    def test_rejects_unknown_semantic_class(self) -> None:
        path = self.root / "validation" / "method-source-scan.json"
        data = read_json(path)
        data["atom_dispositions"][0]["semantic_class"] = "ai_guessed_rule"
        data["atom_dispositions"][0]["risk_flags"] = []
        write_json(path, data)
        self.assert_error("原文 semantic_class 不合法")

    def test_rejects_unresolved_source_used_as_method_step(self) -> None:
        path = self.root / "validation" / "method-source-scan.json"
        data = read_json(path)
        data["atom_dispositions"][0]["semantic_class"] = "unresolved_source"
        data["atom_dispositions"][0]["risk_flags"] = ["mixed_identity"]
        write_json(path, data)
        self.assert_error("残缺或身份混合的原文不能进入方法步骤")

    def test_rejects_unbuilt_method_candidate(self) -> None:
        path = self.root / "validation" / "method-source-scan.json"
        data = read_json(path)
        record = data["atom_dispositions"][0]
        record["disposition"] = "method_candidate"
        record["method_ids"] = []
        record["semantic_class"] = "calculation_rule"
        record["risk_flags"] = []
        write_json(path, data)
        self.assert_error("方法候选尚未完成方法生产")

    def test_rejects_foundational_knowledge_as_method_candidate(self) -> None:
        path = self.root / "validation" / "method-source-scan.json"
        data = read_json(path)
        record = data["atom_dispositions"][0]
        record["disposition"] = "method_candidate"
        record["method_ids"] = []
        record["semantic_class"] = "foundational_knowledge"
        record["risk_flags"] = []
        write_json(path, data)
        self.assert_error("方法候选的 semantic_class 不是方法或规则类型")

    def test_rejects_required_check_drift(self) -> None:
        path = self.root / "references" / "navigation" / "required-checks.json"
        data = read_json(path)
        data["topics"]["bhava-assessment"]["required_facts"] = ["被手改的事实"]
        write_json(path, data)
        self.assert_error("派生文件与机器真相不一致")

    def test_rejects_missing_method_dependency(self) -> None:
        path, data = self.method_data()
        data["methods"][0]["dependencies"] = ["missing-method"]
        write_json(path, data)
        self.assert_error("依赖不存在的方法")

    def test_rejects_step_using_undeclared_fact(self) -> None:
        path, data = self.method_data()
        data["methods"][0]["steps"][0]["required_fact_keys"] = ["未声明事实"]
        write_json(path, data)
        self.assert_error("使用了方法未声明的事实")

    def test_rejects_placeholder_source_fact(self) -> None:
        path, data = self.method_data()
        method = data["methods"][0]
        step = method["steps"][0]
        method["required_facts"] = ["source_condition_v21"]
        step["required_fact_keys"] = ["source_condition_v21"]
        step["stop_fact_keys"] = ["source_condition_v21"]
        step["condition_logic"] = {"fact_key": "source_condition_v21"}
        write_json(path, data)
        self.render_derived()
        self.assert_error("占位事实")

    def test_rejects_placeholder_branch_fact(self) -> None:
        path, data, step = self.add_valid_selection_group()
        step["conditional_fact_requirements"][0]["required_fact_keys"] = ["choice_a"]
        step["conditional_fact_requirements"][0]["branch_condition_logic"] = {"fact_key": "choice_a"}
        data["methods"][0]["conditional_facts"].append("choice_a")
        write_json(path, data)
        self.render_derived()
        self.assert_error("占位事实")

    def test_rejects_step_without_produced_fact_keys(self) -> None:
        path, data = self.method_data()
        data["methods"][0]["steps"][0].pop("produced_fact_keys")
        write_json(path, data)
        self.assert_error("缺字段")

    def test_rejects_step_using_its_own_produced_fact(self) -> None:
        path, data = self.method_data()
        step = data["methods"][0]["steps"][0]
        step["produced_fact_keys"] = ["本步产出"]
        step["required_fact_keys"] = ["用户真正要问的生活主题", "本步产出"]
        step["stop_fact_keys"] = list(step["required_fact_keys"])
        step["condition_logic"] = {
            "operator": "AND",
            "operands": [
                {"fact_key": "用户真正要问的生活主题"},
                {"fact_key": "本步产出"},
            ],
        }
        write_json(path, data)
        self.render_derived()
        self.assert_error("不能把本步骤产出当作本步骤输入")

    def test_rejects_step_using_future_produced_fact(self) -> None:
        path, data = self.method_data()
        method = data["methods"][0]
        first, second = method["steps"][0], json.loads(json.dumps(method["steps"][0]))
        second["step_id"] = "question-to-bhava-routing.step-02"
        second["produced_fact_keys"] = ["未来步骤产出"]
        first["required_fact_keys"] = ["用户真正要问的生活主题", "未来步骤产出"]
        first["stop_fact_keys"] = list(first["required_fact_keys"])
        first["condition_logic"] = {
            "operator": "AND",
            "operands": [
                {"fact_key": "用户真正要问的生活主题"},
                {"fact_key": "未来步骤产出"},
            ],
        }
        method["steps"] = [first, second]
        write_json(path, data)
        self.render_derived()
        self.assert_error("不能使用未来步骤产出的事实")

    def test_rejects_duplicate_produced_fact(self) -> None:
        path, data = self.method_data()
        method = data["methods"][0]
        first, second = method["steps"][0], json.loads(json.dumps(method["steps"][0]))
        second["step_id"] = "question-to-bhava-routing.step-02"
        first["produced_fact_keys"] = ["重复产出"]
        second["produced_fact_keys"] = ["重复产出"]
        method["steps"] = [first, second]
        write_json(path, data)
        self.render_derived()
        self.assert_error("同一方法内重复生产事实")

    def test_rejects_conditional_fact_without_declared_group(self) -> None:
        path, data = self.method_data()
        step = data["methods"][0]["steps"][0]
        step["conditional_fact_requirements"] = [{
            "when": {"fact_key": "用户真正要问的生活主题"},
            "required_fact_keys": ["未声明分支事实"],
            "stop_condition": "缺少未声明分支事实时停止。",
        }]
        write_json(path, data)
        self.render_derived()
        self.assert_error("条件组事实没有在方法 conditional_facts 中声明")

    def test_accepts_previous_output_and_conditional_requirement(self) -> None:
        path, data = self.method_data()
        method = data["methods"][0]
        method["conditional_facts"] = ["按分支取得的事实"]
        first, second = method["steps"][0], json.loads(json.dumps(method["steps"][0]))
        second["step_id"] = "question-to-bhava-routing.step-02"
        first["produced_fact_keys"] = ["已路由宫位"]
        second["produced_fact_keys"] = []
        second["required_fact_keys"] = ["已路由宫位"]
        second["stop_fact_keys"] = ["已路由宫位"]
        second["condition_logic"] = {"fact_key": "已路由宫位"}
        second["conditional_fact_requirements"] = [{
            "when": {"fact_key": "已路由宫位"},
            "required_fact_keys": ["按分支取得的事实"],
            "stop_condition": "缺少按分支取得的事实时停止。",
        }]
        method["steps"] = [first, second]
        write_json(path, data)
        self.render_derived()
        report = self.validate()
        self.assertTrue(report["passed"], report["errors"])

    def test_accepts_selection_group_after_three_branch_simulations(self) -> None:
        path, data, _step = self.add_valid_selection_group()
        write_json(path, data)
        self.render_derived()
        report = self.validate()
        self.assertTrue(report["passed"], report["errors"])

    def test_v2_or_gate_ignores_unquoted_rule_in_same_atom(self) -> None:
        path, data = self.method_data()
        step = data["methods"][0]["steps"][0]
        atom_id = step["evidence_refs"][0]["evidence_atom_id"]
        quoted_rule = "Please tell me, what is to be deduced from each Bhava."
        self.replace_atom_text(
            atom_id,
            quoted_rule + " If A is in B, or in C, use another rule.",
        )
        step["evidence_refs"][0]["quote"] = quoted_rule
        write_json(path, data)
        self.render_derived()
        report = self.validate(require_v2=True)
        self.assertFalse(
            any(
                "方法 question-to-bhava-routing 步骤 1 的正式原文含明确 OR" in error
                for error in report["errors"]
            ),
            report["errors"],
        )

    def test_v2_or_gate_rejects_quoted_condition_without_selection_group(self) -> None:
        path, data = self.method_data()
        step = data["methods"][0]["steps"][0]
        atom_id = step["evidence_refs"][0]["evidence_atom_id"]
        quoted_rule = "If A is in B, or in C, use this rule."
        self.replace_atom_text(atom_id, quoted_rule)
        step["evidence_refs"][0]["quote"] = quoted_rule
        step["minimum_supported_claim"] = quoted_rule
        write_json(path, data)
        self.render_derived()
        report = self.validate(require_v2=True)
        self.assertTrue(
            any(
                "方法 question-to-bhava-routing 步骤 1 的正式原文含明确 OR" in error
                for error in report["errors"]
            ),
            report["errors"],
        )

    def test_v2_or_gate_rejects_compact_condition_without_selection_group(self) -> None:
        path, data = self.method_data()
        step = data["methods"][0]["steps"][0]
        atom_id = step["evidence_refs"][0]["evidence_atom_id"]
        quoted_rule = "If A is in B or C, use this rule."
        self.replace_atom_text(atom_id, quoted_rule)
        step["evidence_refs"][0]["quote"] = quoted_rule
        step["minimum_supported_claim"] = quoted_rule
        write_json(path, data)
        self.render_derived()
        report = self.validate(require_v2=True)
        self.assertTrue(
            any(
                "方法 question-to-bhava-routing 步骤 1 的正式原文含明确 OR" in error
                for error in report["errors"]
            ),
            report["errors"],
        )

    def test_v2_or_gate_rejects_either_without_selection_group(self) -> None:
        path, data = self.method_data()
        step = data["methods"][0]["steps"][0]
        atom_id = step["evidence_refs"][0]["evidence_atom_id"]
        quoted_rule = "Either A or B activates this rule."
        self.replace_atom_text(atom_id, quoted_rule)
        step["evidence_refs"][0]["quote"] = quoted_rule
        step["minimum_supported_claim"] = quoted_rule
        write_json(path, data)
        self.render_derived()
        report = self.validate(require_v2=True)
        self.assertTrue(
            any(
                "方法 question-to-bhava-routing 步骤 1 的正式原文含明确 OR" in error
                for error in report["errors"]
            ),
            report["errors"],
        )

    def test_v2_or_gate_rejects_claim_or_hidden_by_non_or_quote(self) -> None:
        path, data = self.method_data()
        step = data["methods"][0]["steps"][0]
        atom_id = step["evidence_refs"][0]["evidence_atom_id"]
        quoted_rule = "Please tell me, what is to be deduced from each Bhava."
        claimed_rule = "If A is in B, or in C, use this rule."
        self.replace_atom_text(atom_id, quoted_rule + " " + claimed_rule)
        step["evidence_refs"][0]["quote"] = quoted_rule
        step["minimum_supported_claim"] = claimed_rule
        write_json(path, data)
        self.render_derived()
        report = self.validate(require_v2=True)
        self.assertTrue(
            any(
                "方法 question-to-bhava-routing 步骤 1 的正式原文含明确 OR" in error
                for error in report["errors"]
            ),
            report["errors"],
        )

    def test_rejects_selection_group_without_branch_logic(self) -> None:
        path, data, step = self.add_valid_selection_group()
        step["conditional_fact_requirements"][0].pop("branch_condition_logic")
        write_json(path, data)
        self.render_derived()
        self.assert_error("每个分支都必须有 branch_condition_logic")

    def test_accepts_selection_group_with_overlapping_branches(self) -> None:
        path, data, step = self.add_valid_selection_group()
        second = step["conditional_fact_requirements"][1]
        second["required_fact_keys"] = ["选择分支A"]
        second["branch_condition_logic"] = {"fact_key": "选择分支A"}
        step["condition_logic"]["operands"][1]["operands"][1] = {"fact_key": "选择分支A"}
        write_json(path, data)
        self.render_derived()
        report = self.validate()
        self.assertTrue(report["passed"], report["errors"])

    def test_selection_group_crossed_combination_is_checked(self) -> None:
        groups = [
            {
                "selection_group": "fixture:crossed",
                "when": {"fact_key": "前置A"},
                "required_fact_keys": ["分支A事实"],
                "branch_condition_logic": {"fact_key": "选择A"},
            },
            {
                "selection_group": "fixture:crossed",
                "when": {"fact_key": "前置B"},
                "required_fact_keys": ["分支B事实"],
                "branch_condition_logic": {"fact_key": "选择B"},
            },
        ]
        errors: list[str] = []
        # Force the old runtime result (no blocker) so this test proves the
        # validator has a dedicated crossed-combination simulation.
        with mock.patch.object(VALIDATOR, "_conditional_missing_facts", return_value={}):
            VALIDATOR.validate_selection_group_simulation("交叉回归", groups, errors)
        self.assertTrue(any("交叉组合" in error for error in errors), errors)

    def test_accepts_three_branch_cross_when_third_branch_is_active(self) -> None:
        groups = [
            {
                "selection_group": "fixture:three-branch-cross",
                "when": {"fact_key": "前置A"},
                "required_fact_keys": ["分支A事实"],
                "branch_condition_logic": {"fact_key": "选择A"},
            },
            {
                "selection_group": "fixture:three-branch-cross",
                "when": {"fact_key": "前置B"},
                "required_fact_keys": ["分支B事实"],
                "branch_condition_logic": {"fact_key": "选择B"},
            },
            {
                "selection_group": "fixture:three-branch-cross",
                "when": {"fact_key": "前置A"},
                "required_fact_keys": ["分支C事实"],
                "branch_condition_logic": {"fact_key": "选择B"},
            },
        ]
        errors: list[str] = []
        VALIDATOR.validate_selection_group_simulation("三分支交叉回归", groups, errors)
        self.assertFalse(errors, errors)

    def test_rejects_three_branch_when_no_branch_is_active(self) -> None:
        groups = [
            {
                "selection_group": "fixture:three-branch-none",
                "when": {"fact_key": "共同前置"},
                "required_fact_keys": ["分支A事实"],
                "branch_condition_logic": {"fact_key": "选择A"},
            },
            {
                "selection_group": "fixture:three-branch-none",
                "when": {"fact_key": "共同前置"},
                "required_fact_keys": ["分支B事实"],
                "branch_condition_logic": {"fact_key": "选择B"},
            },
            {
                "selection_group": "fixture:three-branch-none",
                "when": {"fact_key": "共同前置"},
                "required_fact_keys": ["分支C事实"],
                "branch_condition_logic": {"fact_key": "选择C"},
            },
        ]
        errors: list[str] = []
        # Force the old runtime result so the machine gate must catch the
        # missing stop when all three OR branches are false.
        with mock.patch.object(VALIDATOR, "_conditional_missing_facts", return_value={}):
            VALIDATOR.validate_selection_group_simulation("三分支全空回归", groups, errors)
        self.assertTrue(any("所有分支都不满足时没有停判" in error for error in errors), errors)

    def test_rejects_minimum_claim_empty_template(self) -> None:
        path, data = self.method_data()
        data["methods"][0]["steps"][0]["minimum_supported_claim"] = "按原文判断。"
        write_json(path, data)
        self.render_derived()
        self.assert_error("最小意思是空话模板")

    def test_rejects_minimum_claim_repeated_three_times(self) -> None:
        path, data = self.method_data()
        method = data["methods"][0]
        first = method["steps"][0]
        second = json.loads(json.dumps(first))
        third = json.loads(json.dumps(first))
        second["step_id"] = f"{method['method']}.step-repeat-02"
        third["step_id"] = f"{method['method']}.step-repeat-03"
        second["produced_fact_keys"] = []
        third["produced_fact_keys"] = []
        method["steps"] = [first, second, third]
        write_json(path, data)
        self.render_derived()
        self.assert_error("至少三个步骤重复同一句最小意思")

    def test_rejects_tampered_seeded_audit_sample(self) -> None:
        path, data = self.method_data()
        for method in data["methods"]:
            method["generalization_scope"] = "general_rule"
        data["schema_version"] = "judgment-method-recipes/v2"
        data["generation"] = {
            "generator": "cangjie-skill/scripts/build_methods.py",
            "generator_version": "2",
            "extraction_schema": "judgment-method-extraction/v2",
            "batch_id": "fixture-sample",
            "chapter_features": ["simple_house_placement"],
            "book_strategy": "rule_book",
            "review_mode": "sample",
            "review_reason": "测试",
            "source_scope_count": 1,
            "audit_step_ids": [],
        }
        write_json(path, data)
        self.render_derived()
        self.assert_error("不是由批次名固定摇号产生")

    def test_rejects_declared_required_fact_unused_by_steps(self) -> None:
        path, data = self.method_data()
        data["methods"][0]["required_facts"].append("声明了但没有步骤使用的事实")
        write_json(path, data)
        self.assert_error("必查事实没有被任何步骤使用")

    def test_rejects_step_without_stop_condition(self) -> None:
        path, data = self.method_data()
        data["methods"][0]["steps"][0]["stop_condition"] = ""
        write_json(path, data)
        self.assert_error("缺少非空 stop_condition")

    def test_rejects_stop_condition_without_fact_binding(self) -> None:
        path, data = self.method_data()
        step = data["methods"][0]["steps"][0]
        step["stop_condition"] = "资料不足时停止"
        step["stop_fact_keys"] = []
        write_json(path, data)
        self.assert_error("stop_fact_keys 必须与 required_fact_keys 一致")

    def test_rejects_unknown_condition_logic_operator(self) -> None:
        path, data = self.method_data()
        step = data["methods"][0]["steps"][0]
        step["condition_logic"] = {
            "operator": "XOR",
            "operands": [{"fact_key": "用户真正要问的生活主题"}],
        }
        write_json(path, data)
        self.assert_error("condition_logic 只允许 AND、OR 或 NOT")

    def test_rejects_step_without_minimum_supported_claim(self) -> None:
        path, data = self.method_data()
        data["methods"][0]["steps"][0]["minimum_supported_claim"] = ""
        write_json(path, data)
        self.assert_error("缺少原文直接支持的最小意思")

    def test_rejects_repeated_support_with_one_source_atom(self) -> None:
        path, data = self.method_data()
        data["methods"][0]["steps"][0]["evidence_refs"] = [
            data["methods"][0]["steps"][0]["evidence_refs"][0]
        ]
        write_json(path, data)
        self.assert_error("repeated_support 至少需要两个独立原文编号")

    def test_rejects_note_as_method_evidence(self) -> None:
        self.replace_atom_content_role("bphs-97:santhanam:ch11:v2", "note")
        self.assert_error("辅助材料，不能作为通用判断步骤证据")

    def test_rejects_case_as_method_evidence(self) -> None:
        self.replace_atom_content_role("bphs-97:santhanam:ch11:v2", "case")
        self.assert_error("辅助材料，不能作为通用判断步骤证据")

    def test_rejects_execution_when_chart_facts_are_unmapped(self) -> None:
        path, data = self.method_data()
        method = data["methods"][0]
        method["workflow_status"] = "independent_verified"
        method["workflow_history"] = [
            "pilot_candidate",
            "mechanical_verified",
            "independent_verified",
        ]
        method["executable_in_pilot"] = True
        write_json(path, data)
        receipt = {
            "schema_version": "independent-verification/v1",
            "run_id": "fixture-independent-run",
            "distillation_run_id": "bphs97-ch11-pilot-20260814",
            "evidence_atoms_sha256": "f4800a67c985246ba3d5103570341c6fb977c83c15a48e94abe738edd0955443",
            "method_ids": ["question-to-bhava-routing"],
        }
        write_json(self.root / "validation" / "independent-verification.json", receipt)
        self.assert_error("排盘事实尚未接通却进入了执行主路")

    def test_rejects_independent_status_without_receipt(self) -> None:
        path, data = self.method_data()
        method = data["methods"][0]
        method["workflow_status"] = "independent_verified"
        method["workflow_history"] = [
            "pilot_candidate",
            "mechanical_verified",
            "independent_verified",
        ]
        write_json(path, data)
        self.assert_error("无法读取 JSON")

    def test_rejects_receipt_without_method_recipe_binding(self) -> None:
        path, data = self.method_data()
        method = data["methods"][0]
        method["workflow_status"] = "independent_verified"
        method["workflow_history"] = [
            "pilot_candidate",
            "mechanical_verified",
            "independent_verified",
        ]
        method["fact_binding_status"] = "mapped"
        write_json(path, data)
        receipt = {
            "schema_version": "independent-verification/v1",
            "run_id": "old-independent-run",
            "distillation_run_id": "bphs97-ch11-pilot-20260814",
            "evidence_atoms_sha256": "f4800a67c985246ba3d5103570341c6fb977c83c15a48e94abe738edd0955443",
            "method_ids": ["question-to-bhava-routing"],
        }
        write_json(self.root / "validation" / "independent-verification.json", receipt)
        self.assert_error("没有绑定当前方法配方内容")

    def test_rejects_method_change_after_bound_receipt(self) -> None:
        path, data = self.method_data()
        method = data["methods"][0]
        method["workflow_status"] = "independent_verified"
        method["workflow_history"] = [
            "pilot_candidate",
            "mechanical_verified",
            "independent_verified",
        ]
        method["fact_binding_status"] = "mapped"
        write_json(path, data)
        receipt = {
            "schema_version": "independent-verification/v1",
            "run_id": "bound-independent-run",
            "distillation_run_id": "bphs97-ch11-pilot-20260814",
            "evidence_atoms_sha256": "f4800a67c985246ba3d5103570341c6fb977c83c15a48e94abe738edd0955443",
            "method_recipes_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "method_ids": [method["method"]],
            "method_steps": {
                method["method"]: [step["step_id"] for step in method["steps"]]
            },
        }
        write_json(self.root / "validation" / "independent-verification.json", receipt)
        data["methods"][0]["steps"][0]["action"] += " 被核验后又修改"
        write_json(path, data)
        self.assert_error("没有绑定当前方法配方内容")

    def test_rejects_pilot_execution_even_with_formatted_receipt(self) -> None:
        path, data = self.method_data()
        method = data["methods"][0]
        method["workflow_status"] = "independent_verified"
        method["workflow_history"] = [
            "pilot_candidate",
            "mechanical_verified",
            "independent_verified",
        ]
        method["fact_binding_status"] = "mapped"
        method["executable_in_pilot"] = True
        write_json(path, data)

        receipt = {
            "schema_version": "independent-verification/v1",
            "run_id": "fake-independent-run",
            "distillation_run_id": "bphs97-ch11-pilot-20260814",
            "evidence_atoms_sha256": (
                "f4800a67c985246ba3d5103570341c6fb977c83c15a48e94abe738edd0955443"
            ),
            "method_ids": ["question-to-bhava-routing"],
        }
        write_json(
            self.root / "validation" / "independent-verification.json",
            receipt,
        )
        self.assert_error("试验状态禁止生产执行")

    def test_rejects_manual_overclaim_in_derived_markdown(self) -> None:
        path = self.root / "methods" / "families" / "bhava-assessment.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n本方法现在可以直接给出最终吉凶。\n", encoding="utf-8")
        self.assert_error("派生文件与机器真相不一致")

    def test_rejects_deleted_machine_upstream_issue(self) -> None:
        path = self.root / "UPSTREAM_ISSUES.json"
        data = read_json(path)
        data["issues"] = []
        write_json(path, data)
        self.assert_error("引用了不存在的上游问题")

    def test_rejects_upstream_issue_missing_dependent_method(self) -> None:
        path, data = self.method_data()
        data["methods"][3]["dependencies"] = ["bhava-assessment"]
        write_json(path, data)
        self.assert_error("上游问题受影响方法清单不完整")

    def test_allows_nonblocking_upstream_issue_without_method_back_reference(self) -> None:
        issue_path = self.root / "UPSTREAM_ISSUES.json"
        data = read_json(issue_path)
        data["issues"].append({
            "issue_id": "fixture-nonblocking-source-note",
            "evidence_atom_id": "bphs-97:santhanam:ch11:v14-16",
            "issue_type": "SOURCE_NOTE",
            "impact": "需要记录的来源备注，不冻结现有方法。",
            "blocking": False,
            "blocking_stage": "method_distillation",
            "status": "open",
            "affected_method_ids": ["bhava-assessment"],
        })
        write_json(issue_path, data)
        self.render_derived()

        report = self.validate()
        self.assertTrue(report["passed"], report["errors"])
        methods = read_json(self.root / "references" / "navigation" / "method-recipes.json")
        bhava = next(item for item in methods["methods"] if item["method"] == "bhava-assessment")
        self.assertNotIn("fixture-nonblocking-source-note", bhava["upstream_issue_ids"])

    def test_allows_upstream_issue_before_any_method_uses_atom(self) -> None:
        atom_id = "bphs-97:santhanam:ch11:v1"
        method_path, methods = self.method_data()
        for method in methods["methods"]:
            for step in method["steps"]:
                step["evidence_refs"] = [
                    ref for ref in step["evidence_refs"]
                    if ref["evidence_atom_id"] != atom_id
                ]
        write_json(method_path, methods)

        scan_path = self.root / "validation" / "method-source-scan.json"
        scan = read_json(scan_path)
        for record in scan["atom_dispositions"]:
            if record["evidence_atom_id"] == atom_id:
                record["disposition"] = "upstream_issue_blocked"
                record["method_ids"] = []
        write_json(scan_path, scan)

        issue_path = self.root / "UPSTREAM_ISSUES.json"
        issues = read_json(issue_path)
        issues["issues"].append({
            "issue_id": "fixture-issue-before-method",
            "evidence_atom_id": atom_id,
            "issue_type": "mixed_primary_and_note_text",
            "impact": "原文身份需要上游复核，当前没有方法引用。",
            "blocking": True,
            "blocking_stage": "method_distillation",
            "status": "open",
            "affected_method_ids": [],
        })
        write_json(issue_path, issues)

        subprocess.run(
            [sys.executable, str(SCRIPT), str(self.root), "--render-derived"],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        report = self.validate()
        self.assertTrue(report["passed"], report["errors"])

    def test_rejects_distiller_marking_upstream_issue_resolved(self) -> None:
        path = self.root / "UPSTREAM_ISSUES.json"
        data = read_json(path)
        data["issues"][0]["status"] = "resolved"
        write_json(path, data)
        self.assert_error("蒸馏窗口不得把上游问题标记为已解决")

    def test_rejects_retired_source_address_fields(self) -> None:
        path = self.root / "references" / "navigation" / "query-recipes.json"
        data = read_json(path)
        data["topics"]["bhava-assessment"]["card_id"] = "retired-address"
        write_json(path, data)
        self.assert_error("新产物包含退役字段")

    def test_rejects_nested_retired_filters_work_ids(self) -> None:
        path = self.root / "references" / "navigation" / "query-recipes.json"
        data = read_json(path)
        data["topics"]["bhava-assessment"]["filters"] = {"work_ids": ["retired"]}
        write_json(path, data)
        self.assert_error("新产物包含退役字段 filters.work_ids")

    def test_rejects_source_change_with_same_size_and_mtime(self) -> None:
        work_path = self.root / "WORK_ORDER.json"
        work = read_json(work_path)
        source = Path(work["input"]["evidence_atoms_path"])
        source_copy = Path(self.temp.name) / "evidence_atoms.jsonl"
        shutil.copy2(source, source_copy)
        original_stat = source_copy.stat()
        raw = source_copy.read_bytes()
        changed = raw.replace(b"Please", b"please", 1)
        self.assertEqual(len(raw), len(changed))
        self.assertNotEqual(raw, changed)
        source_copy.write_bytes(changed)
        os.utime(source_copy, ns=(original_stat.st_atime_ns, original_stat.st_mtime_ns))
        work["input"]["evidence_atoms_path"] = str(source_copy)
        work["input"]["source_snapshot"]["size_bytes"] = source_copy.stat().st_size
        work["input"]["source_snapshot"]["mtime_ns"] = source_copy.stat().st_mtime_ns
        write_json(work_path, work)
        manifest_path = self.root / "DISTILLATION_SOURCE.json"
        manifest = read_json(manifest_path)
        manifest["evidence_atoms_path"] = str(source_copy)
        write_json(manifest_path, manifest)
        self.assert_error("原文原子内容摘要与已锁定输入不一致")

    def test_formal_mode_rejects_bare_atom_path(self) -> None:
        path = self.root / "WORK_ORDER.json"
        work = read_json(path)
        work["artifact_scope"] = "FORMAL"
        work["pilot_only"] = False
        write_json(path, work)
        self.assert_error("正式模式拒绝裸 evidence_atoms.jsonl 路径")

    def test_v2_step_hash_mismatch_is_rejected(self) -> None:
        step = {
            "step_id": "m.step-001",
            "action": "核对条件。",
            "minimum_supported_claim": "土星弱时受损。",
            "evidence_refs": [{"evidence_atom_id": "a1", "quote": "Saturn is weak", "pdf_pages": [1]}],
        }
        step["step_hash"] = VALIDATOR.compute_step_hash(step)
        methods = [{"method": "m", "steps": [step]}]
        generation = {
            "high_risk_terms": {
                "m.step-001": [
                    {
                        "term": "saturn",
                        "term_class": "proper_noun",
                        "mapped_quote": "Saturn is weak",
                        "mapped_claim": "土星弱",
                    }
                ]
            }
        }
        errors: list[str] = []
        VALIDATOR.validate_step_hashes_and_high_risk_terms(generation, methods, errors)
        self.assertEqual(errors, [])
        step["action"] = "被手改的动作。"
        errors = []
        VALIDATOR.validate_step_hashes_and_high_risk_terms(generation, methods, errors)
        self.assertTrue(any("步骤内容指纹" in error for error in errors), errors)

    def test_v2_high_risk_table_must_match_detection(self) -> None:
        step = {
            "step_id": "m.step-001",
            "minimum_supported_claim": "土星弱时受损。",
            "evidence_refs": [{"evidence_atom_id": "a1", "quote": "Saturn is weak", "pdf_pages": [1]}],
        }
        step["step_hash"] = VALIDATOR.compute_step_hash(step)
        methods = [{"method": "m", "steps": [step]}]
        errors: list[str] = []
        VALIDATOR.validate_step_hashes_and_high_risk_terms(
            {"high_risk_terms": {"m.step-001": []}}, methods, errors
        )
        self.assertTrue(any("机器检出不一致" in error for error in errors), errors)

    def test_v2_receipt_binds_step_hashes_not_whole_file(self) -> None:
        step = {"step_id": "m.step-001", "step_hash": "hash-1"}
        methods = {"m": {"steps": [step]}}
        step_hashes = VALIDATOR.method_step_hash_map(methods)
        self.assertEqual(step_hashes, {"m": {"m.step-001": "hash-1"}})
        receipt = {
            "schema_version": "independent-verification/v1",
            "run_id": "other-run",
            "distillation_run_id": "run-1",
            "evidence_atoms_sha256": "atoms-sha",
            "method_ids": ["m"],
            "method_steps": {"m": ["m.step-001"]},
            "method_step_hashes": {"m": {"m.step-001": "hash-1"}},
        }
        receipt_path = Path(self.temp.name) / "receipt.json"
        write_json(receipt_path, receipt)
        errors: list[str] = []
        VALIDATOR.load_receipt(
            receipt_path,
            "independent-verification/v1",
            "atoms-sha",
            "run-1",
            "whole-file-sha-not-required",
            methods,
            errors,
            step_hashes,
        )
        self.assertEqual(errors, [])
        receipt["method_step_hashes"] = {"m": {"m.step-001": "stale-hash"}}
        write_json(receipt_path, receipt)
        errors = []
        VALIDATOR.load_receipt(
            receipt_path,
            "independent-verification/v1",
            "atoms-sha",
            "run-1",
            "whole-file-sha-not-required",
            methods,
            errors,
            step_hashes,
        )
        self.assertTrue(any("步骤内容指纹" in error for error in errors), errors)

    def test_v1_recipe_steps_keep_whole_file_receipt_binding(self) -> None:
        methods = {"m": {"steps": [{"step_id": "m.step-01"}]}}
        self.assertIsNone(VALIDATOR.method_step_hash_map(methods))

    def test_formal_mode_rejects_pilot_package(self) -> None:
        package_path = Path(self.temp.name) / "accepted-package.json"
        package = {
            "schema_version": "accepted-package/v1",
            "package_id": "fixture-pilot-package",
            "artifact_scope": "PILOT_TEMP",
            "distillation_allowed": False,
            "book": {
                "book_id": "fixture-bphs-97",
                "edition_id": "fixture-santhanam-97-chapter",
                "source_artifact_id": "fixture-source",
            },
            "evidence_atoms": {
                "path": str(FIXTURE.parent / "_chunk_bphs97_stage3_v7_20260814" / "evidence_atoms.jsonl"),
                "content_sha256": "f4800a67c985246ba3d5103570341c6fb977c83c15a48e94abe738edd0955443",
                "contract_version": "fixture-evidence-atoms-v7",
            },
            "upstream_gates": {
                "source_text_bidirectional": "pass",
                "chunking_validation": "pass",
                "accepted": "pass",
            },
        }
        write_json(package_path, package)
        work_path = self.root / "WORK_ORDER.json"
        work = read_json(work_path)
        work["artifact_scope"] = "FORMAL"
        work["pilot_only"] = False
        work["input"] = {
            "accepted_package_path": str(package_path),
            "chapter_scope": [11],
            "evidence_atom_scope": [],
        }
        write_json(work_path, work)
        self.assert_error("正式模式拒绝 PILOT_TEMP 输入")


if __name__ == "__main__":
    unittest.main()
