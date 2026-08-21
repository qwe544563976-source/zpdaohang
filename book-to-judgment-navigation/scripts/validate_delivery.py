#!/usr/bin/env python3
"""Validate frozen-evidence-atom judgment-navigation deliveries."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import random
import re
import sys
from collections import Counter
from pathlib import Path


ADAPTER_PATH = Path(__file__).with_name("adapt_jh8_facts.py")
ADAPTER_SPEC = importlib.util.spec_from_file_location("judgment_navigation_fact_adapter", ADAPTER_PATH)
if ADAPTER_SPEC is None or ADAPTER_SPEC.loader is None:
    raise RuntimeError(f"无法加载事实运行逻辑：{ADAPTER_PATH}")
ADAPTER_MODULE = importlib.util.module_from_spec(ADAPTER_SPEC)
ADAPTER_SPEC.loader.exec_module(ADAPTER_MODULE)
_conditional_missing_facts = ADAPTER_MODULE._conditional_missing_facts
_condition_state = ADAPTER_MODULE._condition_state


FORBIDDEN_TOKENS = (
    "work_id",
    "parent_id",
    "card_id",
    "source_atom_ids",
    "filters.work_ids",
    "contract_v2.1",
)
FORBIDDEN_FIELD_NAMES = {"work_id", "parent_id", "card_id", "source_atom_ids"}
METHOD_EVIDENCE_CONTENT_ROLES = {"verse", "prose", "table"}
REQUIRED_ATOM_FIELDS = {
    "evidence_atom_id",
    "chapter_number",
    "chapter_title",
    "heading_path",
    "content_role",
    "exact_text",
    "pdf_pages",
    "citation",
}
REQUIRED_METHOD_FIELDS = {
    "method",
    "title",
    "pilot_only",
    "publishable",
    "workflow_status",
    "workflow_history",
    "source_status",
    "fact_binding_status",
    "upstream_issue_ids",
    "user_intents",
    "required_facts",
    "conditional_facts",
    "dependencies",
    "steps",
    "retrieval_plan",
    "stop_conditions",
    "executable_in_pilot",
}
REQUIRED_TOPIC_FIELDS = {
    "title",
    "user_intents",
    "method_ids",
    "candidate_method_ids",
    "execution_allowed",
    "required_facts",
    "conditional_facts",
    "fact_binding_status",
    "support_queries",
    "counter_queries",
    "boundary_queries",
    "method_queries",
    "stop_conditions",
}
REQUIRED_STEP_FIELDS = {
    "step_id",
    "action",
    "produced_fact_keys",
    "required_fact_keys",
    "condition_logic",
    "source_status",
    "evidence_refs",
    "stop_condition",
    "stop_fact_keys",
    "applicability_scope",
    "minimum_supported_claim",
    "exception_relations",
    "forbidden_extensions",
}
# claim_terms 是 v2 升级后新装配的步骤才有的字段，刻意不列为必填：
# 已并入总账的旧方法在装配时没有保留它，且原始映射已无处回填。
# 没有它时 OR 闸门保持升级前的严格行为（见 or_outside_results）。
QUERY_LANES = (
    "support_queries",
    "counter_queries",
    "boundary_queries",
    "method_queries",
)
SOURCE_STATUSES = {
    "repeated_support",
    "single_explicit_source",
    "structure_hint_only",
    "synthesized_candidate",
    "no_source_in_scope",
}
EXCEPTION_RELATION_TYPES = {"exception", "cancellation", "mitigation", "limitation"}
GENERALIZATION_SCOPES = {"general_rule", "single_case_only"}
_SHARED_SPEC = importlib.util.spec_from_file_location(
    "b2jn_shared_constants", Path(__file__).resolve().with_name("shared_constants.py")
)
assert _SHARED_SPEC and _SHARED_SPEC.loader
shared_constants = importlib.util.module_from_spec(_SHARED_SPEC)
_SHARED_SPEC.loader.exec_module(shared_constants)

EMPTY_CLAIM_FRAGMENTS = shared_constants.EMPTY_CLAIM_FRAGMENTS
PLACEHOLDER_FACT_PATTERNS = shared_constants.PLACEHOLDER_FACT_PATTERNS
GENERATOR_ID = shared_constants.GENERATOR_ID
compute_step_hash = shared_constants.compute_step_hash
detect_high_risk_terms = shared_constants.detect_high_risk_terms
normalize_for_term_match = shared_constants.normalize_for_term_match
EXPLICIT_OR_PATTERN = re.compile(
    r"\band/or\b|\beither\b[^.!?;\n]{0,240}\bor\b|"
    r"\b(?:if|when|whether)\b[^,;.!?\n]{0,240}\bor\b|"
    r"(?:^|\n)\s*should\b[^,;.!?\n]{0,240}\bor\b|"
    r"\bor\s*,?\s*(?:if|when|should|in|at|from)\b",
    flags=re.IGNORECASE,
)
ATOM_DISPOSITIONS = {
    "method_step",
    "method_candidate",
    "knowledge_only",
    "case_or_auxiliary",
    "upstream_issue_blocked",
    "reviewed_no_method",
    "review_pending",
}
METHOD_BEARING_SEMANTIC_CLASSES = {
    "judgment_method",
    "condition_result",
    "exception_boundary",
    "calculation_rule",
}
SEMANTIC_CLASSES = {
    "judgment_method",
    "condition_result",
    "exception_boundary",
    "calculation_rule",
    "foundational_knowledge",
    "case_or_commentary",
    "unresolved_source",
}
WORKFLOW_STATUSES = {
    "pilot_candidate",
    "mechanical_verified",
    "independent_verified",
    "shadow_passed",
    "pilot_passed",
    "blocked",
    "rejected",
}
EXECUTABLE_SOURCE_STATUSES = {"repeated_support", "single_explicit_source"}
FACT_BINDING_STATUSES = {"unmapped", "mapped", "unavailable"}
WORKFLOW_TRANSITIONS = {
    "pilot_candidate": {"mechanical_verified", "blocked", "rejected"},
    "mechanical_verified": {"independent_verified", "blocked", "rejected"},
    "independent_verified": {"shadow_passed", "blocked", "rejected"},
    "shadow_passed": {"pilot_passed", "blocked", "rejected"},
    "pilot_passed": set(),
    "blocked": set(),
    "rejected": set(),
}
INDEPENDENT_OR_LATER = {"independent_verified", "shadow_passed", "pilot_passed"}


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"无法读取 JSON：{path}：{exc}")
        return {}
    if not isinstance(data, dict):
        errors.append(f"JSON 顶层必须是对象：{path}")
        return {}
    return data


def json_text(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_pilot_status(root: Path, work_order: dict, errors: list[str]) -> dict:
    status = load_json(root / "PILOT_STATUS.json", errors)
    expected = {
        "artifact_scope": "PILOT_TEMP",
        "pilot_only": True,
        "publishable": False,
        "formal_migration": "FORBIDDEN",
        "superseded_on_formal_atoms": True,
        "formal_dependency": "accepted-package.json",
        "formal_dependency_status": "missing",
    }
    for field, value in expected.items():
        if status.get(field) != value:
            errors.append(f"PILOT_STATUS.json 字段不合法：{field}")
    for field in ("independent_verification_allowed", "shadow_allowed"):
        if not isinstance(status.get(field), bool):
            errors.append(f"PILOT_STATUS.json 字段必须是布尔值：{field}")
    allowed_uses = status.get("allowed_uses")
    forbidden_uses = status.get("forbidden_uses")
    if not non_empty_list(allowed_uses) or "validator_regression_tests" not in allowed_uses:
        errors.append("PILOT_STATUS.json 没有允许验证器回归测试")
    if not non_empty_list(forbidden_uses) or any(
        value not in forbidden_uses
        for value in ("formal_navigation", "temporary_id_migration", "production_agent_execution")
    ):
        errors.append("PILOT_STATUS.json 没有完整禁止正式导航、编号迁移和生产执行")
    if work_order.get("accepted_package") is not None:
        errors.append("PILOT_TEMP 工作单不得绑定正式已验收书包")
    if work_order.get("formal_migration") != "FORBIDDEN":
        errors.append("PILOT_TEMP 工作单必须禁止正式迁移")
    if work_order.get("mechanical_gate_status") != status.get("mechanical_gate_status"):
        errors.append("工作单与 PILOT_STATUS.json 的机械闸门状态不一致")
    return status


def load_accepted_package(path: Path, errors: list[str]) -> dict:
    package = load_json(path, errors)
    required = {
        "schema_version",
        "package_id",
        "artifact_scope",
        "distillation_allowed",
        "book",
        "evidence_atoms",
        "upstream_gates",
    }
    missing = required - set(package)
    if missing:
        errors.append(f"已验收书包凭证缺字段：{sorted(missing)}")
        return package
    if package.get("schema_version") != "accepted-package/v1":
        errors.append("已验收书包凭证版本不是 accepted-package/v1")
    if package.get("artifact_scope") != "FORMAL" or package.get("distillation_allowed") is not True:
        errors.append("正式已验收书包没有允许蒸馏")
    book = package.get("book")
    if not isinstance(book, dict) or not all(book.get(key) for key in ("book_id", "edition_id", "source_artifact_id")):
        errors.append("已验收书包缺少书籍、版本或源文件身份")
    evidence = package.get("evidence_atoms")
    if not isinstance(evidence, dict) or not all(evidence.get(key) for key in ("path", "content_sha256", "contract_version")):
        errors.append("已验收书包缺少原文原子路径、内容摘要或契约版本")
    gates = package.get("upstream_gates")
    if not isinstance(gates, dict) or any(
        gates.get(key) != "pass"
        for key in ("source_text_bidirectional", "chunking_validation", "accepted")
    ):
        errors.append("已验收书包的上游闸门没有全部通过")
    return package


def resolve_input(
    root: Path, work_order: dict, errors: list[str]
) -> tuple[Path | None, str | None, str | None, dict | None, dict]:
    artifact_scope = work_order.get("artifact_scope")
    input_data = work_order.get("input")
    input_data = input_data if isinstance(input_data, dict) else {}
    package_id: str | None = None

    if artifact_scope == "PILOT_TEMP":
        pilot_status = validate_pilot_status(root, work_order, errors)
        source_path_text = input_data.get("evidence_atoms_path")
        source_path = Path(source_path_text) if isinstance(source_path_text, str) and source_path_text else None
        if source_path is not None and not source_path.is_absolute():
            errors.append("PILOT_TEMP 原文原子路径必须是绝对路径")
        snapshot = input_data.get("source_snapshot")
        snapshot = snapshot if isinstance(snapshot, dict) else {}
        expected_sha = snapshot.get("content_sha256")
        if not isinstance(expected_sha, str) or not expected_sha:
            errors.append("PILOT_TEMP 输入快照缺少 content_sha256")
        return (
            source_path,
            expected_sha if isinstance(expected_sha, str) else None,
            package_id,
            None,
            pilot_status,
        )

    if artifact_scope == "FORMAL":
        if "evidence_atoms_path" in input_data or "source_snapshot" in input_data:
            errors.append("正式模式拒绝裸 evidence_atoms.jsonl 路径和本地快照")
        package_path_text = input_data.get("accepted_package_path")
        package_path = Path(package_path_text) if isinstance(package_path_text, str) and package_path_text else None
        if package_path is not None and not package_path.is_absolute():
            errors.append("正式已验收书包路径必须是绝对路径")
        if package_path is None or not package_path.is_file():
            errors.append(f"正式模式缺少 accepted-package.json：{package_path_text}")
            return None, None, None, None, {}
        package = load_accepted_package(package_path, errors)
        if package.get("artifact_scope") == "PILOT_TEMP":
            errors.append("正式模式拒绝 PILOT_TEMP 输入")
        evidence = package.get("evidence_atoms")
        evidence = evidence if isinstance(evidence, dict) else {}
        source_path_text = evidence.get("path")
        source_path = Path(source_path_text) if isinstance(source_path_text, str) and source_path_text else None
        if source_path is not None and not source_path.is_absolute():
            errors.append("正式原文原子路径必须是绝对路径")
        package_id = package.get("package_id") if isinstance(package.get("package_id"), str) else None
        expected_sha = evidence.get("content_sha256")
        return (
            source_path,
            expected_sha if isinstance(expected_sha, str) else None,
            package_id,
            package,
            {},
        )

    errors.append("工作单 artifact_scope 必须是 PILOT_TEMP 或 FORMAL")
    return None, None, None, None, {}


def validate_distillation_source(
    root: Path,
    work_order: dict,
    source_path: Path | None,
    source_sha: str | None,
    package_id: str | None,
    package: dict | None,
    errors: list[str],
) -> None:
    manifest = load_json(root / "DISTILLATION_SOURCE.json", errors)
    required = {
        "distillation_run_id",
        "artifact_scope",
        "pilot_only",
        "publishable",
        "book_id",
        "edition_id",
        "source_artifact_id",
        "accepted_package_id",
        "accepted_package_path",
        "evidence_contract_version",
        "evidence_atoms_path",
        "evidence_atoms_sha256",
        "chapter_scope",
        "created_at",
    }
    missing = required - set(manifest)
    if missing:
        errors.append(f"蒸馏来源清单缺字段：{sorted(missing)}")
    if manifest.get("artifact_scope") != work_order.get("artifact_scope"):
        errors.append("蒸馏来源清单与工作单的产物身份不一致")
    if manifest.get("pilot_only") is not work_order.get("pilot_only"):
        errors.append("蒸馏来源清单 pilot_only 不一致")
    if manifest.get("publishable") is not work_order.get("publishable"):
        errors.append("蒸馏来源清单 publishable 不一致")
    if source_sha and manifest.get("evidence_atoms_sha256") != source_sha:
        errors.append("蒸馏来源清单没有绑定当前原文原子内容摘要")
    manifest_source = manifest.get("evidence_atoms_path")
    if source_path is not None and (
        not isinstance(manifest_source, str)
        or Path(manifest_source).resolve() != source_path.resolve()
    ):
        errors.append("蒸馏来源清单没有绑定本次实际读取的原文原子路径")
    if not all(manifest.get(key) for key in ("distillation_run_id", "book_id", "edition_id", "source_artifact_id", "evidence_contract_version", "evidence_atoms_path", "created_at")):
        errors.append("蒸馏来源清单缺少非空的运行、书籍、版本、源文件或原文原子身份")
    input_data = work_order.get("input")
    input_data = input_data if isinstance(input_data, dict) else {}
    if manifest.get("chapter_scope") != input_data.get("chapter_scope"):
        errors.append("蒸馏来源清单与工作单的章节范围不一致")
    if work_order.get("artifact_scope") == "FORMAL":
        if manifest.get("accepted_package_id") != package_id:
            errors.append("正式蒸馏来源清单没有绑定当前已验收书包")
        input_data = work_order.get("input")
        input_data = input_data if isinstance(input_data, dict) else {}
        manifest_package_path = manifest.get("accepted_package_path")
        input_package_path = input_data.get("accepted_package_path")
        if (
            not isinstance(manifest_package_path, str)
            or not isinstance(input_package_path, str)
            or Path(manifest_package_path).resolve() != Path(input_package_path).resolve()
        ):
            errors.append("正式蒸馏来源清单没有绑定本次实际读取的已验收书包路径")
        package = package if isinstance(package, dict) else {}
        book = package.get("book")
        book = book if isinstance(book, dict) else {}
        for field in ("book_id", "edition_id", "source_artifact_id"):
            if manifest.get(field) != book.get(field):
                errors.append(f"正式蒸馏来源清单的 {field} 与已验收书包不一致")
        evidence = package.get("evidence_atoms")
        evidence = evidence if isinstance(evidence, dict) else {}
        if manifest.get("evidence_contract_version") != evidence.get("contract_version"):
            errors.append("蒸馏来源清单的原文原子契约版本不一致")
    elif manifest.get("accepted_package_id") is not None or manifest.get("accepted_package_path") is not None:
        errors.append("PILOT_TEMP 蒸馏来源清单不得绑定正式书包")


def non_empty_list(value: object) -> bool:
    return isinstance(value, list) and bool(value)


def load_scoped_atoms(
    path: Path,
    chapter_scope: set[int],
    atom_scope: set[str],
    errors: list[str],
) -> dict[str, dict]:
    atoms: dict[str, dict] = {}
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                try:
                    atom = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"原文原子第 {line_number} 行不是有效 JSON：{exc}")
                    continue
                if not isinstance(atom, dict):
                    continue
                atom_id = atom.get("evidence_atom_id")
                in_scope = (
                    isinstance(atom_id, str)
                    and (
                        atom_id in atom_scope
                        or (
                            isinstance(atom.get("chapter_number"), int)
                            and atom["chapter_number"] in chapter_scope
                        )
                    )
                )
                if not in_scope:
                    continue
                missing = REQUIRED_ATOM_FIELDS - set(atom)
                if missing:
                    errors.append(f"原文原子 {atom_id or line_number} 缺字段：{sorted(missing)}")
                    continue
                if atom_id in atoms:
                    errors.append(f"允许范围内出现重复原文编号：{atom_id}")
                    continue
                atoms[atom_id] = atom
    except OSError as exc:
        errors.append(f"无法读取原文原子文件：{path}：{exc}")
    return atoms


def check_json_flags(root: Path, pilot_only: bool, publishable: bool, errors: list[str]) -> None:
    for path in root.rglob("*.json"):
        relative_parts = path.relative_to(root).parts
        if "validation" in relative_parts or "backups" in relative_parts:
            continue
        data = load_json(path, errors)
        if not data:
            continue
        if data.get("pilot_only") is not pilot_only:
            errors.append(f"机器文件 pilot_only 不一致：{path}")
        if data.get("publishable") is not publishable:
            errors.append(f"机器文件 publishable 不一致：{path}")


def check_forbidden_tokens(root: Path, errors: list[str]) -> None:
    paths = [root / "SKILL.md", root / "WORK_ORDER.json", root / "PIPELINE_STATE.md"]
    paths.extend(
        path
        for path in (root / "references").rglob("*.md")
        if "backups" not in path.relative_to(root).parts
    )
    paths.extend(
        path
        for path in (root / "references").rglob("*.json")
        if "backups" not in path.relative_to(root).parts
    )
    paths.extend(
        path
        for path in (root / "methods").rglob("*.md")
        if "backups" not in path.relative_to(root).parts
    )
    paths.extend(
        path
        for path in (root / "methods").rglob("*.json")
        if "backups" not in path.relative_to(root).parts
    )
    for path in paths:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        found_tokens: set[str] = set()
        if path.suffix == ".json":
            try:
                data = json.loads(text)
            except json.JSONDecodeError:
                data = None

            def inspect_fields(value: object, field_path: tuple[str, ...] = ()) -> None:
                if isinstance(value, dict):
                    for key, child in value.items():
                        current_path = field_path + (key,)
                        token = None
                        if key in FORBIDDEN_FIELD_NAMES:
                            token = key
                        elif len(current_path) >= 2 and current_path[-2:] == ("filters", "work_ids"):
                            token = "filters.work_ids"
                        if token and token not in found_tokens:
                            errors.append(f"新产物包含退役字段 {token}：{path}")
                            found_tokens.add(token)
                        inspect_fields(child, current_path)
                elif isinstance(value, list):
                    for child in value:
                        inspect_fields(child, field_path)

            inspect_fields(data)
        for token in FORBIDDEN_TOKENS:
            if token in text and token not in found_tokens:
                errors.append(f"新产物包含退役字段 {token}：{path}")


def iter_evidence_atom_ids(value: object, label: str):
    if isinstance(value, dict):
        for key, child in value.items():
            child_label = f"{label}.{key}"
            if key == "evidence_atom_id":
                yield child_label, child
            elif key == "evidence_atom_ids":
                if isinstance(child, list):
                    for index, atom_id in enumerate(child, 1):
                        yield f"{child_label}[{index}]", atom_id
                else:
                    yield child_label, child
            else:
                yield from iter_evidence_atom_ids(child, child_label)
    elif isinstance(value, list):
        for index, child in enumerate(value, 1):
            yield from iter_evidence_atom_ids(child, f"{label}[{index}]")


def validate_knowledge_maps(root: Path, atoms: dict[str, dict], errors: list[str]) -> None:
    knowledge = root / "references" / "knowledge"
    files = {
        "chapter-map.json": ("chapters", list),
        "topic-map.json": ("topics", dict),
        "glossary.json": ("terms", list),
    }
    for filename, (collection_name, collection_type) in files.items():
        path = knowledge / filename
        data = load_json(path, errors)
        collection = data.get(collection_name)
        if not isinstance(collection, collection_type) or not collection:
            errors.append(f"知识地图 {filename} 缺少非空 {collection_name}")
            continue
        entries = collection.values() if isinstance(collection, dict) else collection
        for index, entry in enumerate(entries, 1):
            if not isinstance(entry, dict) or not non_empty_list(entry.get("evidence_atom_ids")):
                errors.append(f"知识地图 {filename} 第 {index} 项缺少原文编号")
        for label, atom_id in iter_evidence_atom_ids(data, filename):
            if not isinstance(atom_id, str) or not atom_id:
                errors.append(f"知识地图原文编号必须是非空字符串：{label}")
            elif atom_id not in atoms:
                errors.append(f"知识地图引用了范围外或不存在的原文编号：{atom_id}（{label}）")
        if filename == "chapter-map.json" and isinstance(collection, list):
            mapped_ids = [
                atom_id
                for entry in collection
                if isinstance(entry, dict)
                for atom_id in entry.get("evidence_atom_ids", [])
                if isinstance(atom_id, str) and atom_id
            ]
            missing_ids = set(atoms) - set(mapped_ids)
            if missing_ids:
                errors.append(
                    "章节地图遗漏允许范围内的原文编号："
                    + ", ".join(sorted(missing_ids))
                )
            seen_ids: set[str] = set()
            duplicate_ids: set[str] = set()
            for atom_id in mapped_ids:
                if atom_id in seen_ids:
                    duplicate_ids.add(atom_id)
                seen_ids.add(atom_id)
            if duplicate_ids:
                errors.append("章节地图重复收录原文编号：" + ", ".join(sorted(duplicate_ids)))


def validate_method_source_scan(
    root: Path,
    atoms: dict[str, dict],
    methods: dict[str, dict],
    issues: dict[str, dict],
    errors: list[str],
) -> None:
    path = root / "validation" / "method-source-scan.json"
    data = load_json(path, errors)
    if data.get("pilot_only") is not root.joinpath("PILOT_STATUS.json").is_file():
        errors.append(f"方法审查清单 pilot_only 与运行范围不一致：{path}")
    if data.get("publishable") is True:
        errors.append(f"方法审查清单不能标记为可发布：{path}")
    review_status = data.get("review_status")
    if review_status not in (None, "in_progress", "complete"):
        errors.append(f"方法审查清单 review_status 不合法：{review_status}")
    records = data.get("atom_dispositions")
    if not isinstance(records, list) or not records:
        errors.append(f"方法审查清单缺少非空 atom_dispositions：{path}")
        return

    used_by: dict[str, set[str]] = {}
    for method_id, method in methods.items():
        for step in method.get("steps", []):
            if not isinstance(step, dict):
                continue
            for ref in step.get("evidence_refs", []):
                if isinstance(ref, dict) and isinstance(ref.get("evidence_atom_id"), str):
                    used_by.setdefault(ref["evidence_atom_id"], set()).add(method_id)

    seen: set[str] = set()
    duplicates: set[str] = set()
    for index, record in enumerate(records, 1):
        label = f"方法审查清单第 {index} 项"
        if not isinstance(record, dict):
            errors.append(f"{label} 必须是对象")
            continue
        atom_id = record.get("evidence_atom_id")
        disposition = record.get("disposition")
        if not isinstance(atom_id, str) or not atom_id:
            errors.append(f"{label} 缺少 evidence_atom_id")
            continue
        if atom_id in seen:
            duplicates.add(atom_id)
        seen.add(atom_id)
        if atom_id not in atoms:
            errors.append(f"{label} 引用了范围外或不存在的原文编号：{atom_id}")
        if disposition not in ATOM_DISPOSITIONS:
            errors.append(f"{label} 的 disposition 不合法：{disposition}")
        if disposition == "review_pending":
            errors.append(f"原文尚未完成方法语义审查，不能通过：{atom_id}")
        semantic_class = record.get("semantic_class")
        risk_flags = record.get("risk_flags")
        if semantic_class is None:
            errors.append(f"原文缺少 semantic_class：{atom_id}")
        if semantic_class is not None and semantic_class not in SEMANTIC_CLASSES:
            errors.append(f"原文 semantic_class 不合法：{atom_id} → {semantic_class}")
        if risk_flags is None:
            errors.append(f"原文缺少 risk_flags：{atom_id}")
        if risk_flags is not None and (
            not isinstance(risk_flags, list)
            or any(not isinstance(value, str) or not value for value in risk_flags)
            or len(risk_flags) != len(set(risk_flags))
        ):
            errors.append(f"原文 risk_flags 必须是无重复的字符串数组：{atom_id}")
        if semantic_class == "case_or_commentary" and disposition == "method_step":
            errors.append(f"案例、译注或编辑说明不能进入通用方法步骤：{atom_id}")
        if semantic_class == "unresolved_source" and disposition == "method_step":
            errors.append(f"残缺或身份混合的原文不能进入方法步骤：{atom_id}")
        method_ids = record.get("method_ids", [])
        if not isinstance(method_ids, list) or any(not isinstance(value, str) or not value for value in method_ids):
            errors.append(f"{label} 的 method_ids 必须是字符串数组")
            method_ids = []
        if disposition == "method_step":
            if not method_ids:
                errors.append(f"{label} 标记为 method_step 但没有 method_ids：{atom_id}")
            for method_id in method_ids:
                if method_id not in methods:
                    errors.append(f"{label} 引用了不存在的方法：{method_id}")
                elif method_id not in used_by.get(atom_id, set()):
                    errors.append(f"{label} 标记的方法没有实际引用原文：{atom_id} → {method_id}")
        elif disposition == "method_candidate":
            if method_ids:
                errors.append(f"{label} 标记为 method_candidate 时不得填写 method_ids：{atom_id}")
            if semantic_class not in METHOD_BEARING_SEMANTIC_CLASSES:
                errors.append(f"方法候选的 semantic_class 不是方法或规则类型：{atom_id}")
            errors.append(f"方法候选尚未完成方法生产，不能通过：{atom_id}")
        elif method_ids:
            errors.append(f"{label} 非 method_step 不得填写 method_ids：{atom_id}")
        if disposition == "upstream_issue_blocked":
            if not any(
                issue.get("evidence_atom_id") == atom_id
                and issue.get("status") == "open"
                and issue.get("blocking") is True
                for issue in issues.values()
            ):
                errors.append(f"{label} 标记为上游阻塞但没有对应的开放阻塞问题：{atom_id}")

    if duplicates:
        errors.append("方法审查清单重复收录原文编号：" + ", ".join(sorted(duplicates)))
    missing = set(atoms) - seen
    if missing:
        errors.append("方法审查清单遗漏允许范围内的原文编号：" + ", ".join(sorted(missing)))
    extra = seen - set(atoms)
    if extra:
        errors.append("方法审查清单包含范围外原文编号：" + ", ".join(sorted(extra)))
    for atom_id, method_ids in used_by.items():
        matching = [
            record for record in records
            if isinstance(record, dict)
            and record.get("evidence_atom_id") == atom_id
            and record.get("disposition") == "method_step"
        ]
        declared = {
            method_id
            for record in matching
            for method_id in record.get("method_ids", [])
            if isinstance(method_id, str)
        }
        if declared != method_ids:
            errors.append(
                f"方法审查清单与实际步骤引用不一致：{atom_id}"
            )


def load_upstream_issues(root: Path, atoms: dict[str, dict], errors: list[str]) -> tuple[dict, dict[str, dict]]:
    data = load_json(root / "UPSTREAM_ISSUES.json", errors)
    issues = data.get("issues")
    issues = issues if isinstance(issues, list) else []
    by_id: dict[str, dict] = {}
    required = {
        "issue_id",
        "evidence_atom_id",
        "issue_type",
        "impact",
        "blocking",
        "blocking_stage",
        "status",
        "affected_method_ids",
    }
    for index, issue in enumerate(issues, 1):
        if not isinstance(issue, dict):
            errors.append(f"上游问题第 {index} 项必须是对象")
            continue
        missing = required - set(issue)
        if missing:
            errors.append(f"上游问题第 {index} 项缺字段：{sorted(missing)}")
            continue
        issue_id = issue.get("issue_id")
        if not isinstance(issue_id, str) or not issue_id:
            errors.append(f"上游问题第 {index} 项缺少 issue_id")
            continue
        if issue_id in by_id:
            errors.append(f"上游问题编号重复：{issue_id}")
        by_id[issue_id] = issue
        if issue.get("evidence_atom_id") not in atoms:
            errors.append(f"上游问题引用不存在的原文编号：{issue.get('evidence_atom_id')}")
        if issue.get("status") != "open":
            errors.append(
                f"蒸馏窗口不得把上游问题标记为已解决：{issue_id}；"
                "只能等待新的 accepted-package.json 后重新运行"
            )
        if not isinstance(issue.get("blocking"), bool):
            errors.append(f"上游问题 blocking 必须是布尔值：{issue_id}")
        for field in ("issue_type", "impact", "blocking_stage"):
            if not isinstance(issue.get(field), str) or not issue.get(field):
                errors.append(f"上游问题 {issue_id} 缺少非空 {field}")
        affected_method_ids = issue.get("affected_method_ids")
        if (
            not isinstance(affected_method_ids, list)
            or any(not isinstance(method_id, str) or not method_id for method_id in affected_method_ids)
        ):
            errors.append(f"上游问题 {issue_id} 的 affected_method_ids 必须是字符串数组")
    return data, by_id


def validate_workflow_history(label: str, item: dict, errors: list[str]) -> None:
    history = item.get("workflow_history")
    status = item.get("workflow_status")
    if not isinstance(history, list) or not history:
        errors.append(f"{label} 缺少非空 workflow_history")
        return
    if any(entry not in WORKFLOW_STATUSES for entry in history):
        errors.append(f"{label} 的 workflow_history 含非法状态")
        return
    if history[0] != "pilot_candidate":
        errors.append(f"{label} 的 workflow_history 必须从 pilot_candidate 开始")
    if history[-1] != status:
        errors.append(f"{label} 的 workflow_status 与 workflow_history 末项不一致")
    for previous, current in zip(history, history[1:]):
        if current not in WORKFLOW_TRANSITIONS.get(previous, set()):
            errors.append(f"{label} 的状态跳级：{previous} → {current}")


def bullet_list(values: object, empty_text: str = "无") -> str:
    if not isinstance(values, list) or not values:
        return f"- {empty_text}\n"
    return "".join(f"- {value}\n" for value in values)


def render_method_markdown(item: dict) -> str:
    lines = [
        "---",
        f"method: {item.get('method', '')}",
        f"workflow_status: {item.get('workflow_status', '')}",
        f"source_status: {item.get('source_status', '')}",
        f"fact_binding_status: {item.get('fact_binding_status', '')}",
        f"executable_in_pilot: {str(item.get('executable_in_pilot') is True).lower()}",
        f"pilot_only: {str(item.get('pilot_only') is True).lower()}",
        f"publishable: {str(item.get('publishable') is True).lower()}",
        "---",
        "",
        f"# {item.get('title', '')}",
        "",
        "> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。",
        "",
        "## 适用问题",
        "",
        bullet_list(item.get("user_intents")).rstrip(),
        "",
        "## 来源与事实接入",
        "",
        f"- 来源状态：`{item.get('source_status', '')}`",
        f"- 事实接入状态：`{item.get('fact_binding_status', '')}`",
        f"- 当前状态：`{item.get('workflow_status', '')}`",
        f"- 允许执行：`{str(item.get('executable_in_pilot') is True).lower()}`",
        f"- 允许发布：`{str(item.get('publishable') is True).lower()}`",
        "",
        "## 必查事实",
        "",
        bullet_list(item.get("required_facts")).rstrip(),
        "",
        "## 按情况检查的事实",
        "",
        bullet_list(item.get("conditional_facts")).rstrip(),
        "",
        "## 依赖方法",
        "",
        bullet_list(item.get("dependencies")).rstrip(),
        "",
        "## 执行步骤",
        "",
    ]
    steps = item.get("steps")
    if not isinstance(steps, list) or not steps:
        lines.append("- 当前机器配方没有可执行步骤。")
    else:
        for step in steps:
            lines.extend([
                f"### {step.get('step_id', '')}",
                "",
                f"- 动作：{step.get('action', '')}",
                f"- 适用范围：{step.get('applicability_scope', '')}",
                f"- 原文最小意思：{step.get('minimum_supported_claim', '')}",
                f"- 本步骤产出事实：{json.dumps(step.get('produced_fact_keys', []), ensure_ascii=False)}",
                f"- 所需事实：{json.dumps(step.get('required_fact_keys', []), ensure_ascii=False)}",
                f"- 条件关系：{json.dumps(step.get('condition_logic', {}), ensure_ascii=False)}",
                f"- 按分支必查事实：{json.dumps(step.get('conditional_fact_requirements', []), ensure_ascii=False)}",
                f"- 例外、取消或缓解：{json.dumps(step.get('exception_relations', []), ensure_ascii=False)}",
                f"- 禁止扩大：{json.dumps(step.get('forbidden_extensions', []), ensure_ascii=False)}",
                f"- 来源状态：`{step.get('source_status', '')}`",
                f"- 停止条件：{step.get('stop_condition', '')}",
                f"- 缺失即停字段：{json.dumps(step.get('stop_fact_keys', []), ensure_ascii=False)}",
                "- 原文证据：",
            ])
            refs = step.get("evidence_refs")
            if not isinstance(refs, list) or not refs:
                lines.append("  - 无")
            else:
                for ref in refs:
                    quote = str(ref.get("quote", "")).replace("\n", " ")
                    lines.append(
                        f"  - `{ref.get('evidence_atom_id', '')}`｜PDF {json.dumps(ref.get('pdf_pages', []), ensure_ascii=False)}｜“{quote}”"
                    )
            lines.append("")
    plan = item.get("retrieval_plan")
    plan = plan if isinstance(plan, dict) else {}
    lane_titles = {
        "support_queries": "支持路",
        "counter_queries": "反例或取消路",
        "boundary_queries": "适用边界路",
        "method_queries": "判断方法路",
    }
    lines.extend(["", "## 四路查书计划", ""])
    for lane in QUERY_LANES:
        lines.extend([f"### {lane_titles[lane]}", "", bullet_list(plan.get(lane)).rstrip(), ""])
    lines.extend([
        "## 上游问题",
        "",
        bullet_list(item.get("upstream_issue_ids")).rstrip(),
        "",
        "## 停止条件",
        "",
        bullet_list(item.get("stop_conditions")).rstrip(),
        "",
        "## 固定边界",
        "",
        "- 本文件只展示机器配方，不是原文证据。",
        "- 原文必须在运行时由原文证据检索系统重新取回。",
        "- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。",
        "- 试验产物禁止迁移编号、手改转正或正式发布。",
        "",
    ])
    return "\n".join(lines)


def render_topic_markdown(name: str, item: dict) -> str:
    lane_titles = {
        "support_queries": "支持路",
        "counter_queries": "反例或取消路",
        "boundary_queries": "适用边界路",
        "method_queries": "判断方法路",
    }
    lines = [
        f"# {item.get('title', name)}",
        "",
        "> 本文件由 `query-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变路由或执行许可。",
        "",
        "## 用户会怎样问",
        "",
        bullet_list(item.get("user_intents")).rstrip(),
        "",
        "## 方法路由",
        "",
        f"- 可执行方法：{json.dumps(item.get('method_ids', []), ensure_ascii=False)}",
        f"- 候选方法：{json.dumps(item.get('candidate_method_ids', []), ensure_ascii=False)}",
        f"- 事实接入状态：`{item.get('fact_binding_status', '')}`",
        f"- 允许执行：`{str(item.get('execution_allowed') is True).lower()}`",
        "",
        "## 必查事实",
        "",
        bullet_list(item.get("required_facts")).rstrip(),
        "",
        "## 按情况检查的事实",
        "",
        bullet_list(item.get("conditional_facts")).rstrip(),
        "",
        "## 四路查书计划",
        "",
    ]
    for lane in QUERY_LANES:
        lines.extend([f"### {lane_titles[lane]}", "", bullet_list(item.get(lane)).rstrip(), ""])
    lines.extend([
        "## 停止条件",
        "",
        bullet_list(item.get("stop_conditions")).rstrip(),
        "",
    ])
    return "\n".join(lines)


def render_method_map(methods: list[dict]) -> str:
    lines = [
        "# 方法地图",
        "",
        "> 本文件由 `method-recipes.json` 自动生成。",
        "",
        "| 方法 | 名称 | 状态 | 来源 | 事实接入 | 允许执行 |",
        "|---|---|---|---|---|---|",
    ]
    for item in methods:
        lines.append(
            f"| `{item.get('method', '')}` | {item.get('title', '')} | `{item.get('workflow_status', '')}` | "
            f"`{item.get('source_status', '')}` | `{item.get('fact_binding_status', '')}` | "
            f"{'是' if item.get('executable_in_pilot') is True else '否'} |"
        )
    lines.extend(["", "方法摘要和查询词不是原文证据；正式回答必须重新取回原文。", ""])
    return "\n".join(lines)


def render_verified_methods(methods: list[dict]) -> str:
    lines = [
        "# 方法核验状态",
        "",
        "> 本文件由 `method-recipes.json` 自动生成。状态不能靠手改本文件推进。",
        "",
        "| 方法 | 当前状态 | 上游问题 | 事实接入 | 允许执行 |",
        "|---|---|---|---|---|",
    ]
    for item in methods:
        issues = ", ".join(item.get("upstream_issue_ids", [])) or "无"
        lines.append(
            f"| {item.get('title', '')} | `{item.get('workflow_status', '')}` | {issues} | "
            f"`{item.get('fact_binding_status', '')}` | {'是' if item.get('executable_in_pilot') is True else '否'} |"
        )
    lines.extend(["", "独立核验凭证不存在时，不得把任何方法写成已经独立验证。", ""])
    return "\n".join(lines)


def render_upstream_issues(data: dict) -> str:
    lines = [
        "# 上游问题报告",
        "",
        "> 本文件由 `UPSTREAM_ISSUES.json` 自动生成。问题必须回到上游处理，本窗口不得改原文原子。",
        "",
    ]
    issues = data.get("issues")
    issues = issues if isinstance(issues, list) else []
    if not issues:
        lines.extend(["当前没有登记上游问题。", ""])
        return "\n".join(lines)
    for issue in issues:
        lines.extend([
            f"## {issue.get('issue_id', '')}",
            "",
            f"- 原文证据编号：`{issue.get('evidence_atom_id', '')}`",
            f"- 问题类型：`{issue.get('issue_type', '')}`",
            f"- 状态：`{issue.get('status', '')}`",
            f"- 是否阻塞：`{str(issue.get('blocking') is True).lower()}`",
            f"- 阻塞阶段：`{issue.get('blocking_stage', '')}`",
            f"- 影响：{issue.get('impact', '')}",
            f"- 受影响方法：{json.dumps(issue.get('affected_method_ids', []), ensure_ascii=False)}",
            "",
        ])
    return "\n".join(lines)


def derived_outputs(root: Path, method_data: dict, query_data: dict, issue_data: dict) -> dict[Path, str]:
    methods = method_data.get("methods")
    methods = methods if isinstance(methods, list) else []
    topics = query_data.get("topics")
    topics = topics if isinstance(topics, dict) else {}
    required_checks = {
        "pilot_only": query_data.get("pilot_only"),
        "publishable": query_data.get("publishable"),
        "topics": {
            name: {
                "question_type": item.get("title"),
                "required_facts": item.get("required_facts", []),
                "conditional_facts": item.get("conditional_facts", []),
                "fact_binding_status": item.get("fact_binding_status"),
                "stop_conditions": item.get("stop_conditions", []),
            }
            for name, item in topics.items()
            if isinstance(item, dict)
        },
    }
    outputs = {
        root / "references" / "navigation" / "required-checks.json": json_text(required_checks),
        root / "references" / "navigation" / "method-map.md": render_method_map(methods),
        root / "methods" / "verified.md": render_verified_methods(methods),
        root / "UPSTREAM_ISSUES.md": render_upstream_issues(issue_data),
    }
    for item in methods:
        if isinstance(item, dict) and isinstance(item.get("method"), str):
            outputs[root / "methods" / "families" / f"{item['method']}.md"] = render_method_markdown(item)
    for name, item in topics.items():
        if isinstance(item, dict):
            outputs[root / "references" / "navigation" / "topics" / f"{name}.md"] = render_topic_markdown(name, item)
    return outputs


def sync_derived_outputs(
    root: Path,
    method_data: dict,
    query_data: dict,
    issue_data: dict,
    errors: list[str],
    write: bool,
) -> int:
    outputs = derived_outputs(root, method_data, query_data, issue_data)
    for path, expected in outputs.items():
        if write:
            path.parent.mkdir(parents=True, exist_ok=True)
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                path.write_text(expected, encoding="utf-8")
            continue
        if not path.is_file():
            errors.append(f"缺少派生文件：{path}")
        elif path.read_text(encoding="utf-8") != expected:
            errors.append(f"派生文件与机器真相不一致，请运行 --render-derived：{path}")
    expected_method_files = {
        path for path in outputs if path.parent == root / "methods" / "families"
    }
    actual_method_files = set((root / "methods" / "families").glob("*.md"))
    if actual_method_files != expected_method_files:
        errors.append("methods/families 含有机器配方之外的文件或缺少派生文件")
    expected_topic_files = {
        path for path in outputs if path.parent == root / "references" / "navigation" / "topics"
    }
    actual_topic_files = set((root / "references" / "navigation" / "topics").glob("*.md"))
    if actual_topic_files != expected_topic_files:
        errors.append("topics 目录含有查询配方之外的文件或缺少派生文件")
    return len(outputs)


def check_evidence_ref(
    label: str,
    ref: object,
    atoms: dict[str, dict],
    errors: list[str],
    allowed_content_roles: set[str] = METHOD_EVIDENCE_CONTENT_ROLES,
) -> bool:
    if not isinstance(ref, dict):
        errors.append(f"{label} 的证据必须是对象")
        return False
    missing = {"evidence_atom_id", "quote", "pdf_pages"} - set(ref)
    if missing:
        errors.append(f"{label} 缺少证据三件套字段：{sorted(missing)}")
    atom_id = ref.get("evidence_atom_id")
    quote = ref.get("quote")
    pages = ref.get("pdf_pages")
    atom = atoms.get(atom_id) if isinstance(atom_id, str) else None
    if atom is None:
        errors.append(f"{label} 引用了范围外或不存在的原文编号：{atom_id}")
        return False
    valid = True
    content_role = atom.get("content_role")
    if content_role not in allowed_content_roles:
        errors.append(
            f"{label} 引用了 content_role={content_role} 的辅助材料，不能作为通用判断步骤证据：{atom_id}"
        )
        valid = False
    if not isinstance(quote, str) or not quote or quote not in atom["exact_text"]:
        errors.append(f"{label} 的逐字短引不在原文中：{atom_id}")
        valid = False
    if not isinstance(pages, list) or not pages:
        errors.append(f"{label} 缺少非空 PDF 页码：{atom_id}")
        valid = False
    elif pages != atom["pdf_pages"]:
        errors.append(f"{label} 的 PDF 页码与原文不一致：{atom_id}")
        valid = False
    return valid


NEGATION_SCOPE_PATTERN = re.compile(
    r"\b(devoid\s+of|without|free\s+from|bereft\s+of|not\s+(?:be\s+)?in)\b[^.]*$", re.I
)


def or_outside_results(source_text: str, step: dict) -> bool:
    """原文里的"或"是不是落在条件侧（落在条件侧才必须拆成 selection_group）。

    真实证据：BPHS97 ch14 v7-11 的 `loss of younger brothers and/or sisters`——
    这处 and/or 描述的是结果本身模糊（失去弟弟和/或妹妹），不是"要检查哪个分支"。
    旧闸门不分条件和结果，把这类步骤一律拦下；要通过就只能截断逐字短引，
    而截断正是已登记的"句尾碎片短引"错误家族。

    判据用方案 C 已经强制建立的条件词／结果词分离：命中的 OR 片段若整段落在
    某条结果映射引文里，就是结果侧的或；只要有一处落在结果引文之外，仍然要求拆分支。
    """
    claim_terms = step.get("claim_terms")
    result_quotes = []
    if isinstance(claim_terms, dict):
        result_quotes = [
            pair.get("quote", "")
            for pair in claim_terms.get("results", [])
            if isinstance(pair, dict) and isinstance(pair.get("quote"), str)
        ]
    for match in EXPLICIT_OR_PATTERN.finditer(source_text):
        if any(match.group(0) in quote for quote in result_quotes):
            continue
        # 否定辖域里的"或"是合取，不是任选（德摩根）：
        # `devoid of Yuti with and/or Drishti from malefics` ＝ 既不同宫也不被照，
        # 两个排除都要成立，正确写法是 AND 下两个 NOT，不该拆 selection_group。
        # 真实证据：ch36:v37 的 Lagn Adhi Yog。只认 OR 前同一小句里的显式否定引导词。
        prefix = source_text[max(0, match.start() - 60):match.start()]
        prefix = prefix.rsplit(".", 1)[-1].rsplit(",", 1)[-1]
        if NEGATION_SCOPE_PATTERN.search(prefix):
            continue
        return True
    return False


def validate_condition_logic(value: object, label: str, errors: list[str]) -> set[str]:
    if not isinstance(value, dict):
        errors.append(f"{label} 的 condition_logic 必须是对象")
        return set()
    if "fact_key" in value:
        fact_key = value.get("fact_key")
        if not isinstance(fact_key, str) or not fact_key:
            errors.append(f"{label} 的 condition_logic 含空事实字段")
            return set()
        return {fact_key}
    operator = value.get("operator")
    if operator not in {"AND", "OR", "NOT"}:
        errors.append(f"{label} 的 condition_logic 只允许 AND、OR 或 NOT")
        return set()
    operands = value.get("operands")
    if not isinstance(operands, list) or not operands:
        errors.append(f"{label} 的 condition_logic 缺少非空 operands")
        return set()
    if operator == "NOT" and len(operands) != 1:
        errors.append(f"{label} 的 NOT condition_logic 必须只有一个 operand")
    facts: set[str] = set()
    for index, operand in enumerate(operands, 1):
        facts.update(validate_condition_logic(operand, f"{label} 条件 {index}", errors))
    return facts


def placeholder_fact_reason(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    normalized = " ".join(value.split())
    for pattern, reason in PLACEHOLDER_FACT_PATTERNS:
        if pattern.search(normalized):
            return reason
    return None


def check_placeholder_fact(
    value: object, label: str, errors: list[str], seen: set[str]
) -> None:
    reason = placeholder_fact_reason(value)
    if reason and isinstance(value, str) and value not in seen:
        errors.append(f"{label} 使用占位事实 {value!r}（命中 {reason} 黑名单）")
        seen.add(value)


def _merge_assignments(left: dict[str, bool], right: dict[str, bool]) -> dict[str, bool] | None:
    merged = dict(left)
    for key, value in right.items():
        if key in merged and merged[key] is not value:
            return None
        merged[key] = value
    return merged


def _logic_assignments(node: object, desired: bool) -> list[dict[str, bool]]:
    if not isinstance(node, dict):
        return []
    fact_key = node.get("fact_key")
    if isinstance(fact_key, str) and fact_key:
        return [{fact_key: desired}]
    operator = node.get("operator")
    operands = node.get("operands")
    if operator not in {"AND", "OR", "NOT"} or not isinstance(operands, list) or not operands:
        return []
    if operator == "NOT":
        return _logic_assignments(operands[0], not desired)
    combine_all = (operator == "AND" and desired) or (operator == "OR" and not desired)
    if not combine_all:
        return [assignment for operand in operands for assignment in _logic_assignments(operand, desired)]
    candidates: list[dict[str, bool]] = [{}]
    for operand in operands:
        options = _logic_assignments(operand, desired)
        next_candidates: list[dict[str, bool]] = []
        for candidate in candidates:
            for option in options:
                merged = _merge_assignments(candidate, option)
                if merged is not None:
                    next_candidates.append(merged)
        candidates = next_candidates
        if not candidates:
            break
    return candidates


def _find_assignment(constraints: list[tuple[object, bool]]) -> dict[str, bool] | None:
    candidates: list[dict[str, bool]] = [{}]
    for node, desired in constraints:
        options = _logic_assignments(node, desired)
        next_candidates: list[dict[str, bool]] = []
        for candidate in candidates:
            for option in options:
                merged = _merge_assignments(candidate, option)
                if merged is not None:
                    next_candidates.append(merged)
        candidates = next_candidates
        if not candidates:
            return None
    return candidates[0]


def _simulation_facts(
    keys: set[str], assignment: dict[str, bool], unavailable: set[str] = frozenset()
) -> dict[str, dict[str, object]]:
    return {
        key: (
            {"status": "unavailable", "fact_state": "unavailable"}
            if key in unavailable
            else {"status": "available", "fact_state": "known", "value": assignment.get(key, False)}
        )
        for key in keys
    }


def validate_selection_group_simulation(
    step_label: str, groups: list[dict[str, object]], errors: list[str]
) -> None:
    grouped: dict[str, list[dict[str, object]]] = {}
    for group in groups:
        selection_group = group.get("selection_group")
        if isinstance(selection_group, str) and selection_group:
            grouped.setdefault(selection_group, []).append(group)
    for selection_group, branches in grouped.items():
        label = f"{step_label} 选择组 {selection_group}"
        if len(branches) < 2:
            errors.append(f"{label} 至少需要两个可选分支")
            continue
        if any(not isinstance(branch.get("branch_condition_logic"), dict) for branch in branches):
            errors.append(f"{label} 的每个分支都必须有 branch_condition_logic")
            continue
        keys = set()
        for branch in branches:
            keys.update(validate_condition_logic(branch.get("when"), f"{label} when", errors))
            keys.update(validate_condition_logic(branch.get("branch_condition_logic"), f"{label} 分支", errors))
            keys.update(
                key for key in branch.get("required_fact_keys", [])
                if isinstance(key, str) and key
            )

        for target_index, target in enumerate(branches):
            constraints: list[tuple[object, bool]] = [
                (target.get("when"), True),
                (target.get("branch_condition_logic"), True),
            ]
            assignment = _find_assignment(constraints)
            if assignment is None:
                errors.append(f"{label} 无法构造满足分支 {target_index + 1} 的事实")
                continue
            simulated_facts = _simulation_facts(keys, assignment)
            all_present = _conditional_missing_facts(branches, simulated_facts)
            if all_present:
                errors.append(f"{label} 只满足分支 {target_index + 1} 时没有放行：{sorted(all_present)}")

            active_indexes: set[int] = set()
            for index, branch in enumerate(branches):
                when_state, _ = _condition_state(branch.get("when"), simulated_facts)
                branch_state, _ = _condition_state(
                    branch.get("branch_condition_logic"), simulated_facts
                )
                if when_state == "true" and branch_state == "true":
                    active_indexes.add(index)
            active_required = {
                key
                for index in active_indexes
                for key in branches[index].get("required_fact_keys", [])
                if isinstance(key, str)
            }
            inactive_required = {
                key
                for index, branch in enumerate(branches)
                if index not in active_indexes
                for key in branch.get("required_fact_keys", [])
                if isinstance(key, str)
            } - active_required
            missing_inactive = _conditional_missing_facts(
                branches,
                _simulation_facts(keys, assignment, inactive_required),
            )
            if missing_inactive:
                errors.append(
                    f"{label} 已满足分支 {target_index + 1}，却被未选分支的缺失事实误停："
                    f"{sorted(missing_inactive)}"
                )

        for left_index, left in enumerate(branches):
            for right_index in range(left_index + 1, len(branches)):
                right = branches[right_index]
                assignment = _find_assignment([
                    (left.get("when"), True),
                    (left.get("branch_condition_logic"), True),
                    (right.get("when"), True),
                    (right.get("branch_condition_logic"), True),
                ])
                if assignment is None:
                    continue
                both_missing = _conditional_missing_facts(
                    branches,
                    _simulation_facts(keys, assignment),
                )
                if both_missing:
                    errors.append(
                        f"{label} 同时满足分支 {left_index + 1} 和 {right_index + 1} 时没有放行："
                        f"{sorted(both_missing)}"
                    )

                # Crossed prerequisites must still stop: the first branch's
                # when is true while its branch logic is false, and the
                # second branch's when is false while its branch logic is
                # true.  No branch has both of its own conditions satisfied.
                for first_index, second_index in (
                    (left_index, right_index),
                    (right_index, left_index),
                ):
                    first = branches[first_index]
                    second = branches[second_index]
                    cross_assignment = _find_assignment([
                        (first.get("when"), True),
                        (first.get("branch_condition_logic"), False),
                        (second.get("when"), False),
                        (second.get("branch_condition_logic"), True),
                    ] + [
                        # A crossed pair is a stop case only when no other
                        # branch in the same OR group is actually active.
                        (
                            {
                                "operator": "AND",
                                "operands": [
                                    other.get("when"),
                                    other.get("branch_condition_logic"),
                                ],
                            },
                            False,
                        )
                        for other_index, other in enumerate(branches)
                        if other_index not in {first_index, second_index}
                    ])
                    if cross_assignment is None:
                        continue
                    cross_missing = _conditional_missing_facts(
                        branches,
                        _simulation_facts(keys, cross_assignment),
                    )
                    if not cross_missing:
                        errors.append(
                            f"{label} 交叉组合（分支 {first_index + 1} 的 when 与分支 "
                            f"{second_index + 1} 的 branch_condition_logic）没有停判"
                        )

        all_false_constraints: list[tuple[object, bool]] = [(branches[0].get("when"), True)]
        all_false_constraints.extend((branch.get("branch_condition_logic"), False) for branch in branches)
        all_false_assignment = _find_assignment(all_false_constraints)
        if all_false_assignment is None:
            errors.append(f"{label} 无法构造所有分支都不满足的事实")
            continue
        all_false_missing = _conditional_missing_facts(
            branches,
            _simulation_facts(keys, all_false_assignment),
        )
        if not all_false_missing:
            errors.append(f"{label} 所有分支都不满足时没有停判")


def validate_generation_metadata(
    root: Path, recipe_data: dict, methods: list[dict], errors: list[str]
) -> None:
    if recipe_data.get("schema_version") != "judgment-method-recipes/v2":
        return
    generation = recipe_data.get("generation")
    if not isinstance(generation, dict):
        errors.append("v2 方法配方缺少 generation 生成记录")
        return
    if generation.get("generator") != GENERATOR_ID:
        errors.append("v2 方法配方不是由唯一正式生成器 build_methods.py 生成")
    state_path = root / "validation" / "batch-state.json"
    state = load_json(state_path, errors)
    if state:
        if state.get("schema_version") != "judgment-batch-state/v2":
            errors.append("v2 批次状态文件 schema_version 不合法")
        if state.get("batch_id") != generation.get("batch_id"):
            errors.append("v2 批次状态与方法配方的 batch_id 不一致")
        if state.get("current_state") not in {"mechanical_testing", "audit_in_progress", "merged"}:
            errors.append("v2 批次状态没有按单向流程进入机检仿真、审计中或已并入")
        recipe_path = root / "references" / "navigation" / "method-recipes.json"
        if recipe_path.is_file() and state.get("method_recipes_sha256") != sha256_file(recipe_path):
            errors.append("v2 批次状态没有绑定当前 method-recipes.json")
        if state.get("review_mode") != generation.get("review_mode"):
            errors.append("v2 批次状态与方法配方的审查模式不一致")
        if state.get("audit_step_ids") != generation.get("audit_step_ids"):
            errors.append("v2 批次状态与方法配方的应审步骤名单不一致")
    features = generation.get("chapter_features")
    features = set(features) if isinstance(features, list) else set()
    review_mode = generation.get("review_mode")
    if features & {"dasha_or_transit", "multi_planet_combination", "complex_yoga"} and review_mode != "full":
        errors.append("大运流年、多星同聚或复杂瑜伽批次必须逐步全审")
    step_ids = sorted(
        step.get("step_id")
        for method in methods if isinstance(method, dict)
        for step in method.get("steps", []) if isinstance(step, dict) and isinstance(step.get("step_id"), str)
    )
    audit_step_ids = generation.get("audit_step_ids")
    if not isinstance(audit_step_ids, list) or any(not isinstance(value, str) for value in audit_step_ids):
        errors.append("v2 方法配方缺少机器生成的 audit_step_ids")
        return
    if review_mode == "full":
        expected = step_ids
    elif review_mode == "sample":
        if features != {"simple_house_placement"}:
            errors.append("抽审只允许结构单一的落宫章节")
            return
        batch_id = generation.get("batch_id")
        if not isinstance(batch_id, str) or not batch_id:
            errors.append("抽审批次缺少 batch_id")
            return
        size = max(1, math.ceil(len(step_ids) * 0.2))
        expected = sorted(random.Random(batch_id).sample(step_ids, size))
    else:
        errors.append("v2 方法配方的 review_mode 不合法")
        return
    if audit_step_ids != expected:
        errors.append("audit_step_ids 不是由批次名固定摇号产生的应审步骤集合")
    validate_step_hashes_and_high_risk_terms(generation, methods, errors)


def validate_step_hashes_and_high_risk_terms(
    generation: dict, methods: list[dict], errors: list[str]
) -> None:
    """v2 步骤级哈希（Q1）与高风险词差异表（Q15/Q21）的机械复核。"""
    table = generation.get("high_risk_terms")
    if not isinstance(table, dict):
        errors.append("v2 方法配方缺少机器生成的 high_risk_terms 差异表")
        table = {}
    step_ids: set[str] = set()
    for method in methods:
        if not isinstance(method, dict):
            continue
        for step in method.get("steps", []):
            if not isinstance(step, dict) or not isinstance(step.get("step_id"), str):
                continue
            step_id = step["step_id"]
            step_ids.add(step_id)
            recorded_hash = step.get("step_hash")
            if not isinstance(recorded_hash, str) or recorded_hash != compute_step_hash(step):
                errors.append(f"步骤内容指纹缺失或与内容不一致：{step_id}")
            quotes = "\n".join(
                ref.get("quote", "")
                for ref in step.get("evidence_refs", [])
                if isinstance(ref, dict) and isinstance(ref.get("quote"), str)
            )
            detected_terms = {item["term"] for item in detect_high_risk_terms(quotes)}
            rows = table.get(step_id)
            rows = rows if isinstance(rows, list) else []
            row_terms = {
                row.get("term") for row in rows if isinstance(row, dict) and isinstance(row.get("term"), str)
            }
            if row_terms != detected_terms:
                errors.append(f"高风险词差异表与逐字短引的机器检出不一致：{step_id}")
                continue
            claim = step.get("minimum_supported_claim")
            claim = claim if isinstance(claim, str) else ""
            for row in rows:
                if not isinstance(row, dict):
                    continue
                mapped_quote = row.get("mapped_quote")
                mapped_claim = row.get("mapped_claim")
                if (
                    not isinstance(mapped_quote, str)
                    or normalize_for_term_match(str(row.get("term"))) not in normalize_for_term_match(mapped_quote)
                    or mapped_quote not in quotes
                ):
                    errors.append(f"高风险词映射的引文词不在逐字短引中：{step_id}：{row.get('term')}")
                if not isinstance(mapped_claim, str) or mapped_claim not in claim:
                    errors.append(f"高风险词映射的主张词不在最小意思中：{step_id}：{row.get('term')}")
    orphan_rows = set(table) - step_ids
    if orphan_rows:
        errors.append(f"高风险词差异表包含不存在的步骤：{sorted(orphan_rows)}")


def validate_repeated_minimum_claims(methods: list[dict], errors: list[str]) -> None:
    claims = [
        " ".join(step.get("minimum_supported_claim", "").split()).casefold()
        for method in methods if isinstance(method, dict)
        for step in method.get("steps", []) if isinstance(step, dict)
        if isinstance(step.get("minimum_supported_claim"), str)
    ]
    repeated = [claim for claim, count in Counter(claims).items() if claim and count >= 3]
    if repeated:
        errors.append(f"同一批次至少三个步骤重复同一句最小意思：{sorted(repeated)[0]}")


def validate_method(
    item: object,
    atoms: dict[str, dict],
    issues: dict[str, dict],
    pilot_only: bool,
    publishable: bool,
    errors: list[str],
    enforce_v2: bool = False,
) -> tuple[str | None, bool]:
    if not isinstance(item, dict):
        errors.append("方法配方条目必须是对象")
        return None, False
    method = item.get("method")
    label = f"方法 {method or '<缺少编号>'}"
    missing = REQUIRED_METHOD_FIELDS - set(item)
    if missing:
        errors.append(f"{label} 缺字段：{sorted(missing)}")
    if not isinstance(method, str) or not method:
        errors.append("方法配方缺少 method")
        return None, False
    if item.get("pilot_only") is not pilot_only or item.get("publishable") is not publishable:
        errors.append(f"{label} 的试验/发布标记与工作单不一致")
    if item.get("source_status") not in SOURCE_STATUSES:
        errors.append(f"{label} 的 source_status 不合法")
    if item.get("workflow_status") not in WORKFLOW_STATUSES:
        errors.append(f"{label} 的 workflow_status 不合法")
    if item.get("fact_binding_status") not in FACT_BINDING_STATUSES:
        errors.append(f"{label} 的 fact_binding_status 不合法")
    generalization_scope = item.get("generalization_scope")
    if generalization_scope is not None and generalization_scope not in GENERALIZATION_SCOPES:
        errors.append(f"{label} 的 generalization_scope 不合法")
    validate_workflow_history(label, item, errors)
    for field in ("user_intents", "required_facts", "stop_conditions"):
        if not non_empty_list(item.get(field)):
            errors.append(f"{label} 缺少非空数组 {field}")
    retrieval_plan = item.get("retrieval_plan")
    if not isinstance(retrieval_plan, dict):
        errors.append(f"{label} 缺少 retrieval_plan")
    else:
        # V3：空车道是诚实结果（原文没写反例/边界就不许硬凑），不再要求四路全非空。
        # 但支持路不能整个失守：抽取员写的支持路为空时，必须有程序派生的步级查询顶上。
        for lane in QUERY_LANES:
            if not isinstance(retrieval_plan.get(lane), list):
                errors.append(f"{label} 的查询路线 {lane} 必须是数组")
        if not non_empty_list(retrieval_plan.get("support_queries")) \
                and not non_empty_list(retrieval_plan.get("derived_step_queries")):
            errors.append(f"{label} 支持路为空且没有派生步级查询——该方法完全无法被检索")

    upstream_issue_ids = item.get("upstream_issue_ids")
    upstream_issue_ids = upstream_issue_ids if isinstance(upstream_issue_ids, list) else []
    if any(not isinstance(issue_id, str) or not issue_id for issue_id in upstream_issue_ids):
        errors.append(f"{label} 的 upstream_issue_ids 必须是字符串数组")
    for issue_id in upstream_issue_ids:
        issue = issues.get(issue_id)
        if issue is None:
            errors.append(f"{label} 引用了不存在的上游问题：{issue_id}")
        elif issue.get("status") != "open" or issue.get("blocking") is not True:
            errors.append(
                f"{label} 的 upstream_issue_ids 只能引用开放且 blocking=true 的上游问题：{issue_id}"
            )
        elif method not in issue.get("affected_method_ids", []):
            errors.append(f"{label} 与上游问题 {issue_id} 的受影响方法记录不一致")

    declared_facts = set()
    placeholder_facts_seen: set[str] = set()
    for field in ("required_facts", "conditional_facts"):
        values = item.get(field)
        if not isinstance(values, list) or any(not isinstance(value, str) or not value for value in values):
            errors.append(f"{label} 的 {field} 必须是字符串数组")
        else:
            declared_facts.update(values)
            for fact_key in values:
                check_placeholder_fact(fact_key, f"{label} 的 {field}", errors, placeholder_facts_seen)

    method_required_facts = item.get("required_facts")
    method_required_facts = (
        set(method_required_facts) if isinstance(method_required_facts, list) else set()
    )
    method_conditional_facts = item.get("conditional_facts")
    method_conditional_facts = (
        set(method_conditional_facts) if isinstance(method_conditional_facts, list) else set()
    )
    overlap = method_required_facts & method_conditional_facts
    if overlap:
        errors.append(f"{label} 的 required_facts 与 conditional_facts 重复：{sorted(overlap)}")

    steps = item.get("steps")
    steps = steps if isinstance(steps, list) else []
    produced_by_step: list[set[str]] = []
    produced_owner: dict[str, int] = {}
    for index, step in enumerate(steps, 1):
        step_label = f"{label} 步骤 {index}"
        if not isinstance(step, dict):
            produced_by_step.append(set())
            continue
        produced = step.get("produced_fact_keys")
        if not isinstance(produced, list) or any(not isinstance(value, str) or not value for value in produced):
            produced_by_step.append(set())
            continue
        produced_set = set(produced)
        for fact_key in produced_set:
            check_placeholder_fact(fact_key, f"{step_label} 的 produced_fact_keys", errors, placeholder_facts_seen)
        if len(produced_set) != len(produced):
            errors.append(f"{step_label} 的 produced_fact_keys 不能重复")
        for fact_key in produced_set:
            previous_index = produced_owner.get(fact_key)
            if previous_index is not None:
                errors.append(
                    f"{step_label} 与步骤 {previous_index} 同一方法内重复生产事实：{fact_key}"
                )
            else:
                produced_owner[fact_key] = index
        produced_by_step.append(produced_set)
    all_produced_facts = set(produced_owner)
    declared_output_overlap = all_produced_facts & declared_facts
    if declared_output_overlap:
        errors.append(
            f"{label} 的步骤产出不得写入 required_facts 或 conditional_facts：{sorted(declared_output_overlap)}"
        )
    all_steps_have_evidence = bool(steps)
    used_fact_keys: set[str] = set()
    method_evidence_atom_ids: set[str] = set()
    for index, step in enumerate(steps, 1):
        step_label = f"{label} 步骤 {index}"
        if not isinstance(step, dict):
            errors.append(f"{step_label} 必须是对象")
            all_steps_have_evidence = False
            continue
        missing_step_fields = REQUIRED_STEP_FIELDS - set(step)
        if missing_step_fields:
            errors.append(f"{step_label} 缺字段：{sorted(missing_step_fields)}")
        produced_fact_keys = step.get("produced_fact_keys")
        if (
            not isinstance(produced_fact_keys, list)
            or any(not isinstance(value, str) or not value for value in produced_fact_keys)
        ):
            errors.append(f"{step_label} 的 produced_fact_keys 必须是字符串数组")
        for field, description in (
            ("applicability_scope", "适用范围"),
            ("minimum_supported_claim", "原文直接支持的最小意思"),
        ):
            if not isinstance(step.get(field), str) or not step.get(field).strip():
                errors.append(f"{step_label} 缺少{description}")
        minimum_claim = step.get("minimum_supported_claim")
        if isinstance(minimum_claim, str):
            lowered_claim = minimum_claim.casefold()
            for fragment in EMPTY_CLAIM_FRAGMENTS:
                if fragment.casefold() in lowered_claim:
                    errors.append(f"{step_label} 的最小意思是空话模板：{fragment}")
                    break
        forbidden_extensions = step.get("forbidden_extensions")
        if (
            not isinstance(forbidden_extensions, list)
            or not forbidden_extensions
            or any(not isinstance(value, str) or not value for value in forbidden_extensions)
        ):
            errors.append(f"{step_label} 缺少非空 forbidden_extensions")
        exception_relations = step.get("exception_relations")
        if not isinstance(exception_relations, list):
            errors.append(f"{step_label} 的 exception_relations 必须是数组")
            exception_relations = []
        for relation_index, relation in enumerate(exception_relations, 1):
            relation_label = f"{step_label} 例外关系 {relation_index}"
            if not isinstance(relation, dict):
                errors.append(f"{relation_label} 必须是对象")
                continue
            if relation.get("type") not in EXCEPTION_RELATION_TYPES:
                errors.append(f"{relation_label} 的 type 不合法")
            relation_logic = relation.get("condition_logic")
            if relation_logic is not None:
                relation_facts = validate_condition_logic(
                    relation_logic, f"{relation_label} condition_logic", errors
                )
                for fact_key in relation_facts:
                    check_placeholder_fact(
                        fact_key,
                        f"{relation_label} condition_logic",
                        errors,
                        placeholder_facts_seen,
                    )
                unavailable_relation_facts = relation_facts - declared_facts - set().union(
                    *produced_by_step[: index - 1]
                )
                if unavailable_relation_facts:
                    errors.append(
                        f"{relation_label} 引用了未声明或尚未产出的事实："
                        f"{sorted(unavailable_relation_facts)}"
                    )
            relation_atoms = relation.get("evidence_atom_ids")
            if (
                not isinstance(relation_atoms, list)
                or not relation_atoms
                or any(atom_id not in atoms for atom_id in relation_atoms)
            ):
                errors.append(f"{relation_label} 缺少有效 evidence_atom_ids")
        if step.get("source_status") not in SOURCE_STATUSES:
            errors.append(f"{step_label} 的 source_status 不合法")
        stop_condition = step.get("stop_condition")
        if not isinstance(stop_condition, str) or not stop_condition.strip():
            errors.append(f"{step_label} 缺少非空 stop_condition")
        fact_keys = step.get("required_fact_keys")
        fact_keys = fact_keys if isinstance(fact_keys, list) else []
        if not fact_keys or any(not isinstance(value, str) or not value for value in fact_keys):
            errors.append(f"{step_label} 缺少非空 required_fact_keys")
        for fact_key in fact_keys:
            check_placeholder_fact(fact_key, f"{step_label} 的 required_fact_keys", errors, placeholder_facts_seen)
        stop_fact_keys = step.get("stop_fact_keys")
        if (
            not isinstance(stop_fact_keys, list)
            or any(not isinstance(value, str) or not value for value in stop_fact_keys)
            or set(stop_fact_keys) != set(fact_keys)
        ):
            errors.append(f"{step_label} 的 stop_fact_keys 必须与 required_fact_keys 一致")
        condition_facts = validate_condition_logic(step.get("condition_logic"), step_label, errors)
        for fact_key in condition_facts:
            check_placeholder_fact(fact_key, f"{step_label} 的 condition_logic", errors, placeholder_facts_seen)
        produced_fact_set = produced_by_step[index - 1]
        prior_produced_facts = set().union(*produced_by_step[: index - 1]) if index > 1 else set()
        future_produced_facts = all_produced_facts - prior_produced_facts - produced_fact_set
        fact_key_set = set(fact_keys)
        self_inputs = fact_key_set & produced_fact_set
        if self_inputs:
            errors.append(f"{step_label} 不能把本步骤产出当作本步骤输入：{sorted(self_inputs)}")
        future_inputs = fact_key_set & future_produced_facts
        if future_inputs:
            errors.append(f"{step_label} 不能使用未来步骤产出的事实：{sorted(future_inputs)}")
        conditional_as_required = fact_key_set & method_conditional_facts
        if conditional_as_required:
            errors.append(
                f"{step_label} 的 required_fact_keys 不能引用仅按分支取得的事实：{sorted(conditional_as_required)}"
            )
        undeclared_required = fact_key_set - method_required_facts - prior_produced_facts
        undeclared_required -= self_inputs | future_inputs
        undeclared_required -= conditional_as_required
        if undeclared_required:
            errors.append(f"{step_label} 使用了方法未声明的事实：{sorted(undeclared_required)}")

        groups = step.get("conditional_fact_requirements", [])
        if groups is None:
            groups = []
        if not isinstance(groups, list):
            errors.append(f"{step_label} 的 conditional_fact_requirements 必须是数组")
            groups = []
        conditional_group_facts: set[str] = set()
        for group_index, group in enumerate(groups, 1):
            group_label = f"{step_label} 条件组 {group_index}"
            if not isinstance(group, dict):
                errors.append(f"{group_label} 必须是对象")
                continue
            group_required = group.get("required_fact_keys")
            if (
                not isinstance(group_required, list)
                or not group_required
                or any(not isinstance(value, str) or not value for value in group_required)
            ):
                errors.append(f"{group_label} 的 required_fact_keys 必须是非空字符串数组")
                group_required = []
            group_required_set = set(group_required)
            for fact_key in group_required_set:
                check_placeholder_fact(
                    fact_key,
                    f"{group_label} 的 required_fact_keys",
                    errors,
                    placeholder_facts_seen,
                )
            conditional_group_facts.update(group_required_set)
            group_stop = group.get("stop_condition")
            if not isinstance(group_stop, str) or not group_stop.strip():
                errors.append(f"{group_label} 缺少非空 stop_condition")
            when_facts = validate_condition_logic(group.get("when"), f"{group_label} when", errors)
            for fact_key in when_facts:
                check_placeholder_fact(fact_key, f"{group_label} when", errors, placeholder_facts_seen)
            if when_facts - fact_key_set - prior_produced_facts:
                errors.append(
                    f"{group_label} 的 when 无法选择：只能引用本步骤 required_fact_keys 或前序步骤产出"
                )
            if group_required_set & fact_key_set:
                errors.append(f"{group_label} 不能重复声明本步骤 always-required 输入")
            if group_required_set & produced_fact_set:
                errors.append(f"{group_label} 不能把本步骤产出当作条件输入")
            if group_required_set & future_produced_facts:
                errors.append(f"{group_label} 不能使用未来步骤产出的事实")
            undeclared_group = group_required_set - method_conditional_facts - prior_produced_facts
            if undeclared_group:
                errors.append(
                    f"{group_label} 条件组事实没有在方法 conditional_facts 中声明：{sorted(undeclared_group)}"
                )
            selection_group = group.get("selection_group")
            branch_logic = group.get("branch_condition_logic")
            if selection_group is not None or branch_logic is not None:
                if not isinstance(selection_group, str) or not selection_group:
                    errors.append(f"{group_label} 的 selection_group 必须是非空字符串")
                branch_facts = validate_condition_logic(
                    branch_logic, f"{group_label} branch_condition_logic", errors
                )
                for fact_key in branch_facts:
                    check_placeholder_fact(
                        fact_key,
                        f"{group_label} branch_condition_logic",
                        errors,
                        placeholder_facts_seen,
                    )
                unavailable_branch_facts = branch_facts - group_required_set - prior_produced_facts
                if unavailable_branch_facts:
                    errors.append(
                        f"{group_label} 的 branch_condition_logic 引用了分支外事实："
                        f"{sorted(unavailable_branch_facts)}"
                    )
        validate_selection_group_simulation(step_label, groups, errors)
        allowed_condition_facts = fact_key_set | conditional_group_facts | prior_produced_facts
        unavailable_condition_facts = condition_facts - allowed_condition_facts
        if unavailable_condition_facts:
            errors.append(
                f"{step_label} 的 condition_logic 引用了未声明、当前产出或未来产出的事实：{sorted(unavailable_condition_facts)}"
            )
        if not fact_key_set.issubset(condition_facts):
            errors.append(f"{step_label} 的 condition_logic 没有准确覆盖 required_fact_keys")
        for fact_key in fact_keys:
            used_fact_keys.add(fact_key)
        refs = step.get("evidence_refs")
        refs = refs if isinstance(refs, list) else []
        if not refs:
            all_steps_have_evidence = False
        step_evidence_atom_ids = {
            ref.get("evidence_atom_id")
            for ref in refs
            if isinstance(ref, dict) and isinstance(ref.get("evidence_atom_id"), str)
        }
        method_evidence_atom_ids.update(step_evidence_atom_ids)
        source_text = "\n".join(
            ref.get("quote", "")
            for ref in refs
            if isinstance(ref, dict) and isinstance(ref.get("quote"), str)
        )
        source_text = "\n".join((source_text, step.get("minimum_supported_claim", "")))
        has_selection_group = any(
            isinstance(group, dict)
            and isinstance(group.get("selection_group"), str)
            and group.get("selection_group")
            for group in groups
        )
        if enforce_v2 and not has_selection_group and or_outside_results(source_text, step):
            errors.append(
                f"{step_label} 的正式原文含明确 OR／任选分支，但配方没有 selection_group"
            )
        if step.get("source_status") == "repeated_support" and len(step_evidence_atom_ids) < 2:
            errors.append(f"{step_label} 的 repeated_support 至少需要两个独立原文编号")
        allowed_content_roles = set(METHOD_EVIDENCE_CONTENT_ROLES)
        if generalization_scope == "single_case_only":
            allowed_content_roles.add("case")
        for ref_index, ref in enumerate(refs, 1):
            if not check_evidence_ref(
                f"{step_label} 证据 {ref_index}", ref, atoms, errors, allowed_content_roles
            ):
                all_steps_have_evidence = False

    unused_required_facts = set(item.get("required_facts", [])) - used_fact_keys if steps else set()
    if unused_required_facts:
        errors.append(
            f"{label} 的必查事实没有被任何步骤使用：{sorted(unused_required_facts)}"
        )
    if item.get("source_status") == "repeated_support" and len(method_evidence_atom_ids) < 2:
        errors.append(f"{label} 的 repeated_support 至少需要两个独立原文编号")

    executable = item.get("executable_in_pilot") is True
    if executable:
        if generalization_scope == "single_case_only":
            errors.append(f"{label} 是单案例专用方法，不能进入通用执行主路")
        if item.get("source_status") not in EXECUTABLE_SOURCE_STATUSES:
            errors.append(f"{label} 来源状态不足却进入了执行主路")
        for index, step in enumerate(steps, 1):
            if isinstance(step, dict) and step.get("source_status") not in EXECUTABLE_SOURCE_STATUSES:
                errors.append(f"{label} 步骤 {index} 来源状态不足却进入了执行主路")
        if not all_steps_have_evidence:
            errors.append(f"{label} 存在无证据步骤却进入了执行主路")
        if item.get("fact_binding_status") != "mapped":
            errors.append(f"{label} 的排盘事实尚未接通却进入了执行主路")
        if item.get("workflow_status") not in {
            "independent_verified",
            "shadow_passed",
            "pilot_passed",
        }:
            errors.append(f"{label} 尚未完成独立核验却进入了执行主路")
        for issue_id in upstream_issue_ids:
            issue = issues.get(issue_id)
            if issue and issue.get("status") == "open" and issue.get("blocking") is True:
                errors.append(f"{label} 仍有阻塞中的上游问题却进入了执行主路：{issue_id}")
    return method, executable


def validate_method_links(
    methods: dict[str, dict], executable_methods: set[str], issues: dict[str, dict], errors: list[str]
) -> None:
    graph: dict[str, list[str]] = {}
    for method, item in methods.items():
        dependencies = item.get("dependencies")
        dependencies = dependencies if isinstance(dependencies, list) else []
        if any(not isinstance(value, str) or not value for value in dependencies):
            errors.append(f"方法 {method} 的 dependencies 必须是字符串数组")
        graph[method] = [value for value in dependencies if isinstance(value, str)]
        for dependency in graph[method]:
            if dependency not in methods:
                errors.append(f"方法 {method} 依赖不存在的方法：{dependency}")
            elif method in executable_methods and dependency not in executable_methods:
                errors.append(f"可执行方法 {method} 依赖不可执行的方法：{dependency}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(method: str, trail: list[str]) -> None:
        if method in visiting:
            cycle = " → ".join(trail + [method])
            errors.append(f"方法依赖存在循环：{cycle}")
            return
        if method in visited:
            return
        visiting.add(method)
        for dependency in graph.get(method, []):
            if dependency in graph:
                visit(dependency, trail + [method])
        visiting.remove(method)
        visited.add(method)

    for method in graph:
        visit(method, [])

    for issue_id, issue in issues.items():
        if issue.get("blocking") is not True:
            continue
        for method in issue.get("affected_method_ids", []):
            if method not in methods:
                errors.append(f"上游问题 {issue_id} 引用了不存在的方法：{method}")
            elif issue_id not in methods[method].get("upstream_issue_ids", []):
                errors.append(f"上游问题 {issue_id} 没有被受影响方法 {method} 引用")


def validate_upstream_impact(
    methods: dict[str, dict],
    issues: dict[str, dict],
    query_data: dict,
    errors: list[str],
) -> None:
    for issue_id, issue in issues.items():
        if issue.get("blocking") is not True:
            continue
        atom_id = issue.get("evidence_atom_id")
        impacted: set[str] = set()
        for method_id, method in methods.items():
            if any(
                isinstance(ref, dict) and ref.get("evidence_atom_id") == atom_id
                for step in method.get("steps", [])
                if isinstance(step, dict)
                for ref in step.get("evidence_refs", [])
            ):
                impacted.add(method_id)

        changed = True
        while changed:
            changed = False
            for method_id, method in methods.items():
                dependencies = method.get("dependencies", [])
                if method_id not in impacted and any(dep in impacted for dep in dependencies):
                    impacted.add(method_id)
                    changed = True

        declared = set(issue.get("affected_method_ids", []))
        if declared != impacted:
            errors.append(
                f"上游问题受影响方法清单不完整：{issue_id}；实际应冻结 "
                + ", ".join(sorted(impacted))
            )
        for method_id in impacted:
            if issue_id not in methods[method_id].get("upstream_issue_ids", []):
                errors.append(f"上游问题没有传递到受影响方法：{issue_id} → {method_id}")

        if issue.get("status") == "open" and issue.get("blocking") is True:
            topics = query_data.get("topics")
            topics = topics if isinstance(topics, dict) else {}
            for topic_id, topic in topics.items():
                if not isinstance(topic, dict):
                    continue
                routed = set(topic.get("method_ids", [])) | set(topic.get("candidate_method_ids", []))
                if routed & impacted and (
                    topic.get("execution_allowed") is True
                    or set(topic.get("method_ids", [])) & impacted
                ):
                    errors.append(
                        f"开放主题仍引用被上游问题冻结的方法：{issue_id} → {topic_id}"
                    )


def method_step_hash_map(methods: dict[str, dict]) -> dict[str, dict[str, str]] | None:
    """v2 配方（步骤带 step_hash）返回 {方法: {步骤: 指纹}}；v1 配方返回 None。"""
    mapping: dict[str, dict[str, str]] = {}
    for method_id, method in methods.items():
        steps = {}
        for step in method.get("steps", []):
            if not isinstance(step, dict):
                return None
            step_id = step.get("step_id")
            step_hash = step.get("step_hash")
            if not isinstance(step_id, str) or not isinstance(step_hash, str):
                return None
            steps[step_id] = step_hash
        mapping[method_id] = steps
    return mapping


def load_receipt(
    path: Path,
    schema_version: str,
    source_sha: str,
    distillation_run_id: str,
    method_recipes_sha: str,
    methods: dict[str, dict],
    errors: list[str],
    step_hashes_by_method: dict[str, dict[str, str]] | None = None,
) -> dict:
    receipt = load_json(path, errors)
    required = {
        "schema_version",
        "run_id",
        "distillation_run_id",
        "evidence_atoms_sha256",
        "method_ids",
        "method_steps",
    }
    # Q1：v2 凭证逐步骤绑定 step_hash；v1 历史夹具仍绑整份配方哈希。
    if step_hashes_by_method is None:
        required.add("method_recipes_sha256")
    else:
        required.add("method_step_hashes")
    missing = required - set(receipt)
    if missing:
        errors.append(f"核验凭证缺字段 {sorted(missing)}：{path}")
    if receipt.get("schema_version") != schema_version:
        errors.append(f"核验凭证版本不合法：{path}")
    if receipt.get("evidence_atoms_sha256") != source_sha:
        errors.append(f"核验凭证没有绑定当前原文原子：{path}")
    if receipt.get("distillation_run_id") != distillation_run_id:
        errors.append(f"核验凭证没有绑定当前蒸馏运行：{path}")
    if step_hashes_by_method is None and receipt.get("method_recipes_sha256") != method_recipes_sha:
        errors.append(f"核验凭证没有绑定当前方法配方内容：{path}")
    if receipt.get("run_id") == distillation_run_id or not receipt.get("run_id"):
        errors.append(f"核验凭证必须来自不同运行记录：{path}")
    if not non_empty_list(receipt.get("method_ids")):
        errors.append(f"核验凭证没有方法编号：{path}")
    method_steps = receipt.get("method_steps")
    if not isinstance(method_steps, dict):
        errors.append(f"核验凭证没有绑定方法步骤：{path}")
        method_steps = {}
    receipt_step_hashes = receipt.get("method_step_hashes")
    if step_hashes_by_method is not None and not isinstance(receipt_step_hashes, dict):
        errors.append(f"核验凭证没有逐步骤绑定 step_hash：{path}")
        receipt_step_hashes = {}
    for method_id in receipt.get("method_ids", []):
        method = methods.get(method_id)
        if not method:
            errors.append(f"核验凭证引用不存在的方法：{method_id}")
            continue
        expected_steps = [
            step.get("step_id")
            for step in method.get("steps", [])
            if isinstance(step, dict) and isinstance(step.get("step_id"), str)
        ]
        if method_steps.get(method_id) != expected_steps:
            errors.append(f"核验凭证没有绑定当前方法步骤：{method_id}")
        if step_hashes_by_method is not None:
            if receipt_step_hashes.get(method_id) != step_hashes_by_method.get(method_id):
                errors.append(f"核验凭证没有绑定当前方法步骤内容指纹：{method_id}")
    return receipt


def validate_status_receipts(
    root: Path,
    methods: dict[str, dict],
    source_sha: str,
    distillation_run_id: str,
    errors: list[str],
) -> None:
    method_recipes_sha = sha256_file(root / "references" / "navigation" / "method-recipes.json")
    step_hashes_by_method = method_step_hash_map(methods)
    independent_methods = {
        method for method, item in methods.items()
        if item.get("workflow_status") in INDEPENDENT_OR_LATER
    }
    shadow_methods = {
        method for method, item in methods.items()
        if item.get("workflow_status") in {"shadow_passed", "pilot_passed"}
    }
    approved_methods = {
        method for method, item in methods.items()
        if item.get("workflow_status") == "pilot_passed"
    }
    independent_receipt: dict = {}
    if independent_methods:
        independent_receipt = load_receipt(
            root / "validation" / "independent-verification.json",
            "independent-verification/v1",
            source_sha,
            distillation_run_id,
            method_recipes_sha,
            methods,
            errors,
            step_hashes_by_method,
        )
        missing = independent_methods - set(independent_receipt.get("method_ids", []))
        if missing:
            errors.append(f"独立核验凭证缺少方法：{sorted(missing)}")
    shadow_receipt: dict = {}
    if shadow_methods:
        shadow_receipt = load_receipt(
            root / "validation" / "shadow-results.json",
            "shadow-results/v1",
            source_sha,
            distillation_run_id,
            method_recipes_sha,
            methods,
            errors,
            step_hashes_by_method,
        )
        if shadow_receipt.get("independent_run_id") != independent_receipt.get("run_id"):
            errors.append("Shadow 凭证没有绑定当前独立核验运行")
        missing = shadow_methods - set(shadow_receipt.get("method_ids", []))
        if missing:
            errors.append(f"Shadow 凭证缺少方法：{sorted(missing)}")
    if approved_methods:
        approval = load_json(root / "validation" / "pilot-approval.json", errors)
        if approval.get("schema_version") != "pilot-approval/v1" or approval.get("approved") is not True:
            errors.append("试验通过状态缺少人工批准凭证")
        if approval.get("shadow_run_id") != shadow_receipt.get("run_id"):
            errors.append("人工批准凭证没有绑定当前 Shadow 运行")
        missing = approved_methods - set(approval.get("method_ids", []))
        if missing:
            errors.append(f"人工批准凭证缺少方法：{sorted(missing)}")


def validate_topics(
    query_data: dict,
    methods: dict[str, dict],
    executable_methods: set[str],
    errors: list[str],
) -> int:
    query_topics = query_data.get("topics")
    query_topics = query_topics if isinstance(query_topics, dict) else {}
    if not query_topics:
        errors.append("query-recipes.json 没有主题配方")
    for name, item in query_topics.items():
        label = f"主题 {name}"
        if not isinstance(item, dict):
            errors.append(f"{label} 必须是对象")
            continue
        missing = REQUIRED_TOPIC_FIELDS - set(item)
        if missing:
            errors.append(f"{label} 缺字段：{sorted(missing)}")
        for field in ("user_intents", "required_facts", "stop_conditions"):
            if not non_empty_list(item.get(field)):
                errors.append(f"{label} 缺少非空数组 {field}")
        # V3：主题层四路同方法层——空车道是诚实结果，但必须是数组；
        # 支持路可由派生步级查询兜底。
        for lane in QUERY_LANES:
            if not isinstance(item.get(lane), list):
                errors.append(f"{label} 的查询路线 {lane} 必须是数组")
        if not non_empty_list(item.get("support_queries")) \
                and not non_empty_list(item.get("derived_step_queries")):
            errors.append(f"{label} 支持路为空且没有派生步级查询")
        conditional_facts = item.get("conditional_facts")
        if not isinstance(conditional_facts, list):
            errors.append(f"{label} 的 conditional_facts 必须是数组")
            conditional_facts = []
        if item.get("fact_binding_status") not in FACT_BINDING_STATUSES:
            errors.append(f"{label} 的 fact_binding_status 不合法")
        method_ids = item.get("method_ids")
        candidate_method_ids = item.get("candidate_method_ids")
        method_ids = method_ids if isinstance(method_ids, list) else []
        candidate_method_ids = (
            candidate_method_ids if isinstance(candidate_method_ids, list) else []
        )
        if not method_ids and not candidate_method_ids:
            errors.append(f"{label} 没有可执行方法或候选方法")
        if set(method_ids) & set(candidate_method_ids):
            errors.append(f"{label} 同一方法同时出现在可执行和候选列表")
        for method_id in method_ids:
            if method_id not in executable_methods:
                errors.append(f"{label} 引用了未进入执行主路的方法：{method_id}")
        for method_id in candidate_method_ids:
            if method_id not in methods:
                errors.append(f"{label} 引用了不存在的候选方法：{method_id}")
        topic_facts = set(item.get("required_facts", [])) | set(conditional_facts)
        for method_id in method_ids + candidate_method_ids:
            method = methods.get(method_id)
            if not method:
                continue
            missing_facts = set(method.get("required_facts", [])) - topic_facts
            if missing_facts:
                errors.append(f"{label} 漏掉方法 {method_id} 的必查事实：{sorted(missing_facts)}")
        execution_allowed = item.get("execution_allowed") is True
        if candidate_method_ids and execution_allowed:
            errors.append(f"{label} 仍有候选方法却允许实际执行")
        if execution_allowed and not method_ids:
            errors.append(f"{label} 允许实际执行但没有可执行方法")
        if execution_allowed and item.get("fact_binding_status") != "mapped":
            errors.append(f"{label} 的排盘事实尚未接通却允许实际执行")
    return len(query_topics)


def validate_pilot_policy(
    pilot_status: dict,
    methods: dict[str, dict],
    executable_methods: set[str],
    query_data: dict,
    errors: list[str],
) -> None:
    if pilot_status.get("independent_verification_allowed") is False:
        for method, item in methods.items():
            if item.get("workflow_status") in INDEPENDENT_OR_LATER:
                errors.append(f"试验状态禁止独立核验，但方法 {method} 已进入后续状态")

    if pilot_status.get("shadow_allowed") is False:
        for method, item in methods.items():
            if item.get("workflow_status") in {"shadow_passed", "pilot_passed"}:
                errors.append(
                    f"试验状态禁止 Shadow（独立影子考试），但方法 {method} 已进入 Shadow 或更后状态"
                )

    if "production_agent_execution" in pilot_status.get("forbidden_uses", []):
        if executable_methods:
            errors.append(
                "试验状态禁止生产执行，但存在可执行方法："
                + ", ".join(sorted(executable_methods))
            )
        topics = query_data.get("topics")
        topics = topics if isinstance(topics, dict) else {}
        for topic, item in topics.items():
            if isinstance(item, dict) and item.get("execution_allowed") is True:
                errors.append(f"试验状态禁止生产执行，但主题 {topic} 被允许执行")


def validate_v3_queries(methods: list[dict], source_path, errors: list[str]) -> None:
    """V3 查询的验证器侧独立复核（与生成器同一共享函数、各自独立执行）。"""
    import re as _re
    if not source_path:
        return  # 原文路径缺失由前置检查报，不在这里重复
    try:
        lines = Path(source_path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return  # 原文文件缺失由前置检查报，不在这里重复
    parts, titles = [], set()
    for line in lines:
        if not line.strip():
            continue
        atom = json.loads(line)
        parts.append(shared_constants.normalize_for_verbatim(atom.get("exact_text", "")))
        if atom.get("chapter_title"):
            titles.add(shared_constants.normalize_for_verbatim(atom["chapter_title"]))
    corpus = " \n ".join(parts + sorted(titles))
    ascii_query = _re.compile(r"^[\x00-\x7f\u00c0-\u024f\u1e00-\u1eff’‘“”]+$")
    for method in methods:
        plan = method.get("retrieval_plan")
        if not isinstance(plan, dict):
            continue
        label = f"方法 {method.get('method')}"
        derived = plan.get("derived_step_queries")
        if isinstance(derived, list):
            expected: list[dict] = []
            for number, step in enumerate(method.get("steps") or [], 1):
                claim_terms = step.get("claim_terms") if isinstance(step, dict) else None
                if isinstance(claim_terms, dict):
                    expected.extend(shared_constants.derive_step_queries(
                        f"{method.get('method')}.step-{number:03d}", claim_terms
                    ))
            if derived != expected:
                errors.append(f"{label} 的 derived_step_queries 与从 claim_terms 重新派生的结果不一致（疑被手改）")
        for lane in ("support_queries", "counter_queries", "boundary_queries", "method_queries"):
            for query in plan.get(lane) or []:
                if isinstance(query, str) and ascii_query.match(query) \
                        and not shared_constants.is_verbatim_in(query, corpus):
                    errors.append(f"{label} 的 {lane} 含无法在冻结原文逐字命中的英文查询：{query[:70]!r}")


def validate(root: Path, require_v2: bool = False) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    required_paths = (
        root / "SKILL.md",
        root / "WORK_ORDER.json",
        root / "PIPELINE_STATE.md",
        root / "DISTILLATION_SOURCE.json",
        root / "UPSTREAM_ISSUES.json",
        root / "UPSTREAM_ISSUES.md",
        root / "references" / "knowledge" / "chapter-map.json",
        root / "references" / "knowledge" / "topic-map.json",
        root / "references" / "knowledge" / "glossary.json",
        root / "references" / "navigation" / "method-map.md",
        root / "references" / "navigation" / "required-checks.json",
        root / "references" / "navigation" / "query-recipes.json",
        root / "references" / "navigation" / "method-recipes.json",
        root / "references" / "navigation" / "version-routing.md",
        root / "methods" / "verified.md",
        root / "validation" / "method-source-scan.json",
    )
    for path in required_paths:
        if not path.is_file():
            errors.append(f"缺少文件：{path}")

    work_order = load_json(root / "WORK_ORDER.json", errors)
    pilot_only = work_order.get("pilot_only") is True
    publishable = work_order.get("publishable") is True
    if pilot_only and publishable:
        errors.append("试验任务不能标记为允许发布")
    artifact_scope = work_order.get("artifact_scope")
    if artifact_scope == "PILOT_TEMP" and not pilot_only:
        errors.append("PILOT_TEMP 必须标记为仅供试验")
    if artifact_scope == "FORMAL" and pilot_only:
        errors.append("FORMAL 正式输入不能标记为仅供试验")
    if artifact_scope == "PILOT_TEMP" and not (root / "PILOT_STATUS.json").is_file():
        errors.append("PILOT_TEMP 缺少 PILOT_STATUS.json")

    input_data = work_order.get("input")
    input_data = input_data if isinstance(input_data, dict) else {}
    chapter_scope = {
        value for value in input_data.get("chapter_scope", [])
        if isinstance(value, int) and not isinstance(value, bool)
    }
    atom_scope = {
        value for value in input_data.get("evidence_atom_scope", [])
        if isinstance(value, str) and value
    }
    if not chapter_scope and not atom_scope:
        errors.append("工作单没有允许章节或原文编号范围")
    source_path, expected_sha, package_id, package, pilot_status = resolve_input(
        root, work_order, errors
    )
    atoms: dict[str, dict] = {}
    actual_sha = ""
    if source_path is None or not source_path.is_file():
        errors.append(f"原文原子文件不存在：{source_path}")
    else:
        actual_sha = sha256_file(source_path)
        if expected_sha != actual_sha:
            errors.append("原文原子内容摘要与已锁定输入不一致")
        if artifact_scope == "PILOT_TEMP":
            snapshot = input_data.get("source_snapshot")
            snapshot = snapshot if isinstance(snapshot, dict) else {}
            stat = source_path.stat()
            if snapshot.get("size_bytes") != stat.st_size:
                errors.append("原文原子文件大小与开工快照不一致")
            if snapshot.get("mtime_ns") != stat.st_mtime_ns:
                errors.append("原文原子文件修改时间与开工快照不一致")
        atoms = load_scoped_atoms(source_path, chapter_scope, atom_scope, errors)
        if not atoms:
            errors.append("允许范围内没有可用原文原子")

    validate_distillation_source(
        root, work_order, source_path, actual_sha or expected_sha, package_id, package, errors
    )
    check_json_flags(root, pilot_only, publishable, errors)
    check_forbidden_tokens(root, errors)
    validate_knowledge_maps(root, atoms, errors)
    issue_data, issues = load_upstream_issues(root, atoms, errors)

    recipe_data = load_json(
        root / "references" / "navigation" / "method-recipes.json", errors
    )
    methods = recipe_data.get("methods")
    methods = methods if isinstance(methods, list) else []
    # V3 独立复核（不信任生成器自报）：
    # 1) derived_step_queries 若存在，必须与"从 claim_terms 重新派生"逐字节一致——
    #    claim_terms 受步骤指纹保护，所以这一条同时保证派生查询没被手改；
    # 2) 四路英文查询在全书冻结原文（含章名）上重跑逐字命中。
    validate_v3_queries(methods, source_path, errors)
    enforce_v2 = recipe_data.get("schema_version") == "judgment-method-recipes/v2" or require_v2
    if require_v2 and recipe_data.get("schema_version") != "judgment-method-recipes/v2":
        errors.append("本批要求 v2，但方法配方不是由唯一正式生成器重新生成")
    validate_generation_metadata(root, recipe_data, methods, errors)
    validate_repeated_minimum_claims(methods, errors)
    if not methods:
        errors.append("method-recipes.json 没有方法候选")
    method_names: set[str] = set()
    executable_methods: set[str] = set()
    method_items: dict[str, dict] = {}
    for item in methods:
        method, executable = validate_method(
            item, atoms, issues, pilot_only, publishable, errors, enforce_v2=enforce_v2
        )
        if method:
            if method in method_names:
                errors.append(f"方法编号重复：{method}")
            method_names.add(method)
            if isinstance(item, dict):
                method_items[method] = item
            if executable:
                executable_methods.add(method)

    validate_method_source_scan(root, atoms, method_items, issues, errors)
    validate_method_links(method_items, executable_methods, issues, errors)
    manifest = load_json(root / "DISTILLATION_SOURCE.json", errors)
    if actual_sha and isinstance(manifest.get("distillation_run_id"), str):
        validate_status_receipts(
            root,
            method_items,
            actual_sha,
            manifest["distillation_run_id"],
            errors,
        )
    query_data = load_json(root / "references" / "navigation" / "query-recipes.json", errors)
    topic_count = validate_topics(query_data, method_items, executable_methods, errors)
    validate_upstream_impact(method_items, issues, query_data, errors)
    if artifact_scope == "PILOT_TEMP":
        validate_pilot_policy(
            pilot_status,
            method_items,
            executable_methods,
            query_data,
            errors,
        )
    derived_count = sync_derived_outputs(
        root, recipe_data, query_data, issue_data, errors, write=False
    )
    if pilot_only and publishable:
        warnings.append("试验状态错误会阻止交付")

    return {
        "target": str(root),
        "pilot_only": pilot_only,
        "publishable": publishable,
        "scoped_atoms": len(atoms),
        "methods": len(method_names),
        "executable_methods": len(executable_methods),
        "topics": topic_count,
        "derived_files": derived_count,
        "errors": errors,
        "warnings": warnings,
        "passed": not errors,
    }


def render_derived(root: Path) -> dict:
    errors: list[str] = []
    method_data = load_json(root / "references" / "navigation" / "method-recipes.json", errors)
    query_data = load_json(root / "references" / "navigation" / "query-recipes.json", errors)
    issue_data = load_json(root / "UPSTREAM_ISSUES.json", errors)
    count = 0
    if not errors:
        count = sync_derived_outputs(root, method_data, query_data, issue_data, errors, write=True)
    return {"target": str(root), "rendered_files": count, "errors": errors, "passed": not errors}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument(
        "--render-derived",
        action="store_true",
        help="从方法、主题和上游问题机器真相重新生成人读派生文件",
    )
    parser.add_argument(
        "--require-v2",
        action="store_true",
        help="新批次强制要求唯一正式生成器的 v2 方法配方",
    )
    args = parser.parse_args()
    root = args.target.resolve()
    if not root.is_dir():
        print(json.dumps({"passed": False, "errors": [f"目标目录不存在：{root}"]}, ensure_ascii=False, indent=2))
        return 2
    if args.render_derived:
        render_report = render_derived(root)
        if not render_report["passed"]:
            print(json.dumps(render_report, ensure_ascii=False, indent=2))
            return 1
    report = validate(root, require_v2=args.require_v2)
    if args.render_derived:
        report["rendered_files"] = render_report["rendered_files"]
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
