---
method: ch17-v2-ari-lord-ulcers
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 身上的溃疡与瘀伤：六宫主落六宫、上升宫或八宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身上会不会长疮或有瘀伤
- 我这辈子容易受什么外伤

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘六宫主（Ari's Lord）落在哪一宫

## 按情况检查的事实

- 六宫主（Ari's Lord）是否落六宫（Ari）
- 六宫主（Ari's Lord）是否落上升宫（Lagna）
- 六宫主（Ari's Lord）是否落八宫（Randhr）

## 依赖方法

- 无

## 执行步骤

### ch17-v2-ari-lord-ulcers.step-001

- 动作：核对六宫主（Ari's Lord）落在哪一宫，判断身体是否有溃疡或瘀伤。
- 适用范围：仅限本命盘六宫溃疡瘀伤主题；原文未给上升、时间或部位限定，部位另见同偈后半句。
- 原文最小意思：六宫主落六宫、上升宫或八宫时，身上会有溃疡或瘀伤。
- 本步骤产出事实：["六宫主落宫的溃疡瘀伤判定"]
- 所需事实：["本盘六宫主（Ari's Lord）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落六宫（Ari）"}, {"fact_key": "六宫主（Ari's Lord）是否落上升宫（Lagna）"}, {"fact_key": "六宫主（Ari's Lord）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘六宫主（Ari's Lord）落在哪一宫"}, "required_fact_keys": ["六宫主（Ari's Lord）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "六宫主（Ari's Lord）是否落六宫（Ari）"}, "selection_group": "ch17-v2-ari-lord-ulcers.step-001:ari-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫主（Ari's Lord）是否落六宫（Ari）。"}, {"when": {"fact_key": "本盘六宫主（Ari's Lord）落在哪一宫"}, "required_fact_keys": ["六宫主（Ari's Lord）是否落上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "六宫主（Ari's Lord）是否落上升宫（Lagna）"}, "selection_group": "ch17-v2-ari-lord-ulcers.step-001:ari-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫主（Ari's Lord）是否落上升宫（Lagna）。"}, {"when": {"fact_key": "本盘六宫主（Ari's Lord）落在哪一宫"}, "required_fact_keys": ["六宫主（Ari's Lord）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "六宫主（Ari's Lord）是否落八宫（Randhr）"}, "selection_group": "ch17-v2-ari-lord-ulcers.step-001:ari-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫主（Ari's Lord）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断溃疡或瘀伤的部位、发生年份或严重程度。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘六宫主（Ari's Lord）落在哪一宫。
- 缺失即停字段：["本盘六宫主（Ari's Lord）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v2`｜PDF [32]｜“Should Ari’s Lord be in Ari itself, or in Lagna, or Randhr, there will be ulcers, or bruises on the body.”


## 四路查书计划

### 支持路

- 六宫主落六宫 上升 八宫 溃疡 瘀伤

### 反例或取消路

- 吉星相关的部位只留印记而非溃疡

### 适用边界路

- Effects of Ari’s Lord in Various Bhavas 六宫主落各宫
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- 判断六宫溃疡应检查哪些位置

## 上游问题

- 无

## 停止条件

- 缺少六宫主落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
