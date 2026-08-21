---
method: ch17-v7-leprosy-lagna-lord
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 麻风：火星或水星主管上升星座并与月亮、罗睺、土星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会得麻风一类的重皮肤病
- 上升主与凶星同宫会怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagna's Lord）是哪颗行星
- 上升主（Lagna's Lord）是否与月亮（Chandra）同宫
- 上升主（Lagna's Lord）是否与罗睺（Rahu）同宫
- 上升主（Lagna's Lord）是否与土星（Shani）同宫

## 按情况检查的事实

- 上升主（Lagna's Lord）是否为火星（Mangal）
- 上升主（Lagna's Lord）是否为水星（Budh）

## 依赖方法

- 无

## 执行步骤

### ch17-v7-leprosy-lagna-lord.step-001

- 动作：先看上升星座由哪颗行星主管，再核对它与月亮、罗睺、土星的同宫。
- 适用范围：仅限本命盘麻风主题；原文未给上升星座、时间或麻风种类限定，种类另见同偈后文。
- 原文最小意思：火星或水星主管上升星座、并与月亮、罗睺、土星同宫时，会患麻风。
- 本步骤产出事实：["上升主聚月罗土的麻风判定"]
- 所需事实：["上升主（Lagna's Lord）是否与月亮（Chandra）同宫", "上升主（Lagna's Lord）是否与罗睺（Rahu）同宫", "上升主（Lagna's Lord）是否与土星（Shani）同宫", "本盘上升主（Lagna's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagna's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagna's Lord）是否与月亮（Chandra）同宫"}, {"fact_key": "上升主（Lagna's Lord）是否与罗睺（Rahu）同宫"}, {"fact_key": "上升主（Lagna's Lord）是否与土星（Shani）同宫"}]}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagna's Lord）是否为火星（Mangal）"}, {"fact_key": "上升主（Lagna's Lord）是否为水星（Budh）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagna's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagna's Lord）是否与月亮（Chandra）同宫"}, {"fact_key": "上升主（Lagna's Lord）是否与罗睺（Rahu）同宫"}, {"fact_key": "上升主（Lagna's Lord）是否与土星（Shani）同宫"}]}, "required_fact_keys": ["上升主（Lagna's Lord）是否为火星（Mangal）"], "branch_condition_logic": {"fact_key": "上升主（Lagna's Lord）是否为火星（Mangal）"}, "selection_group": "ch17-v7-leprosy-lagna-lord.step-001:ascendant-owner", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagna's Lord）是否为火星（Mangal）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagna's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagna's Lord）是否与月亮（Chandra）同宫"}, {"fact_key": "上升主（Lagna's Lord）是否与罗睺（Rahu）同宫"}, {"fact_key": "上升主（Lagna's Lord）是否与土星（Shani）同宫"}]}, "required_fact_keys": ["上升主（Lagna's Lord）是否为水星（Budh）"], "branch_condition_logic": {"fact_key": "上升主（Lagna's Lord）是否为水星（Budh）"}, "selection_group": "ch17-v7-leprosy-lagna-lord.step-001:ascendant-owner", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagna's Lord）是否为水星（Budh）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此判定麻风的种类，种类另有专条。", "不得据此推断发病年龄或轻重。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagna's Lord）是否与月亮（Chandra）同宫、上升主（Lagna's Lord）是否与罗睺（Rahu）同宫、上升主（Lagna's Lord）是否与土星（Shani）同宫、本盘上升主（Lagna's Lord）是哪颗行星。
- 缺失即停字段：["上升主（Lagna's Lord）是否与月亮（Chandra）同宫", "上升主（Lagna's Lord）是否与罗睺（Rahu）同宫", "上升主（Lagna's Lord）是否与土星（Shani）同宫", "本盘上升主（Lagna's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v7-8.5`｜PDF [32]｜“Mangal, or Budh, having ownership of the ascending Rashiand joining Chandra, Rahu and Shani, will cause leprosy.”


## 四路查书计划

### 支持路

- Mangal, or Budh, having ownership of the ascending Rashi joining Chandra, Rahu and Shani will cause leprosy
- 上升主为火星或水星 与月亮罗睺土星同宫 麻风

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed
- Guru in similar case will destroy any disease

### 适用边界路

- Shani and Chandra together in Ari bloodleprosy at the age of 45
- Antar Dashas leprosy 大运中出现麻风的时点
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Indications of Ari Bhava diseases ulcers
- 判断皮肤重症应检查上升主与哪些行星

## 上游问题

- 无

## 停止条件

- 缺少上升主身份事实时停止。
- 缺少上升主与月亮、罗睺、土星同宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
