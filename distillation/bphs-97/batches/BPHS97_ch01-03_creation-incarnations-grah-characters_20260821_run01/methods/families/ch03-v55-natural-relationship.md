---
method: ch03-v55-natural-relationship
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 自然关系：由 Mooltrikon 与入旺星座定友、敌、中立

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 两颗行星天然是友是敌
- 自然friendship怎么算

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘待判行星（Grah）的 Mooltrikon 落在哪个星座
- 另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座

## 按情况检查的事实

- 另一行星（Grah）是否主管从待判行星 Mooltrikon 起第2个星座
- 另一行星（Grah）是否主管从待判行星 Mooltrikon 起第4个星座
- 另一行星（Grah）是否主管从待判行星 Mooltrikon 起第5个星座
- 另一行星（Grah）是否主管从待判行星 Mooltrikon 起第8个星座
- 另一行星（Grah）是否主管从待判行星 Mooltrikon 起第9个星座
- 另一行星（Grah）是否主管从待判行星 Mooltrikon 起第12个星座
- 另一行星（Grah）是否主管待判行星的入旺星座（exaltation Rāśi）

## 依赖方法

- 无

## 执行步骤

### ch03-v55-natural-relationship.step-001

- 动作：从待判行星的 Mooltrikon 数出第 2、4、5、8、9、12 个星座，看另一行星是否主管其中某一个，或是否主管其入旺星座，据以判定自然友星。
- 适用范围：第3章自然关系条；本条只给友、敌、中立的判法，未给这三种关系各自的吉凶结果。
- 原文最小意思：从该行星（Grah）的 Mooltrikon 起第 2、4、5、8、9、12 个星座，主管这些星座的行星是它的友星，以及其入旺星座（exaltation Rāśi）之主也是友星。
- 本步骤产出事实：["两行星自然友星判定"]
- 所需事实：["本盘待判行星（Grah）的 Mooltrikon 落在哪个星座", "另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘待判行星（Grah）的 Mooltrikon 落在哪个星座"}, {"fact_key": "另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座"}]}, {"operator": "OR", "operands": [{"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第2个星座"}, {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第4个星座"}, {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第5个星座"}, {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第8个星座"}, {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第9个星座"}, {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第12个星座"}, {"fact_key": "另一行星（Grah）是否主管待判行星的入旺星座（exaltation Rāśi）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘待判行星（Grah）的 Mooltrikon 落在哪个星座"}, {"fact_key": "另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座"}]}, "required_fact_keys": ["另一行星（Grah）是否主管从待判行星 Mooltrikon 起第2个星座"], "branch_condition_logic": {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第2个星座"}, "selection_group": "ch03-v55-natural-relationship.step-001:friend-source", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）是否主管从待判行星 Mooltrikon 起第2个星座。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘待判行星（Grah）的 Mooltrikon 落在哪个星座"}, {"fact_key": "另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座"}]}, "required_fact_keys": ["另一行星（Grah）是否主管从待判行星 Mooltrikon 起第4个星座"], "branch_condition_logic": {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第4个星座"}, "selection_group": "ch03-v55-natural-relationship.step-001:friend-source", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）是否主管从待判行星 Mooltrikon 起第4个星座。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘待判行星（Grah）的 Mooltrikon 落在哪个星座"}, {"fact_key": "另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座"}]}, "required_fact_keys": ["另一行星（Grah）是否主管从待判行星 Mooltrikon 起第5个星座"], "branch_condition_logic": {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第5个星座"}, "selection_group": "ch03-v55-natural-relationship.step-001:friend-source", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）是否主管从待判行星 Mooltrikon 起第5个星座。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘待判行星（Grah）的 Mooltrikon 落在哪个星座"}, {"fact_key": "另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座"}]}, "required_fact_keys": ["另一行星（Grah）是否主管从待判行星 Mooltrikon 起第8个星座"], "branch_condition_logic": {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第8个星座"}, "selection_group": "ch03-v55-natural-relationship.step-001:friend-source", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）是否主管从待判行星 Mooltrikon 起第8个星座。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘待判行星（Grah）的 Mooltrikon 落在哪个星座"}, {"fact_key": "另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座"}]}, "required_fact_keys": ["另一行星（Grah）是否主管从待判行星 Mooltrikon 起第9个星座"], "branch_condition_logic": {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第9个星座"}, "selection_group": "ch03-v55-natural-relationship.step-001:friend-source", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）是否主管从待判行星 Mooltrikon 起第9个星座。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘待判行星（Grah）的 Mooltrikon 落在哪个星座"}, {"fact_key": "另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座"}]}, "required_fact_keys": ["另一行星（Grah）是否主管从待判行星 Mooltrikon 起第12个星座"], "branch_condition_logic": {"fact_key": "另一行星（Grah）是否主管从待判行星 Mooltrikon 起第12个星座"}, "selection_group": "ch03-v55-natural-relationship.step-001:friend-source", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）是否主管从待判行星 Mooltrikon 起第12个星座。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘待判行星（Grah）的 Mooltrikon 落在哪个星座"}, {"fact_key": "另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座"}]}, "required_fact_keys": ["另一行星（Grah）是否主管待判行星的入旺星座（exaltation Rāśi）"], "branch_condition_logic": {"fact_key": "另一行星（Grah）是否主管待判行星的入旺星座（exaltation Rāśi）"}, "selection_group": "ch03-v55-natural-relationship.step-001:friend-source", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）是否主管待判行星的入旺星座（exaltation Rāśi）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这里的星座计数改成宫位计数——原文数的是 Rāśis。", "不得据本条推出友星带来什么吉果——本条只定关系。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘待判行星（Grah）的 Mooltrikon 落在哪个星座、另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座。
- 缺失即停字段：["本盘待判行星（Grah）的 Mooltrikon 落在哪个星座", "另一行星（Grah）主管的星座是从待判行星 Mooltrikon 起的第几个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v55`｜PDF [12]｜“Note the Rāśis, which are the 2<sup>nd</sup> , 4<sup>th</sup> , 5<sup>th</sup> , 8<sup>th</sup> , 9<sup>th</sup> and 12<sup>th</sup> from the Mooltrikon of a Grah. The Grahas ruling such Rāśis are its friends, apart from the Lord of its exaltation Rāśi.”

### ch03-v55-natural-relationship.step-002

- 动作：把不在上述友星之列的星座之主判为敌星。
- 适用范围：第3章自然关系条；「上述之外」承本方法第一步给出的友星名单。
- 原文最小意思：上述之外的星座之主是它的敌星。
- 本步骤产出事实：["两行星自然敌星判定"]
- 所需事实：["两行星自然友星判定"]
- 条件关系：{"operator": "NOT", "operands": [{"fact_key": "两行星自然友星判定"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出敌星带来什么凶果——本条只定关系。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：两行星自然友星判定。
- 缺失即停字段：["两行星自然友星判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v55`｜PDF [12]｜“Lords other than these are its enemies.”

### ch03-v55-natural-relationship.step-003

- 动作：若同一颗行星按上述两种算法既算友星又算敌星，判为中立。
- 适用范围：第3章自然关系条；「两种算法」承本偈前两句的友星算法与敌星算法。
- 原文最小意思：若一颗行星（Grah）依上述两种算法（two computations）既成其友星又成其敌星，则它是中立（neutral, or equal）。
- 本步骤产出事实：["两行星自然中立判定"]
- 所需事实：["两行星自然友星判定", "两行星自然敌星判定"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "两行星自然友星判定"}, {"fact_key": "两行星自然敌星判定"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出中立关系带来什么结果——本条只定关系。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：两行星自然友星判定、两行星自然敌星判定。
- 缺失即停字段：["两行星自然友星判定", "两行星自然敌星判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v55`｜PDF [12]｜“If a Grah becomes its friend as well, as its enemy (on account of the said two computations), then it is neutral, or equal.”


## 四路查书计划

### 支持路

- Note the Rāśis, which are the 2<sup>nd</sup> , 4<sup>th</sup> , 5<sup>th</sup> , 8<sup>th</sup> , 9<sup>th</sup> and 12<sup>th</sup> from the Mooltrikon of a Grah
- The Grahas ruling such Rāśis are its friends, apart from the Lord of its exaltation Rāśi
- 自然友星 敌星 中立 怎么定

### 反例或取消路

- The Grah, posited in the 2<sup>nd</sup> , 3<sup>rd</sup> , 4<sup>th</sup> , 10<sup>th</sup> , 11<sup>th</sup> , or the 12<sup>th</sup> from another, becomes a mutual friend. There is enmity otherwise
- 临时关系可能与自然关系相反

### 适用边界路

- (This applies to a given Janm Kundali)
- 自然关系与限于出生盘的临时关系之别

### 判断方法路

- Should two Grahas be naturally and temporarily friendly, they become extremely friendly
- Its beneficence is one fourth in a friendly Rāśi
- 定完友敌之后怎么用

## 上游问题

- 无

## 停止条件

- 缺少待判行星 Mooltrikon 所在星座时停止。
- 缺少另一行星所主星座与 Mooltrikon 的相对位次时停止。
- 本条只定友敌中立，没有给吉凶结果，要下断语必须另找原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
