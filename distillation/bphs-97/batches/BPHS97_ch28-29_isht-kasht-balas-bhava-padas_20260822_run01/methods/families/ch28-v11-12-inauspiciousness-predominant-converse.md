---
method: ch28-v11-12-inauspiciousness-predominant-converse
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶性占优：前句判定相反

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 行星凶性大于吉性时怎么看
- 我这个大运是不是反过来断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 所考察行星（Grah）的凶性数值是否占优（predominant）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch28-v11-12-inauspiciousness-predominant-converse.step-001

- 动作：判定所考察行星的凶性是否占优，若占优则把前句的吉断反过来。
- 适用范围：原文只写“These are converse”，没有把反过来的内容逐项写出；本步只保留“相反”这一层意思，不替原文列举具体应验。
- 原文最小意思：该行星（Grah）凶性占优时，前句关于大运（Dasha）与诸宫（Bhavas）为吉的判定相反。
- 本步骤产出事实：["所考察行星相关大运与诸宫的相反判定"]
- 所需事实：["所考察行星（Grah）的凶性数值是否占优（predominant）"]
- 条件关系：{"fact_key": "所考察行星（Grah）的凶性数值是否占优（predominant）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写“相反”，不得替它写出具体的凶事、程度或时间。", "不得把“凶性占优”等同于行星本身是凶星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所考察行星（Grah）的凶性数值是否占优（predominant）。
- 缺失即停字段：["所考察行星（Grah）的凶性数值是否占优（predominant）"]
- 原文证据：
  - `bphs-97:santhanam:ch28:v11-12`｜PDF [61]｜“These are converse, if inauspiciousness is predominant.”


## 四路查书计划

### 支持路

- These are converse, if inauspiciousness is predominant
- 凶性占优 结论相反

### 反例或取消路

- If auspiciousness is more in the case of a Grah’s strength, the Dasha and Bhavas, related to that Grah will be auspicious
- 吉性较多时的吉断

### 适用边界路

- and Kaal Bal itself is indicative of effects, due to the day
- “相反”到底反到什么程度，原文未定

### 判断方法路

- Deducting those figures from 60, the extent of inauspiciousness is known
- 怎样算行星的凶性数值

## 上游问题

- 无

## 停止条件

- 缺少所考察行星的凶性与吉性数值时停止。
- 原文未写明“相反”的具体内容，需要具体应验事项时停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
