---
method: ch20-v2-guru-in-dharm-extremely-fortunate
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 极为有福：木星落九宫、九宫主落角宫、上升主有力

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 木星落九宫是不是很有福
- 什么组合算极为有福

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否落九宫（Dharm）
- 九宫主（Dharm's Lord）是否落角宫
- 上升主（Lagn's Lord）是否有力

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v2-guru-in-dharm-extremely-fortunate.step-001

- 动作：核对木星（Guru）是否落九宫、九宫主（Dharm's Lord）是否落角宫、上升主（Lagn's Lord）是否有力。
- 适用范围：仅限本命盘九宫（Dharm Bhava）福分主题；「有力」的判准原文本句未给（待排盘窗口定义）；原文未给时间限定。
- 原文最小意思：木星落九宫、九宫主落角宫、上升主有力时，命主极为有福。
- 本步骤产出事实：["木星落九宫三条件的极为有福判定"]
- 所需事实：["木星（Guru）是否落九宫（Dharm）", "九宫主（Dharm's Lord）是否落角宫", "上升主（Lagn's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落九宫（Dharm）"}, {"fact_key": "九宫主（Dharm's Lord）是否落角宫"}, {"fact_key": "上升主（Lagn's Lord）是否有力"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得只凭木星落九宫一项就下断语。", "不得据此推断得福的具体年份或财富数量。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落九宫（Dharm）、九宫主（Dharm's Lord）是否落角宫、上升主（Lagn's Lord）是否有力。
- 缺失即停字段：["木星（Guru）是否落九宫（Dharm）", "九宫主（Dharm's Lord）是否落角宫", "上升主（Lagn's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v2`｜PDF [36]｜“Should Guru be in Dharm Bhava, while Dharm’s Lord is in an angle and Lagn’s Lord is endowed with strength, one will be extremely fortunate.”


## 四路查书计划

### 支持路

- Should Guru be in Dharm Bhava, while Dharm’s Lord is in an angle and Lagn’s Lord is endowed with strength, one will be extremely fortunate
- 木星落九宫 九宫主落角宫 上升主有力 极为有福

### 反例或取消路

- If Rahu is in the 9th from Dharm Bhava, as his dispositor is in Randhr Bhava and Dharm’s Lord is in fall, the native be devoid of fortunes
- Should Shani be in Dharm Bhava along with Chandra, as Lagn’s Lord is in fall, the native will acquire food by begging

### 适用边界路

- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Abundant fortunes be acquired after the 20th year, if Dharm has Guru in it, as its Lord is in an angle from Lagn

### 判断方法路

- these are the effects related to Dharm Bhava. I have explained briefly. These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava
- Effects of Dharm’s Lord in Various Bhavas
- 九宫的福分要看木星与上升主吗

## 上游问题

- 无

## 停止条件

- 缺少木星或九宫主落宫事实时停止。
- 缺少上升主强弱事实时停止（该判准待排盘窗口定义）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
