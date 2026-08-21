---
method: ch18-v22-marriage-age-5-9
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 5岁或9岁成婚：七宫主落吉星宫位、金星入旺或落本宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我大概几岁结婚
- 七宫主落吉星宫位又金星入旺主什么婚期

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 七宫主（Yuvati's Lord）是否落吉星主管的宫位（Bhava）

## 按情况检查的事实

- 金星（Shukra）是否入旺
- 金星（Shukra）是否落本宫

## 依赖方法

- 无

## 执行步骤

### ch18-v22-marriage-age-5-9.step-001

- 动作：先核对七宫主是否落在吉星主管的宫位，再核对金星是入旺还是落本宫。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；原文夹注「or in Dharm, as Subha Rashiso means」是译本对 Subha Rashi 一词的解读，只作版本注记，结论强度不与作者自断等同；本偈起为「TIME OF MARRIAGE (upto Sloka 34)」时间段落；原文本偈用中性的 marry，未限男女。
- 原文最小意思：七宫主落吉星主管的宫位（原文注：据 Subha Rashi 一说即落九宫），同时金星入旺或落本宫时，命主会在5岁或9岁成婚。
- 本步骤产出事实：["第5或9岁成婚判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "七宫主（Yuvati's Lord）是否落吉星主管的宫位（Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "七宫主（Yuvati's Lord）是否落吉星主管的宫位（Bhava）"}]}, {"operator": "OR", "operands": [{"fact_key": "金星（Shukra）是否入旺"}, {"fact_key": "金星（Shukra）是否落本宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "七宫主（Yuvati's Lord）是否落吉星主管的宫位（Bhava）"}]}, "required_fact_keys": ["金星（Shukra）是否入旺"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否入旺"}, "selection_group": "ch18-v22-marriage-age-5-9.step-001:shukra-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否入旺。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "七宫主（Yuvati's Lord）是否落吉星主管的宫位（Bhava）"}]}, "required_fact_keys": ["金星（Shukra）是否落本宫"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落本宫"}, "selection_group": "ch18-v22-marriage-age-5-9.step-001:shukra-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落本宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 Dharm 一说当作与吉星宫位同等强度的条件。", "不得据此推断配偶身份或婚姻质量。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、七宫主（Yuvati's Lord）是否落吉星主管的宫位（Bhava）。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "七宫主（Yuvati's Lord）是否落吉星主管的宫位（Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v22`｜PDF [34]｜“If Yuvati Lord is in a benefic’s Bhava (or in Dharm, as Subha Rashiso means), while Shukra is exalted, or is in own Rāśi, the native will marry at the age of 5, or 9.”


## 四路查书计划

### 支持路

- If Yuvati Lord is in a benefic’s Bhava, while Shukra is exalted, or is in own Rāśi, the native will marry at the age of 5, or 9
- 七宫主落吉星宫位 金星入旺 本宫 5岁 9岁 成婚

### 反例或取消路

- The native will marry at 30, or 27, if Shukra is in Lagna, while the 7th Lord is in Yuvati itself
- If Chandra is in Yuvati, as Yuvati Lord is in Vyaya and the Karaka (indicator Shukr) is bereft of strength, the native will not be endowed with marital happiness

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34)
- or in Dharm, as Subha Rashiso means benefic’s Bhava

### 判断方法路

- how to time marriage from Yuvati Lord and Shukra dignity BPHS
- 判断婚期要看七宫主所落宫位与金星的尊贵状态

## 上游问题

- 无

## 停止条件

- 缺少吉星名册事实时停止。
- 缺少七宫主是否落吉星宫位的事实时停止。
- 金星入旺与落本宫两个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
