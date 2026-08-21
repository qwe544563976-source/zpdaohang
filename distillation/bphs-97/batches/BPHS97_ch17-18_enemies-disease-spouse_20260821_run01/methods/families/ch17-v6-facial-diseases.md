---
method: ch17-v6-facial-diseases
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 面部疾病：上升主落火星或水星的星座并相照水星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我脸上会不会有病
- 我的面部健康怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagna's Lord）是否相照水星（Budh）

## 按情况检查的事实

- 上升主（Lagna's Lord）是否落火星（Mangal）主管的星座
- 上升主（Lagna's Lord）是否落水星（Budh）主管的星座

## 依赖方法

- 无

## 执行步骤

### ch17-v6-facial-diseases.step-001

- 动作：核对上升主（Lagn's Lord）所落星座的主星，以及它对水星（Budh）的相照。
- 适用范围：仅限本命盘面部疾病主题；原文未给时间限定，也未说明具体病名。
- 原文最小意思：上升主落于火星主管的星座或水星主管的星座、并相照水星时，会有面部疾病。
- 本步骤产出事实：["上升主与水星的面部疾病判定"]
- 所需事实：["上升主（Lagna's Lord）是否相照水星（Budh）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagna's Lord）是否相照水星（Budh）"}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagna's Lord）是否落火星（Mangal）主管的星座"}, {"fact_key": "上升主（Lagna's Lord）是否落水星（Budh）主管的星座"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "上升主（Lagna's Lord）是否相照水星（Budh）"}, "required_fact_keys": ["上升主（Lagna's Lord）是否落火星（Mangal）主管的星座"], "branch_condition_logic": {"fact_key": "上升主（Lagna's Lord）是否落火星（Mangal）主管的星座"}, "selection_group": "ch17-v6-facial-diseases.step-001:lagna-lord-sign", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagna's Lord）是否落火星（Mangal）主管的星座。"}, {"when": {"fact_key": "上升主（Lagna's Lord）是否相照水星（Budh）"}, "required_fact_keys": ["上升主（Lagna's Lord）是否落水星（Budh）主管的星座"], "branch_condition_logic": {"fact_key": "上升主（Lagna's Lord）是否落水星（Budh）主管的星座"}, "selection_group": "ch17-v6-facial-diseases.step-001:lagna-lord-sign", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagna's Lord）是否落水星（Budh）主管的星座。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断面部疾病的病名、部位细节或发生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagna's Lord）是否相照水星（Budh）。
- 缺失即停字段：["上升主（Lagna's Lord）是否相照水星（Budh）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v6`｜PDF [32]｜“Should Lagn’s Lord be in a Rashiof Mangal, or of Budh and has a Drishti on Budh, there will be diseases of the face.”


## 四路查书计划

### 支持路

- Should Lagn’s Lord be in a Rashiof Mangal, or of Budh and has a Drishti on Budh diseases of the face
- 上升主 火星星座 水星星座 相照水星 面部疾病

### 反例或取消路

- Guru in similar case will destroy any disease
- Lagn Lord is singly capable of counteracting all evils

### 适用边界路

- Evaluation of Drishtis of Grahas 相照的取值范围
- Decanates and Bodily Limbs head eyes ears nose temple chin and face

### 判断方法路

- Indications of Ari Bhava ulcers enemies
- 判断面部与头部疾病应检查哪些行星

## 上游问题

- 无

## 停止条件

- 缺少上升主相照水星的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
