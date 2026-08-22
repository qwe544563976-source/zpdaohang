---
method: ch03-v70-gulik-longitude
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Gulik 的黄经：取其时段起始时刻的上升度数

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Gulik 的度数怎么定
- 断 Gulik 效应该用哪个位置

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘出生地 Gulik 之分起始时刻上升的度数是多少

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v70-gulik-longitude.step-001

- 动作：取上一偈算出的 Gulik 之分起始时刻，记下当时正在上升的度数，作为该地 Gulik 的黄经。
- 适用范围：第3章 Gulik 位置条；「如上」承上一偈的 Gulik 时段算法，且黄经因地而异。
- 原文最小意思：Gulik 之分起始时刻正在上升的那个度数（degree），就是该地 Gulik 的黄经。
- 本步骤产出事实：["Gulik 黄经判定"]
- 所需事实：["本盘出生地 Gulik 之分起始时刻上升的度数是多少"]
- 条件关系：{"fact_key": "本盘出生地 Gulik 之分起始时刻上升的度数是多少"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得改用 Gulik 时段的中点或终点——原文取的是起始时刻。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生地 Gulik 之分起始时刻上升的度数是多少。
- 缺失即停字段：["本盘出生地 Gulik 之分起始时刻上升的度数是多少"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v70`｜PDF [13]｜“The degree, ascending at the time of start of Gulik’s portion (as above), will be the longitude of Gulik at a given place.”

### ch03-v70-gulik-longitude.step-002

- 动作：断某一命盘的 Gulik 效应时，只依这个黄经。
- 适用范围：第3章 Gulik 位置条；本句限定了断 Gulik 效应的取位依据。
- 原文最小意思：只依这个黄经，来估断某一命盘中 Gulik 的效应。
- 本步骤产出事实：["Gulik 效应取位依据判定"]
- 所需事实：["Gulik 黄经判定"]
- 条件关系：{"fact_key": "Gulik 黄经判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得改用别的取法来断 Gulik 的效应——原文明说只依这个黄经。", "不得据本条推出 Gulik 落各宫的具体断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Gulik 黄经判定。
- 缺失即停字段：["Gulik 黄经判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v70`｜PDF [13]｜“Based on this longitude only, Gulik’s effects for a particular nativity be estimated.”


## 四路查书计划

### 支持路

- The degree, ascending at the time of start of Gulik’s portion (as above), will be the longitude of Gulik at a given place. Based on this longitude only, Gulik’s effects for a particular nativity be estimated
- Gulik 黄经 起始时刻 上升度数

### 反例或取消路

- 无

### 适用边界路

- Note the angular distance between Shani and Mandi (Gulik)
- 别处用 Gulik 的另一种用法

### 判断方法路

- Effects of Gulik in Various Bhavas (up to Sloka 73). If Gulik is in Tanu Bhava, the native will be afflicted by diseases
- 拿到 Gulik 黄经之后怎么断落宫效应

## 上游问题

- 无

## 停止条件

- 缺少 Gulik 之分起始时刻上升度数时停止。
- 上一偈的 Gulik 时段没算出来时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
