---
method: ch20-v13-25-father-death-year-16-18
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲在第16年或第18年去世：罗睺落九宫起第八宫、太阳落九宫起第九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲会不会在我少年时去世
- 罗睺与太阳从九宫起算的位置说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 罗睺（Rahu）是否落从九宫（Dharm）起算的第八宫
- 太阳（Surya）是否落从九宫（Dharm）起算的第九宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v13-25-father-death-year-16-18.step-001

- 动作：核对罗睺（Rahu）是否落在从九宫（Dharm）起算的第八宫，并核对太阳（Surya）是否落在从九宫（Dharm）起算的第九宫。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文以「Combinations for Father’s Death」立目，末句「Thus the Jyotishis may know the effects」把这组组合交由 Jyotishis 判读；原文未给上升限定。
- 原文最小意思：罗睺（Rahu）落从九宫（Dharm）起算的第八宫、且太阳（Surya）落从九宫（Dharm）起算的第九宫时，父亲在命主第16年或第18年去世。
- 本步骤产出事实：["罗睺落九宫起第八宫且太阳落九宫起第九宫主父亲第16或18年去世判定"]
- 所需事实：["罗睺（Rahu）是否落从九宫（Dharm）起算的第八宫", "太阳（Surya）是否落从九宫（Dharm）起算的第九宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "罗睺（Rahu）是否落从九宫（Dharm）起算的第八宫"}, {"fact_key": "太阳（Surya）是否落从九宫（Dharm）起算的第九宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的死因。", "不得把第16年与第18年之外的年份也算进本条。", "不得把从九宫起算的宫位换成从上升起算的宫位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：罗睺（Rahu）是否落从九宫（Dharm）起算的第八宫、太阳（Surya）是否落从九宫（Dharm）起算的第九宫。
- 缺失即停字段：["罗睺（Rahu）是否落从九宫（Dharm）起算的第八宫", "太阳（Surya）是否落从九宫（Dharm）起算的第九宫"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v13-25`｜PDF [37]｜“Should Rahu be in the 8<sup>th</sup> from Dharm, as Surya is in the 9<sup>th</sup> from Dharm, death of father will take place in the 16<sup>th</sup> , or the 18<sup>th</sup> year of the native.”


## 四路查书计划

### 支持路

- Should Rahu be in the 8<sup>th</sup> from Dharm, as Surya is in the 9<sup>th</sup> from Dharm, death of father will take place in the 16<sup>th</sup> , or the 18<sup>th</sup> year of the native.
- 罗睺落九宫起第八宫 太阳落九宫起第九宫 父亲第16年 第18年

### 反例或取消路

- Long-living Father. Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life
- If Dharm’s Lord is an angle and receives a Drishti from Guru, the native’s father will be a king endowed with conveyances, or be equal to a king

### 适用边界路

- If Shani is in the 7<sup>th</sup> from Randhr Bhava, as Surya is in the 7<sup>th</sup> from Shani, the ages of 21, 26, or 30 will be fatal for the father
- The 9<sup>th</sup> from Surya denotes father

### 判断方法路

- Dharm Bhava and the 9<sup>th</sup> from Surya deal with one’s father
- 判断父亲去世年岁要看从九宫（Dharm）起算的哪些宫位

## 上游问题

- 无

## 停止条件

- 缺少罗睺（Rahu）落宫事实时停止。
- 缺少太阳（Surya）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
