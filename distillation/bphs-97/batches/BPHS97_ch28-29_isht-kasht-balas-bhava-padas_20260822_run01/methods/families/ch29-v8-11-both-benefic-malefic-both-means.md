---
method: ch29-v8-11-both-benefic-malefic-both-means
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 吉凶两类同时关联上升 Pad 起第 11 宫：财富经由两种途径

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的进项是不是好坏来路都有
- 钱路混杂怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升 Pad（Lagn Pad）落在哪一宫

## 按情况检查的事实

- 上升 Pad（Lagn Pad）起第 11 宫是否被吉星占据
- 上升 Pad（Lagn Pad）起第 11 宫是否被吉星相照
- 上升 Pad（Lagn Pad）起第 11 宫是否被凶星占据
- 上升 Pad（Lagn Pad）起第 11 宫是否被凶星相照

## 依赖方法

- 无

## 执行步骤

### ch29-v8-11-both-benefic-malefic-both-means.step-001

- 动作：分别核对与上升 Pad（Lagn Pad）起第 11 宫关联的吉星与凶星，两类同时存在时按本条断。
- 适用范围：原文的「as above」指同偈前句所说的占据或相照两种关联方式；吉星凶星的判准见第 3 章第 11 偈。
- 原文最小意思：上升 Pad（Lagn Pad）起第 11 宫被占据，或受相照，而其中既有吉星又有凶星时，财富经由两种途径而来。
- 本步骤产出事实：["上升 Pad 起第 11 宫的吉凶混合得财来路判定"]
- 所需事实：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被吉星占据"}, {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被吉星相照"}]}, {"operator": "OR", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被凶星占据"}, {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被凶星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 11 宫是否被吉星占据"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被吉星占据"}, "selection_group": "ch29-v8-11-both-benefic-malefic-both-means.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 11 宫是否被吉星占据。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 11 宫是否被吉星相照"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被吉星相照"}, "selection_group": "ch29-v8-11-both-benefic-malefic-both-means.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 11 宫是否被吉星相照。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 11 宫是否被凶星占据"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被凶星占据"}, "selection_group": "ch29-v8-11-both-benefic-malefic-both-means.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 11 宫是否被凶星占据。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 11 宫是否被凶星相照"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被凶星相照"}, "selection_group": "ch29-v8-11-both-benefic-malefic-both-means.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 11 宫是否被凶星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断两种途径各占多少比例。", "不得把两种途径改读成两个不同的时间段。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升 Pad（Lagn Pad）落在哪一宫。
- 缺失即停字段：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v8-11`｜PDF [62]｜“If the 11<sup>th</sup> from Lagn Pad is occupied, or receives a Drishti from a Grah the native will be happy and rich”
  - `bphs-97:santhanam:ch29:v8-11`｜PDF [62]｜“If there be both a benefic and a malefic, it will be through both means.”


## 四路查书计划

### 支持路

- If there be both a benefic and a malefic, it will be through both means
- 吉凶同时关联上升 Pad 起第 11 宫

### 反例或取消路

- A malefic will confer wealth through questionable means
- 只有凶星关联时

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics.
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 吉星凶星怎么分

## 上游问题

- 无

## 停止条件

- 缺少本盘上升 Pad（Lagn Pad）落宫事实时停止。
- 缺少吉星或凶星与上升 Pad 起第 11 宫的关联事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
