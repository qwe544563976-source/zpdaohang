---
method: ch18-v40-41-three-marriages
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三次婚姻：月亮在金星起第七宫、水星在月亮起第七宫、八宫主落五宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有三次婚姻
- 我的几次婚姻分别在哪一年

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否落金星（Shukra）起第七宫（Yuvati）
- 水星（Budh）是否落月亮（Chandra）起第七宫（Yuvati）
- 八宫主（Randhr's Lord）是否落五宫（Putr）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v40-41-three-marriages.step-001

- 动作：核对月亮（Chandra）是否落在从金星起算的第七宫、水星（Budh）是否落在从月亮起算的第七宫，并核对八宫主（Randhr's Lord）是否落从上升起算的五宫（Putr），判断婚姻次数与各次婚期。
- 适用范围：仅限本命盘七宫（Yuvati）婚姻次数与婚期主题；原文把第一次婚期写作 Karm 年，未折算成岁数。
- 原文最小意思：月亮（Chandra）落在从金星（Shukr）起算的第七宫（Yuvati），水星（Budh）落在从月亮（Chandra）起算的第七宫（Yuvati），且八宫主（Randhr's Lord）落在从上升（Lagna）起算的五宫（Putr）时，会有三次婚姻：一次在 Karm 年，另一次在第22年，再一次在第33年。
- 本步骤产出事实：["月亮水星互在第七宫且八宫主落五宫主三次婚姻判定"]
- 所需事实：["月亮（Chandra）是否落金星（Shukra）起第七宫（Yuvati）", "水星（Budh）是否落月亮（Chandra）起第七宫（Yuvati）", "八宫主（Randhr's Lord）是否落五宫（Putr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落金星（Shukra）起第七宫（Yuvati）"}, {"fact_key": "水星（Budh）是否落月亮（Chandra）起第七宫（Yuvati）"}, {"fact_key": "八宫主（Randhr's Lord）是否落五宫（Putr）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 Karm 年折算成具体岁数——原文只写 Karm year。", "不得据此推断离婚原因或配偶身份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否落金星（Shukra）起第七宫（Yuvati）、水星（Budh）是否落月亮（Chandra）起第七宫（Yuvati）、八宫主（Randhr's Lord）是否落五宫（Putr）。
- 缺失即停字段：["月亮（Chandra）是否落金星（Shukra）起第七宫（Yuvati）", "水星（Budh）是否落月亮（Chandra）起第七宫（Yuvati）", "八宫主（Randhr's Lord）是否落五宫（Putr）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v40-41`｜PDF [35]｜“THREE MARRIAGES. Should Chandra be in Yuvati from Shukr, while Budh is in Yuvati from Chandra and Randhr Lord is in Putr (from the Lagna), there will be marriage in Karm year followed by another in the 22<sup>nd</sup> year and yet another in the 33<sup>rd</sup> year.”


## 四路查书计划

### 支持路

- 月亮在金星起第七宫 水星在月亮起第七宫 八宫主落五宫 三次婚姻 Karm 年

### 反例或取消路

- One will have two wives, if Yuvati Lord is in fall, or in a malefic Rashialong with a malefic
- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)

### 适用边界路

- Karm year 以宫位名指年份的算法

### 判断方法路

- 判断婚姻次数应检查什么

## 上游问题

- 无

## 停止条件

- 缺少月亮（Chandra）相对金星（Shukra）的落宫事实时停止。
- 缺少水星（Budh）相对月亮（Chandra）的落宫事实时停止。
- 缺少八宫主（Randhr's Lord）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
