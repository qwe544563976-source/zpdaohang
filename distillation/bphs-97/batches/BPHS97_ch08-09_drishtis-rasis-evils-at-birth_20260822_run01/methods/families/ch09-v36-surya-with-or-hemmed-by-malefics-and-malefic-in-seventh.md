---
method: ch09-v36-surya-with-or-hemmed-by-malefics-and-malefic-in-seventh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 太阳与凶星同宫或被凶星夹，且自太阳起第 7 位另有凶星：早年失父

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 太阳被凶星夹会怎样
- 早年失去父亲的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 自太阳（Surya）起算的第 7 位是否有另一颗凶星

## 按情况检查的事实

- 太阳（Surya）是否与凶星同宫
- 太阳（Surya）是否被凶星夹（hemmed between malefics）

## 依赖方法

- 无

## 执行步骤

### ch09-v36-surya-with-or-hemmed-by-malefics-and-malefic-in-seventh.step-001

- 动作：核对太阳是否与凶星同宫或被凶星夹，并核对自太阳起算第 7 位有无另一颗凶星。
- 适用范围：仅限本命盘对父亲的凶象；原文以太阳为父亲的指示星立说。
- 原文最小意思：太阳（Surya）与凶星同宫、或被凶星夹，同时自太阳起算的第 7 位另有一颗凶星时，会早年失去父亲。
- 本步骤产出事实：["太阳受克的早年失父判定"]
- 所需事实：["自太阳（Surya）起算的第 7 位是否有另一颗凶星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "自太阳（Surya）起算的第 7 位是否有另一颗凶星"}, {"operator": "OR", "operands": [{"fact_key": "太阳（Surya）是否与凶星同宫"}, {"fact_key": "太阳（Surya）是否被凶星夹（hemmed between malefics）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "自太阳（Surya）起算的第 7 位是否有另一颗凶星"}, "required_fact_keys": ["太阳（Surya）是否与凶星同宫"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否与凶星同宫"}, "selection_group": "ch09-v36-surya-with-or-hemmed-by-malefics-and-malefic-in-seventh.step-001:surya-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否与凶星同宫。"}, {"when": {"fact_key": "自太阳（Surya）起算的第 7 位是否有另一颗凶星"}, "required_fact_keys": ["太阳（Surya）是否被凶星夹（hemmed between malefics）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否被凶星夹（hemmed between malefics）"}, "selection_group": "ch09-v36-surya-with-or-hemmed-by-malefics-and-malefic-in-seventh.step-001:surya-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否被凶星夹（hemmed between malefics）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『早年失去父亲』补成具体年岁。", "不得省略自太阳起算第 7 位另有凶星这一前提。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：自太阳（Surya）起算的第 7 位是否有另一颗凶星。
- 缺失即停字段：["自太阳（Surya）起算的第 7 位是否有另一颗凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v36`｜PDF [24]｜“Early loss of father will take place, if Surya is with a malefic, or is hemmed between malefics, as there is another malefic in the 7<sup>th</sup> from Surya.”


## 四路查书计划

### 支持路

- Early loss of father will take place, if Surya is with a malefic, or is hemmed between malefics, as there is another malefic in the 7<sup>th</sup> from Surya
- 太阳 与凶星同宫 被夹 第七位凶星 失父

### 反例或取消路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Evil to Father (up to Sloka 42)
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 父亲用哪颗星看

## 上游问题

- 无

## 停止条件

- 缺少太阳同宫行星与被夹事实时停止。
- 缺少自太阳起算第 7 位的占据者事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
