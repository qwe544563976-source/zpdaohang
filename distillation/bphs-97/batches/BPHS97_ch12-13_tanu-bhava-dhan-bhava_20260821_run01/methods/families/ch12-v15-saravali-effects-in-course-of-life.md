---
method: ch12-v15-saravali-effects-in-course-of-life
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 记号在一生中才显现：所涉行星既不落本星座也不落本九分盘

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身上的痕迹会不会后来才出现
- 不落本星座本九分盘时记号什么时候出现

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 与该肢体关联的行星是否落本星座（own Rāśi）
- 与该肢体关联的行星是否落本九分盘（own Navāńś）

## 按情况检查的事实

- 无

## 依赖方法

- ch12-v15-saravali-effects-from-birth

## 执行步骤

### ch12-v15-saravali-effects-in-course-of-life.step-001

- 动作：在与该肢体关联的行星既不落本星座也不落本九分盘时，把效果的出现时间判为一生的过程中。
- 适用范围：此句是英译者在括注中转引 Saravali 第4章第6颂的说法，不是 BPHS 作者自断；原文的 In other cases 直接指前一句所述 落本星座或本九分盘 之外的情形。
- 原文最小意思：上述以外的情形下，这些效果会在命主一生的过程中才显现。
- 本步骤产出事实：["肢体记号在一生中显现的判定"]
- 所需事实：["与该肢体关联的行星是否落本星座（own Rāśi）", "与该肢体关联的行星是否落本九分盘（own Navāńś）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "与该肢体关联的行星是否落本星座（own Rāśi）"}]}, {"operator": "NOT", "operands": [{"fact_key": "与该肢体关联的行星是否落本九分盘（own Navāńś）"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 in the course of one’s life 落实成某个年份或大运，原文没有给。", "不得把这条转引的 Saravali 说法当成 BPHS 作者自断。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：与该肢体关联的行星是否落本星座（own Rāśi）、与该肢体关联的行星是否落本九分盘（own Navāńś）。
- 缺失即停字段：["与该肢体关联的行星是否落本星座（own Rāśi）", "与该肢体关联的行星是否落本九分盘（own Navāńś）"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v15`｜PDF [27]｜“In other cases it will be in the course of one’s life, that these effects will come to pass”


## 四路查书计划

### 支持路

- In other cases it will be in the course of one’s life, that these effects will come to pass
- 不落本星座本九分盘 记号在一生中才显现

### 反例或取消路

- that a malefic, or a benefic, if be in own Rāśi, or Navāńś, the effects will be right from birth

### 适用边界路

- Effects of Moles, Marks, Signs etc. for Men and Women
- The Navāńś calculation are for a Movable Rashifrom there itself, for a Fixed Rashifrom the 9th thereof and for a Dual Rashifrom the 5th thereof
- The Sixteen Divisions of a Rāśi

### 判断方法路

- Now I will describe to you the effects of moles, marks, spots and signs, found on the body of women and men
- One third of a Rashiis called Dreshkan. These are totally 36, counted from Mesh, repeating thrice at the rate of 12 per round
- 判断记号出现的时间要看所涉行星落不落本星座本九分盘

## 上游问题

- 无

## 停止条件

- 缺少行星是否落本星座、是否落本九分盘的事实时停止。
- 此条出自转引 Saravali，需要与 BPHS 自断区分时须回查原书。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
