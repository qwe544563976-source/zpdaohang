---
method: ch23-v8-visible-half-explicit-results
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 结果显于外：行星落在黄道的可见半

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 这颗星的作用会不会明摆着看得见
- 我盘里的行星是明着起作用还是暗着起作用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 所论行星（Graha）是否落在黄道可见半（visible half）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch23-v8-visible-half-explicit-results.step-001

- 动作：核对所论行星（Graha）是否落在黄道的可见半（visible half），落在可见半的行星给出明显的结果。
- 适用范围：本句只区分结果显与隐，不判吉凶；原文本句没有给出黄道可见半（visible half）的宫位范围界定，界定未确定即停判；原文未给时间限定。
- 原文最小意思：行星落在黄道的可见半（visible half）时，会给出明显的结果。
- 本步骤产出事实：["行星所在黄道半区的结果显隐判定"]
- 所需事实：["所论行星（Graha）是否落在黄道可见半（visible half）"]
- 条件关系：{"fact_key": "所论行星（Graha）是否落在黄道可见半（visible half）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自行把可见半认定为某几个宫位；原文本句未给界定。", "不得把「明显的结果」读成好结果或坏结果。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论行星（Graha）是否落在黄道可见半（visible half）。
- 缺失即停字段：["所论行星（Graha）是否落在黄道可见半（visible half）"]
- 原文证据：
  - `bphs-97:santhanam:ch23:v8`｜PDF [40]｜“Grahas placed in the visible half of the zodiac will give explicit results”


## 四路查书计划

### 支持路

- Grahas placed in the visible half of the zodiac will give explicit results
- 行星 黄道可见半 明显的结果

### 反例或取消路

- while the ones in the invisible half will confer secret results
- Full, half, one third, one fourth, one fifth and one sixth are the deductions of contributions, made by malefics, placed in the visible half of the zodiac

### 适用边界路

- if Lagn Lord is in the invisible half (i.e. from Lagn cusp to descendental cusp)
- Deductions for Grahas in the Visible Half of the Zodiac

### 判断方法路

- Just as these effects are derived from Tanu Bhava in regard to the native, similar deductions be made about co-borns etc. from Sahaj and other Bhavas.
- 判断行星结果显隐要先定黄道的可见半与不可见半

## 上游问题

- 无

## 停止条件

- 黄道可见半（visible half）的宫位范围界定未确定时停止。
- 缺少所论行星是否落在可见半的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
