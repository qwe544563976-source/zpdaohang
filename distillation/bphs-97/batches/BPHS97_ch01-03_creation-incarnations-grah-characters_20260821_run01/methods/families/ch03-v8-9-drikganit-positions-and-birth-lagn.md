---
method: ch03-v8-9-drikganit-positions-and-birth-lagn
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 起盘取用：行星位置依 Drikganit，出生上升（Lagn）依各地星座升起时长

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 行星位置该按什么方法取
- 出生时的上升（Lagn）怎么定出来

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘行星位置是否依 Drikganit 取得
- 本盘出生地适用的星座升起时长（Rashi durations）是多少

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v8-9-drikganit-positions-and-birth-lagn.step-001

- 动作：核对本盘给定时刻的行星位置是否依 Drikganit 取得。
- 适用范围：第3章起盘取用的规定；原文只写 Drikganit，未指明具体星历表、历元或岁差取值。
- 原文最小意思：给定时刻的行星位置应依 Drikganit 取得。
- 本步骤产出事实：["行星位置取用依据判定"]
- 所需事实：["本盘行星位置是否依 Drikganit 取得"]
- 条件关系：{"fact_key": "本盘行星位置是否依 Drikganit 取得"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条指定某一部具体星历表或某一种岁差数值——原文只写 Drikganit。", "不得据本条推出行星位置之外的其他取用规定。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘行星位置是否依 Drikganit 取得。
- 缺失即停字段：["本盘行星位置是否依 Drikganit 取得"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v8-9`｜PDF [9]｜“The positions of the Grahas for a given time be taken, as per Drikganit.”

### ch03-v8-9-drikganit-positions-and-birth-lagn.step-002

- 动作：以各地适用的星座升起时长（Rashi durations）求出生时的上升（Lagn）。
- 适用范围：第3章求出生上升（Lagn）的规定；原文只说依各地适用的星座升起时长，未给具体时长表，也未指定宫位制。
- 原文最小意思：应依各地适用的星座升起时长，求出生时的上升（Lagn）。
- 本步骤产出事实：["出生时上升（Lagn）取得判定"]
- 所需事实：["本盘出生地适用的星座升起时长（Rashi durations）是多少"]
- 条件关系：{"fact_key": "本盘出生地适用的星座升起时长（Rashi durations）是多少"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条选定某一套具体的星座升起时长表——原文没有给表值。", "不得把本条读成 Bhava Lagn、Hora Lagn 等其他上升的求法，原文此处求的是出生时的上升（Lagn）。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生地适用的星座升起时长（Rashi durations）是多少。
- 缺失即停字段：["本盘出生地适用的星座升起时长（Rashi durations）是多少"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v8-9`｜PDF [9]｜“And with the help of Rashidurations, applicable to the respective places, Lagn at birth should be known.”


## 四路查书计划

### 支持路

- The positions of the Grahas for a given time be taken, as per Drikganit
- with the help of Rashidurations, applicable to the respective places, Lagn at birth should be known

### 反例或取消路

- Bhava Lagn From sunrise to the time of birth every 5 Ghatis constitute one Bhava Lagn
- Hora Lagn Ghati Lagn 另一种上升的取法

### 适用边界路

- Lagn is a very important point in the horoscope It is the Rāśi, that rises in the East, on the latitude of birth
- two hours are required for a Rashito pass via the horizon every degree taking four minutes to ascend dependent on the concerned latitude

### 判断方法路

- Gulik’s Position The degree, ascending at the time of start of Gulik’s portion
- The Rashirising is known as Lagn Based on Lagn and the Grahas 起盘之后怎么用

## 上游问题

- 无

## 停止条件

- 缺少「本盘行星位置是否依 Drikganit 取得」时停止。
- 缺少出生地适用的星座升起时长（Rashi durations）时停止。
- 原文未给具体的升起时长表与星历表，取值来源不确定即停判，不得自行选定。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
