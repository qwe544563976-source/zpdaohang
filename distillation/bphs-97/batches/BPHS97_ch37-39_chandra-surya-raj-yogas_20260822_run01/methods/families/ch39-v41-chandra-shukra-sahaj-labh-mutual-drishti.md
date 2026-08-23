---
method: ch39-v41-chandra-shukra-sahaj-labh-mutual-drishti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮与金星互处三宫十一宫并互照：贵格成立

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮金星隔着三宫十一宫说明什么
- 我有没有贵格

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）与金星（Shukra）是否互处三宫与十一宫（Sahaj、Labh）
- 月亮（Chandra）与金星（Shukra）是否互相相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v41-chandra-shukra-sahaj-labh-mutual-drishti.step-001

- 动作：核对月亮（Chandra）与金星（Shukra）是否互处三宫与十一宫，并互相相照。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文另有 while they are placed elsewhere 一语，未界定所指，本方法不据此细分情形；原文没有时间限定。
- 原文最小意思：月亮（Chandra）与金星（Shukra）互处三宫与十一宫（Sahaj and Labh Bhava）并互相相照时，Raj Yog 成立。
- 本步骤产出事实：["月亮金星互处三宫十一宫的贵格判定"]
- 所需事实：["月亮（Chandra）与金星（Shukra）是否互处三宫与十一宫（Sahaj、Labh）", "月亮（Chandra）与金星（Shukra）是否互相相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）与金星（Shukra）是否互处三宫与十一宫（Sahaj、Labh）"}, {"fact_key": "月亮（Chandra）与金星（Shukra）是否互相相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文界定 while they are placed elsewhere 的所指。", "不得据此推断收益、婚姻或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）与金星（Shukra）是否互处三宫与十一宫（Sahaj、Labh）、月亮（Chandra）与金星（Shukra）是否互相相照。
- 缺失即停字段：["月亮（Chandra）与金星（Shukra）是否互处三宫与十一宫（Sahaj、Labh）", "月亮（Chandra）与金星（Shukra）是否互相相照"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v41`｜PDF [84]｜“Should Chandra and Shukra be mutually in Sahaj and Labh Bhava and receiving Drishtis from each other, while they are placed elsewhere, a Raj Yog is obtained.”


## 四路查书计划

### 支持路

- Should Chandra and Shukra be mutually in Sahaj and Labh Bhava and receiving Drishtis from each other, while they are placed elsewhere, a Raj Yog is obtained
- 月亮金星互处三宫十一宫 互相相照 贵格

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Sahaj, Ari, Karm and Labh Bhava are Upachaya Bhavas
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少月亮与金星互处三宫十一宫的事实时停止。
- 缺少两者互照的事实时停止。
- 原文的 while they are placed elsewhere 所指未定，若需据此细分情形则停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
