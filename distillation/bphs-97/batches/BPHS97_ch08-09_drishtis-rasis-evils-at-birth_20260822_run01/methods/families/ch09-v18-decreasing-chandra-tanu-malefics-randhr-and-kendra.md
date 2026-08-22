---
method: ch09-v18-decreasing-chandra-tanu-malefics-randhr-and-kendra
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 渐亏的月亮落一宫，凶星占据八宫与一个角宫：早亡

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 渐亏的月亮落一宫怎么断
- 凶星占八宫又占角宫会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）
- 八宫（Randhr Bhava）是否被凶星占据
- 是否有角宫（Kendra）被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v18-decreasing-chandra-tanu-malefics-randhr-and-kendra.step-001

- 动作：核对渐亏的月亮是否落一宫，并核对八宫与角宫是否被凶星占据。
- 适用范围：仅限本命盘出生时的凶象；原文另加一句『此事无疑』的强度语。
- 原文最小意思：渐亏的月亮（decreasing Chandra）落一宫（Tanu Bhava），同时凶星占据八宫（Randhr Bhava）与一个角宫（Kendra）时，命主会被判早亡；此事无疑。
- 本步骤产出事实：["渐亏月亮落一宫的早亡判定"]
- 所需事实：["渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）", "八宫（Randhr Bhava）是否被凶星占据", "是否有角宫（Kendra）被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）"}, {"fact_key": "八宫（Randhr Bhava）是否被凶星占据"}, {"fact_key": "是否有角宫（Kendra）被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『渐亏的月亮』换成一般的月亮。", "不得把『早亡』补成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）、八宫（Randhr Bhava）是否被凶星占据、是否有角宫（Kendra）被凶星占据。
- 缺失即停字段：["渐亏的月亮（decreasing Chandra）是否落一宫（Tanu Bhava）", "八宫（Randhr Bhava）是否被凶星占据", "是否有角宫（Kendra）被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v18`｜PDF [23]｜“Early death will be inflicted on the native, if decreasing Chandra is in Tanu Bhava, while malefics capture Randhr Bhava and a Kendra. There is no doubt about that.”


## 四路查书计划

### 支持路

- Early death will be inflicted on the native, if decreasing Chandra is in Tanu Bhava, while malefics capture Randhr Bhava and a Kendra
- 渐亏月亮 一宫 凶星八宫 角宫 早亡

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Short-life Combinations (up to Sloka 23)

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- 角宫是哪几宫

## 上游问题

- 无

## 停止条件

- 缺少月亮盈亏状态时停止（渐亏与否见第 3 章 decreasing Chandra 的判准）。
- 缺少八宫、角宫的凶星占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
