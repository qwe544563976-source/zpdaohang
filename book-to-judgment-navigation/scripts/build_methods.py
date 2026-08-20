#!/usr/bin/env python3
"""Build method-recipes.json from schema-validated AI extraction JSON."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
import random
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

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
map_high_risk_terms = shared_constants.map_high_risk_terms

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "references" / "method-extraction.schema.json"
GENERATOR_VERSION = "2"
METHOD_EVIDENCE_CONTENT_ROLES = {"verse", "prose", "table"}
HIGH_RISK_FEATURES = {"dasha_or_transit", "multi_planet_combination", "complex_yoga"}


class BuildError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BuildError(f"无法读取 JSON：{path}：{exc}") from exc
    if not isinstance(value, dict):
        raise BuildError(f"JSON 顶层必须是对象：{path}")
    return value


def validate_schema(value: dict[str, Any]) -> None:
    schema = load_json(SCHEMA_PATH)
    errors = sorted(Draft202012Validator(schema).iter_errors(value), key=lambda item: list(item.path))
    if errors:
        details = []
        for error in errors[:20]:
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            details.append(f"{location}：{error.message}")
        if len(errors) > 20:
            details.append(f"其余 {len(errors) - 20} 个结构错误未展开")
        raise BuildError("AI 抽取 JSON 不符合严格 Schema：\n- " + "\n- ".join(details))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def resolve_atoms(accepted_package_path: Path, batch: dict[str, Any]) -> tuple[dict[str, dict], dict]:
    package = load_json(accepted_package_path)
    if package.get("artifact_scope") != batch["artifact_scope"]:
        raise BuildError("AI 抽取批次与 accepted-package 的 artifact_scope 不一致")
    if package.get("distillation_allowed") is not True:
        raise BuildError("accepted-package 没有开放蒸馏权限")
    gates = package.get("upstream_gates") or {}
    if any(gates.get(key) != "pass" for key in ("source_text_bidirectional", "chunking_validation", "accepted")):
        raise BuildError("accepted-package 的上游检查没有全部通过")
    book = package.get("book") or {}
    if book.get("book_id") != batch["book_id"] or book.get("edition_id") != batch["edition_id"]:
        raise BuildError("AI 抽取批次的书籍或版本与 accepted-package 不一致")
    atom_info = package.get("evidence_atoms") or {}
    atom_path_value = atom_info.get("path")
    if not isinstance(atom_path_value, str) or not atom_path_value:
        raise BuildError("accepted-package 缺少 evidence_atoms.path")
    atom_path = Path(atom_path_value)
    if not atom_path.is_file():
        raise BuildError(f"原文原子文件不存在：{atom_path}")
    expected_hash = atom_info.get("content_sha256")
    if not isinstance(expected_hash, str) or sha256(atom_path) != expected_hash:
        raise BuildError("原文原子文件内容与 accepted-package 不一致")
    atoms: dict[str, dict] = {}
    for line_number, line in enumerate(atom_path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            atom = json.loads(line)
        except json.JSONDecodeError as exc:
            raise BuildError(f"原文原子第 {line_number} 行不是合法 JSON：{exc}") from exc
        atom_id = atom.get("evidence_atom_id") if isinstance(atom, dict) else None
        if not isinstance(atom_id, str) or not atom_id:
            raise BuildError(f"原文原子第 {line_number} 行缺少 evidence_atom_id")
        if atom_id in atoms:
            raise BuildError(f"原文原子编号重复：{atom_id}")
        atoms[atom_id] = atom
    return atoms, package


def logic_facts(node: dict[str, Any]) -> set[str]:
    fact_key = node.get("fact_key")
    if isinstance(fact_key, str):
        return {fact_key}
    return set().union(*(logic_facts(item) for item in node.get("operands", [])))


def placeholder_fact_reason(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    normalized = " ".join(value.split())
    for pattern, reason in PLACEHOLDER_FACT_PATTERNS:
        if pattern.search(normalized):
            return reason
    return None


def validate_fact_key_not_placeholder(value: object, label: str) -> None:
    reason = placeholder_fact_reason(value)
    if reason:
        raise BuildError(f"{label} 使用占位事实 {value!r}（命中 {reason} 黑名单）")


def validate_method_fact_keys(method: dict[str, Any]) -> None:
    method_id = method["method"]

    def check_list(values: object, label: str) -> None:
        if isinstance(values, list):
            for index, value in enumerate(values, 1):
                validate_fact_key_not_placeholder(value, f"方法 {method_id} {label}[{index}]")

    for fact in method["facts"]:
        validate_fact_key_not_placeholder(fact["key"], f"方法 {method_id} facts.key")
    for step_number, step in enumerate(method["steps"], 1):
        step_label = f"方法 {method_id} 步骤 {step_number}"
        check_list(step["required_fact_keys"], f"步骤 {step_number} required_fact_keys")
        check_list(step["produced_fact_keys"], f"步骤 {step_number} produced_fact_keys")
        check_list(step["time_scope"]["fact_keys"], f"步骤 {step_number} time_scope.fact_keys")
        for node in [step["condition_logic"], *step["concession_conditions"]]:
            for fact_key in logic_facts(node):
                validate_fact_key_not_placeholder(fact_key, f"{step_label} condition fact")
        for group in step["conditional_requirements"]:
            check_list(group["required_fact_keys"], f"步骤 {step_number} conditional required_fact_keys")
            for fact_key in logic_facts(group["when"]):
                validate_fact_key_not_placeholder(fact_key, f"{step_label} conditional when fact")
        for alternative_group in step["alternative_groups"]:
            for branch in alternative_group["branches"]:
                check_list(branch["required_fact_keys"], f"步骤 {step_number} alternative required_fact_keys")
                for fact_key in logic_facts(branch["condition_logic"]):
                    validate_fact_key_not_placeholder(fact_key, f"{step_label} alternative fact")
        for relation in step["exception_relations"]:
            for fact_key in logic_facts(relation["condition_logic"]):
                validate_fact_key_not_placeholder(fact_key, f"{step_label} exception fact")


def contains_operator(node: dict[str, Any], operator: str) -> bool:
    if node.get("operator") == operator:
        return True
    return any(contains_operator(item, operator) for item in node.get("operands", []))


def and_logic(nodes: list[dict[str, Any]]) -> dict[str, Any]:
    nodes = [node for node in nodes if node]
    if len(nodes) == 1:
        return nodes[0]
    return {"operator": "AND", "operands": nodes}


def or_logic(nodes: list[dict[str, Any]]) -> dict[str, Any]:
    if len(nodes) == 1:
        return nodes[0]
    return {"operator": "OR", "operands": nodes}


def effective_review(batch: dict[str, Any]) -> tuple[str, str]:
    features = set(batch["chapter_features"])
    if features & HIGH_RISK_FEATURES:
        return "full", "包含大运流年、多星同聚或复杂瑜伽，强制逐步全审"
    if batch["requested_review"] != "sample":
        return "full", "工作单要求逐步全审"
    if features != {"simple_house_placement"}:
        return "full", "只有结构单一的落宫章节允许抽审"
    if batch["consecutive_clean_batches"] < 3:
        return "full", "尚未连续三个批次零新异议"
    if batch["review_cycle_position"] == 3:
        return "full", "高速挡每三个批次强制全审一个批次"
    return "sample", "简单落宫章节且已连续三个批次零新异议"


def validate_claim(step_label: str, step: dict[str, Any], evidence_quotes: str) -> list[dict[str, str]]:
    claim = step["minimum_supported_claim"].strip()
    lowered = claim.casefold()
    matched = [fragment for fragment in EMPTY_CLAIM_FRAGMENTS if fragment.casefold() in lowered]
    if matched:
        raise BuildError(f"{step_label} 的最小意思是空话模板：{matched[0]}")
    pairs: list[tuple[str, str]] = []
    for lane in ("conditions", "results"):
        for pair in step["claim_terms"][lane]:
            if pair["quote"] not in evidence_quotes:
                raise BuildError(f"{step_label} 的 claim_terms.{lane} 引文词不在逐字短引中：{pair['quote']}")
            if pair["claim"] not in claim:
                raise BuildError(f"{step_label} 的 claim_terms.{lane} 主张词不在最小意思中：{pair['claim']}")
            pairs.append((pair["quote"], pair["claim"]))
    # 方案 C（Q15）：逐字短引中的专名／数值／单位／时间词必须进入 claim_terms 映射；
    # 映射行写入差异表，交独立审计按清单逐词单选确认（Q21）。
    rows, uncovered = map_high_risk_terms(detect_high_risk_terms(evidence_quotes), pairs)
    if uncovered:
        raise BuildError(
            f"{step_label} 的逐字短引含未映射的高风险词（专名／数值／单位／时间词）：{uncovered}"
        )
    return rows


def validate_method_semantics(
    method: dict[str, Any], atoms: dict[str, dict], source_scope: set[str], book_strategy: str
) -> dict[str, list[dict[str, str]]]:
    method_id = method["method"]
    high_risk_terms_by_step: dict[str, list[dict[str, str]]] = {}
    facts = method["facts"]
    validate_method_fact_keys(method)
    fact_items = {item["key"]: item for item in facts}
    if len(fact_items) != len(facts):
        raise BuildError(f"方法 {method_id} 的 facts 存在重复 key")
    always_facts = {key for key, item in fact_items.items() if item["availability"] == "always"}
    conditional_facts = {key for key, item in fact_items.items() if item["availability"] == "conditional"}
    produced: set[str] = set()
    for step_number, step in enumerate(method["steps"], 1):
        label = f"方法 {method_id} 步骤 {step_number}"
        required = set(step["required_fact_keys"])
        if required - always_facts - produced:
            raise BuildError(f"{label} 使用了未声明的固定事实：{sorted(required - always_facts - produced)}")
        base_facts = logic_facts(step["condition_logic"])
        if not required.issubset(base_facts):
            raise BuildError(f"{label} 的 condition_logic 没有覆盖全部 required_fact_keys")
        if contains_operator(step["condition_logic"], "OR"):
            raise BuildError(f"{label} 的 OR 必须写进 alternative_groups，不能平铺在 condition_logic")

        all_branch_logic_facts: set[str] = set()
        group_ids: set[str] = set()
        for group in step["alternative_groups"]:
            if group["group_id"] in group_ids:
                raise BuildError(f"{label} 的 alternative_groups 存在重复 group_id：{group['group_id']}")
            group_ids.add(group["group_id"])
            branch_ids: set[str] = set()
            for branch in group["branches"]:
                if branch["branch_id"] in branch_ids:
                    raise BuildError(f"{label} 的分支编号重复：{branch['branch_id']}")
                branch_ids.add(branch["branch_id"])
                branch_required = set(branch["required_fact_keys"])
                if branch_required - conditional_facts - produced:
                    raise BuildError(
                        f"{label} 分支 {branch['branch_id']} 使用了未声明的按分支事实："
                        f"{sorted(branch_required - conditional_facts - produced)}"
                    )
                branch_logic_facts = logic_facts(branch["condition_logic"])
                if not branch_logic_facts.issubset(branch_required | produced):
                    raise BuildError(f"{label} 分支 {branch['branch_id']} 的条件引用了分支外事实")
                if contains_operator(branch["condition_logic"], "OR"):
                    raise BuildError(f"{label} 分支 {branch['branch_id']} 内的 OR 必须继续拆成独立选择组")
                all_branch_logic_facts.update(branch_logic_facts)

        conditional_input_facts: set[str] = set()
        for group in step["conditional_requirements"]:
            when_facts = logic_facts(group["when"])
            if when_facts - required - produced:
                raise BuildError(f"{label} 的条件分支 when 引用了当前不可用事实")
            group_required = set(group["required_fact_keys"])
            if group_required - conditional_facts - produced:
                raise BuildError(f"{label} 的条件分支使用了未声明事实")
            conditional_input_facts.update(group_required)

        risk_logic_facts = base_facts | all_branch_logic_facts
        remedy_facts = {key for key, item in fact_items.items() if item["role"] == "remedy_condition"}
        leaked_remedies = risk_logic_facts & remedy_facts
        if leaked_remedies:
            raise BuildError(f"{label} 把补救事实混入了风险成立条件：{sorted(leaked_remedies)}")

        concession_facts = set().union(*(logic_facts(node) for node in step["concession_conditions"]))
        leaked_concessions = concession_facts & risk_logic_facts
        if leaked_concessions:
            raise BuildError(f"{label} 把 even if 让步条件写成了成立前提：{sorted(leaked_concessions)}")

        time_scope = step["time_scope"]
        if time_scope["kind"] == "phase":
            phase_facts = set(time_scope["fact_keys"])
            if not phase_facts.issubset(risk_logic_facts):
                raise BuildError(f"{label} 的阶段事实没有挂到对应条件分支：{sorted(phase_facts - risk_logic_facts)}")
            wrong_roles = {key for key in phase_facts if fact_items.get(key, {}).get("role") != "phase_condition"}
            if wrong_roles:
                raise BuildError(f"{label} 的阶段事实没有标记为 phase_condition：{sorted(wrong_roles)}")

        if step["context_reference"] and not step["context_bindings"]:
            raise BuildError(f"{label} 存在代词或承接关系，但没有绑定前置原文")
        for atom_id in step["context_bindings"]:
            if atom_id not in source_scope or atom_id not in atoms:
                raise BuildError(f"{label} 的前置原文绑定不在本批正式范围：{atom_id}")

        evidence_quotes = []
        for evidence in step["evidence"]:
            atom_id = evidence["evidence_atom_id"]
            atom = atoms.get(atom_id)
            if atom_id not in source_scope or atom is None:
                raise BuildError(f"{label} 引用了本批范围外的原文：{atom_id}")
            content_role = atom.get("content_role")
            case_only = method["generalization_scope"] == "single_case_only"
            allowed_case = book_strategy == "case_book" and case_only and content_role == "case"
            if content_role not in METHOD_EVIDENCE_CONTENT_ROLES and not allowed_case:
                raise BuildError(f"{label} 引用了不能作为通用方法证据的原文身份：{atom_id}")
            quote = evidence["quote"]
            if quote not in atom.get("exact_text", ""):
                raise BuildError(f"{label} 的逐字短引不在正式原文中：{atom_id}")
            evidence_quotes.append(quote)
        detected_terms = validate_claim(label, step, "\n".join(evidence_quotes))
        if detected_terms:
            high_risk_terms_by_step[f"{method_id}.step-{step_number:03d}"] = detected_terms

        for relation in step["exception_relations"]:
            relation_facts = logic_facts(relation["condition_logic"])
            if relation["type"] in {"mitigation", "cancellation"} and not relation_facts & remedy_facts:
                raise BuildError(f"{label} 的补救或取消关系没有绑定 remedy_condition 事实")
            for atom_id in relation["evidence_atom_ids"]:
                if atom_id not in source_scope or atom_id not in atoms:
                    raise BuildError(f"{label} 的例外关系引用了范围外原文：{atom_id}")

        new_produced = set(step["produced_fact_keys"])
        if new_produced & (set(fact_items) | produced):
            raise BuildError(f"{label} 的 produced_fact_keys 与输入或前序产出重复")
        produced.update(new_produced)
    return high_risk_terms_by_step


def evidence_refs(step: dict[str, Any], atoms: dict[str, dict]) -> list[dict[str, Any]]:
    return [
        {
            "evidence_atom_id": item["evidence_atom_id"],
            "quote": item["quote"],
            "pdf_pages": atoms[item["evidence_atom_id"]]["pdf_pages"],
        }
        for item in step["evidence"]
    ]


def assemble_step(method_id: str, number: int, step: dict[str, Any], atoms: dict[str, dict]) -> dict[str, Any]:
    base_logic = step["condition_logic"]
    condition_nodes = [base_logic]
    conditional_requirements = [
        {
            "when": item["when"],
            "required_fact_keys": item["required_fact_keys"],
            "stop_condition": "命中该条件分支后，缺少以下事实即停止：" + "、".join(item["required_fact_keys"]) + "。",
        }
        for item in step["conditional_requirements"]
    ]
    for group in step["alternative_groups"]:
        selection_group = f"{method_id}.step-{number:03d}:{group['group_id']}"
        branch_nodes = [branch["condition_logic"] for branch in group["branches"]]
        condition_nodes.append(or_logic(branch_nodes))
        for branch in group["branches"]:
            conditional_requirements.append(
                {
                    "when": base_logic,
                    "required_fact_keys": branch["required_fact_keys"],
                    "branch_condition_logic": branch["condition_logic"],
                    "selection_group": selection_group,
                    "stop_condition": "选中该分支后，缺少以下事实即停止："
                    + "、".join(branch["required_fact_keys"])
                    + "。",
                }
            )
    required = step["required_fact_keys"]
    assembled = {
        "step_id": f"{method_id}.step-{number:03d}",
        "action": step["action"],
        "applicability_scope": step["applicability_scope"],
        "minimum_supported_claim": step["minimum_supported_claim"],
        "produced_fact_keys": step["produced_fact_keys"],
        "required_fact_keys": required,
        "condition_logic": and_logic(condition_nodes),
        "conditional_fact_requirements": conditional_requirements,
        "source_status": step["source_status"],
        # 保留条件词／结果词映射：验证器据此区分"条件里的或"（必须拆分支）和
        # "结果里的或"（如 loss of younger brothers and/or sisters，是结果本身模糊），
        # 独立审计也据此逐词确认高风险词。
        "claim_terms": step["claim_terms"],
        "evidence_refs": evidence_refs(step, atoms),
        "stop_condition": "缺少以下固定事实即停止：" + "、".join(required) + "。",
        "stop_fact_keys": list(required),
        "exception_relations": step["exception_relations"],
        "forbidden_extensions": step["forbidden_extensions"],
    }
    # Q1：步骤级内容指纹。审计凭证逐步骤绑定 step_hash；
    # 改第 7 步只让第 7 步的凭证失效，其余步骤"已通过"保持有效。
    assembled["step_hash"] = compute_step_hash(assembled)
    return assembled


def assemble(extraction: dict[str, Any], atoms: dict[str, dict]) -> tuple[dict[str, Any], dict[str, Any]]:
    batch = extraction["batch"]
    source_scope = set(extraction["source_scope"])
    missing_scope = source_scope - set(atoms)
    if missing_scope:
        raise BuildError(f"本批 source_scope 含不存在的正式原文编号：{sorted(missing_scope)}")
    source_records = extraction["source_records"]
    source_record_ids = [item["evidence_atom_id"] for item in source_records]
    if len(set(source_record_ids)) != len(source_record_ids) or set(source_record_ids) != source_scope:
        raise BuildError("source_records 必须与 source_scope 逐编号完全一致且不能重复")
    method_ids = [item["method"] for item in extraction["methods"]]
    if len(set(method_ids)) != len(method_ids):
        raise BuildError("AI 抽取 JSON 含重复方法编号")

    high_risk_terms: dict[str, list[dict[str, str]]] = {}
    for method in extraction["methods"]:
        if batch["book_strategy"] == "rule_book" and method["generalization_scope"] != "general_rule":
            raise BuildError(f"规则书方法 {method['method']} 不能标成 single_case_only")
        high_risk_terms.update(
            validate_method_semantics(method, atoms, source_scope, batch["book_strategy"])
        )
    claims = [
        " ".join(step["minimum_supported_claim"].split()).casefold()
        for method in extraction["methods"]
        for step in method["steps"]
    ]
    repeated = sorted(claim for claim, count in Counter(claims).items() if count >= 3)
    if repeated:
        raise BuildError(f"同一批次至少三个步骤重复同一句最小意思：{repeated[0]}")

    review_mode, review_reason = effective_review(batch)
    methods = []
    for method in extraction["methods"]:
        facts = method["facts"]
        method_output = {
            "method": method["method"],
            "title": method["title"],
            "generalization_scope": method["generalization_scope"],
            "pilot_only": batch["pilot_only"],
            "publishable": False,
            "workflow_status": "pilot_candidate",
            "workflow_history": ["pilot_candidate"],
            "source_status": method["source_status"],
            "fact_binding_status": method["fact_binding_status"],
            "upstream_issue_ids": method["upstream_issue_ids"],
            "user_intents": method["user_intents"],
            "required_facts": [item["key"] for item in facts if item["availability"] == "always"],
            "conditional_facts": [item["key"] for item in facts if item["availability"] == "conditional"],
            "dependencies": method["dependencies"],
            "steps": [
                assemble_step(method["method"], number, step, atoms)
                for number, step in enumerate(method["steps"], 1)
            ],
            "retrieval_plan": method["retrieval_plan"],
            "stop_conditions": method["stop_conditions"],
            "executable_in_pilot": False,
            # Q17 留插座：PVR（整盘步骤脊梁）未加工前一律 null，不猜结构。
            "spine_slot_hint": method["spine_slot_hint"],
        }
        if "target_house" in method:
            method_output["target_house"] = method["target_house"]
        methods.append(method_output)
    refs_by_atom: dict[str, set[str]] = {}
    for method in methods:
        for step in method["steps"]:
            for ref in step["evidence_refs"]:
                refs_by_atom.setdefault(ref["evidence_atom_id"], set()).add(method["method"])
    # 原文去向：默认每条都要进方法步骤；但书里确实存在过渡句、章节引言和收尾语这类
    # 没有判断规则的正文（例："三宫已讲完，现在听四宫"）。这类原文必须显式声明
    # 非 method_step 的去向，既不许被方法引用，也不再被当成"漏做的方法"。
    dispositions = {
        record["evidence_atom_id"]: record.get("disposition", "method_step")
        for record in source_records
    }
    method_step_scope = {atom_id for atom_id in source_scope if dispositions[atom_id] == "method_step"}
    unused_scope = method_step_scope - set(refs_by_atom)
    if unused_scope:
        raise BuildError(f"本批候选原文没有进入任何方法步骤：{sorted(unused_scope)}")
    wrongly_used = {atom_id for atom_id in refs_by_atom if dispositions.get(atom_id) != "method_step"}
    if wrongly_used:
        raise BuildError(
            f"声明为非方法去向的原文却被方法步骤引用：{sorted(wrongly_used)}"
        )
    step_ids = [step["step_id"] for method in methods for step in method["steps"]]
    if review_mode == "full":
        audit_step_ids = sorted(step_ids)
    else:
        sample_size = max(1, math.ceil(len(step_ids) * 0.2))
        audit_step_ids = sorted(random.Random(batch["batch_id"]).sample(sorted(step_ids), sample_size))

    output = {
        "schema_version": "judgment-method-recipes/v2",
        "pilot_only": batch["pilot_only"],
        "publishable": False,
        "generation": {
            "generator": GENERATOR_ID,
            "generator_version": GENERATOR_VERSION,
            "extraction_schema": extraction["schema_version"],
            "batch_id": batch["batch_id"],
            "chapter_features": batch["chapter_features"],
            "book_strategy": batch["book_strategy"],
            "review_mode": review_mode,
            "review_reason": review_reason,
            "source_scope_count": len(source_scope),
            "audit_step_ids": audit_step_ids,
            "high_risk_terms": high_risk_terms,
        },
        "methods": methods,
    }
    report = {
        "passed": True,
        "generator": GENERATOR_ID,
        "generator_version": GENERATOR_VERSION,
        "batch_id": batch["batch_id"],
        "review_mode": review_mode,
        "review_reason": review_reason,
        "audit_step_ids": audit_step_ids,
        "high_risk_terms": high_risk_terms,
        "methods": len(methods),
        "steps": sum(len(item["steps"]) for item in methods),
        "source_scope_count": len(source_scope),
        "executable_methods": 0,
        "errors": [],
    }
    return output, report


def build_query_recipes(method_data: dict[str, Any]) -> dict[str, Any]:
    topics = {}
    for method in method_data["methods"]:
        topics[method["method"]] = {
            "title": method["title"],
            "user_intents": method["user_intents"],
            "method_ids": [],
            "candidate_method_ids": [method["method"]],
            "execution_allowed": False,
            "required_facts": method["required_facts"],
            "conditional_facts": method["conditional_facts"],
            "fact_binding_status": method["fact_binding_status"],
            **method["retrieval_plan"],
            "stop_conditions": method["stop_conditions"],
        }
    return {
        "schema_version": "judgment-query-recipes/v2",
        "pilot_only": method_data["pilot_only"],
        "publishable": False,
        "topics": topics,
    }


def build_source_scan(extraction: dict[str, Any], method_data: dict[str, Any]) -> dict[str, Any]:
    refs_by_atom: dict[str, set[str]] = {}
    for method in method_data["methods"]:
        for step in method["steps"]:
            for ref in step["evidence_refs"]:
                refs_by_atom.setdefault(ref["evidence_atom_id"], set()).add(method["method"])
    records = []
    for source in extraction["source_records"]:
        atom_id = source["evidence_atom_id"]
        disposition = source.get("disposition", "method_step")
        records.append(
            {
                "evidence_atom_id": atom_id,
                "semantic_class": source["semantic_class"],
                "risk_flags": source["risk_flags"],
                "disposition": disposition,
                "method_ids": sorted(refs_by_atom[atom_id]) if disposition == "method_step" else [],
            }
        )
    return {
        "schema_version": "method-source-scan/v2",
        "pilot_only": extraction["batch"]["pilot_only"],
        "review_status": "complete",
        "atom_dispositions": records,
    }


def atomic_write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temp_name, path)
    except BaseException:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def batch_state(batch: dict[str, Any], report: dict[str, Any], recipe_sha256: str) -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    return {
        "schema_version": "judgment-batch-state/v2",
        "batch_id": batch["batch_id"],
        "current_state": "mechanical_testing",
        "review_mode": report["review_mode"],
        "audit_step_ids": report["audit_step_ids"],
        "method_recipes_sha256": recipe_sha256,
        "history": [
            {"state": "not_started", "recorded_at": now, "recorded_by": GENERATOR_ID},
            {"state": "generating", "recorded_at": now, "recorded_by": GENERATOR_ID},
            {"state": "mechanical_testing", "recorded_at": now, "recorded_by": GENERATOR_ID},
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="从强校验 AI 抽取 JSON 生成唯一方法机器配方")
    parser.add_argument("--extraction", required=True, type=Path, help="AI 结构化抽取 JSON")
    parser.add_argument("--accepted-package", required=True, type=Path, help="当前正式或试验书包凭证")
    parser.add_argument("--output", required=True, type=Path, help="新的 method-recipes.json 输出路径")
    parser.add_argument("--query-output", type=Path, help="查询配方；默认与方法配方同目录")
    parser.add_argument("--scan-output", type=Path, help="本批原文去向总账；默认写入 validation")
    parser.add_argument("--report", type=Path, help="机器生成报告；默认与输出文件同目录")
    parser.add_argument("--check-only", action="store_true", help="只校验，不写文件")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        extraction = load_json(args.extraction.resolve())
        validate_schema(extraction)
        atoms, _package = resolve_atoms(args.accepted_package.resolve(), extraction["batch"])
        output, report = assemble(extraction, atoms)
        if not args.check_only:
            output_path = args.output.resolve()
            standard_root = (
                output_path.parents[2]
                if output_path.name == "method-recipes.json"
                and output_path.parent.name == "navigation"
                and output_path.parent.parent.name == "references"
                else output_path.parent
            )
            report_path = (args.report or standard_root / "validation" / "build-methods-report.json").resolve()
            state_path = standard_root / "validation" / "batch-state.json"
            query_path = (args.query_output or output_path.with_name("query-recipes.json")).resolve()
            scan_path = (args.scan_output or standard_root / "validation" / "method-source-scan.json").resolve()
            for path in (output_path, query_path, scan_path, report_path, state_path):
                if path.exists():
                    raise BuildError(f"拒绝覆盖已有文件，请使用新的目标目录：{path}")
            atomic_write_json(output_path, output)
            atomic_write_json(query_path, build_query_recipes(output))
            atomic_write_json(scan_path, build_source_scan(extraction, output))
            atomic_write_json(report_path, report)
            atomic_write_json(state_path, batch_state(extraction["batch"], report, sha256(output_path)))
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except (BuildError, OSError) as exc:
        report = {"passed": False, "errors": [str(exc)]}
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
