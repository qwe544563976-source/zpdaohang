---
method: ch22-v9-labh-dhan-lords-interchange-after-marriage
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 婚后积聚丰厚财运：十一宫主落二宫、二宫主落十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我结婚以后财运会不会变好
- 二宫主与十一宫主互换是什么效果

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十一宫主（Labh's Lord）是否落二宫（Dhan）
- 二宫主（Dhan's Lord）是否落十一宫（Labh）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch22-v9-labh-dhan-lords-interchange-after-marriage.step-001

- 动作：核对十一宫主（Labh's Lord）是否落二宫（Dhan），同时核对二宫主（Dhan's Lord）是否落十一宫（Labh）。
- 适用范围：仅限本命盘十一宫（Labh）收获主题；两宫主须互换落宫，缺一不成立；原文把应期定在婚后，未给具体年岁。
- 原文最小意思：十一宫主落二宫、二宫主落十一宫时，本人在婚后积聚丰厚的财运。
- 本步骤产出事实：["十一宫主二宫主互换婚后财运判定"]
- 所需事实：["十一宫主（Labh's Lord）是否落二宫（Dhan）", "二宫主（Dhan's Lord）是否落十一宫（Labh）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落二宫（Dhan）"}, {"fact_key": "二宫主（Dhan's Lord）是否落十一宫（Labh）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断婚期本身，也不得推断配偶带来多少财产。", "不得只凭单向落宫就下断：原文要求两宫主互换。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十一宫主（Labh's Lord）是否落二宫（Dhan）、二宫主（Dhan's Lord）是否落十一宫（Labh）。
- 缺失即停字段：["十一宫主（Labh's Lord）是否落二宫（Dhan）", "二宫主（Dhan's Lord）是否落十一宫（Labh）"]
- 原文证据：
  - `bphs-97:santhanam:ch22:v9`｜PDF [40]｜“If Labh’s Lord is in Dhan Bhava, as Dhan’s Lord is in Labh Bhava, one will amass abundant fortunes after marriage.”


## 四路查书计划

### 支持路

- If Labh’s Lord is in Dhan Bhava, as Dhan’s Lord is in Labh Bhava, one will amass abundant fortunes after marriage
- 十一宫主落二宫（Dhan） 二宫主落十一宫（Labh） 婚后 财运

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic
- There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic

### 适用边界路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- Indications of Labh Bhava. All articles, son’s wife, income, prosperity, quadrupeds etc. are to be understood from Labh Bhava

### 判断方法路

- If Dhan Lord is in Labh, while the Lord of Labh in Dhan, wealth will be acquired by the native. Alternately these two Lords may join in an angle, or in a trine
- If Dhan’s Lord is in Labh Bhava, the native will have all kinds of wealth, be ever diligent, honourable and famous

## 上游问题

- 无

## 停止条件

- 缺少十一宫主落二宫事实时停止。
- 缺少二宫主落十一宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
