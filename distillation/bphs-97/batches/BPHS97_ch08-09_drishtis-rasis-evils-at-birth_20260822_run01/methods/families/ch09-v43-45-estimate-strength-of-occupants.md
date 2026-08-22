---
method: ch09-v43-45-estimate-strength-of-occupants
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 对相关占据行星的强弱要作适当估量

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 判断父母之事还要看什么
- 占据行星的强弱要不要考虑

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘相关位次的占据行星（occupants concerned）是哪几颗
- 这些占据行星（occupants concerned）的强弱如何

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v43-45-estimate-strength-of-occupants.step-001

- 动作：取出相关位次的占据行星，估量它们的强弱。
- 适用范围：仅限第 9 章父母一节的收束指示；原文本偈没有给强弱的算法（算法见第 27 章 Shad Bal）。
- 原文最小意思：对相关占据行星（occupants concerned）的强弱与否，应作适当的估量。
- 本步骤产出事实：["相关占据行星的强弱估量结论"]
- 所需事实：["本盘相关位次的占据行星（occupants concerned）是哪几颗", "这些占据行星（occupants concerned）的强弱如何"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘相关位次的占据行星（occupants concerned）是哪几颗"}, {"fact_key": "这些占据行星（occupants concerned）的强弱如何"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自造强弱的算法——原文本偈没有给。", "不得据本句直接下吉凶断语——本句只要求估量强弱。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘相关位次的占据行星（occupants concerned）是哪几颗、这些占据行星（occupants concerned）的强弱如何。
- 缺失即停字段：["本盘相关位次的占据行星（occupants concerned）是哪几颗", "这些占据行星（occupants concerned）的强弱如何"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v43-45`｜PDF [24, 25]｜“The strength, or otherwise of the occupants concerned be suitably estimated.”


## 四路查书计划

### 支持路

- The strength, or otherwise of the occupants concerned be suitably estimated
- 占据行星 强弱 估量

### 反例或取消路

- 无

### 适用边界路

- Parents
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Evil to Father (up to Sloka 42)

### 判断方法路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Evils at Birth
- 行星强弱怎么算

## 上游问题

- 无

## 停止条件

- 强弱的算法原文本偈未给，须另查第 27 章 Shad Bal；该事实取不到值时停止。
- 未指明要估量哪几颗占据行星时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
