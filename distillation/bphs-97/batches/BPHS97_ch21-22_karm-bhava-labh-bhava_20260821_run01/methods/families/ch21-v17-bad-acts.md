---
method: ch21-v17-bad-acts
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 从事恶行：十宫主落八宫、八宫主落十宫并与凶星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会走上歪路
- 十宫主与八宫主互换位置对我意味着什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否落八宫（Randhr）
- 八宫主（Randhr's Lord）是否落十宫（Karm）
- 八宫主（Randhr's Lord）是否与凶星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v17-bad-acts.step-001

- 动作：核对十宫主（Karm's Lord）是否落八宫（Randhr）、八宫主（Randhr's Lord）是否落十宫（Karm）并与凶星同宫。
- 适用范围：仅限本命盘十宫（Karm）行为品性主题；原文三个条件同时成立才下断语；原文未给行为种类与时间，凶星名册按本书自身的定义取。
- 原文最小意思：十宫主落八宫、八宫主落十宫并与凶星同宫时，命主从事恶行。
- 本步骤产出事实：["十宫主八宫主互涉从事恶行判定"]
- 所需事实：["十宫主（Karm's Lord）是否落八宫（Randhr）", "八宫主（Randhr's Lord）是否落十宫（Karm）", "八宫主（Randhr's Lord）是否与凶星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落八宫（Randhr）"}, {"fact_key": "八宫主（Randhr's Lord）是否落十宫（Karm）"}, {"fact_key": "八宫主（Randhr's Lord）是否与凶星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断恶行的种类、后果或应期。", "不得只凭十宫主落八宫一项就下断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否落八宫（Randhr）、八宫主（Randhr's Lord）是否落十宫（Karm）、八宫主（Randhr's Lord）是否与凶星同宫。
- 缺失即停字段：["十宫主（Karm's Lord）是否落八宫（Randhr）", "八宫主（Randhr's Lord）是否落十宫（Karm）", "八宫主（Randhr's Lord）是否与凶星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v17`｜PDF [39]｜“One will indulge in bad acts, if Karm’s Lord is in Randhr Bhava, while Randhr’s Lord is in Karm Bhava with a malefic.”


## 四路查书计划

### 支持路

- One will indulge in bad acts, if Karm’s Lord is in Randhr Bhava, while Randhr’s Lord is in Karm Bhava with a malefic
- 十宫主落八宫 八宫主落十宫 与凶星同宫 恶行

### 反例或取消路

- Should Karm’s Lord be in Lagn along with Lagn’s Lord, as Chandra is in an angle, or in a trine, the native will be interested in good deeds
- If Karm’s Lord is strong and in exaltation, or in its own Rāśi/Navāńś, the native will derive extreme paternal happiness, will enjoy fame and will perform good deeds

### 适用边界路

- If Karm’s Lord is in Randhr Bhava, the native will be devoid of acts, long-lived and intent on blaming others
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- If the Lord of Karm Bhava is relegated to Randhr Bhava along with Rahu, the native will hate others; be a great fool and will do bad deeds
- 判断十宫（Karm）行为善恶应检查十宫主落在哪一宫

## 上游问题

- 无

## 停止条件

- 缺少十宫主落宫事实时停止。
- 缺少八宫主落宫事实时停止。
- 缺少八宫主是否与凶星同宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
