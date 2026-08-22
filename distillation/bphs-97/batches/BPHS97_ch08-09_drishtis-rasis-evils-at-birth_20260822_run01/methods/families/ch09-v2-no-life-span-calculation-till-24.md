---
method: ch09-v2-no-life-span-calculation-till-24
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 24 岁之前不做确定的寿命推算

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 什么时候才能算寿命
- 小孩子的寿命能不能算
- 早年凶象到几岁为止

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本人当前年龄是多少岁

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v2-no-life-span-calculation-till-24.step-001

- 动作：核对命主当前年岁，未满原文所说的年岁时不做确定的寿命推算。
- 适用范围：仅限寿命推算的时机限制；原文只给年岁界限，不给寿命的推算方法（详见第 43 章）。
- 原文最小意思：致提早终结的凶象存在到人 24 岁为止，因此在该年岁之前不应做确定的寿命推算。
- 本步骤产出事实：["是否可以对本盘做确定的寿命推算"]
- 所需事实：["本人当前年龄是多少岁"]
- 条件关系：{"fact_key": "本人当前年龄是多少岁"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 24 岁改成原文没写的其他年岁。", "不得据本偈推断 24 岁之后寿命一定长或一定短——原文只说此前不作确定推算。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本人当前年龄是多少岁。
- 缺失即停字段：["本人当前年龄是多少岁"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v2`｜PDF [22]｜“Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.”


## 四路查书计划

### 支持路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- 24 岁之前 不算寿命

### 反例或取消路

- Surya in Vyaya will confer a hundred-year life span on one born in Tul Lagn.

### 适用边界路

- Short-life Combinations (up to Sloka 23)
- Kindly detail methods of ascertaining the life-span of human beings.
- 寿命推算的年龄门槛

### 判断方法路

- Evils at Birth
- O Brahmin, first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas.
- 寿命怎么推算

## 上游问题

- 无

## 停止条件

- 缺少命主当前年岁时停止。
- 原文本偈不给寿命推算方法，要算寿命须另查原文（第 43 章 Longevity），本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
