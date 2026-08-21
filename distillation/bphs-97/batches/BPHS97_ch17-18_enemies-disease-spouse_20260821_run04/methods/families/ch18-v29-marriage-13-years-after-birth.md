---
method: ch18-v29-marriage-13-years-after-birth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 出生后13年成婚：二宫主与十一宫主互换星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我大概几岁结婚
- 二宫主与十一宫主互换主什么婚期

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫主（Dhan's Lord）与十一宫主（Labh's Lord）是否互换星座

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v29-marriage-13-years-after-birth.step-001

- 动作：核对二宫主与十一宫主是否互换星座。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；原文只说 exchange（互换），未指明互换的其他形式；原文本偈用中性的 marriage，未限男女。
- 原文最小意思：二宫主与十一宫主互换星座时，婚姻在出生后13年到来。
- 本步骤产出事实：["出生后13年成婚判定"]
- 所需事实：["二宫主（Dhan's Lord）与十一宫主（Labh's Lord）是否互换星座"]
- 条件关系：{"fact_key": "二宫主（Dhan's Lord）与十一宫主（Labh's Lord）是否互换星座"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断配偶身份或婚姻质量。", "不得把互换扩大成二宫主或十一宫主的单向落宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫主（Dhan's Lord）与十一宫主（Labh's Lord）是否互换星座。
- 缺失即停字段：["二宫主（Dhan's Lord）与十一宫主（Labh's Lord）是否互换星座"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v29`｜PDF [35]｜“An exchange between the Lords of Dhan and Labh will bring marriage 13 years after birth.”


## 四路查书计划

### 支持路

- An exchange between the Lords of Dhan and Labh will bring marriage 13 years after birth
- 二宫主 十一宫主 互换星座 出生后13年 成婚

### 反例或取消路

- Marriage will be in the 15th year, if Dhan Lord is in Labh, while Lagn Lord is in Karm
- Shukra in Dhan, while Yuvati Lord is in Labh will give marriage at the age of 10, or 16

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34)

### 判断方法路

- 判断婚期要看二宫主与十一宫主之间的互换关系

## 上游问题

- 无

## 停止条件

- 缺少二宫主与十一宫主是否互换的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
