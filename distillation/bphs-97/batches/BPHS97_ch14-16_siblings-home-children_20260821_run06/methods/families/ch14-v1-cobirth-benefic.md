---
method: ch14-v1-cobirth-benefic
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三宫与吉星同宫或受吉星相照：得兄弟姐妹并有勇气

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有兄弟姐妹
- 我兄弟姐妹多不多
- 我这个人算不算有胆量

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本命盘中哪些行星被判为吉星

## 按情况检查的事实

- 三宫是否与吉星同宫
- 三宫是否被吉星相照

## 依赖方法

- 无

## 执行步骤

### ch14-v1-cobirth-benefic.step-001

- 动作：核对三宫（Sahaj Bhava）与吉星的同宫或相照关系，判断兄弟姐妹与勇气。
- 适用范围：仅限本命盘三宫兄弟姐妹与勇气主题；原文未给上升、时间或数量限定。
- 原文最小意思：三宫与吉星同宫，或受吉星相照，得兄弟姐妹并有勇气。
- 本步骤产出事实：["三宫吉星联结得兄弟姐妹与勇气判定"]
- 所需事实：["本命盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本命盘中哪些行星被判为吉星"}, {"operator": "OR", "operands": [{"fact_key": "三宫是否与吉星同宫"}, {"fact_key": "三宫是否被吉星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本命盘中哪些行星被判为吉星"}, "required_fact_keys": ["三宫是否与吉星同宫"], "branch_condition_logic": {"fact_key": "三宫是否与吉星同宫"}, "selection_group": "ch14-v1-cobirth-benefic.step-001:benefic-link", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫是否与吉星同宫。"}, {"when": {"fact_key": "本命盘中哪些行星被判为吉星"}, "required_fact_keys": ["三宫是否被吉星相照"], "branch_condition_logic": {"fact_key": "三宫是否被吉星相照"}, "selection_group": "ch14-v1-cobirth-benefic.step-001:benefic-link", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫是否被吉星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断兄弟姐妹的具体数目、性别或出生顺序。", "不得把本条的勇气结论扩大到其他宫位主题。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本命盘中哪些行星被判为吉星。
- 缺失即停字段：["本命盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v1`｜PDF [28]｜“Should Sahaj Bhava be yuti with, or drishtied by a benefic, the native will be endowed with co-born and be courageous.”


## 四路查书计划

### 支持路

- 三宫 吉星同宫 相照 兄弟姐妹 勇气

### 反例或取消路

- 三宫受凶星 兄弟姐妹受损

### 适用边界路

- 三宫吉星判断的适用边界

### 判断方法路

- 判断三宫兄弟姐妹应检查什么

## 上游问题

- 无

## 停止条件

- 缺少本命盘吉星判定事实时停止。
- 缺少三宫同宫与相照行星事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
