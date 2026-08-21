---
method: ch20-v13-25-father-death-year-7-19
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲在第7年或第19年去世：土星落月亮起第九宫、太阳与罗睺同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲会不会在我很年轻时去世
- 土星在月亮起第九宫又太阳与罗睺同宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 土星（Shani）是否落从月亮（Chandra）起算的第九宫
- 太阳（Surya）是否与罗睺（Rahu）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v13-25-father-death-year-7-19.step-001

- 动作：核对土星（Shani）是否落在从月亮（Chandra）起算的第九宫，并核对太阳（Surya）是否与罗睺（Rahu）同宫。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文以「Combinations for Father’s Death」立目，末句「Thus the Jyotishis may know the effects」把这组组合交由 Jyotishis 判读；原文未给上升限定。
- 原文最小意思：土星（Shani）落从月亮（Chandra）起算的第九宫、且太阳（Surya）与罗睺（Rahu）同宫时，命主的父亲在命主第7年或第19年去世。
- 本步骤产出事实：["土星落月亮起第九宫且太阳会罗睺主父亲第7或19年去世判定"]
- 所需事实：["土星（Shani）是否落从月亮（Chandra）起算的第九宫", "太阳（Surya）是否与罗睺（Rahu）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否落从月亮（Chandra）起算的第九宫"}, {"fact_key": "太阳（Surya）是否与罗睺（Rahu）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的死因。", "不得把第7年与第19年之外的年份也算进本条。", "不得把从月亮起算的第九宫换成本盘九宫（Dharm）。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星（Shani）是否落从月亮（Chandra）起算的第九宫、太阳（Surya）是否与罗睺（Rahu）同宫。
- 缺失即停字段：["土星（Shani）是否落从月亮（Chandra）起算的第九宫", "太阳（Surya）是否与罗睺（Rahu）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v13-25`｜PDF [37]｜“If Shani is in the 9<sup>th</sup> from Chandra, as Surya is with Rahu, the native’s father will die in the 7<sup>th</sup> , or the 19<sup>th</sup> year of the native.”


## 四路查书计划

### 支持路

- If Shani is in the 9<sup>th</sup> from Chandra, as Surya is with Rahu, the native’s father will die in the 7<sup>th</sup> , or the 19<sup>th</sup> year of the native.
- 土星落月亮起第九宫 太阳与罗睺同宫 父亲第7年 第19年 去世

### 反例或取消路

- Long-living Father. Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life
- Fortunate (Affluent) Father. If Dharm’s Lord is with strength, as Shukra is in Dharm, while Guru is in an angle from Tanu Bhava, the native’s father is fortunate

### 适用边界路

- Evil to Father (up to Sloka 42). One’s father will incur early death, if Shani, Mangal and Chandra in their orders are in Tanu, Yuvati and Ari Bhava
- The stronger among Surya and Shukra indicates the father

### 判断方法路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- 判断父亲去世年岁要看从月亮（Chandra）起算的宫位与太阳（Surya）的会合

## 上游问题

- 无

## 停止条件

- 缺少土星（Shani）落宫事实时停止。
- 缺少太阳（Surya）与罗睺（Rahu）是否同宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
