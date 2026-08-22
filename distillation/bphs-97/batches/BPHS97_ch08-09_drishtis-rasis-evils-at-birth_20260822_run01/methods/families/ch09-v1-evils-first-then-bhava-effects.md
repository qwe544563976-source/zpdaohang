---
method: ch09-v1-evils-first-then-bhava-effects
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 断十二宫之前，先经上升估量凶象与其化解因素

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 看盘该从哪里开始
- 什么时候才能断十二宫的效果
- 凶象要在什么时候看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升（Lagn）落在哪个星座（Rāśi）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v1-evils-first-then-bhava-effects.step-001

- 动作：先经上升（Lagn）估量凶象与其化解因素，之后再宣说十二宫（Bhavas）的效果。
- 适用范围：仅限判断次序：原文只给先后，不给凶象的具体判准（凶象条见本章以下各偈，化解见第 10 章）。
- 原文最小意思：先经上升（Lagn）估量凶象与其化解因素，然后再宣说十二宫（12 Bhavas）的效果。
- 本步骤产出事实：["是否已完成凶象与化解因素的估量"]
- 所需事实：["本盘上升（Lagn）落在哪个星座（Rāśi）"]
- 条件关系：{"fact_key": "本盘上升（Lagn）落在哪个星座（Rāśi）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本偈判断具体是哪一种凶象或哪一种化解——原文这里只给次序。", "不得把『通过上升估量』改写成原文没有的其他起点。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagn）落在哪个星座（Rāśi）。
- 缺失即停字段：["本盘上升（Lagn）落在哪个星座（Rāśi）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v1`｜PDF [22]｜“O Brahmin, first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas.”


## 四路查书计划

### 支持路

- O Brahmin, first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas.
- 先看凶象与化解 再断十二宫

### 反例或取消路

- 无

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- 凶象估量的年龄边界

### 判断方法路

- Evils at Birth
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- 判断次序 先凶象后十二宫

## 上游问题

- 无

## 停止条件

- 缺少本盘上升（Lagn）时停止。
- 原文本偈只给次序、不给凶象与化解的判准，具体判断须另查本章以下各偈与第 10 章，本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
