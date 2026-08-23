---
method: ch39-v22-atma-karak-in-benefic-rasi
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Atma Karak 落吉星主管的星座或九分盘：富有

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的财运怎么样
- Atma Karak 落在哪里算好

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Atma Karak 是哪颗行星
- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- Atma Karak 是否落吉星主管的星座（Rāśi）
- Atma Karak 在九分盘（Navāńś D9）中是否落吉星主管的星座

## 依赖方法

- 无

## 执行步骤

### ch39-v22-atma-karak-in-benefic-rasi.step-001

- 动作：先认出 Atma Karak 并取吉星名册，再核对它所落的星座或九分盘星座是否由吉星主管。
- 适用范围：仅限本命盘财富主题；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：Atma Karak 落在吉星主管的星座（Rāśi）或吉星主管的九分盘（Navāńś）星座时，命主会富有。
- 本步骤产出事实：["Atma Karak 居吉星星座的富有判定"]
- 所需事实：["本盘的 Atma Karak 是哪颗行星", "本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, {"operator": "OR", "operands": [{"fact_key": "Atma Karak 是否落吉星主管的星座（Rāśi）"}, {"fact_key": "Atma Karak 在九分盘（Navāńś D9）中是否落吉星主管的星座"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["Atma Karak 是否落吉星主管的星座（Rāśi）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落吉星主管的星座（Rāśi）"}, "selection_group": "ch39-v22-atma-karak-in-benefic-rasi.step-001:rasi-or-navamsa", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落吉星主管的星座（Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["Atma Karak 在九分盘（Navāńś D9）中是否落吉星主管的星座"], "branch_condition_logic": {"fact_key": "Atma Karak 在九分盘（Navāńś D9）中是否落吉星主管的星座"}, "selection_group": "ch39-v22-atma-karak-in-benefic-rasi.step-001:rasi-or-navamsa", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 在九分盘（Navāńś D9）中是否落吉星主管的星座。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、来源或发财时间。", "Navāńś 是九分盘（D9），不得换成别的分盘。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Atma Karak 是哪颗行星、本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘的 Atma Karak 是哪颗行星", "本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v22`｜PDF [83]｜“If the Atma Karak Grah is in a benefic’s Rāśi/Navāńś, the native will be wealthy.”


## 四路查书计划

### 支持路

- If the Atma Karak Grah is in a benefic’s Rāśi/Navāńś, the native will be wealthy
- Atma Karak 落吉星星座 九分盘 富有

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- The Lord of the Navāńś, occupied by Chandra, joining a Marak Grah, or occupying a Marak Bhava, will make one penniless

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Budh, however, is a malefic, if he joins a malefic
- Karakāńś is the Navāńś, occupied by the Atma Karak Grah

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少 Atma Karak 身份事实时停止。
- 缺少本盘吉星名册事实时停止。
- 星座与九分盘两项归属事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
