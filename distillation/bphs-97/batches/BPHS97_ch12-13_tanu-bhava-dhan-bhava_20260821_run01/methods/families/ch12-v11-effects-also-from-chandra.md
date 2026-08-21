---
method: ch12-v11-effects-also-from-chandra
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 断语也要以月亮起算：适用于上升的效果同样用于月亮

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我该从上升看还是从月亮看
- 月亮能不能当上升用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘月亮（Chandra）落在哪一宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch12-v11-effects-also-from-chandra.step-001

- 动作：凡是以上升为起点作出的断语，再以月亮所落之处为起点重做一遍。
- 适用范围：本偈是通则性的方法指示，没有给出任何具体断语内容，也没有说以月亮起算与以上升起算孰先孰后。
- 原文最小意思：凡是适用于上升（Lagn）的断语，通晓占星者也应以月亮（Chandra）为依据来推断。
- 本步骤产出事实：["以月亮为起点重做上升断语的指示"]
- 所需事实：["本盘月亮（Chandra）落在哪一宫"]
- 条件关系：{"fact_key": "本盘月亮（Chandra）落在哪一宫"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此给出以月亮为起点的具体断语内容，本偈只给方法指示，没有给任何结论。", "不得断言以月亮起算与以上升起算哪一个更准或优先，原文没有说。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘月亮（Chandra）落在哪一宫。
- 缺失即停字段：["本盘月亮（Chandra）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v11`｜PDF [27]｜“The learned in Jyotish should base the effects on Chandra also, as are applicable to Lagn.”


## 四路查书计划

### 支持路

- The learned in Jyotish should base the effects on Chandra also, as are applicable to Lagn
- 适用于上升的断语也要以月亮为依据

### 反例或取消路

- 无

### 适用边界路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Whatever results are to be known from Bandhu, Tanu, Dhan, Labh and Dharm should also be known from the 4th of Chandra, from Kark Rashiitself and from the 2nd, 11th and 9th from Chandra, respectively
- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- 判断时要不要同时从月亮起算

## 上游问题

- 无

## 停止条件

- 缺少月亮落宫事实时停止。
- 本偈没有给出具体断语内容，需要结论时须回到对应章节的原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
