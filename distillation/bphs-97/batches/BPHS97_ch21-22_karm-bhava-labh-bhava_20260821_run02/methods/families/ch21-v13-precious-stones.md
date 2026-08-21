---
method: ch21-v13-precious-stones
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 获得宝石：十宫主落十一宫、十一宫主落一宫、金星落十宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子会不会有贵重宝石
- 我的珠宝首饰运怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否落十一宫（Labh）
- 十一宫主（Labh's Lord）是否落上升宫（Lagna）
- 金星（Shukra）是否落十宫（Karm）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v13-precious-stones.step-001

- 动作：核对十宫主（Karm's Lord）、十一宫主（Labh's Lord）与金星（Shukra）三者的落宫，判断命主是否获得宝石。
- 适用范围：仅限本命盘十宫（Karm）主题下的宝石所得；原文三个条件是同时成立的合取；原文未给数量、时间与上升限定；一宫在本偈的原文写法是 Tanu Bhava。
- 原文最小意思：十宫主落十一宫、十一宫主落一宫（Tanu Bhava）、金星落十宫时，命主获得宝石。
- 本步骤产出事实：["十宫主落十一宫得宝石判定"]
- 所需事实：["十宫主（Karm's Lord）是否落十一宫（Labh）", "十一宫主（Labh's Lord）是否落上升宫（Lagna）", "金星（Shukra）是否落十宫（Karm）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落十一宫（Labh）"}, {"fact_key": "十一宫主（Labh's Lord）是否落上升宫（Lagna）"}, {"fact_key": "金星（Shukra）是否落十宫（Karm）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断宝石的种类、数量、来源或所得年份。", "不得把三个落宫条件中的任何一个单独当成得宝石的判据。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否落十一宫（Labh）、十一宫主（Labh's Lord）是否落上升宫（Lagna）、金星（Shukra）是否落十宫（Karm）。
- 缺失即停字段：["十宫主（Karm's Lord）是否落十一宫（Labh）", "十一宫主（Labh's Lord）是否落上升宫（Lagna）", "金星（Shukra）是否落十宫（Karm）"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v13`｜PDF [38]｜“Should Karm’s Lord be in Labh, while Labh’s Lord is in Tanu Bhava and Shukra is in Karm, the native will be endowed with precious stones.”


## 四路查书计划

### 支持路

- Should Karm’s Lord be in Labh, while Labh’s Lord is in Tanu Bhava and Shukra is in Karm, the native will be endowed with precious stones
- 十宫主落十一宫 十一宫主落一宫 金星落十宫 宝石

### 反例或取消路

- There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic
- Should Rahu, Surya, Shani and Mangal be in Labh Bhava, the native will incur cessation of his duties

### 适用边界路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava

### 判断方法路

- If Karm’s Lord is in Labh Bhava, the native will be endowed with wealth, happiness and sons
- 判断十宫（Karm）与十一宫（Labh）互涉应检查什么

## 上游问题

- 无

## 停止条件

- 缺少十宫主落宫事实时停止。
- 缺少十一宫主落宫事实时停止。
- 缺少金星落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
