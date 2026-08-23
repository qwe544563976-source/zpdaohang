---
method: ch38-v1-vosi-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Vosi Yog：月亮以外的行星落太阳起算第12宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有靠本事和学问出头的组合
- 太阳后一宫有行星说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第12宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch38-v1-vosi-yog.step-001

- 动作：核对除月亮（Chandra）以外是否有 Mangal 等行星落在从太阳（Surya）起算的第12宫，判定 Vosi Yog 是否成立。
- 适用范围：仅限本命盘 Vosi Yog 的成立判定；原文此分句承同偈前句的 a Grah among Mangal etc.；原文没有时间限定。
- 原文最小意思：除月亮（Chandra）外的 Mangal 等行星落在从太阳（Surya）起算的第12宫时，Vosi Yog 成立。
- 本步骤产出事实：["Vosi Yog 成立判定"]
- 所需事实：["除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第12宫"]
- 条件关系：{"fact_key": "除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第12宫"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只排除月亮，不得再排除别的行星。", "不得把起算点从太阳换成上升或月亮。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第12宫。
- 缺失即停字段：["除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第12宫"]
- 原文证据：
  - `bphs-97:santhanam:ch38:v1`｜PDF [82]｜“Barring Chandra, if a Grah among Mangal etc.”
  - `bphs-97:santhanam:ch38:v1`｜PDF [82]｜“if in the 12<sup>th</sup> from Surya, Vosi Yog is formed”

### ch38-v1-vosi-yog.step-002

- 动作：在 Vosi Yog 成立时读取才能、名声与学识断语。
- 适用范围：仅限已判定 Vosi Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：生于 Vosi Yog 者心灵手巧、乐善好施，并有名声、学识与力量。
- 本步骤产出事实：["Vosi Yog 效果断语"]
- 所需事实：["Vosi Yog 成立判定"]
- 条件关系：{"fact_key": "Vosi Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断学历、职业或成名时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Vosi Yog 成立判定。
- 缺失即停字段：["Vosi Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch38:v2-3`｜PDF [82]｜“One born with Vosi Yog will be skilful, charitable and endowed with fame, learning and strength.”


## 四路查书计划

### 支持路

- if in the 12<sup>th</sup> from Surya, Vosi Yog is formed
- One born with Vosi Yog will be skilful, charitable and endowed with fame, learning and strength
- 太阳起算第12宫有行星 Vosi Yog

### 反例或取消路

- Benefics, causing Vesi, Vosi, or Ubhayachari Yogas, will give the above-mentioned effects, while malefics will produce contrary effects
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Budh, however, is a malefic, if he joins a malefic
- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 缺少太阳起算第12宫的占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
