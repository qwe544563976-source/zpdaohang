---
method: ch14-v6-cobirth-happiness
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Mangal 或三宫主入角宫、三角宫、入旺或友好分盘：兄弟姐妹方面得幸福

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我和兄弟姐妹能不能过得顺心
- 兄弟姐妹方面我有没有福气

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 三宫主是哪颗行星

## 按情况检查的事实

- Mangal 是否落于角宫
- Mangal 是否落于三角宫
- Mangal 是否入旺
- Mangal 是否落于友好分盘
- 三宫主是否落于角宫
- 三宫主是否落于三角宫
- 三宫主是否入旺
- 三宫主是否落于友好分盘

## 依赖方法

- 无

## 执行步骤

### ch14-v6-cobirth-happiness.step-001

- 动作：核对 Mangal 或三宫主是否落于角宫、三角宫、入旺或友好分盘。
- 适用范围：仅限本命盘兄弟姐妹方面的幸福主题；本句以“in this respect”承接同偈的兄弟姐妹话题，原文未给时间限定。
- 原文最小意思：Mangal 或三宫主落于角宫、三角宫、入旺或友好分盘时，兄弟姐妹方面得幸福。
- 本步骤产出事实：["兄弟姐妹方面得幸福判定"]
- 所需事实：["三宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "三宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "Mangal 是否落于角宫"}, {"fact_key": "Mangal 是否落于三角宫"}, {"fact_key": "Mangal 是否入旺"}, {"fact_key": "Mangal 是否落于友好分盘"}, {"fact_key": "三宫主是否落于角宫"}, {"fact_key": "三宫主是否落于三角宫"}, {"fact_key": "三宫主是否入旺"}, {"fact_key": "三宫主是否落于友好分盘"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["Mangal 是否落于角宫"], "branch_condition_logic": {"fact_key": "Mangal 是否落于角宫"}, "selection_group": "ch14-v6-cobirth-happiness.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：Mangal 是否落于角宫。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["Mangal 是否落于三角宫"], "branch_condition_logic": {"fact_key": "Mangal 是否落于三角宫"}, "selection_group": "ch14-v6-cobirth-happiness.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：Mangal 是否落于三角宫。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["Mangal 是否入旺"], "branch_condition_logic": {"fact_key": "Mangal 是否入旺"}, "selection_group": "ch14-v6-cobirth-happiness.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：Mangal 是否入旺。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["Mangal 是否落于友好分盘"], "branch_condition_logic": {"fact_key": "Mangal 是否落于友好分盘"}, "selection_group": "ch14-v6-cobirth-happiness.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：Mangal 是否落于友好分盘。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫主是否落于角宫"], "branch_condition_logic": {"fact_key": "三宫主是否落于角宫"}, "selection_group": "ch14-v6-cobirth-happiness.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主是否落于角宫。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫主是否落于三角宫"], "branch_condition_logic": {"fact_key": "三宫主是否落于三角宫"}, "selection_group": "ch14-v6-cobirth-happiness.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主是否落于三角宫。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫主是否入旺"], "branch_condition_logic": {"fact_key": "三宫主是否入旺"}, "selection_group": "ch14-v6-cobirth-happiness.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主是否入旺。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫主是否落于友好分盘"], "branch_condition_logic": {"fact_key": "三宫主是否落于友好分盘"}, "selection_group": "ch14-v6-cobirth-happiness.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主是否落于友好分盘。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断兄弟姐妹的数目、性别或幸福出现的时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：三宫主是哪颗行星。
- 缺失即停字段：["三宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v5-6`｜PDF [28, 29]｜“Happiness in this respect will come to pass, if Mangal, or Sahaj’s Lord is in an angle, or in a trine, or in exaltation, or friendly divisions.”


## 四路查书计划

### 支持路

- 火星或三宫主 角宫 三角宫 入旺 友好分盘 兄弟姐妹幸福

### 反例或取消路

- 三宫主与火星落八宫 兄弟姐妹毁灭

### 适用边界路

- 兄弟姐妹幸福判断的适用边界

### 判断方法路

- 判断兄弟姐妹是否顺遂的步骤

## 上游问题

- 无

## 停止条件

- 缺少三宫主行星身份事实时停止。
- 缺少 Mangal 与三宫主的落宫、庙旺与分盘事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
