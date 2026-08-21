---
method: ch15-v4-beautiful-mansions
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 华美宅第：十宫主与四宫主在角宫或三角宫会合

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能不能住上好房子
- 我会不会有豪宅

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm’s Lord）是否与四宫主（Bandhu’s Lord）会合

## 按情况检查的事实

- 十宫主与四宫主的会合处是否为角宫
- 十宫主与四宫主的会合处是否为三角宫

## 依赖方法

- 无

## 执行步骤

### ch15-v4-beautiful-mansions.step-001

- 动作：核对十宫主（Karm’s Lord）与四宫主（Bandhu’s Lord）是否会合，并核对会合处是角宫还是三角宫。
- 适用范围：仅限十宫主与四宫主会合于角宫或三角宫这一组合与宅第结果；原文未给时间限定。
- 原文最小意思：十宫主（Karm’s Lord）与四宫主（Bandhu’s Lord）在角宫、或在三角宫会合时，命主将获得华美的宅第。
- 本步骤产出事实：["华美宅第判定"]
- 所需事实：["十宫主（Karm’s Lord）是否与四宫主（Bandhu’s Lord）会合"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm’s Lord）是否与四宫主（Bandhu’s Lord）会合"}, {"operator": "OR", "operands": [{"fact_key": "十宫主与四宫主的会合处是否为角宫"}, {"fact_key": "十宫主与四宫主的会合处是否为三角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "十宫主（Karm’s Lord）是否与四宫主（Bandhu’s Lord）会合"}, "required_fact_keys": ["十宫主与四宫主的会合处是否为角宫"], "branch_condition_logic": {"fact_key": "十宫主与四宫主的会合处是否为角宫"}, "selection_group": "ch15-v4-beautiful-mansions.step-001:join-place", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主与四宫主的会合处是否为角宫。"}, {"when": {"fact_key": "十宫主（Karm’s Lord）是否与四宫主（Bandhu’s Lord）会合"}, "required_fact_keys": ["十宫主与四宫主的会合处是否为三角宫"], "branch_condition_logic": {"fact_key": "十宫主与四宫主的会合处是否为三角宫"}, "selection_group": "ch15-v4-beautiful-mansions.step-001:join-place", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主与四宫主的会合处是否为三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断宅第的数量、地点或取得年份。", "不得把角宫、三角宫以外的位置也算作成立条件。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm’s Lord）是否与四宫主（Bandhu’s Lord）会合。
- 缺失即停字段：["十宫主（Karm’s Lord）是否与四宫主（Bandhu’s Lord）会合"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v4`｜PDF [29]｜“If Karm’s Lord joins Bandhu’s Lord in an angle, or in a trine, the native will acquire beautiful mansions.”


## 四路查书计划

### 支持路

- Karm’s Lord joins Bandhu’s Lord angle trine beautiful mansions
- 十宫主 四宫主 会合 角宫 三角宫 宅第

### 反例或取消路

- Bandhu’s Lord in dusthana loss of house
- 四宫主受克 无好房子

### 适用边界路

- angle and trine definition for this combination
- 角宫三角宫会合规则的适用边界

### 判断方法路

- how to judge acquisition of mansions in BPHS
- 判断能否得好房子要查什么

## 上游问题

- 无

## 停止条件

- 缺少十宫主与四宫主是否会合的事实时停止。
- 缺少会合处是角宫还是三角宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
