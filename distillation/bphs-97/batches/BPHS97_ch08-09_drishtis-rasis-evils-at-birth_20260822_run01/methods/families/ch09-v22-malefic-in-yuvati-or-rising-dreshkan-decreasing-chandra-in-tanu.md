---
method: ch09-v22-malefic-in-yuvati-or-rising-dreshkan-decreasing-chandra-in-tanu
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶星落七宫或上升所在三分盘，渐亏的月亮落一宫：早亡

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 凶星落上升的三分盘会怎样
- 渐亏月亮落一宫又有凶星怎么断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）

## 按情况检查的事实

- 七宫（Yuvati Bhava）是否被凶星占据
- 上升所在的三分盘（Dreshkan D3）内是否有凶星

## 依赖方法

- 无

## 执行步骤

### ch09-v22-malefic-in-yuvati-or-rising-dreshkan-decreasing-chandra-in-tanu.step-001

- 动作：核对渐亏的月亮是否落一宫，并核对七宫或上升所在三分盘内有无凶星。
- 适用范围：仅限本命盘出生时的凶象；原文所说 rising Dreshkan 指上升所落的那一个三分盘（Dreshkan D3）。
- 原文最小意思：凶星落七宫（Yuvati Bhava）、或落上升所在的三分盘（rising Dreshkan D3），同时渐亏的月亮（decreasing Chandra）落一宫（Tanu Bhava）时，会早早遭遇死亡。
- 本步骤产出事实：["渐亏月亮落一宫兼凶星的早亡判定"]
- 所需事实：["渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）"}, {"operator": "OR", "operands": [{"fact_key": "七宫（Yuvati Bhava）是否被凶星占据"}, {"fact_key": "上升所在的三分盘（Dreshkan D3）内是否有凶星"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）"}, "required_fact_keys": ["七宫（Yuvati Bhava）是否被凶星占据"], "branch_condition_logic": {"fact_key": "七宫（Yuvati Bhava）是否被凶星占据"}, "selection_group": "ch09-v22-malefic-in-yuvati-or-rising-dreshkan-decreasing-chandra-in-tanu.step-001:malefic-place", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫（Yuvati Bhava）是否被凶星占据。"}, {"when": {"fact_key": "渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）"}, "required_fact_keys": ["上升所在的三分盘（Dreshkan D3）内是否有凶星"], "branch_condition_logic": {"fact_key": "上升所在的三分盘（Dreshkan D3）内是否有凶星"}, "selection_group": "ch09-v22-malefic-in-yuvati-or-rising-dreshkan-decreasing-chandra-in-tanu.step-001:malefic-place", "stop_condition": "选中该分支后，缺少以下事实即停止：上升所在的三分盘（Dreshkan D3）内是否有凶星。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把三分盘（Dreshkan D3）换成九分盘或十分盘。", "不得把『渐亏的月亮』换成一般的月亮。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）。
- 缺失即停字段：["渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v22`｜PDF [23]｜“With a malefic in Yuvati Bhava, or in the rising Dreshkan, while decreasing Chandra is in Tanu Bhava, death be experienced early.”


## 四路查书计划

### 支持路

- With a malefic in Yuvati Bhava, or in the rising Dreshkan, while decreasing Chandra is in Tanu Bhava, death be experienced early
- 凶星七宫 上升三分盘 渐亏月亮一宫 早亡

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Short-life Combinations (up to Sloka 23)
- One third of a Rashiis called Dreshkan

### 判断方法路

- Evils at Birth
- The 1<sup>st</sup> , 5<sup>th</sup> and the 9<sup>th</sup> Rāśis from a Rashiare its three Dreshkanas
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 三分盘怎么起

## 上游问题

- 无

## 停止条件

- 缺少月亮盈亏状态与落宫时停止。
- 缺少七宫凶星占据事实时停止。
- 缺少上升所在三分盘（Dreshkan D3）的取值时该分支停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
