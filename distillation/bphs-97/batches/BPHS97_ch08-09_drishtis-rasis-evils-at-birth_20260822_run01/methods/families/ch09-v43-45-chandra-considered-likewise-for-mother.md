---
method: ch09-v43-45-chandra-considered-likewise-for-mother
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮为母亲的指示星：月亮就母亲一事照太阳的同一办法考量

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 母亲用哪颗星看
- 月亮被凶星照会给母亲带来什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘月亮（Chandra）落在哪一宫

## 按情况检查的事实

- 月亮（Chandra）是否受凶星相照
- 月亮（Chandra）是否被凶星夹（hemmed between malefics）

## 依赖方法

- 无

## 执行步骤

### ch09-v43-45-chandra-considered-likewise-for-mother.step-001

- 动作：以月亮为母亲的指示星，照太阳一条的同一办法核对月亮是否受凶星相照或被凶星夹。
- 适用范围：仅限本命盘对母亲的判断；原文以『同样地』把太阳一条的办法移到月亮与母亲，未另给结果措辞。
- 原文最小意思：母亲由月亮（Chandra）所指示；太阳（Surya）受一颗或多颗凶星相照、或被凶星夹主父亲有凶事，月亮就母亲一事照此同样考量。
- 本步骤产出事实：["月亮受克的母亲判定"]
- 所需事实：["本盘月亮（Chandra）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘月亮（Chandra）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否受凶星相照"}, {"fact_key": "月亮（Chandra）是否被凶星夹（hemmed between malefics）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘月亮（Chandra）落在哪一宫"}, "required_fact_keys": ["月亮（Chandra）是否受凶星相照"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否受凶星相照"}, "selection_group": "ch09-v43-45-chandra-considered-likewise-for-mother.step-001:chandra-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否受凶星相照。"}, {"when": {"fact_key": "本盘月亮（Chandra）落在哪一宫"}, "required_fact_keys": ["月亮（Chandra）是否被凶星夹（hemmed between malefics）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否被凶星夹（hemmed between malefics）"}, "selection_group": "ch09-v43-45-chandra-considered-likewise-for-mother.step-001:chandra-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否被凶星夹（hemmed between malefics）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『同样考量』展开成原文没有为母亲另写的结果措辞。", "不得把母亲的指示星换成月亮以外的行星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘月亮（Chandra）落在哪一宫。
- 缺失即停字段：["本盘月亮（Chandra）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v43-45`｜PDF [24, 25]｜“Surya is the indicator of father for all beings, while the mother is indicated by Chandra. Should Surya receive a Drishti from one, or more malefics, or be hemmed between them, this will cause evils to father. Similarly Chandra be considered in respect of mother.”


## 四路查书计划

### 支持路

- Similarly Chandra be considered in respect of mother
- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- 月亮 母亲指示星 受凶照 被夹

### 反例或取消路

- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Evils to Mother (up to Sloka 33)
- Parents

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 母亲用哪颗星看

## 上游问题

- 无

## 停止条件

- 缺少月亮所受相照与被夹事实时停止。
- 原文只说照太阳一条同样考量，未为母亲另写结果措辞；需要明确结果时本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
