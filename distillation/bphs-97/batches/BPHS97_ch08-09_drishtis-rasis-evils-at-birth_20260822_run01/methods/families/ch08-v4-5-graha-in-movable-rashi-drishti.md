---
method: ch08-v4-5-graha-in-movable-rashi-drishti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 行星落活动星座：相照其余 3 个固定星座，略去紧邻的那个固定星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 行星落活动星座时相照哪几个星座
- 落活动星座的行星 Drishti 怎么算

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 待判行星（Grah）所落星座（Rāśi）是否为活动星座（Movable Rashi）
- 与待判行星（Grah）所落星座（Rāśi）紧邻的固定星座（Fixed Rashi）是哪一个

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch08-v4-5-graha-in-movable-rashi-drishti.step-001

- 动作：核对待判行星所落星座是否为活动星座，并定出它相照的固定星座（Fixed Rāśis）。
- 适用范围：仅限第 8 章星座相照体系下行星的相照；本句只给相照的去向，不给吉凶断语。
- 原文最小意思：落活动星座（Movable Rashi）的行星（Grah），相照其余 3 个固定星座（Fixed Rāśis），略去紧邻它的那个固定星座（Fixed Rashi）。
- 本步骤产出事实：["落活动星座的待判行星（Grah）所相照的三个固定星座（Fixed Rāśis）"]
- 所需事实：["待判行星（Grah）所落星座（Rāśi）是否为活动星座（Movable Rashi）", "与待判行星（Grah）所落星座（Rāśi）紧邻的固定星座（Fixed Rashi）是哪一个"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "待判行星（Grah）所落星座（Rāśi）是否为活动星座（Movable Rashi）"}, {"fact_key": "与待判行星（Grah）所落星座（Rāśi）紧邻的固定星座（Fixed Rashi）是哪一个"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把相照对象扩大到固定星座（Fixed Rāśis）以外的星座类别。", "不得据本句直接下吉凶断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：待判行星（Grah）所落星座（Rāśi）是否为活动星座（Movable Rashi）、与待判行星（Grah）所落星座（Rāśi）紧邻的固定星座（Fixed Rashi）是哪一个。
- 缺失即停字段：["待判行星（Grah）所落星座（Rāśi）是否为活动星座（Movable Rashi）", "与待判行星（Grah）所落星座（Rāśi）紧邻的固定星座（Fixed Rashi）是哪一个"]
- 原文证据：
  - `bphs-97:santhanam:ch08:v4-5`｜PDF [22]｜“A Grah in a Movable Rashigives a Drishti to the other 3 Fixed Rāśis, leaving the Fixed Rashinext to it.”


## 四路查书计划

### 支持路

- A Grah in a Movable Rashigives a Drishti to the other 3 Fixed Rāśis, leaving the Fixed Rashinext to it
- 行星落活动星座 相照 三个固定星座

### 反例或取消路

- 无

### 适用边界路

- O Brahmin, I have earlier stated Drishtis, based on Rāśis. The other kind is between Grahas, which I detail below.
- 行星自身的相照另有一套

### 判断方法路

- Drishtis of the Rāśis
- Dristhis of the Grahas
- 落某类星座的行星相照哪几个星座

## 上游问题

- 无

## 停止条件

- 未指明要判哪一颗行星（Grah）时停止。
- 缺少该行星所落星座（Rāśi）的活动／固定／共同性质时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
