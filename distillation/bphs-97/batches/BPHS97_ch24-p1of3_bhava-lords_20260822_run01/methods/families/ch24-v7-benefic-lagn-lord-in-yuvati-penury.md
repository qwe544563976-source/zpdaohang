---
method: ch24-v7-benefic-lagn-lord-in-yuvati-penury
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 吉星上升主落七宫：漫无目的地漂泊、陷入贫困并沮丧

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我为什么总是四处奔波还没积蓄
- 我这辈子会不会一直不得志

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 上升主（Lagn's Lord）是否被判为吉星
- 上升主（Lagn's Lord）是否落七宫（Yuvati）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v7-benefic-lagn-lord-in-yuvati-penury.step-001

- 动作：先确定本盘吉星名册，再核对上升主（Lagn's Lord）本身是否为吉星、是否落七宫（Yuvati）。
- 适用范围：仅限本命盘上升主落七宫（Yuvati Bhava）且本身为吉星一条；本条条件出自同偈第二句「If the Grah in question is a benefic」，其中「the Grah」承同偈第一句所说的上升主（落七宫），为不让指代落空，第一句一并作为逐字短引给出，但第一句的凶星断语另立方法、不属本条；同偈还给出「有力则转而成为国王」的择一断语，也另立方法；原文未给时间限定。
- 原文最小意思：上升主（Lagn's Lord）是吉星且落七宫（Yuvati）时，本人漫无目的地漂泊、陷入贫困并沮丧。
- 本步骤产出事实：["吉星上升主落七宫的漂泊贫困判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "上升主（Lagn's Lord）是否被判为吉星", "上升主（Lagn's Lord）是否落七宫（Yuvati）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "上升主（Lagn's Lord）是否被判为吉星"}, {"fact_key": "上升主（Lagn's Lord）是否落七宫（Yuvati）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断漂泊的地点、贫困的程度或起止时间。", "不得把本条与同偈「有力则转而成为国王」一条同时下断——原文写的是择一。", "不得把本条套用到凶星上升主落七宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、上升主（Lagn's Lord）是否被判为吉星、上升主（Lagn's Lord）是否落七宫（Yuvati）。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "上升主（Lagn's Lord）是否被判为吉星", "上升主（Lagn's Lord）是否落七宫（Yuvati）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v7`｜PDF [41]｜“If Lagn’s Lord is a malefic and is placed in Yuvati Bhava, the natives wife will not live (long). If the Grah in question is a benefic, one will wander aimlessly, face penury and be dejected.”


## 四路查书计划

### 支持路

- If the Grah in question is a benefic, one will wander aimlessly, face penury and be dejected
- 吉星上升主 落七宫 漂泊 贫困 沮丧

### 反例或取消路

- He will alternatively become a king (if the said Grah is strong)
- Should Yuvati Lord be endowed with strength and be yuti with, or be drishtied by a benefic, the native will be wealthy, honourable, happy and fortunate

### 适用边界路

- Indications of Yuvati Bhava. Wife, travel, trade, loss of sight, death etc. be known from Yuvati Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Effects of Yuvati’s Lord in Various Bhavas
- Effects of Lagn’s Lord in Various Bhavas

## 上游问题

- 无

## 停止条件

- 缺少上升主是否落七宫的事实时停止。
- 吉星名册未确定时停止。
- 缺少上升主本身是否为吉星的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
