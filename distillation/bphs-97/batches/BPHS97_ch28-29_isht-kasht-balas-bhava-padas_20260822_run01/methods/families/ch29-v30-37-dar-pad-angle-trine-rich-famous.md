---
method: ch29-v30-37-dar-pad-angle-trine-rich-famous
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Dar Pad 落上升 Pad 的角宫三角宫或两 Pad 都有有力行星：富有且在本国有名

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会又有钱又有名
- 夫妻位和命位的关系怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升 Pad（Lagn Pad）落在哪一宫
- 本盘 Dar Pad（Kalatr Pad）落在哪一宫

## 按情况检查的事实

- Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起算的角宫（Kendra）
- Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起算的三角宫（Kona）
- 上升 Pad（Lagn Pad）是否被有力的行星（strong Grah）占据
- Dar Pad（Kalatr Pad）是否被有力的行星（strong Grah）占据

## 依赖方法

- 无

## 执行步骤

### ch29-v30-37-dar-pad-angle-trine-rich-famous.step-001

- 动作：先定出上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）各落哪一宫，再看 Dar Pad 是否落在从上升 Pad 起算的角宫或三角宫，或两个 Pad 内是否都有有力的行星。
- 适用范围：力量判准原文未在本偈给出，见第 27 章六力（Shad Bal）诸目；原文以 in his country 的口吻立说。
- 原文最小意思：Dar Pad（Kalatr Pad）从上升 Pad（Lagn Pad）起算落在角宫、或落在三角宫，或上升 Pad 与 Dar Pad 内都有有力的行星时，命主富有并在本国有名。
- 本步骤产出事实：["上升 Pad 与 Dar Pad 相对位置的富名判定"]
- 所需事实：["本盘上升 Pad（Lagn Pad）落在哪一宫", "本盘 Dar Pad（Kalatr Pad）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}]}, {"operator": "OR", "operands": [{"fact_key": "Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起算的角宫（Kendra）"}, {"fact_key": "Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起算的三角宫（Kona）"}, {"operator": "AND", "operands": [{"fact_key": "上升 Pad（Lagn Pad）是否被有力的行星（strong Grah）占据"}, {"fact_key": "Dar Pad（Kalatr Pad）是否被有力的行星（strong Grah）占据"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}]}, "required_fact_keys": ["Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起算的角宫（Kendra）"], "branch_condition_logic": {"fact_key": "Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起算的角宫（Kendra）"}, "selection_group": "ch29-v30-37-dar-pad-angle-trine-rich-famous.step-001:configuration", "stop_condition": "选中该分支后，缺少以下事实即停止：Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起算的角宫（Kendra）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}]}, "required_fact_keys": ["Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起算的三角宫（Kona）"], "branch_condition_logic": {"fact_key": "Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起算的三角宫（Kona）"}, "selection_group": "ch29-v30-37-dar-pad-angle-trine-rich-famous.step-001:configuration", "stop_condition": "选中该分支后，缺少以下事实即停止：Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起算的三角宫（Kona）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}]}, "required_fact_keys": ["上升 Pad（Lagn Pad）是否被有力的行星（strong Grah）占据", "Dar Pad（Kalatr Pad）是否被有力的行星（strong Grah）占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升 Pad（Lagn Pad）是否被有力的行星（strong Grah）占据"}, {"fact_key": "Dar Pad（Kalatr Pad）是否被有力的行星（strong Grah）占据"}]}, "selection_group": "ch29-v30-37-dar-pad-angle-trine-rich-famous.step-001:configuration", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）是否被有力的行星（strong Grah）占据、Dar Pad（Kalatr Pad）是否被有力的行星（strong Grah）占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 trine（三角宫）读成三分盘（Drekkana D3）。", "不得据此推断名声的领域或财富数额。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升 Pad（Lagn Pad）落在哪一宫、本盘 Dar Pad（Kalatr Pad）落在哪一宫。
- 缺失即停字段：["本盘上升 Pad（Lagn Pad）落在哪一宫", "本盘 Dar Pad（Kalatr Pad）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v30-37`｜PDF [63]｜“If the Dar Pad falls in an angle, or in a trine, counted from Lagn Pad, or, if Lagn Pad and Dar Pad both have strong Grahas, the native will be rich and be famous in his country.”


## 四路查书计划

### 支持路

- If the Dar Pad falls in an angle, or in a trine, counted from Lagn Pad, or, if Lagn Pad and Dar Pad both have strong Grahas, the native will be rich and be famous in his country.
- Dar Pad 落上升 Pad 的角宫三角宫 富有有名

### 反例或取消路

- If the Dar Pad falls in the 6<sup>th</sup> / 8<sup>th</sup> /12<sup>th</sup> from Lagn Pad, then the native will be poor.
- Dar Pad 落 6、8、12 宫时的贫穷条

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- Dar (Kalatr) of Yuvati
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- Dar Pad 是哪一个 Pad

## 上游问题

- 无

## 停止条件

- 缺少上升 Pad 或 Dar Pad 落宫事实时停止。
- 缺少两个 Pad 内是否有有力行星的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
