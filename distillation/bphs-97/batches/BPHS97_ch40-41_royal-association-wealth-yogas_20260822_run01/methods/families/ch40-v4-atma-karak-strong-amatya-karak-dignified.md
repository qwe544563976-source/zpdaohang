---
method: ch40-v4-atma-karak-strong-amatya-karak-dignified
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 必为王之大臣：Atma Karak 有力偕吉星，或 Amatya Karak 落本宫、入旺

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能不能坐到辅佐大位
- 我这辈子官运如何

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Atma Karak 是哪颗行星
- 本盘的 Amatya Karak 是哪颗行星
- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- Atma Karak 是否有力
- Atma Karak 是否与吉星同宫
- Amatya Karak 是否落本宫（own Bhava）
- Amatya Karak 是否入旺

## 依赖方法

- 无

## 执行步骤

### ch40-v4-atma-karak-strong-amatya-karak-dignified.step-001

- 动作：先认出 Atma Karak 与 Amatya Karak 并取吉星名册，再核对 Atma Karak 是否有力且与吉星同宫，或 Amatya Karak 是否落本宫、是否入旺。
- 适用范围：仅限本命盘两个 Char Karak 一线；原文本偈未给「有力」的判准（须另按本书 Shad Bal 一章取得），也未给吉星判准（须另按本书第 3 章的吉凶星名册取得）；原文未给时间限定。
- 原文最小意思：Atma Karak 有力并与吉星同宫，或 Amatya Karak 落本宫（own Bhava），或 Amatya Karak 入旺时，命主必定成为王之大臣。
- 本步骤产出事实：["两个 Char Karak 的大臣格判定"]
- 所需事实：["本盘的 Atma Karak 是哪颗行星", "本盘的 Amatya Karak 是哪颗行星", "本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Amatya Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否有力"}, {"fact_key": "Atma Karak 是否与吉星同宫"}]}, {"fact_key": "Amatya Karak 是否落本宫（own Bhava）"}, {"fact_key": "Amatya Karak 是否入旺"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Amatya Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["Atma Karak 是否有力", "Atma Karak 是否与吉星同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否有力"}, {"fact_key": "Atma Karak 是否与吉星同宫"}]}, "selection_group": "ch40-v4-atma-karak-strong-amatya-karak-dignified.step-001:which-karak-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否有力、Atma Karak 是否与吉星同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Amatya Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["Amatya Karak 是否落本宫（own Bhava）"], "branch_condition_logic": {"fact_key": "Amatya Karak 是否落本宫（own Bhava）"}, "selection_group": "ch40-v4-atma-karak-strong-amatya-karak-dignified.step-001:which-karak-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：Amatya Karak 是否落本宫（own Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Amatya Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["Amatya Karak 是否入旺"], "branch_condition_logic": {"fact_key": "Amatya Karak 是否入旺"}, "selection_group": "ch40-v4-atma-karak-strong-amatya-karak-dignified.step-001:which-karak-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：Amatya Karak 是否入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文的「有力」与「与吉星同宫」只加在 Atma Karak 这一支，不得移到 Amatya Karak 的两支上。", "不得据此推断职衔、任期或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Atma Karak 是哪颗行星、本盘的 Amatya Karak 是哪颗行星、本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘的 Atma Karak 是哪颗行星", "本盘的 Amatya Karak 是哪颗行星", "本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v4`｜PDF [85]｜“If Atma Karak is strong and is with a benefic, or Amatya Karak is in its own Bhava, or in exaltation, one will surely become a king’s minister.”


## 四路查书计划

### 支持路

- If Atma Karak is strong and is with a benefic, or Amatya Karak is in its own Bhava, or in exaltation
- Atma Karak 有力 与吉星同宫 Amatya Karak 落本宫 入旺 大臣

### 反例或取消路

- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The Grah next to Atma Karak in terms of longitude is called Amatya Karak

### 判断方法路

- Yogas For Royal Association
- There is no doubt in one’s becoming a king’s minister and famous, if Atma Karak is in Tanu, or Putr, or Dharm Bhava

## 上游问题

- 无

## 停止条件

- Atma Karak 或 Amatya Karak 的身份事实缺失时停止。
- 「有力」的判准未按本书 Shad Bal 一章取到时，该分支停判。
- 吉星名册未定时停止：须先按 BPHS 自己的吉凶星定义取名册。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
