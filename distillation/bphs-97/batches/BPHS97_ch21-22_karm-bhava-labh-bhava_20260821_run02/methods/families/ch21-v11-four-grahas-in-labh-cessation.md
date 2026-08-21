---
method: ch21-v11-four-grahas-in-labh-cessation
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 职务中断：罗睺、太阳、土星与火星同落十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的工作会不会中断
- 十一宫聚了这四颗星会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 罗睺（Rahu）是否落十一宫（Labh）
- 太阳（Surya）是否落十一宫（Labh）
- 土星（Shani）是否落十一宫（Labh）
- 火星（Mangal）是否落十一宫（Labh）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v11-four-grahas-in-labh-cessation.step-001

- 动作：核对罗睺（Rahu）、太阳（Surya）、土星（Shani）与火星（Mangal）是否都落十一宫（Labh）。
- 适用范围：仅限四颗行星同落十一宫这一种配置；原文以 his 指代命主，未给时间限定。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：罗睺、太阳、土星与火星同落十一宫时，命主的职务会中断。
- 本步骤产出事实：["四颗行星聚十一宫的职务中断判定"]
- 所需事实：["罗睺（Rahu）是否落十一宫（Labh）", "太阳（Surya）是否落十一宫（Labh）", "土星（Shani）是否落十一宫（Labh）", "火星（Mangal）是否落十一宫（Labh）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "罗睺（Rahu）是否落十一宫（Labh）"}, {"fact_key": "太阳（Surya）是否落十一宫（Labh）"}, {"fact_key": "土星（Shani）是否落十一宫（Labh）"}, {"fact_key": "火星（Mangal）是否落十一宫（Labh）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断中断的时间、原因或是否复职。", "不得把四颗行星同落放宽成其中几颗落十一宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：罗睺（Rahu）是否落十一宫（Labh）、太阳（Surya）是否落十一宫（Labh）、土星（Shani）是否落十一宫（Labh）、火星（Mangal）是否落十一宫（Labh）。
- 缺失即停字段：["罗睺（Rahu）是否落十一宫（Labh）", "太阳（Surya）是否落十一宫（Labh）", "土星（Shani）是否落十一宫（Labh）", "火星（Mangal）是否落十一宫（Labh）"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v11`｜PDF [38]｜“Should Rahu, Surya, Shani and Mangal be in Labh Bhava, the native will incur cessation of his duties.”


## 四路查书计划

### 支持路

- Should Rahu, Surya, Shani and Mangal be in Labh Bhava, the native will incur cessation of his duties
- 罗睺 太阳 土星 火星 同落十一宫 职务中断

### 反例或取消路

- Should Labh’s Lord be in Labh itself, or be in an angle, or in a trine from Lagna, there will be many gains
- If Labh’s Lord is in Karm Bhava, the native will be honoured by the king, be virtuous
- 十一宫主落十一宫 收益丰厚

### 适用边界路

- Indications of Labh Bhava. All articles, son’s wife, income, prosperity, quadrupeds etc. are to be understood from Labh Bhava
- Sahaj, Ari, Karm and Labh are Upachayas
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- I now explain effects relating to Labh Bhava, the auspiciousness of which Bhava will make one happy at all times
- 判断十一宫聚集行星的效果要查什么

## 上游问题

- 无

## 停止条件

- 缺少罗睺、太阳、土星或火星落十一宫其中任一事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
