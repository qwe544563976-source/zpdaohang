---
method: ch09-v19-chandra-in-tanu-randhr-vyaya-yuvati-hemmed-between-malefics
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮落一、八、十二或七宫并被凶星夹：早亡

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮被凶星夹怎么断
- 月亮落一宫八宫十二宫七宫有什么凶

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否被凶星夹（hemmed between malefics）

## 按情况检查的事实

- 月亮（Chandra）是否落一宫（Tanu Bhava）
- 月亮（Chandra）是否落八宫（Randhr Bhava）
- 月亮（Chandra）是否落十二宫（Vyaya Bhava）
- 月亮（Chandra）是否落七宫（Yuvati Bhava）

## 依赖方法

- 无

## 执行步骤

### ch09-v19-chandra-in-tanu-randhr-vyaya-yuvati-hemmed-between-malefics.step-001

- 动作：核对月亮所落宫位，并核对月亮是否被凶星夹。
- 适用范围：仅限本命盘出生时的凶象；原文列出四个落宫，任一成立即可。
- 原文最小意思：月亮（Chandra）落一宫（Tanu）、八宫（Randhr）、十二宫（Vyaya）或七宫（Yuvati Bhava）并被凶星夹时，会致早亡。
- 本步骤产出事实：["月亮被凶星夹的早亡判定"]
- 所需事实：["月亮（Chandra）是否被凶星夹（hemmed between malefics）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否被凶星夹（hemmed between malefics）"}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否落一宫（Tanu Bhava）"}, {"fact_key": "月亮（Chandra）是否落八宫（Randhr Bhava）"}, {"fact_key": "月亮（Chandra）是否落十二宫（Vyaya Bhava）"}, {"fact_key": "月亮（Chandra）是否落七宫（Yuvati Bhava）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "月亮（Chandra）是否被凶星夹（hemmed between malefics）"}, "required_fact_keys": ["月亮（Chandra）是否落一宫（Tanu Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落一宫（Tanu Bhava）"}, "selection_group": "ch09-v19-chandra-in-tanu-randhr-vyaya-yuvati-hemmed-between-malefics.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落一宫（Tanu Bhava）。"}, {"when": {"fact_key": "月亮（Chandra）是否被凶星夹（hemmed between malefics）"}, "required_fact_keys": ["月亮（Chandra）是否落八宫（Randhr Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落八宫（Randhr Bhava）"}, "selection_group": "ch09-v19-chandra-in-tanu-randhr-vyaya-yuvati-hemmed-between-malefics.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落八宫（Randhr Bhava）。"}, {"when": {"fact_key": "月亮（Chandra）是否被凶星夹（hemmed between malefics）"}, "required_fact_keys": ["月亮（Chandra）是否落十二宫（Vyaya Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落十二宫（Vyaya Bhava）"}, "selection_group": "ch09-v19-chandra-in-tanu-randhr-vyaya-yuvati-hemmed-between-malefics.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落十二宫（Vyaya Bhava）。"}, {"when": {"fact_key": "月亮（Chandra）是否被凶星夹（hemmed between malefics）"}, "required_fact_keys": ["月亮（Chandra）是否落七宫（Yuvati Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落七宫（Yuvati Bhava）"}, "selection_group": "ch09-v19-chandra-in-tanu-randhr-vyaya-yuvati-hemmed-between-malefics.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落七宫（Yuvati Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把落宫扩大到原文所列四宫以外。", "不得把『早亡』补成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否被凶星夹（hemmed between malefics）。
- 缺失即停字段：["月亮（Chandra）是否被凶星夹（hemmed between malefics）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v19`｜PDF [23]｜“Chandra in Tanu, Randhr, Vyaya, or Yuvati Bhava and hemmed between malefics will confer premature death.”


## 四路查书计划

### 支持路

- Chandra in Tanu, Randhr, Vyaya, or Yuvati Bhava and hemmed between malefics will confer premature death
- 月亮 被凶星夹 一宫八宫十二宫七宫 早亡

### 反例或取消路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- Short-life Combinations (up to Sloka 23)

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- 被凶星夹怎么算

## 上游问题

- 无

## 停止条件

- 缺少月亮所落宫位时停止。
- 缺少月亮是否被凶星夹的事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
