---
method: ch14-v12-single-cobirth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 十二宫主（或版本作十一宫主）与 Mangal、Guru 同宫且三宫被 Chandra 占据：只有1位兄弟姐妹

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我是不是只有一个兄弟姐妹
- 我家里孩子多不多

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 三宫是否被 Chandra 占据

## 按情况检查的事实

- 十二宫主是否与 Mangal 及 Guru 同宫
- 十一宫主是否与 Mangal 及 Guru 同宫

## 依赖方法

- 无

## 执行步骤

### ch14-v12-single-cobirth.step-001

- 动作：核对三宫是否被 Chandra 占据，并按版本分支核对十二宫主或十一宫主是否与 Mangal 及 Guru 同宫。
- 适用范围：仅限本命盘三宫兄弟姐妹数目主题；原文自带“some texts read”的版本异文，两种读法各自成一支。
- 原文最小意思：十二宫主（Vyaya’s Lord）与 Mangal 及 Guru 同宫，或有些版本作十一宫主（Labh’s Lord），同时三宫被 Chandra 占据时，只有1位兄弟姐妹。
- 本步骤产出事实：["只有1位兄弟姐妹的判定"]
- 所需事实：["三宫是否被 Chandra 占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "三宫是否被 Chandra 占据"}, {"operator": "OR", "operands": [{"fact_key": "十二宫主是否与 Mangal 及 Guru 同宫"}, {"fact_key": "十一宫主是否与 Mangal 及 Guru 同宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "三宫是否被 Chandra 占据"}, "required_fact_keys": ["十二宫主是否与 Mangal 及 Guru 同宫"], "branch_condition_logic": {"fact_key": "十二宫主是否与 Mangal 及 Guru 同宫"}, "selection_group": "ch14-v12-single-cobirth.step-001:lord-reading", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主是否与 Mangal 及 Guru 同宫。"}, {"when": {"fact_key": "三宫是否被 Chandra 占据"}, "required_fact_keys": ["十一宫主是否与 Mangal 及 Guru 同宫"], "branch_condition_logic": {"fact_key": "十一宫主是否与 Mangal 及 Guru 同宫"}, "selection_group": "ch14-v12-single-cobirth.step-001:lord-reading", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主是否与 Mangal 及 Guru 同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断这位兄弟姐妹的性别、长幼或存亡。", "不得把两种版本读法当成同时成立的条件。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：三宫是否被 Chandra 占据。
- 缺失即停字段：["三宫是否被 Chandra 占据"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v12-13`｜PDF [29]｜“There will be 1 co-born, if Vyaya’s Lord (some texts read, as Labh’s Lord) joins Mangal and Guru, while Sahaj Bhava is occupied by Chandra.”


## 四路查书计划

### 支持路

- There will be 1 co-born Vyaya Lord joins Mangal and Guru Sahaj occupied by Chandra
- 十二宫主与火星木星同宫 三宫月亮 只有一位兄弟姐妹

### 反例或取消路

- 12 will be the number of total co-born
- 兄弟姐妹总数十二人

### 适用边界路

- some texts read as Labh Lord variant reading
- 版本异文对兄弟姐妹数目判断的影响

### 判断方法路

- how to judge single co-born in BPHS
- 判断只有一位兄弟姐妹的步骤

## 上游问题

- 无

## 停止条件

- 缺少三宫是否被 Chandra 占据的事实时停止。
- 缺少十二宫主或十一宫主与 Mangal、Guru 的同宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
