---
method: ch17-v23-water-danger-putr-dharm-years
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Putr 年与 Dharm 年的水厄：太阳落六宫或八宫、月亮落太阳起第十二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有落水的危险
- 哪些年份要防水

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘太阳（Surya）落在哪一宫
- 月亮（Chandra）是否落太阳（Surya）起第十二宫（Vyaya）

## 按情况检查的事实

- 太阳（Surya）是否落六宫（Ari）
- 太阳（Surya）是否落八宫（Randhr）

## 依赖方法

- 无

## 执行步骤

### ch17-v23-water-danger-putr-dharm-years.step-001

- 动作：核对太阳落宫，以及月亮是否落自太阳起算的第十二宫。
- 适用范围：仅限本命盘水厄主题；原文以 Putr 年、Dharm 年称呼年份，未换算成具体年岁。
- 原文最小意思：太阳落六宫或八宫、月亮落太阳起第十二宫时，Putr 年与 Dharm 年要防水厄。
- 本步骤产出事实：["Putr 年与 Dharm 年水厄判定"]
- 所需事实：["本盘太阳（Surya）落在哪一宫", "月亮（Chandra）是否落太阳（Surya）起第十二宫（Vyaya）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）落在哪一宫"}, {"fact_key": "月亮（Chandra）是否落太阳（Surya）起第十二宫（Vyaya）"}]}, {"operator": "OR", "operands": [{"fact_key": "太阳（Surya）是否落六宫（Ari）"}, {"fact_key": "太阳（Surya）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）落在哪一宫"}, {"fact_key": "月亮（Chandra）是否落太阳（Surya）起第十二宫（Vyaya）"}]}, "required_fact_keys": ["太阳（Surya）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否落六宫（Ari）"}, "selection_group": "ch17-v23-water-danger-putr-dharm-years.step-001:surya-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）落在哪一宫"}, {"fact_key": "月亮（Chandra）是否落太阳（Surya）起第十二宫（Vyaya）"}]}, "required_fact_keys": ["太阳（Surya）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否落八宫（Randhr）"}, "selection_group": "ch17-v23-water-danger-putr-dharm-years.step-001:surya-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 Putr 年、Dharm 年自行换算成本条没写出的年岁。", "不得据此推断落水的地点或致死与否。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘太阳（Surya）落在哪一宫、月亮（Chandra）是否落太阳（Surya）起第十二宫（Vyaya）。
- 缺失即停字段：["本盘太阳（Surya）落在哪一宫", "月亮（Chandra）是否落太阳（Surya）起第十二宫（Vyaya）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v23-25`｜PDF [33]｜“Danger through water will have to be feared during Putr and Dharm years, if Surya is in Ari, or Randhr, while Chandra is in Vyaya from the said Surya.”


## 四路查书计划

### 支持路

- Danger through water will have to be feared during Putr and Dharm years, if Surya is in Ari, or Randhr
- 太阳落六宫 八宫 月亮太阳起第十二宫 水厄

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed
- Guru in similar case will destroy any disease

### 适用边界路

- Chandra in Yuti with the Lords of Ari and Randhr Bhava dangers through water
- Evils, causing premature end, exist up to the 24th year of one’s age

### 判断方法路

- Indications of Ari Bhava doubts about death
- 判断水厄年份应从哪颗星起算宫位

## 上游问题

- 无

## 停止条件

- 缺少太阳落宫事实时停止。
- 缺少月亮相对太阳落宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
