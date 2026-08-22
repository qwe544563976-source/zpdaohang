---
method: ch29-v19-budh-malefic-loss-through-disputes
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 水星落上升 Pad 起第 12 宫且与凶星关联：因争讼而失去财富

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会因为打官司破财
- 争执会不会让我损财

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 水星（Budh）是否落上升 Pad（Lagn Pad）起第 12 宫

## 按情况检查的事实

- 水星（Budh）是否与凶星同宫
- 水星（Budh）是否被凶星相照

## 依赖方法

- 无

## 执行步骤

### ch29-v19-budh-malefic-loss-through-disputes.step-001

- 动作：先看水星（Budh）是否落上升 Pad（Lagn Pad）起第 12 宫，再看与它同宫或相照它的是不是凶星。
- 适用范围：原文的「so related」承同偈前句所说的同宫或相照两种关联方式；凶星判准见第 3 章第 11 偈。
- 原文最小意思：水星（Budh）落上升 Pad（Lagn Pad）起第 12 宫，而与之同宫或相照、与该水星如此关联的是凶星时，因争讼而失去财富。
- 本步骤产出事实：["水星在上升 Pad 起第 12 宫的争讼失财判定"]
- 所需事实：["水星（Budh）是否落上升 Pad（Lagn Pad）起第 12 宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落上升 Pad（Lagn Pad）起第 12 宫"}, {"operator": "OR", "operands": [{"fact_key": "水星（Budh）是否与凶星同宫"}, {"fact_key": "水星（Budh）是否被凶星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "水星（Budh）是否落上升 Pad（Lagn Pad）起第 12 宫"}, "required_fact_keys": ["水星（Budh）是否与凶星同宫"], "branch_condition_logic": {"fact_key": "水星（Budh）是否与凶星同宫"}, "selection_group": "ch29-v19-budh-malefic-loss-through-disputes.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否与凶星同宫。"}, {"when": {"fact_key": "水星（Budh）是否落上升 Pad（Lagn Pad）起第 12 宫"}, "required_fact_keys": ["水星（Budh）是否被凶星相照"], "branch_condition_logic": {"fact_key": "水星（Budh）是否被凶星相照"}, "selection_group": "ch29-v19-budh-malefic-loss-through-disputes.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否被凶星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断诉讼种类、结果或时间。", "不得据此推断损失金额。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：水星（Budh）是否落上升 Pad（Lagn Pad）起第 12 宫。
- 缺失即停字段：["水星（Budh）是否落上升 Pad（Lagn Pad）起第 12 宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v19`｜PDF [62]｜“If Budh is in the 12<sup>th</sup> from Lagn Pad and is yuti with, or receives a Drishti from a benefic, similarly there will be expenses through paternal relatives.”
  - `bphs-97:santhanam:ch29:v19`｜PDF [62]｜“A malefic so related to the said Budh will cause loss of wealth through disputes.”


## 四路查书计划

### 支持路

- A malefic so related to the said Budh will cause loss of wealth through disputes.
- 水星与凶星关联 因争讼失财

### 反例或取消路

- If Budh is in the 12<sup>th</sup> from Lagn Pad and is yuti with, or receives a Drishti from a benefic, similarly there will be expenses through paternal relatives.
- 同一水星与吉星关联时的开销来由

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics.
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 哪些行星算凶星

## 上游问题

- 无

## 停止条件

- 缺少水星相对上升 Pad 起第 12 宫的落宫事实时停止。
- 缺少水星与凶星的同宫或相照事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
