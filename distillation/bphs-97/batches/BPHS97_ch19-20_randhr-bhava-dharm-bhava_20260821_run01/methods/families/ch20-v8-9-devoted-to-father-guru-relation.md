---
method: ch20-v8-9-devoted-to-father-guru-relation
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 孝敬父亲：太阳落三角宫、九宫主落七宫并与木星同宫或受木星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会孝顺父亲
- 九宫主落七宫又与木星有关系说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否落三角宫
- 九宫主（Dharm's Lord）是否落七宫（Yuvati）

## 按情况检查的事实

- 九宫主（Dharm's Lord）是否与木星（Guru）同宫
- 九宫主（Dharm's Lord）是否被木星（Guru）相照

## 依赖方法

- 无

## 执行步骤

### ch20-v8-9-devoted-to-father-guru-relation.step-001

- 动作：核对太阳（Surya）是否落上升起算的三角宫、九宫主（Dharm's Lord）是否落七宫（Yuvati），再看九宫主与木星（Guru）是同宫还是被其相照。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文断语是「the native will be devoted to his father」，his 指命主；原文未给时间限定。
- 原文最小意思：太阳（Surya）落上升（Lagna）起算的三角宫、九宫主（Dharm's Lord）落七宫（Yuvati）、且与木星（Guru）同宫，或被木星（Guru）相照时，命主孝敬他的父亲。
- 本步骤产出事实：["太阳落三角宫且九宫主落七宫会木星主孝敬父亲判定"]
- 所需事实：["太阳（Surya）是否落三角宫", "九宫主（Dharm's Lord）是否落七宫（Yuvati）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落三角宫"}, {"fact_key": "九宫主（Dharm's Lord）是否落七宫（Yuvati）"}]}, {"operator": "OR", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否与木星（Guru）同宫"}, {"fact_key": "九宫主（Dharm's Lord）是否被木星（Guru）相照"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落三角宫"}, {"fact_key": "九宫主（Dharm's Lord）是否落七宫（Yuvati）"}]}, "required_fact_keys": ["九宫主（Dharm's Lord）是否与木星（Guru）同宫"], "branch_condition_logic": {"fact_key": "九宫主（Dharm's Lord）是否与木星（Guru）同宫"}, "selection_group": "ch20-v8-9-devoted-to-father-guru-relation.step-001:guru-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫主（Dharm's Lord）是否与木星（Guru）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落三角宫"}, {"fact_key": "九宫主（Dharm's Lord）是否落七宫（Yuvati）"}]}, "required_fact_keys": ["九宫主（Dharm's Lord）是否被木星（Guru）相照"], "branch_condition_logic": {"fact_key": "九宫主（Dharm's Lord）是否被木星（Guru）相照"}, "selection_group": "ch20-v8-9-devoted-to-father-guru-relation.step-001:guru-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫主（Dharm's Lord）是否被木星（Guru）相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的寿命、财富或婚姻。", "不得把同宫与相照合并成一个条件，两者是原文给的两种取径。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落三角宫、九宫主（Dharm's Lord）是否落七宫（Yuvati）。
- 缺失即停字段：["太阳（Surya）是否落三角宫", "九宫主（Dharm's Lord）是否落七宫（Yuvati）"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v8-9`｜PDF [37]｜“If Surya is in a trine from Lagna, while Dharm’s Lord is in Yuvati in yuti with, or receiving a Drishti from Guru, the native will be devoted to his father.”


## 四路查书计划

### 支持路

- If Surya is in a trine from Lagna, while Dharm’s Lord is in Yuvati in yuti with, or receiving a Drishti from Guru, the native will be devoted to his father.
- 太阳落三角宫 九宫主落七宫 与木星同宫 被木星相照 孝敬父亲

### 反例或取消路

- There will be mutual enmity between the father and the native, if Lagn’s Lord is in Dharm Bhava, but with the Lord of Ari
- If Sahaj’s Lord is in Vyaya, the native will spend on evil deeds, will have a wicked father

### 适用边界路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

### 判断方法路

- Dharm Bhava and the 9<sup>th</sup> from Surya deal with one’s father
- 判断父子关系要看太阳（Surya）、九宫主（Dharm's Lord）与木星（Guru）的哪些关系

## 上游问题

- 无

## 停止条件

- 缺少太阳（Surya）是否落三角宫的事实时停止。
- 缺少九宫主（Dharm's Lord）落宫事实时停止。
- 同宫与相照两个分支事实都缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
