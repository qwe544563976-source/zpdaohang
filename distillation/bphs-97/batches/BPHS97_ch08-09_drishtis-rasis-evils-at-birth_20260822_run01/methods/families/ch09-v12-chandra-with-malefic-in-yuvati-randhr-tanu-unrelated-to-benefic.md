---
method: ch09-v12-chandra-with-malefic-in-yuvati-randhr-tanu-unrelated-to-benefic
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮与凶星同落七宫、八宫或一宫且与吉星无关联：致早终

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮与凶星同宫落七宫八宫一宫怎么断
- 月亮致早终的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否与凶星同宫
- 月亮（Chandra）是否与吉星有关联（related to a benefic）

## 按情况检查的事实

- 月亮（Chandra）是否落七宫（Yuvati Bhava）
- 月亮（Chandra）是否落八宫（Randhr Bhava）
- 月亮（Chandra）是否落一宫（Tanu Bhava）

## 依赖方法

- 无

## 执行步骤

### ch09-v12-chandra-with-malefic-in-yuvati-randhr-tanu-unrelated-to-benefic.step-001

- 动作：核对月亮是否与凶星同落七、八、一宫，并核对月亮与吉星有无关联。
- 适用范围：仅限本命盘出生时的凶象；原文只写 unrelated to a benefic，没有界定『关联』的具体形式。
- 原文最小意思：月亮（Chandra）与凶星同处七宫（Yuvati）、八宫（Randhr）或一宫（Tanu Bhava），且与吉星无关联时，能致提早终结。
- 本步骤产出事实：["月亮与凶星同宫的早终判定"]
- 所需事实：["月亮（Chandra）是否与凶星同宫", "月亮（Chandra）是否与吉星有关联（related to a benefic）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否与吉星有关联（related to a benefic）"}]}]}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否落七宫（Yuvati Bhava）"}, {"fact_key": "月亮（Chandra）是否落八宫（Randhr Bhava）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu Bhava）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否与吉星有关联（related to a benefic）"}]}]}, "required_fact_keys": ["月亮（Chandra）是否落七宫（Yuvati Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落七宫（Yuvati Bhava）"}, "selection_group": "ch09-v12-chandra-with-malefic-in-yuvati-randhr-tanu-unrelated-to-benefic.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落七宫（Yuvati Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否与吉星有关联（related to a benefic）"}]}]}, "required_fact_keys": ["月亮（Chandra）是否落八宫（Randhr Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落八宫（Randhr Bhava）"}, "selection_group": "ch09-v12-chandra-with-malefic-in-yuvati-randhr-tanu-unrelated-to-benefic.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落八宫（Randhr Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否与吉星有关联（related to a benefic）"}]}]}, "required_fact_keys": ["月亮（Chandra）是否落一宫（Tanu Bhava）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落一宫（Tanu Bhava）"}, "selection_group": "ch09-v12-chandra-with-malefic-in-yuvati-randhr-tanu-unrelated-to-benefic.step-001:chandra-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落一宫（Tanu Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文定义『与吉星有关联』的具体形式（同宫、相照或其他）——原文没有写。", "不得把『提早终结』补成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否与凶星同宫、月亮（Chandra）是否与吉星有关联（related to a benefic）。
- 缺失即停字段：["月亮（Chandra）是否与凶星同宫", "月亮（Chandra）是否与吉星有关联（related to a benefic）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v12`｜PDF [22, 23]｜“Chandra is capable of causing early end, if she is with a malefic in Yuvati, Randhr, or Tanu Bhava and unrelated to a benefic.”


## 四路查书计划

### 支持路

- Chandra is capable of causing early end, if she is with a malefic in Yuvati, Randhr, or Tanu Bhava and unrelated to a benefic
- 月亮 与凶星同宫 七宫八宫一宫 早终

### 反例或取消路

- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Short-life Combinations (up to Sloka 23)
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 吉星凶星怎么定

## 上游问题

- 无

## 停止条件

- 缺少月亮所落宫位与同宫行星事实时停止。
- 『与吉星有关联』的判准原文未给，该事实取不到值时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
