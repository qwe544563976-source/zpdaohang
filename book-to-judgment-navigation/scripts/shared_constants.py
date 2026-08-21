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
    # 星座 Rāśi。它与宫 Bhava 是盘上两种不同对象，混译等于换了个查询对象。
    # 真实证据：ch21:v2 的 "in its own Rāśi" 被译成"落本宫"，
    # 而同批知识地图里"宫"对应的是 Bhava。行星主管两个星座，本星座与本宫并不等同。
    "rasi", "rashi", "rāśi", "raashi",
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


# 事实名是交给排盘系统的接口，必须是能直接取值的原子事实。
# 名字里出现析取词，说明把多个可分辨的事实压成了一个"是否"判断——
# 那正是已登记错误家族「OR 被压成 AND / 藏进单个事实」的另一种形态。
# 真实证据：ch16 v16 的「五宫主是否落二宫、五宫或九宫之一」、
# 「五宫主是否与木星同宫或被木星相照」，ch16 v24-32 的
# 「五宫有凶星或土星落木星起第5宫是否成立」。
# "及其"「与…及…」这类隐性合取同样把多个条件压进一个事实名。
# 真实证据：ch15 v10-14 的「是否有吉星与四宫（Bandhu Bhava）及其宫主发生关系」——
# 原文是四选一（落四宫／相照四宫／与四宫主同宫／相照四宫主），"及其"把它写成了
# 四宫与四宫主都要，比原文严，且四种关系合并后排盘无法直接取值。
DISJUNCTIVE_FACT_PATTERN = re.compile(r"或|之一|和/或|任一|任意一|及其")

# 术语译名红线：不比较整句主张词（同一个 yuti 出现在不同短语里，主张词本就不同），
# 只对"译错就等于换一张盘/换一种状态"的词卡死禁用译名。
# 真实证据（第一批）：exalted 被译成"入庙旺"（庙是 own sign，旺是 exaltation，
# 触发面从入旺扩大到入庙或入旺）；trine 被译成"三分宫"，而"三分盘"正是同批
# Decanate/D3 的译名，只差一字。
TERM_RENDERING_RULES = {
    "exalted": ("庙",),
    "exaltation": ("庙",),
    "debilitated": ("庙",),
    "trine": ("三分宫", "三分盘"),
    "decanate": ("十分盘", "九分盘"),
    "drekkana": ("十分盘", "九分盘"),
    "navamsa": ("三分盘", "十分盘"),
}

# 短语级红线：有些错必须连着上下文才认得出，单看一个词会大面积误伤。
# Rāśi 就是典型——中文的"宫"几乎每句都有（"四宫主""七宫主"），
# 只查"含 rasi 且含宫"，实测全书语料 34 处命中里绝大多数是正确译法。
# 真正的错法只有一种：把 own Rāśi（本星座）写成"本宫"。行星主管两个星座，
# 本星座与本宫不是同一件事；本书里"宫"对应的是 Bhava。
# 真实证据：ch21:v2「in its own Rāśi/Navāńś」→「落本宫」、
# ch23:v1-4「be in its own Rashiand/or Navāńś」→「落本宫或…」、ch18:v1、ch16:v1-3。
PHRASE_RENDERING_RULES = (
    (
        re.compile(r"\bown\s+ra[sz]h?i", re.I),
        ("本宫",),
        "own Rāśi 是本星座（行星自己主管的星座），不是本宫；本书里宫对应 Bhava",
    ),
)


def term_rendering_violations(pairs_by_step: dict) -> list[dict]:
    """找出把关键术语译成禁用词的映射对。

    pairs_by_step: {步骤编号: [(引文词, 主张词), ...]}
    """
    found: list[dict] = []
    for step_id, pairs in pairs_by_step.items():
        for quote, claim in pairs:
            normalized = normalize_for_term_match(quote)
            # 短语级红线：原书排印会丢空格（Rashiand／Rashialong），故不加右词边界。
            for pattern, forbidden_words, reason in PHRASE_RENDERING_RULES:
                if not pattern.search(normalized):
                    continue
                for word in forbidden_words:
                    if word in claim:
                        found.append({
                            "step_id": step_id, "term": pattern.pattern,
                            "forbidden_rendering": word, "claim": claim, "reason": reason,
                        })
            for term, forbidden in TERM_RENDERING_RULES.items():
                if not re.search(rf"\b{re.escape(term)}\b", normalized):
                    continue
                for word in forbidden:
                    if word in claim:
                        found.append({
                            "step_id": step_id, "term": term,
                            "forbidden_rendering": word, "claim": claim,
                        })
    return found


