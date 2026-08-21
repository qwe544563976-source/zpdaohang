---
method: ch22-v6-guru-in-labh-chandra-shukra-6000-nishkas
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 拥有6000 Nishkas：木星落十一宫、月亮落二宫、金星落九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子能积下多少家当
- 木星落十一宫是什么财运

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否落十一宫（Labh）
- 月亮（Chandra）是否落二宫（Dhan）
- 金星（Shukra）是否落九宫（Dharm）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch22-v6-guru-in-labh-chandra-shukra-6000-nishkas.step-001

- 动作：核对十一宫（Labh）是否被木星（Guru）占据，并核对二宫（Dhan）与九宫（Dharm）是否分别被月亮（Chandra）与金星（Shukra）占据。
- 适用范围：仅限本命盘十一宫（Labh）收获主题；原文三个落宫是并列前提，且二宫对月亮、九宫对金星的对应次序由原文 respectively 定死；原文未给应期。
- 原文最小意思：十一宫被木星占据，二宫与九宫分别被月亮和金星按落宫占据时，本人拥有6000 Nishkas。
- 本步骤产出事实：["木星落十一宫6000 Nishkas判定"]
- 所需事实：["木星（Guru）是否落十一宫（Labh）", "月亮（Chandra）是否落二宫（Dhan）", "金星（Shukra）是否落九宫（Dharm）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落十一宫（Labh）"}, {"fact_key": "月亮（Chandra）是否落二宫（Dhan）"}, {"fact_key": "金星（Shukra）是否落九宫（Dharm）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把月亮与金星的落宫对调：原文 respectively 已定死二宫配月亮、九宫配金星。", "不得把 6000 Nishkas 换算成任何现代货币金额，也不得据此推断应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落十一宫（Labh）、月亮（Chandra）是否落二宫（Dhan）、金星（Shukra）是否落九宫（Dharm）。
- 缺失即停字段：["木星（Guru）是否落十一宫（Labh）", "月亮（Chandra）是否落二宫（Dhan）", "金星（Shukra）是否落九宫（Dharm）"]
- 原文证据：
  - `bphs-97:santhanam:ch22:v6`｜PDF [39]｜“The native will own 6000 Nishkas, if Labh Bhava is occupied by Guru, while Dhan Bhava and Dharm Bhava are, respectively, taken over by Chandra and Shukra by position.”


## 四路查书计划

### 支持路

- The native will own 6000 Nishkas, if Labh Bhava is occupied by Guru, while Dhan Bhava and Dharm Bhava are, respectively, taken over by Chandra and Shukra by position
- 木星（Guru）落十一宫 月亮（Chandra）落二宫 金星（Shukra）落九宫 6000 Nishkas

### 反例或取消路

- Should the Lords of Dhan and Labh Bhava be relegated to Ari, Randhr, or Vyaya Bhava, while Mangal is in Labh Bhava and Rahu is in Dhan Bhava, the native will lose his wealth on account of royal punishments
- There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic

### 适用边界路

- Indications of Labh Bhava. All articles, son’s wife, income, prosperity, quadrupeds etc. are to be understood from Labh Bhava
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

### 判断方法路

- When Guru is in Labh, Shukra is in Dhan and a benefic is placed in Vyaya Bhava, while Dhan’s Lord is yuti with a benefic, there will be expenses on religious, or charitable grounds
- Should Simh be Putr Bhava and be occupied by Surya himself, as Shani, Chandra and Guru are in Labh Bhava, the native will be very affluent

## 上游问题

- 无

## 停止条件

- 缺少木星落十一宫事实时停止。
- 缺少月亮落二宫事实时停止。
- 缺少金星落九宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
