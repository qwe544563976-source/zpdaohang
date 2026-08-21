---
method: ch18-v30-marriage-22-27
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 婚期第22年与第27年：金星落八宫起第七宫（即二宫）、其星座主与火星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我大概哪一年会结婚
- 我的婚期会不会落在第22年或第27年

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 金星（Shukra）是否落二宫（Dhan）
- 金星（Shukra）的星座主是否与火星（Mangal）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v30-marriage-22-27.step-001

- 动作：核对金星（Shukra）是否落在从八宫（Randhr）起算的第七宫、即上升起算的二宫（Dhan），以及金星的星座主是否与火星（Mangal）同宫，判断婚期。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；原文「his dispositor」的 his 指同句的金星（Shukra）；原文只把婚期系在第22与第27年两个年份。
- 原文最小意思：金星（Shukra）落在从八宫（Randhr）起算的第七宫（Yuvati）、即从上升（Lagna）起算的二宫（Dhan），且其星座主与火星（Mangal）同宫时，命主第22或第27年成婚。
- 本步骤产出事实：["金星落二宫且其星座主会火星主第22或第27年成婚判定"]
- 所需事实：["金星（Shukra）是否落二宫（Dhan）", "金星（Shukra）的星座主是否与火星（Mangal）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落二宫（Dhan）"}, {"fact_key": "金星（Shukra）的星座主是否与火星（Mangal）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断配偶相貌、家世或婚姻次数。", "不得把第22年与第27年之外的年份也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：金星（Shukra）是否落二宫（Dhan）、金星（Shukra）的星座主是否与火星（Mangal）同宫。
- 缺失即停字段：["金星（Shukra）是否落二宫（Dhan）", "金星（Shukra）的星座主是否与火星（Mangal）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v30`｜PDF [35]｜“Ones 22<sup>nd</sup> /27<sup>th</sup> year will confer marriage, if Shukra is in Yuvati from the 8<sup>th</sup> Bhava (i.e. Dhan from Lagna), while his dispositor is yuti with Mangal.”


## 四路查书计划

### 支持路

- Shukra is in Yuvati from the 8th Bhava (i.e. Dhan from Lagna) dispositor yuti with Mangal marriage
- 金星落八宫起第七宫 即二宫 星座主与火星同宫 第22年 第27年 婚期

### 反例或取消路

- An exchange between the Lords of Dhan and Labh will bring marriage 13 years after birth
- Shukra in Dhan, while Yuvati Lord is in Labh will give marriage at the age of 10, or 16

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34) Yuvati Lord is in a benefic’s Bhava marry at the age of 5, or 9
- Shani is in Yuvati counted from Shukr 从行星起算宫位的算法

### 判断方法路

- Effects of Yuvati Bhava marriage timing rules Shukra dispositor
- 判断婚期应检查哪些行星与宫位

## 上游问题

- 无

## 停止条件

- 缺少金星（Shukra）落宫事实时停止。
- 缺少金星星座主与火星（Mangal）是否同宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
