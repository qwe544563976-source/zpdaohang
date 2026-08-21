---
method: ch17-v7-blood-leprosy
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 血麻风：月亮落上升宫（非巨蟹座）并与火星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会得麻风一类的重皮肤病
- 月亮与火星同宫在上升会怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否落上升宫（Lagna）
- 本盘上升（Lagna）所在星座是否为巨蟹座（Cancer）
- 月亮（Chandra）是否与火星（Mangal）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v7-blood-leprosy.step-001

- 动作：核对月亮（Chandra）是否落上升宫、上升星座是否为巨蟹座，以及月亮与火星的同宫。
- 适用范围：仅限本命盘麻风种类主题；原文明确排除巨蟹座上升，未给时间限定。
- 原文最小意思：月亮落上升宫、且该上升星座不是巨蟹座、又与火星同宫时，会有血麻风。
- 本步骤产出事实：["月亮上升与火星同宫的麻风种类判定"]
- 所需事实：["月亮（Chandra）是否落上升宫（Lagna）", "本盘上升（Lagna）所在星座是否为巨蟹座（Cancer）", "月亮（Chandra）是否与火星（Mangal）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落上升宫（Lagna）"}, {"operator": "NOT", "operands": [{"fact_key": "本盘上升（Lagna）所在星座是否为巨蟹座（Cancer）"}]}, {"fact_key": "月亮（Chandra）是否与火星（Mangal）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断发病年龄、轻重或可治与否。", "不得在上升为巨蟹座时套用本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否落上升宫（Lagna）、本盘上升（Lagna）所在星座是否为巨蟹座（Cancer）、月亮（Chandra）是否与火星（Mangal）同宫。
- 缺失即停字段：["月亮（Chandra）是否落上升宫（Lagna）", "本盘上升（Lagna）所在星座是否为巨蟹座（Cancer）", "月亮（Chandra）是否与火星（Mangal）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v7-8.5`｜PDF [32]｜“If Chandra is in Lagna, which is not however Cancer”
  - `bphs-97:santhanam:ch17:v7-8.5`｜PDF [32]｜“Mangal similarly will afflict one with bloodleprosy”


## 四路查书计划

### 支持路

- 月亮落上升 火星同宫 会有血麻风

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age

### 判断方法路

- 判断麻风种类应看月亮与哪颗行星同宫

## 上游问题

- 无

## 停止条件

- 缺少月亮落宫事实时停止。
- 缺少上升星座事实时停止。
- 缺少月亮与火星同宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
