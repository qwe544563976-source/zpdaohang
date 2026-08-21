---
method: ch18-v25-marriage-year-11
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第11年成婚：金星落角宫、上升主落摩羯座或水瓶座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我大概几岁结婚
- 金星落角宫又上升主落摩羯或水瓶主什么婚期

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 金星（Shukra）是否落角宫
- 本盘上升主（Lagn's Lord）落在哪个星座

## 按情况检查的事实

- 上升主（Lagn's Lord）是否落摩羯座（Makar）
- 上升主（Lagn's Lord）是否落水瓶座（Kumbh）

## 依赖方法

- 无

## 执行步骤

### ch18-v25-marriage-year-11.step-001

- 动作：先核对金星是否落上升起的角宫，再取出上升主所落星座，核对它是摩羯座还是水瓶座。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；原文的角宫以上升（Lagna）起算；原文本偈用中性的 Marriage，未限男女。
- 原文最小意思：金星落上升起的角宫、且上升主落摩羯座或水瓶座时，婚姻发生在第11年。
- 本步骤产出事实：["第11年成婚判定"]
- 所需事实：["金星（Shukra）是否落角宫", "本盘上升主（Lagn's Lord）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落角宫"}, {"fact_key": "本盘上升主（Lagn's Lord）落在哪个星座"}]}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落摩羯座（Makar）"}, {"fact_key": "上升主（Lagn's Lord）是否落水瓶座（Kumbh）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落角宫"}, {"fact_key": "本盘上升主（Lagn's Lord）落在哪个星座"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否落摩羯座（Makar）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落摩羯座（Makar）"}, "selection_group": "ch18-v25-marriage-year-11.step-001:lagn-lord-rasi", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落摩羯座（Makar）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落角宫"}, {"fact_key": "本盘上升主（Lagn's Lord）落在哪个星座"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否落水瓶座（Kumbh）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落水瓶座（Kumbh）"}, "selection_group": "ch18-v25-marriage-year-11.step-001:lagn-lord-rasi", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落水瓶座（Kumbh）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断配偶身份或婚姻质量。", "不得把角宫的起算点从上升改成别的星体。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：金星（Shukra）是否落角宫、本盘上升主（Lagn's Lord）落在哪个星座。
- 缺失即停字段：["金星（Shukra）是否落角宫", "本盘上升主（Lagn's Lord）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v25`｜PDF [34]｜“Marriage will take place during the 11<sup>th</sup> year, if Shukra is in an angle from Lagna, while Lagn Lord is in Makar, or Kumbh.”


## 四路查书计划

### 支持路

- Marriage will take place during the 11th year, if Shukra is in an angle from Lagna, while Lagn Lord is in Makar, or Kumbh
- 金星落角宫 上升主落摩羯座 水瓶座 第11年 成婚

### 反例或取消路

- The native will marry at 12, or l9, if Shukra is in an angle from the Lagna, while Shani is in Yuvati counted from Shukr
- The native will marry at 30, or 27, if Shukra is in Lagna, while the 7th Lord is in Yuvati itself

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34)
- if Shukra is in an angle from the Lagna angle kendra from Lagna marriage

### 判断方法路

- Shukra in an angle from Lagna Lagn Lord Rāśi marriage timing
- 判断婚期要看金星是否落角宫与上升主所落星座

## 上游问题

- 无

## 停止条件

- 缺少金星是否落角宫的事实时停止。
- 缺少上升主所落星座事实时停止。
- 摩羯座与水瓶座两个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
