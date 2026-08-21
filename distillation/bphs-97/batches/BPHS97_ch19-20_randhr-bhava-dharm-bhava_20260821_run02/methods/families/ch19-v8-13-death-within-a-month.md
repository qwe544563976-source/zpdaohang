---
method: ch19-v8-13-death-within-a-month
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 出生后一个月内去世：八宫主落八宫、月亮与凶星同宫且无吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮与凶星同宫又没有吉星照会怎样
- 婴儿期最凶的组合是什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫主（Randhr's Lord）是否落八宫（Randhr）
- 月亮（Chandra）是否与凶星同宫
- 月亮（Chandra）是否被吉星相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch19-v8-13-death-within-a-month.step-001

- 动作：核对八宫主（Randhr's Lord）是否落八宫，并核对月亮（Chandra）是否与凶星同宫且未受吉星相照。
- 适用范围：仅限本命盘寿命主题；原文把结果限在出生后一个月内。
- 原文最小意思：八宫主落八宫、月亮与凶星同宫且未受吉星相照时，孩子在出生后一个月内去世。
- 本步骤产出事实：["八宫主落八宫月亮受凶的一月内去世判定"]
- 所需事实：["八宫主（Randhr's Lord）是否落八宫（Randhr）", "月亮（Chandra）是否与凶星同宫", "月亮（Chandra）是否被吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落八宫（Randhr）"}, {"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否被吉星相照"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把一个月的期限改写成别的时段。", "不得据此推断死因。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否落八宫（Randhr）、月亮（Chandra）是否与凶星同宫、月亮（Chandra）是否被吉星相照。
- 缺失即停字段：["八宫主（Randhr's Lord）是否落八宫（Randhr）", "月亮（Chandra）是否与凶星同宫", "月亮（Chandra）是否被吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v8-13`｜PDF [36]｜“Within a month of birth, death will befall the child, if Randhr’s Lord is in Randhr itself, while Chandra is with malefics and be bereft of beneficial Drishti.”


## 四路查书计划

### 支持路

- Within a month of birth, death will befall the child, if Randhr’s Lord is in Randhr itself, while Chandra is with malefics and be bereft of beneficial Drishti
- 八宫主落八宫 月亮与凶星同宫 无吉星相照 出生一个月内去世

### 反例或取消路

- Should Chandra be in Ari, Randhr, or Vyaya Bhava and receives a Drishti from a malefic, the child will die soon. If in the process there be a Drishti from a benefic, it may live up to 8
- a single, but strong Guru in Lagn will ward off all the evils
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- Chandra is capable of causing early end, if she is with a malefic in Yuvati, Randhr, or Tanu Bhava and unrelated to a benefic

### 判断方法路

- first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas
- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- 婴儿夭险要看月亮的哪些状态

## 上游问题

- 无

## 停止条件

- 缺少八宫主落宫事实时停止。
- 缺少月亮同宫或受相照的事实时停止。
- 吉凶星名册未定时停止（判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
