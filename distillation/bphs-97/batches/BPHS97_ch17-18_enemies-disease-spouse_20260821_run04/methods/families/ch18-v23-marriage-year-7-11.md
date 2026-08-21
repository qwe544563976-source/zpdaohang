---
method: ch18-v23-marriage-year-7-11
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第7或第11个年岁成婚：太阳落七宫、太阳所落星座主星与金星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我大概几岁结婚
- 太阳落七宫对婚期有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否落七宫（Yuvati）
- 太阳（Surya）所落星座的主星是否与金星（Shukra）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v23-marriage-year-7-11.step-001

- 动作：核对太阳是否落七宫，再核对太阳所落星座的主星是否与金星同宫。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；「his dispositor」指太阳所落星座的主星；原文按 year of age（年岁）计；原文本偈用中性的 marriage，未限男女。
- 原文最小意思：太阳落七宫、且太阳所落星座的主星与金星同宫时，成婚在第7个或第11个年岁。
- 本步骤产出事实：["第7或第11年岁成婚判定"]
- 所需事实：["太阳（Surya）是否落七宫（Yuvati）", "太阳（Surya）所落星座的主星是否与金星（Shukra）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落七宫（Yuvati）"}, {"fact_key": "太阳（Surya）所落星座的主星是否与金星（Shukra）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断配偶身份或婚姻质量。", "不得把年岁改写成别的纪年方式。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落七宫（Yuvati）、太阳（Surya）所落星座的主星是否与金星（Shukra）同宫。
- 缺失即停字段：["太阳（Surya）是否落七宫（Yuvati）", "太阳（Surya）所落星座的主星是否与金星（Shukra）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v23`｜PDF [34]｜“If Surya is in Yuvati, while his dispositor is yuti with Shukr, there will be marriage at 7<sup>th</sup> , or 11<sup>th</sup> year of age.”


## 四路查书计划

### 支持路

- If Surya is in Yuvati, while his dispositor is yuti with Shukr, there will be marriage at 7th, or 11th year of age
- 太阳落七宫 太阳的星座主星与金星同宫 第7年 第11年 成婚

### 反例或取消路

- Ones 22nd/27th year will confer marriage, if Shukra is in Yuvati from the 8th Bhava (i.e. Dhan from Lagna), while his dispositor is yuti with Mangal
- The native will marry at 30, or 27, if Shukra is in Lagna, while the 7th Lord is in Yuvati itself

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34)
- The native will befriend barren females, if Surya is in Yuvati

### 判断方法路

- 判断婚期要看太阳落宫与其星座主星的同宫关系

## 上游问题

- 无

## 停止条件

- 缺少太阳落宫事实时停止。
- 缺少太阳所落星座主星与金星是否同宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
