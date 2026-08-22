---
method: ch24-v6-lagn-lord-in-ari-with-malefic
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升主落六宫且与凶星关联、无吉星相照：没有身体安乐并受敌人困扰

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我为什么老是身体不舒服还犯小人
- 我和对手之间的处境怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星
- 本盘中哪些行星被判为吉星
- 上升主（Lagn's Lord）是否落六宫（Ari）
- 上升主（Lagn's Lord）是否与凶星发生关联
- 原文未指明相照对象的吉星相照（benefic Drishti）是否存在

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v6-lagn-lord-in-ari-with-malefic.step-001

- 动作：先确定本盘吉星与凶星名册，再核对上升主（Lagn's Lord）是否落六宫（Ari）、是否与凶星发生关联，以及原文所说的吉星相照是否存在。
- 适用范围：仅限本命盘上升主落六宫（Ari Bhava）一条；原文只说 related to a malefic，未在本偈界定「关联」是同宫还是相照；原文只说 if there is no benefic Drishti，未指明受相照的对象是上升主还是六宫——两处均未确定即停判；原文未给时间限定。
- 原文最小意思：上升主（Lagn's Lord）落六宫（Ari）、与凶星发生关联（related to a malefic），且没有吉星相照（no benefic Drishti）时，本人没有身体安乐，并受敌人困扰。
- 本步骤产出事实：["上升主落六宫与凶星关联时的身体与敌人判定"]
- 所需事实：["本盘中哪些行星被判为凶星", "本盘中哪些行星被判为吉星", "上升主（Lagn's Lord）是否落六宫（Ari）", "上升主（Lagn's Lord）是否与凶星发生关联", "原文未指明相照对象的吉星相照（benefic Drishti）是否存在"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "上升主（Lagn's Lord）是否落六宫（Ari）"}, {"fact_key": "上升主（Lagn's Lord）是否与凶星发生关联"}, {"operator": "NOT", "operands": [{"fact_key": "原文未指明相照对象的吉星相照（benefic Drishti）是否存在"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「无吉星相照」默认绑定到上升主一方或六宫一方——原文未指明相照对象。", "不得把「与凶星发生关联」自行坐实为同宫、相照或任何一种具体关系——原文未在本偈界定。", "不得据此推断疾病名称、敌人身份或发生时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星、本盘中哪些行星被判为吉星、上升主（Lagn's Lord）是否落六宫（Ari）、上升主（Lagn's Lord）是否与凶星发生关联、原文未指明相照对象的吉星相照（benefic Drishti）是否存在。
- 缺失即停字段：["本盘中哪些行星被判为凶星", "本盘中哪些行星被判为吉星", "上升主（Lagn's Lord）是否落六宫（Ari）", "上升主（Lagn's Lord）是否与凶星发生关联", "原文未指明相照对象的吉星相照（benefic Drishti）是否存在"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v6`｜PDF [41]｜“If Lagn’s Lord is in Ari Bhava and related to a malefic the native will be devoid of physical happiness and will be troubled by enemies, if there is no benefic Drishti.”


## 四路查书计划

### 支持路

- If Lagn’s Lord is in Ari Bhava and related to a malefic the native will be devoid of physical happiness and will be troubled by enemies
- 上升主落六宫 与凶星关联 无吉星相照 敌人困扰

### 反例或取消路

- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle
- If there is a Drishti in the process from a benefic, then these evils will not mature
- Should Lagn’s Lord be in Lagn itself, the native will be endowed with physical happiness and prowess

### 适用边界路

- Indications of Ari Bhava. Maternal uncle, doubts about death, enemies, ulcers, stepmother etc. are to be estimated from Ari Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- If a malefic is related to the said placement by yuti with Dhan’s Lord, or by Drishti, the native’s wife will be of questionable character

### 判断方法路

- Effects of Ari’s Lord in Various Bhavas
- Effects of Lagn’s Lord in Various Bhavas

## 上游问题

- 无

## 停止条件

- 缺少上升主是否落六宫的事实时停止。
- 原文未界定「与凶星发生关联」的形式，该事实未确定即停止。
- 原文未指明吉星相照的对象是上升主还是六宫，该事实未确定即停止。
- 吉星名册或凶星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
