---
method: ch05-v9-use-of-special-lagnas
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 特殊上升的用法：行星位置不动，逐个特殊上升起宫盘，照本命上升的办法分析

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 特殊上升起出来以后怎么用
- Bhava Lagn、Hora Lagn 这些盘怎么看
- 特殊上升要不要重新排行星

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘出生时各行星（Grahas）的黄经分别是多少度
- 本盘各特殊上升（special Lagn）的黄经分别是多少度

## 按情况检查的事实

- 无

## 依赖方法

- ch05-v2-3-bhava-lagn
- ch05-v4-5-hora-lagn
- ch05-v6-8-ghati-lagn

## 执行步骤

### ch05-v9-use-of-special-lagnas.step-001

- 动作：保持出生时诸行星（Grahas）的位置不动，就每一个特殊上升（special Lagn）分别起出各自的宫盘（Bhava Kundali）。
- 适用范围：「每一个特殊上升」承接本章前文所讲的诸特殊上升，本偈没有列出名单，不得把它封闭成固定几个；原文也没有给宫盘（Bhava Kundali）的起宫方式。
- 原文最小意思：保持出生时诸行星（Grahas）的位置不动，就每一个特殊上升（special Lagn）分别起出宫盘（Bhava Kundalis）。
- 本步骤产出事实：["各特殊上升的宫盘（Bhava Kundali）"]
- 所需事实：["本盘出生时各行星（Grahas）的黄经分别是多少度", "本盘各特殊上升（special Lagn）的黄经分别是多少度"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘出生时各行星（Grahas）的黄经分别是多少度"}, {"fact_key": "本盘各特殊上升（special Lagn）的黄经分别是多少度"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得在起特殊上升宫盘时改动出生时的行星位置。", "原文没有列出特殊上升的名单，名单未确定即停判，不得自行封闭成固定几个。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生时各行星（Grahas）的黄经分别是多少度、本盘各特殊上升（special Lagn）的黄经分别是多少度。
- 缺失即停字段：["本盘出生时各行星（Grahas）的黄经分别是多少度", "本盘各特殊上升（special Lagn）的黄经分别是多少度"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v9`｜PDF [16]｜“Keeping the Grahas at birth, as it is, prepare various Bhava Kundalis with respect to each special Lagn and analyze, as done for the natal Lagn.”
  - `bphs-97:santhanam:ch05:v2-3`｜PDF [16]｜“This is called Bhava Lagn.”

### ch05-v9-use-of-special-lagnas.step-002

- 动作：对各特殊上升所起的宫盘，按分析本命上升（natal Lagn）的同样办法去分析。
- 适用范围：原文只说照分析本命上升的办法分析，没有给分析细则；细则须另查本书讲各宫、各星的原文。
- 原文最小意思：各特殊上升所起的宫盘，按分析本命上升（natal Lagn）的同样办法分析。
- 本步骤产出事实：["各特殊上升宫盘的分析结论"]
- 所需事实：["各特殊上升的宫盘（Bhava Kundali）"]
- 条件关系：{"fact_key": "各特殊上升的宫盘（Bhava Kundali）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文没有给特殊上升宫盘的具体断法，断法未确定即停判，不得自造一套。", "不得把特殊上升的宫盘拿去替换本命上升盘的判断结论。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：各特殊上升的宫盘（Bhava Kundali）。
- 缺失即停字段：["各特殊上升的宫盘（Bhava Kundali）"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v9`｜PDF [16]｜“prepare various Bhava Kundalis with respect to each special Lagn and analyze, as done for the natal Lagn.”


## 四路查书计划

### 支持路

- Use of Special Lagnas Keeping the Grahas at birth prepare various Bhava Kundalis
- prepare various Bhava Kundalis with respect to each special Lagn and analyze, as done for the natal Lagn
- 特殊上升 宫盘 照本命上升分析

### 反例或取消路

- These Varnad Dashas are only for Bhavas Rāśis and not their occupants
- The natal Lagn is to be calculated according to birth place
- 本命上升 与 特殊上升 判断范围不同

### 适用边界路

- I explain below again some special Lagnas viz. Bhava Lagna Hora Lagn and Ghati Lagn
- Bhava Madhya cusp Bhava Kundali 起宫 方式
- special Lagnas 适用范围 出生地 共通

### 判断方法路

- analyze, as done for the natal Lagn
- Effects of Varnad. Now listen to the use of the above
- 怎么分析本命上升盘 各宫 各星

## 上游问题

- 无

## 停止条件

- 缺少出生时诸行星位置时停止。
- 各特殊上升的位置未算出时停止（须先按本章前文的起法算出）。
- 原文没有给特殊上升宫盘的具体断法，断法未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
