---
method: ch09-v17-malefics-in-tanu-yuvati-chandra-with-malefic-no-relief
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶星占据一宫与七宫、月亮与凶星同宫且无吉星救助：早亡

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 凶星占一宫七宫怎么断
- 月亮与凶星同宫没有吉星救会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 一宫（Tanu Bhava）是否被凶星占据
- 七宫（Yuvati Bhava）是否被凶星占据
- 月亮（Chandra）是否与凶星同宫
- 月亮（Chandra）是否得到吉星的救助（relief from a benefic）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v17-malefics-in-tanu-yuvati-chandra-with-malefic-no-relief.step-001

- 动作：核对一宫与七宫的凶星占据、月亮与凶星的同宫，以及有无来自吉星的救助。
- 适用范围：仅限本命盘出生时的凶象；原文只写 with no relief from a benefic，没有界定『救助』的具体形式。
- 原文最小意思：凶星占据一宫（Tanu）与七宫（Yuvati Bhava）、月亮（Chandra）与凶星同宫且得不到吉星的救助时，也会致早亡。
- 本步骤产出事实：["一七宫凶星兼月亮受克的早亡判定"]
- 所需事实：["一宫（Tanu Bhava）是否被凶星占据", "七宫（Yuvati Bhava）是否被凶星占据", "月亮（Chandra）是否与凶星同宫", "月亮（Chandra）是否得到吉星的救助（relief from a benefic）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "一宫（Tanu Bhava）是否被凶星占据"}, {"fact_key": "七宫（Yuvati Bhava）是否被凶星占据"}, {"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否得到吉星的救助（relief from a benefic）"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文定义『来自吉星的救助』是相照、同宫还是别的形式——原文没有写。", "不得把『早亡』补成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：一宫（Tanu Bhava）是否被凶星占据、七宫（Yuvati Bhava）是否被凶星占据、月亮（Chandra）是否与凶星同宫、月亮（Chandra）是否得到吉星的救助（relief from a benefic）。
- 缺失即停字段：["一宫（Tanu Bhava）是否被凶星占据", "七宫（Yuvati Bhava）是否被凶星占据", "月亮（Chandra）是否与凶星同宫", "月亮（Chandra）是否得到吉星的救助（relief from a benefic）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v17`｜PDF [23]｜“Malefics, occupying Tanu and Yuvati Bhava, while Chandra is yuti with a malefic with no relief from a benefic, will also cause premature death.”


## 四路查书计划

### 支持路

- Malefics, occupying Tanu and Yuvati Bhava, while Chandra is yuti with a malefic with no relief from a benefic, will also cause premature death
- 一宫七宫凶星 月亮同凶 无吉救 早亡

### 反例或取消路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Short-life Combinations (up to Sloka 23)
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 吉星救助怎么看

## 上游问题

- 无

## 停止条件

- 缺少一宫、七宫的凶星占据事实时停止。
- 缺少月亮同宫行星事实时停止。
- 『来自吉星的救助』原文未给判准，该事实取不到值时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
