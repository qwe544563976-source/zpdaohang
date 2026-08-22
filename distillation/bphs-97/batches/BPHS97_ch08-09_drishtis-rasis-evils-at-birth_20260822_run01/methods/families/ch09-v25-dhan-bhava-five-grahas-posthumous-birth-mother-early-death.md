---
method: ch09-v25-dhan-bhava-five-grahas-posthumous-birth-mother-early-death
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 二宫聚罗睺、水星、金星、太阳与土星：命主生于父亲去世之后，母亲也早去世

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 二宫聚了很多星会怎样
- 遗腹子的组合
- 父母双方的凶象

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫（Dhan Bhava）是否被罗睺（Rahu）占据
- 二宫（Dhan Bhava）是否被水星（Budh）占据
- 二宫（Dhan Bhava）是否被金星（Shukr）占据
- 二宫（Dhan Bhava）是否被太阳（Surya）占据
- 二宫（Dhan Bhava）是否被土星（Shani）占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v25-dhan-bhava-five-grahas-posthumous-birth-mother-early-death.step-001

- 动作：核对二宫是否被罗睺、水星、金星、太阳与土星占据。
- 适用范围：仅限本命盘出生时对父母的凶象；原文以五颗行星同占二宫立说。
- 原文最小意思：二宫（Dhan Bhava）被罗睺（Rahu）、水星（Budh）、金星（Shukr）、太阳（Surya）与土星（Shani）占据时，孩子出生在父亲去世之后，连母亲也会早去世。
- 本步骤产出事实：["二宫五星聚集的父母凶象判定"]
- 所需事实：["二宫（Dhan Bhava）是否被罗睺（Rahu）占据", "二宫（Dhan Bhava）是否被水星（Budh）占据", "二宫（Dhan Bhava）是否被金星（Shukr）占据", "二宫（Dhan Bhava）是否被太阳（Surya）占据", "二宫（Dhan Bhava）是否被土星（Shani）占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "二宫（Dhan Bhava）是否被罗睺（Rahu）占据"}, {"fact_key": "二宫（Dhan Bhava）是否被水星（Budh）占据"}, {"fact_key": "二宫（Dhan Bhava）是否被金星（Shukr）占据"}, {"fact_key": "二宫（Dhan Bhava）是否被太阳（Surya）占据"}, {"fact_key": "二宫（Dhan Bhava）是否被土星（Shani）占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把五颗行星减为其中几颗。", "不得把母亲『早去世』补成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫（Dhan Bhava）是否被罗睺（Rahu）占据、二宫（Dhan Bhava）是否被水星（Budh）占据、二宫（Dhan Bhava）是否被金星（Shukr）占据、二宫（Dhan Bhava）是否被太阳（Surya）占据、二宫（Dhan Bhava）是否被土星（Shani）占据。
- 缺失即停字段：["二宫（Dhan Bhava）是否被罗睺（Rahu）占据", "二宫（Dhan Bhava）是否被水星（Budh）占据", "二宫（Dhan Bhava）是否被金星（Shukr）占据", "二宫（Dhan Bhava）是否被太阳（Surya）占据", "二宫（Dhan Bhava）是否被土星（Shani）占据"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v25`｜PDF [23]｜“Should Dhan Bhava be occupied by Rahu, Budh, Shukr, Surya and Shani, the child’s birth has been after its father’s death, while even the mother will face early death.”


## 四路查书计划

### 支持路

- Should Dhan Bhava be occupied by Rahu, Budh, Shukr, Surya and Shani, the child’s birth has been after its father’s death, while even the mother will face early death
- 二宫 罗睺水星金星太阳土星 遗腹 母亲早亡

### 反例或取消路

- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evils to Mother (up to Sloka 33)
- Evil to Father (up to Sloka 42)
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas

### 判断方法路

- Evils at Birth
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- 父母的凶象怎么看

## 上游问题

- 无

## 停止条件

- 缺少二宫占据者事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
