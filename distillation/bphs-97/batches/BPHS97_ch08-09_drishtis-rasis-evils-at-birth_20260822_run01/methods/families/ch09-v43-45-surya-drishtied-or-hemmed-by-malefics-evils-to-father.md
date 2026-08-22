---
method: ch09-v43-45-surya-drishtied-or-hemmed-by-malefics-evils-to-father
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 太阳为父亲的指示星：太阳受凶星相照或被凶星夹，主父亲有凶事

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 父亲用哪颗星看
- 太阳被凶星照会给父亲带来什么
- 父亲的凶象怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘太阳（Surya）落在哪一宫

## 按情况检查的事实

- 太阳（Surya）是否受凶星相照
- 太阳（Surya）是否被凶星夹（hemmed between malefics）

## 依赖方法

- 无

## 执行步骤

### ch09-v43-45-surya-drishtied-or-hemmed-by-malefics-evils-to-father.step-001

- 动作：以太阳为父亲的指示星，核对太阳是否受凶星相照或被凶星夹。
- 适用范围：仅限本命盘对父亲的判断；原文先立太阳为众生之父的指示星，再给这一条。
- 原文最小意思：太阳（Surya）是众生之父的指示星，母亲则由月亮（Chandra）所指示；太阳受一颗或多颗凶星相照、或被凶星夹时，会给父亲带来凶事。
- 本步骤产出事实：["太阳受克的父亲凶象判定"]
- 所需事实：["本盘太阳（Surya）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "太阳（Surya）是否受凶星相照"}, {"fact_key": "太阳（Surya）是否被凶星夹（hemmed between malefics）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘太阳（Surya）落在哪一宫"}, "required_fact_keys": ["太阳（Surya）是否受凶星相照"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否受凶星相照"}, "selection_group": "ch09-v43-45-surya-drishtied-or-hemmed-by-malefics-evils-to-father.step-001:surya-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否受凶星相照。"}, {"when": {"fact_key": "本盘太阳（Surya）落在哪一宫"}, "required_fact_keys": ["太阳（Surya）是否被凶星夹（hemmed between malefics）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否被凶星夹（hemmed between malefics）"}, "selection_group": "ch09-v43-45-surya-drishtied-or-hemmed-by-malefics-evils-to-father.step-001:surya-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否被凶星夹（hemmed between malefics）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『凶事』补成去世等原文没写的具体结果。", "不得把父亲的指示星换成太阳以外的行星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘太阳（Surya）落在哪一宫。
- 缺失即停字段：["本盘太阳（Surya）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v43-45`｜PDF [24, 25]｜“Surya is the indicator of father for all beings, while the mother is indicated by Chandra. Should Surya receive a Drishti from one, or more malefics, or be hemmed between them, this will cause evils to father.”


## 四路查书计划

### 支持路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- Should Surya receive a Drishti from one, or more malefics, or be hemmed between them, this will cause evils to father
- 太阳 父亲指示星 受凶照 被夹

### 反例或取消路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Evil to Father (up to Sloka 42)
- Parents

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 父亲用哪颗星看

## 上游问题

- 无

## 停止条件

- 缺少太阳所受相照与被夹事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
