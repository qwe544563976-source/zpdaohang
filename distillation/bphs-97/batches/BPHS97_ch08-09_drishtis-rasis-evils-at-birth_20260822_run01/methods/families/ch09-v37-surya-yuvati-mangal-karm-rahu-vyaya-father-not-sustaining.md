---
method: ch09-v37-surya-yuvati-mangal-karm-rahu-vyaya-father-not-sustaining
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 太阳落七宫、火星落十宫、罗睺落十二宫：父亲存续的可能极小

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 太阳七宫火星十宫罗睺十二宫怎么断
- 父亲能不能长久

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否落七宫（Yuvati Bhava）
- 火星（Mangal）是否落十宫（Karm Bhava）
- 罗睺（Rahu）是否落十二宫（Vyaya Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v37-surya-yuvati-mangal-karm-rahu-vyaya-father-not-sustaining.step-001

- 动作：核对太阳、火星、罗睺是否分别落七宫、十宫与十二宫。
- 适用范围：仅限本命盘对父亲的凶象；原文以『可能极小』的措辞给出结论强度。
- 原文最小意思：太阳（Surya）落七宫（Yuvati），火星（Mangal）落十宫（Karm），罗睺（Rahu）落十二宫（Vyaya Bhava）时，父亲得以存续的可能极小。
- 本步骤产出事实：["日火罗睺三落宫的父亲存续判定"]
- 所需事实：["太阳（Surya）是否落七宫（Yuvati Bhava）", "火星（Mangal）是否落十宫（Karm Bhava）", "罗睺（Rahu）是否落十二宫（Vyaya Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落七宫（Yuvati Bhava）"}, {"fact_key": "火星（Mangal）是否落十宫（Karm Bhava）"}, {"fact_key": "罗睺（Rahu）是否落十二宫（Vyaya Bhava）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『可能极小』改写成必然去世。", "不得把三颗行星的落宫拆开单用。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落七宫（Yuvati Bhava）、火星（Mangal）是否落十宫（Karm Bhava）、罗睺（Rahu）是否落十二宫（Vyaya Bhava）。
- 缺失即停字段：["太阳（Surya）是否落七宫（Yuvati Bhava）", "火星（Mangal）是否落十宫（Karm Bhava）", "罗睺（Rahu）是否落十二宫（Vyaya Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v37`｜PDF [24]｜“Remote will be the possibility of one’s father sustaining, if Surya is in Yuvati, while Mangal is in Karm and Rahu is in Vyaya Bhava.”


## 四路查书计划

### 支持路

- Remote will be the possibility of one’s father sustaining, if Surya is in Yuvati, while Mangal is in Karm and Rahu is in Vyaya Bhava
- 太阳七宫 火星十宫 罗睺十二宫 父亲

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evil to Father (up to Sloka 42)
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- 父亲的凶象怎么看

## 上游问题

- 无

## 停止条件

- 缺少三颗行星任一落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
