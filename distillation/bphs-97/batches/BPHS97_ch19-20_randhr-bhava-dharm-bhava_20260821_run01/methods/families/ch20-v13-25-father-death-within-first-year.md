---
method: ch20-v13-25-father-death-within-first-year
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲在命主出生后一年内去世：太阳落八宫、八宫主落九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲会不会在我很小的时候就不在了
- 太阳落八宫又八宫主落九宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否落八宫（Randhr）
- 八宫主（Randhr's Lord）是否落九宫（Dharm）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v13-25-father-death-within-first-year.step-001

- 动作：核对太阳（Surya）是否落八宫（Randhr），并核对八宫主（Randhr's Lord）是否落九宫（Dharm）。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文以「Combinations for Father’s Death」立目，末句「Thus the Jyotishis may know the effects」把这组组合交由 Jyotishis 判读；原文未给上升限定。原文「within a year of his birth」的 his，按同偈前句的「the native’s birth」读作命主出生。
- 原文最小意思：太阳（Surya）落八宫（Randhr）、且八宫主（Randhr's Lord）落九宫（Dharm）时，命主的父亲会在命主出生后一年之内去世。
- 本步骤产出事实：["太阳落八宫且八宫主落九宫主父亲一年内去世判定"]
- 所需事实：["太阳（Surya）是否落八宫（Randhr）", "八宫主（Randhr's Lord）是否落九宫（Dharm）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落八宫（Randhr）"}, {"fact_key": "八宫主（Randhr's Lord）是否落九宫（Dharm）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的死因。", "不得把出生一年之后的时间也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落八宫（Randhr）、八宫主（Randhr's Lord）是否落九宫（Dharm）。
- 缺失即停字段：["太阳（Surya）是否落八宫（Randhr）", "八宫主（Randhr's Lord）是否落九宫（Dharm）"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v13-25`｜PDF [37]｜“Should Surya be in Randhr Bhava, while Randhr’s Lord is in Dharm, the native’s father will pass away within a year of his birth.”


## 四路查书计划

### 支持路

- Should Surya be in Randhr Bhava, while Randhr’s Lord is in Dharm, the native’s father will pass away within a year of his birth.
- 太阳落八宫 八宫主落九宫 父亲出生一年内去世

### 反例或取消路

- Long-living Father. Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life
- Fortunate (Affluent) Father. If Dharm’s Lord is with strength, as Shukra is in Dharm, while Guru is in an angle from Tanu Bhava, the native’s father is fortunate

### 适用边界路

- The father will not see the native till his (the native’s) 23<sup>rd</sup> year, if Rahu and Guru are together in an inimical Rashiidentical with Tanu, or Bandhu Bhava
- Evil to Father (up to Sloka 42). One’s father will incur early death, if Shani, Mangal and Chandra in their orders are in Tanu, Yuvati and Ari Bhava
- The 9<sup>th</sup> from Surya denotes father

### 判断方法路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- 判断父亲早亡的年岁要看太阳（Surya）与八宫（Randhr）的哪些配置

## 上游问题

- 无

## 停止条件

- 缺少太阳（Surya）落宫事实时停止。
- 缺少八宫主（Randhr's Lord）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
