#!/usr/bin/env python3
"""Prepare the locked source packet consumed by Stage A AI extraction."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


BUILD_SCRIPT = Path(__file__).with_name("build_methods.py")
BUILD_SPEC = importlib.util.spec_from_file_location("cangjie_build_methods", BUILD_SCRIPT)
if BUILD_SPEC is None or BUILD_SPEC.loader is None:
    raise RuntimeError(f"无法加载正式生成器：{BUILD_SCRIPT}")
BUILD = importlib.util.module_from_spec(BUILD_SPEC)
BUILD_SPEC.loader.exec_module(BUILD)


def main() -> int:
    parser = argparse.ArgumentParser(description="从正式书包和全书分类总账准备 Stage A 只读原文输入")
    parser.add_argument("--work-order", required=True, type=Path)
    parser.add_argument("--full-scan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        work = BUILD.load_json(args.work_order.resolve())
        input_data = work.get("input") if isinstance(work.get("input"), dict) else {}
        accepted = input_data.get("accepted_package_path")
        scope = input_data.get("evidence_atom_scope")
        if not isinstance(accepted, str) or not accepted:
            raise BUILD.BuildError("工作单缺少 input.accepted_package_path")
        if not isinstance(scope, list) or not scope or any(not isinstance(item, str) for item in scope):
            raise BUILD.BuildError("工作单缺少非空 evidence_atom_scope")
        package = BUILD.load_json(Path(accepted))
        book = package.get("book") or {}
        batch = {
            "artifact_scope": work.get("artifact_scope"),
            "book_id": book.get("book_id"),
            "edition_id": book.get("edition_id"),
        }
        atoms, _package = BUILD.resolve_atoms(Path(accepted), batch)
        scan = BUILD.load_json(args.full_scan.resolve())
        rows = scan.get("atom_dispositions")
        rows = rows if isinstance(rows, list) else []
        row_map = {
            item.get("evidence_atom_id"): item
            for item in rows
            if isinstance(item, dict) and isinstance(item.get("evidence_atom_id"), str)
        }
        records = []
        source_atoms = []
        for atom_id in scope:
            atom = atoms.get(atom_id)
            row = row_map.get(atom_id)
            if atom is None:
                raise BUILD.BuildError(f"工作单原文编号不在正式书包：{atom_id}")
            if row is None or row.get("disposition") != "method_candidate":
                raise BUILD.BuildError(f"全书总账中的原文不是待生产方法候选：{atom_id}")
            records.append(
                {
                    "evidence_atom_id": atom_id,
                    "semantic_class": row.get("semantic_class"),
                    "risk_flags": row.get("risk_flags", []),
                }
            )
            source_atoms.append(
                {
                    key: atom.get(key)
                    for key in (
                        "evidence_atom_id",
                        "chapter_number",
                        "chapter_title",
                        "heading_path",
                        "content_role",
                        "exact_text",
                        "pdf_pages",
                        "citation",
                    )
                }
            )
        output = args.output.resolve()
        if output.exists():
            raise BUILD.BuildError(f"拒绝覆盖已有 Stage A 输入：{output}")
        BUILD.atomic_write_json(
            output,
            {
                "schema_version": "judgment-method-stage-a-source/v2",
                "accepted_package_path": str(Path(accepted).resolve()),
                "book": book,
                "source_scope": scope,
                "source_records": records,
                "atoms": source_atoms,
            },
        )
        print(json.dumps({"passed": True, "atoms": len(source_atoms), "output": str(output), "errors": []}, ensure_ascii=False, indent=2))
        return 0
    except (BUILD.BuildError, OSError) as exc:
        print(json.dumps({"passed": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
