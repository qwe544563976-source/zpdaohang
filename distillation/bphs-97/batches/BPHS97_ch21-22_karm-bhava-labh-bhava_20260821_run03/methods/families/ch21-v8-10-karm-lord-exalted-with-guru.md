---
method: ch21-v8-10-karm-lord-exalted-with-guru
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 荣誉财富与勇武：十宫主入旺并与木星同宫，同时九宫主落十宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子能不能有地位和财富
- 十宫主入旺又碰上木星会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否入旺
- 十宫主（Karm's Lord）是否与木星（Guru）同宫
- 九宫主（Dharm's Lord）是否落十宫（Karm）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v8-10-karm-lord-exalted-with-guru.step-001

- 动作：核对十宫主（Karm's Lord）是否入旺、是否与木星（Guru）同宫，并核对九宫主（Dharm's Lord）是否落十宫（Karm）。
- 适用范围：仅限三项条件同时成立这一种配置；原文未给上升与时间限定。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：十宫主入旺并与木星同宫，同时九宫主落十宫时，命主会获得荣誉、财富与勇武。
- 本步骤产出事实：["十宫主入旺与木星同宫的荣誉财富判定"]
- 所需事实：["十宫主（Karm's Lord）是否入旺", "十宫主（Karm's Lord）是否与木星（Guru）同宫", "九宫主（Dharm's Lord）是否落十宫（Karm）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否入旺"}, {"fact_key": "十宫主（Karm's Lord）是否与木星（Guru）同宫"}, {"fact_key": "九宫主（Dharm's Lord）是否落十宫（Karm）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断官职级别、财富数额或应期。", "不得把三项条件拆成任取其一。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否入旺、十宫主（Karm's Lord）是否与木星（Guru）同宫、九宫主（Dharm's Lord）是否落十宫（Karm）。
- 缺失即停字段：["十宫主（Karm's Lord）是否入旺", "十宫主（Karm's Lord）是否与木星（Guru）同宫", "九宫主（Dharm's Lord）是否落十宫（Karm）"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v8-10`｜PDF [38]｜“Should Karm’s Lord be in exaltation and be in the company of Guru, as Dharm’s Lord is in Karm the native will be endowed with honour, wealth and valour.”


## 四路查书计划

### 支持路

- Should Karm’s Lord be in exaltation and be in the company of Guru, as Dharm’s Lord is in Karm the native will be endowed with honour, wealth and valour
- 十宫主入旺 与木星同宫 九宫主落十宫 荣誉 财富 勇武

### 反例或取消路

- If Karm’s Lord is devoid of strength, the native will face obstructions in his work
- Should Karm and Labh Bhava be both occupied by malefics, the native will indulge only in bad deeds
- 十宫主无力 事业受阻

### 适用边界路

- If Dharm’s Lord is in Karm Bhava, the native will be a king, or equal to him, or be a minister, or an Army chief
- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava

### 判断方法路

- Effects of Karm’s Lord in Various Bhavas
- 判断荣誉与财富要核对十宫主与九宫主

## 上游问题

- 无

## 停止条件

- 缺少十宫主入旺事实时停止。
- 缺少十宫主与木星同宫的事实时停止。
- 缺少九宫主落十宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
