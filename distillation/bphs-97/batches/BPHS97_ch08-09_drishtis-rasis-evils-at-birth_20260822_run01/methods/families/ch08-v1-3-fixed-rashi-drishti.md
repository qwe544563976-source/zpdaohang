---
method: ch08-v1-3-fixed-rashi-drishti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 固定星座的相照：相照 3 个活动星座，略去相邻的那个活动星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 某个固定星座相照哪几个星座
- 固定星座的 Drishti 落在哪里

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 待判星座（Rāśi）是否为固定星座（Fixed Rashi）
- 与待判星座（Rāśi）相邻的活动星座（Movable Rashi）是哪一个

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch08-v1-3-fixed-rashi-drishti.step-001

- 动作：核对待判星座是否为固定星座（Fixed Rashi），并定出它所相照的活动星座（Movable Rāśis）。
- 适用范围：仅限第 8 章星座之间的相照（Rāśi Drishti）；本句只给相照的去向，不给吉凶断语。
- 原文最小意思：每个固定星座（Fixed Rashi）相照 3 个活动星座（Movable Rāśis），但不照相邻的那个活动星座（Movable Rāśi）。
- 本步骤产出事实：["待判固定星座（Fixed Rashi）所相照的三个活动星座（Movable Rāśis）"]
- 所需事实：["待判星座（Rāśi）是否为固定星座（Fixed Rashi）", "与待判星座（Rāśi）相邻的活动星座（Movable Rashi）是哪一个"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "待判星座（Rāśi）是否为固定星座（Fixed Rashi）"}, {"fact_key": "与待判星座（Rāśi）相邻的活动星座（Movable Rashi）是哪一个"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把相照对象扩大到活动星座（Movable Rāśis）以外的星座类别。", "不得据本句直接下吉凶断语——本句只给相照的去向。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：待判星座（Rāśi）是否为固定星座（Fixed Rashi）、与待判星座（Rāśi）相邻的活动星座（Movable Rashi）是哪一个。
- 缺失即停字段：["待判星座（Rāśi）是否为固定星座（Fixed Rashi）", "与待判星座（Rāśi）相邻的活动星座（Movable Rashi）是哪一个"]
- 原文证据：
  - `bphs-97:santhanam:ch08:v1-3`｜PDF [21, 22]｜“Every Fixed Rashigives Drishti to the 3 Movable Rāśis, barring the adjacent Movable Rāśi.”


## 四路查书计划

### 支持路

- Every Fixed Rashigives Drishti to the 3 Movable Rāśis, barring the adjacent Movable Rāśi
- 固定星座 相照 三个活动星座 Rāśi Drishti

### 反例或取消路

- 无

### 适用边界路

- O Brahmin, I have earlier stated Drishtis, based on Rāśis. The other kind is between Grahas, which I detail below.
- 星座相照与行星相照是两套不同的相照

### 判断方法路

- Drishtis of the Rāśis
- Diagram of Dristhis. As depicted by Lord Brahma, I now narrate the diagram of Drishtis
- 星座之间的相照怎么排

## 上游问题

- 无

## 停止条件

- 未指明要判哪一个星座（Rāśi）时停止。
- 缺少该星座的活动／固定／共同性质时停止。
- 原文本句不给吉凶，要断吉凶须另查原文，本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
