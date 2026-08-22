---
method: ch09-v3-6-chandra-in-dusthana-benefic-drishti-lives-up-to-eight
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 同一情形中另有吉星相照：可活到 8

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮落凶宫又有吉星相照能活多久
- 凶象里有吉星相照会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否受凶星相照
- 月亮（Chandra）是否受吉星相照

## 按情况检查的事实

- 月亮（Chandra）是否落六宫（Ari Bhava）
- 月亮（Chandra）是否落八宫（Randhr Bhava）
- 月亮（Chandra）是否落十二宫（Vyaya Bhava）

## 依赖方法

- 无

## 执行步骤

### ch09-v3-6-chandra-in-dusthana-benefic-drishti-lives-up-to-eight.step-001

- 动作：在月亮落六、八、十二宫并受凶星相照的同一情形中，核对是否另有吉星相照。
- 适用范围：仅限上句所述情形；原文只写 up to 8，没有给单位（年、月或其他），不得替它补。
- 原文最小意思：月亮（Chandra）落六宫（Ari）、八宫（Randhr）或十二宫（Vyaya）并受凶星相照，其中若另有吉星相照，它可能活到 8。
- 本步骤产出事实：["月亮落凶宫兼受吉凶相照的存活年限判定"]
- 所需事实：["月亮（Chandra）是否受凶星相照", "月亮（Chandra）是否受吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否受凶星相照"}, {"fact_key": "月亮（Chandra）是否受吉星相照"}]}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否落六宫（Ari Bhava）"}, {"fact_key": "月亮（Chandra）是否落八宫（Randhr Bhava）"}, {"fact_key": "月亮（Chandra）是否落十二宫（Vyaya Bhava）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否受凶星相照"}, {"fact_key": "月亮（Chandra）是否受吉星相照"}]}, "required_fact_keys": ["月亮（Chandra）是否落六宫（Ari Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落六宫（Ari Bhava）"}, "selection_group": "ch09-v3-6-chandra-in-dusthana-benefic-drishti-lives-up-to-eight.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落六宫（Ari Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否受凶星相照"}, {"fact_key": "月亮（Chandra）是否受吉星相照"}]}, "required_fact_keys": ["月亮（Chandra）是否落八宫（Randhr Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落八宫（Randhr Bhava）"}, "selection_group": "ch09-v3-6-chandra-in-dusthana-benefic-drishti-lives-up-to-eight.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落八宫（Randhr Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否受凶星相照"}, {"fact_key": "月亮（Chandra）是否受吉星相照"}]}, "required_fact_keys": ["月亮（Chandra）是否落十二宫（Vyaya Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落十二宫（Vyaya Bhava）"}, "selection_group": "ch09-v3-6-chandra-in-dusthana-benefic-drishti-lives-up-to-eight.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落十二宫（Vyaya Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 8 补成 8 岁、8 年或 8 个月——原文只写 up to 8。", "不得把『可能』写成必然。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否受凶星相照、月亮（Chandra）是否受吉星相照。
- 缺失即停字段：["月亮（Chandra）是否受凶星相照", "月亮（Chandra）是否受吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v3-6`｜PDF [22]｜“Should Chandra be in Ari, Randhr, or Vyaya Bhava and receives a Drishti from a malefic, the child will die soon. If in the process there be a Drishti from a benefic, it may live up to 8.”


## 四路查书计划

### 支持路

- If in the process there be a Drishti from a benefic, it may live up to 8
- 月亮落凶宫 吉星相照 可活到 8

### 反例或取消路

- Should Chandra be in Ari, Randhr, or Vyaya Bhava and receives a Drishti from a malefic, the child will die soon

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Short-life Combinations (up to Sloka 23)
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 吉星相照能减多少凶

## 上游问题

- 无

## 停止条件

- 缺少月亮所落宫位时停止。
- 缺少月亮所受吉星、凶星相照事实时停止。
- 原文只给数字 8 未给单位，需要具体年限时本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
