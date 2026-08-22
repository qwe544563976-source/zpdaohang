---
method: ch09-v35-guru-in-tanu-four-grahas-in-dhan-father-lost-at-marriage
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 木星落一宫、土日火水聚二宫：命主结婚之时失去父亲

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 什么时候会失去父亲
- 木星落一宫四星聚二宫怎么断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否落一宫（Tanu Bhava）
- 二宫（Dhan Bhava）是否被土星（Shani）占据
- 二宫（Dhan Bhava）是否被太阳（Surya）占据
- 二宫（Dhan Bhava）是否被火星（Mangal）占据
- 二宫（Dhan Bhava）是否被水星（Budh）占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v35-guru-in-tanu-four-grahas-in-dhan-father-lost-at-marriage.step-001

- 动作：核对木星是否落一宫，并核对土星、太阳、火星、水星是否同聚二宫。
- 适用范围：仅限本命盘对父亲的凶象；原文以男命立说（his marriage），并把时间点定在命主结婚之时。
- 原文最小意思：木星（Guru）落一宫（Tanu Bhava），同时土星（Shani）、太阳（Surya）、火星（Mangal）与水星（Budh）同聚二宫（Dhan Bhava）时，命主会在自己结婚之时失去父亲。
- 本步骤产出事实：["木星落一宫兼四星聚二宫的失父时点判定"]
- 所需事实：["木星（Guru）是否落一宫（Tanu Bhava）", "二宫（Dhan Bhava）是否被土星（Shani）占据", "二宫（Dhan Bhava）是否被太阳（Surya）占据", "二宫（Dhan Bhava）是否被火星（Mangal）占据", "二宫（Dhan Bhava）是否被水星（Budh）占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落一宫（Tanu Bhava）"}, {"fact_key": "二宫（Dhan Bhava）是否被土星（Shani）占据"}, {"fact_key": "二宫（Dhan Bhava）是否被太阳（Surya）占据"}, {"fact_key": "二宫（Dhan Bhava）是否被火星（Mangal）占据"}, {"fact_key": "二宫（Dhan Bhava）是否被水星（Budh）占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把四颗行星减为其中几颗。", "不得把时间点从『结婚之时』改成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落一宫（Tanu Bhava）、二宫（Dhan Bhava）是否被土星（Shani）占据、二宫（Dhan Bhava）是否被太阳（Surya）占据、二宫（Dhan Bhava）是否被火星（Mangal）占据、二宫（Dhan Bhava）是否被水星（Budh）占据。
- 缺失即停字段：["木星（Guru）是否落一宫（Tanu Bhava）", "二宫（Dhan Bhava）是否被土星（Shani）占据", "二宫（Dhan Bhava）是否被太阳（Surya）占据", "二宫（Dhan Bhava）是否被火星（Mangal）占据", "二宫（Dhan Bhava）是否被水星（Budh）占据"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v35`｜PDF [24]｜“The native will at the time of his marriage lose his father, if Guru is in Tanu Bhava, while Shani, Surya, Mangal and Budh are together in Dhan Bhava.”


## 四路查书计划

### 支持路

- The native will at the time of his marriage lose his father, if Guru is in Tanu Bhava, while Shani, Surya, Mangal and Budh are together in Dhan Bhava
- 木星一宫 四星聚二宫 结婚之时 失父

### 反例或取消路

- a single, but strong Guru in Lagn will ward off all the evils
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evil to Father (up to Sloka 42)
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 父亲的凶象怎么看

## 上游问题

- 无

## 停止条件

- 缺少木星落宫事实时停止。
- 缺少二宫占据者事实时停止。
- 原文以男命（his marriage）立说，女命命主要用时须另查原文，本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
