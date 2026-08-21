---
method: ch20-v31-food-by-begging
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 靠乞讨取得食物：土星与月亮同落九宫、上升主落陷

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会生计无着
- 土星月亮同落九宫又上升主落陷说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 土星（Shani）是否落九宫（Dharm）
- 月亮（Chandra）是否与土星（Shani）同宫
- 上升主（Lagn's Lord）是否落陷

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v31-food-by-begging.step-001

- 动作：核对土星（Shani）是否落九宫（Dharm）、月亮（Chandra）是否与土星同宫，并核对上升主（Lagn's Lord）是否落陷。
- 适用范围：仅限本命盘九宫（Dharm）生计主题；原文未给时间或上升限定。
- 原文最小意思：土星（Shani）落九宫（Dharm）、月亮（Chandra）与土星同宫、且上升主（Lagn's Lord）落陷时，命主靠乞讨取得食物。
- 本步骤产出事实：["土星月亮同落九宫且上升主落陷主乞讨得食判定"]
- 所需事实：["土星（Shani）是否落九宫（Dharm）", "月亮（Chandra）是否与土星（Shani）同宫", "上升主（Lagn's Lord）是否落陷"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否落九宫（Dharm）"}, {"fact_key": "月亮（Chandra）是否与土星（Shani）同宫"}, {"fact_key": "上升主（Lagn's Lord）是否落陷"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断乞讨发生的年岁或时长。", "不得只凭土星落九宫就下断语，月亮同宫与上升主落陷是原文并列的条件。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星（Shani）是否落九宫（Dharm）、月亮（Chandra）是否与土星（Shani）同宫、上升主（Lagn's Lord）是否落陷。
- 缺失即停字段：["土星（Shani）是否落九宫（Dharm）", "月亮（Chandra）是否与土星（Shani）同宫", "上升主（Lagn's Lord）是否落陷"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v31`｜PDF [38]｜“Should Shani be in Dharm Bhava along with Chandra, as Lagn’s Lord is in fall, the native will acquire food by begging.”


## 四路查书计划

### 支持路

- Should Shani be in Dharm Bhava along with Chandra, as Lagn’s Lord is in fall, the native will acquire food by begging.
- 土星落九宫 与月亮同宫 上升主落陷 乞讨取得食物

### 反例或取消路

- One will be fortunate (or affluent), if Dharm’s Lord is in Dharm Bhava with strength
- Abundant fortunes be acquired after the 20<sup>th</sup> year, if Dharm has Guru in it, as its Lord is in an angle from Lagn

### 适用边界路

- If Karm’s Lord and Sahaj’s Lord are bereft of strength, while Dharm’s Lord is in fall, or combust the native will go begging for his food
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

### 判断方法路

- These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava and in other manners as well
- 判断生计困顿要看九宫（Dharm）的占据者与上升主（Lagn's Lord）的状态

## 上游问题

- 无

## 停止条件

- 缺少土星（Shani）落宫事实时停止。
- 缺少月亮（Chandra）与土星是否同宫的事实时停止。
- 缺少上升主（Lagn's Lord）是否落陷的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
