---
method: ch29-v16-17-benefic-fair-means
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升 Pad 起第 12 宫关联吉星：收支经由正当途径

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的钱进出正不正当
- 开销是走正路还是歪路

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升 Pad（Lagn Pad）落在哪一宫

## 按情况检查的事实

- 上升 Pad（Lagn Pad）起第 12 宫是否被吉星相照
- 上升 Pad（Lagn Pad）起第 12 宫是否与吉星同宫

## 依赖方法

- 无

## 执行步骤

### ch29-v16-17-benefic-fair-means.step-001

- 动作：看与上升 Pad（Lagn Pad）起第 12 宫相照或同宫的是不是吉星，据此断收支途径。
- 适用范围：原文的「will cause」承同偈前句的丰厚进项与大量开销；吉星判准见第 3 章第 11 偈。
- 原文最小意思：上升 Pad（Lagn Pad）起第 12 宫受相照、或与之同宫的是吉星时，前述进项与开销经由正当途径。
- 本步骤产出事实：["上升 Pad 起第 12 宫收支途径的吉星判定"]
- 所需事实：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否被吉星相照"}, {"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否与吉星同宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 12 宫是否被吉星相照"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否被吉星相照"}, "selection_group": "ch29-v16-17-benefic-fair-means.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 12 宫是否被吉星相照。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 12 宫是否与吉星同宫"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否与吉星同宫"}, "selection_group": "ch29-v16-17-benefic-fair-means.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 12 宫是否与吉星同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断具体开销项目或金额。", "不得把正当途径读成收入必然增加。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升 Pad（Lagn Pad）落在哪一宫。
- 缺失即停字段：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v16-17`｜PDF [62]｜“If the 12<sup>th</sup> from Lagn Pad receives a Drishti from, or is yuti with both benefics and malefics, there will be abundant earnings, but plenty of expenses.”
  - `bphs-97:santhanam:ch29:v16-17`｜PDF [62]｜“The benefic will cause through fair means, malefic through unfair means and mixed Grahas through both fair and unfair means.”


## 四路查书计划

### 支持路

- The benefic will cause through fair means
- 上升 Pad 起第 12 宫吉星 正当途径

### 反例或取消路

- malefic through unfair means
- 凶星关联时的不正当途径

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics.
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 哪些行星算吉星

## 上游问题

- 无

## 停止条件

- 缺少上升 Pad 起第 12 宫与吉星的相照或同宫事实时停止。
- 缺少本盘上升 Pad（Lagn Pad）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
