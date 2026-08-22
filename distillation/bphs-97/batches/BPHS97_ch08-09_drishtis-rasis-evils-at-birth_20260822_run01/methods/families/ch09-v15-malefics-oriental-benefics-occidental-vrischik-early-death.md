---
method: ch09-v15-malefics-oriental-benefics-occidental-vrischik-early-death
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶星尽在东半、吉星尽在西半：生于天蝎座（Vrischik）者早亡

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 凶星都在东半会怎样
- 生于天蝎的人短寿吗
- 吉星凶星分居东西半怎么断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘所有凶星是否都落东半（oriental half）
- 本盘所有吉星是否都落西半（occidental half）
- 本人是否生于天蝎座（Vrischik）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v15-malefics-oriental-benefics-occidental-vrischik-early-death.step-001

- 动作：核对凶星是否尽在东半、吉星是否尽在西半，并核对是否生于天蝎座。
- 适用范围：仅限原文所写『生于 Vrischik 者』；原文没有指明这是上升落天蝎、月亮落天蝎还是别的起点，未确定即停判。原文另加一句『此事无须再作思量』的强度语。
- 原文最小意思：所有凶星落东半（oriental half）、吉星落西半（occidental half）时，生于天蝎座（Vrischik）者会早亡；此事无须再作思量。
- 本步骤产出事实：["凶吉分居东西半的天蝎生人早亡判定"]
- 所需事实：["本盘所有凶星是否都落东半（oriental half）", "本盘所有吉星是否都落西半（occidental half）", "本人是否生于天蝎座（Vrischik）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘所有凶星是否都落东半（oriental half）"}, {"fact_key": "本盘所有吉星是否都落西半（occidental half）"}, {"fact_key": "本人是否生于天蝎座（Vrischik）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『生于 Vrischik』坐实成上升落天蝎或月亮落天蝎——原文没有指明，未确定即停判。", "不得据本偈把结论推广到天蝎座以外的生人。", "不得把『早亡』补成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘所有凶星是否都落东半（oriental half）、本盘所有吉星是否都落西半（occidental half）、本人是否生于天蝎座（Vrischik）。
- 缺失即停字段：["本盘所有凶星是否都落东半（oriental half）", "本盘所有吉星是否都落西半（occidental half）", "本人是否生于天蝎座（Vrischik）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v15`｜PDF [23]｜“Should all the malefics be in the oriental half, while benefics are in the occidental half, early death of one born in Vrischik, will follow. In this case there is no need of any rethinking.”


## 四路查书计划

### 支持路

- Should all the malefics be in the oriental half, while benefics are in the occidental half, early death of one born in Vrischik, will follow
- 凶星东半 吉星西半 天蝎 早亡

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Short-life Combinations (up to Sloka 23)
- Early Death

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 吉星凶星怎么定

## 上游问题

- 无

## 停止条件

- 原文只写『生于 Vrischik』，未指明以上升、月亮还是其他起点取值；该指代未确定即停判。
- 缺少东半、西半的划分事实时停止（本偈未给东西半的界定）。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
