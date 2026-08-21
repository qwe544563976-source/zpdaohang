---
method: ch13-v9-religious-charitable-expenses
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 开销用于宗教慈善：木星落十一宫、金星落二宫、十二宫有吉星且二宫主与吉星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的钱会花在什么地方
- 我会不会把钱用在宗教或慈善上

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否落十一宫（Labh）
- 金星（Shukra）是否落二宫（Dhan）
- 十二宫（Vyaya）是否被吉星占据
- 二宫主（Dhan's Lord）是否与吉星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch13-v9-religious-charitable-expenses.step-001

- 动作：核对木星落十一宫、金星落二宫、十二宫内有吉星、二宫主与吉星同宫四项是否同时成立，判断开销去向。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；原文四个条件同时要求，未给时间限定。
- 原文最小意思：木星（Guru）落十一宫（Labh）、金星（Shukra）落二宫（Dhan）、十二宫（Vyaya Bhava）内有吉星，且二宫主与吉星同宫时，命主的开销花在宗教或慈善用途上。
- 本步骤产出事实：["宗教慈善开销判定"]
- 所需事实：["木星（Guru）是否落十一宫（Labh）", "金星（Shukra）是否落二宫（Dhan）", "十二宫（Vyaya）是否被吉星占据", "二宫主（Dhan's Lord）是否与吉星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落十一宫（Labh）"}, {"fact_key": "金星（Shukra）是否落二宫（Dhan）"}, {"fact_key": "十二宫（Vyaya）是否被吉星占据"}, {"fact_key": "二宫主（Dhan's Lord）是否与吉星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把四个条件减成任意一两条成立即可。", "不得据此推断开销的金额、频次或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落十一宫（Labh）、金星（Shukra）是否落二宫（Dhan）、十二宫（Vyaya）是否被吉星占据、二宫主（Dhan's Lord）是否与吉星同宫。
- 缺失即停字段：["木星（Guru）是否落十一宫（Labh）", "金星（Shukra）是否落二宫（Dhan）", "十二宫（Vyaya）是否被吉星占据", "二宫主（Dhan's Lord）是否与吉星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v9`｜PDF [28]｜“When Guru is in Labh, Shukra is in Dhan and a benefic is placed in Vyaya Bhava, while Dhan’s Lord is yuti with a benefic, there will be expenses on religious, or charitable grounds.”


## 四路查书计划

### 支持路

- When Guru is in Labh, Shukra is in Dhan and a benefic is placed in Vyaya Bhava, while Dhan’s Lord is yuti with a benefic, there will be expenses on religious, or charitable grounds
- 木星落十一宫 金星落二宫 十二宫吉星 二宫主与吉星同宫 宗教慈善开销

### 反例或取消路

- a malefic in the 12<sup>th</sup> from Karakāńś will cause bad expenses
- And, if Vyaya’s Lord is in Ari, or Randhr Bhava, or be in enemy’s Navāńś, in debilitation Navāńś, or in Randhr Bhava in Navāńś, one will be devoid of happiness from wife, be troubled by expenses
- Should the Lords of Dhan and Labh Bhava be relegated to Ari, Randhr, or Vyaya Bhava

### 适用边界路

- From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava

### 判断方法路

- There will be expenses on good accounts, if Vyaya’s Lord is with a benefic, or in his own Bhava, or exalted, or, if a benefic occupies Vyaya
- If Lagn’s Lord is in Vyaya, while Vyaya’s Lord is in Lagn with Shukr, expenses will be on religious grounds
- 判断开销去向要看十二宫和二宫主

## 上游问题

- 无

## 停止条件

- 四个条件事实缺任一时停止。
- 吉星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
