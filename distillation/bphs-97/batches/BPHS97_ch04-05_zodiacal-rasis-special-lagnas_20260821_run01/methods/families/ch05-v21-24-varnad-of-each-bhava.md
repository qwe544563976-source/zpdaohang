---
method: ch05-v21-24-varnad-of-each-bhava
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 各宫 Varnad 的评断、只判宫不判居留行星、子期长度与顺逆

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 每一宫的 Varnad 怎么用
- Varnad 大运的子期有多长
- Varnad 大运判宫还是判行星

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘各宫（Bhava）的 Varnad 星座分别是哪个
- 本盘各 Varnad 大运的年数分别是多少
- 本盘上升（Lagn）落在哪个星座

## 按情况检查的事实

- 本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）
- 本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）

## 依赖方法

- ch05-v14-15-varnad-start-direction-years
- ch05-v16-20-varnad-kon-malefic-longevity

## 执行步骤

### ch05-v21-24-varnad-of-each-bhava.step-001

- 动作：自第一宫起，对每一宫的 Varnad 作同样的评断，由此得知这个命造的凶与吉。
- 适用范围：「同样的评断」承接本章前两偈对上升 Varnad 的做法，原文没有在此重述做法。
- 原文最小意思：自第一宫起，对每一宫（Bhava）的 Varnad 作同样的评断，由此得知一个命造的凶与吉。
- 本步骤产出事实：["各宫 Varnad 的评断结论"]
- 所需事实：["本盘各宫（Bhava）的 Varnad 星座分别是哪个"]
- 条件关系：{"fact_key": "本盘各宫（Bhava）的 Varnad 星座分别是哪个"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["「同样的评断」限于本章前文对上升 Varnad 已经写明的做法，不得扩大成原文没写的其他判法。", "原文只说由此得知命造的凶与吉，不得据此断具体事项或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘各宫（Bhava）的 Varnad 星座分别是哪个。
- 缺失即停字段：["本盘各宫（Bhava）的 Varnad 星座分别是哪个"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v21-24`｜PDF [17]｜“Similar assessments be made with reference to the Varnad of each Bhava, commencing the first, and the evils and goods due to a nativity be known.”

### ch05-v21-24-varnad-of-each-bhava.step-002

- 动作：记住这些 Varnad 大运只针对各宫（即星座），不针对宫中的居留行星。
- 适用范围：这是原文对 Varnad 大运适用对象的限定，与前一步的评断同时成立。
- 原文最小意思：这些 Varnad 大运只针对各宫（Bhavas，即星座 Rāśis），不针对宫中的居留行星。
- 本步骤产出事实：["Varnad 大运只判宫不判居留行星的限定"]
- 所需事实：["各宫 Varnad 的评断结论"]
- 条件关系：{"fact_key": "各宫 Varnad 的评断结论"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 Varnad 大运套到宫中的居留行星上。", "不得据此推断居留行星在 Varnad 里另有一套大运。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：各宫 Varnad 的评断结论。
- 缺失即停字段：["各宫 Varnad 的评断结论"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v21-24`｜PDF [17]｜“These Varnad Dashas are only for Bhavas (Rāśis) and not their occupants.”

### ch05-v21-24-varnad-of-each-bhava.step-003

- 动作：把每一个大运的十二分之一取作它的子期长度。
- 适用范围：原文只给子期占大运的比例，没有给子期在十二宫上的分配对象。
- 原文最小意思：每一个大运（Dasha）的子期，是该大运的十二分之一。
- 本步骤产出事实：["各 Varnad 大运子期的长度"]
- 所需事实：["本盘各 Varnad 大运的年数分别是多少"]
- 条件关系：{"fact_key": "本盘各 Varnad 大运的年数分别是多少"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只给十二分之一的比例，不得改成原文没写的其他比例。", "不得据此推出子期的具体起讫日期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘各 Varnad 大运的年数分别是多少。
- 缺失即停字段：["本盘各 Varnad 大运的年数分别是多少"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v21-24`｜PDF [17]｜“The sub period of each Dasha will be one twelfth of the Dasha”

### ch05-v21-24-varnad-of-each-bhava.step-004

- 动作：子期的排列次序照前面讲过的办法定：本命上升是奇数星座就顺时针，否则逆时针。
- 适用范围：「as explained earlier」明指前偈已讲过的顺逆判准，本步据该判准接线，不另加条件。
- 原文最小意思：子期的次序也同样是顺时针或逆时针，按前面讲过的办法定：本命上升（natal Lagn）是奇数星座（odd Rāśi）时顺时针，否则逆时针。
- 本步骤产出事实：["各 Varnad 大运子期的排列次序"]
- 所需事实：["各 Varnad 大运子期的长度", "本盘上升（Lagn）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "各 Varnad 大运子期的长度"}, {"fact_key": "本盘上升（Lagn）落在哪个星座"}]}, {"operator": "OR", "operands": [{"fact_key": "本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）"}, {"fact_key": "本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "各 Varnad 大运子期的长度"}, {"fact_key": "本盘上升（Lagn）落在哪个星座"}]}, "required_fact_keys": ["本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）"], "branch_condition_logic": {"fact_key": "本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）"}, "selection_group": "ch05-v21-24-varnad-of-each-bhava.step-004:sub-period-order", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "各 Varnad 大运子期的长度"}, {"fact_key": "本盘上升（Lagn）落在哪个星座"}]}, "required_fact_keys": ["本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）"], "branch_condition_logic": {"fact_key": "本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）"}, "selection_group": "ch05-v21-24-varnad-of-each-bhava.step-004:sub-period-order", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把顺时针、逆时针对调。", "原文说照前面讲过的办法定，不得另立一套顺逆判准。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：各 Varnad 大运子期的长度、本盘上升（Lagn）落在哪个星座。
- 缺失即停字段：["各 Varnad 大运子期的长度", "本盘上升（Lagn）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v21-24`｜PDF [17]｜“the order will also be clockwise, or anti-clockwise, as explained earlier”
  - `bphs-97:santhanam:ch05:v14-15`｜PDF [16]｜“If the natal Lagn is an odd Rāśi, the counting of Dashas is clockwise, otherwise anticlockwise.”


## 四路查书计划

### 支持路

- Similar assessments be made with reference to the Varnad of each Bhava commencing the first
- The sub period of each Dasha will be one twelfth of the Dasha and the order will also be clockwise, or anti-clockwise, as explained earlier
- 各宫 Varnad 评断 子期 十二分之一

### 反例或取消路

- These Varnad Dashas are only for Bhavas Rāśis and not their occupants
- Now I am going to describe the Sthir Dasha. In this Dasha system 7, 8 and 9 years are the Dasha spans of the Movable (Char), Fixed (Sthir) and Dual (Dvisva Bhava) Rāśis
- 子期 是否按行星分配 另有说法

### 适用边界路

- Lagn Dasha years will equal the number of Rāśis intervening between the natal Lagn and Varnad
- If the natal Lagn is an odd Rāśi the counting of Dashas is clockwise otherwise anticlockwise
- The natal Lagn is to be calculated according to birth place

### 判断方法路

- Effects of Varnad. Now listen to the use of the above
- The Varnad Lagn be considered, as natal Lagna, while the 7<sup>th</sup> from Varnad will denote the longevity of the spouse
- Varnad 各宫 怎么排大运

## 上游问题

- 无

## 停止条件

- 缺少各宫的 Varnad 星座时停止。
- 缺少各 Varnad 大运的年数时，子期长度停判。
- 本命上升所在星座的奇偶未定时，子期次序停判。
- 原文没有说明子期分配到哪些宫，分配对象未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
