---
method: ch08-v1-3-common-rashi-drishti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 共同星座的相照：相照其余三个共同星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 某个共同星座相照哪几个星座
- 共同星座的 Drishti 落在哪里

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 待判星座（Rāśi）是否为共同星座（Common Rashi）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch08-v1-3-common-rashi-drishti.step-001

- 动作：核对待判星座是否为共同星座（Common Rashi），并定出它所相照的共同星座（Common Rāśis）。
- 适用范围：仅限第 8 章星座之间的相照（Rāśi Drishti）；本句只给相照的去向，不给吉凶断语。
- 原文最小意思：共同星座（Common Rashi）相照其余三个共同星座（Common Rāśis）。
- 本步骤产出事实：["待判共同星座（Common Rashi）所相照的三个共同星座（Common Rāśis）"]
- 所需事实：["待判星座（Rāśi）是否为共同星座（Common Rashi）"]
- 条件关系：{"fact_key": "待判星座（Rāśi）是否为共同星座（Common Rashi）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得给共同星座补上活动、固定两类星座那样的『略去相邻一个』的除外条款——原文对共同星座没有写这一条。", "不得据本句直接下吉凶断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：待判星座（Rāśi）是否为共同星座（Common Rashi）。
- 缺失即停字段：["待判星座（Rāśi）是否为共同星座（Common Rashi）"]
- 原文证据：
  - `bphs-97:santhanam:ch08:v1-3`｜PDF [21, 22]｜“And a Common Rashigives a Drishti to the other three Common Rāśis.”


## 四路查书计划

### 支持路

- And a Common Rashigives a Drishti to the other three Common Rāśis
- 共同星座 相照 其余三个共同星座

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
