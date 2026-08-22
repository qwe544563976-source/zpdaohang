---
method: ch09-v3-6-retrograde-benefic-in-dusthana-death-within-a-month
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 吉星逆行落六、八、十二宫受凶星相照：出生一个月内死亡（限上升未被吉星占据）

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 吉星逆行落凶宫有什么后果
- 出生一个月内的凶象怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升（Lagn）是否被吉星占据

## 按情况检查的事实

- 是否有逆行的吉星落六宫（Ari Bhava）
- 是否有逆行的吉星落八宫（Randhr Bhava）
- 是否有逆行的吉星落十二宫（Vyaya Bhava）
- 落六宫（Ari Bhava）的逆行吉星是否受凶星相照
- 落八宫（Randhr Bhava）的逆行吉星是否受凶星相照
- 落十二宫（Vyaya Bhava）的逆行吉星是否受凶星相照

## 依赖方法

- 无

## 执行步骤

### ch09-v3-6-retrograde-benefic-in-dusthana-death-within-a-month.step-001

- 动作：核对是否有逆行吉星落六、八、十二宫并受凶星相照，同时核对上升有无吉星占据。
- 适用范围：仅限本命盘出生时的凶象；原文明写这一条只在上升未被吉星占据时成立。
- 原文最小意思：吉星逆行落六宫（Ari）、八宫（Randhr）或十二宫（Vyaya）并受凶星相照时，出生后一个月内死亡；这只在上升（Lagn）未被吉星占据时成立。
- 本步骤产出事实：["逆行吉星落凶宫的一个月内死亡判定"]
- 所需事实：["上升（Lagn）是否被吉星占据"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "上升（Lagn）是否被吉星占据"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "是否有逆行的吉星落六宫（Ari Bhava）"}, {"fact_key": "落六宫（Ari Bhava）的逆行吉星是否受凶星相照"}]}, {"operator": "AND", "operands": [{"fact_key": "是否有逆行的吉星落八宫（Randhr Bhava）"}, {"fact_key": "落八宫（Randhr Bhava）的逆行吉星是否受凶星相照"}]}, {"operator": "AND", "operands": [{"fact_key": "是否有逆行的吉星落十二宫（Vyaya Bhava）"}, {"fact_key": "落十二宫（Vyaya Bhava）的逆行吉星是否受凶星相照"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "NOT", "operands": [{"fact_key": "上升（Lagn）是否被吉星占据"}]}, "required_fact_keys": ["是否有逆行的吉星落六宫（Ari Bhava）", "落六宫（Ari Bhava）的逆行吉星是否受凶星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "是否有逆行的吉星落六宫（Ari Bhava）"}, {"fact_key": "落六宫（Ari Bhava）的逆行吉星是否受凶星相照"}]}, "selection_group": "ch09-v3-6-retrograde-benefic-in-dusthana-death-within-a-month.step-001:retrograde-benefic-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有逆行的吉星落六宫（Ari Bhava）、落六宫（Ari Bhava）的逆行吉星是否受凶星相照。"}, {"when": {"operator": "NOT", "operands": [{"fact_key": "上升（Lagn）是否被吉星占据"}]}, "required_fact_keys": ["是否有逆行的吉星落八宫（Randhr Bhava）", "落八宫（Randhr Bhava）的逆行吉星是否受凶星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "是否有逆行的吉星落八宫（Randhr Bhava）"}, {"fact_key": "落八宫（Randhr Bhava）的逆行吉星是否受凶星相照"}]}, "selection_group": "ch09-v3-6-retrograde-benefic-in-dusthana-death-within-a-month.step-001:retrograde-benefic-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有逆行的吉星落八宫（Randhr Bhava）、落八宫（Randhr Bhava）的逆行吉星是否受凶星相照。"}, {"when": {"operator": "NOT", "operands": [{"fact_key": "上升（Lagn）是否被吉星占据"}]}, "required_fact_keys": ["是否有逆行的吉星落十二宫（Vyaya Bhava）", "落十二宫（Vyaya Bhava）的逆行吉星是否受凶星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "是否有逆行的吉星落十二宫（Vyaya Bhava）"}, {"fact_key": "落十二宫（Vyaya Bhava）的逆行吉星是否受凶星相照"}]}, "selection_group": "ch09-v3-6-retrograde-benefic-in-dusthana-death-within-a-month.step-001:retrograde-benefic-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有逆行的吉星落十二宫（Vyaya Bhava）、落十二宫（Vyaya Bhava）的逆行吉星是否受凶星相照。"}]
- 例外、取消或缓解：[{"type": "limitation", "evidence_atom_ids": ["bphs-97:santhanam:ch09:v3-6"], "condition_logic": {"fact_key": "上升（Lagn）是否被吉星占据"}}]
- 禁止扩大：["不得把上升被吉星占据时的结果补成原文没写的内容——原文只说那时本条不成立。", "不得把『逆行的吉星』换成任意行星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升（Lagn）是否被吉星占据。
- 缺失即停字段：["上升（Lagn）是否被吉星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v3-6`｜PDF [22]｜“If a benefic is retrograde in Ari, Randhr, or Vyaya Bhava, receiving a Drishti from a malefic, death will occur within a month of birth. This is true, only when Lagn is not occupied by a benefic.”


## 四路查书计划

### 支持路

- If a benefic is retrograde in Ari, Randhr, or Vyaya Bhava, receiving a Drishti from a malefic, death will occur within a month of birth
- 逆行吉星 落凶宫 一个月内 死亡

### 反例或取消路

- This is true, only when Lagn is not occupied by a benefic
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- Short-life Combinations (up to Sloka 23)

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 吉星凶星怎么定
- 逆行怎么看

## 上游问题

- 无

## 停止条件

- 缺少上升是否被吉星占据的事实时停止。
- 缺少各宫内逆行吉星与其所受相照的事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
