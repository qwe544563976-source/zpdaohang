---
method: ch09-v34-shani-mangal-chandra-in-tanu-yuvati-ari-father-early-death
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 土星、火星、月亮依次落一宫、七宫、六宫：父亲早去世

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 土星火星月亮分落一七六宫怎么断
- 父亲会不会早走

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 土星（Shani）是否落一宫（Tanu Bhava）
- 火星（Mangal）是否落七宫（Yuvati Bhava）
- 月亮（Chandra）是否落六宫（Ari Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v34-shani-mangal-chandra-in-tanu-yuvati-ari-father-early-death.step-001

- 动作：核对土星、火星、月亮是否依次落一宫、七宫与六宫。
- 适用范围：仅限本命盘对父亲的凶象；原文写明 in their orders（依次对应）。
- 原文最小意思：土星（Shani）、火星（Mangal）与月亮（Chandra）依次落一宫（Tanu）、七宫（Yuvati）与六宫（Ari Bhava）时，命主的父亲会早去世。
- 本步骤产出事实：["土火月三落宫的父亲早亡判定"]
- 所需事实：["土星（Shani）是否落一宫（Tanu Bhava）", "火星（Mangal）是否落七宫（Yuvati Bhava）", "月亮（Chandra）是否落六宫（Ari Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否落一宫（Tanu Bhava）"}, {"fact_key": "火星（Mangal）是否落七宫（Yuvati Bhava）"}, {"fact_key": "月亮（Chandra）是否落六宫（Ari Bhava）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得打乱三颗行星与三个宫的对应次序——原文写明 in their orders。", "不得把『早去世』补成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星（Shani）是否落一宫（Tanu Bhava）、火星（Mangal）是否落七宫（Yuvati Bhava）、月亮（Chandra）是否落六宫（Ari Bhava）。
- 缺失即停字段：["土星（Shani）是否落一宫（Tanu Bhava）", "火星（Mangal）是否落七宫（Yuvati Bhava）", "月亮（Chandra）是否落六宫（Ari Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v34`｜PDF [24]｜“One’s father will incur early death, if Shani, Mangal and Chandra in their orders are in Tanu, Yuvati and Ari Bhava.”


## 四路查书计划

### 支持路

- One’s father will incur early death, if Shani, Mangal and Chandra in their orders are in Tanu, Yuvati and Ari Bhava
- 土星一宫 火星七宫 月亮六宫 父亲早亡

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evil to Father (up to Sloka 42)
- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- 父亲用哪颗星看

## 上游问题

- 无

## 停止条件

- 缺少三颗行星任一落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
