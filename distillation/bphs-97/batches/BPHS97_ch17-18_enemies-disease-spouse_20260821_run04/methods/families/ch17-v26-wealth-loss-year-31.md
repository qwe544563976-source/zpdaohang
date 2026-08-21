---
method: ch17-v26-wealth-loss-year-31
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第31年因敌破财：十一宫主与六宫主互换星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会因为对头破财
- 三十一岁前后财运怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十一宫主（Labh's Lord）与六宫主（Ari's Lord）是否互换星座

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v26-wealth-loss-year-31.step-001

- 动作：核对十一宫主与六宫主是否互换星座。
- 适用范围：仅限本命盘因敌破财主题；原文只给第31年，未说明损失数额与来源细节。
- 原文最小意思：十一宫主与六宫主互换星座时，第31年会有财物损失。
- 本步骤产出事实：["第31年破财判定"]
- 所需事实：["十一宫主（Labh's Lord）与六宫主（Ari's Lord）是否互换星座"]
- 条件关系：{"fact_key": "十一宫主（Labh's Lord）与六宫主（Ari's Lord）是否互换星座"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断损失数额、财物种类或是否可追回。", "不得把第31年推广到其他年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十一宫主（Labh's Lord）与六宫主（Ari's Lord）是否互换星座。
- 缺失即停字段：["十一宫主（Labh's Lord）与六宫主（Ari's Lord）是否互换星座"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v26`｜PDF [33]｜“Loss of wealth will come to pass during the 31<sup>st</sup> year, if Labh and 6<sup>th</sup> Lords exchange their Rāśis.”


## 四路查书计划

### 支持路

- Loss of wealth will come to pass during the 31st year, if Labh and 6th Lords exchange their Rāśis
- 十一宫主 六宫主 互换星座 破财 第31年

### 反例或取消路

- Combinations for Wealth 招财组合
- Lagn Lord is singly capable of counteracting all evils

### 适用边界路

- Combinations for Penury 贫穷组合的判据
- Effects of Labh’s Lord in Various Bhavas 十一宫主落各宫

### 判断方法路

- 判断破财年份应检查哪两宫的宫主

## 上游问题

- 无

## 停止条件

- 缺少十一宫主与六宫主互换星座的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
