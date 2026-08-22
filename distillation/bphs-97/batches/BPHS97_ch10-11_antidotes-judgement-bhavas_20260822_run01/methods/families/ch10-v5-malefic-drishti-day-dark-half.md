---
method: ch10-v5-malefic-drishti-day-dark-half
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 消解凶恶：暗半月昼生者上升受凶星相照（承本偈前句）

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 白天出生上升被凶星照怎么看
- 凶星相照上升是不是一定不好

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘出生时段是白天（day）还是夜间（night）
- 本盘出生时的月相属暗半月（dark half）还是明半月（bright half）
- 上升（Lagn）是否被凶星相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch10-v5-malefic-drishti-day-dark-half.step-001

- 动作：核对出生是否在暗半月（dark half）的白天，并核对上升（Lagn）是否被凶星相照。
- 适用范围：仅限第 10 章消解凶恶（Antidotes for Evils）主题；本句以 Similarly 承本偈前句，结果词取自前句「All evils are destroyed」；本条只适用于暗半月昼生者，原文未给时间限定。
- 原文最小意思：承本偈前句，生于暗半月（dark half）白天者，其上升（Lagn）被凶星相照时，一切凶恶被摧毁。
- 本步骤产出事实：["暗半月昼生上升受凶照消解凶恶判定"]
- 所需事实：["本盘出生时段是白天（day）还是夜间（night）", "本盘出生时的月相属暗半月（dark half）还是明半月（bright half）", "上升（Lagn）是否被凶星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘出生时段是白天（day）还是夜间（night）"}, {"fact_key": "本盘出生时的月相属暗半月（dark half）还是明半月（bright half）"}, {"fact_key": "上升（Lagn）是否被凶星相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把本条搬到夜间出生或明半月出生的盘上。", "不得据此推断凶星相照在别处也一律消解凶恶。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生时段是白天（day）还是夜间（night）、本盘出生时的月相属暗半月（dark half）还是明半月（bright half）、上升（Lagn）是否被凶星相照。
- 缺失即停字段：["本盘出生时段是白天（day）还是夜间（night）", "本盘出生时的月相属暗半月（dark half）还是明半月（bright half）", "上升（Lagn）是否被凶星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch10:v5`｜PDF [25]｜“All evils are destroyed”
  - `bphs-97:santhanam:ch10:v5`｜PDF [25]｜“Similarly a malefic’s Drishti on Lagn of one born during day time in the dark half.”


## 四路查书计划

### 支持路

- Similarly a malefic’s Drishti on Lagn of one born during day time in the dark half
- 暗半月昼生 上升被凶星相照 一切凶恶被摧毁

### 反例或取消路

- If Shani and Mangal give a Drishti to Lagna, as the luminaries are yuti with Rahu (elsewhere), the child will live a fortnight
- Should Chandra be in Ari, Randhr, or Vyaya Bhava and receives a Drishti from a malefic, the child will die soon

### 适用边界路

- Definition of Sandhya. 3 Ghatis before the sight of the semi disc (half) of the rising Surya and a similar duration, following Surya’s set, are called, as morning twilight and evening twilight, respectively
- 昼夜与明暗半月的界定

### 判断方法路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- O Brahmin, first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas
- 怎样判断上升是否被凶星相照

## 上游问题

- 无

## 停止条件

- 缺少出生昼夜事实时停止。
- 缺少出生月相（明半月／暗半月）事实时停止。
- 缺少上升是否被凶星相照的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
