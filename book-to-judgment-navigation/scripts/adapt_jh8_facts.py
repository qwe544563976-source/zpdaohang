#!/usr/bin/env python3
"""把 JH8 已计算事实整理为判断导航可消费的中文事实，不重新排盘。"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any


PLANETS = ("Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu")
SIGN_NAMES = (
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
)
RESOLVED_FACT_STATUSES = frozenset({"available", "not_applicable"})
UNRESOLVED_FACT_STATUSES = frozenset(
    {"partial", "unavailable", "unmapped", "caller_required", "method_or_rag_required"}
)


class AdapterError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise AdapterError(f"缺少 JH8 文件：{path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AdapterError(f"无法读取 JH8 文件 {path}：{exc}") from exc
    if not isinstance(value, dict):
        raise AdapterError(f"JH8 文件顶层必须是对象：{path}")
    return value


def need(value: Any, path: str) -> Any:
    current = value
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            raise AdapterError(f"JH8 缺少必需字段：{path}")
        current = current[part]
    return current


def record(status: str, value: Any = None, reason: str | None = None, *source_fields: str) -> dict[str, Any]:
    if status not in RESOLVED_FACT_STATUSES | UNRESOLVED_FACT_STATUSES:
        raise AdapterError(f"事实状态不合法：{status}")
    item: dict[str, Any] = {
        "status": status,
        "fact_state": (
            "known"
            if status == "available"
            else "not_applicable"
            if status == "not_applicable"
            else "unavailable"
            if status == "unavailable"
            else "unknown"
        ),
    }
    if value is not None:
        item["value"] = value
    if reason:
        item["reason"] = reason
    if source_fields:
        item["source_fields"] = list(source_fields)
    return item


def _fact_entry(facts: dict[str, dict[str, Any]], key: str) -> dict[str, Any]:
    item = facts.get(key)
    if isinstance(item, dict):
        return item
    return record("unmapped", reason="适配器尚未定义此事实")


def _fact_blocker(key: str, item: dict[str, Any]) -> dict[str, Any]:
    return {
        "fact": key,
        "status": item.get("status", "unmapped"),
        "fact_state": item.get("fact_state", "unknown"),
        "reason": item.get("reason", "必查事实没有取得可用值"),
    }


def _condition_state(
    node: Any,
    facts: dict[str, dict[str, Any]],
) -> tuple[str, set[str]]:
    """用现有条件树做三值判断：true、false 或 unknown。"""
    if not isinstance(node, dict):
        return "unknown", set()
    fact_key = node.get("fact_key")
    if isinstance(fact_key, str) and fact_key:
        item = _fact_entry(facts, fact_key)
        if item.get("status") == "not_applicable":
            return "false", set()
        if item.get("status") != "available":
            return "unknown", {fact_key}
        value = item.get("value")
        if isinstance(value, bool):
            return ("true" if value else "false"), set()
        # Presence-only facts (lord names, dates, phase labels, etc.) are
        # usable as a gate once their value is available.  Recipe branches
        # that need a boolean condition still emit a boolean fact value.
        if value is not None:
            return "true", set()
        return "unknown", {fact_key}
    operator = node.get("operator")
    operands = node.get("operands")
    if operator not in {"AND", "OR", "NOT"} or not isinstance(operands, list) or not operands:
        return "unknown", set()
    if operator == "NOT":
        state, unresolved = _condition_state(operands[0], facts)
        return ("unknown", unresolved) if state == "unknown" else ("false" if state == "true" else "true", set())
    states = [_condition_state(operand, facts) for operand in operands]
    values = [state for state, _ in states]
    unresolved = set().union(*(missing for _, missing in states))
    if operator == "AND":
        if "false" in values:
            return "false", set()
        if all(value == "true" for value in values):
            return "true", set()
        return "unknown", unresolved
    if "true" in values:
        return "true", set()
    if all(value == "false" for value in values):
        return "false", set()
    return "unknown", unresolved


def _append_blocker(blockers: list[dict[str, Any]], item: dict[str, Any]) -> None:
    key = item.get("fact")
    if not any(existing.get("fact") == key for existing in blockers):
        blockers.append(item)


def _conditional_missing_facts(
    groups: list[Any],
    facts: dict[str, dict[str, Any]],
) -> dict[str, str]:
    """Return only facts needed by the active conditional branch.

    A selection_group represents OR alternatives.  Once one branch is true,
    an unavailable fact belonging only to another branch must not block the
    selected branch.  Groups without a selection_group retain the legacy
    conditional requirement behavior.
    """
    missing: dict[str, str] = {}
    grouped: dict[str, list[dict[str, Any]]] = {}
    ungrouped: list[Any] = []

    for group in groups or []:
        if not isinstance(group, dict):
            missing["<conditional_when>"] = "条件分支格式无法从当前事实判定"
            continue
        selection_group = group.get("selection_group")
        if isinstance(selection_group, str) and selection_group:
            grouped.setdefault(selection_group, []).append(group)
        else:
            ungrouped.append(group)

    def add_unknown(keys: set[str], reason: str) -> None:
        for key in keys or {"<conditional_when>"}:
            missing.setdefault(key, reason)

    for group in ungrouped:
        when_state, when_missing = _condition_state(group.get("when"), facts)
        if when_state == "unknown":
            add_unknown(when_missing, "条件分支 when 无法从当前事实判定")
            continue
        if when_state != "true":
            continue
        for key in group.get("required_fact_keys", []) or []:
            item = _fact_entry(facts, key)
            if item.get("status") not in RESOLVED_FACT_STATUSES:
                missing.setdefault(key, "命中的条件分支缺少必查事实")

    for selection_group, candidates in grouped.items():
        when_states = [_condition_state(group.get("when"), facts) for group in candidates]
        if any(state == "unknown" for state, _ in when_states):
            unresolved = set().union(*(keys for state, keys in when_states if state == "unknown"))
            add_unknown(unresolved, f"选择组 {selection_group} 的前置条件无法判定")
            continue
        if not any(state == "true" for state, _ in when_states):
            continue

        active: list[dict[str, Any]] = []
        unresolved_branches: list[set[str]] = []
        for group in candidates:
            when_state, _ = _condition_state(group.get("when"), facts)
            if when_state != "true":
                # A branch is selectable only when its own prerequisite is
                # true; another branch's true prerequisite must not activate
                # this branch.
                continue
            condition = group.get("branch_condition_logic")
            if condition is None:
                # A selection group without explicit branch logic is a
                # malformed new recipe; do not guess which branch is active.
                missing.setdefault(
                    "<conditional_branch_logic>",
                    f"选择组 {selection_group} 缺少 branch_condition_logic",
                )
                continue
            state, unresolved = _condition_state(condition, facts)
            if state == "true":
                active.append(group)
            elif state == "unknown":
                unresolved_branches.append(unresolved)

        if active:
            for group in active:
                for key in group.get("required_fact_keys", []) or []:
                    item = _fact_entry(facts, key)
                    if item.get("status") not in RESOLVED_FACT_STATUSES:
                        missing.setdefault(key, "已命中的条件分支缺少必查事实")
        elif unresolved_branches:
            add_unknown(
                set().union(*unresolved_branches),
                f"选择组 {selection_group} 没有可确认的分支",
            )
        else:
            missing.setdefault(
                f"<selection_group:{selection_group}>",
                f"选择组 {selection_group} 的所有分支均不成立",
            )

    return missing


def build_method_gate(
    method: dict[str, Any],
    facts: dict[str, dict[str, Any]],
    methods_by_id: dict[str, dict[str, Any]] | None = None,
    _stack: frozenset[str] = frozenset(),
    target_house: int | None = None,
) -> dict[str, Any]:
    """只决定能否生成判断请求，不判断星盘含义。"""
    method_name = method.get("method")
    if not isinstance(method_name, str) or not method_name:
        return {
            "method": method_name,
            "required_fact_statuses": {},
            "conditional_fact_statuses": {},
            "blocking_facts": [],
            "authorization_blockers": [{"type": "method_authorization", "reason": "方法缺少 method 编号"}],
            "allowed": False,
        }
    if method_name in _stack:
        return {
            "method": method_name,
            "required_fact_statuses": {},
            "conditional_fact_statuses": {},
            "blocking_facts": [],
            "authorization_blockers": [{"type": "dependency", "reason": f"方法依赖形成循环：{method_name}"}],
            "allowed": False,
        }
    required_statuses = {
        key: _fact_entry(facts, key).get("status", "unmapped")
        for key in method.get("required_facts", [])
    }
    conditional_statuses = {
        key: _fact_entry(facts, key).get("status", "unmapped")
        for key in method.get("conditional_facts", [])
    }
    blockers = [
        _fact_blocker(key, _fact_entry(facts, key))
        for key, status in required_statuses.items()
        if status not in RESOLVED_FACT_STATUSES
    ]
    for step in method.get("steps", []):
        if not isinstance(step, dict):
            continue
        for key, reason in _conditional_missing_facts(
            step.get("conditional_fact_requirements", []) or [], facts
        ).items():
            _append_blocker(
                blockers,
                {
                    **_fact_blocker(key, _fact_entry(facts, key)),
                    "reason": reason,
                },
            )
    authorization_blockers: list[dict[str, Any]] = []
    if method.get("fact_binding_status") != "mapped":
        authorization_blockers.append({
            "type": "method_authorization",
            "reason": "方法的 fact_binding_status 不是 mapped，不能进入判断主路",
        })
    if method.get("executable_in_pilot") is not True:
        authorization_blockers.append({
            "type": "method_authorization",
            "reason": "方法没有明确 executable_in_pilot=true，不能生成判断请求",
        })
    if method.get("execution_allowed") is False:
        authorization_blockers.append({
            "type": "method_authorization",
            "reason": "方法明确禁止执行",
        })
    declared_target_house = method.get("target_house")
    if declared_target_house is not None:
        if isinstance(declared_target_house, bool) or not isinstance(declared_target_house, int):
            authorization_blockers.append({
                "type": "target_house_mismatch",
                "reason": "方法声明的 target_house 必须是整数",
            })
        elif target_house is None:
            authorization_blockers.append({
                "type": "target_house_mismatch",
                "reason": f"方法声明 target_house={declared_target_house}，当前 gate 没有实际 target_house，无法确认宫位匹配",
            })
        elif declared_target_house != target_house:
            authorization_blockers.append({
                "type": "target_house_mismatch",
                "reason": f"方法声明 target_house={declared_target_house}，但 CLI 实际 target_house={target_house}，拒绝把其他宫位事实喂给该方法",
            })
    for issue_id in method.get("upstream_issue_ids", []):
        authorization_blockers.append({
            "type": "upstream_issue",
            "reason": f"方法仍有未解决的上游问题：{issue_id}",
        })
    if methods_by_id:
        for dependency in method.get("dependencies", []):
            dependency_method = methods_by_id.get(dependency)
            if dependency_method is None:
                authorization_blockers.append({
                    "type": "dependency",
                    "reason": f"找不到依赖方法：{dependency}",
                })
            else:
                dependency_gate = build_method_gate(
                    dependency_method,
                    facts,
                    methods_by_id,
                    _stack | {method_name},
                    target_house=target_house,
                )
                if dependency_gate["allowed"]:
                    continue
                authorization_blockers.append({
                    "type": "dependency",
                    "reason": f"依赖方法尚未获准执行：{dependency}",
                })
    return {
        "method": method_name,
        "required_fact_statuses": required_statuses,
        "conditional_fact_statuses": conditional_statuses,
        "blocking_facts": blockers,
        "authorization_blockers": authorization_blockers,
        "allowed": not blockers and not authorization_blockers,
    }


def build_stop_output(
    facts: dict[str, dict[str, Any]],
    gate: dict[str, Any] | None,
    extra_reasons: list[str] | None = None,
) -> dict[str, Any]:
    confirmed = []
    if gate:
        for key, status in gate.get("required_fact_statuses", {}).items():
            if status in RESOLVED_FACT_STATUSES:
                item = _fact_entry(facts, key)
                confirmed.append({"fact": key, "value": item.get("value"), "status": status})
    blockers = list(gate.get("blocking_facts", [])) if gate else []
    reasons = [item.get("reason", "必查事实未解决") for item in blockers]
    reasons.extend(item.get("reason", "执行授权未满足") for item in (gate or {}).get("authorization_blockers", []))
    reasons.extend(extra_reasons or [])
    return {
        "confirmed_facts": confirmed,
        "missing_key_facts": blockers,
        "why_stopped": list(dict.fromkeys(reasons)),
        "prohibited_conclusions": [
            "不得判断吉凶",
            "不得判断成败或兑现时间",
            "不得补写人物故事、事件剧情或因果解释",
        ],
    }


def build_judgment_request(
    method_id: str | None,
    facts: dict[str, dict[str, Any]],
    gate: dict[str, Any] | None,
) -> dict[str, Any] | None:
    if not method_id or not gate or gate.get("allowed") is not True:
        return None
    return {
        "method": method_id,
        "facts": facts,
        "instruction": "只依据已提供事实和真实原文返回；不得补写缺失事实，不得把未知当成不满足。",
    }


def active_period(rows: list[dict[str, Any]], as_of: date) -> dict[str, Any] | None:
    for item in rows:
        try:
            start = date.fromisoformat(item["start"])
            end = date.fromisoformat(item["end"])
        except (KeyError, TypeError, ValueError):
            continue
        if start <= as_of < end:
            return item
    return None


def period_view(item: dict[str, Any] | None) -> dict[str, Any] | None:
    if not item:
        return None
    return {key: item[key] for key in ("lord", "start", "end", "start_datetime_local", "end_datetime_local") if key in item}


def period_phase(item: dict[str, Any], as_of: date) -> str:
    start = date.fromisoformat(item["start"])
    end = date.fromisoformat(item["end"])
    ratio = (as_of - start).days / max(1, (end - start).days)
    return "前段" if ratio < 1 / 3 else "中段" if ratio < 2 / 3 else "后段"


def load_jh8(chart_dir: Path) -> dict[str, Any]:
    full_path = chart_dir / "01_命盘完整包.json"
    light_path = chart_dir / "02_命盘轻量包.json"
    detail_path = chart_dir / "资料柜" / "细节包.json"
    closure_path = chart_dir / "资料柜" / "命盘闭环验收.json"
    full = load_json(full_path)
    light = load_json(light_path)
    detail = load_json(detail_path)
    closure = load_json(closure_path)

    if full.get("package_role") != "formal_jh8_facts" or full.get("status") != "PASS":
        raise AdapterError("01_命盘完整包.json 不是状态为 PASS 的正式 JH8 事实包")
    if light.get("package_role") != "formal_jh8_facts" or light.get("status") != "PASS":
        raise AdapterError("02_命盘轻量包.json 不是状态为 PASS 的正式 JH8 事实包")

    full_facts = need(full, "formal_selected_fields")
    facts = need(light, "formal_selected_fields")
    bodies = need(facts, "d1.bodies")
    asc_idx = need(bodies, "Asc.sign_idx")
    if not isinstance(asc_idx, int):
        raise AdapterError("JH8 上升星座编号不是整数")

    for name, body in bodies.items():
        if not isinstance(body, dict) or "sign_idx" not in body or "rasi_house_whole_sign" not in body:
            raise AdapterError(f"JH8 D1 行星字段不完整：{name}")
        expected_house = (body["sign_idx"] - asc_idx) % 12 + 1
        if body["rasi_house_whole_sign"] != expected_house:
            raise AdapterError(
                f"JH8 D1 落宫自相矛盾：{name} 写成第 {body['rasi_house_whole_sign']} 宫，"
                f"按星座与上升应为第 {expected_house} 宫"
            )

    lord_rows = need(detail, "raw_facts_v2.house_lords.D1.rows")
    if not isinstance(lord_rows, list):
        raise AdapterError("JH8 宫主表 rows 不是数组")
    houses = {row.get("house"): row for row in lord_rows if isinstance(row, dict)}
    if set(houses) != set(range(1, 13)):
        raise AdapterError("JH8 宫主表没有完整覆盖第 1～12 宫")
    for house, row in houses.items():
        expected_sign = (asc_idx + house - 1) % 12
        lord = row.get("lord")
        if row.get("final_allowed") is not True or row.get("sign_idx") != expected_sign:
            raise AdapterError(f"JH8 第 {house} 宫宫主记录未获正式使用或星座不一致")
        if lord not in bodies or row.get("lord_sign_idx") != bodies[lord].get("sign_idx"):
            raise AdapterError(f"JH8 第 {house} 宫宫主 {lord} 的位置与 D1 不一致")

    return {
        "full_path": full_path,
        "light_path": light_path,
        "detail_path": detail_path,
        "closure_path": closure_path,
        "bodies": bodies,
        "houses": houses,
        "d9": need(facts, "vargas.D9"),
        "shadbala": need(detail, "shadbala.rows"),
        "vimshottari": need(full_facts, "dashas.vimshottari"),
        "closure": closure,
    }


def adapt(
    chart_dir: Path,
    target_house: int,
    as_of: date,
    recipes_path: Path | None = None,
    method_id: str | None = None,
) -> dict[str, Any]:
    if target_house not in range(1, 13):
        raise AdapterError("目标宫位必须是 1～12")
    source = load_jh8(chart_dir)
    bodies = source["bodies"]
    houses = source["houses"]
    d9 = source["d9"]
    shadbala = source["shadbala"]
    asc_idx = need(bodies, "Asc.sign_idx")
    d9_asc = need(d9, "Asc.sign_idx")

    def strength(name: str) -> dict[str, Any] | None:
        row = shadbala.get(name)
        if not isinstance(row, dict):
            return None
        pct = row.get("strength_pct")
        return {
            "rupas": row.get("rupas"),
            "required_rupas": row.get("final_aggregate_4bc2d0_required_rupa_table"),
            "strength_pct": pct,
            "meets_minimum": isinstance(pct, (int, float)) and pct >= 100,
        }

    def planet_state(name: str) -> dict[str, Any]:
        body = bodies[name]
        d9_body = d9.get(name, {})
        d9_sign_idx = d9_body.get("sign_idx")
        return {
            "planet": name,
            "d1_sign": body.get("sign"),
            "d1_house": body.get("rasi_house_whole_sign"),
            "retrograde": body.get("retrograde"),
            "dignity_states": need(body, "dignity.states"),
            "d9_sign": d9_body.get("sign"),
            "d9_house": ((d9_sign_idx - d9_asc) % 12 + 1) if isinstance(d9_sign_idx, int) else None,
            "shadbala": strength(name),
        }

    def occupants(house: int) -> list[str]:
        return [name for name in PLANETS if bodies.get(name, {}).get("rasi_house_whole_sign") == house]

    def lordships(name: str) -> list[int]:
        return [house for house, row in houses.items() if row["lord"] == name]

    def house_state(house: int) -> dict[str, Any]:
        row = houses[house]
        return {
            "house": house,
            "sign": row["sign"],
            "occupants": occupants(house),
            "lord": row["lord"],
            "lord_state": planet_state(row["lord"]),
        }

    target_lord = houses[target_house]["lord"]
    target_lord_state = planet_state(target_lord)
    current_md = active_period(need(source["vimshottari"], "mahadasha_timeline"), as_of)
    current_ad = active_period(current_md.get("antardasha", []), as_of) if current_md else None
    current_pd = active_period(current_ad.get("pratyantardasha", []), as_of) if current_ad else None
    current_sd = active_period(current_pd.get("sookshma", []), as_of) if current_pd else None
    period_lord = current_md.get("lord") if current_md else None

    facts: dict[str, dict[str, Any]] = {}

    def put(key: str, item: dict[str, Any]) -> None:
        facts[key] = item

    put("用户问题的生活主题", record("caller_required", reason="由问题分类步骤提供，不属于排盘事实"))
    put("财富问题类型", record("caller_required", reason="由问题分类步骤提供，不属于排盘事实"))
    put("运期问题类型", record("caller_required", reason="由问题分类步骤提供，不属于排盘事实"))
    put("目标宫位", record("available", target_house, None, "输入参数 target_house"))
    target_sign_idx = (asc_idx + target_house - 1) % 12
    target_sign_name = SIGN_NAMES[target_sign_idx]
    put(
        "目标宫位使用的计算口径及实际覆盖星座",
        record(
            "available",
            f"整宫制 (Whole Sign)，第 {target_house} 宫对应 {target_sign_name}",
            None,
            "formal_selected_fields.d1.bodies.Asc.sign_idx",
            "formal_selected_fields.d1.bodies.Asc.rasi_house_whole_sign",
            "formal_selected_fields.d1.bodies.*.rasi_house_whole_sign",
        ),
    )
    put("目标宫位内行星", record("available", occupants(target_house), None, "formal_selected_fields.d1.bodies"))
    put("目标宫位所受相位", record("unavailable", reason="等待 JH8 正式交付可用于最终判断的宫位照射矩阵"))
    put("相关行星的吉凶分类依据", record("unavailable", reason="JH8 闭环检查仍缺功能吉凶，天然吉凶也只有部分字段"))
    put("目标宫位对应的自然征象星", record("method_or_rag_required", reason="由已核验方法或原文确定，不由排盘器猜测"))
    put("自然征象星参考宫位的状态", record("method_or_rag_required", reason="先由方法确定自然征象星及参考位置后才能提取"))
    put("目标宫主", record("available", target_lord, None, "raw_facts_v2.house_lords.D1.rows"))
    put("目标宫主落宫", record("available", target_lord_state["d1_house"], None, f"formal_selected_fields.d1.bodies.{target_lord}.rasi_house_whole_sign"))
    target_strength = target_lord_state["shadbala"]
    put(
        "目标宫主强弱",
        record("available", target_strength, None, f"shadbala.rows.{target_lord}")
        if target_strength
        else record("unavailable", reason=f"JH8 没有 {target_lord} 的六力记录"),
    )
    put("目标宫主的全部宫主身份", record("available", lordships(target_lord), None, "raw_facts_v2.house_lords.D1.rows"))
    put(
        "目标宫主是否主管两个宫位",
        record(
            "available",
            len(lordships(target_lord)) == 2,
            None,
            "raw_facts_v2.house_lords.D1.rows",
        ),
    )
    put(
        "目标宫主强弱档位（原书三档）",
        record(
            "method_or_rag_required",
            reason="JH8 六力百分比没有 BPHS 原文 full、medium、negligible 三档的映射阈值；不能由百分比猜原书档位",
        ),
    )
    put(
        "双重宫主两项原文证据",
        record(
            "method_or_rag_required",
            reason="两项宫主结果必须由方法或 RAG 分别取回原文后对照；适配器不能把语义证据压成布尔值",
        ),
    )
    put("目标宫主两项宫主结果是否冲突", record("method_or_rag_required", reason="必须先取得两项原文结果，不能由排盘器判断语义冲突"))
    put(
        "目标宫主是否入本宫或擢升",
        record(
            "available",
            {
                "in_target_house": target_lord_state["d1_house"] == target_house,
                "in_own_sign": bool(need(bodies[target_lord], "dignity.own_sign_4ae4e0")),
                "exalted": "Exalted" in target_lord_state["dignity_states"],
            },
            None,
            f"formal_selected_fields.d1.bodies.{target_lord}",
        ),
    )

    for house, key, lord_key in (
        (2, "第二宫状态", "第二宫主状态与强弱"),
        (11, "第十一宫状态", "第十一宫主状态与强弱"),
    ):
        state = house_state(house)
        put(key, record("partial", state, "已取得落星和宫主；宫位照射与吉凶分类仍待 JH8 正式字段", "formal_selected_fields.d1.bodies", "raw_facts_v2.house_lords.D1.rows"))
        put(lord_key, record("available", state["lord_state"], None, f"shadbala.rows.{state['lord']}"))

    for house, key in ((5, "第五宫主状态"), (9, "第九宫主状态")):
        lord = houses[house]["lord"]
        put(key, record("available", planet_state(lord), None, "raw_facts_v2.house_lords.D1.rows", f"formal_selected_fields.d1.bodies.{lord}", f"shadbala.rows.{lord}"))

    wealth_lords = {houses[5]["lord"], houses[9]["lord"]}
    joined = {
        lord: [name for name in occupants(bodies[lord]["rasi_house_whole_sign"]) if name != lord]
        for lord in sorted(wealth_lords)
    }
    put("与第五宫主或第九宫主结合的行星", record("available", joined, None, "formal_selected_fields.d1.bodies"))
    for key in ("财富组合的全部成立条件", "贫困组合的全部成立条件", "贫困组合的取消条件", "其他财富组合", "其他贫困组合", "专题具体规则的全部联合条件", "相关专题的本命承诺"):
        put(key, record("method_or_rag_required", reason="必须从已核验方法和 RAG 原文取得，排盘器不生成古籍条件"))
    put("支持与反对结果所涉行星的强弱", record("method_or_rag_required", reason="先由 RAG 确定涉及哪些行星，再从六力表逐颗取得"))

    put("采用的运期系统", record("available", "Vimshottari", None, "formal_selected_fields.dashas.vimshottari"))
    put("当前大运或星座运", record("available", period_view(current_md), None, "formal_selected_fields.dashas.vimshottari.mahadasha_timeline") if current_md else record("unavailable", reason="指定日期不在 JH8 大运时间线内"))
    put("当前小运或星座分运", record("available", period_view(current_ad), None, "formal_selected_fields.dashas.vimshottari.mahadasha_timeline[].antardasha") if current_ad else record("unavailable", reason="指定日期没有匹配的小运"))
    put("相关大运或分运", record("available", {"mahadasha": period_view(current_md), "antardasha": period_view(current_ad), "pratyantardasha": period_view(current_pd), "sookshma": period_view(current_sd)}, None, "formal_selected_fields.dashas.vimshottari"))
    put("当月细运", record("available", {"pratyantardasha": period_view(current_pd), "sookshma": period_view(current_sd)}, None, "formal_selected_fields.dashas.vimshottari") if current_pd else record("unavailable", reason="指定日期没有匹配的细运"))

    if period_lord and period_lord in bodies:
        period_state = planet_state(period_lord)
        put("运主本命落宫", record("available", period_state["d1_house"], None, f"formal_selected_fields.d1.bodies.{period_lord}.rasi_house_whole_sign"))
        put("运主是否逆行", record("available", period_state["retrograde"], None, f"formal_selected_fields.d1.bodies.{period_lord}.retrograde"))
        drekkana = int(bodies[period_lord]["degree"] // 10) + 1
        put("运主所在 Dreshkan", record("available", drekkana, None, f"formal_selected_fields.d1.bodies.{period_lord}.degree"))
        put("运主或星座主强弱", record("available", period_state["shadbala"], None, f"shadbala.rows.{period_lord}") if period_state["shadbala"] else record("unavailable", reason=f"JH8 六力只含七颗可见行星，没有 {period_lord}"))
    else:
        for key in ("运主本命落宫", "运主是否逆行", "运主所在 Dreshkan", "运主或星座主强弱"):
            put(key, record("unavailable", reason="没有取得当前运主"))

    phase_value = period_phase(current_md, as_of) if current_md else None
    put("当前处于运期前段中段或后段", record("available", phase_value, None, "当前日期与大运起止日期") if current_md else record("unavailable", reason="没有取得当前大运"))
    for phase_key, expected in (
        ("current_antardasha_phase_commencement", "前段"),
        ("current_antardasha_phase_middle", "中段"),
        ("current_antardasha_phase_end", "后段"),
        ("current_antardasha_phase_later", "后段"),
    ):
        put(
            phase_key,
            record("available", phase_value == expected, None, "当前日期与大运起止日期")
            if current_md
            else record("unavailable", reason="没有取得当前大运"),
        )
    put("运期开始时运主落宫", record("unavailable", reason="等待 JH8 提供运期开始时的实际行星落位"))
    put("运主与其他行星的关系", record("unavailable", reason="等待 JH8 提供可用于最终判断的行星关系字段"))
    put("分运星座是否落六八十二宫", record("not_applicable", reason="当前采用行星维姆绍塔里运，不是星座运"))
    put("分运星座内行星及吉凶分类依据", record("not_applicable", reason="当前采用行星维姆绍塔里运，不是星座运"))
    put("分运星座八分值", record("not_applicable", reason="当前采用行星维姆绍塔里运，不是星座运"))
    put("当月行运", record("unavailable", reason="等待 JH8 提供稳定的指定月份行运输出"))

    coverage: dict[str, Any] = {}
    recipes: list[dict[str, Any]] = []
    if recipes_path:
        recipe_doc = load_json(recipes_path)
        recipes = recipe_doc.get("methods", [])
        if not isinstance(recipes, list) or any(not isinstance(item, dict) for item in recipes):
            raise AdapterError("方法配方的 methods 必须是对象数组")
        methods_by_id = {item.get("method"): item for item in recipes if isinstance(item.get("method"), str)}
        if method_id and method_id not in methods_by_id:
            raise AdapterError(f"找不到方法配方：{method_id}")
        for method in recipes:
            keys = method.get("required_facts", []) + method.get("conditional_facts", [])
            statuses = {key: _fact_entry(facts, key)["status"] for key in keys}
            gate = build_method_gate(
                method,
                facts,
                methods_by_id,
                target_house=target_house,
            )
            coverage[method["method"]] = {
                "statuses": statuses,
                "automatic_fact_binding_complete": all(status in {"available", "not_applicable"} for status in statuses.values()),
                "gate": gate,
            }

    hard_missing = sorted(key for key, item in facts.items() if item["status"] not in RESOLVED_FACT_STATUSES)
    selected_gate = coverage.get(method_id, {}).get("gate") if method_id else None
    base_stop_reasons = []
    if not recipes_path:
        base_stop_reasons.append("没有加载方法配方，只允许检查事实，不允许生成判断请求")
    if not method_id:
        base_stop_reasons.append("没有选择具体方法，只允许检查事实，不允许生成判断请求")
    if selected_gate and not selected_gate["allowed"]:
        base_stop_reasons.append("所选方法的必查事实或执行授权未全部通过")
    judgment_allowed = bool(selected_gate and selected_gate["allowed"])
    stop_output = None if judgment_allowed else build_stop_output(facts, selected_gate, base_stop_reasons)
    judgment_request = build_judgment_request(method_id, facts, selected_gate)
    return {
        "schema_version": "jh8-navigation-facts/v2",
        "source": {
            "chart_dir": str(chart_dir.resolve()),
            "full_package": str(source["full_path"].resolve()),
            "light_package": str(source["light_path"].resolve()),
            "detail_package": str(source["detail_path"].resolve()),
            "closure_report": str(source["closure_path"].resolve()),
            "light_package_status": "PASS",
            "closure_status": source["closure"].get("overall"),
            "closure_missing_fields": source["closure"].get("missing_fields", []),
            "closure_partial_fields": source["closure"].get("partial_fields", []),
        },
        "as_of": as_of.isoformat(),
        "target_house": target_house,
        "output_mode": "judgment_gate" if method_id else "inspection",
        "facts": facts if not method_id else None,
        "method_coverage": coverage,
        "hard_missing_facts": hard_missing,
        "selected_method": method_id,
        "selected_method_gate": selected_gate,
        "judgment_allowed": judgment_allowed,
        "judgment_request": judgment_request,
        "stop_output": stop_output,
        "stop_reasons": (stop_output or {}).get("why_stopped", []),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chart_dir", type=Path)
    parser.add_argument("--target-house", type=int, required=True)
    parser.add_argument("--as-of", type=date.fromisoformat, required=True)
    parser.add_argument("--recipes", type=Path)
    parser.add_argument("--method", dest="method_id", help="只为这个方法生成判断闸门结果")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = adapt(args.chart_dir, args.target_house, args.as_of, args.recipes, args.method_id)
    except AdapterError as exc:
        print(json.dumps({"passed": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
