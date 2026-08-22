---
method: ch24-v18-dhan-lord-ari-with-benefic
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 从敌人处得财：二宫主落六宫（Ari）并与吉星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会从对头身上赚到钱
- 二宫主落六宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫主（Dhan's Lord）是否落六宫（Ari）
- 二宫主（Dhan's Lord）是否与吉星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v18-dhan-lord-ari-with-benefic.step-001

- 动作：先核对二宫主（Dhan's Lord）是否落六宫（Ari），再核对它是否与吉星同宫。
- 适用范围：仅限本命盘二宫主（Dhan's Lord）落宫主题；原文写 along with a benefic，即与吉星同宫；吉星名册以本书 ch03:v11 的界定为准；同偈另有与凶星同宫的一支，另立方法；原文未给财富数额、敌人身份或时间限定。
- 原文最小意思：二宫主（Dhan's Lord）落六宫（Ari）并与吉星同宫时，命主会通过他的敌人获得财富。
- 本步骤产出事实：["二宫主落六宫与吉星同宫的得财判定"]
- 所需事实：["二宫主（Dhan's Lord）是否落六宫（Ari）", "二宫主（Dhan's Lord）是否与吉星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落六宫（Ari）"}, {"fact_key": "二宫主（Dhan's Lord）是否与吉星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、敌人身份或得财时间。", "不得把与吉星同宫的一支与同偈与凶星同宫的一支合并使用。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫主（Dhan's Lord）是否落六宫（Ari）、二宫主（Dhan's Lord）是否与吉星同宫。
- 缺失即停字段：["二宫主（Dhan's Lord）是否落六宫（Ari）", "二宫主（Dhan's Lord）是否与吉星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v18`｜PDF [42]｜“If Dhan’s Lord is in Ari Bhava along with a benefic, the native will gain wealth through his enemies; if Dhan’s Lord is yuti with a malefic, there will be loss through enemies apart from mutilation of shanks.”


## 四路查书计划

### 支持路

- If Dhan’s Lord is in Ari Bhava along with a benefic, the native will gain wealth through his enemies
- 二宫主落六宫 与吉星同宫 从敌人处得财

### 反例或取消路

- if Dhan’s Lord is yuti with a malefic, there will be loss through enemies apart from mutilation of shanks
- LOSS THROUGH ENEMIES. Loss of wealth will come to pass during the 31<sup>st</sup> year, if Labh and 6<sup>th</sup> Lords exchange their Rāśis

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Ari Bhava. Maternal uncle, doubts about death, enemies, ulcers, stepmother etc. are to be estimated from Ari Bhava

### 判断方法路

- Effects of Dhan’s Lord in Various Bhavas (up to Sloka 24)
- 二宫主落六宫时吉星与凶星同宫各自怎么判

## 上游问题

- 无

## 停止条件

- 缺少二宫主是否落六宫（Ari）的事实时停止。
- 缺少二宫主是否与吉星同宫的事实时停止。
- 吉星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
