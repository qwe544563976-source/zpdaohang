---
method: ch20-v30-devoid-of-fortunes
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 没有财运：罗睺落九宫起第九宫、其星座主落八宫、九宫主落陷

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我为什么一直没有财运
- 罗睺落九宫起第九宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 罗睺（Rahu）是否落从九宫（Dharm）起算的第九宫
- 罗睺（Rahu）的星座主是否落八宫（Randhr）
- 九宫主（Dharm's Lord）是否落陷

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v30-devoid-of-fortunes.step-001

- 动作：核对罗睺（Rahu）是否落在从九宫（Dharm）起算的第九宫、罗睺的星座主是否落八宫（Randhr），并核对九宫主（Dharm's Lord）是否落陷。
- 适用范围：仅限本命盘九宫（Dharm）财运主题；原文「his dispositor」的 his，句内先行词是罗睺（Rahu）；原文未给时间限定。
- 原文最小意思：罗睺（Rahu）落从九宫（Dharm）起算的第九宫、其星座主落八宫（Randhr）、且九宫主（Dharm's Lord）落陷时，命主没有财运。
- 本步骤产出事实：["罗睺落九宫起第九宫且星座主落八宫九宫主落陷主没有财运判定"]
- 所需事实：["罗睺（Rahu）是否落从九宫（Dharm）起算的第九宫", "罗睺（Rahu）的星座主是否落八宫（Randhr）", "九宫主（Dharm's Lord）是否落陷"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "罗睺（Rahu）是否落从九宫（Dharm）起算的第九宫"}, {"fact_key": "罗睺（Rahu）的星座主是否落八宫（Randhr）"}, {"fact_key": "九宫主（Dharm's Lord）是否落陷"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断贫困的程度或起止年岁。", "不得把从九宫（Dharm）起算的第九宫换成从上升（Lagn）起算的宫位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：罗睺（Rahu）是否落从九宫（Dharm）起算的第九宫、罗睺（Rahu）的星座主是否落八宫（Randhr）、九宫主（Dharm's Lord）是否落陷。
- 缺失即停字段：["罗睺（Rahu）是否落从九宫（Dharm）起算的第九宫", "罗睺（Rahu）的星座主是否落八宫（Randhr）", "九宫主（Dharm's Lord）是否落陷"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v30`｜PDF [38]｜“If Rahu is in the 9<sup>th</sup> from Dharm Bhava, as his dispositor is in Randhr Bhava and Dharm’s Lord is in fall, the native be devoid of fortunes.”


## 四路查书计划

### 支持路

- If Rahu is in the 9<sup>th</sup> from Dharm Bhava, as his dispositor is in Randhr Bhava and Dharm’s Lord is in fall, the native be devoid of fortunes.
- 罗睺落九宫起第九宫 星座主落八宫 九宫主落陷 没有财运

### 反例或取消路

- One will be fortunate (or affluent), if Dharm’s Lord is in Dharm Bhava with strength
- Should Guru be in Dharm Bhava, while Dharm’s Lord is in an angle and Lagn’s Lord is endowed with strength, one will be extremely fortunate

### 适用边界路

- One will enjoy abundant fortunes, if Shukra is in deep exaltation and be in the company of Dharm’s Lord, as Shani is in Sahaj
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

### 判断方法路

- These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava and in other manners as well
- 判断财运匮乏要看罗睺（Rahu）与九宫主（Dharm's Lord）的哪些状态

## 上游问题

- 无

## 停止条件

- 缺少罗睺（Rahu）落宫事实时停止。
- 缺少罗睺星座主落宫事实时停止。
- 缺少九宫主（Dharm's Lord）是否落陷的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
