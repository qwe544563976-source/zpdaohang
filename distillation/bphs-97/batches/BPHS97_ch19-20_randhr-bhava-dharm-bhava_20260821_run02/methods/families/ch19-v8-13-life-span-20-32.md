---
method: ch19-v8-13-life-span-20-32
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 寿数20至32岁：上升主力量微弱而八宫主落角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的寿数大概在什么区间
- 上升主弱八宫主落角宫会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否有力
- 八宫主（Randhr's Lord）是否落角宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch19-v8-13-life-span-20-32.step-001

- 动作：核对上升主（Lagn's Lord）的强弱与八宫主（Randhr's Lord）是否落角宫，判断寿数区间。
- 适用范围：仅限本命盘寿命主题；「力量微弱」按原文 weak 接线，用「上升主是否有力」的否定表示，强弱判准原文本句未给（待排盘窗口定义）；原文只给20至32岁这个区间。
- 原文最小意思：上升主力量微弱、而八宫主落角宫时，寿数在20岁至32岁之间。
- 本步骤产出事实：["上升主微弱八宫主落角宫的寿数区间判定"]
- 所需事实：["上升主（Lagn's Lord）是否有力", "八宫主（Randhr's Lord）是否落角宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "上升主（Lagn's Lord）是否有力"}]}, {"fact_key": "八宫主（Randhr's Lord）是否落角宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把20至32岁的区间收窄成某一个具体年岁。", "不得自行发明「有力」的判准。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否有力、八宫主（Randhr's Lord）是否落角宫。
- 缺失即停字段：["上升主（Lagn's Lord）是否有力", "八宫主（Randhr's Lord）是否落角宫"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v8-13`｜PDF [36]｜“One’s span of life will be between 20 and 32 years, if Lagn’s Lord is weak, while Randhr’s Lord is an angle.”


## 四路查书计划

### 支持路

- One’s span of life will be between 20 and 32 years, if Lagn’s Lord is weak, while Randhr’s Lord is an angle
- 上升主无力 八宫主落角宫 寿数20到32岁

### 反例或取消路

- If Randhr’s Lord is in an angle, long life is indicated
- If Lagn’s Lord is exceedingly strong and receives a Drishti from a benefic, which is placed in an angle, the person concerned will be wealthy, virtuous and long-lived
- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- The life-span in Bal Risht is 8 years, in Yog Risht 20 years, in short, medium and long lives, respectively, 32, 64 and 120 years
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- The strength and weakness of the Grahas concerned be estimated in deciding longevity
- 上升主的强弱怎么判定

## 上游问题

- 无

## 停止条件

- 缺少上升主强弱事实时停止（该判准待排盘窗口定义）。
- 缺少八宫主落角宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
