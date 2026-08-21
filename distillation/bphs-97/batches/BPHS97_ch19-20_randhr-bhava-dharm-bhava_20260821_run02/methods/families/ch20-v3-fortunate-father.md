---
method: ch20-v3-fortunate-father
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲有福：九宫主有力、金星落九宫、木星落上升起的角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲这辈子有没有福气
- 金星落九宫对父亲有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否有力
- 金星（Shukra）是否落九宫（Dharm）
- 木星（Guru）是否落上升宫（Tanu Bhava）起算的角宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v3-fortunate-father.step-001

- 动作：核对九宫主（Dharm's Lord）是否有力、金星（Shukra）是否落九宫、木星（Guru）是否落自上升宫起算的角宫。
- 适用范围：仅限本命盘九宫（Dharm Bhava）主题下父亲的福分；原文把角宫的起算宫位写明为 Tanu Bhava；「有力」的判准原文本句未给（待排盘窗口定义）；原文未给时间限定。
- 原文最小意思：九宫主有力、金星落九宫、木星落自上升宫（Tanu Bhava）起算的角宫时，命主的父亲有福。
- 本步骤产出事实：["九宫主有力金木得位的父亲有福判定"]
- 所需事实：["九宫主（Dharm's Lord）是否有力", "金星（Shukra）是否落九宫（Dharm）", "木星（Guru）是否落上升宫（Tanu Bhava）起算的角宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否有力"}, {"fact_key": "金星（Shukra）是否落九宫（Dharm）"}, {"fact_key": "木星（Guru）是否落上升宫（Tanu Bhava）起算的角宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把角宫的起算点从上升宫换成别的宫位。", "不得据此推断父亲的财富数量或具体年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否有力、金星（Shukra）是否落九宫（Dharm）、木星（Guru）是否落上升宫（Tanu Bhava）起算的角宫。
- 缺失即停字段：["九宫主（Dharm's Lord）是否有力", "金星（Shukra）是否落九宫（Dharm）", "木星（Guru）是否落上升宫（Tanu Bhava）起算的角宫"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v3`｜PDF [36]｜“If Dharm’s Lord is with strength, as Shukra is in Dharm, while Guru is in an angle from Tanu Bhava, the native’s father is fortunate.”


## 四路查书计划

### 支持路

- If Dharm’s Lord is with strength, as Shukra is in Dharm, while Guru is in an angle from Tanu Bhava, the native’s father is fortunate
- 九宫主有力 金星落九宫 木星角宫 父亲有福

### 反例或取消路

- If Dharm’s Lord is debilitated, while the 2nd and/or the 4th from Dharm Bhava is occupied by Mangal, the native’s father is poor
- There will be mutual enmity between the father and the native, if Lagn’s Lord is in Dharm Bhava, but with the Lord of Ari

### 适用边界路

- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- these are the effects related to Dharm Bhava. I have explained briefly. These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava
- Should Dharm’s Lord be in Karm Bhava, while Karm’s Lord receives a Drishti from a benefic the native’s father will be very rich and famous
- 判断父亲的境遇要看九宫还是十宫

## 上游问题

- 无

## 停止条件

- 缺少九宫主强弱事实时停止（该判准待排盘窗口定义）。
- 缺少金星或木星落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
