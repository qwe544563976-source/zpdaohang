---
method: ch20-v27-28-fortunes-after-20
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第20年之后得丰厚财运：木星落九宫、九宫主落角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的财运什么时候开始好转
- 木星落九宫又九宫主落角宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否落九宫（Dharm）
- 九宫主（Dharm's Lord）是否落角宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v27-28-fortunes-after-20.step-001

- 动作：核对木星（Guru）是否落九宫（Dharm），并核对九宫主（Dharm's Lord）是否落上升起算的角宫。
- 适用范围：仅限本命盘九宫（Dharm）财运主题；原文「its Lord」的 its，句内先行词是九宫（Dharm）；原文把获得时间系在第20年之后。
- 原文最小意思：木星（Guru）落九宫（Dharm）、且九宫主落上升（Lagn）起算的角宫时，第20年之后会获得丰厚的财运。
- 本步骤产出事实：["木星落九宫且九宫主落角宫主第20年后财运丰厚判定"]
- 所需事实：["木星（Guru）是否落九宫（Dharm）", "九宫主（Dharm's Lord）是否落角宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落九宫（Dharm）"}, {"fact_key": "九宫主（Dharm's Lord）是否落角宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额或来源。", "不得把第20年之前的时间也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落九宫（Dharm）、九宫主（Dharm's Lord）是否落角宫。
- 缺失即停字段：["木星（Guru）是否落九宫（Dharm）", "九宫主（Dharm's Lord）是否落角宫"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v27-28`｜PDF [37]｜“Abundant fortunes be acquired after the 20<sup>th</sup> year, if Dharm has Guru in it, as its Lord is in an angle from Lagn.”


## 四路查书计划

### 支持路

- Abundant fortunes be acquired after the 20<sup>th</sup> year, if Dharm has Guru in it, as its Lord is in an angle from Lagn.
- 木星落九宫 九宫主落角宫 第20年之后 丰厚财运

### 反例或取消路

- If Rahu is in the 9<sup>th</sup> from Dharm Bhava, as his dispositor is in Randhr Bhava and Dharm’s Lord is in fall, the native be devoid of fortunes
- Should Shani be in Dharm Bhava along with Chandra, as Lagn’s Lord is in fall, the native will acquire food by begging

### 适用边界路

- Should Guru be in Dharm Bhava, while Dharm’s Lord is in an angle and Lagn’s Lord is endowed with strength, one will be extremely fortunate
- One will be fortunate (or affluent), if Dharm’s Lord is in Dharm Bhava with strength
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

### 判断方法路

- These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava and in other manners as well
- 判断财运起运年岁要看木星（Guru）与九宫主（Dharm's Lord）的落宫

## 上游问题

- 无

## 停止条件

- 缺少木星（Guru）落宫事实时停止。
- 缺少九宫主（Dharm's Lord）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
