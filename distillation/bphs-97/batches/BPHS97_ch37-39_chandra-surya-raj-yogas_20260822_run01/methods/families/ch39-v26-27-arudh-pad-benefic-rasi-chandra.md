---
method: ch39-v26-27-arudh-pad-benefic-rasi-chandra
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Arudh Pad 为吉星星座并含月亮、木星居二宫：同样成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Arudh Pad 落在吉星星座说明什么
- 木星在二宫配合 Arudh Pad 有什么用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Arudh Pad 落在哪个星座
- 本盘中哪些行星被判为吉星
- Arudh Pad 所在星座是否为吉星主管的星座
- 月亮（Chandra）是否落 Arudh Pad
- 木星（Guru）是否落二宫（Dhan）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v26-27-arudh-pad-benefic-rasi-chandra.step-001

- 动作：核对 Arudh Pad 所在星座是否由吉星主管并含月亮（Chandra），同时木星（Guru）是否落二宫（Dhan Bhava）。
- 适用范围：仅限本命盘；原文的 the same effect 承同偈前句的国王断语；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：Arudh Pad 落在吉星主管的星座（Rāśi）并含月亮（Chandra），同时木星（Guru）落二宫（Dhan Bhava）时，同样的效果成立，即命主会成为国王。
- 本步骤产出事实：["Arudh Pad 吉星星座含月亮的贵格判定"]
- 所需事实：["本盘的 Arudh Pad 落在哪个星座", "本盘中哪些行星被判为吉星", "Arudh Pad 所在星座是否为吉星主管的星座", "月亮（Chandra）是否落 Arudh Pad", "木星（Guru）是否落二宫（Dhan）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘的 Arudh Pad 落在哪个星座"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "Arudh Pad 所在星座是否为吉星主管的星座"}, {"fact_key": "月亮（Chandra）是否落 Arudh Pad"}, {"fact_key": "木星（Guru）是否落二宫（Dhan）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文本句没有写 Argala 条件，不得把前句的无凶星 Argala 要求搬到这里。", "不得据此推断登位时间或具体权位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Arudh Pad 落在哪个星座、本盘中哪些行星被判为吉星、Arudh Pad 所在星座是否为吉星主管的星座、月亮（Chandra）是否落 Arudh Pad、木星（Guru）是否落二宫（Dhan）。
- 缺失即停字段：["本盘的 Arudh Pad 落在哪个星座", "本盘中哪些行星被判为吉星", "Arudh Pad 所在星座是否为吉星主管的星座", "月亮（Chandra）是否落 Arudh Pad", "木星（Guru）是否落二宫（Dhan）"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v26-27`｜PDF [83]｜“If the Arudh Pad is a benefic Rāśi, containing Chandra, while Guru is in Dhan Bhava, the same effect will prevail.”
  - `bphs-97:santhanam:ch39:v26-27`｜PDF [83]｜“the native will become a king”


## 四路查书计划

### 支持路

- If the Arudh Pad is a benefic Rāśi, containing Chandra, while Guru is in Dhan Bhava, the same effect will prevail
- Arudh Pad 吉星星座 含月亮 木星在二宫 国王

### 反例或取消路

- If malefics be in Karakāńś, Arudh Lagn and the 2<sup>nd</sup> and 8<sup>th</sup> from these places, there will be Kemadrum Yog
- Should Mangal and Shani be together in Dhan Bhava, the native’s wealth will be destroyed

### 适用边界路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Grahas in the 4<sup>th</sup> , 2<sup>nd</sup> and the 11<sup>th</sup> cause Argalas, while obstructors of the Argala will be those in the 10<sup>th</sup> , 12<sup>th</sup> and 3<sup>rd</sup> from a Bhava, or a Grah

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少 Arudh Pad 定位事实时停止。
- 三项条件事实缺任一项时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
