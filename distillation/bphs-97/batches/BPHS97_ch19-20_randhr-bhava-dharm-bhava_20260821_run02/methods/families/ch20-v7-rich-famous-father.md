---
method: ch20-v7-rich-famous-father
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲富有且有名望：九宫主落十宫、十宫主受吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲的家境和名声怎么样
- 九宫主落十宫说明父亲什么状况

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否落十宫（Karm）
- 十宫主（Karm's Lord）是否被吉星相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v7-rich-famous-father.step-001

- 动作：核对九宫主（Dharm's Lord）是否落十宫（Karm），并核对十宫主（Karm's Lord）是否受吉星相照。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文未给时间或上升限定；吉星名册须按本书自己的吉凶星定义取得。
- 原文最小意思：九宫主（Dharm's Lord）落十宫（Karm）、且十宫主（Karm's Lord）受吉星相照时，命主的父亲非常富有且有名望。
- 本步骤产出事实：["九宫主落十宫且十宫主受吉星相照主父亲富有闻名判定"]
- 所需事实：["九宫主（Dharm's Lord）是否落十宫（Karm）", "十宫主（Karm's Lord）是否被吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落十宫（Karm）"}, {"fact_key": "十宫主（Karm's Lord）是否被吉星相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的财富数额、职业或成名途径。", "不得把富有与名望的断语从父亲移到命主本人。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否落十宫（Karm）、十宫主（Karm's Lord）是否被吉星相照。
- 缺失即停字段：["九宫主（Dharm's Lord）是否落十宫（Karm）", "十宫主（Karm's Lord）是否被吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v7`｜PDF [37]｜“Should Dharm’s Lord be in Karm Bhava, while Karm’s Lord receives a Drishti from a benefic the native’s father will be very rich and famous.”


## 四路查书计划

### 支持路

- Should Dharm’s Lord be in Karm Bhava, while Karm’s Lord receives a Drishti from a benefic the native’s father will be very rich and famous.
- 九宫主落十宫 十宫主受吉星相照 父亲富有 有名望

### 反例或取消路

- Indigent Father. If Dharm’s Lord is debilitated, while the 2<sup>nd</sup> and/or the 4<sup>th</sup> from Dharm Bhava is occupied by Mangal, the native’s father is poor
- Malefics in Ari and Vyaya Bhava will bring evils to mother. The child’s father will receive similar effects, if Bandhu and Karm Bhava are captured by malefics

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava
- Fortunate (Affluent) Father. If Dharm’s Lord is with strength, as Shukra is in Dharm, while Guru is in an angle from Tanu Bhava, the native’s father is fortunate

### 判断方法路

- Dharm Bhava and the 9<sup>th</sup> from Surya deal with one’s father
- 判断父亲的财富与名望要看九宫（Dharm）与十宫（Karm）的哪些配置

## 上游问题

- 无

## 停止条件

- 缺少九宫主（Dharm's Lord）落宫事实时停止。
- 缺少十宫主（Karm's Lord）是否被吉星相照的事实时停止。
- 本盘吉星名册未按本书吉凶星定义确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
