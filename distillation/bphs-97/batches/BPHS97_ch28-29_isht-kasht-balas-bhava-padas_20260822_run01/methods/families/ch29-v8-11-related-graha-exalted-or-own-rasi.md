---
method: ch29-v8-11-related-graha-exalted-or-own-rasi
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 关联行星入旺或落本星座：得益丰厚、快乐丰厚

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的财运能有多旺
- 这颗管我进项的星强不强

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升 Pad（Lagn Pad）落在哪一宫

## 按情况检查的事实

- 上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）占据
- 上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）相照
- 与上升 Pad（Lagn Pad）起第 11 宫发生关联的行星（Grah）是否入旺
- 与上升 Pad（Lagn Pad）起第 11 宫发生关联的行星（Grah）是否落本星座（own Rāśi）

## 依赖方法

- 无

## 执行步骤

### ch29-v8-11-related-graha-exalted-or-own-rasi.step-001

- 动作：先认出与上升 Pad（Lagn Pad）起第 11 宫发生关联的那颗行星，再看它是否入旺、或落自己主管的星座。
- 适用范围：原文的「the Grah in question」指同偈前句中占据上升 Pad 起第 11 宫、或相照该宫的那颗行星；原文以 etc. 泛指其他同类尊贵位置而未列举，未列举者不在本条内。own Rāśi 是行星自己主管的星座，不是本宫。
- 原文最小意思：上升 Pad（Lagn Pad）起第 11 宫被占据，或受相照，所论的那颗行星入旺、或落本星座（own Rāśi）时，得益丰厚、快乐丰厚。
- 本步骤产出事实：["上升 Pad 起第 11 宫关联行星的尊贵加成判定"]
- 所需事实：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）占据"}, {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）相照"}]}, {"operator": "OR", "operands": [{"fact_key": "与上升 Pad（Lagn Pad）起第 11 宫发生关联的行星（Grah）是否入旺"}, {"fact_key": "与上升 Pad（Lagn Pad）起第 11 宫发生关联的行星（Grah）是否落本星座（own Rāśi）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）占据"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）占据"}, "selection_group": "ch29-v8-11-related-graha-exalted-or-own-rasi.step-001:relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）占据。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）相照"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）相照"}, "selection_group": "ch29-v8-11-related-graha-exalted-or-own-rasi.step-001:relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）相照。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["与上升 Pad（Lagn Pad）起第 11 宫发生关联的行星（Grah）是否入旺"], "branch_condition_logic": {"fact_key": "与上升 Pad（Lagn Pad）起第 11 宫发生关联的行星（Grah）是否入旺"}, "selection_group": "ch29-v8-11-related-graha-exalted-or-own-rasi.step-001:dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：与上升 Pad（Lagn Pad）起第 11 宫发生关联的行星（Grah）是否入旺。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["与上升 Pad（Lagn Pad）起第 11 宫发生关联的行星（Grah）是否落本星座（own Rāśi）"], "branch_condition_logic": {"fact_key": "与上升 Pad（Lagn Pad）起第 11 宫发生关联的行星（Grah）是否落本星座（own Rāśi）"}, "selection_group": "ch29-v8-11-related-graha-exalted-or-own-rasi.step-001:dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：与上升 Pad（Lagn Pad）起第 11 宫发生关联的行星（Grah）是否落本星座（own Rāśi）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 own Rāśi（本星座）改读成本宫（Bhava）。", "不得据此推断得益的具体数额或时段。", "原文用 etc. 未列举的其他尊贵位置不得自行补入。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升 Pad（Lagn Pad）落在哪一宫。
- 缺失即停字段：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v8-11`｜PDF [62]｜“If the 11<sup>th</sup> from Lagn Pad is occupied, or receives a Drishti from a Grah the native will be happy and rich”
  - `bphs-97:santhanam:ch29:v8-11`｜PDF [62]｜“If the Grah in question be in exaltation, or in own Rashietc., there will be plenty of gains and plenty of happiness.”


## 四路查书计划

### 支持路

- If the Grah in question be in exaltation, or in own Rashietc., there will be plenty of gains and plenty of happiness
- 关联行星入旺或落本星座 得益丰厚

### 反例或取消路

- 无

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- 行星尊贵与力量怎么算

## 上游问题

- 无

## 停止条件

- 缺少本盘上升 Pad（Lagn Pad）落宫事实时停止。
- 无法确定与上升 Pad 起第 11 宫关联的是哪颗行星时停止。
- 原文以 etc. 泛指的其他尊贵位置未确定，落在这些位置时停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
