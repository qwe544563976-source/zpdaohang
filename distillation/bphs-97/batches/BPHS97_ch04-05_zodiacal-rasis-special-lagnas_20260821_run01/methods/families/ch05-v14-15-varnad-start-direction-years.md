---
method: ch05-v14-15-varnad-start-direction-years
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Varnad 大运的起算处、顺逆方向与上升大运年数

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Varnad 大运从哪里起
- Varnad 大运往哪个方向数
- 上升大运有多少年

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升（Lagn）与时上升（Hora Lagn）两者中哪一个更有力
- 本盘上升（Lagn）落在哪个星座
- 本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座
- 本盘上升（Lagn）与其 Varnad 之间相隔几个星座

## 按情况检查的事实

- 本盘上升（Lagn）是否比时上升（Hora Lagn）更有力
- 本盘时上升（Hora Lagn）是否比本盘上升（Lagn）更有力
- 本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）
- 本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）

## 依赖方法

- ch05-v10-13-5-varnad-for-lagn
- ch05-v4-5-hora-lagn

## 执行步骤

### ch05-v14-15-varnad-start-direction-years.step-001

- 动作：在本命上升（natal Lagn）与时上升（Hora Lagna）二者中取较有力者，Varnad 自该处起算。
- 适用范围：原文只说「whichever is stronger」，本偈没有给强弱的判准；判准未确定即停判，须另查本书讲力量（Shad Bal）的原文。本步承接前偈算出的 Varnad。
- 原文最小意思：本命上升（natal Lagn）与时上升（Hora Lagna）二者之中，较有力的那一个，Varnad 自该处起算。
- 本步骤产出事实：["Varnad 大运的起算处"]
- 所需事实：["本盘上升（Lagn）与时上升（Hora Lagn）两者中哪一个更有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）与时上升（Hora Lagn）两者中哪一个更有力"}, {"operator": "OR", "operands": [{"fact_key": "本盘上升（Lagn）是否比时上升（Hora Lagn）更有力"}, {"fact_key": "本盘时上升（Hora Lagn）是否比本盘上升（Lagn）更有力"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升（Lagn）与时上升（Hora Lagn）两者中哪一个更有力"}, "required_fact_keys": ["本盘上升（Lagn）是否比时上升（Hora Lagn）更有力"], "branch_condition_logic": {"fact_key": "本盘上升（Lagn）是否比时上升（Hora Lagn）更有力"}, "selection_group": "ch05-v14-15-varnad-start-direction-years.step-001:stronger-of-the-two", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）是否比时上升（Hora Lagn）更有力。"}, {"when": {"fact_key": "本盘上升（Lagn）与时上升（Hora Lagn）两者中哪一个更有力"}, "required_fact_keys": ["本盘时上升（Hora Lagn）是否比本盘上升（Lagn）更有力"], "branch_condition_logic": {"fact_key": "本盘时上升（Hora Lagn）是否比本盘上升（Lagn）更有力"}, "selection_group": "ch05-v14-15-varnad-start-direction-years.step-001:stronger-of-the-two", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘时上升（Hora Lagn）是否比本盘上升（Lagn）更有力。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文没有给本命上升与时上升的强弱判准，判准未确定即停判，不得自定一套强弱算法。", "不得把「较有力者」固定读成其中某一个。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagn）与时上升（Hora Lagn）两者中哪一个更有力。
- 缺失即停字段：["本盘上升（Lagn）与时上升（Hora Lagn）两者中哪一个更有力"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v14-15`｜PDF [16]｜“Now listen to the use of the above. Out of the two, viz. natal Lagn and Hora Lagna, whichever is stronger, from there Varnad starts.”

### ch05-v14-15-varnad-start-direction-years.step-002

- 动作：看本命上升是否落奇数星座：是则大运（Dashas）顺时针数，否则逆时针数。
- 适用范围：仅限 Varnad 大运的排列方向；原文以本命上升的奇偶立说，没有说时上升的奇偶在此起作用。
- 原文最小意思：本命上升（natal Lagn）是奇数星座（odd Rāśi）时，大运（Dashas）的计数是顺时针；否则是逆时针。
- 本步骤产出事实：["Varnad 大运的计数方向"]
- 所需事实：["本盘上升（Lagn）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）落在哪个星座"}, {"operator": "OR", "operands": [{"fact_key": "本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）"}, {"fact_key": "本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升（Lagn）落在哪个星座"}, "required_fact_keys": ["本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）"], "branch_condition_logic": {"fact_key": "本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）"}, "selection_group": "ch05-v14-15-varnad-start-direction-years.step-002:dasha-counting-direction", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）。"}, {"when": {"fact_key": "本盘上升（Lagn）落在哪个星座"}, "required_fact_keys": ["本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）"], "branch_condition_logic": {"fact_key": "本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）"}, "selection_group": "ch05-v14-15-varnad-start-direction-years.step-002:dasha-counting-direction", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把顺时针、逆时针对调。", "不得把奇偶的判断对象从本命上升换成原文没写的其他点。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagn）落在哪个星座。
- 缺失即停字段：["本盘上升（Lagn）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v14-15`｜PDF [16]｜“If the natal Lagn is an odd Rāśi, the counting of Dashas is clockwise, otherwise anticlockwise.”

### ch05-v14-15-varnad-start-direction-years.step-003

- 动作：数出本命上升与 Varnad 之间相隔的星座数，那就是上升大运（Lagn Dasha）的年数；其余各宫照此办理。
- 适用范围：原文只给年数的算法，没有给大运的起讫日期换算；「其余各宫同理」是原文自己写的推广，不再另加条件。
- 原文最小意思：上升大运（Lagn Dasha）的年数，等于本命上升（natal Lagn）与 Varnad 之间相隔的星座（Rāśis）数；其余各宫（Bhavas）同理。
- 本步骤产出事实：["上升大运（Lagn Dasha）的年数"]
- 所需事实：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "本盘上升（Lagn）与其 Varnad 之间相隔几个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}, {"fact_key": "本盘上升（Lagn）与其 Varnad 之间相隔几个星座"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只给年数，不得据此推出大运的具体起讫年月。", "不得把相隔星座数换成原文没写的其他计数方式。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座、本盘上升（Lagn）与其 Varnad 之间相隔几个星座。
- 缺失即停字段：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "本盘上升（Lagn）与其 Varnad 之间相隔几个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v14-15`｜PDF [16]｜“Lagn Dasha years will equal the number of Rāśis, intervening between the natal Lagn and Varnad. Similarly for other Bhavas.”


## 四路查书计划

### 支持路

- Out of the two natal Lagn and Hora Lagna whichever is stronger from there Varnad starts
- Lagn Dasha years will equal the number of Rāśis intervening between the natal Lagn and Varnad
- Varnad 大运 年数 顺时针 逆时针

### 反例或取消路

- These Varnad Dashas are only for Bhavas Rāśis and not their occupants
- The sub period of each Dasha will be one twelfth of the Dasha
- Sool Dasha Rudra Grah 寿命 另一套大运

### 适用边界路

- Shad Bal consists of the following Sthan Bal positional Dig Bal directional Kaal Bal Temporal
- Similar assessments be made with reference to the Varnad of each Bhava commencing the first
- The natal Lagn is to be calculated according to birth place

### 判断方法路

- I now detail Varnad Dasha If the natal Lagn is an odd Rāśi count directly from Mesh
- Now listen to the use of the above
- Varnad 大运 排出来以后怎么断

## 上游问题

- 无

## 停止条件

- 原文未给本命上升与时上升的强弱判准，判准未确定即停判（须另查 Shad Bal 一类原文）。
- 本命上升所在星座的奇偶未定时，大运方向停判。
- 缺少上升的 Varnad 星座时停止。
- 缺少本命上升与 Varnad 之间相隔星座数时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
