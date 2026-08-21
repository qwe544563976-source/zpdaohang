---
method: ch14-v3-cobirth-destruction-malefic
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三宫主与 Mangal 遇凶星或落凶星星座：兄弟姐妹立即毁灭

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的兄弟姐妹会不会去世
- 家里孩子是不是养不住

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本命盘中哪些行星被判为凶星

## 按情况检查的事实

- 三宫主与 Mangal 是否与凶星同宫
- 三宫主与 Mangal 是否落在凶星所主的星座

## 依赖方法

- 无

## 执行步骤

### ch14-v3-cobirth-destruction-malefic.step-001

- 动作：核对前一偈所说的三宫主与 Mangal 这两颗行星是否与凶星同宫，或落在凶星所主的星座。
- 适用范围：仅限本命盘三宫兄弟姐妹存亡主题；本条承接前一偈所指的两颗行星，原文未给时间限定。
- 原文最小意思：前述2颗行星与凶星同宫，或落在凶星所主的星座，兄弟姐妹立即毁灭。
- 本步骤产出事实：["前述两星遇凶导致兄弟姐妹毁灭判定"]
- 所需事实：["本命盘中哪些行星被判为凶星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本命盘中哪些行星被判为凶星"}, {"operator": "OR", "operands": [{"fact_key": "三宫主与 Mangal 是否与凶星同宫"}, {"fact_key": "三宫主与 Mangal 是否落在凶星所主的星座"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本命盘中哪些行星被判为凶星"}, "required_fact_keys": ["三宫主与 Mangal 是否与凶星同宫"], "branch_condition_logic": {"fact_key": "三宫主与 Mangal 是否与凶星同宫"}, "selection_group": "ch14-v3-cobirth-destruction-malefic.step-001:malefic-link", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主与 Mangal 是否与凶星同宫。"}, {"when": {"fact_key": "本命盘中哪些行星被判为凶星"}, "required_fact_keys": ["三宫主与 Mangal 是否落在凶星所主的星座"], "branch_condition_logic": {"fact_key": "三宫主与 Mangal 是否落在凶星所主的星座"}, "selection_group": "ch14-v3-cobirth-destruction-malefic.step-001:malefic-link", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主与 Mangal 是否落在凶星所主的星座。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断毁灭发生的年龄、年份或具体是哪一位兄弟姐妹。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本命盘中哪些行星被判为凶星。
- 缺失即停字段：["本命盘中哪些行星被判为凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v3`｜PDF [28]｜“Destruction at once of co-born will come to pass, if the said 2 Grahas are together with a malefic, or in a Rāśi, owned by a malefic.”


## 四路查书计划

### 支持路

- said 2 Grahas together with a malefic destruction of co-born
- 三宫主与火星 与凶星同宫 兄弟姐妹毁灭

### 反例或取消路

- Mangal or Sahaj Lord in angle trine exaltation happiness co-born
- 三宫主入角宫三角宫 兄弟姐妹得幸福

### 适用边界路

- destruction at once of co-born condition scope
- 兄弟姐妹毁灭判断的适用边界

### 判断方法路

- how to judge destruction of co-born in Sahaj Bhava
- 判断兄弟姐妹是否毁灭的步骤

## 上游问题

- 无

## 停止条件

- 缺少本命盘凶星判定事实时停止。
- 缺少前述两颗行星的同宫与所落星座事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
