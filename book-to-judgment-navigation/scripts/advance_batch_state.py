#!/usr/bin/env python3
"""Advance a v2 batch from machine testing to independent audit."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


VALIDATOR = Path(__file__).with_name("validate_delivery.py")
GATE_REPORT_VALIDATOR_RELATIVE = Path("tools/anti-false-green/assertions/validate-gate-report.js")


class StateError(ValueError):
    pass


class BatchRejected(StateError):
    pass


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise StateError(f"无法读取 JSON：{path}：{exc}") from exc
    if not isinstance(value, dict):
        raise StateError(f"JSON 顶层必须是对象：{path}")
    return value


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_write(path: Path, value: dict) -> None:
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


def find_gate_report_validator(target: Path) -> Path:
    for parent in (target, *target.parents):
        candidate = parent / GATE_REPORT_VALIDATOR_RELATIVE
        if candidate.is_file():
            return candidate
    raise StateError(
        "找不到项目的反假绿报告检查器："
        f"{GATE_REPORT_VALIDATOR_RELATIVE}"
    )


def run_gate_report_validator(target: Path, gate_path: Path) -> dict:
    validator = find_gate_report_validator(target)
    result = subprocess.run(
        ["node", str(validator), str(gate_path)],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    try:
        output = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise StateError(
            "反假绿报告检查器没有输出可读 JSON，批次状态保持不变"
        ) from exc
    if (
        result.returncode != 0
        or not isinstance(output, dict)
        or output.get("passed") is not True
    ):
        errors = output.get("errors") if isinstance(output, dict) else None
        if not isinstance(errors, list) or any(not isinstance(error, str) for error in errors):
            errors = [result.stderr.strip() or "反假绿报告检查器未通过"]
        raise StateError("反假绿报告检查器未通过：" + "；".join(errors))
    return output


def reject_state(
    state_path: Path,
    state: dict,
    reason: str,
    details: list[str],
    evidence: Path | None = None,
) -> None:
    entry = {
        "state": "rejected",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "recorded_by": "book-to-judgment-navigation/scripts/advance_batch_state.py",
        "reason": reason,
        "details": details,
    }
    if evidence is not None:
        entry["evidence"] = str(evidence)
    state["current_state"] = "rejected"
    state.setdefault("history", []).append(entry)
    atomic_write(state_path, state)


def validate_controls(target: Path, report: dict, recipe_path: Path, gate_path: Path) -> None:
    bindings = report.get("artifact_bindings")
    bindings = bindings if isinstance(bindings, list) else []
    current_hash = sha256(recipe_path)
    if not any(
        isinstance(item, dict)
        and Path(str(item.get("path", ""))).resolve() == recipe_path.resolve()
        and item.get("sha256") == current_hash
        for item in bindings
    ):
        raise StateError("三类检查没有绑定当前 method-recipes.json")
    run_gate_report_validator(target, gate_path)
    if report.get("controls") != {"positive": "pass", "negative": "fail", "baseline": "fail"}:
        raise BatchRejected("正确／错误／空白三类检查结果不符合 0／非0／非0")
    if report.get("status") != "machine_check_pass" or report.get("unresolved_blockers") != []:
        raise BatchRejected("三类检查没有通过或仍有阻塞")


def main() -> int:
    parser = argparse.ArgumentParser(description="把通过机器检查的 v2 批次送入独立审计")
    parser.add_argument("target", type=Path)
    parser.add_argument("--gate-report", type=Path)
    args = parser.parse_args()
    target = args.target.resolve()
    state_path = target / "validation" / "batch-state.json"
    recipe_path = target / "references" / "navigation" / "method-recipes.json"
    gate_path = (args.gate_report or target / "validation" / "交付三类检查" / "gate-report.json").resolve()
    try:
        state = load_json(state_path)
        if state.get("schema_version") != "judgment-batch-state/v2":
            raise StateError("批次状态文件不是 v2")
        if state.get("current_state") != "mechanical_testing":
            raise StateError(f"只能从机检仿真进入审计中，当前状态是：{state.get('current_state')}")
        if state.get("method_recipes_sha256") != sha256(recipe_path):
            raise StateError("批次状态没有绑定当前 method-recipes.json")
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), str(target), "--require-v2"],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        if not result.stdout.strip():
            raise StateError("v2 交付验证没有输出可读报告，批次状态保持不变")
        try:
            report = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise StateError(f"v2 交付验证输出不是可读 JSON，批次状态保持不变：{exc}") from exc
        if not isinstance(report, dict):
            raise StateError("v2 交付验证报告不是对象，批次状态保持不变")
        if result.returncode != 0:
            details = report.get("errors")
            if (
                report.get("passed") is not False
                or not isinstance(details, list)
                or not details
                or any(not isinstance(error, str) for error in details)
            ):
                raise StateError("v2 交付验证失败但报告不完整，批次状态保持不变")
            reject_state(state_path, state, "机器交付检查失败", details)
            print(
                json.dumps(
                    {"passed": False, "current_state": "rejected", "errors": details},
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 1
        if report.get("passed") is not True or report.get("errors") != []:
            raise StateError("v2 交付验证返回码为 0 但报告没有确认通过，批次状态保持不变")
        gate_report = load_json(gate_path)
        try:
            validate_controls(target, gate_report, recipe_path, gate_path)
        except BatchRejected as exc:
            reject_state(state_path, state, "正常／错误／空白三类检查失败", [str(exc)], gate_path)
            print(
                json.dumps(
                    {"passed": False, "current_state": "rejected", "errors": [str(exc)]},
                    ensure_ascii=False,
                    indent=2,
                )
            )
            return 1
        state["current_state"] = "audit_in_progress"
        state["history"].append(
            {
                "state": "audit_in_progress",
                "recorded_at": datetime.now(timezone.utc).isoformat(),
                "recorded_by": "book-to-judgment-navigation/scripts/advance_batch_state.py",
                "gate_report": str(gate_path),
            }
        )
        atomic_write(state_path, state)
        print(json.dumps({"passed": True, "current_state": "audit_in_progress", "errors": []}, ensure_ascii=False, indent=2))
        return 0
    except (StateError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"passed": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
