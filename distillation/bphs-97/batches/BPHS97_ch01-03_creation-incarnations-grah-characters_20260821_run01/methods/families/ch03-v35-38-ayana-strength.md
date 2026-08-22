---
method: ch03-v35-38-ayana-strength
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 南行北行强弱：凶星强于南行、吉星强于北行

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我出生在太阳南行还是北行 对吉凶星强弱有什么影响
- Dakshinayan 出生哪类行星有力

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘出生时太阳（Surya）行于南行（Dakshinayan）还是北行（Uttarayan）
- 本盘中哪些行星被判为凶星
- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v35-38-ayana-strength.step-001

- 动作：核对本盘出生时太阳的南北行与吉凶星名册，判断哪一类行星处于有力的行度。
- 适用范围：第3章诸曜强弱条；吉凶星的名册由本书第3章另条界定，本偈不重复。
- 原文最小意思：凶星在南行（Dakshinayan）有力，吉星在北行（Uttarayan）有力。
- 本步骤产出事实：["南行北行吉凶星强弱判定"]
- 所需事实：["本盘出生时太阳（Surya）行于南行（Dakshinayan）还是北行（Uttarayan）", "本盘中哪些行星被判为凶星", "本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘出生时太阳（Surya）行于南行（Dakshinayan）还是北行（Uttarayan）"}, {"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条把强弱读成吉凶结果。", "不得据本条推出南北行强弱的具体分值。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生时太阳（Surya）行于南行（Dakshinayan）还是北行（Uttarayan）、本盘中哪些行星被判为凶星、本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘出生时太阳（Surya）行于南行（Dakshinayan）还是北行（Uttarayan）", "本盘中哪些行星被判为凶星", "本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v35-38`｜PDF [11]｜“Malefics and benefics are, respectively, strong in Dakshinayan and Uttarayan.”


## 四路查书计划

### 支持路

- Malefics and benefics are, respectively, strong in Dakshinayan and Uttarayan
- 南行 北行 吉凶星强弱

### 反例或取消路

- 无

### 适用边界路

- These strengths are computed for the seven Grahas from Surya to Shani. The nodes are not considered
- 南北行强弱只算七曜

### 判断方法路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal), inclusive of Ayan Bal (equinoctial)
- 本书怎么界定吉星与凶星

## 上游问题

- 无

## 停止条件

- 缺少本盘出生时太阳南行北行的事实时停止。
- 缺少本盘吉星或凶星名册时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
