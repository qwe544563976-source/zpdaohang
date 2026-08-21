---
method: ch20-v6-royal-status-father
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲有王者之位：九宫主落角宫并受木星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲的社会地位会不会很高
- 九宫主受木星相照代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否落角宫
- 九宫主（Dharm's Lord）是否被木星（Guru）相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v6-royal-status-father.step-001

- 动作：核对九宫主（Dharm's Lord）是否落角宫，并核对它是否受木星（Guru）相照。
- 适用范围：仅限本命盘九宫（Dharm Bhava）主题下父亲的地位；「或与国王相当」是原文自带的并列说法，本方法照录；原文未给时间限定。
- 原文最小意思：九宫主落角宫并受木星相照时，命主的父亲会是拥有车乘的国王，或与国王相当。
- 本步骤产出事实：["九宫主落角宫受木星照的父亲王者地位判定"]
- 所需事实：["九宫主（Dharm's Lord）是否落角宫", "九宫主（Dharm's Lord）是否被木星（Guru）相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落角宫"}, {"fact_key": "九宫主（Dharm's Lord）是否被木星（Guru）相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把相照的木星换成别的吉星。", "不得据此推断父亲的具体官职、财富或年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否落角宫、九宫主（Dharm's Lord）是否被木星（Guru）相照。
- 缺失即停字段：["九宫主（Dharm's Lord）是否落角宫", "九宫主（Dharm's Lord）是否被木星（Guru）相照"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v6`｜PDF [36]｜“If Dharm’s Lord is an angle and receives a Drishti from Guru, the native’s father will be a king endowed with conveyances, or be equal to a king.”


## 四路查书计划

### 支持路

- If Dharm’s Lord is an angle and receives a Drishti from Guru, the native’s father will be a king endowed with conveyances, or be equal to a king
- 九宫主落角宫 木星相照 父亲如国王

### 反例或取消路

- If Dharm’s Lord is debilitated, while the 2nd and/or the 4th from Dharm Bhava is occupied by Mangal, the native’s father is poor
- There will be mutual enmity between the father and the native, if Lagn’s Lord is in Dharm Bhava, but with the Lord of Ari

### 适用边界路

- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines
- Effects of Dharm’s Lord in Various Bhavas

### 判断方法路

- these are the effects related to Dharm Bhava. I have explained briefly. These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava
- Should Dharm’s Lord be in Karm Bhava, while Karm’s Lord receives a Drishti from a benefic the native’s father will be very rich and famous
- 判断父亲地位要看九宫主的哪些状态

## 上游问题

- 无

## 停止条件

- 缺少九宫主落角宫事实时停止。
- 缺少九宫主受木星相照的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
