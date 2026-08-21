---
method: ch05-v2-3-bhava-lagn
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 宫上升（Bhava Lagn）起法：日出到出生每 5 Ghatis 一个，商加日出时太阳黄经

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的宫上升（Bhava Lagn）在哪里
- Bhava Lagn 怎么起
- 特殊上升点怎么算

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘从日出到出生经过了多少 Ghati
- 本盘日出时刻太阳（Surya）的黄经是多少度

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch05-v2-3-bhava-lagn.step-001

- 动作：从日出量到出生时刻，按每 5 Ghatis（即 120 分钟）为一个宫上升（Bhava Lagn）来分段。
- 适用范围：仅限本命盘由日出起算的宫上升分段；原文只给日出为起点，未说其他起点。
- 原文最小意思：自日出至出生时刻，每 5 Ghatis（即 120 分钟）构成一个宫上升（Bhava Lagn）。
- 本步骤产出事实：["自日出起算已满的宫上升段数"]
- 所需事实：["本盘从日出到出生经过了多少 Ghati"]
- 条件关系：{"fact_key": "本盘从日出到出生经过了多少 Ghati"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 5 Ghatis 的分段改成原文没写的其他时长。", "不得把起点从日出改成原文没写的其他时刻。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘从日出到出生经过了多少 Ghati。
- 缺失即停字段：["本盘从日出到出生经过了多少 Ghati"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v2-3`｜PDF [16]｜“From sunrise to the time of birth every 5 Ghatis (or 120 minutes) constitute one Bhava Lagn.”

### ch05-v2-3-bhava-lagn.step-002

- 动作：把自日出起算的出生时间（以 Ghatis、Vighatis 等计）除以 5，再把商等加到日出时太阳（Surya）的黄经上，所得即宫上升（Bhava Lagn）。
- 适用范围：仅限宫上升（Bhava Lagn）的起法本身；原文这一偈只给算法，不给它的吉凶断法。
- 原文最小意思：把自日出起算的出生时间（Ghatis、Vighatis 等）除以 5，把商等加到日出时太阳（Surya）的黄经上，所得即宫上升（Bhava Lagn）。
- 本步骤产出事实：["宫上升（Bhava Lagn）的黄经"]
- 所需事实：["本盘从日出到出生经过了多少 Ghati", "本盘日出时刻太阳（Surya）的黄经是多少度"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘从日出到出生经过了多少 Ghati"}, {"fact_key": "本盘日出时刻太阳（Surya）的黄经是多少度"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文要求用日出时的太阳黄经，不得换成出生时刻的太阳黄经。", "不得据这一偈直接下吉凶断语——本偈只给起法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘从日出到出生经过了多少 Ghati、本盘日出时刻太阳（Surya）的黄经是多少度。
- 缺失即停字段：["本盘从日出到出生经过了多少 Ghati", "本盘日出时刻太阳（Surya）的黄经是多少度"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v2-3`｜PDF [16]｜“Divide the time of birth (in Ghatis, Vighatis etc.) from sunrise by 5 and add the quotient etc. to Surya’s longitude, as at sunrise. This is called Bhava Lagn.”


## 四路查书计划

### 支持路

- From sunrise to the time of birth every 5 Ghatis (or 120 minutes) constitute one Bhava Lagn
- Divide the time of birth (in Ghatis, Vighatis etc.) from sunrise by 5 and add the quotient etc. to Surya’s longitude, as at sunrise. This is called Bhava Lagn
- 宫上升 Bhava Lagn 起法 日出 太阳黄经

### 反例或取消路

- Hora Lagn repeats itself every 2½ Ghatis (i. e. 60 minutes)
- Now listen to the method of working out Ghati Lagn. This Lagn changes along with every Ghati (24 minutes) from the sunrise
- 特殊上升之间 除数不同 Hora Ghati

### 适用边界路

- The natal Lagn is to be calculated according to birth place, while Bhava Lagna, Hora Lagn etc. are common to all places
- Note birth time in Ghatis and Vighatis. Consider the number of Ghatis past, as number of Rāśis, or Ghati Lagnas
- Keeping the Grahas at birth, as it is, prepare various Bhava Kundalis with respect to each special Lagn and analyze, as done for the natal Lagn

### 判断方法路

- Oh excellent of the Brahmins, I explain below again some special Lagnas, viz. Bhava Lagna, Hora Lagn and Ghati Lagn
- Use of Special Lagnas. Keeping the Grahas at birth, as it is, prepare various Bhava Kundalis
- 特殊上升 Bhava Hora Ghati 怎么算

## 上游问题

- 无

## 停止条件

- 缺少本盘从日出到出生的 Ghati 数时停止。
- 缺少日出时刻太阳（Surya）黄经时停止。
- 日出时刻本身未定（出生地或出生钟点不明）时停止。
- 原文这一偈只给宫上升（Bhava Lagn）的起法、未给吉凶断法，要断吉凶须另查原文，本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
