---
method: ch20-v13-25-father-fatal-age-21-26-30
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 21岁、26岁或30岁对父亲致命：土星落八宫起第七宫、太阳落土星起第七宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲哪几岁比较危险
- 土星与太阳各自起第七宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 土星（Shani）是否落从八宫（Randhr）起算的第七宫
- 太阳（Surya）是否落从土星（Shani）起算的第七宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v13-25-father-fatal-age-21-26-30.step-001

- 动作：核对土星（Shani）是否落在从八宫（Randhr）起算的第七宫，并核对太阳（Surya）是否落在从土星起算的第七宫。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文以「Combinations for Father’s Death」立目，末句「Thus the Jyotishis may know the effects」把这组组合交由 Jyotishis 判读；原文未给上升限定。
- 原文最小意思：土星（Shani）落从八宫（Randhr）起算的第七宫、且太阳（Surya）落从土星（Shani）起算的第七宫时，21岁、26岁或30岁对父亲是致命的。
- 本步骤产出事实：["土星落八宫起第七宫且太阳落土星起第七宫主21岁26岁30岁对父致命判定"]
- 所需事实：["土星（Shani）是否落从八宫（Randhr）起算的第七宫", "太阳（Surya）是否落从土星（Shani）起算的第七宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否落从八宫（Randhr）起算的第七宫"}, {"fact_key": "太阳（Surya）是否落从土星（Shani）起算的第七宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的死因。", "不得把21岁、26岁、30岁之外的年岁也算进本条。", "不得把从八宫或从土星起算的宫位换成从上升起算的宫位。", "原文此句只写 the ages of 21, 26, or 30，没写是谁的年岁；不得替它补出年岁归属。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星（Shani）是否落从八宫（Randhr）起算的第七宫、太阳（Surya）是否落从土星（Shani）起算的第七宫。
- 缺失即停字段：["土星（Shani）是否落从八宫（Randhr）起算的第七宫", "太阳（Surya）是否落从土星（Shani）起算的第七宫"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v13-25`｜PDF [37]｜“If Shani is in the 7<sup>th</sup> from Randhr Bhava, as Surya is in the 7<sup>th</sup> from Shani, the ages of 21, 26, or 30 will be fatal for the father.”


## 四路查书计划

### 支持路

- If Shani is in the 7<sup>th</sup> from Randhr Bhava, as Surya is in the 7<sup>th</sup> from Shani, the ages of 21, 26, or 30 will be fatal for the father.
- 土星落八宫起第七宫 太阳落土星起第七宫 21岁 26岁 30岁 对父亲致命

### 反例或取消路

- Long-living Father. Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life
- If Dharm’s Lord is an angle and receives a Drishti from Guru, the native’s father will be a king endowed with conveyances, or be equal to a king

### 适用边界路

- If Dharm’s Lord is in its debilitation Rāśi, while his dispositor is in Dharm Bhava, the native will lose his father at the age of 26, or 30
- Evil to Father (up to Sloka 42). One’s father will incur early death, if Shani, Mangal and Chandra in their orders are in Tanu, Yuvati and Ari Bhava

### 判断方法路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- 判断对父亲凶险的年岁要看土星（Shani）与太阳（Surya）互起第七宫的配置

## 上游问题

- 无

## 停止条件

- 缺少土星（Shani）落宫事实时停止。
- 缺少太阳（Surya）落宫事实时停止。
- 原文未标明这三个年岁属于谁，需要落到具体某人的年岁时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
