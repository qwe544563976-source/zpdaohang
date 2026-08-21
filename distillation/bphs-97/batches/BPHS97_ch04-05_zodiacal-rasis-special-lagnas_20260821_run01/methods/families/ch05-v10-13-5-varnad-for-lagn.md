---
method: ch05-v10-13-5-varnad-for-lagn
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升的 Varnad（Varnad for Lagn）推算：本命上升与时上升各按奇偶计数，再合成后回数

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的 Varnad 是哪个星座
- Varnad Dasha 怎么起
- Varnad 怎么从上升和时上升算出来

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升（Lagn）落在哪个星座
- 本盘时上升（Hora Lagn）落在哪个星座

## 按情况检查的事实

- 本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）
- 本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）
- 本盘时上升（Hora Lagn）所在星座是否为奇数（odd）
- 本盘时上升（Hora Lagn）所在星座是否为偶数（even）
- 本盘上升（Lagn）的 Varnad 计数值是否为奇数
- 本盘上升（Lagn）的 Varnad 计数值是否为偶数
- 本盘时上升（Hora Lagn）的 Varnad 计数值是否为奇数
- 本盘时上升（Hora Lagn）的 Varnad 计数值是否为偶数
- 本盘 Varnad 推算所得的最后一个数是否为奇数
- 本盘 Varnad 推算所得的最后一个数是否为偶数

## 依赖方法

- ch05-v4-5-hora-lagn

## 执行步骤

### ch05-v10-13-5-varnad-for-lagn.step-001

