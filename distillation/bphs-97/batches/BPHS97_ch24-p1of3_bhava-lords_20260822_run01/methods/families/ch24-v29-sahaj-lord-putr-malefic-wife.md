---
method: ch24-v29-sahaj-lord-putr-malefic-wife
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 妻子令人生畏：三宫主落五宫（Putr）且与凶星同宫或被凶星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我妻子的性子会不会很厉害
- 三宫主落五宫又碰上凶星会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 三宫主（Sahaj's Lord）是否落五宫（Putr）

## 按情况检查的事实

- 三宫主（Sahaj's Lord）是否与凶星同宫
- 三宫主（Sahaj's Lord）是否被凶星相照

## 依赖方法

- 无

## 执行步骤

### ch24-v29-sahaj-lord-putr-malefic-wife.step-001

- 动作：先核对三宫主（Sahaj's Lord）是否落五宫（Putr），再核对三宫主是否与凶星同宫，或是否受到凶星的相照。
- 适用范围：仅限本命盘三宫主（Sahaj's Lord）落宫主题；in the process 承同偈前句的「三宫主落五宫（Putr）」；原文把凶星与三宫主的关系明写成两种（与凶星同宫、受凶星相照），本步照此拆成两个并列分支，两种关系的另一端原文都写明是三宫主本身；本段原文自标「Effects of Sahaj’s Lord in Various Bhavas (up to Sloka 36)」（同章 v25）；原文以 wife 立说，属男命框架；凶星名册以本书 ch03:v11 的界定为准；原文未给婚期或时间限定。
- 原文最小意思：承同偈「三宫主（Sahaj's Lord）落五宫（Putr）」的配置，若三宫主与凶星同宫，或受到凶星的相照，命主会有一位令人生畏的妻子。
- 本步骤产出事实：["三宫主落五宫遇凶星的配偶性情判定"]
- 所需事实：["三宫主（Sahaj's Lord）是否落五宫（Putr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "三宫主（Sahaj's Lord）是否落五宫（Putr）"}, {"operator": "OR", "operands": [{"fact_key": "三宫主（Sahaj's Lord）是否与凶星同宫"}, {"fact_key": "三宫主（Sahaj's Lord）是否被凶星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "三宫主（Sahaj's Lord）是否落五宫（Putr）"}, "required_fact_keys": ["三宫主（Sahaj's Lord）是否与凶星同宫"], "branch_condition_logic": {"fact_key": "三宫主（Sahaj's Lord）是否与凶星同宫"}, "selection_group": "ch24-v29-sahaj-lord-putr-malefic-wife.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主（Sahaj's Lord）是否与凶星同宫。"}, {"when": {"fact_key": "三宫主（Sahaj's Lord）是否落五宫（Putr）"}, "required_fact_keys": ["三宫主（Sahaj's Lord）是否被凶星相照"], "branch_condition_logic": {"fact_key": "三宫主（Sahaj's Lord）是否被凶星相照"}, "selection_group": "ch24-v29-sahaj-lord-putr-malefic-wife.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主（Sahaj's Lord）是否被凶星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「令人生畏」写成家暴、离婚、克夫或配偶去世。", "不得在原文写明的同宫与被相照两种关系之外，另加别的关系类型。", "不得把本条的凶星换成吉星来套用。", "不得据此推断婚期或妻子人数。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：三宫主（Sahaj's Lord）是否落五宫（Putr）。
- 缺失即停字段：["三宫主（Sahaj's Lord）是否落五宫（Putr）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v29`｜PDF [42]｜“If Sahaj’s Lord is in Putr Bhava, the native will have sons and be virtuous. If in the process Sahaj’s Lord be yuti with, or receives a Drishti from a malefic, the native will have a formidable wife.”


## 四路查书计划

### 支持路

- If in the process Sahaj’s Lord be yuti with, or receives a Drishti from a malefic, the native will have a formidable wife
- 三宫主落五宫 与凶星同宫 被凶星相照 妻子令人生畏

### 反例或取消路

- WORTHY SPOUSE. The native will beget a spouse endowed with (the seven principal) virtues, who will expand his dynasty by sons and grandsons
- If Karm’s Lord is in Yuvati Bhava, the native will be endowed with happiness through wife, be intelligent, virtuous, eloquent, truthful and religious

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Putr Bhava. The learned should deduce from Putr Bhava amulets, sacred spells, learning, knowledge, sons, royalty (or authority), fall of position etc.
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- Effects of Sahaj’s Lord in Various Bhavas (up to Sloka 36)
- 判断妻子性情要核对哪些凶星关系

## 上游问题

- 无

## 停止条件

- 缺少三宫主是否落五宫（Putr）的事实时停止。
- 凶星名册未确定时，两个凶星关系分支停止。
- 三宫主与凶星同宫、被凶星相照两项事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
