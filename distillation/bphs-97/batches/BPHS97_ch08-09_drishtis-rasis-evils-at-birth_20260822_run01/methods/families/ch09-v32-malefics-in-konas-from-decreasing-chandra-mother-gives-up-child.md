---
method: ch09-v32-malefics-in-konas-from-decreasing-chandra-mother-gives-up-child
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 自渐亏月亮起的三角宫有凶星且不与吉星同宫：母亲会舍弃孩子

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 母亲会不会舍弃孩子
- 自月亮起三角宫有凶星怎么断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 自渐亏的月亮（decreasing Chandra）起算的三角宫（Konas）内是否有凶星
- 这些凶星是否与吉星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v32-malefics-in-konas-from-decreasing-chandra-mother-gives-up-child.step-001

- 动作：核对自渐亏月亮起算的三角宫内有无凶星，并核对这些凶星有无吉星同宫。
- 适用范围：仅限本命盘对母子关系的判断；原文另加『无疑』的强度语。
- 原文最小意思：自渐亏的月亮（decreasing Chandra）起算的三角宫（Konas）内有凶星，且没有吉星与这些凶星同宫时，母亲无疑会舍弃孩子。
- 本步骤产出事实：["自渐亏月亮起三角宫受克的母子分离判定"]
- 所需事实：["自渐亏的月亮（decreasing Chandra）起算的三角宫（Konas）内是否有凶星", "这些凶星是否与吉星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "自渐亏的月亮（decreasing Chandra）起算的三角宫（Konas）内是否有凶星"}, {"operator": "NOT", "operands": [{"fact_key": "这些凶星是否与吉星同宫"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『舍弃孩子』改写成母亲去世。", "不得把三角宫（Konas）的起算点从渐亏的月亮换成上升。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：自渐亏的月亮（decreasing Chandra）起算的三角宫（Konas）内是否有凶星、这些凶星是否与吉星同宫。
- 缺失即停字段：["自渐亏的月亮（decreasing Chandra）起算的三角宫（Konas）内是否有凶星", "这些凶星是否与吉星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v32`｜PDF [24]｜“Doubtlessly the mother will give up the child, if it has malefics in Konas, counted from the decreasing Chandra. No benefic shall be yuti with the said malefics.”


## 四路查书计划

### 支持路

- Doubtlessly the mother will give up the child, if it has malefics in Konas, counted from the decreasing Chandra
- 渐亏月亮 三角宫 凶星 母亲舍弃孩子

### 反例或取消路

- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evils to Mother (up to Sloka 33)
- Putr and Dharm Bhava are known by the name Kon (or trine)
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.

### 判断方法路

- Evils at Birth
- Putr and Dharm Bhava are known by the name Kon (or trine)
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 三角宫是哪几宫

## 上游问题

- 无

## 停止条件

- 缺少月亮盈亏状态时停止。
- 缺少自月亮起算三角宫的占据者事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
