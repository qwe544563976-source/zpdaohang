---
method: ch05-v6-8-ghati-lagn
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 刻上升（Ghati Lagn）起法：每 Ghati 一个，Vighatis 除 2 化度分，加日出时太阳黄经

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的刻上升（Ghati Lagn）在哪里
- Ghati Lagn 怎么起
- 特殊上升怎么按 Ghati 算

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘从日出到出生经过了多少 Ghati
- 本盘从日出到出生经过了多少 Vighati
- 本盘日出时刻太阳（Surya）的黄经是多少度

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch05-v6-8-ghati-lagn.step-001

- 动作：把出生时间记成 Ghatis 与 Vighatis，再把自日出起已过的 Ghati 数取作星座数，也就是刻上升（Ghati Lagn）数。
- 适用范围：仅限本命盘由日出起算的刻上升；原文这一偈末句注明「So say Maharishis, like Narada」，是转述诸大仙（如那罗陀）之说，结论强度不等同作者自断。
- 原文最小意思：刻上升（Ghati Lagn）自日出起每过一个 Ghati（24 分钟）变换一次；把出生时间记为 Ghatis 与 Vighatis，已过的 Ghati 数就作为星座（Rāśis）数，也就是刻上升（Ghati Lagnas）数。
- 本步骤产出事实：["自日出起算已过的 Ghati 数（即刻上升数）"]
- 所需事实：["本盘从日出到出生经过了多少 Ghati", "本盘从日出到出生经过了多少 Vighati"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘从日出到出生经过了多少 Ghati"}, {"fact_key": "本盘从日出到出生经过了多少 Vighati"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把每 Ghati 一个的分段改成原文没写的其他时长。", "不得把起点从日出改成原文没写的其他时刻。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘从日出到出生经过了多少 Ghati、本盘从日出到出生经过了多少 Vighati。
- 缺失即停字段：["本盘从日出到出生经过了多少 Ghati", "本盘从日出到出生经过了多少 Vighati"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v6-8`｜PDF [16]｜“This Lagn changes along with every Ghati (24 minutes) from the sunrise. Note birth time in Ghatis and Vighatis. Consider the number of Ghatis past, as number of Rāśis, or Ghati Lagnas.”

### ch05-v6-8-ghati-lagn.step-002

- 动作：把 Vighatis 除以 2，算出在该刻上升（Ghati Lagn）中已过的度数与弧分。
- 适用范围：仅限本命盘由日出起算的刻上升；原文这一偈末句注明「So say Maharishis, like Narada」，是转述诸大仙（如那罗陀）之说，结论强度不等同作者自断。
- 原文最小意思：把 Vighatis 除以 2，即得在该刻上升（Ghati Lagn）中已过的度数与弧分。
- 本步骤产出事实：["该刻上升中已过的度分"]
- 所需事实：["本盘从日出到出生经过了多少 Vighati"]
- 条件关系：{"fact_key": "本盘从日出到出生经过了多少 Vighati"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把除数 2 换成原文没写的其他数。", "不得把这一步算出的度分挪去别的特殊上升的起法上。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘从日出到出生经过了多少 Vighati。
- 缺失即停字段：["本盘从日出到出生经过了多少 Vighati"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v6-8`｜PDF [16]｜“The Vighatis be divided by 2 to arrive at degrees and minutes of arc, past in the said Ghati Lagn.”

### ch05-v6-8-ghati-lagn.step-003

- 动作：把前两步所得的星座、度、分之积加到日出时太阳（Surya）的黄经上，得出刻上升（Ghati Lagn）的确切位置。
- 适用范围：仅限本命盘由日出起算的刻上升；原文这一偈末句注明「So say Maharishis, like Narada」，是转述诸大仙（如那罗陀）之说，结论强度不等同作者自断。
- 原文最小意思：把所得的星座（Rāśis）、度数与弧分加到日出时太阳（Surya）的黄经上，即得刻上升（Ghati Lagn）的确切位置。
- 本步骤产出事实：["刻上升（Ghati Lagn）的黄经"]
- 所需事实：["自日出起算已过的 Ghati 数（即刻上升数）", "该刻上升中已过的度分", "本盘日出时刻太阳（Surya）的黄经是多少度"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "自日出起算已过的 Ghati 数（即刻上升数）"}, {"fact_key": "该刻上升中已过的度分"}, {"fact_key": "本盘日出时刻太阳（Surya）的黄经是多少度"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文要求用日出时的太阳黄经，不得换成出生时刻的太阳黄经。", "不得据这一偈直接下吉凶断语——本偈只给起法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：自日出起算已过的 Ghati 数（即刻上升数）、该刻上升中已过的度分、本盘日出时刻太阳（Surya）的黄经是多少度。
- 缺失即停字段：["自日出起算已过的 Ghati 数（即刻上升数）", "该刻上升中已过的度分", "本盘日出时刻太阳（Surya）的黄经是多少度"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v6-8`｜PDF [16]｜“The product so arrived in Rāśis, degrees and minutes be added to Surya’s longitude, as at sunrise, to get the exact location of Ghati Lagn.”


## 四路查书计划

### 支持路

- Ghati Lagn (Ghatik Lagn). Now listen to the method of working out Ghati Lagn. This Lagn changes along with every Ghati (24 minutes) from the sunrise
- The Vighatis be divided by 2 to arrive at degrees and minutes of arc, past in the said Ghati Lagn
- 刻上升 Ghati Lagn 起法 Vighatis 除以 2

### 反例或取消路

- From sunrise to the time of birth every 5 Ghatis constitute one Bhava Lagn
- Hora Lagn repeats itself every 2½ Ghatis divide by 2½
- 特殊上升 起法差别 Bhava Hora Ghati 除数

### 适用边界路

- So say Maharishis, like Narada
- The natal Lagn is to be calculated according to birth place Bhava Lagna Hora Lagn common to all places
- Ghati Vighati 一日 六十 Ghati 换算

### 判断方法路

- Use of Special Lagnas prepare various Bhava Kundalis with respect to each special Lagn
- Now listen to the method of working out Ghati Lagn
- 刻上升 Ghati Lagn 起出来以后怎么用

## 上游问题

- 无

## 停止条件

- 缺少本盘从日出到出生的 Ghati 数时停止。
- 缺少本盘从日出到出生的 Vighati 数时停止。
- 缺少日出时刻太阳（Surya）黄经时停止。
- 日出时刻本身未定（出生地或出生钟点不明）时停止。
- 原文这一偈只给刻上升（Ghati Lagn）的起法、未给吉凶断法，要断吉凶须另查原文，本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
