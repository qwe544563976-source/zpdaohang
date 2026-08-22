---
method: ch09-v3-6-chandra-in-dusthana-malefic-drishti-dies-soon
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮落六、八、十二宫并受凶星相照：孩子很快去世

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮落十二宫又被凶星照有什么后果
- 孩子出生后能不能存活
- 月亮落六宫八宫十二宫怎么断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否受凶星相照

## 按情况检查的事实

- 月亮（Chandra）是否落六宫（Ari Bhava）
- 月亮（Chandra）是否落八宫（Randhr Bhava）
- 月亮（Chandra）是否落十二宫（Vyaya Bhava）
- 月亮（Chandra）是否受吉星相照

## 依赖方法

- 无

## 执行步骤

### ch09-v3-6-chandra-in-dusthana-malefic-drishti-dies-soon.step-001

- 动作：核对月亮所落宫位与所受相照，判断幼年存活。
- 适用范围：仅限本命盘出生时的凶象；原文这一句以孩子为断语对象。
- 原文最小意思：月亮（Chandra）落六宫（Ari）、八宫（Randhr）或十二宫（Vyaya）并受凶星相照时，孩子会很快去世。
- 本步骤产出事实：["月亮落凶宫受凶照的早殇判定"]
- 所需事实：["月亮（Chandra）是否受凶星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否受凶星相照"}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否落六宫（Ari Bhava）"}, {"fact_key": "月亮（Chandra）是否落八宫（Randhr Bhava）"}, {"fact_key": "月亮（Chandra）是否落十二宫（Vyaya Bhava）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "月亮（Chandra）是否受凶星相照"}, "required_fact_keys": ["月亮（Chandra）是否落六宫（Ari Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落六宫（Ari Bhava）"}, "selection_group": "ch09-v3-6-chandra-in-dusthana-malefic-drishti-dies-soon.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落六宫（Ari Bhava）。"}, {"when": {"fact_key": "月亮（Chandra）是否受凶星相照"}, "required_fact_keys": ["月亮（Chandra）是否落八宫（Randhr Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落八宫（Randhr Bhava）"}, "selection_group": "ch09-v3-6-chandra-in-dusthana-malefic-drishti-dies-soon.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落八宫（Randhr Bhava）。"}, {"when": {"fact_key": "月亮（Chandra）是否受凶星相照"}, "required_fact_keys": ["月亮（Chandra）是否落十二宫（Vyaya Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落十二宫（Vyaya Bhava）"}, "selection_group": "ch09-v3-6-chandra-in-dusthana-malefic-drishti-dies-soon.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落十二宫（Vyaya Bhava）。"}]
- 例外、取消或缓解：[{"type": "mitigation", "evidence_atom_ids": ["bphs-97:santhanam:ch09:v3-6"], "condition_logic": {"fact_key": "月亮（Chandra）是否受吉星相照"}}]
- 禁止扩大：["不得把『很快』补成原文没有的具体天数或年岁。", "不得把断语对象从孩子换成父母或别人。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否受凶星相照。
- 缺失即停字段：["月亮（Chandra）是否受凶星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v3-6`｜PDF [22]｜“Should Chandra be in Ari, Randhr, or Vyaya Bhava and receives a Drishti from a malefic, the child will die soon.”


## 四路查书计划

### 支持路

- Should Chandra be in Ari, Randhr, or Vyaya Bhava and receives a Drishti from a malefic, the child will die soon
- 月亮落六宫八宫十二宫 受凶星相照 早殇

### 反例或取消路

- If in the process there be a Drishti from a benefic, it may live up to 8
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils
- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- Short-life Combinations (up to Sloka 23)

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- O Brahmin, first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas.
- 吉星凶星怎么定

## 上游问题

- 无

## 停止条件

- 缺少月亮所落宫位时停止。
- 缺少月亮所受相照事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
