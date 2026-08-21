---
method: ch05-v16-20-varnad-as-lagna-relatives
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 以 Varnad 为上升看亲属寿命：7 配偶、11 兄姐、3 弟妹、5 子、4 母、9 父

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我配偶的寿命从哪一宫看
- 父母的寿命看哪一宫
- 兄弟姐妹和儿子的寿命看哪一宫

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座

## 按情况检查的事实

- 无

## 依赖方法

- ch05-v10-13-5-varnad-for-lagn

## 执行步骤

### ch05-v16-20-varnad-as-lagna-relatives.step-001

- 动作：把上升的 Varnad（Varnad Lagn）当作本命上升（natal Lagna）来看待，据此起出自 Varnad 起算的各宫。
- 适用范围：本步承接前偈算出的上升 Varnad；原文只说当作本命上升看待，没有说本命上升盘因此作废。
- 原文最小意思：上升的 Varnad（Varnad Lagn）要当作本命上升（natal Lagna）来看待。
- 本步骤产出事实：["以 Varnad 为上升的判断框架"]
- 所需事实：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"]
- 条件关系：{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此把本命上升盘作废或替换掉。", "原文只说当作本命上升看待，没有给以 Varnad 为上升时的具体断法，断法未确定即停判。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座。
- 缺失即停字段：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v16-20`｜PDF [17]｜“The Varnad Lagn be considered, as natal Lagna”

### ch05-v16-20-varnad-as-lagna-relatives.step-002

- 动作：以 Varnad 为上升起算，把自 Varnad 起算的第 7 宫作为示配偶的寿命的判断入口。
- 适用范围：宫位自 Varnad 起算，不是自本命上升起算；原文只指出该宫所主的对象，没有给判寿命的具体方法。
- 原文最小意思：自 Varnad 起算的第 7 宫表示配偶的寿命。
- 本步骤产出事实：["自 Varnad 起算第 7 宫主配偶寿命的判断入口"]
- 所需事实：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}, {"fact_key": "以 Varnad 为上升的判断框架"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把自 Varnad 起算的第 7 宫改读成自本命上升起算的第 7 宫。", "原文只说它表示配偶的寿命，不得据此断婚姻好坏或结婚时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座、以 Varnad 为上升的判断框架。
- 缺失即停字段：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v16-20`｜PDF [17]｜“the 7<sup>th</sup> from Varnad will denote the longevity of the spouse”

### ch05-v16-20-varnad-as-lagna-relatives.step-003

- 动作：以 Varnad 为上升起算，把自 Varnad 起算的第 11 宫作为示兄与姐的寿命的判断入口。
- 适用范围：宫位自 Varnad 起算，不是自本命上升起算；原文只指出该宫所主的对象，没有给判寿命的具体方法。
- 原文最小意思：自 Varnad 起算的第 11 宫表示兄与姐的寿命。
- 本步骤产出事实：["自 Varnad 起算第 11 宫主兄姐寿命的判断入口"]
- 所需事实：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}, {"fact_key": "以 Varnad 为上升的判断框架"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把自 Varnad 起算的第 11 宫改读成自本命上升起算的第 11 宫。", "原文只说它表示兄与姐的寿命，不得据此断兄姐的数目或成就。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座、以 Varnad 为上升的判断框架。
- 缺失即停字段：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v16-20`｜PDF [17]｜“the 11<sup>th</sup> longevity of elder brothers and sisters”

### ch05-v16-20-varnad-as-lagna-relatives.step-004

- 动作：以 Varnad 为上升起算，把自 Varnad 起算的第 3 宫作为示弟与妹的寿命的判断入口。
- 适用范围：宫位自 Varnad 起算，不是自本命上升起算；原文只指出该宫所主的对象，没有给判寿命的具体方法。
- 原文最小意思：自 Varnad 起算的第 3 宫表示弟与妹的寿命。
- 本步骤产出事实：["自 Varnad 起算第 3 宫主弟妹寿命的判断入口"]
- 所需事实：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}, {"fact_key": "以 Varnad 为上升的判断框架"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把自 Varnad 起算的第 3 宫改读成自本命上升起算的第 3 宫。", "原文只说它表示弟与妹的寿命，不得据此断弟妹的数目或成就。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座、以 Varnad 为上升的判断框架。
- 缺失即停字段：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v16-20`｜PDF [17]｜“the 3<sup>rd</sup> longevity of younger brothers and sisters”

### ch05-v16-20-varnad-as-lagna-relatives.step-005

- 动作：以 Varnad 为上升起算，把自 Varnad 起算的第 5 宫作为示儿子的寿命的判断入口。
- 适用范围：宫位自 Varnad 起算，不是自本命上升起算；原文只指出该宫所主的对象，没有给判寿命的具体方法。
- 原文最小意思：自 Varnad 起算的第 5 宫表示儿子的寿命。
- 本步骤产出事实：["自 Varnad 起算第 5 宫主儿子寿命的判断入口"]
- 所需事实：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}, {"fact_key": "以 Varnad 为上升的判断框架"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把自 Varnad 起算的第 5 宫改读成自本命上升起算的第 5 宫。", "原文这一句只说儿子的寿命，不得据此断子女的数目或有无。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座、以 Varnad 为上升的判断框架。
- 缺失即停字段：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v16-20`｜PDF [17]｜“the 5<sup>th</sup> the longevity of sons”

### ch05-v16-20-varnad-as-lagna-relatives.step-006

- 动作：以 Varnad 为上升起算，把自 Varnad 起算的第 4 宫作为示母亲的寿命的判断入口。
- 适用范围：宫位自 Varnad 起算，不是自本命上升起算；原文只指出该宫所主的对象，没有给判寿命的具体方法。
- 原文最小意思：自 Varnad 起算的第 4 宫表示母亲的寿命。
- 本步骤产出事实：["自 Varnad 起算第 4 宫主母亲寿命的判断入口"]
- 所需事实：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}, {"fact_key": "以 Varnad 为上升的判断框架"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把自 Varnad 起算的第 4 宫改读成自本命上升起算的第 4 宫。", "原文只说它表示母亲的寿命，不得据此断母亲的其他境遇。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座、以 Varnad 为上升的判断框架。
- 缺失即停字段：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v16-20`｜PDF [17]｜“the 4<sup>th</sup> longevity of mother”

### ch05-v16-20-varnad-as-lagna-relatives.step-007

- 动作：以 Varnad 为上升起算，把自 Varnad 起算的第 9 宫作为示父亲的寿命的判断入口。
- 适用范围：宫位自 Varnad 起算，不是自本命上升起算；原文只指出该宫所主的对象，没有给判寿命的具体方法。
- 原文最小意思：自 Varnad 起算的第 9 宫表示父亲的寿命。
- 本步骤产出事实：["自 Varnad 起算第 9 宫主父亲寿命的判断入口"]
- 所需事实：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座"}, {"fact_key": "以 Varnad 为上升的判断框架"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把自 Varnad 起算的第 9 宫改读成自本命上升起算的第 9 宫。", "原文只说它表示父亲的寿命，不得据此断父亲的其他境遇。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座、以 Varnad 为上升的判断框架。
- 缺失即停字段：["本盘上升的 Varnad 星座（Varnad for Lagn）是哪个星座", "以 Varnad 为上升的判断框架"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v16-20`｜PDF [17]｜“the 9<sup>th</sup> longevity of father”


## 四路查书计划

### 支持路

- The Varnad Lagn be considered, as natal Lagna, while the 7<sup>th</sup> from Varnad will denote the longevity of the spouse
- the 11<sup>th</sup> longevity of elder brothers and sisters, the 3<sup>rd</sup> longevity of younger brothers and sisters, the 5<sup>th</sup> the longevity of sons, the 4<sup>th</sup> longevity of mother and the 9<sup>th</sup> longevity of father
- Varnad 起算 亲属 寿命 配偶 父母

### 反例或取消路

- These Varnad Dashas are only for Bhavas Rāśis and not their occupants
- I have narrated 3 different methods of longevity. Listen to me about the choice among the three systems
- Combinations for Father’s Death. The father of the native would have passed away prior to the native’s birth
- 亲属寿命 另有断法 不经 Varnad

### 适用边界路

- Should a Kon from Lagn’s Varnad be occupied or drishtied by a malefic
- Similar assessments be made with reference to the Varnad of each Bhava commencing the first
- Now be kind enough to throw light on Stri Jatak (female horoscopy)
- Varnad Lagn 与本命上升 起算 差别

### 判断方法路

- Out of the two, viz. natal Lagn and Hora Lagna, whichever is stronger, from there Varnad starts
- I now detail Varnad Dasha longevity of a native
- 以某一宫为上升 起算 各宫 方法

## 上游问题

- 无

## 停止条件

- 缺少上升的 Varnad 星座时停止。
- 原文只指出各宫所主的寿命对象，没有给判寿命的方法，判法未确定即停判。
- 各宫 Varnad 大运的年数须另按本章前偈算出，缺则停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
