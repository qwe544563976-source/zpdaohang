---
method: ch37-v11-13-kema-drum-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Kema Drum Yog：月亮四处皆空（同宫、第2宫、第12宫、上升角宫都无行星）

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我为什么老是被人指责又一无所有
- 我盘里月亮孤零零的说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 除太阳（Surya）外是否有行星与月亮（Chandra）同宫
- 除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫
- 除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第12宫
- 除太阳（Surya）外是否有行星落在从上升（Lagna）起算的角宫（Kendr）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch37-v11-13-kema-drum-yog.step-001

- 动作：除太阳（Surya）外，逐一核对月亮（Chandra）同宫、从月亮起算的第2宫与第12宫、以及从上升（Lagna）起算的角宫内是否都没有行星，判定 Kema Drum Yog 是否成立。
- 适用范围：仅限本命盘 Kema Drum Yog 的成立判定；原文没有时间限定。
- 原文最小意思：除太阳（Surya）外没有行星与月亮（Chandra）同宫，从月亮（Chandra）起算的第2宫内没有行星，从月亮（Chandra）起算的第12宫内没有行星，从上升（Lagna）起算的角宫（Kendr）内也没有行星时，Kema Drum Yog 成立。
- 本步骤产出事实：["Kema Drum Yog 成立判定"]
- 所需事实：["除太阳（Surya）外是否有行星与月亮（Chandra）同宫", "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫", "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第12宫", "除太阳（Surya）外是否有行星落在从上升（Lagna）起算的角宫（Kendr）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "除太阳（Surya）外是否有行星与月亮（Chandra）同宫"}]}, {"operator": "NOT", "operands": [{"fact_key": "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫"}]}, {"operator": "NOT", "operands": [{"fact_key": "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第12宫"}]}, {"operator": "NOT", "operands": [{"fact_key": "除太阳（Surya）外是否有行星落在从上升（Lagna）起算的角宫（Kendr）"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文的四处空位是并列要求，不得只满足其中一处就判定成立。", "原文只排除太阳，不得再排除别的行星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：除太阳（Surya）外是否有行星与月亮（Chandra）同宫、除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫、除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第12宫、除太阳（Surya）外是否有行星落在从上升（Lagna）起算的角宫（Kendr）。
- 缺失即停字段：["除太阳（Surya）外是否有行星与月亮（Chandra）同宫", "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第2宫", "除太阳（Surya）外是否有行星落在从月亮（Chandra）起算的第12宫", "除太阳（Surya）外是否有行星落在从上升（Lagna）起算的角宫（Kendr）"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v11-13`｜PDF [81, 82]｜“Excluding Surya, should there be no Grah with Chandra”
  - `bphs-97:santhanam:ch37:v11-13`｜PDF [81, 82]｜“in the 2<sup>nd</sup>”
  - `bphs-97:santhanam:ch37:v11-13`｜PDF [81, 82]｜“12<sup>th</sup> from Chandra”
  - `bphs-97:santhanam:ch37:v11-13`｜PDF [81, 82]｜“in a Kendr from Lagna, Kema Drum Yog is formed”

### ch37-v11-13-kema-drum-yog.step-002

- 动作：在 Kema Drum Yog 成立时读取名声、才学与处境断语。
- 适用范围：仅限已判定 Kema Drum Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：生于 Kema Drum Yog 者会大受指责，没有智慧与学识，陷入贫困与危难。
- 本步骤产出事实：["Kema Drum Yog 效果断语"]
- 所需事实：["Kema Drum Yog 成立判定"]
- 条件关系：{"fact_key": "Kema Drum Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「陷入贫困与危难」加重成寿命或死因断语。", "不得据此推断贫困发生的时间或程度数值。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Kema Drum Yog 成立判定。
- 缺失即停字段：["Kema Drum Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v11-13`｜PDF [81, 82]｜“One born in Kema Drum Yog will be very much reproached, will be bereft of intelligence, learning, reduced to penury and perils.”


## 四路查书计划

### 支持路

- Excluding Surya, should there be no Grah with Chandra
- One born in Kema Drum Yog will be very much reproached, will be bereft of intelligence, learning, reduced to penury and perils
- 月亮四处无行星 Kema Drum Yog 贫困

### 反例或取消路

- If there is a Grah other than Surya, in the 2<sup>nd</sup> from Chandra, Sunaph Yog is formed
- If benefics occupy the 8<sup>th</sup> , 6<sup>th</sup> and 7<sup>th</sup> , counted from Chandra, Adhi Yog obtains

### 适用边界路

- If malefics be in Karakāńś, Arudh Lagn and the 2<sup>nd</sup> and 8<sup>th</sup> from these places, there will be Kemadrum Yog
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- Should Guru be in a Kendr from Lagna, or from Chandra and be yuti with, or receiving a Drishti from benefic, avoiding at the same time debilitation, combustion and inimical Rāśi, Gaj Kesari Yog is caused

## 上游问题

- 无

## 停止条件

- 月亮同宫、第2宫、第12宫、上升角宫四项占据事实缺任一项时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
