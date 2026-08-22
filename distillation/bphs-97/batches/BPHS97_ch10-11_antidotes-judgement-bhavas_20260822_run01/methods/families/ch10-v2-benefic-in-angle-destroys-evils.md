---
method: ch10-v2-benefic-in-angle-destroys-evils
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 消解凶恶：水星、木星、金星之一落自上升起算的角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我盘里的凶象有没有被化解
- 吉星落角宫能不能消灾

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升（Lagn）落在哪个星座

## 按情况检查的事实

- 水星（Budh）是否落角宫
- 木星（Guru）是否落角宫
- 金星（Shukra）是否落角宫

## 依赖方法

- 无

## 执行步骤

### ch10-v2-benefic-in-angle-destroys-evils.step-001

- 动作：核对水星（Budh）、木星（Guru）、金星（Shukra）中是否有一颗落在自上升（Lagna）起算的角宫。
- 适用范围：仅限第 10 章消解凶恶（Antidotes for Evils）主题；原文只说三曜之一落角宫，未指定是哪一个角宫，也未给时间限定。
- 原文最小意思：水星（Budh）、木星（Guru）、金星（Shukra）三者之一落自上升（Lagna）起算的角宫时，一切凶恶被摧毁。
- 本步骤产出事实：["吉曜落角宫消解凶恶判定"]
- 所需事实：["本盘上升（Lagn）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）落在哪个星座"}, {"operator": "OR", "operands": [{"fact_key": "水星（Budh）是否落角宫"}, {"fact_key": "木星（Guru）是否落角宫"}, {"fact_key": "金星（Shukra）是否落角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升（Lagn）落在哪个星座"}, "required_fact_keys": ["水星（Budh）是否落角宫"], "branch_condition_logic": {"fact_key": "水星（Budh）是否落角宫"}, "selection_group": "ch10-v2-benefic-in-angle-destroys-evils.step-001:benefic-in-angle", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落角宫。"}, {"when": {"fact_key": "本盘上升（Lagn）落在哪个星座"}, "required_fact_keys": ["木星（Guru）是否落角宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落角宫"}, "selection_group": "ch10-v2-benefic-in-angle-destroys-evils.step-001:benefic-in-angle", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落角宫。"}, {"when": {"fact_key": "本盘上升（Lagn）落在哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落角宫"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落角宫"}, "selection_group": "ch10-v2-benefic-in-angle-destroys-evils.step-001:benefic-in-angle", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「一切凶恶被摧毁」缩小或扩大成某一类具体凶恶、某个具体宫位的吉凶。", "不得把这三颗行星扩大成其他行星落角宫也同样消解凶恶。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagn）落在哪个星座。
- 缺失即停字段：["本盘上升（Lagn）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch10:v2`｜PDF [25]｜“Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed”


## 四路查书计划

### 支持路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed
- 水星木星金星之一落角宫 一切凶恶被摧毁

### 反例或取消路

- Malefic in Vyaya and Ari Bhava, or in Randhr and Dhan Bhava, while Lagn is hemmed between other malefics, will bring early death
- Should Shani, Surya and Mangal be in Vyaya, Dharm and Randhr Bhava without Drishti from a benefic, the child will face instant death

### 适用边界路

- O Brahmin, first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas
- 凶恶与消解因素要先从上升看起

### 判断方法路

- I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 怎样判断盘中的凶恶是否被消解

## 上游问题

- 无

## 停止条件

- 缺少本盘上升星座事实、无法定出角宫时停止。
- 三颗行星的落角宫事实全部取不到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
