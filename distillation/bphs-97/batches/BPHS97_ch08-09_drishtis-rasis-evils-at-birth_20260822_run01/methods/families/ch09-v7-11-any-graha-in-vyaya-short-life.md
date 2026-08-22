---
method: ch09-v7-11-any-graha-in-vyaya-short-life
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 十二宫有行星即主短寿，尤以二曜、金星与罗睺为甚；这四星相照十二宫则化解

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 十二宫有行星会怎样
- 什么样的行星落十二宫最凶
- 短寿怎么化解

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十二宫（Vyaya Bhava）是否有行星（Grah）落入

## 按情况检查的事实

- 十二宫（Vyaya Bhava）是否受太阳（Surya）相照
- 十二宫（Vyaya Bhava）是否受月亮（Chandra）相照
- 十二宫（Vyaya Bhava）是否受金星（Shukra）相照
- 十二宫（Vyaya Bhava）是否受罗睺（Rahu）相照

## 依赖方法

- 无

## 执行步骤

### ch09-v7-11-any-graha-in-vyaya-short-life.step-001

- 动作：核对十二宫内有无行星落入，并核对这四颗行星有无相照十二宫。
- 适用范围：仅限本命盘十二宫的短寿判断；原文以『尤其』标出四颗行星，并未把范围限死在这四颗。
- 原文最小意思：任何行星（Grah）落十二宫（Vyaya Bhava）都会成为短寿之源，尤其是二曜、金星（Shukra）与罗睺（Rahu）；但这四颗行星相照十二宫则会抵消此凶。
- 本步骤产出事实：["十二宫有行星的短寿判定"]
- 所需事实：["十二宫（Vyaya Bhava）是否有行星（Grah）落入"]
- 条件关系：{"fact_key": "十二宫（Vyaya Bhava）是否有行星（Grah）落入"}
- 按分支必查事实：[]
- 例外、取消或缓解：[{"type": "cancellation", "evidence_atom_ids": ["bphs-97:santhanam:ch09:v7-11"], "condition_logic": {"operator": "OR", "operands": [{"fact_key": "十二宫（Vyaya Bhava）是否受太阳（Surya）相照"}, {"fact_key": "十二宫（Vyaya Bhava）是否受月亮（Chandra）相照"}, {"fact_key": "十二宫（Vyaya Bhava）是否受金星（Shukra）相照"}, {"fact_key": "十二宫（Vyaya Bhava）是否受罗睺（Rahu）相照"}]}}]
- 禁止扩大：["不得把『尤其是』读成只有这四颗行星落十二宫才主短寿——原文先说任何行星。", "不得把抵消读成寿命变长的具体年数。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十二宫（Vyaya Bhava）是否有行星（Grah）落入。
- 缺失即停字段：["十二宫（Vyaya Bhava）是否有行星（Grah）落入"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v7-11`｜PDF [22]｜“All Grahas (any Grah) in Vyaya Bhava will be the source of a short life, specifically the luminaries, Shukra and Rahu. But the Drishti of these four Grahas (on Vyaya Bhava) will counteract such evils.”


## 四路查书计划

### 支持路

- All Grahas (any Grah) in Vyaya Bhava will be the source of a short life, specifically the luminaries, Shukra and Rahu
- 十二宫 有行星 短寿

### 反例或取消路

- But the Drishti of these four Grahas (on Vyaya Bhava) will counteract such evils.
- Surya in Vyaya will confer a hundred-year life span on one born in Tul Lagn.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- Short-life Combinations (up to Sloka 23)

### 判断方法路

- Evils at Birth
- Kindly detail methods of ascertaining the life-span of human beings.
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 十二宫怎么判

## 上游问题

- 无

## 停止条件

- 缺少十二宫内行星事实时停止。
- 缺少这四颗行星对十二宫的相照事实时，抵消一节停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
