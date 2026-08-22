---
method: ch08-v1-3-graha-follows-its-rashi-drishti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 落某星座的行星，其相照与该星座相同

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 某颗行星相照哪几个星座
- 行星的相照跟它所落星座有什么关系

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 待判行星（Grah）落在哪个星座（Rāśi）
- 该星座（Rāśi）所相照的星座（Rāśis）是哪些

## 按情况检查的事实

- 无

## 依赖方法

- ch08-v1-3-movable-rashi-drishti
- ch08-v1-3-fixed-rashi-drishti
- ch08-v1-3-common-rashi-drishti

## 执行步骤

### ch08-v1-3-graha-follows-its-rashi-drishti.step-001

- 动作：先取待判行星所落的星座，再把该星座的相照对象照搬为该行星的相照对象。
- 适用范围：仅限第 8 章星座之间的相照（Rāśi Drishti）体系内；本句只给相照的去向，不给吉凶断语。
- 原文最小意思：落某星座（Rāśi）的行星（Grah），给出与该星座（Rāśi）相同的相照。
- 本步骤产出事实：["待判行星（Grah）在星座相照体系下所相照的星座（Rāśis）"]
- 所需事实：["待判行星（Grah）落在哪个星座（Rāśi）", "该星座（Rāśi）所相照的星座（Rāśis）是哪些"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "待判行星（Grah）落在哪个星座（Rāśi）"}, {"fact_key": "该星座（Rāśi）所相照的星座（Rāśis）是哪些"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把本句当成行星自身相照（第 26 章的行星相照）的规则——本句说的是星座相照体系。", "不得据本句直接下吉凶断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：待判行星（Grah）落在哪个星座（Rāśi）、该星座（Rāśi）所相照的星座（Rāśis）是哪些。
- 缺失即停字段：["待判行星（Grah）落在哪个星座（Rāśi）", "该星座（Rāśi）所相照的星座（Rāśis）是哪些"]
- 原文证据：
  - `bphs-97:santhanam:ch08:v1-3`｜PDF [21, 22]｜“The Grah in a Rashigives the same Drishti, as the Rashi(in which the Grah is) does.”


## 四路查书计划

### 支持路

- The Grah in a Rashigives the same Drishti, as the Rashi(in which the Grah is) does
- 行星 相照 与所落星座相同

### 反例或取消路

- 无

### 适用边界路

- O Brahmin, I have earlier stated Drishtis, based on Rāśis. The other kind is between Grahas, which I detail below.
- 行星自身的相照另有一套（3、10、5、9、4、8、7 宫）

### 判断方法路

- Drishtis of the Rāśis
- A Grah in a Movable Rashigives a Drishti to the other 3 Fixed Rāśis
- 行星的相照怎么定

## 上游问题

- 无

## 停止条件

- 未指明要判哪一颗行星（Grah）时停止。
- 缺少该行星所落星座（Rāśi）时停止。
- 缺少该星座的相照对象时停止（须先用同章活动／固定／共同三条定出）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
