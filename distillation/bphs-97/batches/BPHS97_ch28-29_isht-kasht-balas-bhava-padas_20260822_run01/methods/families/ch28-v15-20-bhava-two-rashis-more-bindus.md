---
method: ch28-v15-20-bhava-two-rashis-more-bindus
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 宫横跨两星座：Bindus 较多的那个星座结果较佳

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这一宫跨了两个星座该怎么断
- 两个宫主该听哪一个

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘所考察宫（Bhava）是否横跨两个星座（Rāśi）
- 本盘所考察宫（Bhava）横跨的两个星座（Rāśi）中哪一个的 Bindus 较多

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch28-v15-20-bhava-two-rashis-more-bindus.step-001

- 动作：先看所考察宫是否横跨两个星座，再比较两个星座的 Bindus 多寡，取 Bindus 较多的那个星座作为该宫较有利的一边。
- 适用范围：仅限本章宫效应合成的校正环节；原文另写“If both the Rāśis have more auspicious Bindus, take the average”，本步不把那一句当成本条的结论。
- 原文最小意思：某宫（Bhava）横跨两个星座（Rāśi）时，按两个宫主作校正；其中 Bindus 较多的那个星座，就该宫而言会给出较有利的结果。
- 本步骤产出事实：["所考察宫跨两星座时的较佳星座判定"]
- 所需事实：["本盘所考察宫（Bhava）是否横跨两个星座（Rāśi）", "本盘所考察宫（Bhava）横跨的两个星座（Rāśi）中哪一个的 Bindus 较多"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘所考察宫（Bhava）是否横跨两个星座（Rāśi）"}, {"fact_key": "本盘所考察宫（Bhava）横跨的两个星座（Rāśi）中哪一个的 Bindus 较多"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只说较有利，不得据此把另一个星座断成凶。", "不得据此推断具体事项、程度或时间。", "不得把本条推广到只占一个星座的宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘所考察宫（Bhava）是否横跨两个星座（Rāśi）、本盘所考察宫（Bhava）横跨的两个星座（Rāśi）中哪一个的 Bindus 较多。
- 缺失即停字段：["本盘所考察宫（Bhava）是否横跨两个星座（Rāśi）", "本盘所考察宫（Bhava）横跨的两个星座（Rāśi）中哪一个的 Bindus 较多"]
- 原文证据：
  - `bphs-97:santhanam:ch28:v15-20`｜PDF [61]｜“If a Bhava extends to two Rāśis, the rectification will be done, as per both the Lords.”
  - `bphs-97:santhanam:ch28:v15-20`｜PDF [61]｜“In that case, whichever Rashihas more Bindus, that Rashiwill yield more favourable results, concerning that Bhava.”


## 四路查书计划

### 支持路

- In that case, whichever Rashihas more Bindus, that Rashiwill yield more favourable results, concerning that Bhava
- If a Bhava extends to two Rāśis, the rectification will be done, as per both the Lords
- 宫跨两星座 Bindus 较多者结果较佳

### 反例或取消路

- If both the Rāśis have more auspicious Bindus, take the average
- 两个星座 Bindus 都多时取平均

### 适用边界路

- The strength of a Bhava and its Lord have already been explained
- Isht and Kasht Balas
- 本条只在宫效应合成的校正环节内成立

### 判断方法路

- In Ashtak Varg add Bindus (auspicious points) and deduct Karanas (inauspicious points)
- 怎样数一个星座的 Bindus

## 上游问题

- 无

## 停止条件

- 缺少所考察宫是否横跨两个星座的事实时停止。
- 缺少两个星座的 Bindus 数值时停止。
- 两个星座 Bindus 相等时，原文未给判法，停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
