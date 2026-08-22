---
method: ch24-v95-randhr-lord-with-benefic-in-labh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 八宫主在十一宫与吉星同宫：长寿

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的寿元厚不厚
- 盘上有没有护住寿命的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 八宫主（Randhr's Lord）是否落十一宫（Labh）
- 八宫主（Randhr's Lord）是否与吉星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v95-randhr-lord-with-benefic-in-labh.step-001

- 动作：先确定本盘吉星名册，再核对八宫主（Randhr's Lord）是否与吉星同宫并落十一宫（Labh Bhava），据此判断寿命长短。
- 适用范围：仅限本命盘八宫主与吉星同宫且落十一宫（Labh Bhava）一条；同偈另有与凶星同处的一条，条件不同不得混用；本段原文自标「Effects of Randhr’s Lord in Various Bhavas (up to Sloka 96)」；原文未给寿数年份。
- 原文最小意思：八宫主（Randhr's Lord）与吉星同宫（yuti with a benefic）、且落十一宫（Labh Bhava）时，本人长寿。
- 本步骤产出事实：["八宫主与吉星同宫落十一宫的寿命判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "八宫主（Randhr's Lord）是否落十一宫（Labh）", "八宫主（Randhr's Lord）是否与吉星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "八宫主（Randhr's Lord）是否落十一宫（Labh）"}, {"fact_key": "八宫主（Randhr's Lord）是否与吉星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「长寿」换算成具体岁数或年份。", "不得把同偈与凶星同处的一条并入本条。", "不得把「与吉星同宫」放宽成相照或其他关系——原文写的是 yuti。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、八宫主（Randhr's Lord）是否落十一宫（Labh）、八宫主（Randhr's Lord）是否与吉星同宫。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "八宫主（Randhr's Lord）是否落十一宫（Labh）", "八宫主（Randhr's Lord）是否与吉星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v95`｜PDF [47]｜“Should Randhr’s Lord be yuti with a benefic and be in Labh Bhava, the native will be long-lived.”


## 四路查书计划

### 支持路

- Should Randhr’s Lord be yuti with a benefic and be in Labh Bhava, the native will be long-lived
- 八宫主落十一宫 与吉星同宫 长寿

### 反例或取消路

- Should Randhr’s Lord join Lagn’s Lord, or a malefic and be in Randhr itself, the native will be short lived

### 适用边界路

- Indications of Randhr Bhava. Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead and things, that have happened and are to happen
- Indications of Labh Bhava. All articles, son’s wife, income, prosperity, quadrupeds etc. are to be understood from Labh Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Effects of Randhr’s Lord in Various Bhavas
- Effects of Randhr Bhava

## 上游问题

- 无

## 停止条件

- 缺少八宫主是否落十一宫的事实时停止。
- 缺少八宫主是否与吉星同宫的事实时停止。
- 吉星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
