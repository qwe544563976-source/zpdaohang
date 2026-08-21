---
method: ch17-v9-chandra-water-danger
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 水厄与痰疾：月亮与六宫主、八宫主同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有水上的危险
- 我容易有痰湿一类的毛病

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否与六宫主（Ari's Lord）同宫
- 月亮（Chandra）是否与八宫主（Randhr's Lord）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v9-chandra-water-danger.step-001

- 动作：核对月亮（Chandra）是否与六宫主和八宫主同宫。
- 适用范围：仅限本命盘月亮与六宫主、八宫主的同宫；原文未给时间与地点限定。
- 原文最小意思：月亮与六宫主和八宫主同宫时，会有水厄与痰性疾病。
- 本步骤产出事实：["月亮聚六八宫主的水厄痰疾判定"]
- 所需事实：["月亮（Chandra）是否与六宫主（Ari's Lord）同宫", "月亮（Chandra）是否与八宫主（Randhr's Lord）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与六宫主（Ari's Lord）同宫"}, {"fact_key": "月亮（Chandra）是否与八宫主（Randhr's Lord）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断溺水的时间、地点或致死与否。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否与六宫主（Ari's Lord）同宫、月亮（Chandra）是否与八宫主（Randhr's Lord）同宫。
- 缺失即停字段：["月亮（Chandra）是否与六宫主（Ari's Lord）同宫", "月亮（Chandra）是否与八宫主（Randhr's Lord）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Chandra in Yuti with the Lords of Ari and Randhr Bhava will inflict dangers through water and phlegmatic disorders.”


## 四路查书计划

### 支持路

- 月亮 六宫主 八宫主 同宫 水厄 痰疾

### 反例或取消路

- Guru in similar case will destroy any disease
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed

### 适用边界路

- Danger through water will have to be feared during Putr and Dharm years
- Chandra is very windy and phlegmatic 月亮的体质属性

### 判断方法路

- 判断水厄应检查月亮与哪些宫主的关系

## 上游问题

- 无

## 停止条件

- 缺少月亮与六宫主同宫事实时停止。
- 缺少月亮与八宫主同宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
