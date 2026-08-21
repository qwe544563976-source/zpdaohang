---
method: ch19-v8-13-randhr-lord-in-fall-short-life
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 短寿：八宫主落陷、八宫有凶星、上升宫缺乏力量

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 八宫主落陷会不会短寿
- 上升宫没有力量对寿命有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫主（Randhr's Lord）是否落陷
- 八宫（Randhr）是否被凶星占据
- 上升宫（Tanu Bhava）是否有力

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch19-v8-13-randhr-lord-in-fall-short-life.step-001

- 动作：核对八宫主（Randhr's Lord）是否落陷、八宫内是否有凶星、上升宫（Tanu Bhava）是否缺乏力量。
- 适用范围：仅限本命盘寿命主题；「缺乏力量」按原文 bereft of strength 接线，用「上升宫是否有力」的否定表示，判准原文本句未给（待排盘窗口定义）；原文未给具体寿数。
- 原文最小意思：八宫主落陷、八宫内有凶星、上升宫缺乏力量时，命主只会短寿。
- 本步骤产出事实：["八宫主落陷三条件的短寿判定"]
- 所需事实：["八宫主（Randhr's Lord）是否落陷", "八宫（Randhr）是否被凶星占据", "上升宫（Tanu Bhava）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落陷"}, {"fact_key": "八宫（Randhr）是否被凶星占据"}, {"operator": "NOT", "operands": [{"fact_key": "上升宫（Tanu Bhava）是否有力"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推出具体寿数年岁或死亡时间。", "不得自行发明宫位「有力」的判准。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否落陷、八宫（Randhr）是否被凶星占据、上升宫（Tanu Bhava）是否有力。
- 缺失即停字段：["八宫主（Randhr's Lord）是否落陷", "八宫（Randhr）是否被凶星占据", "上升宫（Tanu Bhava）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v8-13`｜PDF [36]｜“The native will only be short-lived, if Randhr’s Lord is in fall, while Randhr Bhava has a malefic in it and Tanu Bhava is bereft of strength.”


## 四路查书计划

### 支持路

- The native will only be short-lived, if Randhr’s Lord is in fall, while Randhr Bhava has a malefic in it and Tanu Bhava is bereft of strength
- 八宫主落陷 八宫有凶星 上升宫无力 短寿

### 反例或取消路

- If Randhr’s Lord is in an angle, long life is indicated
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed
- If a Kendr contains a benefic, while Lagn’s Lord is yuti with, or receives a Drishti from a benefic, or Guru in particular, the native will live a full span of life

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- The strength and weakness of the Grahas concerned be estimated in deciding longevity
- 八宫落陷与上升宫力量怎么一起看

## 上游问题

- 无

## 停止条件

- 缺少八宫主落陷事实时停止。
- 缺少八宫凶星占据事实时停止。
- 缺少上升宫强弱事实时停止（该判准待排盘窗口定义）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
