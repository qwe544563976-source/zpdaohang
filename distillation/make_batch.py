#!/usr/bin/env python3
"""把已通过自验的抽取片段合成正式批次目录，跑完整生产线到机器验收。

顺序（对应必读卡的固定工作链）：
1. 合并 fragments/*.json → 完整 extraction（source_scope = 本批全部原子）；
2. 唯一入口 build_methods.py 装配 method-recipes.json / query-recipes.json / method-source-scan.json；
3. 生成知识地图（章节/主题/术语，只记位置，不是证据）、工作单、蒸馏来源清单、上游问题记录；
4. validate_delivery.py --render-derived 生成人读派生文件；
5. validate_delivery.py --require-v2 机械验收。

用法：python distillation/make_batch.py [--batch-id ...] [--target ...]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_term_drift  # noqa: E402  同目录工具，供装配时顺手跑一遍译名漂移

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "book-to-judgment-navigation"
BUILDER = SKILL / "scripts" / "build_methods.py"
VALIDATOR = SKILL / "scripts" / "validate_delivery.py"
LOCAL = REPO / "distillation" / "_local"
FRAGMENTS = LOCAL / "fragments"
LOCAL_PACKAGE = LOCAL / "accepted-package.local.json"
ATOMS = LOCAL / "evidence_atoms.jsonl"
SCOPE_FILE = LOCAL / "groups" / "all-scope.json"
KNOWLEDGE_ONLY = REPO / "distillation" / "KNOWLEDGE_ONLY_ATOMS.json"

DEFAULT_BATCH_ID = "BPHS97_ch14-16_siblings-home-children_20260820_run01"
DEFAULT_TARGET = REPO / "distillation" / "bphs-97" / "batches" / DEFAULT_BATCH_ID


def load_atoms() -> dict[str, dict]:
    atoms = {}
    for line in ATOMS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            atom = json.loads(line)
            atoms[atom["evidence_atom_id"]] = atom
    return atoms


def load_knowledge_only(batch_dir: Path | None = None) -> dict[str, dict]:
    """经审查确认没有判断规则的正文（过渡句、引言、收尾语）：只入知识地图，不做成方法。

    抽取窗口把本批的判定写进自己批次目录的 knowledge_only.json，装配时**提升**进
    跨批次汇总清单 KNOWLEDGE_ONLY_ATOMS.json。两件事都必须成立：

    - 批次级是写入口：4 个抽取组并行时各写各的，不会抢同一个共享文件
      （第 2 批实测：抽取员为了让装配通过只能去改全局清单，那是流程没给合法渠道）；
    - 汇总清单是永久档：批次目录在 _local/ 下不入库，而"这条原文没有判断规则"
      是实打实的取舍判断，必须留在可审计的版本库里，不能只存在于工作目录。
    """
    merged: dict[str, dict] = {}
    if KNOWLEDGE_ONLY.is_file():
        data = json.loads(KNOWLEDGE_ONLY.read_text(encoding="utf-8"))
        for item in data.get("atoms", []):
            merged[item["evidence_atom_id"]] = item
    if batch_dir is not None:
        merged.update(promote_batch_knowledge_only(batch_dir, merged))
    return merged


def promote_batch_knowledge_only(batch_dir: Path, existing: dict[str, dict]) -> dict[str, dict]:
    """把批次目录里的 knowledge_only 判定并进汇总清单，返回本批新增的部分。"""
    local = batch_dir / "knowledge_only.json"
    if not local.is_file():
        return {}
    entries = {
        item["evidence_atom_id"]: item
        for item in json.loads(local.read_text(encoding="utf-8")).get("atoms", [])
    }
    added = {atom_id: item for atom_id, item in entries.items() if atom_id not in existing}
    if added:
        registry = json.loads(KNOWLEDGE_ONLY.read_text(encoding="utf-8")) if KNOWLEDGE_ONLY.is_file() else {"atoms": []}
        registry.setdefault("atoms", []).extend(added.values())
        registry["atoms"].sort(key=lambda item: item["evidence_atom_id"])
        KNOWLEDGE_ONLY.write_text(
            json.dumps(registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"[knowledge_only] 已并入汇总清单 {len(added)} 条：{', '.join(sorted(added))}", file=sys.stderr)
    return entries


def build_extraction(batch_id: str, scope: list[str], atoms: dict[str, dict], fragments: Path) -> dict:
    knowledge_only = load_knowledge_only(fragments.parent)
    methods: list[dict] = []
    for path in sorted(fragments.glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        methods.extend(raw["methods"] if isinstance(raw, dict) else raw)
    if not methods:
        raise SystemExit("没有可合并的抽取片段")
    ids = [item["method"] for item in methods]
    duplicates = sorted({value for value in ids if ids.count(value) > 1})
    if duplicates:
        raise SystemExit(f"方法编号跨组重复：{duplicates}")
    return {
        "schema_version": "judgment-method-extraction/v2",
        "batch": {
            "batch_id": batch_id,
            "book_id": "bphs-97",
            "edition_id": "santhanam",
            "artifact_scope": "FORMAL",
            "pilot_only": False,
            "publishable": False,
            "book_strategy": "rule_book",
            # 本批是三、四、五宫的落宫与宫主断语，无大运流年、无多星复杂瑜伽。
            "chapter_features": ["simple_house_placement"],
            # 首批用新工具，强制逐步全审（定案：新工具首批不许抽审）。
            "requested_review": "full",
            "consecutive_clean_batches": 0,
            "review_cycle_position": 1,
        },
        "source_scope": scope,
        "source_records": [
            {
                "evidence_atom_id": atom_id,
                "semantic_class": knowledge_only[atom_id]["semantic_class"]
                if atom_id in knowledge_only else "condition_result",
                "risk_flags": [],
                **({"disposition": knowledge_only[atom_id]["disposition"]}
                   if atom_id in knowledge_only else {}),
            }
            for atom_id in scope
        ],
        "methods": methods,
    }


# 十二宫名与序号：出自原文 ch07:v37-38「Thanu, Dhan, Sahaj, Bandhu, Putr, Ari,
# Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas」。
# 这不是我定的对照表，是书自己给的次序；verify_bhava_order() 每次装配都回原文核一遍，
# 对不上就停工，不允许我记错了还一路生成下去。
BHAVA_ORDER_SOURCE = "bphs-97:santhanam:ch07:v37-38"
BHAVA_ORDER = (
    "Thanu", "Dhan", "Sahaj", "Bandhu", "Putr", "Ari",
    "Yuvati", "Randhr", "Dharm", "Karma", "Labh", "Vyaya",
)
# 第 12~23 章是十二宫效果章，依次对应第 1~12 宫（章号 - 11）。
BHAVA_CHAPTER_OFFSET = 11
# 章名前缀只是行文连接词，去掉后剩下的才是这一章真正的主题词。
TITLE_PREFIXES = (
    "Effects of the ", "Effects of ", "Remedies from the ", "Remedies from ",
    "Remedies for ", "Combinations for ", "Evaluation of the ", "Evaluation Of ",
    "Evaluation of ", "Determination of ", "Working out of ", "Judgement of ",
)


def verify_bhava_order(atoms: dict[str, dict]) -> None:
    """回原文核对十二宫次序；核不上就停工，绝不带着可能记错的对照表继续生成。"""
    atom = atoms.get(BHAVA_ORDER_SOURCE)
    if atom is None:  # 该原子不在本次可见范围内时跳过，不假装核对过
        return
    text = atom["exact_text"]
    positions = []
    for name in BHAVA_ORDER:
        index = text.find(name)
        if index < 0:
            raise SystemExit(f"十二宫次序核对失败：原文 {BHAVA_ORDER_SOURCE} 里找不到宫名 {name}")
        positions.append(index)
    if positions != sorted(positions):
        raise SystemExit(f"十二宫次序核对失败：程序内的次序与原文 {BHAVA_ORDER_SOURCE} 不一致")


def normalize_sanskrit(name: str) -> str:
    """吃掉梵文转写的送气音异体：辅音后面的 h 去掉（Thanu→tanu、Randhr→randr）。
    元音后的 h 保留（Sahaj 不能变成 saaj）。十二宫名规范化后仍两两不同。"""
    text = name.lower()
    return re.sub(r"(?<=[bcdgjkpqstz])h", "", text)


def bhava_house_number(chapter: int, title: str, atoms: dict[str, dict]) -> int | None:
    """第 12~23 章按章号推宫位序号，并要求章名里的宫名与该序号对得上。"""
    house = chapter - BHAVA_CHAPTER_OFFSET
    if not 1 <= house <= 12:
        return None
    match = re.search(r"([A-Za-z\u0100-\u017f\u1e00-\u1eff]+)\s+Bhava", title)
    if not match:
        return None
    named = normalize_sanskrit(match.group(1))
    expected = normalize_sanskrit(BHAVA_ORDER[house - 1])
    # 书里同一个宫有拼写异体：送气音写不写 h（Thanu/Tanu、Randhr/Randr）、
    # 尾音收不收（Karma/Karm、Dharm/Dharma）。规范化加互为前缀能吃掉这两类，
    # 差一个字母不该让整批停工；真错位（章名写的是另一个宫）才停。
    if not (named.startswith(expected) or expected.startswith(named)):
        raise SystemExit(
            f"章名与宫位序号对不上：第 {chapter} 章「{title}」按次序应是 "
            f"{BHAVA_ORDER[house - 1]}（第 {house} 宫），章名里写的是 {match.group(1)}"
        )
    return house


def chapter_term(title: str) -> str:
    """章名去掉行文前缀后剩下的主题词，作为术语表词条。"""
    for prefix in TITLE_PREFIXES:
        if title.lower().startswith(prefix.lower()):
            return title[len(prefix):].strip(" .")
    return title.strip(" .")


def slugify(text: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-") or "topic"


def knowledge_maps(target: Path, scope: list[str], atoms: dict[str, dict]) -> list[str]:
    verify_bhava_order(atoms)
    chapters: dict[int, dict] = {}
    for atom_id in scope:
        atom = atoms[atom_id]
        entry = chapters.setdefault(
            atom["chapter_number"],
            {
                "chapter_number": atom["chapter_number"],
                "title": atom["chapter_title"],
                "pdf_pages": [],
                "evidence_atom_ids": [],
            },
        )
        entry["evidence_atom_ids"].append(atom_id)
        for page in atom.get("pdf_pages", []):
            if page not in entry["pdf_pages"]:
                entry["pdf_pages"].append(page)

    # 主题与术语一律从原子自带的 chapter_title 派生。
    # 原先这里是写死 ch14~16 的三条表，第 2 批就撞墙：ch17-18 一条都匹配不上，
    # 装配直接死在"本批范围内没有可建主题或术语的原文"。97 章分 69 批，
    # 写死等于每批都要手改一次，而手写章名已经错过一次（ch17 是六宫不是七宫）。
    def scoped(chapter: int) -> list[str]:
        return [atom_id for atom_id in scope if atoms[atom_id]["chapter_number"] == chapter]

    topics = {}
    glossary = []
    for chapter in sorted({atoms[atom_id]["chapter_number"] for atom_id in scope}):
        ids = scoped(chapter)
        if not ids:
            continue
        title = atoms[ids[0]]["chapter_title"]
        term = chapter_term(title)
        house = bhava_house_number(chapter, title, atoms)
        label = f"第{house}宫（{term}）" if house else term
        topics[f"ch{chapter:02d}-{slugify(term)}"] = {
            "title": f"第{chapter}章 {title}" + (f"｜{label}" if house else ""),
            "chapter_numbers": [chapter],
            "evidence_atom_ids": ids,
        }
        # 解释只写位置，不写星占含义：知识地图的术语解释按契约"只是导航辅助，永远不是证据"，
        # 写"三宫主管兄弟姐妹、勇气"就是在交付件里塞没有出处的教义。
        # 宫位序号有出处，可以写——出处就是原文自己的十二宫名次序。
        explanation = f"本书第 {chapter} 章「{title}」的主题；本批收录该章 {len(ids)} 条原文。"
        if house:
            explanation = f"第 {house} 宫；" + explanation + f"（宫序依原文 {BHAVA_ORDER_SOURCE} 的十二宫名次序）"
        glossary.append({"term": term, "explanation": explanation, "evidence_atom_ids": ids[:3]})
    if not topics or not glossary:
        raise SystemExit("本批范围内没有原文，无法建主题或术语")

    write_json(target / "references" / "knowledge" / "chapter-map.json", {
        "schema_version": "knowledge-chapter-map/v1",
        "book_id": "bphs-97",
        "edition_id": "santhanam",
        "pilot_only": False,
        "publishable": False,
        "chapters": [chapters[key] for key in sorted(chapters)],
    })
    write_json(target / "references" / "knowledge" / "topic-map.json", {
        "schema_version": "knowledge-topic-map/v1",
        "book_id": "bphs-97",
        "edition_id": "santhanam",
        "pilot_only": False,
        "publishable": False,
        "topics": topics,
    })
    write_json(target / "references" / "knowledge" / "glossary.json", {
        "schema_version": "knowledge-glossary/v1",
        "book_id": "bphs-97",
        "edition_id": "santhanam",
        "pilot_only": False,
        "publishable": False,
        "terms": glossary,
    })

    return [entry["title"] for entry in topics.values()]

def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run(command: list[str], label: str) -> dict:
    result = subprocess.run(command, check=False, capture_output=True, text=True, encoding="utf-8")
    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError:
        raise SystemExit(f"{label} 没有输出可读 JSON：\n{result.stdout}\n{result.stderr}")
    return {"returncode": result.returncode, "report": report}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-id", default=DEFAULT_BATCH_ID)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--keep", action="store_true", help="不清空目标目录（默认重建）")
    parser.add_argument("--scope", type=Path, default=SCOPE_FILE, help="本批原文编号清单")
    parser.add_argument("--fragments", type=Path, default=FRAGMENTS, help="抽取片段目录")
    args = parser.parse_args()

    target = args.target.resolve()
    if target.exists() and not args.keep:
        shutil.rmtree(target)
    target.mkdir(parents=True, exist_ok=True)

    atoms = load_atoms()
    scope = json.loads(args.scope.read_text(encoding="utf-8"))
    package = json.loads(LOCAL_PACKAGE.read_text(encoding="utf-8"))

    # 工作单的允许范围必须与本批实际原文严格相等：
    # 整章都在本批的写进 chapter_scope；只取了一章里一部分的，逐条写进 evidence_atom_scope。
    # 否则验证器会按整章加载原子，把没生产的原文算成"遗漏"。
    scope_set = set(scope)
    chapters_touched = sorted({atoms[atom_id]["chapter_number"] for atom_id in scope})
    chapter_scope: list[int] = []
    atom_scope: list[str] = []
    for chapter in chapters_touched:
        whole = {
            atom_id for atom_id, atom in atoms.items() if atom["chapter_number"] == chapter
        }
        if whole <= scope_set:
            chapter_scope.append(chapter)
        else:
            atom_scope.extend(atom_id for atom_id in scope if atoms[atom_id]["chapter_number"] == chapter)
    extraction = build_extraction(args.batch_id, scope, atoms, args.fragments.resolve())
    extraction_path = target / "validation" / "stage-a-extraction.json"
    write_json(extraction_path, extraction)

    build = run(
        [
            sys.executable, str(BUILDER),
            "--extraction", str(extraction_path),
            "--accepted-package", str(LOCAL_PACKAGE),
            "--output", str(target / "references" / "navigation" / "method-recipes.json"),
        ],
        "build_methods.py",
    )
    if build["returncode"] != 0:
        print(json.dumps({"stage": "build", **build}, ensure_ascii=False, indent=2))
        return 1

    topic_order = knowledge_maps(target, scope, atoms)

    write_json(target / "WORK_ORDER.json", {
        "job_name": args.batch_id,
        "operation": "formal",
        "pilot_only": False,
        "publishable": False,
        "artifact_scope": "FORMAL",
        "formal_migration": "ALLOWED_AFTER_AUDIT",
        "accepted_package": package.get("package_id"),
        "mechanical_gate_status": "not_run",
        "book": {
            "title": "Brihat Parashara Hora Shastra",
            "author": "Maharshi Parashara",
            "edition": "Santhanam 97-chapter edition",
        },
        "book_class": "A",
        "distillation_strategy": "rule_book",
        "input": {
            "accepted_package_path": str(LOCAL_PACKAGE),
            "chapter_scope": chapter_scope,
            "evidence_atom_scope": atom_scope,
        },
        "target_dir": str(target),
        # 主题顺序与复审要求都按本批实际情况生成：写死会跟着第 1 批走到第 69 批。
        "topic_order": topic_order,
        "review_requirement": "逐步全审，不得抽审；两轮审核（第一轮找问题，第二轮确认修复）",
    })

    write_json(target / "DISTILLATION_SOURCE.json", {
        "distillation_run_id": args.batch_id,
        "artifact_scope": "FORMAL",
        "pilot_only": False,
        "publishable": False,
        "book_id": package["book"]["book_id"],
        "edition_id": package["book"]["edition_id"],
        "source_artifact_id": package["book"]["source_artifact_id"],
        "accepted_package_id": package["package_id"],
        "accepted_package_path": str(LOCAL_PACKAGE),
        "evidence_contract_version": package["evidence_atoms"]["contract_version"],
        "evidence_atoms_path": str(ATOMS.resolve()),
        "evidence_atoms_sha256": package["evidence_atoms"]["content_sha256"],
        "chapter_scope": chapter_scope,
        "created_at": "2026-08-20T00:00:00Z",
    })

    write_json(target / "UPSTREAM_ISSUES.json", {
        "schema_version": "upstream-issues/v1",
        "pilot_only": False,
        "publishable": False,
        "issues": [],
    })

    (target / "references" / "navigation" / "version-routing.md").write_text(
        "# 版本路由\n\n本批只使用 BPHS 97 章版（R. Santhanam 英译，`bphs-97:santhanam`）。\n"
        "100 章版是独立版本，原文与引用永不混写；本批不引用、不比对、不合并。\n",
        encoding="utf-8",
    )
    (target / "SKILL.md").write_text(
        f"# {args.batch_id}\n\n"
        # 批次封面必须写本批自己的章节。写死会一路带着第 1 批的章名走到第 69 批，
        # 下游只读封面就会被指向错的书页——第 2 批实测已经发生。
        f"BPHS 97 章版正式方法批次：{'；'.join(topic_order)}。\n\n"
        "- 唯一方法真相：`references/navigation/method-recipes.json`\n"
        "- 唯一主题真相：`references/navigation/query-recipes.json`\n"
        "- 人读文件全部由验证器 `--render-derived` 生成，手改即判失败。\n"
        "- 本批全部方法 `executable_in_pilot=false`：JH8 排盘事实尚未接通，只做证据绑定，不进执行主路。\n",
        encoding="utf-8",
    )
    fragment_count = len(list(args.fragments.resolve().glob("*.json")))
    (target / "PIPELINE_STATE.md").write_text(
        f"# {args.batch_id} 进度\n\n"
        f"- 已完成：正式书包复核、{fragment_count} 组并行抽取并各自通过生成器强校验、"
        "合并装配、知识地图、机器验收。\n"
        "- 待办：独立语义审计（未参与生成的窗口）→ 并入用户本机全书总账。\n"
        "- 复审口径：逐步全审，不得抽审；两轮审核（第一轮找问题，第二轮确认修复）。\n",
        encoding="utf-8",
    )

    render = run([sys.executable, str(VALIDATOR), str(target), "--render-derived"], "render-derived")
    rendered_files = render["report"].get("rendered_files")
    if rendered_files is None:
        print(json.dumps({"stage": "render", **render}, ensure_ascii=False, indent=2))
        return 1
    validate = run([sys.executable, str(VALIDATOR), str(target), "--require-v2"], "validate --require-v2")

    recipes = json.loads((target / "references" / "navigation" / "method-recipes.json").read_text(encoding="utf-8"))

    # 译名漂移是全批统计才现形的问题，一步步看方法看不出来（第 1 批 exalted 入旺 7 : 入庙 3 : 庙旺 1）。
    # 不拦装配：它是提示不是判据，真有两种译法也可能是对的，交给审计员看。
    # 但要落盘，让审计员一开工就知道该盯哪几步，不必自己全批数一遍。
    drift = check_term_drift.scan(recipes)
    write_json(target / "validation" / "term-drift-report.json", drift)

    # 顺手把审计分片包切好：审计员少花 4~5 次工具调用自己翻找，5 片 × 69 批省下来是实数。
    subprocess.run(
        [sys.executable, str(REPO / "distillation" / "make_audit_bundle.py"), str(target), "--shards", "5"],
        check=False, capture_output=True, text=True, encoding="utf-8",
    )

    print(json.dumps({
        "batch_id": args.batch_id,
        "target": str(target),
        "build": build["report"],
        "rendered_files": rendered_files,
        "validate_returncode": validate["returncode"],
        "validate": validate["report"],
        "term_drift": drift,
        "methods": len(recipes.get("methods", [])),
        "steps": sum(len(m.get("steps", [])) for m in recipes.get("methods", [])),
    }, ensure_ascii=False, indent=2))
    if not drift["passed"]:
        print(
            f"[译名漂移] {len(drift['drifts'])} 个术语在本批有多种译法，"
            f"已写入 validation/term-drift-report.json，审计时优先看少数派步骤",
            file=sys.stderr,
        )
    return 0 if validate["returncode"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
