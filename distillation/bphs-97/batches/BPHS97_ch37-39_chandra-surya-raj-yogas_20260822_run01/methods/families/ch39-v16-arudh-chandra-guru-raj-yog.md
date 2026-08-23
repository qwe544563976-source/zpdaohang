---
method: ch39-v16-arudh-chandra-guru-raj-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮与吉星居 Arudh Lagn、木星居本命上升第2宫，两处受入旺或居本星座行星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Arudh Lagna 上有月亮说明什么
- 我有没有靠名望起来的贵格

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否落 Arudh Lagna
- Arudh Lagna 是否被吉星占据
- 木星（Guru）是否落本命上升（natal Lagn）起算的第2宫
- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- Arudh Lagna 是否被入旺的行星相照
- 本命上升（natal Lagn）起算的第2宫是否被入旺的行星相照
- Arudh Lagna 是否被落自己主管星座（own Rāśi）的行星相照
- 本命上升（natal Lagn）起算的第2宫是否被落自己主管星座（own Rāśi）的行星相照

## 依赖方法

- 无

## 执行步骤

### ch39-v16-arudh-chandra-guru-raj-yog.step-001

- 动作：核对 Arudh Lagn 内是否同时有月亮（Chandra）与一颗吉星、木星（Guru）是否落本命上升起算的第2宫，再核对这两处是否都被入旺或落自己主管星座的行星相照。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文的 both these places 指 Arudh Lagn 与本命上升起算的第2宫；原文没有时间限定。
- 原文最小意思：月亮（Chandra）与一颗吉星同落 Arudh Lagn，木星（Guru）落本命上升（natal Lagn）起算的第2宫，且这两处都被入旺的行星或落自己主管星座（own Rāśi）的行星相照时，Raj Yog 成立。
- 本步骤产出事实：["Arudh Lagn 月亮木星组合的贵格判定"]
- 所需事实：["月亮（Chandra）是否落 Arudh Lagna", "Arudh Lagna 是否被吉星占据", "木星（Guru）是否落本命上升（natal Lagn）起算的第2宫", "本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落 Arudh Lagna"}, {"fact_key": "Arudh Lagna 是否被吉星占据"}, {"fact_key": "木星（Guru）是否落本命上升（natal Lagn）起算的第2宫"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "Arudh Lagna 是否被入旺的行星相照"}, {"fact_key": "本命上升（natal Lagn）起算的第2宫是否被入旺的行星相照"}]}, {"operator": "AND", "operands": [{"fact_key": "Arudh Lagna 是否被落自己主管星座（own Rāśi）的行星相照"}, {"fact_key": "本命上升（natal Lagn）起算的第2宫是否被落自己主管星座（own Rāśi）的行星相照"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落 Arudh Lagna"}, {"fact_key": "Arudh Lagna 是否被吉星占据"}, {"fact_key": "木星（Guru）是否落本命上升（natal Lagn）起算的第2宫"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["Arudh Lagna 是否被入旺的行星相照", "本命上升（natal Lagn）起算的第2宫是否被入旺的行星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Arudh Lagna 是否被入旺的行星相照"}, {"fact_key": "本命上升（natal Lagn）起算的第2宫是否被入旺的行星相照"}]}, "selection_group": "ch39-v16-arudh-chandra-guru-raj-yog.step-001:drishti-source", "stop_condition": "选中该分支后，缺少以下事实即停止：Arudh Lagna 是否被入旺的行星相照、本命上升（natal Lagn）起算的第2宫是否被入旺的行星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落 Arudh Lagna"}, {"fact_key": "Arudh Lagna 是否被吉星占据"}, {"fact_key": "木星（Guru）是否落本命上升（natal Lagn）起算的第2宫"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["Arudh Lagna 是否被落自己主管星座（own Rāśi）的行星相照", "本命上升（natal Lagn）起算的第2宫是否被落自己主管星座（own Rāśi）的行星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Arudh Lagna 是否被落自己主管星座（own Rāśi）的行星相照"}, {"fact_key": "本命上升（natal Lagn）起算的第2宫是否被落自己主管星座（own Rāśi）的行星相照"}]}, "selection_group": "ch39-v16-arudh-chandra-guru-raj-yog.step-001:drishti-source", "stop_condition": "选中该分支后，缺少以下事实即停止：Arudh Lagna 是否被落自己主管星座（own Rāśi）的行星相照、本命上升（natal Lagn）起算的第2宫是否被落自己主管星座（own Rāśi）的行星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["own Rāśi 是行星自己主管的星座，不得读成落本宫。", "原文要求两处都受相照，不得只满足其中一处。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否落 Arudh Lagna、Arudh Lagna 是否被吉星占据、木星（Guru）是否落本命上升（natal Lagn）起算的第2宫、本盘中哪些行星被判为吉星。
- 缺失即停字段：["月亮（Chandra）是否落 Arudh Lagna", "Arudh Lagna 是否被吉星占据", "木星（Guru）是否落本命上升（natal Lagn）起算的第2宫", "本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v16`｜PDF [83]｜“If Chandra and a benefic are in the Arudh Lang, as Guru is in the 2<sup>nd</sup> from the natal Lagn and both these places are receiving Drishtis from Grahas in exaltation, or Grahas in own Rāśi, there will be a Raj Yog.”


## 四路查书计划

### 支持路

- If Chandra and a benefic are in the Arudh Lang, as Guru is in the 2<sup>nd</sup> from the natal Lagn and both these places are receiving Drishtis from Grahas in exaltation, or Grahas in own Rāśi, there will be a Raj Yog
- 月亮吉星在 Arudh Lagna 木星在第2宫 贵格

### 反例或取消路

- If malefics be in Karakāńś, Arudh Lagn and the 2<sup>nd</sup> and 8<sup>th</sup> from these places, there will be Kemadrum Yog
- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak

### 适用边界路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth

### 判断方法路

- Grahas in the 4<sup>th</sup> , 2<sup>nd</sup> and the 11<sup>th</sup> cause Argalas, while obstructors of the Argala will be those in the 10<sup>th</sup> , 12<sup>th</sup> and 3<sup>rd</sup> from a Bhava, or a Grah
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- 缺少 Arudh Lagna 的定位事实时停止。
- 两处受照的两条路线事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
