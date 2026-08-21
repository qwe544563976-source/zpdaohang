---
method: ch18-v19-21-three-wives
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三位妻子：火星与金星同落七宫，或土星落七宫而上升主落八宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有三位妻子
- 火星金星同落七宫主什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘七宫（Yuvati）内有哪些行星

## 按情况检查的事实

- 火星（Mangal）是否落七宫（Yuvati）
- 金星（Shukra）是否落七宫（Yuvati）
- 土星（Shani）是否落七宫（Yuvati）
- 上升主（Lagn's Lord）是否落八宫（Randhr）

## 依赖方法

- 无

## 执行步骤

### ch18-v19-21-three-wives.step-001

- 动作：取出七宫（Yuvati）内的行星，核对是火星与金星同落七宫，还是土星落七宫而上升主落八宫。
- 适用范围：仅限本命盘七宫（Yuvati）妻子数目主题；原文以「wives」立说，属男命框架；原文第二支由独立的「or, if」引出，故「while the Lord of Lagn is in Randhr」按原文只系于土星那一支，不回补到火星金星那一支。
- 原文最小意思：火星与金星同落七宫，或土星落七宫而上升主落八宫时，命主会有3位妻子。
- 本步骤产出事实：["三位妻子判定"]
- 所需事实：["本盘七宫（Yuvati）内有哪些行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落七宫（Yuvati）"}, {"fact_key": "金星（Shukra）是否落七宫（Yuvati）"}]}, {"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否落七宫（Yuvati）"}, {"fact_key": "上升主（Lagn's Lord）是否落八宫（Randhr）"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, "required_fact_keys": ["火星（Mangal）是否落七宫（Yuvati）", "金星（Shukra）是否落七宫（Yuvati）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落七宫（Yuvati）"}, {"fact_key": "金星（Shukra）是否落七宫（Yuvati）"}]}, "selection_group": "ch18-v19-21-three-wives.step-001:combination", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否落七宫（Yuvati）、金星（Shukra）是否落七宫（Yuvati）。"}, {"when": {"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, "required_fact_keys": ["土星（Shani）是否落七宫（Yuvati）", "上升主（Lagn's Lord）是否落八宫（Randhr）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否落七宫（Yuvati）"}, {"fact_key": "上升主（Lagn's Lord）是否落八宫（Randhr）"}]}, "selection_group": "ch18-v19-21-three-wives.step-001:combination", "stop_condition": "选中该分支后，缺少以下事实即停止：土星（Shani）是否落七宫（Yuvati）、上升主（Lagn's Lord）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断婚期、妻子存殁或婚姻质量。", "不得把「the Lord of Lagn is in Randhr」补进火星与金星那一支。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘七宫（Yuvati）内有哪些行星。
- 缺失即停字段：["本盘七宫（Yuvati）内有哪些行星"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v19-21`｜PDF [34]｜“If Mangal and Shukra are in Yuvati, or, if Shani is Yuvati, while the Lord of Lagn is in Randhr, the native will have 3 wives.”


## 四路查书计划

### 支持路

- If Mangal and Shukra are in Yuvati, or, if Shani is Yuvati, while the Lord of Lagn is in Randhr, the native will have 3 wives
- 火星金星落七宫 土星落七宫 上升主落八宫 三位妻子

### 反例或取消路

- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)
- One will have two wives, if Yuvati Lord is in fall, or in a malefic Rashi along with a malefic

### 适用边界路

- There will be many wives, if Shukra is in a Dual Rāśi, while its Lord is in exaltation
- THREE MARRIAGES Should Chandra be in Yuvati from Shukr, while Budh is in Yuvati from Chandra

### 判断方法路

- PLURALITY OF WIVES 3 wives Yuvati occupants judgment
- 判断妻子数目要看七宫内的行星组合

## 上游问题

- 无

## 停止条件

- 缺少七宫内行星事实时停止。
- 两个组合分支的事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
