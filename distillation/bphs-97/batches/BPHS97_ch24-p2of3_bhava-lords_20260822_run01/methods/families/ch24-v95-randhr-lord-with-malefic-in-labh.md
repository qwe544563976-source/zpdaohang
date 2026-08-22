---
method: ch24-v95-randhr-lord-with-malefic-in-labh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 八宫主与凶星同处十一宫：没有财富、少年困苦而日后转乐

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我小时候为什么这么苦
- 我的日子什么时候能转好

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星
- 八宫主（Randhr's Lord）是否落十一宫（Labh）
- 八宫主（Randhr's Lord）是否与凶星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v95-randhr-lord-with-malefic-in-labh.step-001

- 动作：先确定本盘凶星名册，再核对八宫主（Randhr's Lord）是否与凶星同处十一宫（Labh Bhava），据此判断本人的财富与前后境遇。
- 适用范围：仅限本命盘八宫主与凶星同处十一宫（Labh Bhava）一条；同偈另有与吉星同宫的一条，条件不同不得混用；原文把境遇分为少年时与其后两段，未给具体年份；本段原文自标「Effects of Randhr’s Lord in Various Bhavas (up to Sloka 96)」；原文未给财富数额。
- 原文最小意思：八宫主（Randhr's Lord）与凶星同处（along with a malefic）、落十一宫（Labh Bhava）时，本人没有财富，少年时困苦，日后转为快乐。
- 本步骤产出事实：["八宫主与凶星同处十一宫的财富与境遇判定"]
- 所需事实：["本盘中哪些行星被判为凶星", "八宫主（Randhr's Lord）是否落十一宫（Labh）", "八宫主（Randhr's Lord）是否与凶星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "八宫主（Randhr's Lord）是否落十一宫（Labh）"}, {"fact_key": "八宫主（Randhr's Lord）是否与凶星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得给「少年时」与「日后」补上具体年龄或年份——原文没有给。", "不得把「没有财富」换算成具体数额或贫困等级。", "不得把同偈与吉星同宫的一条并入本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星、八宫主（Randhr's Lord）是否落十一宫（Labh）、八宫主（Randhr's Lord）是否与凶星同宫。
- 缺失即停字段：["本盘中哪些行星被判为凶星", "八宫主（Randhr's Lord）是否落十一宫（Labh）", "八宫主（Randhr's Lord）是否与凶星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v95`｜PDF [47]｜“If Randhr’s Lord along with a malefic is in Labh Bhava, the native will be devoid of wealth and will be miserable in boyhood, but happy later on.”


## 四路查书计划

### 支持路

- If Randhr’s Lord along with a malefic is in Labh Bhava, the native will be devoid of wealth and will be miserable in boyhood
- 八宫主与凶星同处十一宫 没有财富 少年困苦

### 反例或取消路

- I now tell you of special combinations, giving wealth. One born to these Yogas will surely become wealthy

### 适用边界路

- Indications of Randhr Bhava. Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead and things, that have happened and are to happen
- Indications of Labh Bhava. All articles, son’s wife, income, prosperity, quadrupeds etc. are to be understood from Labh Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Effects of Randhr’s Lord in Various Bhavas
- Effects of Labh’s Lord in Various Bhavas

## 上游问题

- 无

## 停止条件

- 缺少八宫主是否落十一宫的事实时停止。
- 缺少八宫主是否与凶星同宫的事实时停止。
- 凶星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
