---
method: ch15-v1-bandhu-topic-scope
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第15章主题归属：三宫结果已述，转入四宫结果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 四宫管的是什么事
- 问住房和母亲要查哪一章

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 提问是否属于四宫（Bandhu Bhava）主题

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch15-v1-bandhu-topic-scope.step-001

- 动作：确认提问落在四宫（Bandhu Bhava）主题上，再进入本章后续的四宫规则。
- 适用范围：仅限界定第15章的主题归属；原文此处没有给出任何星盘条件或吉凶结果。
- 原文最小意思：第15章在简述三宫（Sahaj Bhava）的结果之后，转入与四宫（Bandhu Bhava）有关的结果。
- 本步骤产出事实：["四宫主题归属判定"]
- 所需事实：["提问是否属于四宫（Bandhu Bhava）主题"]
- 条件关系：{"fact_key": "提问是否属于四宫（Bandhu Bhava）主题"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此对四宫做任何吉凶判断，本条只界定章节主题。", "不得把三宫（Sahaj Bhava）的结论搬到四宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：提问是否属于四宫（Bandhu Bhava）主题。
- 缺失即停字段：["提问是否属于四宫（Bandhu Bhava）主题"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v1`｜PDF [29]｜“thus have been briefly told the effects of Sahaj Bhava. Now listen to the results, related to Bandhu Bhava.”


## 四路查书计划

### 支持路

- results related to Bandhu Bhava chapter opening
- 第15章 四宫 Bandhu Bhava 主题

### 反例或取消路

- Sahaj Bhava effects belong to third house not fourth
- 三宫结果 与四宫结果 区分

### 适用边界路

- chapter scope statement no chart condition
- 本章开篇是否给出判断条件

### 判断方法路

- how BPHS orders Bhava chapters
- 四宫结果应查哪一章

## 上游问题

- 无

## 停止条件

- 提问与四宫主题无关时停止。
- 本条只界定主题，缺少后续具体星盘条件时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
