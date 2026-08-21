---
method: ch23-v12-benefic-supported-vyaya-own-country
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 在自己国内活动：十二宫主与十二宫皆有吉星，且宫主与吉星互照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会一直待在本地
- 我适不适合出国

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十二宫主（Vyaya's Lord）是否与吉星同宫
- 十二宫（Vyaya）是否被吉星占据

## 按情况检查的事实

- 十二宫主（Vyaya's Lord）是否相照吉星
- 十二宫主（Vyaya's Lord）是否被吉星相照

## 依赖方法

- 无

## 执行步骤

### ch23-v12-benefic-supported-vyaya-own-country.step-001

- 动作：先核对十二宫主（Vyaya's Lord）是否与吉星同宫、十二宫（Vyaya）内是否有吉星，再核对十二宫主是否相照吉星或被吉星相照。
- 适用范围：仅限本命盘十二宫（Vyaya Bhava）主题；原文把同宫与占据两项并列为共同前提，相照方向为择一；原文未给时间限定。
- 原文最小意思：十二宫主（Vyaya's Lord）与吉星同宫、十二宫（Vyaya）内有吉星，并且十二宫主相照吉星或被吉星相照时，命主会在自己的国家内活动。
- 本步骤产出事实：["十二宫受吉时的本国活动判定"]
- 所需事实：["十二宫主（Vyaya's Lord）是否与吉星同宫", "十二宫（Vyaya）是否被吉星占据"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否与吉星同宫"}, {"fact_key": "十二宫（Vyaya）是否被吉星占据"}]}, {"operator": "OR", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否相照吉星"}, {"fact_key": "十二宫主（Vyaya's Lord）是否被吉星相照"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否与吉星同宫"}, {"fact_key": "十二宫（Vyaya）是否被吉星占据"}]}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否相照吉星"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否相照吉星"}, "selection_group": "ch23-v12-benefic-supported-vyaya-own-country.step-001:benefic-drishti-direction", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否相照吉星。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否与吉星同宫"}, {"fact_key": "十二宫（Vyaya）是否被吉星占据"}]}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否被吉星相照"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否被吉星相照"}, "selection_group": "ch23-v12-benefic-supported-vyaya-own-country.step-001:benefic-drishti-direction", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否被吉星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得省掉同宫与占据两项共同前提，只凭相照下判断。", "不得把「在自己的国家内活动」读成不能出国或必定富裕。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十二宫主（Vyaya's Lord）是否与吉星同宫、十二宫（Vyaya）是否被吉星占据。
- 缺失即停字段：["十二宫主（Vyaya's Lord）是否与吉星同宫", "十二宫（Vyaya）是否被吉星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch23:v12`｜PDF [40]｜“One will move in his own country, if Vyaya’s Lord and Vyaya Bhava are with benefics and Vyaya’s Lord gives a Drishti to, or receives a Drishti from benefics.”


## 四路查书计划

### 支持路

- One will move in his own country, if Vyaya’s Lord and Vyaya Bhava are with benefics
- 十二宫主 与吉星同宫 十二宫有吉星 相照 本国活动

### 反例或取消路

- One will wander from country to country, if Vyaya’s Lord and Vyaya Bhava are with malefics and Vyaya’s Lord gives a Drishti to, or receives a Drishti from malefics.
- If Bandhu, Karm and Vyaya Bhava are all occupied by malefics, both the parents will leave the child to its own fate and wander from place to place.

### 适用边界路

- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Benefics in both Vyaya and Dhan Bhava cause Subh Yog. Malefics in both Vyaya and Dhan Bhava cause Asubh Yog.

### 判断方法路

- Effects of Vyaya’s Lord in Various Bhavas
- 十二宫受吉星支持时怎么判断行止

## 上游问题

- 无

## 停止条件

- 缺少十二宫主是否与吉星同宫的事实时停止。
- 缺少十二宫是否被吉星占据的事实时停止。
- 两个相照方向的事实都缺失时停止。
- 吉星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
