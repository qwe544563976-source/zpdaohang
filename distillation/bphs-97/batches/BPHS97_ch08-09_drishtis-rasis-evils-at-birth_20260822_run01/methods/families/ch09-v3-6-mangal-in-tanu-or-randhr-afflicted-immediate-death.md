---
method: ch09-v3-6-mangal-in-tanu-or-randhr-afflicted-immediate-death
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 火星落一宫或八宫、与土星或太阳同宫或受凶照且无吉照：当即死亡之源

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 火星落一宫八宫有什么凶
- 火星与土星同宫会怎样
- 出生即夭的组合有哪些

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 火星（Mangal）是否受吉星相照

## 按情况检查的事实

- 火星（Mangal）是否落一宫（Tanu Bhava）
- 火星（Mangal）是否落八宫（Randhr Bhava）
- 火星（Mangal）是否与土星（Shani）同宫
- 火星（Mangal）是否与太阳（Surya）同宫
- 火星（Mangal）是否受凶星相照

## 依赖方法

- 无

## 执行步骤

### ch09-v3-6-mangal-in-tanu-or-randhr-afflicted-immediate-death.step-001

- 动作：核对火星所落宫位、与土星或太阳的同宫、所受凶照，以及有无吉星相照。
- 适用范围：仅限本命盘出生时的凶象；原文以『得不到吉星相照』为必要前提。
- 原文最小意思：火星（Mangal）落一宫（Tanu）或八宫（Randhr），与土星（Shani）或太阳（Surya）同宫、或受凶星相照，同时得不到吉星相照时，会成为（当即）死亡之源。
- 本步骤产出事实：["火星落一宫或八宫致死的判定"]
- 所需事实：["火星（Mangal）是否受吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "火星（Mangal）是否受吉星相照"}]}, {"operator": "OR", "operands": [{"fact_key": "火星（Mangal）是否落一宫（Tanu Bhava）"}, {"fact_key": "火星（Mangal）是否落八宫（Randhr Bhava）"}]}, {"operator": "OR", "operands": [{"fact_key": "火星（Mangal）是否与土星（Shani）同宫"}, {"fact_key": "火星（Mangal）是否与太阳（Surya）同宫"}, {"fact_key": "火星（Mangal）是否受凶星相照"}]}]}
- 按分支必查事实：[{"when": {"operator": "NOT", "operands": [{"fact_key": "火星（Mangal）是否受吉星相照"}]}, "required_fact_keys": ["火星（Mangal）是否落一宫（Tanu Bhava）"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否落一宫（Tanu Bhava）"}, "selection_group": "ch09-v3-6-mangal-in-tanu-or-randhr-afflicted-immediate-death.step-001:mangal-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否落一宫（Tanu Bhava）。"}, {"when": {"operator": "NOT", "operands": [{"fact_key": "火星（Mangal）是否受吉星相照"}]}, "required_fact_keys": ["火星（Mangal）是否落八宫（Randhr Bhava）"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否落八宫（Randhr Bhava）"}, "selection_group": "ch09-v3-6-mangal-in-tanu-or-randhr-afflicted-immediate-death.step-001:mangal-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否落八宫（Randhr Bhava）。"}, {"when": {"operator": "NOT", "operands": [{"fact_key": "火星（Mangal）是否受吉星相照"}]}, "required_fact_keys": ["火星（Mangal）是否与土星（Shani）同宫"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否与土星（Shani）同宫"}, "selection_group": "ch09-v3-6-mangal-in-tanu-or-randhr-afflicted-immediate-death.step-001:mangal-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否与土星（Shani）同宫。"}, {"when": {"operator": "NOT", "operands": [{"fact_key": "火星（Mangal）是否受吉星相照"}]}, "required_fact_keys": ["火星（Mangal）是否与太阳（Surya）同宫"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否与太阳（Surya）同宫"}, "selection_group": "ch09-v3-6-mangal-in-tanu-or-randhr-afflicted-immediate-death.step-001:mangal-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否与太阳（Surya）同宫。"}, {"when": {"operator": "NOT", "operands": [{"fact_key": "火星（Mangal）是否受吉星相照"}]}, "required_fact_keys": ["火星（Mangal）是否受凶星相照"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否受凶星相照"}, "selection_group": "ch09-v3-6-mangal-in-tanu-or-randhr-afflicted-immediate-death.step-001:mangal-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否受凶星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『当即』补成原文没有的具体时间。", "不得省略『得不到吉星相照』这一前提。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：火星（Mangal）是否受吉星相照。
- 缺失即停字段：["火星（Mangal）是否受吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v3-6`｜PDF [22]｜“Mangal, placed in Tanu, or in Randhr Bhava and be yuti with Shani, or Surya, or receiving a Drishti from a malefic, being bereft of a Drishti from a benefic, will prove a source of (immediate) death.”


## 四路查书计划

### 支持路

- Mangal, placed in Tanu, or in Randhr Bhava and be yuti with Shani, or Surya, or receiving a Drishti from a malefic, being bereft of a Drishti from a benefic, will prove a source of (immediate) death
- 火星落一宫八宫 与土星太阳同宫 无吉照 死

### 反例或取消路

- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Short-life Combinations (up to Sloka 23)
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- O Brahmin, first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas.
- 火星的凶怎么化

## 上游问题

- 无

## 停止条件

- 缺少火星所落宫位时停止。
- 缺少火星同宫行星与所受相照事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
