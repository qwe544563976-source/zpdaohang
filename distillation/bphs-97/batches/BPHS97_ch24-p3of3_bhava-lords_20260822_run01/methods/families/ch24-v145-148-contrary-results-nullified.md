---
method: ch24-v145-148-contrary-results-nullified
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 两个宫主身份指出相反结果：结果归于无效

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 同一颗星推出的两个结果打架时怎么办
- 为什么我盘里的吉凶好像互相抵消

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星（Grah）同时主管两个宫（Bhava）
- 该行星两个宫主身份所指的结果是否彼此相反

## 按情况检查的事实

- 无

## 依赖方法

- ch24-v145-148-two-lordships

## 执行步骤

### ch24-v145-148-contrary-results-nullified.step-001

- 动作：对同时主管两个宫（Bhava）的行星（Grah），核对它两个宫主身份所指的结果是否彼此相反，据此判断结果是否归于无效。
- 适用范围：适用于本章各宫主落各宫的效果推断（同偈自述「those are the effects of Bhava Lords」）；原文没有界定什么算「相反」，该判准未确定即停判；原文也没有说明哪些属于「性质各异的结果」；原文未给时间限定。
- 原文最小意思：某行星（Grah）主管两个宫（Bhava），由此指示出的结果彼此相反时，这些结果归于无效，性质各异的结果则会应验。
- 本步骤产出事实：["双宫主身份结果相反时的抵消判定"]
- 所需事实：["本盘中哪些行星（Grah）同时主管两个宫（Bhava）", "该行星两个宫主身份所指的结果是否彼此相反"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星（Grah）同时主管两个宫（Bhava）"}, {"fact_key": "该行星两个宫主身份所指的结果是否彼此相反"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文定义什么算「相反结果」；未确定即停判。", "不得替原文划定哪些属于「性质各异的结果」。", "不得把「归于无效」写成转吉、转凶或按比例折算。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星（Grah）同时主管两个宫（Bhava）、该行星两个宫主身份所指的结果是否彼此相反。
- 缺失即停字段：["本盘中哪些行星（Grah）同时主管两个宫（Bhava）", "该行星两个宫主身份所指的结果是否彼此相反"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v145-148`｜PDF [50]｜“In the case of a Grah, owning two Bhavas, the results are to be deducted based on its two lordships.”
  - `bphs-97:santhanam:ch24:v145-148`｜PDF [50]｜“If contrary results are thus indicated, the results will be nullified, while results of varied nature will come to pass.”


## 四路查书计划

### 支持路

- In the case of a Grah, owning two Bhavas, the results are to be deducted based on its two lordships. If contrary results are thus indicated, the results will be nullified, while results of varied nature will come to pass.
- 两个宫主身份结果相反 互相抵消

### 反例或取消路

- 无

### 适用边界路

- those are the effects of Bhava Lords, which are to be deduced, considering their strengths and weaknesses
- Effects of the Bhava Lords
- 结果相反时归于无效这条规则的适用范围

### 判断方法路

- Effects of the Bhava Lords
- 宫主身份怎么定

## 上游问题

- 无

## 停止条件

- 缺少『本盘中哪些行星同时主管两个宫』的事实时停止。
- 原文未界定「相反结果」，该项未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
