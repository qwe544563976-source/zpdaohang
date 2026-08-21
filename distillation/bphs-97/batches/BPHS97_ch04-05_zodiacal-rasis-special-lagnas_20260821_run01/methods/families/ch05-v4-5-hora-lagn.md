---
method: ch05-v4-5-hora-lagn
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 时上升（Hora Lagn）起法：日出到出生每 2½ Ghatis 一个，商加日出时太阳黄经

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的时上升（Hora Lagn）在哪里
- Hora Lagn 怎么起
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

### ch05-v4-5-hora-lagn.step-001

- 动作：从日出量到出生时刻，按每 2½ Ghatis（即 60 分钟）为一段，数出时上升（Hora Lagn）重复了几次。
- 适用范围：仅限本命盘由日出起算的时上升分段；原文只给日出为起点，未说其他起点。
- 原文最小意思：自日出至出生时刻，时上升（Hora Lagn）每 2½ Ghatis（即 60 分钟）重复一次。
- 本步骤产出事实：["自日出起算已满的时上升段数"]
- 所需事实：["本盘从日出到出生经过了多少 Ghati"]
- 条件关系：{"fact_key": "本盘从日出到出生经过了多少 Ghati"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 2½ Ghatis 的分段改成原文没写的其他时长。", "不得把起点从日出改成原文没写的其他时刻。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘从日出到出生经过了多少 Ghati。
- 缺失即停字段：["本盘从日出到出生经过了多少 Ghati"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v4-5`｜PDF [16]｜“Again from sunrise till the time of birth Hora Lagn repeats itself every 2½ Ghatis (i. e. 60 minutes).”

### ch05-v4-5-hora-lagn.step-002

- 动作：把自日出至出生已过的时间除以 2½，把所得的商等以星座、度数等加到日出时太阳（Surya）的黄经上。
- 适用范围：仅限时上升（Hora Lagn）的起法本身；原文这一偈只给算法，不给它的吉凶断法。
- 原文最小意思：把自日出至出生已过的时间除以 2½，再把商等以星座（Rāśis）、度数等加到日出时太阳（Surya）的黄经上，即得时上升（Hora Lagn）的星座（Rāśi）与度数。
- 本步骤产出事实：["时上升（Hora Lagn）的黄经"]
- 所需事实：["本盘从日出到出生经过了多少 Ghati", "本盘日出时刻太阳（Surya）的黄经是多少度"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘从日出到出生经过了多少 Ghati"}, {"fact_key": "本盘日出时刻太阳（Surya）的黄经是多少度"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文要求用日出时的太阳黄经，不得换成出生时刻的太阳黄经。", "不得据这一偈直接下吉凶断语——本偈只给起法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘从日出到出生经过了多少 Ghati、本盘日出时刻太阳（Surya）的黄经是多少度。
- 缺失即停字段：["本盘从日出到出生经过了多少 Ghati", "本盘日出时刻太阳（Surya）的黄经是多少度"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v4-5`｜PDF [16]｜“Divide the time past up to birth from sunrise by 2½ and add the quotient etc. in Rāśis, degrees and so on to the longitude of Surya, as at the sunrise. This will yield Hora Lagn in Rāśi, degrees etc.”


## 四路查书计划

### 支持路

- Hora Lagn repeats itself every 2½ Ghatis 60 minutes from sunrise
- Divide the time past up to birth from sunrise by 2½ add the quotient Surya longitude
- 时上升 Hora Lagn 起法 日出 太阳黄经

### 反例或取消路

- From sunrise to the time of birth every 5 Ghatis constitute one Bhava Lagn
- Now listen to the method of working out Ghati Lagn. This Lagn changes along with every Ghati (24 minutes) from the sunrise
- 特殊上升 除数不同 Bhava Lagn Ghati Lagn 起法差别

### 适用边界路

- The natal Lagn is to be calculated according to birth place Bhava Lagna Hora Lagn common to all places
- Out of the two, viz. natal Lagn and Hora Lagna, whichever is stronger, from there Varnad starts
- Ghati Vighati 时间单位 与 日出 起算

### 判断方法路

- Use of Special Lagnas prepare various Bhava Kundalis with respect to each special Lagn
- I explain below again some special Lagnas, viz. Bhava Lagna, Hora Lagn and Ghati Lagn
- 时上升 Hora Lagn 起出来以后怎么用

## 上游问题

- 无

## 停止条件

- 缺少本盘从日出到出生的 Ghati 数时停止。
- 缺少日出时刻太阳（Surya）黄经时停止。
- 日出时刻本身未定（出生地或出生钟点不明）时停止。
- 原文这一偈只给时上升（Hora Lagn）的起法、未给吉凶断法，要断吉凶须另查原文，本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
