---
method: ch16-v15-born-of-others-loins
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 出自他人血脉：月亮落上升起第8宫、木星落月亮起第8宫并有凶星相照或同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的出身有没有问题
- 我是不是亲生的这件事星盘怎么说

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮是否落上升起第8宫
- 木星是否落月亮起第8宫

## 按情况检查的事实

- 该组合是否受凶星相照
- 该组合是否与凶星同宫

## 依赖方法

- 无

## 执行步骤

### ch16-v15-born-of-others-loins.step-001

- 动作：核对月亮相对上升的宫位、木星相对月亮的宫位，再核对该组合是否有凶星相照或与凶星同宫，判断此人是否出自他人血脉。
- 适用范围：仅限本命出身血脉主题；原文只要求本条所述凶星相照或同宫，未给时间或大运限定。
- 原文最小意思：月亮落上升起第8宫、木星落月亮起第8宫，且有凶星相照或与凶星同宫时，此人出自他人血脉。
- 本步骤产出事实：["出自他人血脉判定"]
- 所需事实：["月亮是否落上升起第8宫", "木星是否落月亮起第8宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "月亮是否落上升起第8宫"}, {"fact_key": "木星是否落月亮起第8宫"}]}, {"operator": "OR", "operands": [{"fact_key": "该组合是否受凶星相照"}, {"fact_key": "该组合是否与凶星同宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "月亮是否落上升起第8宫"}, {"fact_key": "木星是否落月亮起第8宫"}]}, "required_fact_keys": ["该组合是否受凶星相照"], "branch_condition_logic": {"fact_key": "该组合是否受凶星相照"}, "selection_group": "ch16-v15-born-of-others-loins.step-001:malefic-link", "stop_condition": "选中该分支后，缺少以下事实即停止：该组合是否受凶星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮是否落上升起第8宫"}, {"fact_key": "木星是否落月亮起第8宫"}]}, "required_fact_keys": ["该组合是否与凶星同宫"], "branch_condition_logic": {"fact_key": "该组合是否与凶星同宫"}, "selection_group": "ch16-v15-born-of-others-loins.step-001:malefic-link", "stop_condition": "选中该分支后，缺少以下事实即停止：该组合是否与凶星同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["没有凶星相照或同宫时不得下此断语。", "不得据此推断父母姓名、婚姻状况或具体年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮是否落上升起第8宫、木星是否落月亮起第8宫。
- 缺失即停字段：["月亮是否落上升起第8宫", "木星是否落月亮起第8宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v15`｜PDF [31]｜“Undoubtedly the native is born of other’s loins, if Chandra is in the 8<sup>th</sup> from Lagna, while Guru is in the 8<sup>th</sup> from Chandra. Malefic’s Drishti, or Yuti is essential in this Yog.”


## 四路查书计划

### 支持路

- 月亮落上升第8宫 木星落月亮第8宫 出自他人血脉

### 反例或取消路

- 无凶星相照或同宫 该瑜伽不成立

### 适用边界路

- 凶星相照或同宫作为必要条件的边界

### 判断方法路

- 判断出身血脉要看哪些组合

## 上游问题

- 无

## 停止条件

- 缺少月亮相对上升宫位事实时停止。
- 缺少木星相对月亮宫位事实时停止。
- 缺少凶星相照与同宫两项分支事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
