---
method: ch09-v30-budh-in-dhan-malefics-in-tanu-and-vyaya-destroys-family
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 水星落二宫、凶星占一宫与十二宫：此瑜伽毁掉整个家族

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 水星落二宫又有凶星占一宫十二宫怎么断
- 家族败落的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 水星（Budh）是否落二宫（Dhan Bhava）
- 一宫（Tanu Bhava）是否被凶星占据
- 十二宫（Vyaya Bhava）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v30-budh-in-dhan-malefics-in-tanu-and-vyaya-destroys-family.step-001

- 动作：核对水星是否落二宫，并核对一宫与十二宫是否被凶星占据。
- 适用范围：仅限本命盘出生时的凶象；原文把这一组合称作一个 Yoga。
- 原文最小意思：水星（Budh）落二宫（Dhan Bhava），同时凶星占据一宫（Tanu）与十二宫（Vyaya Bhava）时，这个瑜伽（Yoga）会毁掉整个家族。
- 本步骤产出事实：["水星落二宫兼一宫十二宫受克的家族凶象判定"]
- 所需事实：["水星（Budh）是否落二宫（Dhan Bhava）", "一宫（Tanu Bhava）是否被凶星占据", "十二宫（Vyaya Bhava）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落二宫（Dhan Bhava）"}, {"fact_key": "一宫（Tanu Bhava）是否被凶星占据"}, {"fact_key": "十二宫（Vyaya Bhava）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『整个家族』限缩或扩大成原文没写的具体亲属。", "不得漏掉一宫与十二宫都要有凶星这一前提。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：水星（Budh）是否落二宫（Dhan Bhava）、一宫（Tanu Bhava）是否被凶星占据、十二宫（Vyaya Bhava）是否被凶星占据。
- 缺失即停字段：["水星（Budh）是否落二宫（Dhan Bhava）", "一宫（Tanu Bhava）是否被凶星占据", "十二宫（Vyaya Bhava）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v30`｜PDF [24]｜“Budh in Dhan Bhava, while malefics occupy Tanu and Vyaya Bhava: this Yoga will destroy the entire family.”


## 四路查书计划

### 支持路

- Budh in Dhan Bhava, while malefics occupy Tanu and Vyaya Bhava: this Yoga will destroy the entire family
- 水星二宫 凶星一宫十二宫 家族

### 反例或取消路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- Evils to Mother (up to Sloka 33)

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 家族凶象怎么看

## 上游问题

- 无

## 停止条件

- 缺少水星落宫事实时停止。
- 缺少一宫、十二宫的凶星占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
