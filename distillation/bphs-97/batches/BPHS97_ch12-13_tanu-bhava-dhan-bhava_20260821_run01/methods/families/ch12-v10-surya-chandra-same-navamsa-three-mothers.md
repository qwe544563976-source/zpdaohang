---
method: ch12-v10-surya-chandra-same-navamsa-three-mothers
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 由三位母亲抚养：太阳与月亮同宫并落同一九分盘

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我小时候是谁带大的
- 太阳月亮同宫又同九分盘代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否与月亮（Chandra）同宫
- 太阳（Surya）与月亮（Chandra）是否落在同一个九分盘（Navamsa D9）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch12-v10-surya-chandra-same-navamsa-three-mothers.step-001

- 动作：核对太阳与月亮是否落在同一宫，并核对两者是否落在同一个九分盘。
- 适用范围：仅限本命盘出生后养育情形主题；括号内对 Bhratri 的解释是英译者注，其结论强度不与作者自断等同。
- 原文最小意思：太阳（Surya）与月亮（Chandra）同落一宫，并落在同一个九分盘（Navāńś）时，命主在出生后头三个月由三位不同的母亲抚养，之后由父亲和兄弟养大；英译者注把 Bhratri 解为泛指近亲。
- 本步骤产出事实：["日月同宫同九分盘的养育判定"]
- 所需事实：["太阳（Surya）是否与月亮（Chandra）同宫", "太阳（Surya）与月亮（Chandra）是否落在同一个九分盘（Navamsa D9）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否与月亮（Chandra）同宫"}, {"fact_key": "太阳（Surya）与月亮（Chandra）是否落在同一个九分盘（Navamsa D9）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断生母的存亡或去向，原文只说由三位不同的母亲抚养。", "不得把英译者对 Bhratri 的解释当成作者自断的独立断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否与月亮（Chandra）同宫、太阳（Surya）与月亮（Chandra）是否落在同一个九分盘（Navamsa D9）。
- 缺失即停字段：["太阳（Surya）是否与月亮（Chandra）同宫", "太阳（Surya）与月亮（Chandra）是否落在同一个九分盘（Navamsa D9）"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v10`｜PDF [27]｜“If Surya and Chandra join in one and the same Bhava and fall in one Navāńś, the native will be nurtured by three different mothers for the first three months from its birth and will later on be brought up by its father and brother.”
  - `bphs-97:santhanam:ch12:v10`｜PDF [27]｜“‘Bhratri’ apart from meaning a brother calls for interpretation, as a near relative in general”


## 四路查书计划

### 支持路

- If Surya and Chandra join in one and the same Bhava and fall in one Navāńś, the native will be nurtured by three different mothers for the first three months from its birth
- 太阳月亮同宫同九分盘 三位母亲抚养

### 反例或取消路

- Should a malefic be in the 4th, identical with an inimical Rāśi, counted from Chandra, while there is no benefic in a Kendra, the child will lose its mother in a premature manner

### 适用边界路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- The Navāńś calculation are for a Movable Rashifrom there itself, for a Fixed Rashifrom the 9th thereof and for a Dual Rashifrom the 5th thereof
- The Sixteen Divisions of a Rāśi

### 判断方法路

- Whatever results are to be known from Bandhu, Tanu, Dhan, Labh and Dharm should also be known from the 4th of Chandra, from Kark Rashiitself and from the 2nd, 11th and 9th from Chandra, respectively
- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- 判断养育情形要看太阳与月亮的同宫和九分盘

## 上游问题

- 无

## 停止条件

- 缺少太阳月亮同宫事实时停止。
- 缺少太阳月亮同九分盘事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
