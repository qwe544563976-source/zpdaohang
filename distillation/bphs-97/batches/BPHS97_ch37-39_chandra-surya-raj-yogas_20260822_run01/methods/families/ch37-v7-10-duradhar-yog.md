---
method: ch37-v7-10-duradhar-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Duradhar Yog：太阳以外的行星同时落月亮起算第2宫与第12宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能不能过得享受又有排场
- 月亮两侧都有行星说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫
- 除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第12宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch37-v7-10-duradhar-yog.step-001

- 动作：核对除太阳（Surya）以外是否有行星同时落在从月亮（Chandra）起算的第2宫与第12宫，判定 Duradhar Yog 是否成立。
- 适用范围：仅限本命盘 Duradhar Yog 的成立判定；原文此分句承同偈前句的 a Grah other than Surya；原文没有时间限定。
- 原文最小意思：除太阳（Surya）外有行星落在从月亮（Chandra）起算的第2宫与第12宫时，Duradhar Yog 成立。
- 本步骤产出事实：["Duradhar Yog 成立判定"]
- 所需事实：["除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫", "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第12宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫"}, {"fact_key": "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第12宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只排除太阳，不得再排除别的行星，也不得要求该行星必须是吉星。", "不得把起算点从月亮换成上升。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫、除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第12宫。
- 缺失即停字段：["除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫", "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第12宫"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v7-10`｜PDF [81]｜“If there is a Grah other than Surya”
  - `bphs-97:santhanam:ch37:v7-10`｜PDF [81]｜“if in the 2<sup>nd</sup> and 12<sup>th</sup> from Chandra, Duradhar Yog is caused.”

### ch37-v7-10-duradhar-yog.step-002

- 动作：在 Duradhar Yog 成立时读取享受、施舍与仆从断语。
- 适用范围：仅限已判定 Duradhar Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：生于 Duradhar Yog 者会享有欢乐、乐善好施，并有财富、车乘与出色的仆从。
- 本步骤产出事实：["Duradhar Yog 效果断语"]
- 所需事实：["Duradhar Yog 成立判定"]
- 条件关系：{"fact_key": "Duradhar Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、车辆数量或仆从人数。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Duradhar Yog 成立判定。
- 缺失即停字段：["Duradhar Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v7-10`｜PDF [81]｜“One born in Duradhar Yog will enjoy pleasures, will be charitable and endowed with wealth, conveyances and excellent serving force.”


## 四路查书计划

### 支持路

- if in the 2<sup>nd</sup> and 12<sup>th</sup> from Chandra, Duradhar Yog is caused
- 月亮起算第2宫第12宫都有行星 Duradhar Yog

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

- 缺少月亮起算第2宫或第12宫的占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
