---
method: ch18-v6-many-wives-shani-shukra-rasi
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 多妻：七宫主落土星或金星主管的星座并受吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会不止一次结婚
- 七宫主落土星或金星的星座说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 七宫主（Yuvati's Lord）是否被吉星相照

## 按情况检查的事实

- 七宫主（Yuvati's Lord）是否落土星（Shani）主管的星座
- 七宫主（Yuvati's Lord）是否落金星（Shukra）主管的星座

## 依赖方法

- 无

## 执行步骤

### ch18-v6-many-wives-shani-shukra-rasi.step-001

- 动作：核对七宫主（Yuvati's Lord）是否受吉星相照，并核对它落的是土星还是金星主管的星座。
- 适用范围：仅限本命盘七宫（Yuvati）婚姻数目主题；原文以「wives」立说，属男命框架；原文此处印作「Rashiof」（Rashi of），未给妻子的具体人数。
- 原文最小意思：七宫主落土星主管的星座或金星主管的星座、并受吉星相照时，会有多位妻子。
- 本步骤产出事实：["七宫主落土金星座受吉照主多妻判定"]
- 所需事实：["七宫主（Yuvati's Lord）是否被吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否被吉星相照"}, {"operator": "OR", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落土星（Shani）主管的星座"}, {"fact_key": "七宫主（Yuvati's Lord）是否落金星（Shukra）主管的星座"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "七宫主（Yuvati's Lord）是否被吉星相照"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落土星（Shani）主管的星座"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落土星（Shani）主管的星座"}, "selection_group": "ch18-v6-many-wives-shani-shukra-rasi.step-001:rasi-owner", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落土星（Shani）主管的星座。"}, {"when": {"fact_key": "七宫主（Yuvati's Lord）是否被吉星相照"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落金星（Shukra）主管的星座"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落金星（Shukra）主管的星座"}, "selection_group": "ch18-v6-many-wives-shani-shukra-rasi.step-001:rasi-owner", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落金星（Shukra）主管的星座。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断妻子的具体人数、婚期或先后顺序。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：七宫主（Yuvati's Lord）是否被吉星相照。
- 缺失即停字段：["七宫主（Yuvati's Lord）是否被吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v6`｜PDF [33]｜“If Yuvati Lord is in a Rashiof Shani, or of Shukra and be drishtied by a benefic, there will be many wives.”


## 四路查书计划

### 支持路

- If Yuvati Lord is in a Rashiof Shani, or of Shukra and be drishtied by a benefic, there will be many wives
- 七宫主落土星星座 金星星座 受吉星相照 多妻

### 反例或取消路

- The native will beget a spouse endowed with (the seven principal) virtues 7th Lord is exalted strong Lagna Lord
- Yuvati Lord is in his own Rāśi, or in exaltation full happiness through his wife

### 适用边界路

- One will have two wives Yuvati Bhava, or the 7th Navamsa belong to a eunuch planet
- There will be many wives, if Shukra is in a Dual Rāśi, while its Lord is in exaltation
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- PLURALITY OF WIVES Yuvati Lord Rashi Shani Shukra
- 判断妻子数目应检查什么

## 上游问题

- 无

## 停止条件

- 缺少七宫主是否受吉星相照的事实时停止。
- 土星星座、金星星座两个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
