---
method: ch38-v1-ubhayachari-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Ubhayachari Yog：月亮以外的行星同时落太阳起算第2宫与第12宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有贵格
- 太阳两侧都有行星说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第2宫
- 除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第12宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch38-v1-ubhayachari-yog.step-001

- 动作：核对除月亮（Chandra）以外是否有 Mangal 等行星同时落在从太阳（Surya）起算的第2宫与第12宫，判定 Ubhayachari Yog 是否成立。
- 适用范围：仅限本命盘 Ubhayachari Yog 的成立判定；原文此分句承同偈前句的 a Grah among Mangal etc.；原文没有时间限定。
- 原文最小意思：除月亮（Chandra）外的 Mangal 等行星落在从太阳（Surya）起算的第2宫与第12宫时，Ubhayachari Yog 成立。
- 本步骤产出事实：["Ubhayachari Yog 成立判定"]
- 所需事实：["除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第2宫", "除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第12宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第2宫"}, {"fact_key": "除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第12宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只排除月亮，不得再排除别的行星。", "不得把起算点从太阳换成上升或月亮。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第2宫、除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第12宫。
- 缺失即停字段：["除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第2宫", "除月亮（Chandra）外是否有行星落在从太阳（Surya）起算的第12宫"]
- 原文证据：
  - `bphs-97:santhanam:ch38:v1`｜PDF [82]｜“Barring Chandra, if a Grah among Mangal etc.”
  - `bphs-97:santhanam:ch38:v1`｜PDF [82]｜“if in both the 2<sup>nd</sup> and the 12<sup>th</sup> from Surya, Ubhayachari Yog is caused.”

### ch38-v1-ubhayachari-yog.step-002

- 动作：在 Ubhayachari Yog 成立时读取身份与快乐断语。
- 适用范围：仅限已判定 Ubhayachari Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：有 Ubhayachari Yog 的命主会成为国王，或与国王相当，并且快乐。
- 本步骤产出事实：["Ubhayachari Yog 效果断语"]
- 所需事实：["Ubhayachari Yog 成立判定"]
- 条件关系：{"fact_key": "Ubhayachari Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把国王换算成现代具体职务，也不得据此推断登位时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Ubhayachari Yog 成立判定。
- 缺失即停字段：["Ubhayachari Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch38:v2-3`｜PDF [82]｜“The Ubhayachari native will be a king, or equal to a king and be happy.”


## 四路查书计划

### 支持路

- if in both the 2<sup>nd</sup> and the 12<sup>th</sup> from Surya, Ubhayachari Yog is caused
- The Ubhayachari native will be a king, or equal to a king and be happy
- 太阳两侧都有行星 Ubhayachari Yog 国王

### 反例或取消路

- Benefics, causing Vesi, Vosi, or Ubhayachari Yogas, will give the above-mentioned effects, while malefics will produce contrary effects
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless

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

- 缺少太阳起算第2宫或第12宫的占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
