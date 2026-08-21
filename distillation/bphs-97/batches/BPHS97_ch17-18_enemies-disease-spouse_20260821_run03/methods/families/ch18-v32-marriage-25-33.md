---
method: ch18-v32-marriage-25-33
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 婚期第25年与第33年：八宫主落七宫、金星落九分盘的上升宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的婚期在第25年还是第33年
- 八宫主落七宫对婚期有什么说法

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫主（Randhr's Lord）是否落七宫（Yuvati）
- 金星（Shukra）在九分盘（Navamsa D9）中是否落上升宫（Lagna）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v32-marriage-25-33.step-001

- 动作：核对八宫主（Randhr's Lord）是否落七宫（Yuvati），并核对金星（Shukra）在九分盘（Navamsa D9）中是否落上升宫（Lagna），判断婚期。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；原文只给第25与第33年两个年份。
- 原文最小意思：八宫主（Randhr's Lord）落七宫（Yuvati），且金星（Shukra）在九分盘（Navamsa D9）中落上升宫（Lagna）时，婚期在第25或第33年。
- 本步骤产出事实：["八宫主落七宫且金星落九分盘上升宫主第25或第33年成婚判定"]
- 所需事实：["八宫主（Randhr's Lord）是否落七宫（Yuvati）", "金星（Shukra）在九分盘（Navamsa D9）中是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落七宫（Yuvati）"}, {"fact_key": "金星（Shukra）在九分盘（Navamsa D9）中是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断婚姻是否长久或配偶寿命。", "不得把第25年与第33年之外的年份也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否落七宫（Yuvati）、金星（Shukra）在九分盘（Navamsa D9）中是否落上升宫（Lagna）。
- 缺失即停字段：["八宫主（Randhr's Lord）是否落七宫（Yuvati）", "金星（Shukra）在九分盘（Navamsa D9）中是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v32`｜PDF [35]｜“Either the 25<sup>th</sup> year, or the 33<sup>rd</sup> year will bring marriage, if Randhr Lord is in Yuvati, as Shukra is in Navamsa Lagna.”


## 四路查书计划

### 支持路

- Either the 25th year, or the 33rd year will bring marriage, if Randhr Lord is in Yuvati, as Shukra is in Navamsa Lagna
- 八宫主落七宫 金星落九分盘上升 第25年 第33年 婚期

### 反例或取消路

- Marriage will be in the 15th year, if Dhan Lord is in Labh, while Lagn Lord is in Karm
- Should Shukra be in Yuvati from Chandra, while Shani is in Yuvati from Shukr, marriage will be in the 18th year

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34)
- Shukra is in Navamsa Lagna 九分盘上升的取法

### 判断方法路

- Effects of Yuvati Bhava Randhr Lord placement marriage
- 判断婚期应检查哪些宫主

## 上游问题

- 无

## 停止条件

- 缺少八宫主（Randhr's Lord）落宫事实时停止。
- 缺少金星（Shukra）在九分盘（Navamsa D9）中落宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
