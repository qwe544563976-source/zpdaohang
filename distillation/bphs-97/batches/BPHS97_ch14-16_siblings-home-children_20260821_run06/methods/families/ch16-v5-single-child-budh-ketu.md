---
method: ch16-v5-single-child-budh-ketu
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 只生一子：五宫主落陷于六八十二宫且水星与计都在五宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会有几个孩子
- 我是不是只能生一个

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫主是否处于落陷状态
- 水星（Budh）与计都（Ketu）是否同在第五宫

## 按情况检查的事实

- 五宫主是否落陷于第六宫（Ari Bhava）
- 五宫主是否落陷于第八宫（Randhr Bhava）
- 五宫主是否落陷于第十二宫（Vyaya Bhava）

## 依赖方法

- 无

## 执行步骤

### ch16-v5-single-child-budh-ketu.step-001

- 动作：核对五宫主是否落陷、落在第六第八或第十二宫，并核对水星与计都是否同在第五宫。
- 适用范围：仅限本命盘子女人数主题；原文以男命之妻的生育立说，未给出生年份或性别。
- 原文最小意思：五宫主落陷于六宫、八宫或十二宫，同时水星（Budh）与计都（Ketu）都在五宫（Putr Bhava）时，妻子只生一个孩子。
- 本步骤产出事实：["落陷五宫主配水星计都独子判定"]
- 所需事实：["五宫主是否处于落陷状态", "水星（Budh）与计都（Ketu）是否同在第五宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "五宫主是否处于落陷状态"}, {"fact_key": "水星（Budh）与计都（Ketu）是否同在第五宫"}]}, {"operator": "OR", "operands": [{"fact_key": "五宫主是否落陷于第六宫（Ari Bhava）"}, {"fact_key": "五宫主是否落陷于第八宫（Randhr Bhava）"}, {"fact_key": "五宫主是否落陷于第十二宫（Vyaya Bhava）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "五宫主是否处于落陷状态"}, {"fact_key": "水星（Budh）与计都（Ketu）是否同在第五宫"}]}, "required_fact_keys": ["五宫主是否落陷于第六宫（Ari Bhava）"], "branch_condition_logic": {"fact_key": "五宫主是否落陷于第六宫（Ari Bhava）"}, "selection_group": "ch16-v5-single-child-budh-ketu.step-001:fall-house", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落陷于第六宫（Ari Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "五宫主是否处于落陷状态"}, {"fact_key": "水星（Budh）与计都（Ketu）是否同在第五宫"}]}, "required_fact_keys": ["五宫主是否落陷于第八宫（Randhr Bhava）"], "branch_condition_logic": {"fact_key": "五宫主是否落陷于第八宫（Randhr Bhava）"}, "selection_group": "ch16-v5-single-child-budh-ketu.step-001:fall-house", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落陷于第八宫（Randhr Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "五宫主是否处于落陷状态"}, {"fact_key": "水星（Budh）与计都（Ketu）是否同在第五宫"}]}, "required_fact_keys": ["五宫主是否落陷于第十二宫（Vyaya Bhava）"], "branch_condition_logic": {"fact_key": "五宫主是否落陷于第十二宫（Vyaya Bhava）"}, "selection_group": "ch16-v5-single-child-budh-ketu.step-001:fall-house", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落陷于第十二宫（Vyaya Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断这个孩子的性别或出生年份。", "不得把只生一个改写成无子或多子。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否处于落陷状态、水星（Budh）与计都（Ketu）是否同在第五宫。
- 缺失即停字段：["五宫主是否处于落陷状态", "水星（Budh）与计都（Ketu）是否同在第五宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v5`｜PDF [30]｜“Should Putr’s Lord be in fall in Ari, Randhr, or Vyaya Bhava, while Budh and Ketu are in Putr Bhava, the native’s wife will give birth to one child only.”


## 四路查书计划

### 支持路

- 五宫主落陷 水星计都在五宫 只生一子

### 反例或取消路

- 五宫主有力 子女众多 反例

### 适用边界路

- 只生一子断语的适用边界

### 判断方法路

- 怎样查五宫主是否落陷

## 上游问题

- 无

## 停止条件

- 缺少五宫主落陷与落宫事实时停止。
- 缺少水星与计都落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
