---
method: ch09-v26-chandra-seventh-or-eighth-from-malefic-mother-early-end
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮在某凶星的第 7 或第 8 位、自身与凶星同宫又受有力凶星相照：母亲早终

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮在凶星第七第八位怎么断
- 母亲会不会早走

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否与凶星同宫
- 月亮（Chandra）是否受有力凶星（strong malefic）相照

## 按情况检查的事实

- 月亮（Chandra）是否落自某凶星起算的第 7 位
- 月亮（Chandra）是否落自某凶星起算的第 8 位

## 依赖方法

- 无

## 执行步骤

### ch09-v26-chandra-seventh-or-eighth-from-malefic-mother-early-end.step-001

- 动作：核对月亮相对凶星的位次、月亮的同宫行星与所受相照。
- 适用范围：仅限本命盘对母亲的凶象；原文说 strong malefic 却未在本偈给出强弱判准（判准见第 27 章 Shad Bal）。
- 原文最小意思：月亮（Chandra）落在自某凶星起算的第 7 位或第 8 位，自身与凶星同宫，又受有力凶星（strong malefic）相照时，可断母亲早终。
- 本步骤产出事实：["月亮受凶的母亲早终判定"]
- 所需事实：["月亮（Chandra）是否与凶星同宫", "月亮（Chandra）是否受有力凶星（strong malefic）相照"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"fact_key": "月亮（Chandra）是否受有力凶星（strong malefic）相照"}]}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否落自某凶星起算的第 7 位"}, {"fact_key": "月亮（Chandra）是否落自某凶星起算的第 8 位"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"fact_key": "月亮（Chandra）是否受有力凶星（strong malefic）相照"}]}, "required_fact_keys": ["月亮（Chandra）是否落自某凶星起算的第 7 位"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落自某凶星起算的第 7 位"}, "selection_group": "ch09-v26-chandra-seventh-or-eighth-from-malefic-mother-early-end.step-001:chandra-position-from-malefic", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落自某凶星起算的第 7 位。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"fact_key": "月亮（Chandra）是否受有力凶星（strong malefic）相照"}]}, "required_fact_keys": ["月亮（Chandra）是否落自某凶星起算的第 8 位"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落自某凶星起算的第 8 位"}, "selection_group": "ch09-v26-chandra-seventh-or-eighth-from-malefic-mother-early-end.step-001:chandra-position-from-malefic", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落自某凶星起算的第 8 位。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『有力的凶星』读成任意凶星——原文加了 strong。", "不得把『早终』补成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否与凶星同宫、月亮（Chandra）是否受有力凶星（strong malefic）相照。
- 缺失即停字段：["月亮（Chandra）是否与凶星同宫", "月亮（Chandra）是否受有力凶星（strong malefic）相照"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v26`｜PDF [23]｜“If Chandra is in the 7<sup>th</sup> , or the 8<sup>th</sup> from a malefic, be herself with a malefic and receives a Drishti from a strong malefic, predict mothers end to be early.”


## 四路查书计划

### 支持路

- If Chandra is in the 7<sup>th</sup> , or the 8<sup>th</sup> from a malefic, be herself with a malefic and receives a Drishti from a strong malefic, predict mothers end to be early
- 月亮 凶星第七第八位 有力凶星相照 母亲

### 反例或取消路

- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evils to Mother (up to Sloka 33)
- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- Evils at Birth
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 行星强弱怎么算

## 上游问题

- 无

## 停止条件

- 『有力的凶星』的强弱判准原文本偈未给，须另查第 27 章 Shad Bal；该事实取不到值时停止。
- 缺少月亮相对凶星的位次事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
