---
method: ch12-v3-lagna-or-chandra-afflicted-no-bodily-health
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 身体不健康：上升或月亮受凶星相照或同宫且无吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身体健不健康
- 上升和月亮被凶星冲代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星
- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 上升（Lagn）是否被凶星相照
- 一宫（Tanu）是否被凶星占据
- 月亮（Chandra）是否被凶星相照
- 月亮（Chandra）是否与凶星同宫
- 上升（Lagn）是否被吉星相照
- 月亮（Chandra）是否被吉星相照

## 依赖方法

- 无

## 执行步骤

### ch12-v3-lagna-or-chandra-afflicted-no-bodily-health.step-001

- 动作：分别对上升与月亮核对：是否被凶星相照、是否与凶星同宫，且同时得不到吉星相照。
- 适用范围：仅限本命盘一宫（Tanu Bhava）身体健康主题；原文的 being devoid of a benefics Drishti 跟着同一个主语（上升或月亮），不得改挂到另一方。
- 原文最小意思：上升（Lagna）或月亮（Chandra）被凶星相照或与凶星同宫，同时又得不到吉星相照时，身体不会健康。
- 本步骤产出事实：["上升或月亮受克的身体健康判定"]
- 所需事实：["本盘中哪些行星被判为凶星", "本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "上升（Lagn）是否被凶星相照"}, {"operator": "NOT", "operands": [{"fact_key": "上升（Lagn）是否被吉星相照"}]}]}, {"operator": "AND", "operands": [{"fact_key": "一宫（Tanu）是否被凶星占据"}, {"operator": "NOT", "operands": [{"fact_key": "上升（Lagn）是否被吉星相照"}]}]}, {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否被凶星相照"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否被吉星相照"}]}]}, {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否被吉星相照"}]}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["上升（Lagn）是否被凶星相照", "上升（Lagn）是否被吉星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升（Lagn）是否被凶星相照"}, {"operator": "NOT", "operands": [{"fact_key": "上升（Lagn）是否被吉星相照"}]}]}, "selection_group": "ch12-v3-lagna-or-chandra-afflicted-no-bodily-health.step-001:afflicted-subject", "stop_condition": "选中该分支后，缺少以下事实即停止：上升（Lagn）是否被凶星相照、上升（Lagn）是否被吉星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["一宫（Tanu）是否被凶星占据", "上升（Lagn）是否被吉星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "一宫（Tanu）是否被凶星占据"}, {"operator": "NOT", "operands": [{"fact_key": "上升（Lagn）是否被吉星相照"}]}]}, "selection_group": "ch12-v3-lagna-or-chandra-afflicted-no-bodily-health.step-001:afflicted-subject", "stop_condition": "选中该分支后，缺少以下事实即停止：一宫（Tanu）是否被凶星占据、上升（Lagn）是否被吉星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["月亮（Chandra）是否被凶星相照", "月亮（Chandra）是否被吉星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否被凶星相照"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否被吉星相照"}]}]}, "selection_group": "ch12-v3-lagna-or-chandra-afflicted-no-bodily-health.step-001:afflicted-subject", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否被凶星相照、月亮（Chandra）是否被吉星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["月亮（Chandra）是否与凶星同宫", "月亮（Chandra）是否被吉星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否与凶星同宫"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否被吉星相照"}]}]}, "selection_group": "ch12-v3-lagna-or-chandra-afflicted-no-bodily-health.step-001:afflicted-subject", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否与凶星同宫、月亮（Chandra）是否被吉星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此断出寿夭、死因或具体病症，原文只说不会有身体健康。", "不得把无吉星相照这一条挪到与受克对象不同的另一方身上。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星、本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘中哪些行星被判为凶星", "本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v3`｜PDF [26]｜“There will not be bodily health, if Lagna, or Chandra be drishtied by, or yuti with a malefic, being devoid of a benefics Drishti.”


## 四路查书计划

### 支持路

- There will not be bodily health, if Lagna, or Chandra be drishtied by, or yuti with a malefic, being devoid of a benefics Drishti
- 上升或月亮被凶星相照同宫且无吉星相照 身体不健康

### 反例或取消路

- Felicity of the body will be enjoyed, if Lagn is drishtied by, or yuti with a benefic
- With a benefic in an angle, or trine all diseases will disappear

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Malefics, occupying Tanu and Yuvati Bhava, while Chandra is yuti with a malefic with no relief from a benefic, will also cause premature death
- Chandra in Tanu, Randhr, Vyaya, or Yuvati Bhava and hemmed between malefics will confer premature death

### 判断方法路

- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- Whatever results are to be known from Bandhu, Tanu, Dhan, Labh and Dharm should also be known from the 4th of Chandra, from Kark Rashiitself and from the 2nd, 11th and 9th from Chandra, respectively
- 判断身体健康要同时看上升和月亮受不受克

## 上游问题

- 无

## 停止条件

- 缺少吉星或凶星名册事实时停止。
- 四个受克分支事实全缺时停止。
- 凶星名册未定时停止（吉凶判准见第3章 v11）。
- 吉星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
