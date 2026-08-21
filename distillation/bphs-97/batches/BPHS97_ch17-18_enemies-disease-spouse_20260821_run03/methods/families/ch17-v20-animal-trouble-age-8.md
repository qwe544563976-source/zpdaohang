---
method: ch17-v20-animal-trouble-age-8
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第8岁受动物侵扰：月亮与六宫主同宫、八宫主落六宫、十二宫主落上升宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 孩子八岁前后会不会被动物伤到
- 小时候有没有意外伤害

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否与六宫主（Ari's Lord）同宫
- 八宫主（Randhr's Lord）是否落六宫（Ari）
- 十二宫主（Vyaya's Lord）是否落上升宫（Lagna）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v20-animal-trouble-age-8.step-001

- 动作：核对月亮与六宫主的同宫、八宫主与十二宫主的落宫。
- 适用范围：仅限本命盘第8岁的动物之厄；原文未说明是哪一类动物，也未说明伤害轻重。
- 原文最小意思：月亮与六宫主同宫、八宫主落六宫、十二宫主落上升宫时，第8岁会受动物侵扰。
- 本步骤产出事实：["第8岁动物之厄判定"]
- 所需事实：["月亮（Chandra）是否与六宫主（Ari's Lord）同宫", "八宫主（Randhr's Lord）是否落六宫（Ari）", "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与六宫主（Ari's Lord）同宫"}, {"fact_key": "八宫主（Randhr's Lord）是否落六宫（Ari）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断动物种类、伤害部位或致死与否。", "不得把第8岁推广到其他年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否与六宫主（Ari's Lord）同宫、八宫主（Randhr's Lord）是否落六宫（Ari）、十二宫主（Vyaya's Lord）是否落上升宫（Lagna）。
- 缺失即停字段：["月亮（Chandra）是否与六宫主（Ari's Lord）同宫", "八宫主（Randhr's Lord）是否落六宫（Ari）", "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v20-22`｜PDF [33]｜“Should Chandra be yuti with Ari Lord, while the 8<sup>th</sup> Lord is in Ari and the 12<sup>th</sup> Lord is in Lagna, the native will be troubled by animals at the age of eight.”


## 四路查书计划

### 支持路

- Should Chandra be yuti with Ari Lord troubled by animals at the age of eight
- 月亮六宫主同宫 八宫主落六宫 八岁 动物

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed
- Lagn Lord is singly capable of counteracting all evils

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age
- Short-life Combinations Chandra in Ari, Randhr, or Vyaya Bhava

### 判断方法路

- Indications of Ari Bhava enemies doubts about death
- 判断童年凶年应检查哪些宫主

## 上游问题

- 无

## 停止条件

- 缺少月亮与六宫主同宫事实时停止。
- 缺少八宫主落六宫事实时停止。
- 缺少十二宫主落上升宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
