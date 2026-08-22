---
method: ch24-v91-randhr-lord-yuti-malefic-in-yuvati
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 八宫主在七宫与凶星同宫：事业必定衰落

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的生意会不会垮
- 我事业上的风险在哪里

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星
- 八宫主（Randhr's Lord）是否落七宫（Yuvati）
- 八宫主（Randhr's Lord）是否与凶星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v91-randhr-lord-yuti-malefic-in-yuvati.step-001

- 动作：先确定本盘凶星名册，再核对八宫主（Randhr's Lord）是否落七宫（Yuvati Bhava）并与凶星同宫，据此判断事业的成败。
- 适用范围：仅限本命盘八宫主落七宫（Yuvati Bhava）且与凶星同宫（yuti）一条；同偈前句只讲落七宫、不带凶星条件，两条不得混用；本段原文自标「Effects of Randhr’s Lord in Various Bhavas (up to Sloka 96)」；原文未给衰落的时间、行业或程度。
- 原文最小意思：八宫主（Randhr's Lord）与凶星同宫（yuti with a malefic）、且落七宫（Yuvati Bhava）时，其事业必定衰落。
- 本步骤产出事实：["八宫主落七宫与凶星同宫的事业判定"]
- 所需事实：["本盘中哪些行星被判为凶星", "八宫主（Randhr's Lord）是否落七宫（Yuvati）", "八宫主（Randhr's Lord）是否与凶星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "八宫主（Randhr's Lord）是否落七宫（Yuvati）"}, {"fact_key": "八宫主（Randhr's Lord）是否与凶星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断衰落的时间、行业或损失金额。", "不得把同偈「两位妻子」一条并入本条。", "不得把「与凶星同宫」放宽成相照或其他关系——原文写的是 yuti。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星、八宫主（Randhr's Lord）是否落七宫（Yuvati）、八宫主（Randhr's Lord）是否与凶星同宫。
- 缺失即停字段：["本盘中哪些行星被判为凶星", "八宫主（Randhr's Lord）是否落七宫（Yuvati）", "八宫主（Randhr's Lord）是否与凶星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v91`｜PDF [46]｜“If Randhr’s Lord is yuti with a malefic in Yuvati Bhava, there will surely be downfall in his business.”


## 四路查书计划

### 支持路

- If Randhr’s Lord is yuti with a malefic in Yuvati Bhava, there will surely be downfall in his business
- 八宫主落七宫 与凶星同宫 事业衰落

### 反例或取消路

- I now tell you of special combinations, giving wealth. One born to these Yogas will surely become wealthy

### 适用边界路

- Indications of Randhr Bhava. Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead and things, that have happened and are to happen
- Indications of Yuvati Bhava. Wife, travel, trade, loss of sight, death etc. be known from Yuvati Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Effects of Randhr’s Lord in Various Bhavas
- Effects of Randhr Bhava

## 上游问题

- 无

## 停止条件

- 缺少八宫主是否落七宫的事实时停止。
- 缺少八宫主是否与凶星同宫的事实时停止。
- 凶星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
