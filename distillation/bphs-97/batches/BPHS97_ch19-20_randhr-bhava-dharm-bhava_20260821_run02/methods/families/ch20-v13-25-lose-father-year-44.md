---
method: ch20-v13-25-lose-father-year-44
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 命主第44年失去父亲：九宫主落十二宫、十二宫主落九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲的寿命大概到什么时候
- 九宫主与十二宫主互落说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否落十二宫（Vyaya）
- 十二宫主（Vyaya's Lord）是否落九宫（Dharm）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v13-25-lose-father-year-44.step-001

- 动作：核对九宫主（Dharm's Lord）是否落十二宫（Vyaya），并核对十二宫主（Vyaya's Lord）是否落九宫（Dharm）。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文以「Combinations for Father’s Death」立目，末句「Thus the Jyotishis may know the effects」把这组组合交由 Jyotishis 判读；原文未给上升限定。
- 原文最小意思：九宫主（Dharm's Lord）落十二宫（Vyaya）、且十二宫主（Vyaya's Lord）落九宫（Dharm）时，命主在第44年失去父亲。
- 本步骤产出事实：["九宫主落十二宫且十二宫主落九宫主第44年失去父亲判定"]
- 所需事实：["九宫主（Dharm's Lord）是否落十二宫（Vyaya）", "十二宫主（Vyaya's Lord）是否落九宫（Dharm）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落十二宫（Vyaya）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落九宫（Dharm）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的死因。", "不得把第44年之外的年份也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否落十二宫（Vyaya）、十二宫主（Vyaya's Lord）是否落九宫（Dharm）。
- 缺失即停字段：["九宫主（Dharm's Lord）是否落十二宫（Vyaya）", "十二宫主（Vyaya's Lord）是否落九宫（Dharm）"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v13-25`｜PDF [37]｜“The native in his 44<sup>th</sup> year will lose his father, if Dharm’s Lord is in Vyaya, as Vyaya’s Lord is in Dharm.”


## 四路查书计划

### 支持路

- The native in his 44<sup>th</sup> year will lose his father, if Dharm’s Lord is in Vyaya, as Vyaya’s Lord is in Dharm.
- 九宫主落十二宫 十二宫主落九宫 第44年 失去父亲

### 反例或取消路

- Long-living Father. Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life
- If Dharm’s Lord is an angle and receives a Drishti from Guru, the native’s father will be a king endowed with conveyances, or be equal to a king

### 适用边界路

- If Dharm’s Lord is in its debilitation Rāśi, while his dispositor is in Dharm Bhava, the native will lose his father at the age of 26, or 30
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

### 判断方法路

- Dharm Bhava and the 9<sup>th</sup> from Surya deal with one’s father
- 判断失去父亲的年岁要看九宫主（Dharm's Lord）与十二宫主（Vyaya's Lord）的互落

## 上游问题

- 无

## 停止条件

- 缺少九宫主（Dharm's Lord）落宫事实时停止。
- 缺少十二宫主（Vyaya's Lord）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
