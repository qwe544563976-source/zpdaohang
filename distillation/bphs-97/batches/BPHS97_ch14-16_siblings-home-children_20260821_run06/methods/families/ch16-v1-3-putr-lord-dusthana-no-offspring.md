---
method: ch16-v1-3-putr-lord-dusthana-no-offspring
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 无子嗣：五宫主落六宫、八宫或十二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我到底能不能有孩子
- 我这辈子会不会没有子嗣

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫主是哪颗行星

## 按情况检查的事实

- 五宫主是否落在第六宫（Ari Bhava）
- 五宫主是否落在第八宫（Randhr Bhava）
- 五宫主是否落在第十二宫（Vyaya Bhava）

## 依赖方法

- 无

## 执行步骤

### ch16-v1-3-putr-lord-dusthana-no-offspring.step-001

- 动作：先定出五宫主是哪颗行星，再核对它是否落在第六、第八或第十二宫。
- 适用范围：仅限本命盘五宫子女有无主题；原文只列这三个宫位，未给上升、性别或时间限定。
- 原文最小意思：五宫主落六宫、八宫或十二宫时，没有子嗣。
- 本步骤产出事实：["五宫主落凶宫无子嗣判定"]
- 所需事实：["本盘五宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "五宫主是否落在第六宫（Ari Bhava）"}, {"fact_key": "五宫主是否落在第八宫（Randhr Bhava）"}, {"fact_key": "五宫主是否落在第十二宫（Vyaya Bhava）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否落在第六宫（Ari Bhava）"], "branch_condition_logic": {"fact_key": "五宫主是否落在第六宫（Ari Bhava）"}, "selection_group": "ch16-v1-3-putr-lord-dusthana-no-offspring.step-001:dusthana", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落在第六宫（Ari Bhava）。"}, {"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否落在第八宫（Randhr Bhava）"], "branch_condition_logic": {"fact_key": "五宫主是否落在第八宫（Randhr Bhava）"}, "selection_group": "ch16-v1-3-putr-lord-dusthana-no-offspring.step-001:dusthana", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落在第八宫（Randhr Bhava）。"}, {"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否落在第十二宫（Vyaya Bhava）"], "branch_condition_logic": {"fact_key": "五宫主是否落在第十二宫（Vyaya Bhava）"}, "selection_group": "ch16-v1-3-putr-lord-dusthana-no-offspring.step-001:dusthana", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落在第十二宫（Vyaya Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断子女去世的年份或补救方式。", "不得把无子嗣断语改写成子女稀少或迟得。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫主是哪颗行星。
- 缺失即停字段：["本盘五宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v1-3`｜PDF [30]｜“Should Putr’s Lord be in Ari, Randhr, or Vyaya Bhava, there will be no offspring.”


## 四路查书计划

### 支持路

- 五宫主落六宫 八宫 十二宫 没有子嗣

### 反例或取消路

- 五宫主有力 子女众多 反例

### 适用边界路

- 无子断语的适用范围与限制

### 判断方法路

- 查五宫主落宫判断有无子女的步骤

## 上游问题

- 无

## 停止条件

- 缺少五宫主行星身份事实时停止。
- 缺少五宫主落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
