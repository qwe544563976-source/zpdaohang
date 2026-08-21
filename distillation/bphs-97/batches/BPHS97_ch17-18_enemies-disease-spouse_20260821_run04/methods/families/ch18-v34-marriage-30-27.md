---
method: ch18-v34-marriage-30-27
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 婚期30岁与27岁：金星落上升宫、七宫主落七宫本身

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会在30岁或27岁结婚
- 金星落上升宫、七宫主落本宫时婚期在哪一年

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 金星（Shukra）是否落上升宫（Lagna）
- 七宫主（Yuvati's Lord）是否落本宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v34-marriage-30-27.step-001

- 动作：核对金星（Shukra）是否落上升宫（Lagna），并核对七宫主（Yuvati's Lord）是否落七宫（Yuvati）本身，判断婚期。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；原文只给30与27两个岁数。
- 原文最小意思：金星（Shukra）落上升宫（Lagna），且七宫主（Yuvati's Lord）落本宫、即落七宫（Yuvati）本身时，命主在30岁或27岁成婚。
- 本步骤产出事实：["金星落上升宫且七宫主落本宫主30岁或27岁成婚判定"]
- 所需事实：["金星（Shukra）是否落上升宫（Lagna）", "七宫主（Yuvati's Lord）是否落本宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落上升宫（Lagna）"}, {"fact_key": "七宫主（Yuvati's Lord）是否落本宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断婚姻幸福与否。", "不得把30岁与27岁之外的岁数也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：金星（Shukra）是否落上升宫（Lagna）、七宫主（Yuvati's Lord）是否落本宫。
- 缺失即停字段：["金星（Shukra）是否落上升宫（Lagna）", "七宫主（Yuvati's Lord）是否落本宫"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v34`｜PDF [35]｜“The native will marry at 30, or 27, if Shukra is in Lagna, while the 7<sup>th</sup> Lord is in Yuvati itself.”


## 四路查书计划

### 支持路

- The native will marry at 30, or 27, if Shukra is in Lagna, while the 7th Lord is in Yuvati itself
- 金星落上升宫 七宫主落本宫 30岁 27岁 婚期

### 反例或取消路

- Shukra in Dhan, while Yuvati Lord is in Labh will give marriage at the age of 10, or 16
- If Yuvati Lord is in a benefic’s Bhava, while Shukra is exalted, or is in own Rāśi, the native will marry at the age of 5, or 9

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34)
- If Yuvati’s Lord is in Yuvati Bhava, the native will be endowed with happiness through wife

### 判断方法路

- 判断婚期时金星（Shukra）落宫怎么用

## 上游问题

- 无

## 停止条件

- 缺少金星（Shukra）落宫事实时停止。
- 缺少七宫主（Yuvati's Lord）是否落本宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
