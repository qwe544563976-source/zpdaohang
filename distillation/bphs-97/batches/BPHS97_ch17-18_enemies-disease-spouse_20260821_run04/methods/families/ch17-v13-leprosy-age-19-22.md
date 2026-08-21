---
method: ch17-v13-leprosy-age-19-22
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第19岁与第22岁的麻风：月亮落人马座或双鱼座、木星落上升起第六宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我二十岁上下健康会不会出事
- 月亮在人马或双鱼会怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘月亮（Chandra）落在哪个星座
- 木星（Guru）是否落上升起第六宫（Ari）

## 按情况检查的事实

- 月亮（Chandra）是否落人马座（Dhanu）
- 月亮（Chandra）是否落双鱼座（Meen）

## 依赖方法

- 无

## 执行步骤

### ch17-v13-leprosy-age-19-22.step-001

- 动作：核对月亮所落星座与木星是否落上升起第六宫。
- 适用范围：仅限本命盘麻风主题；原文明确从上升起算第六宫，未说明麻风种类。
- 原文最小意思：月亮落人马座或双鱼座、木星落上升起第六宫时，第19岁与第22岁会患麻风。
- 本步骤产出事实：["月亮星座与木星六宫的麻风判定"]
- 所需事实：["木星（Guru）是否落上升起第六宫（Ari）", "本盘月亮（Chandra）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘月亮（Chandra）落在哪个星座"}, {"fact_key": "木星（Guru）是否落上升起第六宫（Ari）"}]}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否落人马座（Dhanu）"}, {"fact_key": "月亮（Chandra）是否落双鱼座（Meen）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘月亮（Chandra）落在哪个星座"}, {"fact_key": "木星（Guru）是否落上升起第六宫（Ari）"}]}, "required_fact_keys": ["月亮（Chandra）是否落人马座（Dhanu）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落人马座（Dhanu）"}, "selection_group": "ch17-v13-leprosy-age-19-22.step-001:chandra-sign", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落人马座（Dhanu）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘月亮（Chandra）落在哪个星座"}, {"fact_key": "木星（Guru）是否落上升起第六宫（Ari）"}]}, "required_fact_keys": ["月亮（Chandra）是否落双鱼座（Meen）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落双鱼座（Meen）"}, "selection_group": "ch17-v13-leprosy-age-19-22.step-001:chandra-sign", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落双鱼座（Meen）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把本条的年龄推广到其他年份。", "不得据此判定麻风的种类。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落上升起第六宫（Ari）、本盘月亮（Chandra）落在哪个星座。
- 缺失即停字段：["木星（Guru）是否落上升起第六宫（Ari）", "本盘月亮（Chandra）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v13-19.5`｜PDF [32, 33]｜“If the Chandra is in Dhanu/Meen, while Guru is in Ari from Lagna, one will suffer from leprosy at the age of 19 and 22.”


## 四路查书计划

### 支持路

- If the Chandra is in Dhanu/Meen, while Guru is in Ari from Lagna leprosy at the age of 19 and 22
- 月亮人马 双鱼 木星六宫 麻风 19岁 22岁

### 反例或取消路

- Guru in similar case will destroy any disease
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age

### 判断方法路

- 判断麻风应检查月亮星座与木星落宫

## 上游问题

- 无

## 停止条件

- 缺少月亮所落星座事实时停止。
- 缺少木星落上升起第六宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
