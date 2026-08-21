---
method: ch12-v9-birth-of-twins
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 生为双胞胎之一：太阳落四足星座且其余行星有力落双体星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我是不是双胞胎
- 太阳落四足星座代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否落四足星座（quadruped Rāśi）
- 其余行星（others）是否落双体星座（Dual Rāśi）
- 其余行星（others）是否有力

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch12-v9-birth-of-twins.step-001

- 动作：核对太阳是否落在四足星座，并核对其余行星是否有力地落在双体星座。
- 适用范围：仅限本命盘出生情形主题；原文只写 others，没有界定它指哪几颗行星、是否需要全部，范围未确定即停判。
- 原文最小意思：太阳（Surya）落四足星座（quadruped Rāśi），同时其余行星（others）落在双体星座（Dual Rāśis）且有力时，命主生为双胞胎之一。
- 本步骤产出事实：["太阳四足星座与其余行星双体星座的双胞胎判定"]
- 所需事实：["太阳（Surya）是否落四足星座（quadruped Rāśi）", "其余行星（others）是否落双体星座（Dual Rāśi）", "其余行星（others）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落四足星座（quadruped Rāśi）"}, {"fact_key": "其余行星（others）是否落双体星座（Dual Rāśi）"}, {"fact_key": "其余行星（others）是否有力"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自行把 others 收窄成某几颗行星，也不得断定必须全部行星都满足，原文没有界定。", "不得据此推断双胞胎的性别、先后或人数。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落四足星座（quadruped Rāśi）、其余行星（others）是否落双体星座（Dual Rāśi）、其余行星（others）是否有力。
- 缺失即停字段：["太阳（Surya）是否落四足星座（quadruped Rāśi）", "其余行星（others）是否落双体星座（Dual Rāśi）", "其余行星（others）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v9`｜PDF [27]｜“The native, who has Surya in a quadruped Rāśi, while others are in Dual Rāśis with strength, is born, as one of the twins.”


## 四路查书计划

### 支持路

- The native, who has Surya in a quadruped Rāśi, while others are in Dual Rāśis with strength, is born, as one of the twins
- 太阳落四足星座 其余行星有力落双体星座 双胞胎

### 反例或取消路

- 无

### 适用边界路

- It is a quadruped Rashiand strong during night
- The Navāńś calculation are for a Movable Rashifrom there itself, for a Fixed Rashifrom the 9th thereof and for a Dual Rashifrom the 5th thereof
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- Shani in Dharm Bhava, while Putr’s Lord is in Putr itself, gives 7 sons, out of which twins will be born twice
- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- 判断双胞胎要看太阳与其余行星落在哪一类星座

## 上游问题

- 无

## 停止条件

- 原文只写 others，未界定其范围，范围未定即停判。
- 缺少太阳落四足星座的事实时停止。
- 有力的判准未定时停止（强弱判准见第27章 Shad Bal）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
