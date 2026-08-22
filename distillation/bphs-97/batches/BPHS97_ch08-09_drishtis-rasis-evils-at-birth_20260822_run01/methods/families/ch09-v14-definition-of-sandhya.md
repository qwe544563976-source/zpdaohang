---
method: ch09-v14-definition-of-sandhya
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 晨昏交界（Sandhya）的界定：日出前 3 Ghati 与日落后同样长的一段

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 晨昏交界怎么算
- Sandhya 是什么时候
- 出生在不在晨昏交界

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘出生地当日日出（rising Surya）的时刻是几点
- 本盘出生地当日日落（Surya’s set）的时刻是几点
- 本盘出生时刻是几点

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v14-definition-of-sandhya.step-001

- 动作：按日出与日落时刻各取 3 Ghati，定出晨交界与昏交界，并核对出生时刻是否落在其中。
- 适用范围：仅限晨昏交界的界定；本偈界定的正是上一偈（v13）判断出生时辰所用的 morning, or evening junctions，本偈自身不给吉凶断语。
- 原文最小意思：见到升起的太阳（Surya）半轮之前的 3 Ghatis，以及太阳（Surya）落下之后同样长的一段，分别称为晨交界（morning twilight）与昏交界（evening twilight）。
- 本步骤产出事实：["本盘出生是否在晨交界（morning twilight）内", "本盘出生是否在昏交界（evening twilight）内"]
- 所需事实：["本盘出生地当日日出（rising Surya）的时刻是几点", "本盘出生地当日日落（Surya’s set）的时刻是几点", "本盘出生时刻是几点"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘出生地当日日出（rising Surya）的时刻是几点"}, {"fact_key": "本盘出生地当日日落（Surya’s set）的时刻是几点"}, {"fact_key": "本盘出生时刻是几点"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 3 Ghati 改成原文没写的其他时长。", "不得据本偈直接下吉凶断语——本偈只给晨昏交界的界定。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生地当日日出（rising Surya）的时刻是几点、本盘出生地当日日落（Surya’s set）的时刻是几点、本盘出生时刻是几点。
- 缺失即停字段：["本盘出生地当日日出（rising Surya）的时刻是几点", "本盘出生地当日日落（Surya’s set）的时刻是几点", "本盘出生时刻是几点"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v14`｜PDF [23]｜“3 Ghatis before the sight of the semi disc (half) of the rising Surya and a similar duration, following Surya’s set, are called, as morning twilight and evening twilight, respectively.”


## 四路查书计划

### 支持路

- 3 Ghatis before the sight of the semi disc (half) of the rising Surya and a similar duration, following Surya’s set, are called, as morning twilight and evening twilight, respectively.
- 晨昏交界 Sandhya 3 Ghati 日出 日落

### 反例或取消路

- 无

### 适用边界路

- Early death will come to pass, if there be a birth in the morning, or evening junctions
- 晨昏交界界定的适用范围

### 判断方法路

- Definition of Sandhya
- Evils at Birth
- 出生时辰怎么定

## 上游问题

- 无

## 停止条件

- 缺少出生地当日日出或日落时刻时停止。
- 缺少出生时刻时停止。
- 原文本偈只给界定、不给吉凶，要断吉凶须查上一偈（v13）等条，本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
