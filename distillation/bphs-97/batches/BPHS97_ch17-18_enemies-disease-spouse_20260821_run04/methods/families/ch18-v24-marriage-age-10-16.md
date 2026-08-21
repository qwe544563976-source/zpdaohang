---
method: ch18-v24-marriage-age-10-16
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 10岁或16岁成婚：金星落二宫、七宫主落十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我大概几岁结婚
- 金星落二宫又七宫主落十一宫主什么婚期

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 金星（Shukra）是否落二宫（Dhan）
- 七宫主（Yuvati's Lord）是否落十一宫（Labh）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v24-marriage-age-10-16.step-001

- 动作：核对金星是否落二宫，并核对七宫主是否落十一宫。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；两个条件在原文里同时成立；原文本偈用中性的 marriage，未限男女。
- 原文最小意思：金星落二宫、且七宫主落十一宫时，会在10岁或16岁成婚。
- 本步骤产出事实：["第10或16岁成婚判定"]
- 所需事实：["金星（Shukra）是否落二宫（Dhan）", "七宫主（Yuvati's Lord）是否落十一宫（Labh）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落二宫（Dhan）"}, {"fact_key": "七宫主（Yuvati's Lord）是否落十一宫（Labh）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断配偶身份或婚姻质量。", "不得把两个条件拆成任一成立即可。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：金星（Shukra）是否落二宫（Dhan）、七宫主（Yuvati's Lord）是否落十一宫（Labh）。
- 缺失即停字段：["金星（Shukra）是否落二宫（Dhan）", "七宫主（Yuvati's Lord）是否落十一宫（Labh）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v24`｜PDF [34]｜“Shukra in Dhan, while Yuvati Lord is in Labh will give marriage at the age of 10, or 16.”


## 四路查书计划

### 支持路

- Shukra in Dhan, while Yuvati Lord is in Labh will give marriage at the age of 10, or 16
- 金星落二宫 七宫主落十一宫 10岁 16岁 成婚

### 反例或取消路

- Marriage will be in the 15th year, if Dhan Lord is in Labh, while Lagn Lord is in Karm
- An exchange between the Lords of Dhan and Labh will bring marriage 13 years after birth

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34)
- Should Yuvati Lord be in Vyaya, while the natal Lord is in Yuvati in Navamsa, marriage will be in 23rd/26th year of age

### 判断方法路

- 判断婚期要看金星与七宫主分别落在哪一宫

## 上游问题

- 无

## 停止条件

- 缺少金星落宫事实时停止。
- 缺少七宫主落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
