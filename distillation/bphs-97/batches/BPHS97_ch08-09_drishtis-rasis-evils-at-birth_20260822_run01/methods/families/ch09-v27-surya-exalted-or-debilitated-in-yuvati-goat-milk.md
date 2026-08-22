---
method: ch09-v27-surya-exalted-or-debilitated-in-yuvati-goat-milk
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 太阳落七宫且入旺或落陷：孩子不吃母乳而吃羊奶

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 孩子能不能吃到母乳
- 太阳落七宫入旺落陷怎么断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否落七宫（Yuvati Bhava）

## 按情况检查的事实

- 太阳（Surya）是否入旺
- 太阳（Surya）是否落陷

## 依赖方法

- 无

## 执行步骤

### ch09-v27-surya-exalted-or-debilitated-in-yuvati-goat-milk.step-001

- 动作：核对太阳是否落七宫，并核对它在该处是入旺还是落陷。
- 适用范围：仅限本命盘对哺乳的判断；原文只给这一条件下的哺乳来源。
- 原文最小意思：太阳（Surya）在七宫（Yuvati Bhava）入旺或落陷时，孩子不靠母乳而靠母山羊的奶存活。
- 本步骤产出事实：["太阳落七宫的哺乳来源判定"]
- 所需事实：["太阳（Surya）是否落七宫（Yuvati Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落七宫（Yuvati Bhava）"}, {"operator": "OR", "operands": [{"fact_key": "太阳（Surya）是否入旺"}, {"fact_key": "太阳（Surya）是否落陷"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "太阳（Surya）是否落七宫（Yuvati Bhava）"}, "required_fact_keys": ["太阳（Surya）是否入旺"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否入旺"}, "selection_group": "ch09-v27-surya-exalted-or-debilitated-in-yuvati-goat-milk.step-001:surya-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否入旺。"}, {"when": {"fact_key": "太阳（Surya）是否落七宫（Yuvati Bhava）"}, "required_fact_keys": ["太阳（Surya）是否落陷"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否落陷"}, "selection_group": "ch09-v27-surya-exalted-or-debilitated-in-yuvati-goat-milk.step-001:surya-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否落陷。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本偈推断母亲的生死——原文只说孩子的哺乳来源。", "不得把入旺与落陷之外的状态也算进来。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落七宫（Yuvati Bhava）。
- 缺失即停字段：["太阳（Surya）是否落七宫（Yuvati Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v27`｜PDF [23]｜“The child will not live on mother’s milk, but on that of she-goat, if Surya is exalted, or debilitated in Yuvati Bhava.”


## 四路查书计划

### 支持路

- The child will not live on mother’s milk, but on that of she-goat, if Surya is exalted, or debilitated in Yuvati Bhava
- 太阳七宫 入旺 落陷 羊奶

### 反例或取消路

- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.

### 适用边界路

- Evils to Mother (up to Sloka 33)
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- 入旺落陷怎么定
- 母亲用哪颗星看

## 上游问题

- 无

## 停止条件

- 缺少太阳落宫事实时停止。
- 缺少太阳的入旺、落陷状态时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
