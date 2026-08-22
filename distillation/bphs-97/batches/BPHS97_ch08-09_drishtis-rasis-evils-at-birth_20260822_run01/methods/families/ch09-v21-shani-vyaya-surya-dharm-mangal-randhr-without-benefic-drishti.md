---
method: ch09-v21-shani-vyaya-surya-dharm-mangal-randhr-without-benefic-drishti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 土星落十二宫、太阳落九宫、火星落八宫且无吉星相照：当即身亡

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 土星十二宫太阳九宫火星八宫怎么断
- 没有吉星相照的凶星组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 土星（Shani）是否落十二宫（Vyaya Bhava）
- 太阳（Surya）是否落九宫（Dharm Bhava）
- 火星（Mangal）是否落八宫（Randhr Bhava）
- 土星（Shani）是否受吉星相照
- 太阳（Surya）是否受吉星相照
- 火星（Mangal）是否受吉星相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v21-shani-vyaya-surya-dharm-mangal-randhr-without-benefic-drishti.step-001

- 动作：核对土星、太阳、火星是否依次落十二宫、九宫与八宫，并核对三者有无吉星相照。
- 适用范围：仅限本命盘出生时的凶象；原文按列举次序把三颗行星对应到三个宫，并以三星整体『无吉星相照』立说。
- 原文最小意思：土星（Shani）落十二宫（Vyaya）、太阳（Surya）落九宫（Dharm）、火星（Mangal）落八宫（Randhr Bhava），且没有吉星相照时，孩子会当即身亡。
- 本步骤产出事实：["三凶星落宫无吉照的当即身亡判定"]
- 所需事实：["土星（Shani）是否落十二宫（Vyaya Bhava）", "太阳（Surya）是否落九宫（Dharm Bhava）", "火星（Mangal）是否落八宫（Randhr Bhava）", "土星（Shani）是否受吉星相照", "太阳（Surya）是否受吉星相照", "火星（Mangal）是否受吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否落十二宫（Vyaya Bhava）"}, {"fact_key": "太阳（Surya）是否落九宫（Dharm Bhava）"}, {"fact_key": "火星（Mangal）是否落八宫（Randhr Bhava）"}, {"operator": "NOT", "operands": [{"fact_key": "土星（Shani）是否受吉星相照"}]}, {"operator": "NOT", "operands": [{"fact_key": "太阳（Surya）是否受吉星相照"}]}, {"operator": "NOT", "operands": [{"fact_key": "火星（Mangal）是否受吉星相照"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把三颗行星与三个宫的对应次序打乱。", "不得把『当即』补成原文没有的具体时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星（Shani）是否落十二宫（Vyaya Bhava）、太阳（Surya）是否落九宫（Dharm Bhava）、火星（Mangal）是否落八宫（Randhr Bhava）、土星（Shani）是否受吉星相照、太阳（Surya）是否受吉星相照、火星（Mangal）是否受吉星相照。
- 缺失即停字段：["土星（Shani）是否落十二宫（Vyaya Bhava）", "太阳（Surya）是否落九宫（Dharm Bhava）", "火星（Mangal）是否落八宫（Randhr Bhava）", "土星（Shani）是否受吉星相照", "太阳（Surya）是否受吉星相照", "火星（Mangal）是否受吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v21`｜PDF [23]｜“Should Shani, Surya and Mangal be in Vyaya, Dharm and Randhr Bhava without Drishti from a benefic, the child will face instant death.”


## 四路查书计划

### 支持路

- Should Shani, Surya and Mangal be in Vyaya, Dharm and Randhr Bhava without Drishti from a benefic, the child will face instant death
- 土星十二宫 太阳九宫 火星八宫 无吉照

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils
- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle
- Surya in Vyaya will confer a hundred-year life span on one born in Tul Lagn.

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- Short-life Combinations (up to Sloka 23)

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 吉星相照怎么算

## 上游问题

- 无

## 停止条件

- 缺少三颗行星任一落宫事实时停止。
- 缺少三颗行星所受吉星相照事实时停止。
- 原文未指明『无吉星相照』所针对的是行星还是所落之宫，需要按宫取值时本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