- 动作：看本命上升（natal Lagn）落奇数星座还是偶数星座：奇数星座就从白羊（Mesh）顺数到本命上升，偶数星座就从双鱼（Meen）逆数到本命上升，得出第一个计数值。
- 适用范围：本偈是 Varnad 大运（Varnad Dasha）的推算法，原文自述「just by knowing which one can deal with the longevity of a native」（知此即可处理命主的寿命），但本偈只给推算、不给寿命断法；本步只算本命上升一侧的计数值。
- 原文最小意思：本命上升（natal Lagn）是奇数星座（odd Rāśi）时，从白羊（Mesh）顺数到本命上升；本命上升是偶数星座（even Rāśi）时，从双鱼（Meen）逆数到本命上升。
- 本步骤产出事实：["本盘上升（Lagn）的 Varnad 计数值"]
- 所需事实：["本盘上升（Lagn）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）落在哪个星座"}, {"operator": "OR", "operands": [{"fact_key": "本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）"}, {"fact_key": "本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升（Lagn）落在哪个星座"}, "required_fact_keys": ["本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）"], "branch_condition_logic": {"fact_key": "本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）"}, "selection_group": "ch05-v10-13-5-varnad-for-lagn.step-001:natal-lagn-parity", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）所在星座是否为奇数星座（odd Rāśi）。"}, {"when": {"fact_key": "本盘上升（Lagn）落在哪个星座"}, "required_fact_keys": ["本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）"], "branch_condition_logic": {"fact_key": "本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）"}, "selection_group": "ch05-v10-13-5-varnad-for-lagn.step-001:natal-lagn-parity", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）所在星座是否为偶数星座（even Rāśi）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把起数点从白羊（Mesh）、双鱼（Meen）改成原文没写的其他星座。", "不得把顺数、逆数的方向对调。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagn）落在哪个星座。
- 缺失即停字段：["本盘上升（Lagn）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v10-13.5`｜PDF [16]｜“If the natal Lagn is an odd Rāśi, count directly from Mesh to natal Lagn. If the natal Lagn is an even Rāśi, count from Meen to the natal Lagn in the reverse order.”

### ch05-v10-13-5-varnad-for-lagn.step-002

- 动作：同样看时上升（Hora Lagn）是奇是偶：奇就从白羊（Mesh）顺数到时上升，偶就从双鱼（Meen）逆数到时上升，得出第二个计数值。
- 适用范围：本步只算时上升一侧的计数值；时上升须先按本章前文的起法算出。
- 原文最小意思：时上升（Hora Lagn）是奇数（odd one）时，从白羊（Mesh）顺数到时上升；时上升是偶数（even one）时，从双鱼（Meen）逆数到时上升。
- 本步骤产出事实：["本盘时上升（Hora Lagn）的 Varnad 计数值"]
- 所需事实：["本盘时上升（Hora Lagn）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘时上升（Hora Lagn）落在哪个星座"}, {"operator": "OR", "operands": [{"fact_key": "本盘时上升（Hora Lagn）所在星座是否为奇数（odd）"}, {"fact_key": "本盘时上升（Hora Lagn）所在星座是否为偶数（even）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘时上升（Hora Lagn）落在哪个星座"}, "required_fact_keys": ["本盘时上升（Hora Lagn）所在星座是否为奇数（odd）"], "branch_condition_logic": {"fact_key": "本盘时上升（Hora Lagn）所在星座是否为奇数（odd）"}, "selection_group": "ch05-v10-13-5-varnad-for-lagn.step-002:hora-lagn-parity", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘时上升（Hora Lagn）所在星座是否为奇数（odd）。"}, {"when": {"fact_key": "本盘时上升（Hora Lagn）落在哪个星座"}, "required_fact_keys": ["本盘时上升（Hora Lagn）所在星座是否为偶数（even）"], "branch_condition_logic": {"fact_key": "本盘时上升（Hora Lagn）所在星座是否为偶数（even）"}, "selection_group": "ch05-v10-13-5-varnad-for-lagn.step-002:hora-lagn-parity", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘时上升（Hora Lagn）所在星座是否为偶数（even）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把起数点从白羊（Mesh）、双鱼（Meen）改成原文没写的其他星座。", "不得用本命上升的奇偶去代替时上升的奇偶。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘时上升（Hora Lagn）落在哪个星座。
- 缺失即停字段：["本盘时上升（Hora Lagn）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v10-13.5`｜PDF [16]｜“Similarly, if the Hora Lagn is an odd one, count from Mesh to Hora Lagn in direct order. If the Hora Lagn is an even one, count from Meen to Hora Lagn in the reverse order.”

### ch05-v10-13-5-varnad-for-lagn.step-003

- 动作：比较两个计数值的奇偶：同为奇数或同为偶数就把两数相加，一奇一偶就取两数之差。
- 适用范围：仅限 Varnad 推算链条中的合成一步；原文只给相加与取差两种处理，没有给其他运算。
- 原文最小意思：两个计数值同为奇数（odd Rāśis）或同为偶数（even Rāśis）时，把两数相加；一个是奇数、另一个是偶数时，取两数之差。
- 本步骤产出事实：["本盘上升与时上升两计数值的合成数"]
- 所需事实：["本盘上升（Lagn）的 Varnad 计数值", "本盘时上升（Hora Lagn）的 Varnad 计数值"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值是否为奇数"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值是否为奇数"}]}, {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值是否为偶数"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值是否为偶数"}]}, {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值是否为奇数"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值是否为偶数"}]}, {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值是否为偶数"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值是否为奇数"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值"}]}, "required_fact_keys": ["本盘上升（Lagn）的 Varnad 计数值是否为奇数", "本盘时上升（Hora Lagn）的 Varnad 计数值是否为奇数"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值是否为奇数"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值是否为奇数"}]}, "selection_group": "ch05-v10-13-5-varnad-for-lagn.step-003:product-parity-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）的 Varnad 计数值是否为奇数、本盘时上升（Hora Lagn）的 Varnad 计数值是否为奇数。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值"}]}, "required_fact_keys": ["本盘上升（Lagn）的 Varnad 计数值是否为偶数", "本盘时上升（Hora Lagn）的 Varnad 计数值是否为偶数"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值是否为偶数"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值是否为偶数"}]}, "selection_group": "ch05-v10-13-5-varnad-for-lagn.step-003:product-parity-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）的 Varnad 计数值是否为偶数、本盘时上升（Hora Lagn）的 Varnad 计数值是否为偶数。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值"}]}, "required_fact_keys": ["本盘上升（Lagn）的 Varnad 计数值是否为奇数", "本盘时上升（Hora Lagn）的 Varnad 计数值是否为偶数"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值是否为奇数"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值是否为偶数"}]}, "selection_group": "ch05-v10-13-5-varnad-for-lagn.step-003:product-parity-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）的 Varnad 计数值是否为奇数、本盘时上升（Hora Lagn）的 Varnad 计数值是否为偶数。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值"}]}, "required_fact_keys": ["本盘上升（Lagn）的 Varnad 计数值是否为偶数", "本盘时上升（Hora Lagn）的 Varnad 计数值是否为奇数"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）的 Varnad 计数值是否为偶数"}, {"fact_key": "本盘时上升（Hora Lagn）的 Varnad 计数值是否为奇数"}]}, "selection_group": "ch05-v10-13-5-varnad-for-lagn.step-003:product-parity-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘上升（Lagn）的 Varnad 计数值是否为偶数、本盘时上升（Hora Lagn）的 Varnad 计数值是否为奇数。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得在两数同奇同偶时取差，也不得在一奇一偶时相加。", "不得给相加、取差之外再补原文没写的运算。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagn）的 Varnad 计数值、本盘时上升（Hora Lagn）的 Varnad 计数值。
- 缺失即停字段：["本盘上升（Lagn）的 Varnad 计数值", "本盘时上升（Hora Lagn）的 Varnad 计数值"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v10-13.5`｜PDF [16]｜“If both the products are odd Rāśis, or even Rāśis, then add both the figures. If one is odd and the other is even, then know the difference between the two products.”

### ch05-v10-13-5-varnad-for-lagn.step-004

- 动作：看合成后所得的最后一个数是奇是偶：奇就从白羊（Mesh）顺数这么多个星座，偶就从双鱼（Meen）逆数这么多个星座，数到的星座就是上升的 Varnad。
- 适用范围：本步给出上升的 Varnad（Varnad for Lagn）本身；各宫的 Varnad 见本章后文。
- 原文最小意思：这一过程中最后所得的数是奇数（odd one）时，从白羊（Mesh）顺数这么多个星座；是偶数（even one）时，从双鱼（Meen）逆数这么多个星座；如此得知的星座就是上升的 Varnad（Varnad for Lagn）。
- 本步骤产出事实：["本盘上升的 Varnad 星座（Varnad for Lagn）"]
- 所需事实：["本盘上升与时上升两计数值的合成数"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升与时上升两计数值的合成数"}, {"operator": "OR", "operands": [{"fact_key": "本盘 Varnad 推算所得的最后一个数是否为奇数"}, {"fact_key": "本盘 Varnad 推算所得的最后一个数是否为偶数"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升与时上升两计数值的合成数"}, "required_fact_keys": ["本盘 Varnad 推算所得的最后一个数是否为奇数"], "branch_condition_logic": {"fact_key": "本盘 Varnad 推算所得的最后一个数是否为奇数"}, "selection_group": "ch05-v10-13-5-varnad-for-lagn.step-004:latest-product-parity", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘 Varnad 推算所得的最后一个数是否为奇数。"}, {"when": {"fact_key": "本盘上升与时上升两计数值的合成数"}, "required_fact_keys": ["本盘 Varnad 推算所得的最后一个数是否为偶数"], "branch_condition_logic": {"fact_key": "本盘 Varnad 推算所得的最后一个数是否为偶数"}, "selection_group": "ch05-v10-13-5-varnad-for-lagn.step-004:latest-product-parity", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘 Varnad 推算所得的最后一个数是否为偶数。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把起数点从白羊（Mesh）、双鱼（Meen）改成原文没写的其他星座。", "原文只说数到的星座就是上升的 Varnad，不得据此直接下寿命断语——断法见本章后文。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升与时上升两计数值的合成数。
- 缺失即停字段：["本盘上升与时上升两计数值的合成数"]
- 原文证据：
  - `bphs-97:santhanam:ch05:v10-13.5`｜PDF [16]｜“If the latest product in this process is an odd one, count so many Rāśis from Mesh in a direct manner; if an even one, count so many Rāśis from Meen in reverse order. The Rashiso known will be the Varnad for Lagn.”


## 四路查书计划

### 支持路

- I now detail Varnad Dasha, just by knowing which one can deal with the longevity of a native
- The Rashiso known will be the Varnad for Lagn
- Varnad 推算 奇数星座 白羊 双鱼 逆数

### 反例或取消路

- Out of the two natal Lagn and Hora Lagna whichever is stronger from there Varnad starts
- These Varnad Dashas are only for Bhavas Rāśis and not their occupants
- Varnad 与其他大运 起法不同 Vimshottari

### 适用边界路

- Similar assessments be made with reference to the Varnad of each Bhava commencing the first
- The natal Lagn is to be calculated according to birth place
- odd Rāśi even Rāśi 奇数星座 偶数星座 界定

### 判断方法路

- I now detail Varnad Dasha longevity of a native
- Hora Lagn repeats itself every 2½ Ghatis divide by 2½
- Varnad for Lagn 算出来以后怎么用

## 上游问题

- 无

## 停止条件

- 缺少本命上升所在星座时停止。
- 缺少时上升（Hora Lagn）所在星座时停止——本推算要用到它。
- 两个计数值的奇偶未定时停止。
- 合成后最后一个数的奇偶未定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
