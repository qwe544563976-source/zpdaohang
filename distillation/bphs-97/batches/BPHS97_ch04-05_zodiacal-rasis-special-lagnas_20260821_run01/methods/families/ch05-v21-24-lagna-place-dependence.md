---
method: ch05-v21-24-lagna-place-dependence
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 本命上升按出生地推算，宫上升、时上升等对一切地点相同

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 特殊上升要不要按出生地校正
- 换个地方出生 Bhava Lagn 会不会变
- 本命上升和特殊上升算法上差在哪

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的出生地点是哪里
- 本盘各特殊上升（special Lagn）的黄经分别是多少度

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch05-v21-24-lagna-place-dependence.step-001

- 动作：推算本命上升（natal Lagn）时按出生地来算。
- 适用范围：原文只说本命上升要按出生地推算，没有给推算所需的地理量或算式。
- 原文最小意思：本命上升（natal Lagn）要按出生地推算。
- 本步骤产出事实：["本命上升须按出生地推算的要求"]
- 所需事实：["本盘的出生地点是哪里"]
- 条件关系：{"fact_key": "本盘的出生地点是哪里"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文没有给按出生地推算本命上升的算式，算式未确定即停判。", "不得把这条要求推及原文说与地点无关的那些上升点。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的出生地点是哪里。
- 缺失即停字段：["本盘的出生地点是哪里"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v21-24`｜PDF [17]｜“The natal Lagn is to be calculated according to birth place”

### ch05-v21-24-lagna-place-dependence.step-002

- 动作：宫上升（Bhava Lagna）、时上升（Hora Lagn）等则不随出生地而变，对一切地点相同。
- 适用范围：原文举的是宫上升、时上升「等」，用了 etc. 没有把名单封闭；名单之外的上升点是否同理，原文未说。
- 原文最小意思：宫上升（Bhava Lagna）、时上升（Hora Lagn）等对一切地点相同。
- 本步骤产出事实：["特殊上升不随出生地而变的判定"]
- 所需事实：["本盘各特殊上升（special Lagn）的黄经分别是多少度"]
- 条件关系：{"fact_key": "本盘各特殊上升（special Lagn）的黄经分别是多少度"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文用 etc. 没有把名单封闭，不得据此断定某个原文没提到的上升点也与地点无关。", "不得据此推翻本章前文以日出为起点的起法——原文只说这些上升点对一切地点相同，没有改动起法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘各特殊上升（special Lagn）的黄经分别是多少度。
- 缺失即停字段：["本盘各特殊上升（special Lagn）的黄经分别是多少度"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v21-24`｜PDF [17]｜“while Bhava Lagna, Hora Lagn etc. are common to all places”


## 四路查书计划

### 支持路

- The natal Lagn is to be calculated according to birth place while Bhava Lagna Hora Lagn etc. are common to all places
- 本命上升 出生地 特殊上升 共通

### 反例或取消路

- From sunrise to the time of birth every 5 Ghatis constitute one Bhava Lagn
- Hora Lagn repeats itself every 2½ Ghatis from sunrise Surya longitude
- 日出时刻 随地点 而变 起算

### 适用边界路

- Use of Special Lagnas prepare various Bhava Kundalis with respect to each special Lagn
- Varnad Dasha natal Lagn Hora Lagn 用到 出生地
- 本命上升 与 特殊上升 的适用地点差别

### 判断方法路

- Lagn is a very important point in the horoscope. It is the Rāśi, that rises in the East, on the latitude of birth
- I explain below again some special Lagnas viz. Bhava Lagna Hora Lagn and Ghati Lagn
- 特殊上升 与 本命上升 算法差别

## 上游问题

- 无

## 停止条件

- 缺少出生地点时，本命上升的推算停止。
- 原文没有给按出生地推算本命上升的算式，算式未确定即停判。
- 原文对 etc. 之外的上升点没有交代，是否与地点无关未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
