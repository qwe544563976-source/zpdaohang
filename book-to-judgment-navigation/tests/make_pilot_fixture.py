#!/usr/bin/env python3
"""自举生成验证器回归测试用的试点夹具（v1 老格式交付目录）。

历史上 64 项验证器回归测试依赖用户本机的
`C:/Users/aa/Documents/ChatGPT/洗书/_judgment_distillation_pilot_bphs97_ch11_20260814`
第 11 章试点夹具。本脚本在任何机器上现场构建一个结构等价的最小夹具，
让测试套件可以脱离那台机器运行；不迁移、不冒充历史 v7 内容。

用法：python tests/make_pilot_fixture.py <输出父目录>
生成：<父目录>/_judgment_distillation_pilot_fixture/   （交付目录，测试的 FIXTURE 根）
      <父目录>/_chunk_bphs97_stage3_v7_20260814/evidence_atoms.jsonl
生成末尾自动运行 validate_delivery.py，非 0 即失败。
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
VALIDATOR = SCRIPTS / "validate_delivery.py"

ATOMS = [
    {
        "evidence_atom_id": "bphs-97:santhanam:ch11:v1",
        "chapter_number": 11,
        "chapter_title": "Judgement of Bhavas",
        "heading_path": ["Ch. 11 Judgement of Bhavas"],
        "content_role": "verse",
        "exact_text": "Please tell me, what is to be deduced from each Bhava.",
        "pdf_pages": [131],
        "citation": "BPHS (Santhanam), Ch. 11, v. 1",
    },
    {
        "evidence_atom_id": "bphs-97:santhanam:ch11:v2",
        "chapter_number": 11,
        "chapter_title": "Judgement of Bhavas",
        "heading_path": ["Ch. 11 Judgement of Bhavas"],
        "content_role": "verse",
        "exact_text": "The Bhava, whose lord is strong, will prosper.",
        "pdf_pages": [132],
        "citation": "BPHS (Santhanam), Ch. 11, v. 2",
    },
    {
        "evidence_atom_id": "bphs-97:santhanam:ch11:v3",
        "chapter_number": 11,
        "chapter_title": "Judgement of Bhavas",
        "heading_path": ["Ch. 11 Judgement of Bhavas"],
        "content_role": "verse",
        "exact_text": "A Bhava receiving a benefic drishti gains strength.",
        "pdf_pages": [132],
        "citation": "BPHS (Santhanam), Ch. 11, v. 3",
    },
    {
        "evidence_atom_id": "bphs-97:santhanam:ch11:v14-16",
        "chapter_number": 11,
        "chapter_title": "Judgement of Bhavas",
        "heading_path": ["Ch. 11 Judgement of Bhavas"],
        "content_role": "verse",
        "exact_text": "The Bhava occupied by its own lord will flourish.",
        "pdf_pages": [133],
        "citation": "BPHS (Santhanam), Ch. 11, v. 14-16",
    },
]

RUN_ID = "bphs97-ch11-pilot-20260814"


def step(method_id: str, fact: str, claim: str, refs: list[dict], source_status: str) -> dict:
    return {
        "step_id": f"{method_id}.step-01",
        "action": f"按原文核对 {fact}。",
        "applicability_scope": "仅限本试点夹具的回归测试。",
        "minimum_supported_claim": claim,
        "produced_fact_keys": [],
        "required_fact_keys": [fact],
        "condition_logic": {"fact_key": fact},
        "conditional_fact_requirements": [],
        "source_status": source_status,
        "evidence_refs": refs,
        "stop_condition": f"缺少{fact}时停止。",
        "stop_fact_keys": [fact],
        "exception_relations": [],
        "forbidden_extensions": ["不得扩大为终身吉凶结论。"],
    }


def method(
    method_id: str,
    title: str,
    fact: str,
    claim: str,
    refs: list[dict],
    source_status: str,
    upstream_issue_ids: list[str] | None = None,
) -> dict:
    return {
        "method": method_id,
        "title": title,
        "pilot_only": True,
        "publishable": False,
        "workflow_status": "pilot_candidate",
        "workflow_history": ["pilot_candidate"],
        "source_status": source_status,
        "fact_binding_status": "unmapped",
        "upstream_issue_ids": upstream_issue_ids or [],
        "user_intents": [f"核对{title}"],
        "required_facts": [fact],
        "conditional_facts": [],
        "dependencies": [],
        "steps": [step(method_id, fact, claim, refs, source_status)],
        "retrieval_plan": {
            "support_queries": [f"{title}支持"],
            "counter_queries": [f"{title}反例"],
            "boundary_queries": [f"{title}边界"],
            "method_queries": [f"{title}方法"],
        },
        "stop_conditions": [f"缺少{fact}时停止。"],
        "executable_in_pilot": False,
    }


def ref(atom_index: int, quote: str | None = None) -> dict:
    atom = ATOMS[atom_index]
    return {
        "evidence_atom_id": atom["evidence_atom_id"],
        "quote": quote or atom["exact_text"],
        "pdf_pages": atom["pdf_pages"],
    }


def topic(title: str, candidates: list[str], facts: list[str]) -> dict:
    return {
        "title": title,
        "user_intents": [f"{title}怎么看"],
        "method_ids": [],
        "candidate_method_ids": candidates,
        "execution_allowed": False,
        "required_facts": facts,
        "conditional_facts": [],
        "fact_binding_status": "unmapped",
        "support_queries": [f"{title}支持"],
        "counter_queries": [f"{title}反例"],
        "boundary_queries": [f"{title}边界"],
        "method_queries": [f"{title}方法"],
        "stop_conditions": ["缺少必查事实时停止。"],
    }


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build(parent: Path) -> Path:
    atoms_dir = parent / "_chunk_bphs97_stage3_v7_20260814"
    atoms_dir.mkdir(parents=True, exist_ok=True)
    atoms_path = atoms_dir / "evidence_atoms.jsonl"
    atoms_path.write_text(
        "\n".join(json.dumps(atom, ensure_ascii=False) for atom in ATOMS) + "\n",
        encoding="utf-8",
    )
    sha = hashlib.sha256(atoms_path.read_bytes()).hexdigest()
    stat = atoms_path.stat()

    root = parent / "_judgment_distillation_pilot_fixture"
    root.mkdir(parents=True, exist_ok=True)

    write_json(
        root / "WORK_ORDER.json",
        {
            "job_name": "bphs97-ch11-judgment-pilot",
            "operation": "pilot",
            "pilot_only": True,
            "publishable": False,
            "artifact_scope": "PILOT_TEMP",
            "formal_migration": "FORBIDDEN",
            "accepted_package": None,
            "mechanical_gate_status": "not_run",
            "allowed_use": "validator_regression_fixture_only",
            "book": {"title": "Brihat Parashara Hora Shastra", "author": "Parashara", "edition": "Santhanam 97"},
            "input": {
                "evidence_atoms_path": str(atoms_path),
                "chapter_scope": [11],
                "evidence_atom_scope": [],
                "source_snapshot": {
                    "size_bytes": stat.st_size,
                    "mtime_ns": stat.st_mtime_ns,
                    "content_sha256": sha,
                },
            },
            "target_dir": str(root),
        },
    )
    write_json(
        root / "PILOT_STATUS.json",
        {
            "artifact_scope": "PILOT_TEMP",
            "pilot_only": True,
            "publishable": False,
            "formal_migration": "FORBIDDEN",
            "superseded_on_formal_atoms": True,
            "formal_dependency": "accepted-package.json",
            "formal_dependency_status": "missing",
            "independent_verification_allowed": True,
            "shadow_allowed": True,
            "allowed_uses": ["validator_regression_tests"],
            "forbidden_uses": [
                "formal_navigation",
                "temporary_id_migration",
                "production_agent_execution",
            ],
            "mechanical_gate_status": "not_run",
        },
    )
    write_json(
        root / "DISTILLATION_SOURCE.json",
        {
            "distillation_run_id": RUN_ID,
            "artifact_scope": "PILOT_TEMP",
            "pilot_only": True,
            "publishable": False,
            "book_id": "bphs-97",
            "edition_id": "santhanam",
            "source_artifact_id": "bphs97-santhanam-v7-pdf",
            "accepted_package_id": None,
            "accepted_package_path": None,
            "evidence_contract_version": "evidence-atoms-v7",
            "evidence_atoms_path": str(atoms_path),
            "evidence_atoms_sha256": sha,
            "chapter_scope": [11],
            "created_at": "2026-08-14T00:00:00Z",
        },
    )
    (root / "SKILL.md").write_text(
        "# 试点夹具\n\n本目录是验证器回归测试专用夹具，禁止发布、迁移或生产执行。\n",
        encoding="utf-8",
    )
    (root / "PIPELINE_STATE.md").write_text(
        "# 试点夹具状态\n\n- 仅供验证器回归测试。\n",
        encoding="utf-8",
    )

    methods = [
        method(
            "question-to-bhava-routing",
            "问题到宫位路由",
            "用户真正要问的生活主题",
            "每个宫位有其应判断的主题，宫主有力则该宫兴旺。",
            [ref(1), ref(2)],
            "repeated_support",
        ),
        method(
            "bhava-assessment",
            "宫位评估",
            "宫位编号",
            "宫主落在本宫时该宫兴旺。",
            [ref(3)],
            "single_explicit_source",
            upstream_issue_ids=["fixture-upstream-issue-1"],
        ),
        method(
            "bhava-lord-strength",
            "宫主星力量",
            "宫主星力量",
            "宫位得到吉星相位时力量增强。",
            [ref(2)],
            "single_explicit_source",
        ),
        method(
            "bhava-verdict",
            "宫位结论",
            "宫位综合状态",
            "宫主有力时该宫兴旺可期。",
            [ref(0)],
            "single_explicit_source",
        ),
    ]
    write_json(
        root / "references" / "navigation" / "method-recipes.json",
        {
            "schema_version": "judgment-method-recipes/v1",
            "pilot_only": True,
            "publishable": False,
            "methods": methods,
        },
    )
    write_json(
        root / "references" / "navigation" / "query-recipes.json",
        {
            "schema_version": "judgment-query-recipes/v1",
            "pilot_only": True,
            "publishable": False,
            "topics": {
                "bhava-assessment": topic(
                    "宫位评估", ["bhava-assessment", "bhava-lord-strength"], ["宫位编号", "宫主星力量"]
                ),
                "question-routing": topic(
                    "问题路由",
                    ["question-to-bhava-routing", "bhava-verdict"],
                    ["用户真正要问的生活主题", "宫位综合状态"],
                ),
            },
        },
    )
    write_json(
        root / "validation" / "method-source-scan.json",
        {
            "schema_version": "method-source-scan/v1",
            "pilot_only": True,
            "publishable": False,
            "review_status": "complete",
            "atom_dispositions": [
                {
                    "evidence_atom_id": "bphs-97:santhanam:ch11:v2",
                    "semantic_class": "condition_result",
                    "risk_flags": [],
                    "disposition": "method_step",
                    "method_ids": ["question-to-bhava-routing"],
                },
                {
                    "evidence_atom_id": "bphs-97:santhanam:ch11:v3",
                    "semantic_class": "condition_result",
                    "risk_flags": [],
                    "disposition": "method_step",
                    "method_ids": ["bhava-lord-strength", "question-to-bhava-routing"],
                },
                {
                    "evidence_atom_id": "bphs-97:santhanam:ch11:v14-16",
                    "semantic_class": "condition_result",
                    "risk_flags": [],
                    "disposition": "method_step",
                    "method_ids": ["bhava-assessment"],
                },
                {
                    "evidence_atom_id": "bphs-97:santhanam:ch11:v1",
                    "semantic_class": "foundational_knowledge",
                    "risk_flags": [],
                    "disposition": "method_step",
                    "method_ids": ["bhava-verdict"],
                },
            ],
        },
    )
    atom_ids = [atom["evidence_atom_id"] for atom in ATOMS]
    write_json(
        root / "references" / "knowledge" / "chapter-map.json",
        {
            "schema_version": "knowledge-chapter-map/v1",
            "pilot_only": True,
            "publishable": False,
            "chapters": [
                {
                    "chapter_number": 11,
                    "title": "Judgement of Bhavas",
                    "evidence_atom_ids": atom_ids,
                }
            ],
        },
    )
    write_json(
        root / "references" / "knowledge" / "topic-map.json",
        {
            "schema_version": "knowledge-topic-map/v1",
            "pilot_only": True,
            "publishable": False,
            "topics": {
                "bhava-judgement": {
                    "title": "宫位判断",
                    "evidence_atom_ids": atom_ids[1:],
                }
            },
        },
    )
    write_json(
        root / "references" / "knowledge" / "glossary.json",
        {
            "schema_version": "knowledge-glossary/v1",
            "pilot_only": True,
            "publishable": False,
            "terms": [
                {
                    "term": "Bhava",
                    "explanation": "宫位；本命盘十二个生活领域之一。",
                    "evidence_atom_ids": [atom_ids[0]],
                }
            ],
        },
    )
    (root / "references" / "navigation").mkdir(parents=True, exist_ok=True)
    (root / "references" / "navigation" / "version-routing.md").write_text(
        "# 版本路由\n\n本夹具只含 BPHS 97 章版（Santhanam 译本）单一版本，无版本分流。\n",
        encoding="utf-8",
    )
    write_json(
        root / "UPSTREAM_ISSUES.json",
        {
            "schema_version": "upstream-issues/v1",
            "pilot_only": True,
            "publishable": False,
            "issues": [
                {
                    "issue_id": "fixture-upstream-issue-1",
                    "evidence_atom_id": "bphs-97:santhanam:ch11:v14-16",
                    "issue_type": "mixed_primary_and_note_text",
                    "impact": "该偈颂的正文与译注身份需要上游复核。",
                    "blocking": True,
                    "blocking_stage": "method_distillation",
                    "status": "open",
                    "affected_method_ids": ["bhava-assessment"],
                }
            ],
        },
    )

    render = subprocess.run(
        [sys.executable, str(VALIDATOR), str(root), "--render-derived"],
        check=False, capture_output=True, text=True, encoding="utf-8",
    )
    report = json.loads(render.stdout) if render.stdout else {}
    if render.returncode != 0 or not report.get("passed"):
        raise SystemExit(
            "夹具自举后没有通过交付验证：\n" + json.dumps(report, ensure_ascii=False, indent=2)
        )
    return root


def main() -> int:
    parent = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    root = build(parent)
    print(json.dumps({"passed": True, "fixture": str(root)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
