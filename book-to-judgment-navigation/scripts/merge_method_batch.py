#!/usr/bin/env python3
"""Merge one independently audited v2 batch into the full-book candidate ledger."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


VALIDATOR = Path(__file__).with_name("validate_delivery.py")
MACHINE_PATHS = (
    Path("references/navigation/method-recipes.json"),
    Path("references/navigation/query-recipes.json"),
    Path("validation/method-source-scan.json"),
)
PIPELINE_STATE_NAME = "PIPELINE_STATE.md"
PROJECT_STATUS_NAME = "JUDGMENT_PIPELINE_STATUS.json"
PIPELINE_STATE_START = "<!-- merge-method-batch:begin -->"
PIPELINE_STATE_END = "<!-- merge-method-batch:end -->"
DERIVED_FIXED_PATHS = (
    Path("UPSTREAM_ISSUES.md"),
    Path("references/navigation/required-checks.json"),
    Path("references/navigation/method-map.md"),
    Path("methods/verified.md"),
)


class MergeError(ValueError):
    pass


class AuditRejected(MergeError):
    def __init__(self, report: dict, rejected_step_ids: list[str]) -> None:
        self.report = report
        self.rejected_step_ids = rejected_step_ids
        super().__init__(f"独立检查发现 {len(rejected_step_ids)} 个步骤有问题")


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise MergeError(f"无法读取 JSON：{path}：{exc}") from exc
    if not isinstance(value, dict):
        raise MergeError(f"JSON 顶层必须是对象：{path}")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def atomic_write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(value)
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def reject_state(state_path: Path, state: dict, reason: str, evidence: Path) -> None:
    state["current_state"] = "rejected"
    state.setdefault("history", []).append(
        {
            "state": "rejected",
            "recorded_at": datetime.now(timezone.utc).isoformat(),
            "recorded_by": "book-to-judgment-navigation/scripts/merge_method_batch.py",
            "reason": reason,
            "evidence": str(evidence),
        }
    )
    atomic_write(state_path, state)


def pipeline_state_with_merge_counts(
    current_text: str, counts: dict, merged_at: str
) -> str:
    block = "\n".join(
        [
            PIPELINE_STATE_START,
            f"- 最近一次成功合并：{merged_at}",
            f"- 本批新增方法数：{counts['added_methods']}",
            f"- 本批消化原文数：{counts['consumed_sources']}",
            f"- 合并后剩余候选数：{counts['remaining_candidates_after']}",
            PIPELINE_STATE_END,
        ]
    )
    pattern = re.compile(
        rf"\n?{re.escape(PIPELINE_STATE_START)}.*?{re.escape(PIPELINE_STATE_END)}\n?",
        flags=re.DOTALL,
    )
    if pattern.search(current_text):
        return pattern.sub("\n" + block + "\n", current_text, count=1)
    return current_text.rstrip("\n") + "\n\n" + block + "\n"


def update_pipeline_state(path: Path, counts: dict, merged_at: str) -> None:
    try:
        current = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise MergeError(f"无法读取整书状态文件：{path}：{exc}") from exc
    atomic_write_text(path, pipeline_state_with_merge_counts(current, counts, merged_at))


def update_project_status(path: Path, counts: dict, merged_at: str, evidence: Path) -> None:
    status = load_json(path)
    remaining = counts["remaining_candidates_after"]
    status["updated_on"] = merged_at[:10]
    current_phase = status.get("current_phase_cn")
    if isinstance(current_phase, str):
        status["current_phase_cn"] = re.sub(r"剩余候选 \d+ 条", f"剩余候选 {remaining} 条", current_phase)
    next_action = status.get("only_next_action")
    if isinstance(next_action, str):
        status["only_next_action"] = re.sub(r"当前剩余候选 \d+ 条", f"当前剩余候选 {remaining} 条", next_action)
    verified = status.get("verified_currently")
    if isinstance(verified, dict):
        verified["full_book_source_manifest"] = f"2024 条唯一原文；{remaining} 条待生产候选；遗漏 0；重复 0"
    evidence_list = status.get("evidence")
    if isinstance(evidence_list, list) and str(evidence) not in evidence_list:
        evidence_list.append(str(evidence))
    atomic_write(path, status)


def collect_derived_files(root: Path) -> set[Path]:
    files = {relative for relative in DERIVED_FIXED_PATHS if (root / relative).is_file()}
    files.update(path.relative_to(root) for path in (root / "methods" / "families").glob("*.md"))
    files.update(path.relative_to(root) for path in (root / "references" / "navigation" / "topics").glob("*.md"))
    return files


def recipe_step_index(recipe_path: Path) -> tuple[dict[str, str], dict[str, list[dict]]]:
    """从当前配方取 {step_id: step_hash} 与 {step_id: 高风险词差异表行}。"""
    recipes = load_json(recipe_path)
    hashes: dict[str, str] = {}
    for method in recipes.get("methods", []):
        if not isinstance(method, dict):
            continue
        for step in method.get("steps", []):
            if not isinstance(step, dict):
                continue
            step_id = step.get("step_id")
            step_hash = step.get("step_hash")
            if isinstance(step_id, str) and isinstance(step_hash, str):
                hashes[step_id] = step_hash
    generation = recipes.get("generation")
    table = generation.get("high_risk_terms") if isinstance(generation, dict) else {}
    table = table if isinstance(table, dict) else {}
    return hashes, table


def verify_audit(batch: Path, state: dict, recipe_path: Path) -> dict:
    report = load_json(batch / "validation" / "independent-semantic-audit.json")
    if report.get("schema_version") != "independent-semantic-audit/v3":
        raise MergeError("独立审计报告不是 v3（v2 整包绑定格式已退役，凭证必须逐步骤绑 step_hash）")
    if report.get("batch_id") != state.get("batch_id"):
        raise MergeError("独立审计报告与批次编号不一致")
    identity = report.get("identity")
    if not isinstance(identity, dict) or identity.get("participated_in_production") is not False:
        raise MergeError("独立审计者身份没有证明未参与本批生产")
    if report.get("review_mode") != state.get("review_mode"):
        raise MergeError("独立审计报告使用了错误的全审／抽审模式")
    expected = state.get("audit_step_ids")
    reviewed = report.get("reviewed_step_ids")
    if reviewed != expected:
        raise MergeError("独立审计没有覆盖机器指定的全部应审步骤")
    entries = report.get("entries")
    if not isinstance(entries, list):
        raise MergeError("独立审计报告缺少 entries")
    step_hashes, high_risk_table = recipe_step_index(recipe_path)
    entry_map = {
        item.get("step_id"): item
        for item in entries
        if isinstance(item, dict) and isinstance(item.get("step_id"), str)
    }
    if len(entry_map) != len(entries) or set(entry_map) != set(expected or []):
        raise MergeError("独立审计 entries 与机器指定步骤不一一对应")
    verdicts = {step_id: item.get("verdict") for step_id, item in entry_map.items()}
    invalid = sorted(step_id for step_id, verdict in verdicts.items() if verdict not in {"PASS", "REJECT"})
    if invalid:
        raise MergeError(f"独立审计使用了非法判定：{invalid}")
    # Q1：凭证逐步骤绑定。entry 绑错或绑旧 step_hash 即无效；
    # 未被改动的步骤在重产批次里指纹不变，其 PASS 凭证保持有效。
    mismatched = sorted(
        step_id
        for step_id, item in entry_map.items()
        if item.get("step_hash") != step_hashes.get(step_id)
    )
    if mismatched:
        raise MergeError(f"独立审计凭证没有逐步骤绑定当前步骤内容指纹：{mismatched}")
    # Q21：高风险词差异表逐词单选确认，只准确认机器清单上的词。
    for step_id, item in entry_map.items():
        listed_terms = {
            row.get("term")
            for row in high_risk_table.get(step_id, [])
            if isinstance(row, dict) and isinstance(row.get("term"), str)
        }
        confirmations = item.get("high_risk_confirmations")
        confirmations = confirmations if isinstance(confirmations, dict) else {}
        if set(confirmations) != listed_terms:
            raise MergeError(f"独立审计的高风险词确认与机器差异表清单不一致：{step_id}")
        illegal = sorted(term for term, choice in confirmations.items() if choice not in {"accept", "reject"})
        if illegal:
            raise MergeError(f"高风险词确认只允许单选 accept/reject：{step_id}：{illegal}")
        if any(choice == "reject" for choice in confirmations.values()) and verdicts[step_id] != "REJECT":
            raise MergeError(f"高风险词被 reject 的步骤必须判 REJECT：{step_id}")
    rejected = sorted(step_id for step_id, verdict in verdicts.items() if verdict != "PASS")
    if rejected:
        if report.get("finding_status") != "本轮找到问题":
            raise MergeError("独立审计有 REJECT，但没有写‘本轮找到问题’")
        raise AuditRejected(report, rejected)
    if report.get("finding_status") != "本轮未找到问题":
        raise MergeError("独立审计结论必须使用‘本轮未找到问题’，不能写成已证明正确")
    return report


def validate_full_book_result(
    report: dict, exit_code: int, remaining_candidate_ids: set[str]
) -> dict:
    errors = report.get("errors")
    if not isinstance(errors, list) or any(not isinstance(error, str) for error in errors):
        raise MergeError("全书验证报告的 errors 不是字符串数组")
    expected_errors = sorted(
        f"方法候选尚未完成方法生产，不能通过：{atom_id}"
        for atom_id in remaining_candidate_ids
    )
    actual_errors = sorted(errors)
    if expected_errors:
        if exit_code == 0 or report.get("passed") is not False:
            raise MergeError("中间批次的全书验证结果没有按剩余候选返回失败")
        if actual_errors != expected_errors:
            raise MergeError("全书验证包含剩余候选错误之外的错误，禁止继续合并")
        return report
    if exit_code != 0 or report.get("passed") is not True or actual_errors:
        raise MergeError("候选已清零但全书验证仍失败")
    return report


def run_validator(
    target: Path,
    require_v2: bool,
    render: bool = False,
    remaining_candidate_ids: set[str] | None = None,
) -> dict:
    command = [sys.executable, str(VALIDATOR), str(target)]
    if render:
        command.append("--render-derived")
    if require_v2:
        command.append("--require-v2")
    result = subprocess.run(command, check=False, capture_output=True, text=True, encoding="utf-8")
    report = json.loads(result.stdout) if result.stdout else {"passed": False, "errors": [result.stderr]}
    if remaining_candidate_ids is not None:
        return validate_full_book_result(report, result.returncode, remaining_candidate_ids)
    if result.returncode != 0 or report.get("passed") is not True:
        raise MergeError("交付验证失败：" + "；".join(report.get("errors", [])))
    return report


def merge_data(batch: Path, target: Path) -> tuple[dict[Path, dict], dict]:
    batch_methods = load_json(batch / MACHINE_PATHS[0])
    batch_queries = load_json(batch / MACHINE_PATHS[1])
    batch_scan = load_json(batch / MACHINE_PATHS[2])
    target_methods = load_json(target / MACHINE_PATHS[0])
    target_queries = load_json(target / MACHINE_PATHS[1])
    target_scan = load_json(target / MACHINE_PATHS[2])

    new_methods = batch_methods.get("methods")
    new_methods = new_methods if isinstance(new_methods, list) else []
    if not new_methods:
        raise MergeError("批次没有方法")
    if any(
        method.get("publishable") is not False or method.get("executable_in_pilot") is not False
        for method in new_methods if isinstance(method, dict)
    ):
        raise MergeError("批次仍有发布或执行许可")
    existing_ids = {item.get("method") for item in target_methods.get("methods", []) if isinstance(item, dict)}
    new_ids = [item.get("method") for item in new_methods if isinstance(item, dict)]
    if len(set(new_ids)) != len(new_ids) or existing_ids & set(new_ids):
        raise MergeError("批次方法编号为空、重复或与全书重复")

    batch_topics = batch_queries.get("topics")
    batch_topics = batch_topics if isinstance(batch_topics, dict) else {}
    target_topics = target_queries.get("topics")
    target_topics = target_topics if isinstance(target_topics, dict) else {}
    if set(batch_topics) & set(target_topics):
        raise MergeError("批次查询主题与全书重复")

    batch_rows = batch_scan.get("atom_dispositions")
    batch_rows = batch_rows if isinstance(batch_rows, list) else []
    if not batch_rows or any(row.get("disposition") != "method_step" for row in batch_rows if isinstance(row, dict)):
        raise MergeError("批次原文去向没有全部变成 method_step")
    batch_row_map = {row.get("evidence_atom_id"): row for row in batch_rows if isinstance(row, dict)}
    if len(batch_row_map) != len(batch_rows):
        raise MergeError("批次原文去向存在空编号或重复编号")
    target_rows = target_scan.get("atom_dispositions")
    target_rows = target_rows if isinstance(target_rows, list) else []
    target_row_map = {row.get("evidence_atom_id"): row for row in target_rows if isinstance(row, dict)}
    if len(target_row_map) != len(target_rows):
        raise MergeError("全书总账存在空编号或重复编号")
    for atom_id in batch_row_map:
        target_row = target_row_map.get(atom_id)
        if target_row is None or target_row.get("disposition") != "method_candidate":
            raise MergeError(f"全书原文不是等待消化的方法候选：{atom_id}")

    merged_methods = copy.deepcopy(target_methods)
    merged_methods.setdefault("methods", []).extend(copy.deepcopy(new_methods))
    merged_queries = copy.deepcopy(target_queries)
    merged_queries.setdefault("topics", {}).update(copy.deepcopy(batch_topics))

    remaining_before = sum(row.get("disposition") == "method_candidate" for row in target_rows)
    merged_scan = copy.deepcopy(target_scan)
    for row in merged_scan["atom_dispositions"]:
        atom_id = row.get("evidence_atom_id")
        if atom_id in batch_row_map:
            row.update(copy.deepcopy(batch_row_map[atom_id]))
    consumed = len(batch_row_map)
    remaining_after = sum(
        row.get("disposition") == "method_candidate"
        for row in merged_scan["atom_dispositions"]
    )
    if remaining_before - consumed != remaining_after:
        raise MergeError("新增方法、消化原文和剩余候选三个数字没有对齐")

    return {
        MACHINE_PATHS[0]: merged_methods,
        MACHINE_PATHS[1]: merged_queries,
        MACHINE_PATHS[2]: merged_scan,
    }, {
        "added_methods": len(new_methods),
        "consumed_sources": consumed,
        "remaining_candidates_before": remaining_before,
        "remaining_candidates_after": remaining_after,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="把一个已完成独立审计的 v2 批次并入全书候选总账")
    parser.add_argument("--batch", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    args = parser.parse_args()
    batch = args.batch.resolve()
    target = args.target.resolve()
    try:
        state_path = batch / "validation" / "batch-state.json"
        state = load_json(state_path)
        original_state = copy.deepcopy(state)
        if state.get("current_state") != "audit_in_progress":
            raise MergeError("批次没有按顺序进入审计中，禁止并入")
        recipe_path = batch / MACHINE_PATHS[0]
        if state.get("method_recipes_sha256") != sha256(recipe_path):
            raise MergeError("批次状态没有绑定当前方法配方")
        audit_path = batch / "validation" / "independent-semantic-audit.json"
        safe_batch = re.sub(r"[^A-Za-z0-9._-]+", "_", str(state["batch_id"]))
        batch_receipt = batch / "validation" / "merge-receipt.json"
        target_receipt = target / "validation" / f"merge-{safe_batch}.json"
        receipt_snapshots: dict[Path, str] = {}
        for receipt_path in (batch_receipt, target_receipt):
            if receipt_path.exists():
                if not receipt_path.is_file():
                    raise MergeError(f"合入凭证路径不是文件：{receipt_path}")
                receipt_snapshots[receipt_path] = receipt_path.read_text(encoding="utf-8")
        try:
            audit = verify_audit(batch, state, recipe_path)
        except AuditRejected as exc:
            reject_state(state_path, state, str(exc), audit_path)
            print(
                json.dumps(
                    {
                        "passed": False,
                        "current_state": "rejected",
                        "errors": [str(exc)],
                        "rejected_step_ids": exc.rejected_step_ids,
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 1
        run_validator(batch, require_v2=True)
        merged, counts = merge_data(batch, target)

        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = target / "backups" / f"{timestamp}-before-{safe_batch}"
        if backup.exists():
            raise MergeError(f"备份目录已经存在：{backup}")
        pipeline_state_path = target / PIPELINE_STATE_NAME
        if not pipeline_state_path.is_file():
            raise MergeError(f"整书状态文件不存在，拒绝合并：{pipeline_state_path}")
        project_status_path = target.parent / PROJECT_STATUS_NAME
        if not project_status_path.is_file():
            raise MergeError(f"项目总状态文件不存在，拒绝合并：{project_status_path}")
        derived_files_before = collect_derived_files(target)
        files_to_backup = set(MACHINE_PATHS) | derived_files_before
        for relative in sorted(files_to_backup, key=str):
            source = target / relative
            destination = backup / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        shutil.copy2(pipeline_state_path, backup / PIPELINE_STATE_NAME)
        shutil.copy2(project_status_path, backup / PROJECT_STATUS_NAME)

        try:
            for relative, value in merged.items():
                atomic_write(target / relative, value)
            merged_scan = merged[MACHINE_PATHS[2]]
            remaining_candidate_ids = {
                row["evidence_atom_id"]
                for row in merged_scan.get("atom_dispositions", [])
                if row.get("disposition") == "method_candidate"
            }
            full_report = run_validator(
                target,
                require_v2=False,
                render=True,
                remaining_candidate_ids=remaining_candidate_ids,
            )
            merged_at = datetime.now(timezone.utc).isoformat()
            update_pipeline_state(pipeline_state_path, counts, merged_at)
            update_project_status(
                project_status_path,
                counts,
                merged_at,
                batch / "validation" / "merge-receipt.json",
            )
            receipt = {
                "schema_version": "formal-method-batch-merge/v2",
                "batch_id": state["batch_id"],
                "merged_at": merged_at,
                "backup_dir": str(backup),
                "independent_audit": str(batch / "validation" / "independent-semantic-audit.json"),
                "audit_finding_status": audit["finding_status"],
                **counts,
                "full_delivery_validation": full_report,
                "all_permissions_false": True,
            }
            atomic_write(batch_receipt, receipt)
            atomic_write(target_receipt, receipt)
            state["current_state"] = "merged"
            state["history"].append(
                {
                    "state": "merged",
                    "recorded_at": datetime.now(timezone.utc).isoformat(),
                    "recorded_by": "book-to-judgment-navigation/scripts/merge_method_batch.py",
                    "merge_receipt": str(batch_receipt),
                }
            )
            atomic_write(state_path, state)
        except BaseException:
            current_derived_files = collect_derived_files(target)
            for relative in sorted(current_derived_files - derived_files_before, key=str):
                (target / relative).unlink()
            for relative in sorted(files_to_backup, key=str):
                shutil.copy2(backup / relative, target / relative)
            shutil.copy2(backup / PIPELINE_STATE_NAME, pipeline_state_path)
            shutil.copy2(backup / PROJECT_STATUS_NAME, project_status_path)
            atomic_write(state_path, original_state)
            for receipt_path in (batch_receipt, target_receipt):
                original_text = receipt_snapshots.get(receipt_path)
                if original_text is None:
                    try:
                        receipt_path.unlink()
                    except FileNotFoundError:
                        pass
                else:
                    atomic_write_text(receipt_path, original_text)
            restored_scan = load_json(target / MACHINE_PATHS[2])
            restored_candidate_ids = {
                row["evidence_atom_id"]
                for row in restored_scan.get("atom_dispositions", [])
                if row.get("disposition") == "method_candidate"
            }
            run_validator(
                target,
                require_v2=False,
                render=True,
                remaining_candidate_ids=restored_candidate_ids,
            )
            raise
        print(json.dumps({"passed": True, **receipt}, ensure_ascii=False, indent=2))
        return 0
    except (MergeError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"passed": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
