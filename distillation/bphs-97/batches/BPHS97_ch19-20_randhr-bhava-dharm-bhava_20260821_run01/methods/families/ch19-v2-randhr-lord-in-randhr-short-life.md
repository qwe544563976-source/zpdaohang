---
method: ch19-v2-randhr-lord-in-randhr-short-life
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 短寿：八宫主落八宫并与上升主或凶星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会短寿
- 八宫主落八宫对我的寿命意味着什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫主（Randhr's Lord）是否落八宫（Randhr）

## 按情况检查的事实

- 八宫主（Randhr's Lord）是否与上升主（Lagn's Lord）同宫
- 八宫主（Randhr's Lord）是否与凶星同宫

## 依赖方法

- 无

## 执行步骤

### ch19-v2-randhr-lord-in-randhr-short-life.step-001

- 动作：先核对八宫主（Randhr's Lord）是否落八宫，再核对它与上升主或凶星是否同宫。
- 适用范围：仅限本命盘八宫（Randhr Bhava）寿命主题；原文未给具体寿数或时间限定。
- 原文最小意思：八宫主落八宫，并与上升主同宫或与凶星同宫时，命主短寿。
- 本步骤产出事实：["八宫主落八宫得上升主或凶星的短寿判定"]
- 所需事实：["八宫主（Randhr's Lord）是否落八宫（Randhr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落八宫（Randhr）"}, {"operator": "OR", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否与上升主（Lagn's Lord）同宫"}, {"fact_key": "八宫主（Randhr's Lord）是否与凶星同宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "八宫主（Randhr's Lord）是否落八宫（Randhr）"}, "required_fact_keys": ["八宫主（Randhr's Lord）是否与上升主（Lagn's Lord）同宫"], "branch_condition_logic": {"fact_key": "八宫主（Randhr's Lord）是否与上升主（Lagn's Lord）同宫"}, "selection_group": "ch19-v2-randhr-lord-in-randhr-short-life.step-001:randhr-lord-companion", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）是否与上升主（Lagn's Lord）同宫。"}, {"when": {"fact_key": "八宫主（Randhr's Lord）是否落八宫（Randhr）"}, "required_fact_keys": ["八宫主（Randhr's Lord）是否与凶星同宫"], "branch_condition_logic": {"fact_key": "八宫主（Randhr's Lord）是否与凶星同宫"}, "selection_group": "ch19-v2-randhr-lord-in-randhr-short-life.step-001:randhr-lord-companion", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）是否与凶星同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推出具体寿数年岁或死亡时间。", "不得把原文的「落八宫」条件省去，只凭同宫成立就下断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否落八宫（Randhr）。
- 缺失即停字段：["八宫主（Randhr's Lord）是否落八宫（Randhr）"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v2`｜PDF [35]｜“Should Randhr’s Lord join Lagn’s Lord, or a malefic and be in Randhr itself, the native will be short lived.”


## 四路查书计划

### 支持路

- Should Randhr’s Lord join Lagn’s Lord, or a malefic and be in Randhr itself, the native will be short lived
- 八宫主落八宫 与上升主同宫 与凶星同宫 短寿

### 反例或取消路

- If Randhr’s Lord is in an angle, long life is indicated
- One will be long-lived, if Lagn’s Lord is in exaltation, while Chandra and Guru are, respectively, in Labh and Randhr Bhava
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead

### 判断方法路

- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- Similarly consider Shani and Karm’s Lord in the matter of longevity
- 判断短寿要看八宫主与谁同宫

## 上游问题

- 无

## 停止条件

- 缺少八宫主是否落八宫的事实时停止。
- 与上升主同宫、与凶星同宫两个分支事实都缺时停止。
- 凶星名册未定时停止（吉凶星判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
