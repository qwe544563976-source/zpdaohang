---
method: ch19-v3-shani-karm-lord-longevity-check
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 寿命考察点：土星与十宫主，十宫主落八宫并与凶星或上升主同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 看寿命还要看哪些星
- 十宫主落八宫要不要纳入寿命判断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否落八宫（Randhr）

## 按情况检查的事实

- 十宫主（Karm's Lord）是否与凶星同宫
- 十宫主（Karm's Lord）是否与上升主（Lagn's Lord）同宫

## 依赖方法

- 无

## 执行步骤

### ch19-v3-shani-karm-lord-longevity-check.step-001

- 动作：在寿命题目下另行核对土星（Shani）与十宫主（Karm's Lord）：先看十宫主是否落八宫，再看它与凶星或上升主是否同宫。
- 适用范围：仅限本命盘寿命主题；「Similarly」承接上一偈（ch19 v2）的短寿判语所在的考察框架。原文本句只给出要考察的对象与配置，没有写出寿长寿短的结论，本方法据此不给吉凶断语。原文也没有写明土星要落在哪里，故本方法不为土星接入任何落宫事实。
- 原文最小意思：在寿命的问题上同样要考察土星与十宫主：十宫主落八宫，并与凶星同宫或与上升主同宫。
- 本步骤产出事实：["十宫主落八宫的寿命考察点判定"]
- 所需事实：["十宫主（Karm's Lord）是否落八宫（Randhr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落八宫（Randhr）"}, {"operator": "OR", "operands": [{"fact_key": "十宫主（Karm's Lord）是否与凶星同宫"}, {"fact_key": "十宫主（Karm's Lord）是否与上升主（Lagn's Lord）同宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "十宫主（Karm's Lord）是否落八宫（Randhr）"}, "required_fact_keys": ["十宫主（Karm's Lord）是否与凶星同宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否与凶星同宫"}, "selection_group": "ch19-v3-shani-karm-lord-longevity-check.step-001:karm-lord-companion", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否与凶星同宫。"}, {"when": {"fact_key": "十宫主（Karm's Lord）是否落八宫（Randhr）"}, "required_fact_keys": ["十宫主（Karm's Lord）是否与上升主（Lagn's Lord）同宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否与上升主（Lagn's Lord）同宫"}, "selection_group": "ch19-v3-shani-karm-lord-longevity-check.step-001:karm-lord-companion", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否与上升主（Lagn's Lord）同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据「Similarly」把上一偈的短寿结论当成本句已给的结论。", "不得替原文补出土星（Shani）的落宫、强弱或与他星的关系条件。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否落八宫（Randhr）。
- 缺失即停字段：["十宫主（Karm's Lord）是否落八宫（Randhr）"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v3`｜PDF [36]｜“Similarly consider Shani and Karm’s Lord in the matter of longevity. Karm’s Lord is in Randhr along with a malefic Grah and/or Lagn’s Lord.”


## 四路查书计划

### 支持路

- Similarly consider Shani and Karm’s Lord in the matter of longevity Karm’s Lord is in Randhr along with a malefic Grah and/or Lagn’s Lord
- 十宫主落八宫 与凶星同宫 上升主 寿命

### 反例或取消路

- If Randhr’s Lord is in an angle, long life is indicated
- Should the Lords of Lagna, Randhr and Karm Bhava and Shani are all disposed severally in an angle, in a trine, or in Labh Bhava, the subject will live long

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead

### 判断方法路

- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- Should Randhr’s Lord join Lagn’s Lord, or a malefic and be in Randhr itself, the native will be short lived
- 寿命判断中土星与十宫主怎么看

## 上游问题

- 无

## 停止条件

- 缺少十宫主是否落八宫的事实时停止。
- 与凶星同宫、与上升主同宫两个分支事实都缺时停止。
- 原文本句未给寿长寿短的结论，只可作为寿命考察点，不得据本方法输出吉凶。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
