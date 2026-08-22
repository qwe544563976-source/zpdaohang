---
method: ch03-v35-38-day-night-strength
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 昼夜强弱：夜间有力之曜、昼夜皆有力之曜与只在白昼有力之曜

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我是夜里出生的 哪些行星更有力
- 白天出生哪些行星有力

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘出生时段是白天（day）还是夜间（night）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v35-38-day-night-strength.step-001

- 动作：核对本盘出生时段，判断夜间有力之曜与昼夜皆有力之曜。
- 适用范围：第3章诸曜强弱条；原文只按昼夜分列有力之曜，未给强弱的量值。
- 原文最小意思：夜间（night）有力的是月亮（Chandra）、火星（Mangal）与土星（Shani），而水星（Budh）昼夜（day and night）皆有力。
- 本步骤产出事实：["夜间有力之曜判定"]
- 所需事实：["本盘出生时段是白天（day）还是夜间（night）"]
- 条件关系：{"fact_key": "本盘出生时段是白天（day）还是夜间（night）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出昼夜强弱的具体分值。", "不得把「昼夜皆有力」读成水星（Budh）比其余诸曜更强。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生时段是白天（day）还是夜间（night）。
- 缺失即停字段：["本盘出生时段是白天（day）还是夜间（night）"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v35-38`｜PDF [11]｜“Again, strong during night are Chandra, Mangal and Shani, while Budh is strong during day and night.”

### ch03-v35-38-day-night-strength.step-002

- 动作：核对本盘出生时段，判断只在白昼有力的行星。
- 适用范围：第3章诸曜强弱条；原文只按昼夜分列有力之曜，未给强弱的量值。
- 原文最小意思：其余（Guru、Surya 与 Shukr）只在白昼（daytime）有力。
- 本步骤产出事实：["白昼有力之曜判定"]
- 所需事实：["本盘出生时段是白天（day）还是夜间（night）"]
- 条件关系：{"fact_key": "本盘出生时段是白天（day）还是夜间（night）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出交点（Rahu、Ketu）的昼夜强弱——本偈只列七曜。", "不得据本条推出昼夜强弱的具体分值。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生时段是白天（day）还是夜间（night）。
- 缺失即停字段：["本盘出生时段是白天（day）还是夜间（night）"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v35-38`｜PDF [11]｜“The rest (i.e. Guru, Surya and Shukr) are strong only in daytime.”


## 四路查书计划

### 支持路

- Again, strong during night are Chandra, Mangal and Shani, while Budh is strong during day and night
- The rest (i.e. Guru, Surya and Shukr) are strong only in daytime
- 昼夜强弱 夜间有力 白昼有力

### 反例或取消路

- 无

### 适用边界路

- Kaal Bal comprises of the following subdivisions: Nathonnata Bal (diurnal and nocturnal)
- 昼夜强弱属 Kaal Bal 的一项

### 判断方法路

- Firstly Nathonnata Bal. Find out the difference between midnight and the apparent birth time, which is called Unnata
- Budh, irrespective of day and night, gets full Nathonnata Bal
- 昼夜强弱怎么算

## 上游问题

- 无

## 停止条件

- 缺少本盘出生昼夜时段的事实时停止。
- 本条只分昼夜列出有力之曜，没有给强弱数值，要量化必须另查 Kaal Bal 原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
