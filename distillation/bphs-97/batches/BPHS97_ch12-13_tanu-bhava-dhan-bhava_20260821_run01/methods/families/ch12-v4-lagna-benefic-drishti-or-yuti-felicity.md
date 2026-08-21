---
method: ch12-v4-lagna-benefic-drishti-or-yuti-felicity
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 身体安适：上升被吉星相照或一宫内有吉星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身体上过得舒不舒服
- 上升被吉星照代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 上升（Lagn）是否被吉星相照
- 一宫（Tanu）是否被吉星占据

## 依赖方法

- 无

## 执行步骤

### ch12-v4-lagna-benefic-drishti-or-yuti-felicity.step-001

- 动作：核对上升是否被吉星相照，或一宫里是否有吉星。
- 适用范围：仅限本命盘一宫（Tanu Bhava）身体安适主题；原文没有给时间限定。
- 原文最小意思：上升（Lagn）被吉星相照，或一宫内有吉星时，会享有身体的安适。
- 本步骤产出事实：["上升得吉星的身体安适判定"]
- 所需事实：["本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"operator": "OR", "operands": [{"fact_key": "上升（Lagn）是否被吉星相照"}, {"fact_key": "一宫（Tanu）是否被吉星占据"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["上升（Lagn）是否被吉星相照"], "branch_condition_logic": {"fact_key": "上升（Lagn）是否被吉星相照"}, "selection_group": "ch12-v4-lagna-benefic-drishti-or-yuti-felicity.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升（Lagn）是否被吉星相照。"}, {"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["一宫（Tanu）是否被吉星占据"], "branch_condition_logic": {"fact_key": "一宫（Tanu）是否被吉星占据"}, "selection_group": "ch12-v4-lagna-benefic-drishti-or-yuti-felicity.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：一宫（Tanu）是否被吉星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富、寿命或子女，本句只说身体安适。", "不得据此推断安适出现的年份或大运。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v4`｜PDF [26]｜“Felicity of the body will be enjoyed, if Lagn is drishtied by, or yuti with a benefic.”


## 四路查书计划

### 支持路

- Felicity of the body will be enjoyed, if Lagn is drishtied by, or yuti with a benefic
- 上升被吉星相照或一宫有吉星 身体安适

### 反例或取消路

- There will not be bodily health, if Lagna, or Chandra be drishtied by, or yuti with a malefic, being devoid of a benefics Drishti
- Should Lagn Lord be yuti with a malefic, or be in Randhr, 6th, or 12th, physical felicity will diminish

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi

### 判断方法路

- Effects of Tanu Bhava
- Effects of Lagn’s Lord in Various Bhavas (up to Sloka 12). Should Lagn’s Lord be in Lagn itself, the native will be endowed with physical happiness and prowess
- 判断身体安适要看上升有没有吉星照或同宫

## 上游问题

- 无

## 停止条件

- 缺少吉星名册事实时停止。
- 相照与同宫两个分支事实全缺时停止。
- 吉星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
