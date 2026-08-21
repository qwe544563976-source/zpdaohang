---
method: ch17-v20-fire-and-bird-danger
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 罗睺落六宫、土星落罗睺起第八宫：第1岁第2岁的火厄与 Sahaj 年的鸟患

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 孩子一两岁会不会有火的危险
- 小孩早年有哪些凶年

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 罗睺（Rahu）是否落六宫（Ari）
- 土星（Shani）是否落罗睺（Rahu）起第八宫（Randhr）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v20-fire-and-bird-danger.step-001

- 动作：核对罗睺是否落六宫、土星是否落自罗睺起算的第八宫，判断幼年火厄。
- 适用范围：仅限本命盘幼年火厄；原文以孩童立说，未说明火厄轻重与致死与否。
- 原文最小意思：罗睺落六宫、土星落罗睺起第八宫时，第1岁与第2岁孩子会有火的危险。
- 本步骤产出事实：["幼年火厄判定"]
- 所需事实：["罗睺（Rahu）是否落六宫（Ari）", "土星（Shani）是否落罗睺（Rahu）起第八宫（Randhr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "罗睺（Rahu）是否落六宫（Ari）"}, {"fact_key": "土星（Shani）是否落罗睺（Rahu）起第八宫（Randhr）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断火厄的形式、伤情或致死与否。", "不得把第1岁与第2岁推广到其他年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：罗睺（Rahu）是否落六宫（Ari）、土星（Shani）是否落罗睺（Rahu）起第八宫（Randhr）。
- 缺失即停字段：["罗睺（Rahu）是否落六宫（Ari）", "土星（Shani）是否落罗睺（Rahu）起第八宫（Randhr）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v20-22`｜PDF [33]｜“if Rahu is in Ari, while Shani is in Randhr from the said Rahu, the child will have danger through fire at the age of 1 and 2”

### ch17-v20-fire-and-bird-danger.step-002

- 动作：同一组合下，另看 Sahaj 年的鸟患。
- 适用范围：仅限本命盘 Sahaj 年的鸟患；原文只写 Sahaj 年，未换算成具体年岁。
- 原文最小意思：罗睺落六宫、土星落罗睺起第八宫时，在 Sahaj 年会有鸟类带来的祸患。
- 本步骤产出事实：["Sahaj 年鸟患判定"]
- 所需事实：["罗睺（Rahu）是否落六宫（Ari）", "土星（Shani）是否落罗睺（Rahu）起第八宫（Randhr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "罗睺（Rahu）是否落六宫（Ari）"}, {"fact_key": "土星（Shani）是否落罗睺（Rahu）起第八宫（Randhr）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 Sahaj 年自行换算成本条没写出的年岁。", "不得据此推断祸患的形式与轻重。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：罗睺（Rahu）是否落六宫（Ari）、土星（Shani）是否落罗睺（Rahu）起第八宫（Randhr）。
- 缺失即停字段：["罗睺（Rahu）是否落六宫（Ari）", "土星（Shani）是否落罗睺（Rahu）起第八宫（Randhr）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v20-22`｜PDF [33]｜“if Rahu is in Ari, while Shani is in Randhr from the said Rahu”
  - `bphs-97:santhanam:ch17:v20-22`｜PDF [33]｜“in Sahaj year birds will bring some evils”


## 四路查书计划

### 支持路

- if Rahu is in Ari, while Shani is in Randhr from the said Rahu danger through fire at the age of 1 and 2
- 罗睺六宫 土星罗睺起第八宫 火厄 Sahaj 年 鸟

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age

### 判断方法路

- 判断幼年凶年应从哪一颗星起算

## 上游问题

- 无

## 停止条件

- 缺少罗睺落六宫事实时停止。
- 缺少土星相对罗睺落宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
