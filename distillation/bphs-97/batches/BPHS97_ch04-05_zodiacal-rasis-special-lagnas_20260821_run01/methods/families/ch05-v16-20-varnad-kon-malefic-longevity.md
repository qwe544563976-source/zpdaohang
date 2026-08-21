---
method: ch05-v16-20-varnad-kon-malefic-longevity
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升 Varnad 的三角宫被凶星占据或相照：命主只活到该星座的大运

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我大概能活到什么时候
- 哪一步大运对我最危险
- Varnad 怎么看寿命

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座
- 本盘中哪些行星被判为凶星

## 按情况检查的事实

- 自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星占据
- 自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星相照

## 依赖方法

- ch05-v10-13-5-varnad-for-lagn
- ch05-v14-15-varnad-start-direction-years

## 执行步骤

### ch05-v16-20-varnad-kon-malefic-longevity.step-001

- 动作：查自上升的 Varnad 起算的三角宫（Kon）有没有被凶星占据、或被凶星相照；若有，命主只活到该星座的大运为止。
- 适用范围：本偈承接前两偈算出的上升 Varnad 与 Varnad 大运；原文以命主本人的寿命立说，没有给「只活到」的具体年龄换算。
- 原文最小意思：自上升的 Varnad（Lagn’s Varnad）起算的三角宫（Kon）被凶星（malefic）占据，或被凶星相照时，命主只活到该星座（Rāśi）的大运（Dasha）为止。
- 本步骤产出事实：["与 Varnad 三角宫（Kon）相关的凶星名单", "命主只活到该星座大运的判定"]
- 所需事实：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "本盘中哪些行星被判为凶星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}, {"fact_key": "本盘中哪些行星被判为凶星"}]}, {"operator": "OR", "operands": [{"fact_key": "自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星占据"}, {"fact_key": "自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星相照"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}, {"fact_key": "本盘中哪些行星被判为凶星"}]}, "required_fact_keys": ["自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星占据"], "branch_condition_logic": {"fact_key": "自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星占据"}, "selection_group": "ch05-v16-20-varnad-kon-malefic-longevity.step-001:kon-malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}, {"fact_key": "本盘中哪些行星被判为凶星"}]}, "required_fact_keys": ["自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星相照"], "branch_condition_logic": {"fact_key": "自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星相照"}, "selection_group": "ch05-v16-20-varnad-kon-malefic-longevity.step-001:kon-malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只说命主活到该星座的大运为止，不得据此推出具体年龄、日期或死因。", "不得把三角宫（Kon）改读成原文没写的其他宫位关系。", "本偈没有界定谁是凶星，凶星名册须另查本书吉凶星原文，未确定即停判。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座、本盘中哪些行星被判为凶星。
- 缺失即停字段：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "本盘中哪些行星被判为凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v16-20`｜PDF [17]｜“Should a Kon from Lagn’s Varnad be occupied, or drishtied by a malefic, the native will live only up to the Dasha of the said Rāśi.”

### ch05-v16-20-varnad-kon-malefic-longevity.step-002

- 动作：把与 Varnad 三角宫（Kon）有关的上述行星，比照 Sool 大运中能致凶的 Rudra Grah 来看待。
- 适用范围：「上述行星」指同一条原文前句中占据或相照该三角宫的凶星；原文在此把它们比照 Sool 大运（Sool Dasha）的 Rudra Grah，但本偈没有给 Rudra Grah 与 Sool 大运的取法，须另查本书讲 Sool Dasha 的原文。
- 原文最小意思：与 Varnad 三角宫（Kon）有关的上述行星（Grahas），应比照 Sool 大运（Sool Dasha）中能致凶的 Rudra Grah 来看待。
- 本步骤产出事实：["Varnad 三角宫相关行星比照 Rudra Grah 的看法"]
- 所需事实：["本盘中哪些行星被判为凶星", "与 Varnad 三角宫（Kon）相关的凶星名单"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "与 Varnad 三角宫（Kon）相关的凶星名单"}]}, {"operator": "OR", "operands": [{"fact_key": "自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星占据"}, {"fact_key": "自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星相照"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "与 Varnad 三角宫（Kon）相关的凶星名单"}]}, "required_fact_keys": ["自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星占据"], "branch_condition_logic": {"fact_key": "自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星占据"}, "selection_group": "ch05-v16-20-varnad-kon-malefic-longevity.step-002:kon-malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "与 Varnad 三角宫（Kon）相关的凶星名单"}]}, "required_fact_keys": ["自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星相照"], "branch_condition_logic": {"fact_key": "自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星相照"}, "selection_group": "ch05-v16-20-varnad-kon-malefic-longevity.step-002:kon-malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：自本盘上升的 Varnad 起算的三角宫（Kon）是否被凶星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只说比照 Rudra Grah 看待，没有给 Rudra Grah 的取法，取法未确定即停判。", "不得把这条比照扩大到与 Varnad 三角宫无关的行星上。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星、与 Varnad 三角宫（Kon）相关的凶星名单。
- 缺失即停字段：["本盘中哪些行星被判为凶星", "与 Varnad 三角宫（Kon）相关的凶星名单"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v16-20`｜PDF [17]｜“Just, as the Rudra Grah in Sool Dasha is capable of causing evils, the above-mentioned Grahas related to Varnad’s Kon be treated.”


## 四路查书计划

### 支持路

- Should a Kon from Lagn’s Varnad be occupied or drishtied by a malefic live only up to the Dasha
- Rudra Grah in Sool Dasha capable of causing evils Grahas related to Varnad’s Kon
- Varnad 三角宫 凶星 占据 相照 寿命

### 反例或取消路

- These Varnad Dashas are only for Bhavas Rāśis and not their occupants
- I have narrated 3 different methods of longevity. Listen to me about the choice among the three systems
- Sool Dasha Rudra Grah 取法 与 例外

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- drishti aspects of the Grahas Kon trine 三角宫 相照 规则
- The Dasha of the Sool Rashi will inflict greater evils

### 判断方法路

- The Varnad Lagn be considered, as natal Lagna, while the 7<sup>th</sup> from Varnad will denote the longevity of the spouse
- just by knowing which one can deal with the longevity of a native
- 怎么判断哪一颗是凶星

## 上游问题

- 无

## 停止条件

- 缺少上升的 Varnad 星座时停止。
- 凶星名册未定时停止——本偈没有界定谁是凶星。
- 三角宫（Kon）的占据与相照事实缺一时，对应分支停判。
- 原文没有给 Rudra Grah 与 Sool 大运的取法，取法未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
