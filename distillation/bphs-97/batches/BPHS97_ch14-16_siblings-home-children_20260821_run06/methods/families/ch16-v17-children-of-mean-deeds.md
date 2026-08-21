---
method: ch16-v17-children-of-mean-deeds
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 子女行为卑劣：五宫被三或四凶星占据且五宫主落陷

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我孩子的品行会怎么样
- 我的子女会不会走歪路

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫主是否落陷
- 五宫内是否有吉星（含水星）

## 按情况检查的事实

- 五宫是否被三颗凶星占据
- 五宫是否被四颗凶星占据

## 依赖方法

- 无

## 执行步骤

### ch16-v17-children-of-mean-deeds.step-001

- 动作：核对五宫内凶星数量与五宫主是否落陷，并核对五宫内是否有吉星（含水星），判断子女品行。
- 适用范围：仅限本命五宫子女品行主题；原文只给三颗或四颗凶星占据这两种数量，未给时间或上升限定。
- 原文最小意思：五宫被三颗或四颗凶星占据、且五宫主落陷时，所得子女会行卑劣之事；五宫中有吉星（含水星）则不算此组合。
- 本步骤产出事实：["子女行为卑劣判定"]
- 所需事实：["五宫主是否落陷", "五宫内是否有吉星（含水星）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "五宫主是否落陷"}, {"operator": "NOT", "operands": [{"fact_key": "五宫内是否有吉星（含水星）"}]}]}, {"operator": "OR", "operands": [{"fact_key": "五宫是否被三颗凶星占据"}, {"fact_key": "五宫是否被四颗凶星占据"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "五宫主是否落陷"}, {"operator": "NOT", "operands": [{"fact_key": "五宫内是否有吉星（含水星）"}]}]}, "required_fact_keys": ["五宫是否被三颗凶星占据"], "branch_condition_logic": {"fact_key": "五宫是否被三颗凶星占据"}, "selection_group": "ch16-v17-children-of-mean-deeds.step-001:malefic-count", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫是否被三颗凶星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "五宫主是否落陷"}, {"operator": "NOT", "operands": [{"fact_key": "五宫内是否有吉星（含水星）"}]}]}, "required_fact_keys": ["五宫是否被四颗凶星占据"], "branch_condition_logic": {"fact_key": "五宫是否被四颗凶星占据"}, "selection_group": "ch16-v17-children-of-mean-deeds.step-001:malefic-count", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫是否被四颗凶星占据。"}]
- 例外、取消或缓解：[{"type": "limitation", "evidence_atom_ids": ["bphs-97:santhanam:ch16:v17"], "condition_logic": {"fact_key": "五宫内是否有吉星（含水星）"}}]
- 禁止扩大：["不得把凶星数量少于三颗的情形也算作本组合。", "不得据此推断子女数量或子女具体行为。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否落陷、五宫内是否有吉星（含水星）。
- 缺失即停字段：["五宫主是否落陷", "五宫内是否有吉星（含水星）"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v17`｜PDF [31]｜“One will obtain children, that will indulge in mean deeds, if Putr is occupied by three, or four malefics, while Putr’s Lord is in fall.”
  - `bphs-97:santhanam:ch16:v17`｜PDF [31]｜“A benefic (including Budh) in Putr is excluded in the said combination.”


## 四路查书计划

### 支持路

- 五宫三四颗凶星 五宫主落陷 子女卑劣

### 反例或取消路

- 五宫有吉星含水星 组合被排除

### 适用边界路

- 五宫凶星数量三或四的适用边界

### 判断方法路

- 判断子女品行要看五宫哪些条件

## 上游问题

- 无

## 停止条件

- 缺少五宫内凶星数量事实时停止。
- 缺少五宫主庙陷状态事实时停止。
- 缺少五宫内是否有吉星（含水星）事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
