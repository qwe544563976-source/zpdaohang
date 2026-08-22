---
method: ch01-v5-8-teaching-unfit-student
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 不可传授的对象：不情愿的学生、异端者、狡诈之人，教之必永远招祸

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 什么样的人不能教这门吠陀占星
- 把这门学问教给不该教的人会怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本次受教者是谁

## 按情况检查的事实

- 受教者是否不情愿学（an unwilling student）
- 受教者是否是异端者（a heterodox）
- 受教者是否是狡诈之人（a crafty person）

## 依赖方法

- 无

## 执行步骤

### ch01-v5-8-teaching-unfit-student.step-001

- 动作：先确定本次受教者是谁，再核对他是否属于原文列出的三类不适格对象。
- 适用范围：只管『可不可以把这门学问传给此人』这一件事，不是本命盘吉凶判断；原文自陈这门学问是 Parashara 从 Lord Brahma 处听来后转述（as heard through Lord Brahma）。原文没有指明祸患落在传授者还是受教者身上，未确定即停判。
- 原文最小意思：把这门学问传授给不情愿的学生、异端者、狡诈之人，无疑将永远招致祸患。
- 本步骤产出事实：["不适格受教者的传授后果判定"]
- 所需事实：["本次受教者是谁"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本次受教者是谁"}, {"operator": "OR", "operands": [{"fact_key": "受教者是否不情愿学（an unwilling student）"}, {"fact_key": "受教者是否是异端者（a heterodox）"}, {"fact_key": "受教者是否是狡诈之人（a crafty person）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本次受教者是谁"}, "required_fact_keys": ["受教者是否不情愿学（an unwilling student）"], "branch_condition_logic": {"fact_key": "受教者是否不情愿学（an unwilling student）"}, "selection_group": "ch01-v5-8-teaching-unfit-student.step-001:unfit-recipient", "stop_condition": "选中该分支后，缺少以下事实即停止：受教者是否不情愿学（an unwilling student）。"}, {"when": {"fact_key": "本次受教者是谁"}, "required_fact_keys": ["受教者是否是异端者（a heterodox）"], "branch_condition_logic": {"fact_key": "受教者是否是异端者（a heterodox）"}, "selection_group": "ch01-v5-8-teaching-unfit-student.step-001:unfit-recipient", "stop_condition": "选中该分支后，缺少以下事实即停止：受教者是否是异端者（a heterodox）。"}, {"when": {"fact_key": "本次受教者是谁"}, "required_fact_keys": ["受教者是否是狡诈之人（a crafty person）"], "branch_condition_logic": {"fact_key": "受教者是否是狡诈之人（a crafty person）"}, "selection_group": "ch01-v5-8-teaching-unfit-student.step-001:unfit-recipient", "stop_condition": "选中该分支后，缺少以下事实即停止：受教者是否是狡诈之人（a crafty person）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这条读成本命盘判断——原文说的是受教者的身份与品性，没有涉及任何行星、宫位或星座。", "不得据此推断祸患的具体内容、轻重或应验时间；原文只说 Woeful forever。", "原文没有指明祸患落在传授者还是受教者身上，未确定即停判，不得指定其中一方。", "不得把不适格对象扩大到原文没有列出的其他人群。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本次受教者是谁。
- 缺失即停字段：["本次受教者是谁"]
- 原文证据：
  - `bphs-97:santhanam:ch01:v5-8`｜PDF [7]｜“Woeful forever, doubtlessly, will it be to impart knowledge of this science to an unwilling student, to a heterodox and to a crafty person.”


## 四路查书计划

### 支持路

- 把这门学问传给不情愿的学生、异端、狡诈之人 招祸

### 反例或取消路

- Teach this supreme Vedanga Jyotish Shastra only to one who is gentle and amiable devoted truthful brilliant

### 适用边界路

- Do not impart the knowledge of this Shastra to one who is insignificative slanders or calumniates others nor to one who is not intelligent is wicked and unknown to you
- Jyotish the supreme limb of the Vedas has three divisions Horā Ganita and Samhita

### 判断方法路

- Now I will impart to you the knowledge of a great secrecy and superior importance which was communicated to me by Lord Brahma
- narrate to you the science of Jyotish as heard through Lord Brahma

## 上游问题

- 无

## 停止条件

- 缺少「本次受教者是谁」时停止。
- 三类不适格身份都无法确认时停止。
- 原文没有指明祸患落在传授者还是受教者身上，未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
