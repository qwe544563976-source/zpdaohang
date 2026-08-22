---
method: ch03-v4-6-lagn-graha-judgment-basis
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 吉凶推断的依据：上升（Lagn）与诸行星（Grahas）彼此的聚合与分离

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 命盘的吉凶到底是根据什么推出来的
- 看盘要先看哪些东西

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升（Lagn）落在哪个星座
- 本盘中每颗行星（Graha）分别落在哪一宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v4-6-lagn-graha-judgment-basis.step-001

- 动作：查本盘所升起的星座，定为上升（Lagn）。
- 适用范围：第3章对上升（Lagn）一词的界定；本条只给名称界定，未给任何吉凶结果，也未给求法。
- 原文最小意思：所升起的星座称为上升（Lagn）。
- 本步骤产出事实：["上升（Lagn）判定"]
- 所需事实：["本盘上升（Lagn）落在哪个星座"]
- 条件关系：{"fact_key": "本盘上升（Lagn）落在哪个星座"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出上升的求法、度数或宫位制——原文此处只给名称界定。", "不得把上升（Lagn）与一宫（Tanu Bhava）的效果断语混为一谈，本条没有给任何效果。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagn）落在哪个星座。
- 缺失即停字段：["本盘上升（Lagn）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v4-6`｜PDF [9]｜“The Rashirising is known, as ‘Lagn’.”

### ch03-v4-6-lagn-graha-judgment-basis.step-002

- 动作：以上升（Lagn）与诸行星（Grahas）彼此聚合、分离为据，推断命主的吉与凶。
- 适用范围：本命盘判断的总纲；原文只指明推断所依据的对象，未给任何具体条件、结果、时间限定，也未界定『聚合与分离』是何种关系。
- 原文最小意思：以上升（Lagn）与诸行星（Grahas）彼此聚合、分离为据，推断命主的吉与凶。
- 本步骤产出事实：["吉凶推断依据判定"]
- 所需事实：["上升（Lagn）判定", "本盘中每颗行星（Graha）分别落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升（Lagn）判定"}, {"fact_key": "本盘中每颗行星（Graha）分别落在哪一宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条下任何具体吉凶断语：原文只指明推断所依据的对象，没有给出任何条件→结果对。", "不得把『joining and departing from each other』坐实成某一种合相、离相或相位（Drishti）算法——原文未给界定。", "不得据本条断言吉凶只能从上升起算，原文此处没有排除别的起算点。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升（Lagn）判定、本盘中每颗行星（Graha）分别落在哪一宫。
- 缺失即停字段：["上升（Lagn）判定", "本盘中每颗行星（Graha）分别落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v4-6`｜PDF [9]｜“Based on Lagn and the Grahas, joining and departing from each other, the native’s good and bad effects are deducted.”


## 四路查书计划

### 支持路

- Based on Lagn and the Grahas, joining and departing from each other, the native’s good and bad effects are deducted
- The Rashirising is known as Lagn 上升 所升起的星座

### 反例或取消路

- Whatever results are to be known from Bandhu, Tanu, Dhan, Labh and Dharm should also be known from the 4th of Chandra
- Dharm Bhava and the 9th from Surya deal with one’s father 从太阳起算而非从上升起算

### 适用边界路

- After assessing the 20 point strength of the ascending degree, of other Bhavas and of the Grahas, the good and bad effects be declared
- Vimsopak strength 20 point strength 宣断吉凶之前先评强弱

### 判断方法路

- The positions of the Grahas for a given time be taken, as per Drikganit 起盘取行星位置
- Those are called Grahas, that move through the Nakshatraas in the zodiac 27 Nakshatraas 12 Rāśis 黄道结构

## 上游问题

- 无

## 停止条件

- 缺少本盘上升（Lagn）所在星座时停止。
- 缺少本盘各行星（Graha）落宫时停止。
- 『joining and departing from each other』（彼此聚合与分离）原文未界定为何种关系，未确定即停判，不得自行选定算法；取各行星落宫只是取得诸曜位置，不表示原文指的就是同宫关系。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
