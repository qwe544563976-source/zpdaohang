---
method: ch21-v18-obstructions-to-acts
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 作为受阻：十宫主落陷、十宫与从十宫起算的第十宫都被凶星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我做事为什么总是受阻
- 我的事业会不会一路碰壁

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否落陷
- 十宫（Karm）是否被凶星占据
- 从十宫（Karm）起算的第十宫是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v18-obstructions-to-acts.step-001

- 动作：核对十宫主（Karm's Lord）是否落陷，并核对十宫（Karm）与从十宫起算的第十宫是否都被凶星占据。
- 适用范围：仅限本命盘十宫（Karm）作为受阻主题；原文三个条件同时成立才下断语；原文未给阻碍种类与时间，凶星名册按本书自身的定义取。
- 原文最小意思：十宫主落陷、十宫与从十宫起算的第十宫都被凶星占据时，命主的作为会遇到阻碍。
- 本步骤产出事实：["十宫主落陷双宫逢凶作为受阻判定"]
- 所需事实：["十宫主（Karm's Lord）是否落陷", "十宫（Karm）是否被凶星占据", "从十宫（Karm）起算的第十宫是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落陷"}, {"fact_key": "十宫（Karm）是否被凶星占据"}, {"fact_key": "从十宫（Karm）起算的第十宫是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断阻碍的种类、起止时间或严重程度。", "不得只凭十宫主落陷一项就下断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否落陷、十宫（Karm）是否被凶星占据、从十宫（Karm）起算的第十宫是否被凶星占据。
- 缺失即停字段：["十宫主（Karm's Lord）是否落陷", "十宫（Karm）是否被凶星占据", "从十宫（Karm）起算的第十宫是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v18`｜PDF [39]｜“Obstructions to the native’s acts will crop up, if Karm’s Lord is in fall, as both Karm Bhava and the 10<sup>th</sup> from Karm Bhava have malefic occupations.”


## 四路查书计划

### 支持路

- Obstructions to the native’s acts will crop up, if Karm’s Lord is in fall, as both Karm Bhava and the 10th from Karm Bhava have malefic occupations
- 十宫主落陷 十宫被凶星占据 从十宫起算的第十宫 作为受阻

### 反例或取消路

- If the Karm’s Lord is exalted in an angle, or a trine and is yuti with Guru, or receives a Drishti from Guru, one will be endowed with deeds
- If Karm’s Lord is with a benefic, or be in an auspicious Bhava, one will always gain through royal patronage and in business

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava

### 判断方法路

- If Karm’s Lord is devoid of strength, the native will face obstructions in his work
- 判断作为受阻应检查十宫（Karm）与十宫主的哪些状态

## 上游问题

- 无

## 停止条件

- 缺少十宫主落陷事实时停止。
- 缺少十宫占据者事实时停止。
- 缺少从十宫起算的第十宫占据者事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
