---
method: ch16-v7-progeny-after-ordeal
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 求子艰辛：九宫主落上升、五宫主落陷、计都与水星在五宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我求子会不会很辛苦
- 我要经历多少折腾才能有孩子

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主是否落在上升（Lagna）
- 五宫主是否处于落陷状态
- 计都（Ketu）与水星（Budh）是否同在第五宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch16-v7-progeny-after-ordeal.step-001

- 动作：核对九宫主是否落上升、五宫主是否落陷，并核对计都与水星是否同在第五宫。
- 适用范围：仅限本命盘得子难易主题；原文只说得子前有极大磨难，未给年份、年龄或子女人数。
- 原文最小意思：九宫主落上升（Lagna）、五宫主落陷、且计都（Ketu）与水星（Budh）同在五宫（Putr）时，要历经极大磨难才能得到子嗣。
- 本步骤产出事实：["九宫主落上升配落陷五宫主求子磨难判定"]
- 所需事实：["九宫主是否落在上升（Lagna）", "五宫主是否处于落陷状态", "计都（Ketu）与水星（Budh）是否同在第五宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主是否落在上升（Lagna）"}, {"fact_key": "五宫主是否处于落陷状态"}, {"fact_key": "计都（Ketu）与水星（Budh）是否同在第五宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把“极大磨难”坐实成某种疾病、手术或治疗。", "不得据此推断得子的年龄或年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主是否落在上升（Lagna）、五宫主是否处于落陷状态、计都（Ketu）与水星（Budh）是否同在第五宫。
- 缺失即停字段：["九宫主是否落在上升（Lagna）", "五宫主是否处于落陷状态", "计都（Ketu）与水星（Budh）是否同在第五宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v7`｜PDF [30]｜“Should Dharm’s Lord be in Lagna, while Putr’s Lord is in fall and Ketu is in Putr along with Budh, obtainment of progeny will be after a great deal of ordeal.”


## 四路查书计划

### 支持路

- Dharm’s Lord in Lagna Putr’s Lord in fall Ketu Budh progeny ordeal
- 九宫主落上升 五宫主落陷 计都水星在五宫 求子艰难

### 反例或取消路

- Putr’s Lord strong early obtainment of children
- 五宫主有力 早得子 反例

### 适用边界路

- ordeal before progeny rule scope
- 求子磨难断语的适用边界

### 判断方法路

- how to check Dharm’s Lord position in Lagna
- 怎样查九宫主是否落在上升

## 上游问题

- 无

## 停止条件

- 缺少九宫主落宫事实时停止。
- 缺少五宫主落陷或计都水星落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