# 结果动词的中文加码：原文只说"去世/失去"，中文写成"夭亡/夭折"就凭空补上了年龄限定。
# 四类高风险词只覆盖专名／数值／单位／时间，覆盖不到结果动词。
# 真实证据：ch16 v24-32 的 `3 will pass away` → "3 个会夭亡"；ch14 v7-11 的
# `the third brother will die` → "第三个弟弟会夭折"。
RESULT_VERB_INFLATION = (
    ("夭亡", "pass away / die 未给年龄，「夭」专指未成年而死"),
    ("夭折", "pass away / die 未给年龄，「夭」专指未成年而死"),
    ("早夭", "原文未给年龄"),
    ("暴毙", "原文未给死因或急缓"),
    ("绝嗣", "原文若只说 no children，不含绝嗣的宗族含义"),
)


def result_verb_inflation_reason(text: object) -> str | None:
    """最小意思里有没有把结果动词写得比原文重。"""
    if not isinstance(text, str):
        return None
    for word, reason in RESULT_VERB_INFLATION:
        if word in text:
            return f"{word}（{reason}）"
    return None


def term_translation_conflicts(pairs_by_step: dict) -> list[dict]:
    """跨方法找同一英文词的中文译名冲突。

    pairs_by_step: {步骤编号: [(引文词, 主张词), ...]}
    返回 [{"term", "renderings": {中文: [步骤…]}}]，只报真出现分歧的词。
    """
    seen: dict[str, dict[str, list[str]]] = {}
    for step_id, pairs in pairs_by_step.items():
        for quote, claim in pairs:
            normalized = normalize_for_term_match(quote)
            for term in TERM_CONSISTENCY_WATCHLIST:
                if re.search(rf"\b{re.escape(term)}\b", normalized):
                    seen.setdefault(term, {}).setdefault(claim, []).append(step_id)
    conflicts = []
    for term, renderings in seen.items():
        if len(renderings) > 1:
            conflicts.append({"term": term, "renderings": renderings})
    return conflicts


def disjunctive_fact_reason(value: object) -> str | None:
    """事实名里是否藏了析取。返回命中的析取词，没有则 None。"""
    if not isinstance(value, str):
        return None
    match = DISJUNCTIVE_FACT_PATTERN.search(value)
    return match.group(0) if match else None


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


# ---------------------------------------------------------------------------
# 第三部分：V3 查询派生（2026-08-21 拆网定案后老板拍板的升级）
#
# V2 的丢分根因：四路查询靠模型看完方法后自由发挥，必然产生宽泛章节词、
# 主体方向颠倒、原文没写的 D9/落陷/化解被硬塞进反例路。
# V3 铁律：支持路查询由程序从步骤已保存的逐字短引（claim_terms）确定性生成，
# 模型不再自由发挥。短引本身经过机器逐字校验（必须是 exact_text 子串），
# 所以派生查询天然做到：步级精确靶向、方向正确、词词有原文出处。
#
# 通用与书籍专属分开：派生函数是通用内核；下面两张表是 BPHS（Santhanam 译本）
# 专属术语表——换一本书换这两张表，函数不动。
# ---------------------------------------------------------------------------

# BPHS 十二宫名 → 宫位序数。次序出自原文 ch07:v37-38 自列的十二宫名
# （装配时 make_batch.verify_bhava_order 回原文核对同一张表的次序）。
BHAVA_ORDINALS = {
    "tanu": 1, "thanu": 1, "dhan": 2, "sahaj": 3, "bandhu": 4, "putr": 5,
    "ari": 6, "yuvati": 7, "randhr": 8, "dharm": 9, "karm": 10, "karma": 10,
    "labh": 11, "vyaya": 12, "lagn": 1, "lagna": 1,
}
# BPHS 行星梵文名 → 现代英文名（双轨检索：FTS5 吃梵文原词，语义检索吃英文）
GRAHA_ENGLISH = {
    "surya": "sun", "chandra": "moon", "mangal": "mars", "budh": "mercury",
    "guru": "jupiter", "shukra": "venus", "shukr": "venus", "shani": "saturn",
    "rahu": "rahu", "ketu": "ketu",
}

_ORDINAL_SUFFIX = {1: "1st", 2: "2nd", 3: "3rd"}


def _ordinal(number: int) -> str:
    return _ORDINAL_SUFFIX.get(number, f"{number}th")


