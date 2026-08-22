---
method: ch09-v40-surya-drishtied-by-shani-in-mesh-or-vrischik-navamsa-father-gone
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 太阳受土星相照且落白羊或天蝎九分盘：父亲在命主出生前已离家或已去世

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 太阳受土星照落九分盘白羊天蝎怎么断
- 父亲是不是在我出生前就不在了

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否受土星（Shani）相照

## 按情况检查的事实

- 太阳（Surya）是否落白羊（Mesh）九分盘（Navāńś D9）
- 太阳（Surya）是否落天蝎（Vrischik）九分盘（Navāńś D9）

## 依赖方法

- 无

## 执行步骤

### ch09-v40-surya-drishtied-by-shani-in-mesh-or-vrischik-navamsa-father-gone.step-001

- 动作：核对太阳是否受土星相照，并核对太阳落在哪一个九分盘星座。
- 适用范围：仅限本命盘对父亲的判断；原文给出离家与去世两种并列结果。
- 原文最小意思：太阳（Surya）受土星（Shani）相照，又落白羊（Mesh）或天蝎（Vrischik）九分盘（Navāńś D9）时，父亲在孩子出生前已舍家而去、或已经去世。
- 本步骤产出事实：["太阳受土星照落特定九分盘的父亲情形判定"]
- 所需事实：["太阳（Surya）是否受土星（Shani）相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否受土星（Shani）相照"}, {"operator": "OR", "operands": [{"fact_key": "太阳（Surya）是否落白羊（Mesh）九分盘（Navāńś D9）"}, {"fact_key": "太阳（Surya）是否落天蝎（Vrischik）九分盘（Navāńś D9）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "太阳（Surya）是否受土星（Shani）相照"}, "required_fact_keys": ["太阳（Surya）是否落白羊（Mesh）九分盘（Navāńś D9）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否落白羊（Mesh）九分盘（Navāńś D9）"}, "selection_group": "ch09-v40-surya-drishtied-by-shani-in-mesh-or-vrischik-navamsa-father-gone.step-001:surya-navamsa", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否落白羊（Mesh）九分盘（Navāńś D9）。"}, {"when": {"fact_key": "太阳（Surya）是否受土星（Shani）相照"}, "required_fact_keys": ["太阳（Surya）是否落天蝎（Vrischik）九分盘（Navāńś D9）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否落天蝎（Vrischik）九分盘（Navāńś D9）"}, "selection_group": "ch09-v40-surya-drishtied-by-shani-in-mesh-or-vrischik-navamsa-father-gone.step-001:surya-navamsa", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否落天蝎（Vrischik）九分盘（Navāńś D9）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得在『舍家而去』与『已经去世』之间替原文选定一个——原文两说并列。", "不得把九分盘（Navāńś D9）换成三分盘或十分盘。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否受土星（Shani）相照。
- 缺失即停字段：["太阳（Surya）是否受土星（Shani）相照"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v40`｜PDF [24]｜“If Surya receives a Drishti from Shani and be in Mesh, or in Vrischik Navāńś, the father would have given up the family before birth of the child, or would have passed away.”


## 四路查书计划

### 支持路

- If Surya receives a Drishti from Shani and be in Mesh, or in Vrischik Navāńś, the father would have given up the family before birth of the child, or would have passed away
- 太阳受土星照 白羊天蝎九分盘 父亲离家

### 反例或取消路

- a single, but strong Guru in Lagn will ward off all the evils
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.

### 适用边界路

- Evil to Father (up to Sloka 42)
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.

### 判断方法路

- Evils at Birth
- Navāńś. The Navāńś calculation are for a Movable Rashifrom there itself, for a Fixed Rashifrom the 9<sup>th</sup> thereof
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- 九分盘怎么起

## 上游问题

- 无

## 停止条件

- 缺少太阳所受相照事实时停止。
- 缺少太阳的九分盘（Navāńś D9）落座时停止。
- 原文并列两种结果，需要唯一结论时本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
