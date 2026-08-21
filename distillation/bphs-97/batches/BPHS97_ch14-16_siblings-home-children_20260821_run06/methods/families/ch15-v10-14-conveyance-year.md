---
method: ch15-v10-14-conveyance-year
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 得车乘的年份：第12年、第32年与第42年的四组条件

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我什么时候能买车
- 我哪一年会有代步工具

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn’s Lord）是否为吉星
- 金星（Shukr）是否落十二宫（Vyaya Bhava）
- 太阳（Surya）是否落四宫（Bandhu Bhava）
- 四宫主（Bandhu’s Lord）是否入旺
- 四宫主（Bandhu’s Lord）是否与金星（Shukr）同处
- 四宫主（Bandhu’s Lord）是否与十宫主（Karm’s Lord）会合
- 四宫主与十宫主的会合处是否为四宫主的入旺 Navāńś
- 十一宫主（Labh’s Lord）与四宫主（Bandhu’s Lord）是否互换宫位

## 按情况检查的事实

- 四宫主（Bandhu’s Lord）是否落陷
- 四宫主（Bandhu’s Lord）是否落十一宫（Labh Bhava）

## 依赖方法

- 无

## 执行步骤

### ch15-v10-14-conveyance-year.step-001

- 动作：核对上升主是否为吉星、金星是否落十二宫，并核对四宫主是落陷还是落十一宫。
- 适用范围：仅限原文这一组条件与第 12 年得车乘的断语；原文未说明其他年份。
- 原文最小意思：上升主（Lagn’s Lord）为吉星、四宫主（Bandhu’s Lord）落陷或落十一宫（Labh Bhava）、且指示星金星（Shukr）落十二宫（Vyaya Bhava）时，命主在其第 12 年得到车乘。
- 本步骤产出事实：["第12年得车乘判定（上升主为吉星的组合）"]
- 所需事实：["上升主（Lagn’s Lord）是否为吉星", "金星（Shukr）是否落十二宫（Vyaya Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn’s Lord）是否为吉星"}, {"fact_key": "金星（Shukr）是否落十二宫（Vyaya Bhava）"}]}, {"operator": "OR", "operands": [{"fact_key": "四宫主（Bandhu’s Lord）是否落陷"}, {"fact_key": "四宫主（Bandhu’s Lord）是否落十一宫（Labh Bhava）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn’s Lord）是否为吉星"}, {"fact_key": "金星（Shukr）是否落十二宫（Vyaya Bhava）"}]}, "required_fact_keys": ["四宫主（Bandhu’s Lord）是否落陷"], "branch_condition_logic": {"fact_key": "四宫主（Bandhu’s Lord）是否落陷"}, "selection_group": "ch15-v10-14-conveyance-year.step-001:bandhu-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫主（Bandhu’s Lord）是否落陷。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn’s Lord）是否为吉星"}, {"fact_key": "金星（Shukr）是否落十二宫（Vyaya Bhava）"}]}, "required_fact_keys": ["四宫主（Bandhu’s Lord）是否落十一宫（Labh Bhava）"], "branch_condition_logic": {"fact_key": "四宫主（Bandhu’s Lord）是否落十一宫（Labh Bhava）"}, "selection_group": "ch15-v10-14-conveyance-year.step-001:bandhu-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫主（Bandhu’s Lord）是否落十一宫（Labh Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把第 12 年改写成任何其他年份或大运时段。", "不得据此推断车辆种类、数量或价格。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn’s Lord）是否为吉星、金星（Shukr）是否落十二宫（Vyaya Bhava）。
- 缺失即停字段：["上升主（Lagn’s Lord）是否为吉星", "金星（Shukr）是否落十二宫（Vyaya Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v10-14`｜PDF [30]｜“If Lagn’s Lord is a benefic, while Bandhu’s Lord is in fall, or in Labh Bhava and the significator (Shukr) is in Vyaya Bhava, the native will obtain conveyances in his 12<sup>th</sup> year.”

### ch15-v10-14-conveyance-year.step-002

- 动作：核对太阳是否落四宫、四宫主是否入旺并与金星同处，判断第 32 年是否得车乘。
- 适用范围：仅限原文这一组条件与第 32 年得车乘的断语；原文未说明其他年份。
- 原文最小意思：太阳（Surya）落四宫（Bandhu Bhava）、四宫主（Bandhu’s Lord）入旺并与金星（Shukr）同处时，命主在其第 32 年获得车乘。
- 本步骤产出事实：["第32年得车乘判定"]
- 所需事实：["太阳（Surya）是否落四宫（Bandhu Bhava）", "四宫主（Bandhu’s Lord）是否入旺", "四宫主（Bandhu’s Lord）是否与金星（Shukr）同处"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落四宫（Bandhu Bhava）"}, {"fact_key": "四宫主（Bandhu’s Lord）是否入旺"}, {"fact_key": "四宫主（Bandhu’s Lord）是否与金星（Shukr）同处"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把第 32 年改写成任何其他年份或大运时段。", "不得把这一组条件与第 12 年那一组混用。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落四宫（Bandhu Bhava）、四宫主（Bandhu’s Lord）是否入旺、四宫主（Bandhu’s Lord）是否与金星（Shukr）同处。
- 缺失即停字段：["太阳（Surya）是否落四宫（Bandhu Bhava）", "四宫主（Bandhu’s Lord）是否入旺", "四宫主（Bandhu’s Lord）是否与金星（Shukr）同处"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v10-14`｜PDF [30]｜“Should Surya be in Bandhu Bhava, as Bandhu’s Lord is exalted and be with Shukr, one will acquire conveyances in his 32<sup>nd</sup> year.”

### ch15-v10-14-conveyance-year.step-003

- 动作：核对四宫主是否与十宫主会合于四宫主的入旺 Navāńś，判断第 42 年是否得车乘。
- 适用范围：仅限原文这一组条件与第 42 年得车乘的断语；原文未说明其他年份。
- 原文最小意思：四宫主（Bandhu’s Lord）与十宫主（Karm’s Lord）会合于四宫主的入旺 Navāńś 时，命主在其第 42 年得享车乘。
- 本步骤产出事实：["第42年得车乘判定"]
- 所需事实：["四宫主（Bandhu’s Lord）是否与十宫主（Karm’s Lord）会合", "四宫主与十宫主的会合处是否为四宫主的入旺 Navāńś"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "四宫主（Bandhu’s Lord）是否与十宫主（Karm’s Lord）会合"}, {"fact_key": "四宫主与十宫主的会合处是否为四宫主的入旺 Navāńś"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把入旺 Navāńś 换成入旺星座或其他分盘。", "不得把第 42 年改写成任何其他年份或大运时段。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：四宫主（Bandhu’s Lord）是否与十宫主（Karm’s Lord）会合、四宫主与十宫主的会合处是否为四宫主的入旺 Navāńś。
- 缺失即停字段：["四宫主（Bandhu’s Lord）是否与十宫主（Karm’s Lord）会合", "四宫主与十宫主的会合处是否为四宫主的入旺 Navāńś"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v10-14`｜PDF [30]｜“It will be in the 42<sup>nd</sup> year, that one will be endowed with conveyances, if Bandhu’s Lord joins Karm’s Lord in his (4<sup>th</sup> Lord’s) exaltation Navāńś.”

### ch15-v10-14-conveyance-year.step-004

- 动作：核对十一宫主与四宫主是否互换宫位，判断第 12 年是否得车乘。
- 适用范围：仅限十一宫主与四宫主互换这一条件与第 12 年得车乘的断语；原文未说明其他年份。
- 原文最小意思：十一宫主与四宫主（Labh’s and Bandhu’s Lords）互换宫位时，命主在第 12 年得到车乘。
- 本步骤产出事实：["第12年得车乘判定（十一宫主与四宫主互换）"]
- 所需事实：["十一宫主（Labh’s Lord）与四宫主（Bandhu’s Lord）是否互换宫位"]
- 条件关系：{"fact_key": "十一宫主（Labh’s Lord）与四宫主（Bandhu’s Lord）是否互换宫位"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把互换扩展成同宫、相照等其他关系。", "不得把第 12 年改写成任何其他年份或大运时段。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十一宫主（Labh’s Lord）与四宫主（Bandhu’s Lord）是否互换宫位。
- 缺失即停字段：["十一宫主（Labh’s Lord）与四宫主（Bandhu’s Lord）是否互换宫位"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v10-14`｜PDF [30]｜“An exchange between Labh’s and Bandhu’s Lords will confer conveyances in the 12<sup>th</sup> year.”


## 四路查书计划

### 支持路

- 第12年 第32年 第42年 得车乘 四宫主

### 反例或取消路

- 四宫受凶星 车辆损失 事故

### 适用边界路

- 原文给的年份是否只对应该组条件

### 判断方法路

- 判断得车乘年份要查什么条件

## 上游问题

- 无

## 停止条件

- 缺少上升主吉凶属性或金星落宫事实时停止。
- 缺少四宫主的落宫、旺弱或互换事实时停止。
- 条件组不完整时不得给出年份结论。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
