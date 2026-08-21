---
method: ch15-v2-housing-comfort
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 住房舒适：四宫被宫主或上升主占据且受吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子住房条件怎么样
- 我能不能住得舒服

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 四宫是否受吉星相照

## 按情况检查的事实

- 四宫是否被四宫主占据
- 四宫是否被上升主占据

## 依赖方法

- 无

## 执行步骤

### ch15-v2-housing-comfort.step-001

- 动作：核对四宫（Bandhu Bhava）的占据者与吉星相照，判断住房舒适程度。
- 适用范围：仅限本命盘四宫住房主题；原文未给时间或上升限定。
- 原文最小意思：四宫被其宫主或上升主占据、并受吉星相照时，住房舒适圆满。
- 本步骤产出事实：["四宫住房舒适判定"]
- 所需事实：["四宫是否受吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "四宫是否受吉星相照"}, {"operator": "OR", "operands": [{"fact_key": "四宫是否被四宫主占据"}, {"fact_key": "四宫是否被上升主占据"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "四宫是否受吉星相照"}, "required_fact_keys": ["四宫是否被四宫主占据"], "branch_condition_logic": {"fact_key": "四宫是否被四宫主占据"}, "selection_group": "ch15-v2-housing-comfort.step-001:occupier", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫是否被四宫主占据。"}, {"when": {"fact_key": "四宫是否受吉星相照"}, "required_fact_keys": ["四宫是否被上升主占据"], "branch_condition_logic": {"fact_key": "四宫是否被上升主占据"}, "selection_group": "ch15-v2-housing-comfort.step-001:occupier", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫是否被上升主占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断房产数量、价值或购房时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：四宫是否受吉星相照。
- 缺失即停字段：["四宫是否受吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v2`｜PDF [29]｜“One will have residential comforts in full degree, if Bandhu is occupied by its Lord, or by Lagn’s Lord and be drishtied by a benefic.”


## 四路查书计划

### 支持路

- 四宫主落四宫 住房舒适

### 反例或取消路

- 四宫受凶星 住房不利

### 适用边界路

- 住房判断的适用边界

### 判断方法路

- 判断四宫应检查什么

## 上游问题

- 无

## 停止条件

- 缺少四宫占据者事实时停止。
- 缺少四宫相位事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
