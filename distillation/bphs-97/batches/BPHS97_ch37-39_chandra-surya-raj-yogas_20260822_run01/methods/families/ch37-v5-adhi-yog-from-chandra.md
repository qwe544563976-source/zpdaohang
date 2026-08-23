---
method: ch37-v5-adhi-yog-from-chandra
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮起算的 Adhi Yog：8、6、7 宫皆吉星，按力量得王、大臣或军队统帅

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有当官掌权的组合
- 我命里的贵格是什么水平

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 从月亮（Chandra）起算的第8宫是否被吉星占据
- 从月亮（Chandra）起算的第6宫是否被吉星占据
- 从月亮（Chandra）起算的第7宫是否被吉星占据
- 参与 Adhi Yog 的行星力量如何

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch37-v5-adhi-yog-from-chandra.step-001

- 动作：先取本盘吉星名册，再核对从月亮（Chandra）起算的第8、第6、第7宫是否都被吉星占据，判定 Adhi Yog 是否成立。
- 适用范围：仅限本命盘 Adhi Yog 的成立判定；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：吉星占据从月亮（Chandra）起算的第8、第6与第7宫时，Adhi Yog 成立。
- 本步骤产出事实：["Adhi Yog 成立判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "从月亮（Chandra）起算的第8宫是否被吉星占据", "从月亮（Chandra）起算的第6宫是否被吉星占据", "从月亮（Chandra）起算的第7宫是否被吉星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "从月亮（Chandra）起算的第8宫是否被吉星占据"}, {"fact_key": "从月亮（Chandra）起算的第6宫是否被吉星占据"}, {"fact_key": "从月亮（Chandra）起算的第7宫是否被吉星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文本句只写从月亮起算的第8、6、7 宫，不得改成从上升起算，也不得增减宫位。", "不得据此推断官职级别、任职时间或收入。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、从月亮（Chandra）起算的第8宫是否被吉星占据、从月亮（Chandra）起算的第6宫是否被吉星占据、从月亮（Chandra）起算的第7宫是否被吉星占据。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "从月亮（Chandra）起算的第8宫是否被吉星占据", "从月亮（Chandra）起算的第6宫是否被吉星占据", "从月亮（Chandra）起算的第7宫是否被吉星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v5`｜PDF [81]｜“If benefics occupy the 8<sup>th</sup> , 6<sup>th</sup> and 7<sup>th</sup> , counted from Chandra, Adhi Yog obtains.”

### ch37-v5-adhi-yog-from-chandra.step-002

- 动作：在 Adhi Yog 成立时，按参与行星的力量读取身份断语。
- 适用范围：仅限已判定 Adhi Yog 成立的本命盘；原文只说按参与行星的力量分为三种身份，既未给出力量的判准，也未说明哪一档力量对应哪一种身份。
- 原文最小意思：Adhi Yog 成立时，按参与行星的力量，命主会成为国王、大臣或军队统帅之一。
- 本步骤产出事实：["Adhi Yog 身份档次断语"]
- 所需事实：["Adhi Yog 成立判定", "参与 Adhi Yog 的行星力量如何"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "Adhi Yog 成立判定"}, {"fact_key": "参与 Adhi Yog 的行星力量如何"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文未给出力量与三种身份的对应关系，不得自行指定哪一档力量对应哪一种身份。", "不得把国王、大臣、军队统帅换算成现代具体职务。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Adhi Yog 成立判定、参与 Adhi Yog 的行星力量如何。
- 缺失即停字段：["Adhi Yog 成立判定", "参与 Adhi Yog 的行星力量如何"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v5`｜PDF [81]｜“According to the strength of the participating Grahas, the native concerned will be either a king, or a minister, or an Army chief.”


## 四路查书计划

### 支持路

- If benefics occupy the 8<sup>th</sup> , 6<sup>th</sup> and 7<sup>th</sup> , counted from Chandra, Adhi Yog obtains
- 月亮起算 8 6 7 宫吉星 Adhi Yog 国王大臣军队统帅

### 反例或取消路

- One born in Kema Drum Yog will be very much reproached, will be bereft of intelligence, learning, reduced to penury and perils
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Budh, however, is a malefic, if he joins a malefic

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn

## 上游问题

- 无

## 停止条件

- 缺少本盘吉星名册事实时停止。
- 从月亮起算的第8、6、7 宫占据事实缺任一项时停止。
- 原文未给出参与行星力量的判准与身份对应关系，力量未确定即停判于身份档次。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
