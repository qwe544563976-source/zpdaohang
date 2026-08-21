---
method: ch20-v4-indigent-father
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲贫穷：九宫主落陷、九宫起的二宫或四宫被火星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲会不会经济困难
- 九宫主落陷对父亲有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否落陷

## 按情况检查的事实

- 从九宫（Dharm）起算的第二宫是否被火星（Mangal）占据
- 从九宫（Dharm）起算的第四宫是否被火星（Mangal）占据

## 依赖方法

- 无

## 执行步骤

### ch20-v4-indigent-father.step-001

- 动作：核对九宫主（Dharm's Lord）是否落陷，再核对从九宫起算的第二宫或第四宫是否被火星（Mangal）占据。
- 适用范围：仅限本命盘九宫（Dharm Bhava）主题下父亲的贫富；原文的二宫、四宫都从九宫起算；原文未给时间限定。
- 原文最小意思：九宫主落陷、而从九宫起算的第二宫或第四宫被火星占据时，命主的父亲贫穷。
- 本步骤产出事实：["九宫主落陷火星临九宫二四的父亲贫穷判定"]
- 所需事实：["九宫主（Dharm's Lord）是否落陷"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落陷"}, {"operator": "OR", "operands": [{"fact_key": "从九宫（Dharm）起算的第二宫是否被火星（Mangal）占据"}, {"fact_key": "从九宫（Dharm）起算的第四宫是否被火星（Mangal）占据"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "九宫主（Dharm's Lord）是否落陷"}, "required_fact_keys": ["从九宫（Dharm）起算的第二宫是否被火星（Mangal）占据"], "branch_condition_logic": {"fact_key": "从九宫（Dharm）起算的第二宫是否被火星（Mangal）占据"}, "selection_group": "ch20-v4-indigent-father.step-001:mangal-from-dharm", "stop_condition": "选中该分支后，缺少以下事实即停止：从九宫（Dharm）起算的第二宫是否被火星（Mangal）占据。"}, {"when": {"fact_key": "九宫主（Dharm's Lord）是否落陷"}, "required_fact_keys": ["从九宫（Dharm）起算的第四宫是否被火星（Mangal）占据"], "branch_condition_logic": {"fact_key": "从九宫（Dharm）起算的第四宫是否被火星（Mangal）占据"}, "selection_group": "ch20-v4-indigent-father.step-001:mangal-from-dharm", "stop_condition": "选中该分支后，缺少以下事实即停止：从九宫（Dharm）起算的第四宫是否被火星（Mangal）占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把二宫、四宫改从上升宫起算——原文写明从九宫起。", "不得据此推断父亲贫穷的时间或程度。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否落陷。
- 缺失即停字段：["九宫主（Dharm's Lord）是否落陷"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v4`｜PDF [36]｜“If Dharm’s Lord is debilitated, while the 2<sup>nd</sup> and/or the 4<sup>th</sup> from Dharm Bhava is occupied by Mangal, the native’s father is poor.”


## 四路查书计划

### 支持路

- If Dharm’s Lord is debilitated, while the 2nd and/or the 4th from Dharm Bhava is occupied by Mangal, the native’s father is poor
- 九宫主落陷 火星占九宫起二宫四宫 父亲贫穷

### 反例或取消路

- If Dharm’s Lord is with strength, as Shukra is in Dharm, while Guru is in an angle from Tanu Bhava, the native’s father is fortunate
- Should Dharm’s Lord be in Karm Bhava, while Karm’s Lord receives a Drishti from a benefic the native’s father will be very rich and famous

### 适用边界路

- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines
- Combinations for Father’s Death

### 判断方法路

- these are the effects related to Dharm Bhava. I have explained briefly. These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava
- Effects of Dharm’s Lord in Various Bhavas
- 从九宫起算的宫位怎么数

## 上游问题

- 无

## 停止条件

- 缺少九宫主落陷事实时停止。
- 九宫起第二宫、第四宫两个火星分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
