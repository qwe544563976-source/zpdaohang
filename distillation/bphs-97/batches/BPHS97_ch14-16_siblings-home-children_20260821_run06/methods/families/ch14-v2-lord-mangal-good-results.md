---
method: ch14-v2-lord-mangal-good-results
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三宫主与 Mangal 相照或落三宫：因三宫得好结果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我和兄弟姐妹的关系好不好
- 兄弟姐妹会不会给我带来好处

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 三宫主是哪颗行星

## 按情况检查的事实

- 三宫主与 Mangal 是否一同相照三宫
- 三宫主与 Mangal 是否同落三宫内

## 依赖方法

- 无

## 执行步骤

### ch14-v2-lord-mangal-good-results.step-001

- 动作：核对三宫主与 Mangal 是否一同相照三宫，或这两颗行星是否同落三宫内。
- 适用范围：仅限本命盘三宫（Sahaj Bhava）好结果主题；原文未给时间、上升或数量限定。
- 原文最小意思：三宫主与 Mangal 一同相照三宫，或这两颗行星同落三宫内，命主因三宫得好结果。
- 本步骤产出事实：["三宫主与 Mangal 带来三宫好结果判定"]
- 所需事实：["三宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "三宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "三宫主与 Mangal 是否一同相照三宫"}, {"fact_key": "三宫主与 Mangal 是否同落三宫内"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫主与 Mangal 是否一同相照三宫"], "branch_condition_logic": {"fact_key": "三宫主与 Mangal 是否一同相照三宫"}, "selection_group": "ch14-v2-lord-mangal-good-results.step-001:lord-mangal-link", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主与 Mangal 是否一同相照三宫。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫主与 Mangal 是否同落三宫内"], "branch_condition_logic": {"fact_key": "三宫主与 Mangal 是否同落三宫内"}, "selection_group": "ch14-v2-lord-mangal-good-results.step-001:lord-mangal-link", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主与 Mangal 是否同落三宫内。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断好结果的具体内容、数量或发生时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：三宫主是哪颗行星。
- 缺失即停字段：["三宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v2`｜PDF [28]｜“If Sahaj’s Lord along with Mangal drishties Sahaj Bhava, the native will enjoy good results, due to Sahaj Bhava. Alternatively these two Grahas may be in Sahaj itself.”


## 四路查书计划

### 支持路

- 三宫主 与火星 相照三宫 好结果

### 反例或取消路

- 三宫主与火星遇凶星 兄弟姐妹毁灭

### 适用边界路

- 三宫好结果的适用边界

### 判断方法路

- 判断三宫主与火星组合的步骤

## 上游问题

- 无

## 停止条件

- 缺少三宫主行星身份事实时停止。
- 缺少三宫主与 Mangal 的相照或落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
