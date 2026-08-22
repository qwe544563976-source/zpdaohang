---
method: ch09-v3-6-putr-bhava-shani-mangal-surya-mother-and-brother-die
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 五宫被土星、火星、太阳共同占据：母亲与兄弟去世

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 五宫聚了土星火星太阳会怎样
- 母亲与兄弟的凶象怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫（Putr Bhava）是否被土星（Shani）占据
- 五宫（Putr Bhava）是否被火星（Mangal）占据
- 五宫（Putr Bhava）是否被太阳（Surya）占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v3-6-putr-bhava-shani-mangal-surya-mother-and-brother-die.step-001

- 动作：核对五宫是否同时被土星、火星与太阳占据。
- 适用范围：仅限本命盘出生时对母亲与兄弟的凶象；原文以『共同占据』立说。
- 原文最小意思：五宫（Putr Bhava）被土星（Shani）、火星（Mangal）与太阳（Surya）共同占据时，母亲与兄弟会（提早）去世。
- 本步骤产出事实：["五宫三凶聚集的母亲与兄弟凶象判定"]
- 所需事实：["五宫（Putr Bhava）是否被土星（Shani）占据", "五宫（Putr Bhava）是否被火星（Mangal）占据", "五宫（Putr Bhava）是否被太阳（Surya）占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫（Putr Bhava）是否被土星（Shani）占据"}, {"fact_key": "五宫（Putr Bhava）是否被火星（Mangal）占据"}, {"fact_key": "五宫（Putr Bhava）是否被太阳（Surya）占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把三颗行星减为其中一颗或两颗——原文要求三者共同占据。", "不得把『兄弟』扩大成原文没写的其他亲属。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫（Putr Bhava）是否被土星（Shani）占据、五宫（Putr Bhava）是否被火星（Mangal）占据、五宫（Putr Bhava）是否被太阳（Surya）占据。
- 缺失即停字段：["五宫（Putr Bhava）是否被土星（Shani）占据", "五宫（Putr Bhava）是否被火星（Mangal）占据", "五宫（Putr Bhava）是否被太阳（Surya）占据"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v3-6`｜PDF [22]｜“Should Putr Bhava be occupied by Shani, Mangal and Surya jointly, (early) death of mother and brother will come to pass.”


## 四路查书计划

### 支持路

- Should Putr Bhava be occupied by Shani, Mangal and Surya jointly, (early) death of mother and brother will come to pass
- 五宫 土星火星太阳 母亲兄弟 凶

### 反例或取消路

- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Evils to Mother (up to Sloka 33)
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas

### 判断方法路

- Evils at Birth
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- 母亲的凶象怎么看

## 上游问题

- 无

## 停止条件

- 缺少五宫占据者事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
