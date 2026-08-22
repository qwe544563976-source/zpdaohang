---
method: ch03-v56-temporary-relationship
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 临时关系：出生盘中互距 2、3、4、10、11、12 位为友，否则为敌

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我盘里这两颗行星临时是友是敌
- 临时friendship怎么算

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 另一行星（Grah）自待判行星起数落在第几个位置

## 按情况检查的事实

- 另一行星（Grah）自待判行星起数是否落在第2个位置
- 另一行星（Grah）自待判行星起数是否落在第3个位置
- 另一行星（Grah）自待判行星起数是否落在第4个位置
- 另一行星（Grah）自待判行星起数是否落在第10个位置
- 另一行星（Grah）自待判行星起数是否落在第11个位置
- 另一行星（Grah）自待判行星起数是否落在第12个位置

## 依赖方法

- 无

## 执行步骤

### ch03-v56-temporary-relationship.step-001

- 动作：数出另一行星自待判行星起的位次，落在第 2、3、4、10、11、12 位时判为互为友星。
- 适用范围：本条限于给定的出生盘（This applies to a given Janm Kundali）；原文没有说明「自另一行星起数」按星座计还是按宫计。
- 原文最小意思：一颗行星（Grah）落在从另一行星起第 2、3、4、10、11、12 个位置时，两者互为友星。
- 本步骤产出事实：["两行星临时友星判定"]
- 所需事实：["另一行星（Grah）自待判行星起数落在第几个位置"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "另一行星（Grah）自待判行星起数落在第几个位置"}, {"operator": "OR", "operands": [{"fact_key": "另一行星（Grah）自待判行星起数是否落在第2个位置"}, {"fact_key": "另一行星（Grah）自待判行星起数是否落在第3个位置"}, {"fact_key": "另一行星（Grah）自待判行星起数是否落在第4个位置"}, {"fact_key": "另一行星（Grah）自待判行星起数是否落在第10个位置"}, {"fact_key": "另一行星（Grah）自待判行星起数是否落在第11个位置"}, {"fact_key": "另一行星（Grah）自待判行星起数是否落在第12个位置"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "另一行星（Grah）自待判行星起数落在第几个位置"}, "required_fact_keys": ["另一行星（Grah）自待判行星起数是否落在第2个位置"], "branch_condition_logic": {"fact_key": "另一行星（Grah）自待判行星起数是否落在第2个位置"}, "selection_group": "ch03-v56-temporary-relationship.step-001:temporary-friend-position", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）自待判行星起数是否落在第2个位置。"}, {"when": {"fact_key": "另一行星（Grah）自待判行星起数落在第几个位置"}, "required_fact_keys": ["另一行星（Grah）自待判行星起数是否落在第3个位置"], "branch_condition_logic": {"fact_key": "另一行星（Grah）自待判行星起数是否落在第3个位置"}, "selection_group": "ch03-v56-temporary-relationship.step-001:temporary-friend-position", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）自待判行星起数是否落在第3个位置。"}, {"when": {"fact_key": "另一行星（Grah）自待判行星起数落在第几个位置"}, "required_fact_keys": ["另一行星（Grah）自待判行星起数是否落在第4个位置"], "branch_condition_logic": {"fact_key": "另一行星（Grah）自待判行星起数是否落在第4个位置"}, "selection_group": "ch03-v56-temporary-relationship.step-001:temporary-friend-position", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）自待判行星起数是否落在第4个位置。"}, {"when": {"fact_key": "另一行星（Grah）自待判行星起数落在第几个位置"}, "required_fact_keys": ["另一行星（Grah）自待判行星起数是否落在第10个位置"], "branch_condition_logic": {"fact_key": "另一行星（Grah）自待判行星起数是否落在第10个位置"}, "selection_group": "ch03-v56-temporary-relationship.step-001:temporary-friend-position", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）自待判行星起数是否落在第10个位置。"}, {"when": {"fact_key": "另一行星（Grah）自待判行星起数落在第几个位置"}, "required_fact_keys": ["另一行星（Grah）自待判行星起数是否落在第11个位置"], "branch_condition_logic": {"fact_key": "另一行星（Grah）自待判行星起数是否落在第11个位置"}, "selection_group": "ch03-v56-temporary-relationship.step-001:temporary-friend-position", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）自待判行星起数是否落在第11个位置。"}, {"when": {"fact_key": "另一行星（Grah）自待判行星起数落在第几个位置"}, "required_fact_keys": ["另一行星（Grah）自待判行星起数是否落在第12个位置"], "branch_condition_logic": {"fact_key": "另一行星（Grah）自待判行星起数是否落在第12个位置"}, "selection_group": "ch03-v56-temporary-relationship.step-001:temporary-friend-position", "stop_condition": "选中该分支后，缺少以下事实即停止：另一行星（Grah）自待判行星起数是否落在第12个位置。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出临时友星带来什么吉果——本条只定关系。", "不得把本条的位次自行认定为星座计数或宫位计数——原文没有说。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：另一行星（Grah）自待判行星起数落在第几个位置。
- 缺失即停字段：["另一行星（Grah）自待判行星起数落在第几个位置"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v56`｜PDF [12]｜“The Grah, posited in the 2<sup>nd</sup> , 3<sup>rd</sup> , 4<sup>th</sup> , 10<sup>th</sup> , 11<sup>th</sup> , or the 12<sup>th</sup> from another, becomes a mutual friend.”

### ch03-v56-temporary-relationship.step-002

- 动作：不落在上述位次时，判为互为敌星。
- 适用范围：本条限于给定的出生盘（This applies to a given Janm Kundali）；「otherwise」承本方法第一步列出的六个位次。
- 原文最小意思：不属上述位次的情形，两者互为敌星。
- 本步骤产出事实：["两行星临时敌星判定"]
- 所需事实：["两行星临时友星判定"]
- 条件关系：{"operator": "NOT", "operands": [{"fact_key": "两行星临时友星判定"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得在临时关系里补出中立一档——本条只给友与敌两种。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：两行星临时友星判定。
- 缺失即停字段：["两行星临时友星判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v56`｜PDF [12]｜“There is enmity otherwise.”


## 四路查书计划

### 支持路

- The Grah, posited in the 2<sup>nd</sup> , 3<sup>rd</sup> , 4<sup>th</sup> , 10<sup>th</sup> , 11<sup>th</sup> , or the 12<sup>th</sup> from another, becomes a mutual friend. There is enmity otherwise
- 临时关系 互为友星 互为敌星

### 反例或取消路

- The Grahas ruling such Rāśis are its friends, apart from the Lord of its exaltation Rāśi. Lords other than these are its enemies
- 自然关系可能与临时关系相反

### 适用边界路

- Temporary Relationships
- (This applies to a given Janm Kundali)
- 临时关系只对给定出生盘成立

### 判断方法路

- Should two Grahas be naturally and temporarily friendly, they become extremely friendly
- 临时关系与自然关系怎么合成

## 上游问题

- 无

## 停止条件

- 缺少两行星相对位次的事实时停止。
- 原文没有说明位次按星座计还是按宫计，计数口径未定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
