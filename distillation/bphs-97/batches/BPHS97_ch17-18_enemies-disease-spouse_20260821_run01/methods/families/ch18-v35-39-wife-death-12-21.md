---
method: ch18-v35-39-wife-death-12-21
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 妻子在第12年与第21年去世：金星落八宫、其星座主落土星星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我妻子可能在我哪一年去世
- 金星落八宫对妻子寿命有什么说法

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 金星（Shukra）是否落八宫（Randhr）
- 金星（Shukra）的星座主是否落土星（Shani）主管的星座

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v35-39-wife-death-12-21.step-001

- 动作：核对金星（Shukra）是否落八宫（Randhr），并核对金星的星座主是否落在土星（Shani）主管的星座，判断妻子去世的年份。
- 适用范围：仅限本命盘七宫（Yuvati）配偶存亡主题；原文以「wife」立说，属男命框架；原文「his dispositor」的 his 指同句的金星（Shukra）；原文只给第12与第21年两个年份。
- 原文最小意思：金星（Shukra）落八宫（Randhr），且金星的星座主落在土星（Shani）主管的星座时，妻子在命主第12或第21年（年龄）去世。
- 本步骤产出事实：["金星落八宫且其星座主落土星星座主妻子第12或第21年去世判定"]
- 所需事实：["金星（Shukra）是否落八宫（Randhr）", "金星（Shukra）的星座主是否落土星（Shani）主管的星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落八宫（Randhr）"}, {"fact_key": "金星（Shukra）的星座主是否落土星（Shani）主管的星座"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断死因或再婚。", "不得把第12年与第21年之外的年份也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：金星（Shukra）是否落八宫（Randhr）、金星（Shukra）的星座主是否落土星（Shani）主管的星座。
- 缺失即停字段：["金星（Shukra）是否落八宫（Randhr）", "金星（Shukra）的星座主是否落土星（Shani）主管的星座"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v35-39`｜PDF [35]｜“If Shukra is in Randhr, while his dispositor is in a Rashiof Shani, death of wife will take place during the native’s 12<sup>th</sup> , or 21<sup>st</sup> year of age.”


## 四路查书计划

### 支持路

- If Shukra is in Randhr, while his dispositor is in a Rashiof Shani, death of wife will take place during the native’s 12th, or 21st year of age
- 金星落八宫 星座主落土星星座 第12年 第21年 妻子去世

### 反例或取消路

- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)
- If Yuvati Lord is in a Rashiof Shani, or of Shukra and be drishtied by a benefic, there will be many wives

### 适用边界路

- Loss of wife will occur in the 18th year, or 33rd year of age of the native, if Yuvati Lord is in fall, while Shukra is in Randhr
- If Shukra yuti a malefic in any Bhava the native will lose his wife

### 判断方法路

- Effects of Yuvati Bhava dispositor Rashi of Shani wife death
- 判断妻子寿命应检查什么

## 上游问题

- 无

## 停止条件

- 缺少金星（Shukra）落宫事实时停止。
- 缺少金星星座主所落星座的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
