---
method: ch39-v29-31-kendra-labh-lord-drishti-with-shukra
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 四宫、十宫、二宫或十一宫主相照上升，金星照 Arudh Lagna 第11宫且 Arudh Lagn 有吉星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有靠贵人和名望上位的组合
- 金星照 Arudh Lagna 的十一宫有什么用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘四宫主（Bandhu's Lord）是哪颗行星
- 本盘十宫主（Karm's Lord）是哪颗行星
- 本盘二宫主（Dhan's Lord）是哪颗行星
- 本盘十一宫主（Labh's Lord）是哪颗行星
- 本盘中哪些行星被判为吉星
- 金星（Shukra）是否相照 Arudh Lagna 起算的第11宫
- Arudh Lagna 是否被吉星占据

## 按情况检查的事实

- 四宫主（Bandhu's Lord）是否相照上升宫（Lagna）
- 十宫主（Karm's Lord）是否相照上升宫（Lagna）
- 二宫主（Dhan's Lord）是否相照上升宫（Lagna）
- 十一宫主（Labh's Lord）是否相照上升宫（Lagna）

## 依赖方法

- 无

## 执行步骤

### ch39-v29-31-kendra-labh-lord-drishti-with-shukra.step-001

- 动作：先认出四宫、十宫、二宫、十一宫的宫主，核对其中哪一个相照上升宫，再核对金星对 Arudh Lagna 起算第11宫的相照与 Arudh Lagn 内的吉星占据。
- 适用范围：仅限本命盘；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：四宫（Bandhu）、十宫（Karm）、二宫（Dhan）或十一宫（Labh）的宫主相照上升宫（Lagna），同时金星（Shukra）相照 Arudh Lagna 起算的第11宫，且 Arudh Lagn 内有吉星时，命主会成为国王。
- 本步骤产出事实：["宫主相照上升配金星照 Arudh 十一宫的贵格判定"]
- 所需事实：["本盘四宫主（Bandhu's Lord）是哪颗行星", "本盘十宫主（Karm's Lord）是哪颗行星", "本盘二宫主（Dhan's Lord）是哪颗行星", "本盘十一宫主（Labh's Lord）是哪颗行星", "本盘中哪些行星被判为吉星", "金星（Shukra）是否相照 Arudh Lagna 起算的第11宫", "Arudh Lagna 是否被吉星占据"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "金星（Shukra）是否相照 Arudh Lagna 起算的第11宫"}, {"fact_key": "Arudh Lagna 是否被吉星占据"}]}, {"operator": "OR", "operands": [{"fact_key": "四宫主（Bandhu's Lord）是否相照上升宫（Lagna）"}, {"fact_key": "十宫主（Karm's Lord）是否相照上升宫（Lagna）"}, {"fact_key": "二宫主（Dhan's Lord）是否相照上升宫（Lagna）"}, {"fact_key": "十一宫主（Labh's Lord）是否相照上升宫（Lagna）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "金星（Shukra）是否相照 Arudh Lagna 起算的第11宫"}, {"fact_key": "Arudh Lagna 是否被吉星占据"}]}, "required_fact_keys": ["四宫主（Bandhu's Lord）是否相照上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "四宫主（Bandhu's Lord）是否相照上升宫（Lagna）"}, "selection_group": "ch39-v29-31-kendra-labh-lord-drishti-with-shukra.step-001:which-lord-drishti", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫主（Bandhu's Lord）是否相照上升宫（Lagna）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "金星（Shukra）是否相照 Arudh Lagna 起算的第11宫"}, {"fact_key": "Arudh Lagna 是否被吉星占据"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否相照上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否相照上升宫（Lagna）"}, "selection_group": "ch39-v29-31-kendra-labh-lord-drishti-with-shukra.step-001:which-lord-drishti", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否相照上升宫（Lagna）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "金星（Shukra）是否相照 Arudh Lagna 起算的第11宫"}, {"fact_key": "Arudh Lagna 是否被吉星占据"}]}, "required_fact_keys": ["二宫主（Dhan's Lord）是否相照上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否相照上升宫（Lagna）"}, "selection_group": "ch39-v29-31-kendra-labh-lord-drishti-with-shukra.step-001:which-lord-drishti", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否相照上升宫（Lagna）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "金星（Shukra）是否相照 Arudh Lagna 起算的第11宫"}, {"fact_key": "Arudh Lagna 是否被吉星占据"}]}, "required_fact_keys": ["十一宫主（Labh's Lord）是否相照上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否相照上升宫（Lagna）"}, "selection_group": "ch39-v29-31-kendra-labh-lord-drishti-with-shukra.step-001:which-lord-drishti", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否相照上升宫（Lagna）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只列四宫、十宫、二宫、十一宫四个宫主，不得把别的宫主也算进来。", "三项条件并列，不得只满足其中一项就下断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘四宫主（Bandhu's Lord）是哪颗行星、本盘十宫主（Karm's Lord）是哪颗行星、本盘二宫主（Dhan's Lord）是哪颗行星、本盘十一宫主（Labh's Lord）是哪颗行星、本盘中哪些行星被判为吉星、金星（Shukra）是否相照 Arudh Lagna 起算的第11宫、Arudh Lagna 是否被吉星占据。
- 缺失即停字段：["本盘四宫主（Bandhu's Lord）是哪颗行星", "本盘十宫主（Karm's Lord）是哪颗行星", "本盘二宫主（Dhan's Lord）是哪颗行星", "本盘十一宫主（Labh's Lord）是哪颗行星", "本盘中哪些行星被判为吉星", "金星（Shukra）是否相照 Arudh Lagna 起算的第11宫", "Arudh Lagna 是否被吉星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v29-31`｜PDF [83]｜“The native will become a king, if a Grah, ruling Bandhu, Karm, Dhan, or Labh, gives a Drishti to Lagna, while Shukra gives a Drishti to the 11<sup>th</sup> from Arudh Lagna, as Arudh Lagn is occupied by a benefic.”


## 四路查书计划

### 支持路

- The native will become a king, if a Grah, ruling Bandhu, Karm, Dhan, or Labh, gives a Drishti to Lagna, while Shukra gives a Drishti to the 11<sup>th</sup> from Arudh Lagna, as Arudh Lagn is occupied by a benefic
- 宫主相照上升 金星照 Arudh 十一宫 国王

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- If malefics be in Karakāńś, Arudh Lagn and the 2<sup>nd</sup> and 8<sup>th</sup> from these places, there will be Kemadrum Yog

### 适用边界路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Grahas in the 4<sup>th</sup> , 2<sup>nd</sup> and the 11<sup>th</sup> cause Argalas, while obstructors of the Argala will be those in the 10<sup>th</sup> , 12<sup>th</sup> and 3<sup>rd</sup> from a Bhava, or a Grah

### 判断方法路

- O Brahmin, the quantum of gains will correspond to the number of Grahas in, or giving a Drishti to the 11<sup>th</sup> from Lagn Pad
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- 四个宫主的身份事实缺任一项时停止。
- 四条相照分支的事实全部缺失时停止。
- 缺少金星相照 Arudh Lagna 第11宫或 Arudh Lagn 吉星占据的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
