---
method: ch16-v6-single-child-shani-budh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 只生一子：五宫主落陷不照五宫且土星与水星在五宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我只能生一个孩子吗
- 我家会有几个小孩

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫主是否处于落陷状态
- 五宫主是否不与第五宫形成相照
- 土星（Shani）与水星（Budh）是否同在第五宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch16-v6-single-child-shani-budh.step-001

- 动作：核对五宫主是否落陷、是否不照第五宫，并核对土星与水星是否同在第五宫。
- 适用范围：仅限本命盘子女人数主题；原文以男命之妻的生育立说，未给出生年份或性别。
- 原文最小意思：五宫主落陷、且不与五宫（Putr）相照，同时土星（Shani）与水星（Budh）都在五宫时，妻子只生一个孩子。
- 本步骤产出事实：["落陷不照五宫配土星水星独子判定"]
- 所需事实：["五宫主是否处于落陷状态", "五宫主是否不与第五宫形成相照", "土星（Shani）与水星（Budh）是否同在第五宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫主是否处于落陷状态"}, {"fact_key": "五宫主是否不与第五宫形成相照"}, {"fact_key": "土星（Shani）与水星（Budh）是否同在第五宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断这个孩子的性别或出生年份。", "不得把不照五宫扩大成五宫全无吉星相照。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否处于落陷状态、五宫主是否不与第五宫形成相照、土星（Shani）与水星（Budh）是否同在第五宫。
- 缺失即停字段：["五宫主是否处于落陷状态", "五宫主是否不与第五宫形成相照", "土星（Shani）与水星（Budh）是否同在第五宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v6`｜PDF [30]｜“If Putr’s Lord is in fall and be not in Drishti to Putr, while Shani and Budh are in Putr, the native’s wife will give birth to one child only.”


## 四路查书计划

### 支持路

- Putr’s Lord in fall not in Drishti to Putr Shani Budh one child
- 五宫主落陷 不照五宫 土星水星在五宫 只生一子

### 反例或取消路

- Putr drishtied by strong Guru many children
- 五宫受木星相照 多子 反例

### 适用边界路

- drishti to Putr condition boundary one child rule
- 五宫相照条件的适用边界

### 判断方法路

- how to check drishti between Putr Lord and Putr Bhava
- 怎样判断五宫主与五宫之间有没有相照

## 上游问题

- 无

## 停止条件

- 缺少五宫主落陷事实时停止。
- 缺少五宫相照与土星水星落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
