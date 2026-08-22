---
method: ch11-v14-16-bhava-lord-in-declining-avastha
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 宫之毁灭一侧：该宫之主处于 Vriddhavastha、Mritavastha、Suptavastha 之一

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 宫主处在衰败状态怎么看
- 我这一宫会不会受损

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘该宫（Bhava）之主是哪颗行星

## 按情况检查的事实

- 该宫之主（Bhava's Lord）是否处于 Vriddhavastha
- 该宫之主（Bhava's Lord）是否处于 Mritavastha
- 该宫之主（Bhava's Lord）是否处于 Suptavastha

## 依赖方法

- 无

## 执行步骤

### ch11-v14-16-bhava-lord-in-declining-avastha.step-001

- 动作：核对该宫之主（Bhava's Lord）是否处于 Vriddhavastha、Mritavastha、Suptavastha 三种状态之一。
- 适用范围：适用于十二宫中任一宫；主语承本偈「whose Lord」——Avastha 是行星的状态；本译本末句只列条件、没有谓语，结果词只取自本偈标题「Prosperity, or Annihilation of a Bhava」；本偈也没有界定这三个状态名，未确定即停判。
- 原文最小意思：该宫之主处于 Vriddhavastha、Mritavastha、Suptavastha 三种状态之一时，属本偈标题所说的宫之毁灭（Annihilation of a Bhava）一侧。
- 本步骤产出事实：["宫主处于衰败状态的毁灭一侧判定"]
- 所需事实：["本盘该宫（Bhava）之主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘该宫（Bhava）之主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "该宫之主（Bhava's Lord）是否处于 Vriddhavastha"}, {"fact_key": "该宫之主（Bhava's Lord）是否处于 Mritavastha"}, {"fact_key": "该宫之主（Bhava's Lord）是否处于 Suptavastha"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘该宫（Bhava）之主是哪颗行星"}, "required_fact_keys": ["该宫之主（Bhava's Lord）是否处于 Vriddhavastha"], "branch_condition_logic": {"fact_key": "该宫之主（Bhava's Lord）是否处于 Vriddhavastha"}, "selection_group": "ch11-v14-16-bhava-lord-in-declining-avastha.step-001:declining-avastha", "stop_condition": "选中该分支后，缺少以下事实即停止：该宫之主（Bhava's Lord）是否处于 Vriddhavastha。"}, {"when": {"fact_key": "本盘该宫（Bhava）之主是哪颗行星"}, "required_fact_keys": ["该宫之主（Bhava's Lord）是否处于 Mritavastha"], "branch_condition_logic": {"fact_key": "该宫之主（Bhava's Lord）是否处于 Mritavastha"}, "selection_group": "ch11-v14-16-bhava-lord-in-declining-avastha.step-001:declining-avastha", "stop_condition": "选中该分支后，缺少以下事实即停止：该宫之主（Bhava's Lord）是否处于 Mritavastha。"}, {"when": {"fact_key": "本盘该宫（Bhava）之主是哪颗行星"}, "required_fact_keys": ["该宫之主（Bhava's Lord）是否处于 Suptavastha"], "branch_condition_logic": {"fact_key": "该宫之主（Bhava's Lord）是否处于 Suptavastha"}, "selection_group": "ch11-v14-16-bhava-lord-in-declining-avastha.step-001:declining-avastha", "stop_condition": "选中该分支后，缺少以下事实即停止：该宫之主（Bhava's Lord）是否处于 Suptavastha。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文补出毁灭的程度、事项或应期——本译本末句没有谓语。", "不得把 Suptavastha 自行等同于第 45 章的任何一种 Avastha——本书没有作这个对应。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘该宫（Bhava）之主是哪颗行星。
- 缺失即停字段：["本盘该宫（Bhava）之主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch11:v14-16`｜PDF [26]｜“Prosperity, or Annihilation of a Bhava.”
  - `bphs-97:santhanam:ch11:v14-16`｜PDF [26]｜“is in one of the three Avasthas, viz, Vriddhavastha, Mritavastha and Suptavastha”


## 四路查书计划

### 支持路

- or is in one of the three Avasthas, viz, Vriddhavastha, Mritavastha and Suptavastha
- 宫主处于衰败 Avastha 宫之毁灭

### 反例或取消路

- Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic

### 适用边界路

- The learned should estimate the effects, due to a Bhava, in the manner, cited above, after ascertaining the strength and weakness
- 本偈末句在本译本没有谓语

### 判断方法路

- the Avasthas, or states of the Grahas are to be considered in the context of the effects of the Grahas
- Infant, youthful, adolescent, old and dead are the states of the Grahas
- The Lord of the Bhava is equally important, when estimating the indications of a particular Bhava
- 行星的 Avastha 怎么定

## 上游问题

- 无

## 停止条件

- 缺少该宫之主是哪颗行星的事实时停止。
- 三个 Avastha 分支的事实全部取不到时停止（本偈未界定这三个状态名）。
- 要断出毁灭的具体后果时停止——原文末句无谓语。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
