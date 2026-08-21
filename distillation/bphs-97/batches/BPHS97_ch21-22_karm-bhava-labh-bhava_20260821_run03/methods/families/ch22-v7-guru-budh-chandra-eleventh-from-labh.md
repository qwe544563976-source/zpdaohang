---
method: ch22-v7-guru-budh-chandra-eleventh-from-labh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 财富谷物与钻石饰物：木星、水星与月亮同落从十一宫起算的第十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有田产珠宝这类家业
- 木星水星月亮聚在一处是什么效果

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否落从十一宫（Labh）起算的第十一宫
- 水星（Budh）是否落从十一宫（Labh）起算的第十一宫
- 月亮（Chandra）是否落从十一宫（Labh）起算的第十一宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch22-v7-guru-budh-chandra-eleventh-from-labh.step-001

- 动作：核对木星（Guru）、水星（Budh）与月亮（Chandra）是否都落在从十一宫（Labh）起算的第十一宫。
- 适用范围：仅限本命盘十一宫（Labh）收获主题；起算点是十一宫本身而不是上升宫，三颗行星须同落该宫；原文未给数额与应期。
- 原文最小意思：木星、水星与月亮同落从十一宫起算的第十一宫时，本人拥有财富、谷物、财运、钻石、饰物等。
- 本步骤产出事实：["木星水星月亮落从十一宫起算第十一宫判定"]
- 所需事实：["木星（Guru）是否落从十一宫（Labh）起算的第十一宫", "水星（Budh）是否落从十一宫（Labh）起算的第十一宫", "月亮（Chandra）是否落从十一宫（Labh）起算的第十一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落从十一宫（Labh）起算的第十一宫"}, {"fact_key": "水星（Budh）是否落从十一宫（Labh）起算的第十一宫"}, {"fact_key": "月亮（Chandra）是否落从十一宫（Labh）起算的第十一宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「从十一宫起算的第十一宫」改成从上升宫起算的第十一宫。", "不得只凭三颗行星中的一颗或两颗落该宫就下断。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落从十一宫（Labh）起算的第十一宫、水星（Budh）是否落从十一宫（Labh）起算的第十一宫、月亮（Chandra）是否落从十一宫（Labh）起算的第十一宫。
- 缺失即停字段：["木星（Guru）是否落从十一宫（Labh）起算的第十一宫", "水星（Budh）是否落从十一宫（Labh）起算的第十一宫", "月亮（Chandra）是否落从十一宫（Labh）起算的第十一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch22:v7`｜PDF [39]｜“Should Guru, Budh and Chandra be in the 11<sup>th</sup> from Labh, the native will be endowed with wealth, grains, fortunes, diamonds, ornaments etc.”


## 四路查书计划

### 支持路

- Should Guru, Budh and Chandra be in the 11th from Labh, the native will be endowed with wealth, grains, fortunes, diamonds, ornaments etc
- 木星（Guru） 水星（Budh） 月亮（Chandra） 从十一宫（Labh）起算第十一宫 财富 谷物 钻石

### 反例或取消路

- There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic
- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic

### 适用边界路

- Just as these effects are derived from Tanu Bhava in regard to the native, similar deductions be made about co-borns etc. from Sahaj and other Bhavas
- Sahaj, Ari, Karm and Labh Bhava are Upachaya Bhavas

### 判断方法路

- If Labh’s Lord is in Labh Bhava, the native will gain in all his undertakings, while his learning and happiness will be on the increase day by day
- Should Simh be Putr Bhava and be occupied by Surya himself, as Shani, Chandra and Guru are in Labh Bhava, the native will be very affluent

## 上游问题

- 无

## 停止条件

- 缺少木星落宫事实时停止。
- 缺少水星落宫事实时停止。
- 缺少月亮落宫事实时停止。
- 从十一宫起算的宫位换算未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
