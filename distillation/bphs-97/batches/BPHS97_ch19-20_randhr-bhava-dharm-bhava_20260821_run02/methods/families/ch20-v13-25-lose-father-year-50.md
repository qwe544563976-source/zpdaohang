---
method: ch20-v13-25-lose-father-year-50
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 命主第50年失去父亲：太阳本身是九宫主并与火星、土星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我到中年以后父亲还在吗
- 太阳作为九宫主又与火星土星同宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否为太阳（Surya）
- 太阳（Surya）是否与火星（Mangal）同宫
- 太阳（Surya）是否与土星（Shani）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v13-25-lose-father-year-50.step-001

- 动作：先核对九宫主（Dharm's Lord）是不是太阳（Surya），再核对太阳是否与火星（Mangal）以及土星（Shani）同宫。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文以「Combinations for Father’s Death」立目，末句「Thus the Jyotishis may know the effects」把这组组合交由 Jyotishis 判读；原文未给上升限定。
- 原文最小意思：太阳（Surya）本身就是九宫主（Dharm's Lord），并与火星（Mangal）及土星（Shani）同宫时，命主在第50年失去父亲。
- 本步骤产出事实：["太阳为九宫主并会火星土星主第50年失去父亲判定"]
- 所需事实：["九宫主（Dharm's Lord）是否为太阳（Surya）", "太阳（Surya）是否与火星（Mangal）同宫", "太阳（Surya）是否与土星（Shani）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否为太阳（Surya）"}, {"fact_key": "太阳（Surya）是否与火星（Mangal）同宫"}, {"fact_key": "太阳（Surya）是否与土星（Shani）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的死因。", "不得把第50年之外的年份也算进本条。", "不得把「与火星及土星同宫」放宽成只与其中一颗同宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否为太阳（Surya）、太阳（Surya）是否与火星（Mangal）同宫、太阳（Surya）是否与土星（Shani）同宫。
- 缺失即停字段：["九宫主（Dharm's Lord）是否为太阳（Surya）", "太阳（Surya）是否与火星（Mangal）同宫", "太阳（Surya）是否与土星（Shani）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v13-25`｜PDF [37]｜“One will lose his father in the 50<sup>th</sup> year, if Surya, being the Lord of Dharm, is conjunct Mangal and Shani.”


## 四路查书计划

### 支持路

- One will lose his father in the 50<sup>th</sup> year, if Surya, being the Lord of Dharm, is conjunct Mangal and Shani.
- 太阳是九宫主 与火星土星同宫 第50年 失去父亲

### 反例或取消路

- Long-living Father. Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life
- If Dharm’s Lord is an angle and receives a Drishti from Guru, the native’s father will be a king endowed with conveyances, or be equal to a king

### 适用边界路

- Evil to Father (up to Sloka 42). One’s father will incur early death, if Shani, Mangal and Chandra in their orders are in Tanu, Yuvati and Ari Bhava
- The stronger among Surya and Shukra indicates the father

### 判断方法路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- 判断失去父亲的年岁要看太阳（Surya）兼任九宫主（Dharm's Lord）时的会合

## 上游问题

- 无

## 停止条件

- 缺少九宫主（Dharm's Lord）是哪颗行星的事实时停止。
- 缺少太阳（Surya）与火星（Mangal）或土星（Shani）是否同宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
