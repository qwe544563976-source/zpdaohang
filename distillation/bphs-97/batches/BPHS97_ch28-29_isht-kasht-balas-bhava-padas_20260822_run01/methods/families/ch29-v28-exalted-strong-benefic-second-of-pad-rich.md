---
method: ch29-v28-exalted-strong-benefic-second-of-pad-rich
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 水星、木星或金星在上升 Pad 起第 2 宫入旺且有力：命主富有

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有钱
- 第 2 宫的入旺星有什么用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升 Pad（Lagn Pad）落在哪一宫

## 按情况检查的事实

- 水星（Budh）是否落上升 Pad（Lagn Pad）起第 2 宫
- 水星（Budh）是否入旺
- 水星（Budh）是否有力
- 木星（Guru）是否落上升 Pad（Lagn Pad）起第 2 宫
- 木星（Guru）是否入旺
- 木星（Guru）是否有力
- 金星（Shukra）是否落上升 Pad（Lagn Pad）起第 2 宫
- 金星（Shukra）是否入旺
- 金星（Shukra）是否有力

## 依赖方法

- 无

## 执行步骤

### ch29-v28-exalted-strong-benefic-second-of-pad-rich.step-001

- 动作：逐颗核对水星（Budh）、木星（Guru）、金星（Shukra）是否在上升 Pad（Lagn Pad）起第 2 宫入旺，并同时有力。
- 适用范围：原文要求同时入旺与有力两件事；力量判准原文未在本偈给出，见第 27 章六力（Shad Bal）诸目。
- 原文最小意思：水星（Budh）、木星（Guru）、金星（Shukra）之中任何一颗在上升 Pad（Lagn Pad）起第 2 宫入旺、并且有力时，命主富有。
- 本步骤产出事实：["上升 Pad 起第 2 宫入旺有力行星的富有判定"]
- 所需事实：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落上升 Pad（Lagn Pad）起第 2 宫"}, {"fact_key": "水星（Budh）是否入旺"}, {"fact_key": "水星（Budh）是否有力"}]}, {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落上升 Pad（Lagn Pad）起第 2 宫"}, {"fact_key": "木星（Guru）是否入旺"}, {"fact_key": "木星（Guru）是否有力"}]}, {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落上升 Pad（Lagn Pad）起第 2 宫"}, {"fact_key": "金星（Shukra）是否入旺"}, {"fact_key": "金星（Shukra）是否有力"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["水星（Budh）是否落上升 Pad（Lagn Pad）起第 2 宫", "水星（Budh）是否入旺", "水星（Budh）是否有力"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落上升 Pad（Lagn Pad）起第 2 宫"}, {"fact_key": "水星（Budh）是否入旺"}, {"fact_key": "水星（Budh）是否有力"}]}, "selection_group": "ch29-v28-exalted-strong-benefic-second-of-pad-rich.step-001:planet", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落上升 Pad（Lagn Pad）起第 2 宫、水星（Budh）是否入旺、水星（Budh）是否有力。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["木星（Guru）是否落上升 Pad（Lagn Pad）起第 2 宫", "木星（Guru）是否入旺", "木星（Guru）是否有力"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落上升 Pad（Lagn Pad）起第 2 宫"}, {"fact_key": "木星（Guru）是否入旺"}, {"fact_key": "木星（Guru）是否有力"}]}, "selection_group": "ch29-v28-exalted-strong-benefic-second-of-pad-rich.step-001:planet", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落上升 Pad（Lagn Pad）起第 2 宫、木星（Guru）是否入旺、木星（Guru）是否有力。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["金星（Shukra）是否落上升 Pad（Lagn Pad）起第 2 宫", "金星（Shukra）是否入旺", "金星（Shukra）是否有力"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落上升 Pad（Lagn Pad）起第 2 宫"}, {"fact_key": "金星（Shukra）是否入旺"}, {"fact_key": "金星（Shukra）是否有力"}]}, "selection_group": "ch29-v28-exalted-strong-benefic-second-of-pad-rich.step-001:planet", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落上升 Pad（Lagn Pad）起第 2 宫、金星（Shukra）是否入旺、金星（Shukra）是否有力。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得只凭入旺而不核对有力就成立本条。", "不得据此推断财富数额或来源。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升 Pad（Lagn Pad）落在哪一宫。
- 缺失即停字段：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v28`｜PDF [63]｜“Anyone of Budh, Guru and Shukra being exalted in the 2<sup>nd</sup> from Lagn Pad and being with strength will make the subject rich.”


## 四路查书计划

### 支持路

- Anyone of Budh, Guru and Shukra being exalted in the 2<sup>nd</sup> from Lagn Pad and being with strength will make the subject rich.
- 水星木星金星在上升 Pad 起第 2 宫入旺有力 富有

### 反例或取消路

- If the Dar Pad falls in the 6<sup>th</sup> / 8<sup>th</sup> /12<sup>th</sup> from Lagn Pad, then the native will be poor.
- Dar Pad 落 6、8、12 宫时的贫穷条

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- O Brahmin, these Yogas, as narrated by me with reference to the 7<sup>th</sup> from Lagn Pad, should also be considered from the 2<sup>nd</sup> of Lagn Pad.
- 第 2 宫这一路断语的来历

### 判断方法路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 有力怎么判

## 上游问题

- 无

## 停止条件

- 缺少这三颗行星相对上升 Pad 起第 2 宫的落宫或入旺事实时停止。
- 缺少该行星是否有力的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
