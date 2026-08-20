#!/usr/bin/env python3
"""开工脚本：把仓库里的正式书包 zip 解成本地只读工作区，并做蒸馏窗口独立复算。

做四件事，全部只读原包、不改一个字：
1. 解包 `2024/BPHS97_2024_formal_package.zip` 到 `_local/`（不入库，zip 才是库内真相）；
2. 独立复算：evidence_atoms.jsonl 的 sha256 是否与书包凭证的 content_sha256 逐字一致、
   记录数、必备字段、编号唯一性、prev/next 链闭合、页码与引用非空；
3. 生成本地重定位副本 `accepted-package.local.json`：**只改 evidence_atoms.path**
   （原值是切卡窗口本机的 F: 盘路径，在本容器不存在），其余字段逐字复制，
   package_id、content_sha256、upstream_gates 一律不动；
4. 写 `PACKAGE_RELOCATION.json` 留痕：原路径、新路径、两边同一份内容的哈希证明。

边界：本脚本不是上游权威验包器（`validate_accepted_package.py` 属切卡窗口，不在包内）。
它做的是蒸馏窗口的独立复算；上游那份 status=pass 的验包结论由包内
`accepted-package-*-validation.json` 提供，二者一并作为开工凭证，缺一即停。

用法：python distillation/setup_workspace.py
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PACKAGE_ZIP = REPO / "2024" / "BPHS97_2024_formal_package.zip"
LOCAL = REPO / "distillation" / "_local"
ATOMS_NAME = "evidence_atoms.jsonl"
PACKAGE_NAME = "accepted-package-20260818T213650Z.json"
UPSTREAM_VALIDATION_NAME = "accepted-package-20260818T213650Z-validation.json"
REQUIRED_ATOM_FIELDS = (
    "evidence_atom_id",
    "chapter_number",
    "chapter_title",
    "heading_path",
    "content_role",
    "exact_text",
    "pdf_pages",
    "citation",
)


class SetupError(RuntimeError):
    pass


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def recompute_atoms(path: Path, expected_sha: str, expected_count: int) -> dict:
    """蒸馏窗口独立复算。发现问题只报告，绝不修原子。"""
    actual_sha = sha256_file(path)
    if actual_sha != expected_sha:
        raise SetupError(
            f"原文原子内容摘要与书包凭证不一致：凭证 {expected_sha}，实测 {actual_sha}"
        )
    atoms: dict[str, dict] = {}
    problems: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        atom = json.loads(line)
        atom_id = atom.get("evidence_atom_id")
        if not isinstance(atom_id, str) or not atom_id:
            problems.append(f"第 {line_number} 行缺 evidence_atom_id")
            continue
        if atom_id in atoms:
            problems.append(f"编号重复：{atom_id}")
            continue
        missing = [field for field in REQUIRED_ATOM_FIELDS if not atom.get(field) and atom.get(field) != 0]
        if missing:
            problems.append(f"{atom_id} 缺字段 {missing}")
        atoms[atom_id] = atom
    if len(atoms) != expected_count:
        problems.append(f"记录数不符：凭证 {expected_count}，实测 {len(atoms)}")

    broken_chain = [
        atom_id
        for atom_id, atom in atoms.items()
        for neighbour in (atom.get("previous_atom_id"), atom.get("next_atom_id"))
        if neighbour and neighbour not in atoms
    ]
    if broken_chain:
        problems.append(f"prev/next 链指向不存在的原子：{sorted(set(broken_chain))[:5]}")
    missing_flags = [atom_id for atom_id, atom in atoms.items() if atom.get("content_missing") is True]
    chapters = sorted({atom["chapter_number"] for atom in atoms.values() if isinstance(atom.get("chapter_number"), int)})
    return {
        "recomputed_sha256": actual_sha,
        "atom_count": len(atoms),
        "chapters": len(chapters),
        "chapter_min": chapters[0] if chapters else None,
        "chapter_max": chapters[-1] if chapters else None,
        "content_missing_atoms": missing_flags,
        "problems": problems,
    }


def main() -> int:
    try:
        if not PACKAGE_ZIP.is_file():
            raise SetupError(f"正式书包 zip 不存在：{PACKAGE_ZIP}")
        if LOCAL.exists():
            shutil.rmtree(LOCAL)
        LOCAL.mkdir(parents=True)
        with zipfile.ZipFile(PACKAGE_ZIP) as archive:
            archive.extractall(LOCAL)

        package_path = LOCAL / PACKAGE_NAME
        atoms_path = LOCAL / ATOMS_NAME
        for path in (package_path, atoms_path, LOCAL / UPSTREAM_VALIDATION_NAME):
            if not path.is_file():
                raise SetupError(f"书包里缺文件：{path.name}")

        package = json.loads(package_path.read_text(encoding="utf-8"))
        evidence = package.get("evidence_atoms") or {}
        original_path = evidence.get("path")
        expected_sha = evidence.get("content_sha256")
        expected_count = evidence.get("record_count")
        if not (isinstance(expected_sha, str) and isinstance(expected_count, int)):
            raise SetupError("书包凭证缺少 evidence_atoms.content_sha256 或 record_count")
        if package.get("artifact_scope") != "FORMAL" or package.get("distillation_allowed") is not True:
            raise SetupError("书包不是允许蒸馏的正式书包")
        gates = package.get("upstream_gates") or {}
        failed_gates = [key for key in ("source_text_bidirectional", "chunking_validation", "accepted") if gates.get(key) != "pass"]
        if failed_gates:
            raise SetupError(f"书包上游闸门未全部通过：{failed_gates}")

        upstream_validation = json.loads((LOCAL / UPSTREAM_VALIDATION_NAME).read_text(encoding="utf-8"))
        if upstream_validation.get("status") != "pass" or upstream_validation.get("errors"):
            raise SetupError(f"上游权威验包结论不是 pass：{upstream_validation}")

        recomputed = recompute_atoms(atoms_path, expected_sha, expected_count)
        if recomputed["problems"]:
            raise SetupError("独立复算发现问题：" + "；".join(recomputed["problems"]))

        local_package = json.loads(json.dumps(package))
        local_package["evidence_atoms"]["path"] = str(atoms_path.resolve())
        local_package_path = LOCAL / "accepted-package.local.json"
        local_package_path.write_text(
            json.dumps(local_package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

        relocation = {
            "schema_version": "package-relocation/v1",
            "reason": "切卡窗口本机的 F: 盘路径在本执行环境不存在；只重定位文件位置，不改内容",
            "package_id": package.get("package_id"),
            "original_evidence_atoms_path": original_path,
            "relocated_evidence_atoms_path": str(atoms_path.resolve()),
            "content_sha256_declared_by_package": expected_sha,
            "content_sha256_recomputed_locally": recomputed["recomputed_sha256"],
            "content_identical": True,
            "fields_changed": ["evidence_atoms.path"],
            "fields_untouched": [
                "package_id", "artifact_scope", "distillation_allowed", "book",
                "evidence_atoms.content_sha256", "evidence_atoms.contract_version",
                "evidence_atoms.record_count", "upstream_gates", "created_at_utc",
            ],
            "upstream_authoritative_validation": upstream_validation,
            "distiller_independent_recheck": recomputed,
            "not_performed": [
                "未运行上游权威验包器 validate_accepted_package.py：该脚本属切卡窗口，不在书包内",
                "未打开原始 PDF 复核逐页结构：属上游责任，蒸馏窗口只认上游凭证",
            ],
            "recorded_at": datetime.now(timezone.utc).isoformat(),
        }
        (LOCAL / "PACKAGE_RELOCATION.json").write_text(
            json.dumps(relocation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

        print(json.dumps(
            {
                "passed": True,
                "local_package": str(local_package_path),
                "evidence_atoms": str(atoms_path.resolve()),
                **{k: recomputed[k] for k in ("atom_count", "chapters", "chapter_min", "chapter_max")},
                "content_missing_atoms": len(recomputed["content_missing_atoms"]),
            },
            ensure_ascii=False, indent=2,
        ))
        return 0
    except (SetupError, OSError, json.JSONDecodeError, zipfile.BadZipFile) as exc:
        print(json.dumps({"passed": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
