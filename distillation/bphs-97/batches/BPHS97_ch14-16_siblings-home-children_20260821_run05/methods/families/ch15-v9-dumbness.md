---
method: ch15-v9-dumbness
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 哑：四宫为动星座且四宫主与火星同处六宫或八宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的言语功能有没有问题
- 命里有没有不能说话的凶象

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 四宫（Bandhu Bhava）是否为动星座
- 四宫主是否与火星（Mangal）同处一宫

## 按情况检查的事实

- 四宫主与火星同处之宫是否为六宫（Ari）
- 四宫主与火星同处之宫是否为八宫（Randhr Bhava）

## 依赖方法

- 无

## 执行步骤

### ch15-v9-dumbness.step-001

- 动作：核对四宫是否落在动星座，并核对四宫主与火星是否同处六宫或八宫。
- 适用范围：仅限原文给出的哑这一结果；原文未给时间限定，也未给程度或治愈说明。
- 原文最小意思：四宫（Bandhu Bhava）为动星座、其宫主与火星（Mangal）同处六宫（Ari）、或同处八宫（Randhr Bhava）时，命主将为哑。
- 本步骤产出事实：["哑之凶象判定"]
- 所需事实：["四宫（Bandhu Bhava）是否为动星座", "四宫主是否与火星（Mangal）同处一宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "四宫（Bandhu Bhava）是否为动星座"}, {"fact_key": "四宫主是否与火星（Mangal）同处一宫"}]}, {"operator": "OR", "operands": [{"fact_key": "四宫主与火星同处之宫是否为六宫（Ari）"}, {"fact_key": "四宫主与火星同处之宫是否为八宫（Randhr Bhava）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "四宫（Bandhu Bhava）是否为动星座"}, {"fact_key": "四宫主是否与火星（Mangal）同处一宫"}]}, "required_fact_keys": ["四宫主与火星同处之宫是否为六宫（Ari）"], "branch_condition_logic": {"fact_key": "四宫主与火星同处之宫是否为六宫（Ari）"}, "selection_group": "ch15-v9-dumbness.step-001:conjunction-house", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫主与火星同处之宫是否为六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "四宫（Bandhu Bhava）是否为动星座"}, {"fact_key": "四宫主是否与火星（Mangal）同处一宫"}]}, "required_fact_keys": ["四宫主与火星同处之宫是否为八宫（Randhr Bhava）"], "branch_condition_logic": {"fact_key": "四宫主与火星同处之宫是否为八宫（Randhr Bhava）"}, "selection_group": "ch15-v9-dumbness.step-001:conjunction-house", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫主与火星同处之宫是否为八宫（Randhr Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这条扩展成其他言语疾病或听力问题。", "不得据此推断发生年龄或可否治愈。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：四宫（Bandhu Bhava）是否为动星座、四宫主是否与火星（Mangal）同处一宫。
- 缺失即停字段：["四宫（Bandhu Bhava）是否为动星座", "四宫主是否与火星（Mangal）同处一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v9`｜PDF [30]｜“Should Bandhu Bhava be a Movable one, while its Lord and Mangal are together in Ari, or Randhr Bhava, the native will be dumb.”


## 四路查书计划

### 支持路

- Bandhu Bhava Movable Lord with Mangal in Ari or Randhr dumb
- 四宫动星座 四宫主火星同宫 六宫八宫 哑

### 反例或取消路

- benefic drishti cancels affliction of Bandhu Lord
- 吉星相照 化解四宫主受克

### 适用边界路

- which signs count as Movable in this rule
- 动星座与同宫位置的适用边界

### 判断方法路

- how to judge speech defects in BPHS
- 判断言语缺陷要查什么

## 上游问题

- 无

## 停止条件

- 缺少四宫星座属性事实时停止。
- 缺少四宫主与火星是否同宫及所在宫位事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
