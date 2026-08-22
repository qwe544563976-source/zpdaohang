---
method: ch09-v31-guru-shani-rahu-in-tanu-dhan-sahaj-mother-early-death
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 木星、土星、罗睺依次落一宫、二宫、三宫：母亲早去世

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 木星土星罗睺分落一二三宫怎么断
- 母亲早亡的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否落一宫（Tanu Bhava）
- 土星（Shani）是否落二宫（Dhan Bhava）
- 罗睺（Rahu）是否落三宫（Sahaj Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v31-guru-shani-rahu-in-tanu-dhan-sahaj-mother-early-death.step-001

- 动作：核对木星、土星、罗睺是否依次落一宫、二宫与三宫。
- 适用范围：仅限本命盘对母亲的凶象；原文写明 respectively（依次对应）。
- 原文最小意思：木星（Guru）、土星（Shani）与罗睺（Rahu）依次落一宫（Tanu）、二宫（Dhan）与三宫（Sahaj Bhava）时，会致母亲早去世。
- 本步骤产出事实：["木土罗睺三落宫的母亲早亡判定"]
- 所需事实：["木星（Guru）是否落一宫（Tanu Bhava）", "土星（Shani）是否落二宫（Dhan Bhava）", "罗睺（Rahu）是否落三宫（Sahaj Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落一宫（Tanu Bhava）"}, {"fact_key": "土星（Shani）是否落二宫（Dhan Bhava）"}, {"fact_key": "罗睺（Rahu）是否落三宫（Sahaj Bhava）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得打乱三颗行星与三个宫的对应次序——原文写明 respectively。", "不得把『早去世』补成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落一宫（Tanu Bhava）、土星（Shani）是否落二宫（Dhan Bhava）、罗睺（Rahu）是否落三宫（Sahaj Bhava）。
- 缺失即停字段：["木星（Guru）是否落一宫（Tanu Bhava）", "土星（Shani）是否落二宫（Dhan Bhava）", "罗睺（Rahu）是否落三宫（Sahaj Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v31`｜PDF [24]｜“Guru, Shani and Rahu, respectively, posited in Tanu, Dhan and Sahaj Bhava will cause mother’s death early.”


## 四路查书计划

### 支持路

- Guru, Shani and Rahu, respectively, posited in Tanu, Dhan and Sahaj Bhava will cause mother’s death early
- 木星一宫 土星二宫 罗睺三宫 母亲早亡

### 反例或取消路

- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Evils to Mother (up to Sloka 33)
- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- 母亲的凶象怎么看

## 上游问题

- 无

## 停止条件

- 缺少三颗行星任一落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
