---
method: ch37-v6-dhan-yog-two-benefics
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Dhan Yog：两颗吉星在月亮起算的 3、6、10、11 宫，财富中等

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的财富算中等吗
- 两颗吉星落增长宫是什么水平

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 从月亮（Chandra）起算的增长宫（Upachaya）内有几颗吉星
- 本盘中哪些行星被判为吉星
- 从月亮（Chandra）起算的第3、6、10、11宫内是否有两颗吉星

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch37-v6-dhan-yog-two-benefics.step-001

- 动作：取本盘吉星名册，数从月亮（Chandra）起算的第3、6、10、11 宫内的吉星颗数，核对是否为两颗。
- 适用范围：仅限本命盘财富主题；原文本句未重复起算点，其宫位承同偈前句的 counted from Chandra；原文没有时间限定。
- 原文最小意思：承同偈前句「全部三颗吉星落在从月亮（Chandra）起算的增长宫（Upachaya）」的起算点，若其中的第3、第6、第10与第11宫内有两颗吉星，则命主在财富上得中等效果。
- 本步骤产出事实：["两吉星在增长宫的中等财富判定"]
- 所需事实：["从月亮（Chandra）起算的增长宫（Upachaya）内有几颗吉星", "本盘中哪些行星被判为吉星", "从月亮（Chandra）起算的第3、6、10、11宫内是否有两颗吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "从月亮（Chandra）起算的增长宫（Upachaya）内有几颗吉星"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "从月亮（Chandra）起算的第3、6、10、11宫内是否有两颗吉星"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额或发财时间。", "原文本句只写两颗吉星一档，不得把它与三颗、一颗两档混用。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：从月亮（Chandra）起算的增长宫（Upachaya）内有几颗吉星、本盘中哪些行星被判为吉星、从月亮（Chandra）起算的第3、6、10、11宫内是否有两颗吉星。
- 缺失即停字段：["从月亮（Chandra）起算的增长宫（Upachaya）内有几颗吉星", "本盘中哪些行星被判为吉星", "从月亮（Chandra）起算的第3、6、10、11宫内是否有两颗吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v6`｜PDF [81]｜“Should all the (three) benefics be Upachaya, counted from Chandra, one will be very affluent. With two benefics, placed in the 3<sup>rd</sup> , the 6<sup>th</sup> , the 10<sup>th</sup> and the 11<sup>th</sup> , one will have medium effects in regard to wealth.”


## 四路查书计划

### 支持路

- With two benefics, placed in the 3<sup>rd</sup> , the 6<sup>th</sup> , the 10<sup>th</sup> and the 11<sup>th</sup> , one will have medium effects in regard to wealth
- 两颗吉星在 3 6 10 11 宫 财富中等

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- One born in Kema Drum Yog will be very much reproached, will be bereft of intelligence, learning, reduced to penury and perils

### 适用边界路

- Sahaj, Ari, Karm and Labh Bhava are Upachaya Bhavas
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Budh, however, is a malefic, if he joins a malefic

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn

## 上游问题

- 无

## 停止条件

- 缺少本盘吉星名册事实时停止。
- 缺少增长宫内吉星颗数事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
