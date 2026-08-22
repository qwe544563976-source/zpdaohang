---
method: ch29-v13-15-benefic-drishti-ascending-gains
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升 Pad 起第 11 宫受来自上升等处的吉星相照：得益递增

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 吉星从哪里照过来更旺财
- 我的进项能不能层层加码

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联

## 按情况检查的事实

- 上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）的吉星相照
- 上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）起第 9 宫的吉星相照

## 依赖方法

- 无

## 执行步骤

### ch29-v13-15-benefic-drishti-ascending-gains.step-001

- 动作：先确认上升 Pad（Lagn Pad）起第 12 宫不与凶星关联，再看其起第 11 宫受到的吉星相照来自哪一处。
- 适用范围：原文以「the 9<sup>th</sup> etc.」泛指其余起照位置而未逐一列举，未列举者不在本条内；原文的「the said 11<sup>th</sup>」承同偈前句的上升 Pad 起第 11 宫。
- 原文最小意思：上升 Pad（Lagn Pad）起第 12 宫同时不与凶星关联的前提下，上升 Pad（Lagn Pad）起第 11 宫受来自上升（Lagna）、第 9 宫等处的吉星相照时，得益按递增次序增加。
- 本步骤产出事实：["上升 Pad 起第 11 宫受吉星相照的递增得益判定"]
- 所需事实：["上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"}]}, {"operator": "OR", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）的吉星相照"}, {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）起第 9 宫的吉星相照"}]}]}
- 按分支必查事实：[{"when": {"operator": "NOT", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"}]}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）的吉星相照"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）的吉星相照"}, "selection_group": "ch29-v13-15-benefic-drishti-ascending-gains.step-001:drishti-source", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）的吉星相照。"}, {"when": {"operator": "NOT", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"}]}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）起第 9 宫的吉星相照"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）起第 9 宫的吉星相照"}, "selection_group": "ch29-v13-15-benefic-drishti-ascending-gains.step-001:drishti-source", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）起第 9 宫的吉星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文以 etc. 未列举的其余起照位置不得自行补入。", "不得据此排出具体的得益名次或数额。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联。
- 缺失即停字段：["上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v13-15`｜PDF [62]｜“O Brahmin, the quantum of gains will correspond to the number of Grahas in, or giving a Drishti to the 11<sup>th</sup> from Lagn Pad.”
  - `bphs-97:santhanam:ch29:v13-15`｜PDF [62]｜“If the said 11<sup>th</sup> receives a Drishti from a benefic from Lagna, the 9<sup>th</sup> etc., gains will increase in the ascending order.”
  - `bphs-97:santhanam:ch29:v13-15`｜PDF [62]｜“In all these cases, the 12<sup>th</sup> from Pad should simultaneously be free from malefic association.”


## 四路查书计划

### 支持路

- If the said 11<sup>th</sup> receives a Drishti from a benefic from Lagna, the 9<sup>th</sup> etc., gains will increase in the ascending order
- 上升 Pad 起第 11 宫受上升与第 9 宫吉星照 得益递增

### 反例或取消路

- If the 12<sup>th</sup> from Lagn Pad receives a Drishti from, or is yuti with both benefics and malefics, there will be abundant earnings, but plenty of expenses.
- 第 12 宫方向的开销条

### 适用边界路

- In all these cases, the 12<sup>th</sup> from Pad should simultaneously be free from malefic association.
- 本段各条共有的第 12 宫前提

### 判断方法路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics.
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 吉星相照怎么判

## 上游问题

- 无

## 停止条件

- 缺少上升 Pad 起第 11 宫受吉星相照的起照位置事实时停止。
- 原文以 etc. 泛指的其余起照位置未确定，落在这些位置时停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
