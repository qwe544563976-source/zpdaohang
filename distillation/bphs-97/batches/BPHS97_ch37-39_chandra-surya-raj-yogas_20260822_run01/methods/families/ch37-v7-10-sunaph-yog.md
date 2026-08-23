---
method: ch37-v7-10-sunaph-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Sunaph Yog：太阳以外的行星落月亮起算第2宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有靠自己挣出名堂的组合
- 月亮前一宫有行星说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch37-v7-10-sunaph-yog.step-001

- 动作：核对除太阳（Surya）以外是否有行星落在从月亮（Chandra）起算的第2宫，判定 Sunaph Yog 是否成立。
- 适用范围：仅限本命盘 Sunaph Yog 的成立判定；原文没有时间限定。
- 原文最小意思：除太阳（Surya）外有行星落在从月亮（Chandra）起算的第2宫时，Sunaph Yog 成立。
- 本步骤产出事实：["Sunaph Yog 成立判定"]
- 所需事实：["除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫"]
- 条件关系：{"fact_key": "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只排除太阳，不得再排除别的行星，也不得要求该行星必须是吉星。", "不得把起算点从月亮换成上升。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫。
- 缺失即停字段：["除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v7-10`｜PDF [81]｜“If there is a Grah other than Surya, in the 2<sup>nd</sup> from Chandra, Sunaph Yog is formed”

### ch37-v7-10-sunaph-yog.step-002

- 动作：在 Sunaph Yog 成立时读取身份与财富断语。
- 适用范围：仅限已判定 Sunaph Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：有 Sunaph Yog 者会成为国王，或与国王相当，并有智慧、财富、名声与自己挣来的财富。
- 本步骤产出事实：["Sunaph Yog 效果断语"]
- 所需事实：["Sunaph Yog 成立判定"]
- 条件关系：{"fact_key": "Sunaph Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把国王换算成现代具体职务，也不得据此推断财富数额与发生时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Sunaph Yog 成立判定。
- 缺失即停字段：["Sunaph Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v7-10`｜PDF [81]｜“One with Sunaph Yog will be a king, or equal to a king, endowed with intelligence, wealth, fame and self-earned wealth.”


## 四路查书计划

### 支持路

- If there is a Grah other than Surya, in the 2<sup>nd</sup> from Chandra, Sunaph Yog is formed
- 月亮起算第2宫有行星 Sunaph Yog 自赚财富

### 反例或取消路

- One born in Kema Drum Yog will be very much reproached, will be bereft of intelligence, learning, reduced to penury and perils
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- Should Guru be in a Kendr from Lagna, or from Chandra and be yuti with, or receiving a Drishti from benefic, avoiding at the same time debilitation, combustion and inimical Rāśi, Gaj Kesari Yog is caused

## 上游问题

- 无

## 停止条件

- 缺少月亮起算第2宫占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
