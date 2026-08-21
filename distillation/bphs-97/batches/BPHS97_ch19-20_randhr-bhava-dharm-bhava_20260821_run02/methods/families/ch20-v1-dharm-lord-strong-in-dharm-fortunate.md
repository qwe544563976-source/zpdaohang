---
method: ch20-v1-dharm-lord-strong-in-dharm-fortunate
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 有福（或富足）：九宫主有力地落在九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子有没有福气
- 九宫主落九宫是什么意思

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否落九宫（Dharm）
- 九宫主（Dharm's Lord）是否有力

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v1-dharm-lord-strong-in-dharm-fortunate.step-001

- 动作：核对九宫主（Dharm's Lord）是否落九宫，并核对它是否有力。
- 适用范围：仅限本命盘九宫（Dharm Bhava）福分主题；「有福（或富足）」的括号为原文自带的并列译法，本方法照录不作取舍；「有力」的判准原文本句未给（待排盘窗口定义）；原文未给时间限定。
- 原文最小意思：九宫主落九宫且有力时，命主有福（或富足）。
- 本步骤产出事实：["九宫主有力落九宫的有福判定"]
- 所需事实：["九宫主（Dharm's Lord）是否落九宫（Dharm）", "九宫主（Dharm's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落九宫（Dharm）"}, {"fact_key": "九宫主（Dharm's Lord）是否有力"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得省去「有力」这一前提，只凭九宫主落九宫就下断语。", "不得据此推断具体财富数量或得福年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否落九宫（Dharm）、九宫主（Dharm's Lord）是否有力。
- 缺失即停字段：["九宫主（Dharm's Lord）是否落九宫（Dharm）", "九宫主（Dharm's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v1`｜PDF [36]｜“One will be fortunate (or affluent), if Dharm’s Lord is in Dharm Bhava with strength.”


## 四路查书计划

### 支持路

- One will be fortunate (or affluent), if Dharm’s Lord is in Dharm Bhava with strength
- 九宫主落九宫 有力 有福 富足

### 反例或取消路

- If Rahu is in the 9th from Dharm Bhava, as his dispositor is in Randhr Bhava and Dharm’s Lord is in fall, the native be devoid of fortunes
- If Karm’s Lord and Sahaj’s Lord are bereft of strength, while Dharm’s Lord is in fall, or combust the native will go begging for his food

### 适用边界路

- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Abundant fortunes be acquired after the 20th year, if Dharm has Guru in it, as its Lord is in an angle from Lagn

### 判断方法路

- these are the effects related to Dharm Bhava. I have explained briefly. These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava
- Effects of Dharm’s Lord in Various Bhavas
- 判断福分要看九宫主的什么状态

## 上游问题

- 无

## 停止条件

- 缺少九宫主落宫事实时停止。
- 缺少九宫主强弱事实时停止（该判准待排盘窗口定义）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
