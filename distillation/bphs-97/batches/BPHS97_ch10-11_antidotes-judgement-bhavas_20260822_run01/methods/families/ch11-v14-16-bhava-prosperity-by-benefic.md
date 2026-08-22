---
method: ch11-v14-16-bhava-prosperity-by-benefic
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 宫之兴旺：该宫与吉星同宫或被吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这一宫是好是坏
- 怎么看某一宫兴不兴旺

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本次判断的是哪一宫（Bhava）

## 按情况检查的事实

- 该宫（Bhava）是否与吉星同宫
- 该宫（Bhava）是否被吉星相照

## 依赖方法

- 无

## 执行步骤

### ch11-v14-16-bhava-prosperity-by-benefic.step-001

- 动作：核对待判之宫（Bhava）是否与吉星同宫，或是否被吉星相照。
- 适用范围：适用于十二宫中任一宫；原文只给兴旺与否的方向，未给程度、事项或时间。
- 原文最小意思：该宫与吉星同宫，或被吉星相照时，该宫兴旺（prosperity）。
- 本步骤产出事实：["该宫受吉星相涉的兴旺判定"]
- 所需事实：["本次判断的是哪一宫（Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本次判断的是哪一宫（Bhava）"}, {"operator": "OR", "operands": [{"fact_key": "该宫（Bhava）是否与吉星同宫"}, {"fact_key": "该宫（Bhava）是否被吉星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本次判断的是哪一宫（Bhava）"}, "required_fact_keys": ["该宫（Bhava）是否与吉星同宫"], "branch_condition_logic": {"fact_key": "该宫（Bhava）是否与吉星同宫"}, "selection_group": "ch11-v14-16-bhava-prosperity-by-benefic.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：该宫（Bhava）是否与吉星同宫。"}, {"when": {"fact_key": "本次判断的是哪一宫（Bhava）"}, "required_fact_keys": ["该宫（Bhava）是否被吉星相照"], "branch_condition_logic": {"fact_key": "该宫（Bhava）是否被吉星相照"}, "selection_group": "ch11-v14-16-bhava-prosperity-by-benefic.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：该宫（Bhava）是否被吉星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「兴旺」具体化成某一件事（财、子、寿等），原文只给方向。", "不得据此推断兴旺的程度或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本次判断的是哪一宫（Bhava）。
- 缺失即停字段：["本次判断的是哪一宫（Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch11:v14-16`｜PDF [26]｜“Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic.”


## 四路查书计划

### 支持路

- Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic
- 该宫与吉星同宫或被吉星相照 该宫兴旺

### 反例或取消路

- The Bhava, which is not drishtied by its Lord, or, whose Lord is with a malefic Grah

### 适用边界路

- The learned should estimate the effects, due to a Bhava, in the manner, cited above, after ascertaining the strength and weakness
- 宫的吉凶要连同强弱一起估量

### 判断方法路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The Lord of the Bhava is equally important, when estimating the indications of a particular Bhava
- 怎样判断一个宫的兴衰

## 上游问题

- 无

## 停止条件

- 未指明要判哪一宫时停止。
- 该宫的吉星同宫与吉星相照事实都取不到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
