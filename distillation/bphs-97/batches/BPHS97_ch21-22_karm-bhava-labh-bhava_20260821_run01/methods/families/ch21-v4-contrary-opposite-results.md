---
method: ch21-v4-contrary-opposite-results
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 相反情形只得相反结果：十宫主既不与吉星同宫也不落吉宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 十宫主没有吉星帮扶会怎样
- 这条规则反过来该怎么判

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否与吉星同宫
- 十宫主（Karm's Lord）是否落在吉宫（auspicious Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- ch21-v4-karm-lord-royal-gains

## 执行步骤

### ch21-v4-contrary-opposite-results.step-001

- 动作：核对同偈前句的两个条件是否都不成立，若都不成立则按原文判为只会出现相反的结果。
- 适用范围：承接同偈前句（十宫主与吉星同宫，或落在吉宫）；原文只说「相反情形」与「相反结果」，既未写出相反情形的具体配置，也未写出相反结果的具体内容，本条只按前句条件的否定接线。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：在与前句条件相反的情形下，只会出现相反的结果。
- 本步骤产出事实：["十宫主相反情形的相反结果判定"]
- 所需事实：["十宫主（Karm's Lord）是否与吉星同宫", "十宫主（Karm's Lord）是否落在吉宫（auspicious Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "十宫主（Karm's Lord）是否与吉星同宫"}]}, {"operator": "NOT", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落在吉宫（auspicious Bhava）"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「相反的结果」具体化为原文没有写的破财、失业、降职等断语。", "不得脱离同偈前句单独使用本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否与吉星同宫、十宫主（Karm's Lord）是否落在吉宫（auspicious Bhava）。
- 缺失即停字段：["十宫主（Karm's Lord）是否与吉星同宫", "十宫主（Karm's Lord）是否落在吉宫（auspicious Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v4`｜PDF [38]｜“In a contrary situation, only opposite results will come to pass.”


## 四路查书计划

### 支持路

- In a contrary situation, only opposite results will come to pass
- 十宫主 相反情形 相反结果

### 反例或取消路

- If Karm’s Lord is with a benefic, or be in an auspicious Bhava, one will always gain through royal patronage and in business
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon
- 凶星被吉星包围 恶果消失

### 适用边界路

- Ari, Randhr and Vyaya are Trikas, Dusthan, or malefic Bhavas
- Kendras and Konas (Putr and Dharm) are auspicious Bhavas, the association with which turns even evil into auspiciousness
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Effects of Karm’s Lord in Various Bhavas
- 判断相反情形要先核对前句列出的条件

## 上游问题

- 无

## 停止条件

- 缺少十宫主与吉星同宫的事实时停止。
- 缺少十宫主是否落吉宫的事实时停止。
- 吉星名册与吉宫的界定未取得时停止。
- 同偈前句的结论未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
