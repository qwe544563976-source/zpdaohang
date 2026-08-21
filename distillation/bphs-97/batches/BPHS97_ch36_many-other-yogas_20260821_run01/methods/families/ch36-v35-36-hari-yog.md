---
method: ch36-v35-36-hari-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Hari Yog：从二宫主起算的第2、第12、第8位被吉星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子过得顺不顺、有没有财富和子女
- 我的学问怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 从二宫主（Dhan's Lord）所落宫起算的第2宫是否被吉星占据
- 从二宫主（Dhan's Lord）所落宫起算的第12宫是否被吉星占据
- 从二宫主（Dhan's Lord）所落宫起算的第8宫是否被吉星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch36-v35-36-hari-yog.step-001

- 动作：以二宫主（Dhan's Lord）所落之处为起点，核对第2、第12与第8位是否都被吉星占据。
- 适用范围：仅限本命盘 Hari Yog 的成立与效果；起点是二宫主所落之处，不是上升。原文把 Hari、Hara、Brahma 三个 Yog 写在同一偈，并共用同一句结果（One born in anyone of the said three Yogas…），三者互斥独立，本方法只取其中一个；另两个各自成方法。原文未给上升限定，也未给时间限定。
- 原文最小意思：从二宫主（Dhan's Lord）所落之处起算，第2宫、第12宫与第8宫都被吉星占据时，成立 Hari Yog；原文说生于所说三个 Yoga 之一者会快乐、有学问、拥有财富与子女。
- 本步骤产出事实：["Hari Yog 成立判定"]
- 所需事实：["从二宫主（Dhan's Lord）所落宫起算的第2宫是否被吉星占据", "从二宫主（Dhan's Lord）所落宫起算的第12宫是否被吉星占据", "从二宫主（Dhan's Lord）所落宫起算的第8宫是否被吉星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "从二宫主（Dhan's Lord）所落宫起算的第2宫是否被吉星占据"}, {"fact_key": "从二宫主（Dhan's Lord）所落宫起算的第12宫是否被吉星占据"}, {"fact_key": "从二宫主（Dhan's Lord）所落宫起算的第8宫是否被吉星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把起点从二宫主改成上升或二宫本身。", "不得据此推断子女数目或财富数额。", "不得把 Hara Yog、Brahma Yog 的位置条件混进本方法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：从二宫主（Dhan's Lord）所落宫起算的第2宫是否被吉星占据、从二宫主（Dhan's Lord）所落宫起算的第12宫是否被吉星占据、从二宫主（Dhan's Lord）所落宫起算的第8宫是否被吉星占据。
- 缺失即停字段：["从二宫主（Dhan's Lord）所落宫起算的第2宫是否被吉星占据", "从二宫主（Dhan's Lord）所落宫起算的第12宫是否被吉星占据", "从二宫主（Dhan's Lord）所落宫起算的第8宫是否被吉星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v35-36`｜PDF [80, 81]｜“Counted from Dhan’s Lord, if benefics occupy the 2<sup>nd</sup> , 12<sup>th</sup> and 8<sup>th</sup> , Hari Yog is formed.”
  - `bphs-97:santhanam:ch36:v35-36`｜PDF [80, 81]｜“One born in anyone of the said three Yogas will be happy, learned and endowed with wealth and sons.”


## 四路查书计划

### 支持路

- Trimurthi Yogas. Counted from Dhan’s Lord, if benefics occupy the 2nd, 12th and 8th, Hari Yog is formed
- Hari Yog 从二宫主起算 第2 第12 第8 吉星

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- The Bhava, which is not drishtied by its Lord, or, whose Lord is with a malefic Grah, or with one of the Lords of evil and such other Bhavas

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 判断方法路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- Prosperity, or Annihilation of a Bhava. Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic

## 上游问题

- 无

## 停止条件

- 缺少从二宫主起算的第2、第12或第8位吉星占据事实时停止。
- 二宫主落宫未知时停止。
- 吉星名册未按本书 ch03:v11 取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
