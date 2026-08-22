---
method: ch29-v30-37-dar-pad-6-8-12-poor
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Dar Pad 落上升 Pad 起第 6、8、12 宫：命主贫穷

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会一直缺钱
- 夫妻位落在坏位置有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘 Dar Pad（Kalatr Pad）落在哪一宫

## 按情况检查的事实

- Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 6 宫
- Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 8 宫
- Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 12 宫

## 依赖方法

- 无

## 执行步骤

### ch29-v30-37-dar-pad-6-8-12-poor.step-001

- 动作：先定出 Dar Pad（Kalatr Pad）落在哪一宫，再看它从上升 Pad（Lagn Pad）起算是否落第 6、8 或 12 宫。
- 适用范围：本条以上升 Pad（Lagn Pad）为起算点；原文没有给时间或程度限定。
- 原文最小意思：Dar Pad（Kalatr Pad）从上升 Pad（Lagn Pad）起算落在第 6 宫、第 8 宫、或第 12 宫时，命主贫穷。
- 本步骤产出事实：["上升 Pad 与 Dar Pad 相对位置的贫穷判定"]
- 所需事实：["本盘 Dar Pad（Kalatr Pad）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 6 宫"}, {"fact_key": "Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 8 宫"}, {"fact_key": "Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 12 宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}, "required_fact_keys": ["Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 6 宫"], "branch_condition_logic": {"fact_key": "Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 6 宫"}, "selection_group": "ch29-v30-37-dar-pad-6-8-12-poor.step-001:position", "stop_condition": "选中该分支后，缺少以下事实即停止：Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 6 宫。"}, {"when": {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}, "required_fact_keys": ["Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 8 宫"], "branch_condition_logic": {"fact_key": "Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 8 宫"}, "selection_group": "ch29-v30-37-dar-pad-6-8-12-poor.step-001:position", "stop_condition": "选中该分支后，缺少以下事实即停止：Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 8 宫。"}, {"when": {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}, "required_fact_keys": ["Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 12 宫"], "branch_condition_logic": {"fact_key": "Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 12 宫"}, "selection_group": "ch29-v30-37-dar-pad-6-8-12-poor.step-001:position", "stop_condition": "选中该分支后，缺少以下事实即停止：Dar Pad（Kalatr Pad）是否落上升 Pad（Lagn Pad）起第 12 宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断贫穷的时段或程度。", "不得把 Dar Pad 与本命第 7 宫混为一处。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘 Dar Pad（Kalatr Pad）落在哪一宫。
- 缺失即停字段：["本盘 Dar Pad（Kalatr Pad）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v30-37`｜PDF [63]｜“If the Dar Pad falls in the 6<sup>th</sup> / 8<sup>th</sup> /12<sup>th</sup> from Lagn Pad, then the native will be poor.”


## 四路查书计划

### 支持路

- If the Dar Pad falls in the 6<sup>th</sup> / 8<sup>th</sup> /12<sup>th</sup> from Lagn Pad, then the native will be poor.
- Dar Pad 落上升 Pad 起第 6、8、12 宫 贫穷

### 反例或取消路

- If the Dar Pad falls in an angle, or in a trine, counted from Lagn Pad, or, if Lagn Pad and Dar Pad both have strong Grahas, the native will be rich and be famous in his country.
- Dar Pad 落角宫三角宫时的富名条

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- Dar (Kalatr) of Yuvati
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- Dar Pad 是哪一个 Pad

## 上游问题

- 无

## 停止条件

- 缺少 Dar Pad 相对上升 Pad 的位次事实时停止。
- 缺少本盘上升 Pad（Lagn Pad）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