def bilingual_variant(text: str, bhava_ordinals: dict | None = None,
                      graha_english: dict | None = None) -> str | None:
    """把含梵文宫名/曜名的逐字引文翻成现代英文序数写法，供语义检索用。

    例：`Dharm's Lord be in Karm Bhava` → `9th lord be in 10th house`。
    纯确定性替换，没有任何一处替换发生就返回 None（不产出无信息的复读）。
    """
    bhava_ordinals = BHAVA_ORDINALS if bhava_ordinals is None else bhava_ordinals
    graha_english = GRAHA_ENGLISH if graha_english is None else graha_english
    result = re.sub(r"</?sup>", "", text)
    changed = False

    def sub(pattern: str, repl_fn) -> None:
        nonlocal result, changed
        new = re.sub(pattern, repl_fn, result, flags=re.I)
        if new != result:
            changed = True
            result = new

    names = "|".join(sorted(bhava_ordinals, key=len, reverse=True))
    # X's Lord / Lord of X → Nth lord
    sub(rf"\b({names})['’]s\s+Lord", lambda m: f"{_ordinal(bhava_ordinals[m.group(1).lower()])} lord")
    sub(rf"\bLord\s+of\s+({names})\b", lambda m: f"{_ordinal(bhava_ordinals[m.group(1).lower()])} lord")
    # X Bhava / 裸宫名 → Nth house
    sub(rf"\b({names})\s+Bhava\b", lambda m: f"{_ordinal(bhava_ordinals[m.group(1).lower()])} house")
    sub(rf"\b({names})\b(?!\s*(?:Bhava|house|lord))",
        lambda m: f"{_ordinal(bhava_ordinals[m.group(1).lower()])} house")
    # 行星梵文名 → 英文名
    graha = "|".join(sorted(graha_english, key=len, reverse=True))
    sub(rf"\b({graha})\b", lambda m: graha_english[m.group(1).lower()])
    return result if changed else None


def derive_step_queries(step_id: str, claim_terms: dict) -> list[dict]:
    """从一步的逐字短引确定性生成支持路查询（V3 内核，模型零参与）。

    每条查询独立成串（不写混合长句）：
    - 每条条件短引单独一条（逐字，FTS5 直接命中）；
    - 每条结果短引单独一条（逐字）；
    - 每条条件＋第一条结果拼一条精准组合（含条件词与结果词，供重排核对完整关系）；
    - 每条逐字查询若含梵文术语，追加一条英文序数变体（双轨）。
    """
    conditions = [item["quote"] for item in claim_terms.get("conditions", []) if item.get("quote")]
    results = [item["quote"] for item in claim_terms.get("results", []) if item.get("quote")]
    derived: list[dict] = []
    seen: set[str] = set()

    def add(query: str, origin: str) -> None:
        cleaned = re.sub(r"</?sup>", "", query).strip()
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            derived.append({"step_id": step_id, "lane": "support", "origin": origin, "query": cleaned})

    for quote in conditions:
        add(quote, "verbatim_condition")
    for quote in results:
        add(quote, "verbatim_result")
    if results:
        for quote in conditions:
            add(f"{quote} {results[0]}", "verbatim_condition_plus_result")
    for item in list(derived):
        variant = bilingual_variant(item["query"])
        if variant and variant.casefold() != item["query"].casefold():
            add(variant, "bilingual_" + item["origin"])
    return derived


def normalize_for_verbatim(text: str) -> str:
    """逐字校验用的规范化：去 <sup> 标签、去音符、小写、去标点、压空白。

    标点不敏感：抽取员常把原文里相邻两句拼成一条查询（丢掉中间的句号），
    内容仍然逐字——实测 ch19-20 有 18 条这类"句号级差异"，不该按编造拦。
    去掉标点后，编造的内容（原文根本没有的词序）依旧接不上，闸门效力不变。"""
    cleaned = re.sub(r"</?sup>", "", text)
    cleaned = normalize_for_term_match(cleaned)
    cleaned = re.sub(r"[.,;:!?()\[\]{}\"'’‘“”/\\-]", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def is_verbatim_in(query: str, normalized_corpus: str) -> bool:
    """查询是否词词有原文出处。

    合格的两种形态（实测 ch19-20 全部 487 条派生查询与 15 条方法路查询归入这两类）：
    1. 整条是冻结原文（规范化后）的连续子串；
    2. 拆成不超过 3 段，每段要么是 ≥4 个词的连续逐字片段，要么是单个高风险
       专名表里的词（例：标题「The Sixteen Divisions of a Rāśi」＋「Navāńś」）。
    编造的查询（如 `Dharm Lord debilitated combust afflicted`）拼不出 ≥4 词的
    连续片段，仍然被拦。
    """
    normalized = normalize_for_verbatim(query)
    if not normalized:
        return False
    if normalized in normalized_corpus:
        return True
    words = normalized.split()
    fragments = 0
    index = 0
    while index < len(words):
        # 贪心找从 index 起最长的连续命中片段
        best = 0
        for end in range(index + 1, len(words) + 1):
            if " ".join(words[index:end]) in normalized_corpus:
                best = end
            else:
                break
        length = best - index
        if length >= 4:
            fragments += 1
            index = best
        elif length >= 1 and words[index] in HIGH_RISK_PROPER_NOUNS:
            fragments += 1
            index += 1
        else:
            return False
        if fragments > 3:
            return False
    return True
