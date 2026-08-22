---
method: ch28-v11-12-auspiciousness-more-dasha-bhavas-auspicious
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 吉性较多：该行星的大运与诸宫为吉

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 这颗行星的大运对我是好是坏
- 行星力量算出来之后怎么断吉凶

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 所考察行星（Grah）的吉性数值是否多于凶性数值

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch28-v11-12-auspiciousness-more-dasha-bhavas-auspicious.step-001

- 动作：把所考察行星所得的 Dig Bal 等力量数值与从 60 减得的凶性数值相比，吉性较多时断该行星相关的大运与诸宫为吉。
- 适用范围：原文本句以 Dig Bal、Kaal Bal 等力量数值立说；原文没有指明吉果体现在哪一宫、哪一事项或哪一时段。
- 原文最小意思：行星（Grah）所得的 Dig Bal 等力量数值即其吉性程度，从 60 减去这些数值即得凶性程度；该行星力量所显吉性较多时，与该行星相关的大运（Dasha）与诸宫（Bhavas）为吉。
- 本步骤产出事实：["所考察行星相关大运与诸宫的吉凶定性"]
- 所需事实：["所考察行星（Grah）的吉性数值是否多于凶性数值"]
- 条件关系：{"fact_key": "所考察行星（Grah）的吉性数值是否多于凶性数值"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推算大运的起止年份或具体应验事项。", "原文只说相关的大运与诸宫为吉，不得改读成该行星本身变成吉星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所考察行星（Grah）的吉性数值是否多于凶性数值。
- 缺失即停字段：["所考察行星（Grah）的吉性数值是否多于凶性数值"]
- 原文证据：
  - `bphs-97:santhanam:ch28:v11-12`｜PDF [61]｜“Whatever quantum of Dig Bal etc. are obtained by a Grah, will be the extent of auspicious effects, acquirable on account of that strength.”
  - `bphs-97:santhanam:ch28:v11-12`｜PDF [61]｜“Deducting those figures from 60, the extent of inauspiciousness is known.”
  - `bphs-97:santhanam:ch28:v11-12`｜PDF [61]｜“If auspiciousness is more in the case of a Grah’s strength, the Dasha and Bhavas, related to that Grah will be auspicious.”


## 四路查书计划

### 支持路

- If auspiciousness is more in the case of a Grah’s strength, the Dasha and Bhavas, related to that Grah will be auspicious
- Whatever quantum of Dig Bal etc. are obtained by a Grah, will be the extent of auspicious effects
- 吉性大于凶性 大运与宫为吉

### 反例或取消路

- These are converse, if inauspiciousness is predominant
- 凶性占优时的相反结论

### 适用边界路

- The directional strength of a Grah is itself representative of the effects, due to the direction
- 本条只在 Dig Bal、Kaal Bal 等力量体系内成立

### 判断方法路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- 怎样计算行星的六力与方位力

## 上游问题

- 无

## 停止条件

- 缺少所考察行星的吉性与凶性数值时停止。
- 无法判定两者孰多孰少时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
