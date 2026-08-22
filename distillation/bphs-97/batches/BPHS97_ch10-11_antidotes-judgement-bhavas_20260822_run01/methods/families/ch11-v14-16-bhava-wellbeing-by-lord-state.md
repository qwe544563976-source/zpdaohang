---
method: ch11-v14-16-bhava-wellbeing-by-lord-state
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 宫之安泰：宫主处于 Yuvavastha、Prabuddhavastha、Kismaravastha 之一或落十宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 宫主的状态怎么影响这一宫
- 宫主落十宫对这一宫有什么用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘该宫（Bhava）之主是哪颗行星

## 按情况检查的事实

- 该宫之主（Bhava's Lord）是否处于 Yuvavastha
- 该宫之主（Bhava's Lord）是否处于 Prabuddhavastha
- 该宫之主（Bhava's Lord）是否处于 Kismaravastha
- 该宫之主（Bhava's Lord）是否落十宫（Karm Bhava）

## 依赖方法

- 无

## 执行步骤

### ch11-v14-16-bhava-wellbeing-by-lord-state.step-001

- 动作：核对该宫之主是否处于 Yuvavastha、Prabuddhavastha、Kismaravastha 三种状态之一，或是否落十宫（Karm Bhava）。
- 适用范围：适用于十二宫中任一宫；本句以 its Lord 承前句「the Bhava」；本译本没有在别处界定 Yuvavastha、Prabuddhavastha、Kismaravastha 这三个状态名，未确定即停判。
- 原文最小意思：该宫之主处于 Yuvavastha、Prabuddhavastha、Kismaravastha 之一，或落十宫（Karm Bhava）时，该宫安泰（well-being）。
- 本步骤产出事实：["该宫之主状态带来的安泰判定"]
- 所需事实：["本盘该宫（Bhava）之主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘该宫（Bhava）之主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "该宫之主（Bhava's Lord）是否处于 Yuvavastha"}, {"fact_key": "该宫之主（Bhava's Lord）是否处于 Prabuddhavastha"}, {"fact_key": "该宫之主（Bhava's Lord）是否处于 Kismaravastha"}, {"fact_key": "该宫之主（Bhava's Lord）是否落十宫（Karm Bhava）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘该宫（Bhava）之主是哪颗行星"}, "required_fact_keys": ["该宫之主（Bhava's Lord）是否处于 Yuvavastha"], "branch_condition_logic": {"fact_key": "该宫之主（Bhava's Lord）是否处于 Yuvavastha"}, "selection_group": "ch11-v14-16-bhava-wellbeing-by-lord-state.step-001:lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：该宫之主（Bhava's Lord）是否处于 Yuvavastha。"}, {"when": {"fact_key": "本盘该宫（Bhava）之主是哪颗行星"}, "required_fact_keys": ["该宫之主（Bhava's Lord）是否处于 Prabuddhavastha"], "branch_condition_logic": {"fact_key": "该宫之主（Bhava's Lord）是否处于 Prabuddhavastha"}, "selection_group": "ch11-v14-16-bhava-wellbeing-by-lord-state.step-001:lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：该宫之主（Bhava's Lord）是否处于 Prabuddhavastha。"}, {"when": {"fact_key": "本盘该宫（Bhava）之主是哪颗行星"}, "required_fact_keys": ["该宫之主（Bhava's Lord）是否处于 Kismaravastha"], "branch_condition_logic": {"fact_key": "该宫之主（Bhava's Lord）是否处于 Kismaravastha"}, "selection_group": "ch11-v14-16-bhava-wellbeing-by-lord-state.step-001:lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：该宫之主（Bhava's Lord）是否处于 Kismaravastha。"}, {"when": {"fact_key": "本盘该宫（Bhava）之主是哪颗行星"}, "required_fact_keys": ["该宫之主（Bhava's Lord）是否落十宫（Karm Bhava）"], "branch_condition_logic": {"fact_key": "该宫之主（Bhava's Lord）是否落十宫（Karm Bhava）"}, "selection_group": "ch11-v14-16-bhava-wellbeing-by-lord-state.step-001:lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：该宫之主（Bhava's Lord）是否落十宫（Karm Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 Yuvavastha、Prabuddhavastha、Kismaravastha 自行等同于第 45 章的任何一种 Avastha——原文没有作这个对应。", "不得把「安泰」具体化成某一件事或某个程度。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘该宫（Bhava）之主是哪颗行星。
- 缺失即停字段：["本盘该宫（Bhava）之主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch11:v14-16`｜PDF [26]｜“Also, when its Lord is in Yuvavastha, or Prabuddhavastha, or in Kismaravastha, or in Karm Bhava, the Bhavas well-being is indicated.”


## 四路查书计划

### 支持路

- Also, when its Lord is in Yuvavastha, or Prabuddhavastha, or in Kismaravastha, or in Karm Bhava, the Bhavas well-being is indicated
- 宫主处于 Yuvavastha 或落十宫 该宫安泰

### 反例或取消路

- The Bhava, which is not drishtied by its Lord, or, whose Lord is with a malefic Grah

### 适用边界路

- The learned should estimate the effects, due to a Bhava, in the manner, cited above, after ascertaining the strength and weakness
- 本译本未界定 Yuvavastha、Prabuddhavastha、Kismaravastha

### 判断方法路

- the Avasthas, or states of the Grahas are to be considered in the context of the effects of the Grahas
- Infant, youthful, adolescent, old and dead are the states of the Grahas
- The Lord of the Bhava is equally important, when estimating the indications of a particular Bhava
- 行星的 Avastha 怎么定

## 上游问题

- 无

## 停止条件

- 缺少该宫之主是哪颗行星的事实时停止。
- Yuvavastha、Prabuddhavastha、Kismaravastha 三名在本译本未获界定，取不到值即停止。
- 四个分支的事实全部取不到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
