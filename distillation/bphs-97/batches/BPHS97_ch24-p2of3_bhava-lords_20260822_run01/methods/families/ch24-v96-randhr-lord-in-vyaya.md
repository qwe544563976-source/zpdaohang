---
method: ch24-v96-randhr-lord-in-vyaya
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 八宫主落十二宫：花费于恶行、寿短；同宫另有凶星则更甚

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的钱都花在什么地方
- 我的寿元会不会偏短

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫主（Randhr's Lord）是否落十二宫（Vyaya）
- 本盘中哪些行星被判为凶星
- 十二宫（Vyaya）内除八宫主（Randhr's Lord）外是否另有凶星

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v96-randhr-lord-in-vyaya.step-001

- 动作：核对八宫主（Randhr's Lord）是否落十二宫（Vyaya Bhava），据此判断本人的花费去向与寿命长短。
- 适用范围：仅限本命盘八宫主落十二宫（Vyaya Bhava）一条；本段原文自标「Effects of Randhr’s Lord in Various Bhavas (up to Sloka 96)」；原文未给寿数年份或花费金额。
- 原文最小意思：八宫主（Randhr's Lord）落十二宫（Vyaya Bhava）时，本人会把钱花在恶行上，并且寿命短促。
- 本步骤产出事实：["八宫主落十二宫的花费与寿命判定"]
- 所需事实：["八宫主（Randhr's Lord）是否落十二宫（Vyaya）"]
- 条件关系：{"fact_key": "八宫主（Randhr's Lord）是否落十二宫（Vyaya）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「寿命短促」换算成具体岁数或死亡年份。", "不得据此推断花费的金额、对象或时间。", "不得把本条套用到八宫主落其他宫位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否落十二宫（Vyaya）。
- 缺失即停字段：["八宫主（Randhr's Lord）是否落十二宫（Vyaya）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v96`｜PDF [47]｜“If Randhr’s Lord is in Vyaya Bhava, the native will spend on evil deeds and will incur a short life.”

### ch24-v96-randhr-lord-in-vyaya.step-002

- 动作：在上一步已成立的前提下，再确定本盘凶星名册，核对十二宫（Vyaya Bhava）中除八宫主外是否另有凶星，据此判断上述结果是否更甚。
- 适用范围：仅限承接上一步、八宫主已落十二宫（Vyaya Bhava）的盘；原文用 the said Bhava 承同偈前句的十二宫，逐字短引已把整偈一并给出；原文只说 More so，未说明加重到什么程度；本段原文自标「Effects of Randhr’s Lord in Various Bhavas (up to Sloka 96)」；原文未给时间限定。
- 原文最小意思：八宫主（Randhr's Lord）落十二宫（Vyaya Bhava）的前提下，十二宫（Vyaya Bhava）中另有凶星时，上述结果更甚。
- 本步骤产出事实：["八宫主落十二宫再加凶星的加重判定"]
- 所需事实：["八宫主（Randhr's Lord）是否落十二宫（Vyaya）", "本盘中哪些行星被判为凶星", "十二宫（Vyaya）内除八宫主（Randhr's Lord）外是否另有凶星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落十二宫（Vyaya）"}, {"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "十二宫（Vyaya）内除八宫主（Randhr's Lord）外是否另有凶星"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「更甚」量化成具体倍数、年数或程度等级。", "不得在没有第二颗凶星时使用本步的加重结论。", "不得把本步的加重条件读成上一步结论成立的必要前提。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否落十二宫（Vyaya）、本盘中哪些行星被判为凶星、十二宫（Vyaya）内除八宫主（Randhr's Lord）外是否另有凶星。
- 缺失即停字段：["八宫主（Randhr's Lord）是否落十二宫（Vyaya）", "本盘中哪些行星被判为凶星", "十二宫（Vyaya）内除八宫主（Randhr's Lord）外是否另有凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v96`｜PDF [47]｜“If Randhr’s Lord is in Vyaya Bhava, the native will spend on evil deeds and will incur a short life. More so, if there be additionally a malefic in the said Bhava.”


## 四路查书计划

### 支持路

- If Randhr’s Lord is in Vyaya Bhava, the native will spend on evil deeds and will incur a short life
- 八宫主落十二宫 花费恶行 寿短 另有凶星更甚

### 反例或取消路

- If Randhr’s Lord is in an angle, long life is indicated
- There will be expenses on good accounts, if Vyaya’s Lord is with a benefic, or in his own Bhava, or exalted, or, if a benefic occupies Vyaya

### 适用边界路

- Indications of Randhr Bhava. Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead and things, that have happened and are to happen
- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Effects of Randhr’s Lord in Various Bhavas
- Effects of Vyaya’s Lord in Various Bhavas

## 上游问题

- 无

## 停止条件

- 缺少八宫主是否落十二宫的事实时停止。
- 判断加重一步时，缺少十二宫内是否另有凶星的事实即停止。
- 凶星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
