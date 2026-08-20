#!/usr/bin/env python3
"""生成器与验证器共享的常量和纯函数（唯一真相，两边只准 import，不准复制）。

第一部分：从 build_methods.py 与 validate_delivery.py 原样搬入的两组黑名单，
搬家前已实测两份逐字一致，只搬不改（拆网定案·四·1）。
第二部分：v2 升级新增的共享逻辑——步骤级哈希（Q1）与四类高风险词检测（Q15）。
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from typing import Any

# ---------------------------------------------------------------------------
# 第一部分：原样搬入，只搬不改
# ---------------------------------------------------------------------------

EMPTY_CLAIM_FRAGMENTS = (
    "按原文判断",
    "根据原文判断",
    "按引文核对后引用引文结果",
    "按引文核对后引用原文结果",
    "as stated in the quote",
    "judge according to the source",
)
PLACEHOLDER_FACT_PATTERNS = (
    (re.compile(r"^source_[A-Za-z0-9][A-Za-z0-9_.:-]*$"), "source_*"),
    (re.compile(r"^choice_[A-Za-z0-9][A-Za-z0-9_.:-]*$"), "choice_*"),
    (re.compile(r"原文事实已取得"), "原文事实已取得"),
    (re.compile(r"或者\s*分支\s*[A-Za-z](?:\s*/\s*[A-Za-z])?"), "或者分支 A/B"),
    (re.compile(r"条件已成立"), "条件已成立"),
)

# ---------------------------------------------------------------------------
# 第二部分：v2 新增共享逻辑
# ---------------------------------------------------------------------------

# 唯一正式生成器身份。Q19 把生成器搬入本技能后，身份随文件地址一起更新；
# 已并入总账的旧记录由 backfill_step_hash.py 一次性改写为新身份。
GENERATOR_ID = "book-to-judgment-navigation/scripts/build_methods.py"


def compute_step_hash(step: dict[str, Any]) -> str:
    """步骤内容指纹（Q1）。

    对步骤除 step_hash 外的全部字段做键排序紧凑 JSON，再取 sha256。
    改第 7 步只改变第 7 步的指纹；其余步骤的审计凭证保持有效。
    纯计算，不读不写任何经文内容。
    """
    content = {key: value for key, value in step.items() if key != "step_hash"}
    canonical = json.dumps(content, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# 四类高风险词（Q15 方案 C）：专有名词（行星／宫位／星座名）、数值、单位、时间词。
# 只强制映射这四类；一步通常只命中 2～5 个词。词表按已登记错误家族流程扩充，
# 不做全量词映射表。检测在去音符、不分大小写的规范化文本上按词边界进行。
HIGH_RISK_PROPER_NOUNS = (
    # 行星（含常见梵文名与 Santhanam 译本的短形式）
    "sun", "moon", "mars", "mercury", "jupiter", "venus", "saturn", "rahu", "ketu",
    "surya", "chandra", "mangal", "kuja", "budh", "budha", "guru", "brihaspati",
    "shukra", "shukr", "sukra", "shani", "sani", "mandi", "gulika",
    # 宫位梵文名（Santhanam 译本正文多用无尾音短形式：Putr、Lagn、Randhr…）
    "lagna", "lagn", "tanu", "dhan", "dhana", "sahaj", "sahaja", "bandhu",
    "putr", "putra", "ari", "yuvati", "randhr", "randhra", "dharm", "dharma",
    "karm", "karma", "labh", "labha", "vyaya",
    # 分盘名（写错分盘＝换一张盘，属最高风险）
    "navamsa", "navans", "dwadasamsa", "drekkana", "decanate",
    # 星座
    "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio",
    "sagittarius", "capricorn", "aquarius", "pisces",
    "mesha", "vrishabha", "mithuna", "karka", "simha", "kanya", "tula",
    "vrischika", "dhanu", "makara", "kumbha", "meena",
)
HIGH_RISK_UNIT_WORDS = ("degree", "degrees", "ghati", "ghatis", "ghatika", "amsa", "amsha")
HIGH_RISK_TIME_WORDS = (
    "dasha", "dasa", "antardasha", "bhukti", "pratyantar",
    "year", "years", "month", "months", "day", "days", "age",
)
HIGH_RISK_ORDINAL_WORDS = (
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
    "eighth", "ninth", "tenth", "eleventh", "twelfth",
)
# 基数词也是数值：BPHS 的子女、兄弟数量断语几乎全用基数词
# （"There will be 10 sons" 与 "Nine will be the number of sons" 同章并存）。
# 真实证据：ch14 v7-11、ch16 v10/v11/v17/v24-32。
# 故意不含 "one"：Santhanam 译本里 one 绝大多数是代词（"one will beget a child"），
# 强制映射它只会产生无信息噪音；真正的 "one child only"（ch16 v5、v6）其结果词
# 本来就必须进 results 映射。若将来出现 one 被写错的真实批次证据，再按错误家族纪律加入。
HIGH_RISK_CARDINAL_WORDS = (
    "two", "three", "four", "five", "six", "seven",
    "eight", "nine", "ten", "eleven", "twelve",
)
HIGH_RISK_NUMBER_PATTERN = re.compile(r"\b\d+(?:st|nd|rd|th)?\b")

_HIGH_RISK_WORD_CLASSES = (
    ("proper_noun", HIGH_RISK_PROPER_NOUNS),
    ("unit", HIGH_RISK_UNIT_WORDS),
    ("time", HIGH_RISK_TIME_WORDS),
    ("number", HIGH_RISK_ORDINAL_WORDS),
    ("number", HIGH_RISK_CARDINAL_WORDS),
)


def normalize_for_term_match(text: str) -> str:
    """去掉音符（Sūrya→surya）、统一小写，用于高风险词匹配。"""
    decomposed = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    return stripped.casefold()


def detect_high_risk_terms(text: str) -> list[dict[str, str]]:
    """在一段逐字短引里检出四类高风险词。

    返回 [{"term": 命中词, "term_class": 类别}]，按出现顺序去重。
    """
    normalized = normalize_for_term_match(text)
    found: list[dict[str, str]] = []
    seen: set[str] = set()

    def add(term: str, term_class: str) -> None:
        if term not in seen:
            seen.add(term)
            found.append({"term": term, "term_class": term_class})

    for match in HIGH_RISK_NUMBER_PATTERN.finditer(normalized):
        add(match.group(0), "number")
    for term_class, words in _HIGH_RISK_WORD_CLASSES:
        for word in words:
            if re.search(rf"\b{re.escape(word)}\b", normalized):
                add(word, term_class)
    return found


def high_risk_term_covered(term: str, quote_terms: list[str]) -> bool:
    """高风险词是否已被某个 claim_terms 映射对的引文词按整词覆盖。

    必须按词边界判断：子串判断会让 "money" 假装覆盖 "one"、"100" 假装覆盖 "10"，
    等于把写错数值的步骤放行。
    """
    pattern = re.compile(rf"\b{re.escape(normalize_for_term_match(term))}\b")
    return any(pattern.search(normalize_for_term_match(quote)) for quote in quote_terms)


def map_high_risk_terms(
    detected: list[dict[str, str]], pairs: list[tuple[str, str]]
) -> tuple[list[dict[str, str]], list[str]]:
    """把检出的高风险词逐个对上 claim_terms 映射对。

    pairs 为 (引文词, 主张词) 列表。返回（差异表行, 未映射词列表）；
    差异表行含 term、term_class、mapped_quote、mapped_claim，供独立审计
    按清单逐词单选 accept/reject（Q21），不得在清单外自行找茬。
    """
    rows: list[dict[str, str]] = []
    uncovered: list[str] = []
    for item in detected:
        match = next(
            (
                (quote, claim)
                for quote, claim in pairs
                if high_risk_term_covered(item["term"], [quote])
            ),
            None,
        )
        if match is None:
            uncovered.append(item["term"])
        else:
            rows.append(
                {
                    "term": item["term"],
                    "term_class": item["term_class"],
                    "mapped_quote": match[0],
                    "mapped_claim": match[1],
                }
            )
    return rows, uncovered
