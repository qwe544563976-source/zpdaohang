---
method: ch16-v11-adopted-issue-six-grahas
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 养子女：五宫聚六星、五宫主落十二宫、月亮与上升有力

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会领养孩子
- 我的孩子会不会不是自己生的

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 第五宫（Putr）内是否有六颗行星
- 五宫主是否落在第十二宫（Vyaya Bhava）
- 月亮（Chandra）与上升（Lagn）是否都有力量

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch16-v11-adopted-issue-six-grahas.step-001

- 动作：数清第五宫内的行星是否达到六颗，核对五宫主是否落第十二宫，并核对月亮与上升是否有力。
- 适用范围：仅限本命盘领养子女主题；原文只给这一组条件，未给领养时间、人数或性别。
- 原文最小意思：五宫（Putr）中有六颗行星、五宫主落十二宫（Vyaya Bhava）、且月亮（Chandra）与上升（Lagn）都有力时，主养子女。
- 本步骤产出事实：["五宫聚六星养子女判定"]
- 所需事实：["第五宫（Putr）内是否有六颗行星", "五宫主是否落在第十二宫（Vyaya Bhava）", "月亮（Chandra）与上升（Lagn）是否都有力量"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "第五宫（Putr）内是否有六颗行星"}, {"fact_key": "五宫主是否落在第十二宫（Vyaya Bhava）"}, {"fact_key": "月亮（Chandra）与上升（Lagn）是否都有力量"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把六颗行星放宽成五颗或更少。", "不得据此推断领养的时间或子女人数。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：第五宫（Putr）内是否有六颗行星、五宫主是否落在第十二宫（Vyaya Bhava）、月亮（Chandra）与上升（Lagn）是否都有力量。
- 缺失即停字段：["第五宫（Putr）内是否有六颗行星", "五宫主是否落在第十二宫（Vyaya Bhava）", "月亮（Chandra）与上升（Lagn）是否都有力量"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v11`｜PDF [31]｜“Adopted issue is indicated, if Putr is tenanted by six Grahas, while its Lord is in Vyaya Bhava and Chandra and Lagn are endowed with strength.”


## 四路查书计划

### 支持路

- Putr tenanted by six Grahas Lord in Vyaya Chandra Lagn strength adopted issue
- 五宫六颗行星 五宫主落十二宫 月亮上升有力 养子女

### 反例或取消路

- Putr Bhava strong lord own children
- 五宫主有力 亲生子女 反例

### 适用边界路

- six Grahas in Putr requirement boundary
- 五宫聚六星条件的适用边界

### 判断方法路

- how to count Grahas tenanting Putr Bhava
- 怎样数第五宫里的行星数量

## 上游问题

- 无

## 停止条件

- 缺少第五宫内行星数量事实时停止。
- 缺少五宫主落宫或月亮上升力量事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
