---
method: ch20-v10-fortunes-after-32
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第32岁之后得财运、车乘与名声：九宫主落二宫、二宫主落九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我什么时候开始转运
- 九宫主与二宫主互落说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否落二宫（Dhan）
- 二宫主（Dhan's Lord）是否落九宫（Dharm）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v10-fortunes-after-32.step-001

- 动作：核对九宫主（Dharm's Lord）是否落二宫（Dhan），并核对二宫主（Dhan's Lord）是否落九宫（Dharm）。
- 适用范围：仅限本命盘九宫（Dharm）财运主题；原文把获得时间系在第32岁之后。
- 原文最小意思：九宫主（Dharm's Lord）落二宫（Dhan）、且二宫主（Dhan's Lord）落九宫（Dharm）时，第32岁之后会有财运、车乘与名声的获得。
- 本步骤产出事实：["九宫主落二宫且二宫主落九宫主第32岁后得财运车乘名声判定"]
- 所需事实：["九宫主（Dharm's Lord）是否落二宫（Dhan）", "二宫主（Dhan's Lord）是否落九宫（Dharm）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落二宫（Dhan）"}, {"fact_key": "二宫主（Dhan's Lord）是否落九宫（Dharm）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额或车乘种类。", "不得把第32岁之前的时间也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否落二宫（Dhan）、二宫主（Dhan's Lord）是否落九宫（Dharm）。
- 缺失即停字段：["九宫主（Dharm's Lord）是否落二宫（Dhan）", "二宫主（Dhan's Lord）是否落九宫（Dharm）"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v10`｜PDF [37]｜“Acquisition of fortunes, conveyances and fame will follow the 32<sup>nd</sup> year of age, if Dharm’s Lord is in Dhan, while Dhan’s Lord is in Dharm.”


## 四路查书计划

### 支持路

- Acquisition of fortunes, conveyances and fame will follow the 32<sup>nd</sup> year of age, if Dharm’s Lord is in Dhan, while Dhan’s Lord is in Dharm.
- 九宫主落二宫 二宫主落九宫 第32年 财运 车乘 名声

### 反例或取消路

- If Rahu is in the 9<sup>th</sup> from Dharm Bhava, as his dispositor is in Randhr Bhava and Dharm’s Lord is in fall, the native be devoid of fortunes
- If Karm’s Lord and Sahaj’s Lord are bereft of strength, while Dharm’s Lord is in fall, or combust the native will go begging for his food

### 适用边界路

- One will be fortunate (or affluent), if Dharm’s Lord is in Dharm Bhava with strength
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

### 判断方法路

- These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava and in other manners as well
- 判断财运起运年岁要看九宫（Dharm）与二宫（Dhan）的哪些互落

## 上游问题

- 无

## 停止条件

- 缺少九宫主（Dharm's Lord）落宫事实时停止。
- 缺少二宫主（Dhan's Lord）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
