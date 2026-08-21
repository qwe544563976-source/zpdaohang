---
method: ch15-v8-cows-and-buffaloes
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 牲畜瑜伽：日在四宫、月土在九宫、火在十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有牲畜家产
- 我有没有养牛的运

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否落四宫（Bandhu）
- 月亮（Chandra）是否落九宫（Dharm）
- 土星（Shani）是否落九宫（Dharm）
- 火星（Mangal）是否落十一宫（Labh Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch15-v8-cows-and-buffaloes.step-001

- 动作：核对太阳、月亮、土星、火星是否同时落在原文指定的四个位置，判断此瑜伽是否成立。
- 适用范围：仅限原文这一组四星同时成立的瑜伽与牲畜结果；原文未给时间限定。
- 原文最小意思：太阳（Surya）落四宫（Bandhu）、月亮（Chandra）与土星（Shani）落九宫（Dharm）、火星（Mangal）落十一宫（Labh Bhava）时，此瑜伽给命主带来母牛与水牛。
- 本步骤产出事实：["牲畜瑜伽成立判定"]
- 所需事实：["太阳（Surya）是否落四宫（Bandhu）", "月亮（Chandra）是否落九宫（Dharm）", "土星（Shani）是否落九宫（Dharm）", "火星（Mangal）是否落十一宫（Labh Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落四宫（Bandhu）"}, {"fact_key": "月亮（Chandra）是否落九宫（Dharm）"}, {"fact_key": "土星（Shani）是否落九宫（Dharm）"}, {"fact_key": "火星（Mangal）是否落十一宫（Labh Bhava）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断牲畜数量或得畜年份。", "四个位置必须同时成立，不得只凭其中一两个位置下结论。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落四宫（Bandhu）、月亮（Chandra）是否落九宫（Dharm）、土星（Shani）是否落九宫（Dharm）、火星（Mangal）是否落十一宫（Labh Bhava）。
- 缺失即停字段：["太阳（Surya）是否落四宫（Bandhu）", "月亮（Chandra）是否落九宫（Dharm）", "土星（Shani）是否落九宫（Dharm）", "火星（Mangal）是否落十一宫（Labh Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v8`｜PDF [30]｜“Surya in Bandhu, Chandra and Shani in Dharm and Mangal in Labh Bhava; this Yoga will confer cows and buffaloes on the native.”


## 四路查书计划

### 支持路

- Surya in Bandhu Chandra Shani in Dharm Mangal in Labh cows buffaloes
- 太阳四宫 月土九宫 火十一宫 牲畜瑜伽

### 反例或取消路

- malefic in Bandhu loss of cattle
- 牲畜损失 相关组合

### 适用边界路

- does this Yoga require all four placements together
- 此瑜伽是否要求四个位置同时成立

### 判断方法路

- how to judge cattle and quadrupeds in BPHS
- 判断牲畜家产要查什么组合

## 上游问题

- 无

## 停止条件

- 四颗行星的落宫事实缺任何一条时停止。
- 只有部分位置成立时不得下此瑜伽结论。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
