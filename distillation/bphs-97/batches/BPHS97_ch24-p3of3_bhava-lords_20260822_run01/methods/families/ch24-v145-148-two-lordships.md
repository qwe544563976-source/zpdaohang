---
method: ch24-v145-148-two-lordships
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 一星主两宫：依它的两个宫主身份分别推结果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 同一颗星管着两个宫时该怎么断
- 我盘里一颗星兼两个宫主该看哪一边

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星（Grah）同时主管两个宫（Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v145-148-two-lordships.step-001

- 动作：核对本盘中哪些行星（Grah）同时主管两个宫（Bhava），对这类行星按它的两个宫主身份分别推出结果。
- 适用范围：适用于本章各宫主落各宫的效果推断（同偈自述「those are the effects of Bhava Lords」）；原文只说按两个宫主身份分别推出，没有给合并结果的算法；原文未给时间限定。
- 原文最小意思：某行星（Grah）主管两个宫（Bhava）时，该行星的结果要依它的两个宫主身份分别推出。
- 本步骤产出事实：["一星主两宫时的双宫主身份推断路径"]
- 所需事实：["本盘中哪些行星（Grah）同时主管两个宫（Bhava）"]
- 条件关系：{"fact_key": "本盘中哪些行星（Grah）同时主管两个宫（Bhava）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文给出把两个宫主身份的结果合并起来的算法。", "不得据此判定哪一个宫主身份更重要。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星（Grah）同时主管两个宫（Bhava）。
- 缺失即停字段：["本盘中哪些行星（Grah）同时主管两个宫（Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v145-148`｜PDF [50]｜“In the case of a Grah, owning two Bhavas, the results are to be deducted based on its two lordships.”


## 四路查书计划

### 支持路

- In the case of a Grah, owning two Bhavas, the results are to be deducted based on its two lordships.
- 一颗行星主管两个宫 分别按两个宫主身份推断

### 反例或取消路

- 无

### 适用边界路

- those are the effects of Bhava Lords, which are to be deduced, considering their strengths and weaknesses
- Effects of the Bhava Lords
- 一星主两宫这条规则的适用范围

### 判断方法路

- Effects of the Bhava Lords
- 宫主身份怎么定

## 上游问题

- 无

## 停止条件

- 缺少『本盘中哪些行星同时主管两个宫』的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
