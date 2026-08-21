---
method: ch19-v14-15-lagn-lord-exalted-long-life
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 长寿：上升主入旺、月亮落十一宫、木星落八宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 上升主入旺我会不会长寿
- 月亮落十一宫木星落八宫是什么格局

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否入旺
- 月亮（Chandra）是否落十一宫（Labh）
- 木星（Guru）是否落八宫（Randhr）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch19-v14-15-lagn-lord-exalted-long-life.step-001

- 动作：核对上升主（Lagn's Lord）是否入旺，并核对月亮（Chandra）落十一宫、木星（Guru）落八宫。
- 适用范围：仅限本命盘寿命主题；原文 respectively 指月亮落十一宫、木星落八宫，本方法按此对应接线；原文未给时间限定。
- 原文最小意思：上升主入旺、月亮落十一宫、木星落八宫时，命主长寿。
- 本步骤产出事实：["上升主入旺月木分落的长寿判定"]
- 所需事实：["上升主（Lagn's Lord）是否入旺", "月亮（Chandra）是否落十一宫（Labh）", "木星（Guru）是否落八宫（Randhr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否入旺"}, {"fact_key": "月亮（Chandra）是否落十一宫（Labh）"}, {"fact_key": "木星（Guru）是否落八宫（Randhr）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把月亮与木星的落宫对调——原文写明 respectively。", "不得据此推出具体寿数年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否入旺、月亮（Chandra）是否落十一宫（Labh）、木星（Guru）是否落八宫（Randhr）。
- 缺失即停字段：["上升主（Lagn's Lord）是否入旺", "月亮（Chandra）是否落十一宫（Labh）", "木星（Guru）是否落八宫（Randhr）"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v14-15`｜PDF [36]｜“One will be long-lived, if Lagn’s Lord is in exaltation, while Chandra and Guru are, respectively, in Labh and Randhr Bhava.”


## 四路查书计划

### 支持路

- One will be long-lived, if Lagn’s Lord is in exaltation, while Chandra and Guru are, respectively, in Labh and Randhr Bhava
- 上升主入旺 月亮十一宫 木星八宫 长寿

### 反例或取消路

- One’s span of life will be between 20 and 32 years, if Lagn’s Lord is weak, while Randhr’s Lord is an angle
- Should Randhr’s Lord join Lagn’s Lord, or a malefic and be in Randhr itself, the native will be short lived

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- The life-span in Bal Risht is 8 years, in Yog Risht 20 years, in short, medium and long lives, respectively, 32, 64 and 120 years
- If Guru is in Lagna, or in Yuvati Bhava and receives a Drishti from, or is yuti with only benefics, the class of longevity will increase

### 判断方法路

- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- The strength and weakness of the Grahas concerned be estimated in deciding longevity
- 上升主入旺在寿命判断里怎么用

## 上游问题

- 无

## 停止条件

- 缺少上升主入旺事实时停止。
- 缺少月亮或木星落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
