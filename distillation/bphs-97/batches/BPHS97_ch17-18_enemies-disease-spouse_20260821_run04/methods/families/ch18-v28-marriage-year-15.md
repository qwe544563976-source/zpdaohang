---
method: ch18-v28-marriage-year-15
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第15年成婚：二宫主落十一宫、上升主落十宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我大概几岁结婚
- 二宫主落十一宫又上升主落十宫主什么婚期

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫主（Dhan's Lord）是否落十一宫（Labh）
- 上升主（Lagn's Lord）是否落十宫（Karm）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v28-marriage-year-15.step-001

- 动作：核对二宫主是否落十一宫，并核对上升主是否落十宫。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；本偈的条件全在二宫、十一宫与十宫，不涉及七宫本身；原文本偈用中性的 Marriage，未限男女。
- 原文最小意思：二宫主落十一宫、且上升主落十宫时，婚姻发生在第15年。
- 本步骤产出事实：["第15年成婚判定"]
- 所需事实：["二宫主（Dhan's Lord）是否落十一宫（Labh）", "上升主（Lagn's Lord）是否落十宫（Karm）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落十一宫（Labh）"}, {"fact_key": "上升主（Lagn's Lord）是否落十宫（Karm）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断配偶身份或婚姻质量。", "不得把两个条件拆成任一成立即可。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫主（Dhan's Lord）是否落十一宫（Labh）、上升主（Lagn's Lord）是否落十宫（Karm）。
- 缺失即停字段：["二宫主（Dhan's Lord）是否落十一宫（Labh）", "上升主（Lagn's Lord）是否落十宫（Karm）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v28`｜PDF [35]｜“Marriage will be in the 15<sup>th</sup> year, if Dhan Lord is in Labh, while Lagn Lord is in Karm.”


## 四路查书计划

### 支持路

- Marriage will be in the 15th year, if Dhan Lord is in Labh, while Lagn Lord is in Karm
- 二宫主落十一宫 上升主落十宫 第15年 成婚

### 反例或取消路

- An exchange between the Lords of Dhan and Labh will bring marriage 13 years after birth
- Shukra in Dhan, while Yuvati Lord is in Labh will give marriage at the age of 10, or 16

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34)
- Either the 25th year, or the 33rd year will bring marriage, if Randhr Lord is in Yuvati, as Shukra is in Navamsa Lagna

### 判断方法路

- 判断婚期要看二宫主与上升主分别落在哪一宫

## 上游问题

- 无

## 停止条件

- 缺少二宫主落宫事实时停止。
- 缺少上升主落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
