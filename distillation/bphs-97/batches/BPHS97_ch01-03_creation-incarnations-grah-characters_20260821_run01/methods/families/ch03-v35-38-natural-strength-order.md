---
method: ch03-v35-38-natural-strength-order
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 七曜的自然强弱升序：土星最弱、太阳最强

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 两颗行星本身谁更强
- 七曜的天然强弱次序是什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中待比较自然强弱的两颗行星分别是哪两颗

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v35-38-natural-strength-order.step-001

- 动作：把待比较的两颗行星放进原文给的升序名单，判断哪一颗自然更强。
- 适用范围：第3章诸曜强弱条；本名单只列七曜，不含交点，且未给分值。
- 原文最小意思：按升序一个比一个更强的次序是土星（Shani）、火星（Mangal）、水星（Budh）、木星（Guru）、金星（Shukr）、月亮（Chandra）、太阳（Surya）。
- 本步骤产出事实：["七曜自然强弱次序判定"]
- 所需事实：["本盘中待比较自然强弱的两颗行星分别是哪两颗"]
- 条件关系：{"fact_key": "本盘中待比较自然强弱的两颗行星分别是哪两颗"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这条自然次序当成盘中实际强弱的最终结论——本偈另有方位、昼夜、明暗半月等来源。", "不得据本条推出交点（Rahu、Ketu）在这条次序中的位置——本名单只列七曜。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中待比较自然强弱的两颗行星分别是哪两颗。
- 缺失即停字段：["本盘中待比较自然强弱的两颗行星分别是哪两颗"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v35-38`｜PDF [11]｜“Again, stronger than the other in the ascending are Shani, Mangal, Budh, Guru, Shukr, Chandra and Surya.”


## 四路查书计划

### 支持路

- Again, stronger than the other in the ascending are Shani, Mangal, Budh, Guru, Shukr, Chandra and Surya
- 七曜 自然强弱 升序

### 反例或取消路

- 无

### 适用边界路

- These strengths are computed for the seven Grahas from Surya to Shani. The nodes are not considered
- 自然强弱不含交点

### 判断方法路

- Naisargika Bal. Divide one Rupa by 7 and multiply the resultant product by 1 to 7 separately, which will indicate the Naisargika Bal, due to Shani, Mangal, Budh, Guru, Shukr, Chandra and Surya, respectively
- 自然强弱怎么量化

## 上游问题

- 无

## 停止条件

- 缺少待比较的两颗行星时停止。
- 本条只给自然强弱的相对次序，没有分值，要量化必须另查 Naisargika Bal 原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
