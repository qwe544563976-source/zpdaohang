---
method: ch29-v30-37-strong-graha-occupation-marital-happiness
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 有力行星占据上升 Pad 及其第 7、角、三角、Upachaya 宫：夫妻和乐

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的婚姻幸不幸福
- 夫妻关系怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升 Pad（Lagn Pad）落在哪一宫

## 按情况检查的事实

- 上升 Pad（Lagn Pad）是否被有力的行星（strong Grah）占据
- 上升 Pad（Lagn Pad）起第 7 宫是否被有力的行星（strong Grah）占据
- 上升 Pad（Lagn Pad）起算的角宫（Kendra）是否被有力的行星（strong Grah）占据
- 上升 Pad（Lagn Pad）起算的三角宫（Kona）是否被有力的行星（strong Grah）占据
- 上升 Pad（Lagn Pad）起算的 Upachaya 宫是否被有力的行星（strong Grah）占据

## 依赖方法

- 无

## 执行步骤

### ch29-v30-37-strong-graha-occupation-marital-happiness.step-001

- 动作：先定出本盘上升 Pad（Lagn Pad）落在哪一宫，再看有力的行星占据的是上升 Pad 与其起第 7 宫，还是从其起算的角宫、三角宫或 Upachaya 宫。
- 适用范围：力量判准原文未在本偈给出，见第 27 章六力（Shad Bal）诸目；原文断的是夫妻双方之间的和乐。
- 原文最小意思：上升 Pad（Lagn Pad）与其起第 7 宫，或从其起算的角宫、三角宫、Upachaya 宫被有力的行星占据时，夫妻之间和乐。
- 本步骤产出事实：["上升 Pad 一路被有力行星占据的夫妻和乐判定"]
- 所需事实：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "上升 Pad（Lagn Pad）是否被有力的行星（strong Grah）占据"}, {"fact_key": "上升 Pad（Lagn Pad）起第 7 宫是否被有力的行星（strong Grah）占据"}]}, {"fact_key": "上升 Pad（Lagn Pad）起算的角宫（Kendra）是否被有力的行星（strong Grah）占据"}, {"fact_key": "上升 Pad（Lagn Pad）起算的三角宫（Kona）是否被有力的行星（strong Grah）占据"}, {"fact_key": "上升 Pad（Lagn Pad）起算的 Upachaya 宫是否被有力的行星（strong Grah）占据"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）是否被有力的行星（strong Grah）占据", "上升 Pad（Lagn Pad）起第 7 宫是否被有力的行星（strong Grah）占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升 Pad（Lagn Pad）是否被有力的行星（strong Grah）占据"}, {"fact_key": "上升 Pad（Lagn Pad）起第 7 宫是否被有力的行星（strong Grah）占据"}]}, "selection_group": "ch29-v30-37-strong-graha-occupation-marital-happiness.step-001:occupied-place", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）是否被有力的行星（strong Grah）占据、上升 Pad（Lagn Pad）起第 7 宫是否被有力的行星（strong Grah）占据。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起算的角宫（Kendra）是否被有力的行星（strong Grah）占据"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起算的角宫（Kendra）是否被有力的行星（strong Grah）占据"}, "selection_group": "ch29-v30-37-strong-graha-occupation-marital-happiness.step-001:occupied-place", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起算的角宫（Kendra）是否被有力的行星（strong Grah）占据。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起算的三角宫（Kona）是否被有力的行星（strong Grah）占据"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起算的三角宫（Kona）是否被有力的行星（strong Grah）占据"}, "selection_group": "ch29-v30-37-strong-graha-occupation-marital-happiness.step-001:occupied-place", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起算的三角宫（Kona）是否被有力的行星（strong Grah）占据。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起算的 Upachaya 宫是否被有力的行星（strong Grah）占据"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起算的 Upachaya 宫是否被有力的行星（strong Grah）占据"}, "selection_group": "ch29-v30-37-strong-graha-occupation-marital-happiness.step-001:occupied-place", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起算的 Upachaya 宫是否被有力的行星（strong Grah）占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 trine（三角宫）读成三分盘（Drekkana D3）。", "不得据此推断结婚时间或配偶特征。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升 Pad（Lagn Pad）落在哪一宫。
- 缺失即停字段：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v30-37`｜PDF [63]｜“If Lagn Pad and the 7<sup>th</sup> therefrom, or an angle, a trine, an Upachaya therefrom is occupied by a strong Grah, there will be happiness between the husband and wife.”


## 四路查书计划

### 支持路

- If Lagn Pad and the 7<sup>th</sup> therefrom, or an angle, a trine, an Upachaya therefrom is occupied by a strong Grah, there will be happiness between the husband and wife.
- 有力行星占据上升 Pad 一路 夫妻和乐

### 反例或取消路

- If these be in mutually 6<sup>th</sup> /8<sup>th</sup> /12<sup>th</sup> , doubtlessly mutual enmity will crop up.
- 两 Pad 互为 6、8、12 时的敌意条

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 有力怎么判

## 上游问题

- 无

## 停止条件

- 缺少本盘上升 Pad（Lagn Pad）落宫事实时停止。
- 缺少各处是否被有力行星占据的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
