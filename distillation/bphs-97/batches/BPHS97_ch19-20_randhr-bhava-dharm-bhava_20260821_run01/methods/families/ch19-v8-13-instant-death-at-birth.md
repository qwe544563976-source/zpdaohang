---
method: ch19-v8-13-instant-death-at-birth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 出生时即刻去世：八宫、八宫主与十二宫都与凶星会合

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 八宫十二宫都有凶星意味着什么
- 出生时的凶险组合有哪些

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫（Randhr）是否被凶星占据
- 八宫主（Randhr's Lord）是否与凶星同宫
- 十二宫（Vyaya）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch19-v8-13-instant-death-at-birth.step-001

- 动作：核对八宫（Randhr）、八宫主（Randhr's Lord）与十二宫（Vyaya）是否都与凶星会合。
- 适用范围：仅限本命盘寿命主题；原文断在出生当时，未给其他时间限定。
- 原文最小意思：八宫、八宫主与十二宫都与凶星会合时，出生时即刻去世。
- 本步骤产出事实：["三处皆会凶星的出生即刻去世判定"]
- 所需事实：["八宫（Randhr）是否被凶星占据", "八宫主（Randhr's Lord）是否与凶星同宫", "十二宫（Vyaya）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "八宫（Randhr）是否被凶星占据"}, {"fact_key": "八宫主（Randhr's Lord）是否与凶星同宫"}, {"fact_key": "十二宫（Vyaya）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断死因或去世的具体时刻。", "不得只凭三项中的一两项成立就下断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫（Randhr）是否被凶星占据、八宫主（Randhr's Lord）是否与凶星同宫、十二宫（Vyaya）是否被凶星占据。
- 缺失即停字段：["八宫（Randhr）是否被凶星占据", "八宫主（Randhr's Lord）是否与凶星同宫", "十二宫（Vyaya）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v8-13`｜PDF [36]｜“Death will be instant at birth, if Randhr Bhava, Randhr’s Lord and Vyaya Bhava are all conjunct malefics.”


## 四路查书计划

### 支持路

- Death will be instant at birth, if Randhr Bhava, Randhr’s Lord and Vyaya Bhava are all conjunct malefics
- 八宫 八宫主 十二宫 皆与凶星 出生即刻去世

### 反例或取消路

- a single, but strong Guru in Lagn will ward off all the evils
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- Should Shani, Surya and Mangal be in Vyaya, Dharm and Randhr Bhava without Drishti from a benefic, the child will face instant death

### 判断方法路

- first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas
- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- 出生凶险组合与解厄怎么一起看

## 上游问题

- 无

## 停止条件

- 缺少八宫、八宫主或十二宫的凶星事实时停止。
- 凶星名册未定时停止（吉凶星判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
