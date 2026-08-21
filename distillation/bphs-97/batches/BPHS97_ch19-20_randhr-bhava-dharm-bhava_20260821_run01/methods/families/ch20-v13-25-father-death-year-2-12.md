---
method: ch20-v13-25-father-death-year-2-12
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲在第2年或第12年去世：上升主落八宫、八宫主与太阳同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲会不会在我童年时去世
- 上升主落八宫又八宫主会太阳说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否落八宫（Randhr）
- 八宫主（Randhr's Lord）是否与太阳（Surya）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v13-25-father-death-year-2-12.step-001

- 动作：核对上升主（Lagn's Lord）是否落八宫（Randhr），并核对八宫主（Randhr's Lord）是否与太阳（Surya）同宫。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文以「Combinations for Father’s Death」立目，末句「Thus the Jyotishis may know the effects」把这组组合交由 Jyotishis 判读；原文未给上升限定。
- 原文最小意思：上升主（Lagn's Lord）落八宫（Randhr）、且八宫主（Randhr's Lord）与太阳（Surya）同宫时，父亲在第2年或第12年去世。
- 本步骤产出事实：["上升主落八宫且八宫主会太阳主父亲第2或12年去世判定"]
- 所需事实：["上升主（Lagn's Lord）是否落八宫（Randhr）", "八宫主（Randhr's Lord）是否与太阳（Surya）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落八宫（Randhr）"}, {"fact_key": "八宫主（Randhr's Lord）是否与太阳（Surya）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的死因。", "不得把第2年与第12年之外的年份也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否落八宫（Randhr）、八宫主（Randhr's Lord）是否与太阳（Surya）同宫。
- 缺失即停字段：["上升主（Lagn's Lord）是否落八宫（Randhr）", "八宫主（Randhr's Lord）是否与太阳（Surya）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v13-25`｜PDF [37]｜“Death of father will occur in the 2<sup>nd</sup> , or the 12<sup>th</sup> year, if Lagn’s Lord is in Randhr Bhava, as Randhr’s Lord is with Surya.”


## 四路查书计划

### 支持路

- Death of father will occur in the 2<sup>nd</sup> , or the 12<sup>th</sup> year, if Lagn’s Lord is in Randhr Bhava, as Randhr’s Lord is with Surya.
- 上升主落八宫 八宫主与太阳同宫 父亲第2年 第12年 去世

### 反例或取消路

- Long-living Father. Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life
- Fortunate (Affluent) Father. If Dharm’s Lord is with strength, as Shukra is in Dharm, while Guru is in an angle from Tanu Bhava, the native’s father is fortunate

### 适用边界路

- The father will not see the native till his (the native’s) 23<sup>rd</sup> year, if Rahu and Guru are together in an inimical Rashiidentical with Tanu, or Bandhu Bhava
- If Lagn’s Lord is in Randhr Bhava, as Chandra is in Surya’s Navāńś, the native in his 35<sup>th</sup> , or 41<sup>st</sup> year will lose his father

### 判断方法路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- 判断父亲去世年岁要看上升主（Lagn's Lord）与八宫（Randhr）的哪些配置

## 上游问题

- 无

## 停止条件

- 缺少上升主（Lagn's Lord）落宫事实时停止。
- 缺少八宫主与太阳（Surya）是否同宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
