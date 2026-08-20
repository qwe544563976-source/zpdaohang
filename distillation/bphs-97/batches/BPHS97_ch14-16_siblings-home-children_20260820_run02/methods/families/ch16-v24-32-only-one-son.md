---
method: ch16-v24-32-only-one-son
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 只主一子：五宫有凶星且木土互在对方起第5宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我是不是只能有一个孩子
- 我子女会不会很少

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫是否有凶星占据

## 按情况检查的事实

- 木星是否落土星起第5宫
- 土星是否落木星起第5宫

## 依赖方法

- 无

## 执行步骤

### ch16-v24-32-only-one-son.step-001

- 动作：核对五宫是否有凶星，并核对木星与土星是否互在对方起第5宫，判断是否只主一个儿子。
- 适用范围：仅限本命五宫儿子数量主题；原文只给只主一子这一个结论，未给时间或上升限定。
- 原文最小意思：五宫中有凶星，且木星落土星起第5宫或土星落木星起第5宫时，只主一个儿子。
- 本步骤产出事实：["独子判定"]
- 所需事实：["五宫是否有凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫是否有凶星占据"}, {"operator": "OR", "operands": [{"fact_key": "木星是否落土星起第5宫"}, {"fact_key": "土星是否落木星起第5宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "五宫是否有凶星占据"}, "required_fact_keys": ["木星是否落土星起第5宫"], "branch_condition_logic": {"fact_key": "木星是否落土星起第5宫"}, "selection_group": "ch16-v24-32-only-one-son.step-001:guru-shani-fifth", "stop_condition": "选中该分支后，缺少以下事实即停止：木星是否落土星起第5宫。"}, {"when": {"fact_key": "五宫是否有凶星占据"}, "required_fact_keys": ["土星是否落木星起第5宫"], "branch_condition_logic": {"fact_key": "土星是否落木星起第5宫"}, "selection_group": "ch16-v24-32-only-one-son.step-001:guru-shani-fifth", "stop_condition": "选中该分支后，缺少以下事实即停止：土星是否落木星起第5宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把只主一子扩大成子女总数或女儿数量的断语。", "不得据此推断该子出生的年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫是否有凶星占据。
- 缺失即停字段：["五宫是否有凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v24-32`｜PDF [31, 32]｜“Only one son is denoted, if there be a malefic in Putr Bhava, while Guru is in the 5<sup>th</sup> from Shani, or vice versa.”


## 四路查书计划

### 支持路

- Only one son is denoted malefic in Putr Bhava Guru 5th from Shani
- 五宫有凶星 木星土星互在第5宫 只主一子

### 反例或取消路

- Putr’s Lord in deep exaltation many sons
- 五宫主深度入庙 子女众多

### 适用边界路

- one son only rule scope Putr Bhava
- 只主一子断语的适用边界

### 判断方法路

- how to judge a single child yoga from Putr Bhava
- 判断独子组合要检查什么

## 上游问题

- 无

## 停止条件

- 缺少五宫内凶星占据事实时停止。
- 缺少木星与土星相对位置事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
