---
method: ch03-v71-74-pranapad-calculation
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Pranapad 的推算：由 Vighatis 除 15 再按太阳所落星座类别加度

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Pranapad 怎么算
- 我盘里的 Pranapad 落在哪里

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘出生时刻换算成 Vighatis 是多少
- 本盘太阳（Surya）所落星座属于动、固定、双体中的哪一类

## 按情况检查的事实

- 太阳（Surya）所落星座是否为动星座（Movable Rāśi）
- 太阳（Surya）所落星座是否为固定星座（Fixed Rāśi）
- 太阳（Surya）所落星座是否为双体星座（Dual Rāśi）

## 依赖方法

- 无

## 执行步骤

### ch03-v71-74-pranapad-calculation.step-001

- 动作：把出生时刻化为 Vighatis 后除以 15，得到用于推算的星座与度数。
- 适用范围：第3章 Pranapad 推算条；本原子后附 Santhanam 译注，本方法只据偈文正文。
- 原文最小意思：把给定时刻化为 Vighatis，再除以 15。
- 本步骤产出事实：["Pranapad 推算的基础商数判定"]
- 所需事实：["本盘出生时刻换算成 Vighatis 是多少"]
- 条件关系：{"fact_key": "本盘出生时刻换算成 Vighatis 是多少"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本步直接得出 Pranapad——还要按太阳所落星座类别加度。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生时刻换算成 Vighatis 是多少。
- 缺失即停字段：["本盘出生时刻换算成 Vighatis 是多少"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v71-74`｜PDF [13, 14]｜“Convert the given time into Vighatis and divide the same by 15.”

### ch03-v71-74-pranapad-calculation.step-002

- 动作：按太阳所落星座属动、固定还是双体，把所得加到太阳上并另加相应度数，得 Pranapad。
- 适用范围：第3章 Pranapad 推算条；本原子后附 Santhanam 译注，本方法只据偈文正文。
- 原文最小意思：所得的星座与度数（degrees）：若太阳（Surya）落在动星座（Movable Rāśi）就加到太阳上；若太阳落在固定星座（Fixed Rāśi），另加 240 度；若落在双体星座（Dual Rāśi），再加 120 度，得到 Pranapad。
- 本步骤产出事实：["Pranapad 位置判定"]
- 所需事实：["本盘太阳（Surya）所落星座属于动、固定、双体中的哪一类", "Pranapad 推算的基础商数判定"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）所落星座属于动、固定、双体中的哪一类"}, {"fact_key": "Pranapad 推算的基础商数判定"}]}, {"operator": "OR", "operands": [{"fact_key": "太阳（Surya）所落星座是否为动星座（Movable Rāśi）"}, {"fact_key": "太阳（Surya）所落星座是否为固定星座（Fixed Rāśi）"}, {"fact_key": "太阳（Surya）所落星座是否为双体星座（Dual Rāśi）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）所落星座属于动、固定、双体中的哪一类"}, {"fact_key": "Pranapad 推算的基础商数判定"}]}, "required_fact_keys": ["太阳（Surya）所落星座是否为动星座（Movable Rāśi）"], "branch_condition_logic": {"fact_key": "太阳（Surya）所落星座是否为动星座（Movable Rāśi）"}, "selection_group": "ch03-v71-74-pranapad-calculation.step-002:surya-rasi-type", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）所落星座是否为动星座（Movable Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）所落星座属于动、固定、双体中的哪一类"}, {"fact_key": "Pranapad 推算的基础商数判定"}]}, "required_fact_keys": ["太阳（Surya）所落星座是否为固定星座（Fixed Rāśi）"], "branch_condition_logic": {"fact_key": "太阳（Surya）所落星座是否为固定星座（Fixed Rāśi）"}, "selection_group": "ch03-v71-74-pranapad-calculation.step-002:surya-rasi-type", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）所落星座是否为固定星座（Fixed Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）所落星座属于动、固定、双体中的哪一类"}, {"fact_key": "Pranapad 推算的基础商数判定"}]}, "required_fact_keys": ["太阳（Surya）所落星座是否为双体星座（Dual Rāśi）"], "branch_condition_logic": {"fact_key": "太阳（Surya）所落星座是否为双体星座（Dual Rāśi）"}, "selection_group": "ch03-v71-74-pranapad-calculation.step-002:surya-rasi-type", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）所落星座是否为双体星座（Dual Rāśi）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 240 度与 120 度对调——原文分别系于固定星座与双体星座。", "不得据本步推出 Pranapad 的吉凶——那由下一句另断。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘太阳（Surya）所落星座属于动、固定、双体中的哪一类、Pranapad 推算的基础商数判定。
- 缺失即停字段：["本盘太阳（Surya）所落星座属于动、固定、双体中的哪一类", "Pranapad 推算的基础商数判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v71-74`｜PDF [13, 14]｜“The resultant Rāśi, degrees etc. be added to Surya, if he is in a Movable Rāśi, which will yield Pranapad. If Surya is in a Fixed Rāśi, add 240 degrees additionally and, if in a Dual Rāśi, add 120 degrees in furtherance to get Pranapad.”


## 四路查书计划

### 支持路

- Convert the given time into Vighatis and divide the same by 15
- The resultant Rāśi, degrees etc. be added to Surya, if he is in a Movable Rāśi, which will yield Pranapad
- Pranapad 推算 Vighatis 除以 15

### 反例或取消路

- 无

### 适用边界路

- Starting from Mesh for a Movable Rāśi, from Simh for a Fixed Rashiand from Dhanu for a Dual Rāśi
- 动 固定 双体三类星座在别处的用法

### 判断方法路

- The birth will be auspicious, if Pranapad falls in the 2<sup>nd</sup> , 5<sup>th</sup> , 9<sup>th</sup> , 4<sup>th</sup> , 10<sup>th</sup> , or 11<sup>th</sup> from the natal Lagn
- Effects of Pranapad’s Position with reference to Lagn and in Various Bhavas (up to Sloka 85)
- 算出 Pranapad 之后怎么断

## 上游问题

- 无

## 停止条件

- 缺少出生时刻的 Vighatis 换算时停止。
- 缺少太阳所落星座类别时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
