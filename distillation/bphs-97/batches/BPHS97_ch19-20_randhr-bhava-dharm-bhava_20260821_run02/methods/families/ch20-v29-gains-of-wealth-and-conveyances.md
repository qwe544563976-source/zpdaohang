---
method: ch20-v29-gains-of-wealth-and-conveyances
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 得财富与车乘：上升主落九宫、九宫主落上升宫、木星落七宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能不能置办车产
- 上升主与九宫主互落又木星落七宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否落九宫（Dharm）
- 九宫主（Dharm's Lord）是否落上升宫（Lagna）
- 木星（Guru）是否落七宫（Yuvati）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v29-gains-of-wealth-and-conveyances.step-001

- 动作：核对上升主（Lagn's Lord）是否落九宫（Dharm）、九宫主（Dharm's Lord）是否落上升宫（Lagn），并核对木星（Guru）是否落七宫（Yuvati）。
- 适用范围：仅限本命盘九宫（Dharm）财运主题；原文未给时间或上升限定。
- 原文最小意思：上升主（Lagn's Lord）落九宫（Dharm）、九宫主（Dharm's Lord）落上升宫（Lagn）、且木星（Guru）落七宫（Yuvati）时，会有财富与车乘的获得。
- 本步骤产出事实：["上升主九宫主互落且木星落七宫主得财富车乘判定"]
- 所需事实：["上升主（Lagn's Lord）是否落九宫（Dharm）", "九宫主（Dharm's Lord）是否落上升宫（Lagna）", "木星（Guru）是否落七宫（Yuvati）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落九宫（Dharm）"}, {"fact_key": "九宫主（Dharm's Lord）是否落上升宫（Lagna）"}, {"fact_key": "木星（Guru）是否落七宫（Yuvati）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、车乘种类或得财年岁。", "不得只凭上升主与九宫主互落就下断语，木星落七宫是原文并列的条件。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否落九宫（Dharm）、九宫主（Dharm's Lord）是否落上升宫（Lagna）、木星（Guru）是否落七宫（Yuvati）。
- 缺失即停字段：["上升主（Lagn's Lord）是否落九宫（Dharm）", "九宫主（Dharm's Lord）是否落上升宫（Lagna）", "木星（Guru）是否落七宫（Yuvati）"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v29`｜PDF [37]｜“Should Lagn’s Lord be in Dharm, as Dharm’s Lord is in Lagn and Guru is in Yuvati, there will be gains of wealth and conveyances.”


## 四路查书计划

### 支持路

- Should Lagn’s Lord be in Dharm, as Dharm’s Lord is in Lagn and Guru is in Yuvati, there will be gains of wealth and conveyances.
- 上升主落九宫 九宫主落上升宫 木星落七宫 财富 车乘

### 反例或取消路

- If Rahu is in the 9<sup>th</sup> from Dharm Bhava, as his dispositor is in Randhr Bhava and Dharm’s Lord is in fall, the native be devoid of fortunes
- Should Shani be in Dharm Bhava along with Chandra, as Lagn’s Lord is in fall, the native will acquire food by begging

### 适用边界路

- One will be fortunate (or affluent), if Dharm’s Lord is in Dharm Bhava with strength
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

### 判断方法路

- These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava and in other manners as well
- 判断财富与车乘要看上升主（Lagn's Lord）与九宫主（Dharm's Lord）的互落

## 上游问题

- 无

## 停止条件

- 缺少上升主（Lagn's Lord）落宫事实时停止。
- 缺少九宫主（Dharm's Lord）落宫事实时停止。
- 缺少木星（Guru）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
