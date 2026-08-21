---
method: ch36-v35-36-hara-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Hara Yog：从七宫主所落星座起算的第4、第9、第8个星座被吉星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子过得顺不顺、有没有财富和子女
- 我的婚姻宫位配置对整体运势有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 从七宫主（Yuvati's Lord）所落星座起算的第4个星座是否被吉星占据
- 从七宫主（Yuvati's Lord）所落星座起算的第9个星座是否被吉星占据
- 从七宫主（Yuvati's Lord）所落星座起算的第8个星座是否被吉星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch36-v35-36-hara-yog.step-001

- 动作：以七宫主（Yuvati's Lord）所落星座为起点，核对第4、第9与第8个星座是否都被吉星占据。
- 适用范围：仅限本命盘 Hara Yog 的成立与效果；原文起点写的是七宫主所占的星座（Rāśi），不是七宫本身。原文把 Hari、Hara、Brahma 三个 Yog 写在同一偈，并共用同一句结果（One born in anyone of the said three Yogas…），三者互斥独立，本方法只取其中一个；另两个各自成方法。原文未给上升限定，也未给时间限定。
- 原文最小意思：以七宫主（Yuvati's Lord）所落星座（Rāśi）为起点，第4、第9与第8个星座都被吉星占据时，成立 Hara Yog；原文说生于所说三个 Yoga 之一者会快乐、有学问、拥有财富与子女。
- 本步骤产出事实：["Hara Yog 成立判定"]
- 所需事实：["从七宫主（Yuvati's Lord）所落星座起算的第4个星座是否被吉星占据", "从七宫主（Yuvati's Lord）所落星座起算的第9个星座是否被吉星占据", "从七宫主（Yuvati's Lord）所落星座起算的第8个星座是否被吉星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "从七宫主（Yuvati's Lord）所落星座起算的第4个星座是否被吉星占据"}, {"fact_key": "从七宫主（Yuvati's Lord）所落星座起算的第9个星座是否被吉星占据"}, {"fact_key": "从七宫主（Yuvati's Lord）所落星座起算的第8个星座是否被吉星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把起点从七宫主所落星座改成七宫或上升。", "不得据此推断配偶情况、子女数目或财富数额。", "不得把 Hari Yog、Brahma Yog 的位置条件混进本方法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：从七宫主（Yuvati's Lord）所落星座起算的第4个星座是否被吉星占据、从七宫主（Yuvati's Lord）所落星座起算的第9个星座是否被吉星占据、从七宫主（Yuvati's Lord）所落星座起算的第8个星座是否被吉星占据。
- 缺失即停字段：["从七宫主（Yuvati's Lord）所落星座起算的第4个星座是否被吉星占据", "从七宫主（Yuvati's Lord）所落星座起算的第9个星座是否被吉星占据", "从七宫主（Yuvati's Lord）所落星座起算的第8个星座是否被吉星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v35-36`｜PDF [80, 81]｜“If the 4<sup>th</sup> , 9<sup>th</sup> and 8<sup>th</sup> with reference to the Rāśi, occupied by Yuvati’s Lord, are occupied by benefics, Hara Yog is obtainable.”
  - `bphs-97:santhanam:ch36:v35-36`｜PDF [80, 81]｜“One born in anyone of the said three Yogas will be happy, learned and endowed with wealth and sons.”


## 四路查书计划

### 支持路

- If the 4th, 9th and 8th with reference to the Rāśi, occupied by Yuvati’s Lord, are occupied by benefics, Hara Yog
- Hara Yog 七宫主所落星座 第4 第9 第8 吉星

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Ari Bhava, while Ari’s Lord is in Lagna, yuti with, or receiving a Drishti from a Marak Lord
- The Bhava, which is not drishtied by its Lord, or, whose Lord is with a malefic Grah, or with one of the Lords of evil and such other Bhavas

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 判断方法路

- Indications of Yuvati Bhava. Wife, travel, trade, loss of sight, death etc. be known from Yuvati Bhava
- Prosperity, or Annihilation of a Bhava. Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic

## 上游问题

- 无

## 停止条件

- 缺少从七宫主所落星座起算的第4、第9或第8个星座吉星占据事实时停止。
- 七宫主所落星座未知时停止。
- 吉星名册未按本书 ch03:v11 取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
