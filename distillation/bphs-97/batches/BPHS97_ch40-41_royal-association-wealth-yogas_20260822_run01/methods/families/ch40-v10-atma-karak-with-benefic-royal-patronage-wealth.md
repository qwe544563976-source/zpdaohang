---
method: ch40-v10-atma-karak-with-benefic-royal-patronage-wealth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 因王家庇护而得财：Atma Karak 偕吉星落五宫、七宫、十宫或九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的钱会从什么路子来
- 我能不能靠上面的关照挣到钱

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Atma Karak 落在哪一宫
- 本盘中哪些行星被判为吉星
- Atma Karak 是否与吉星同宫

## 按情况检查的事实

- Atma Karak 是否落五宫（Putr Bhava）
- Atma Karak 是否落七宫（Yuvati Bhava）
- Atma Karak 是否落十宫（Karm Bhava）
- Atma Karak 是否落九宫（Dharm Bhava）

## 依赖方法

- 无

## 执行步骤

### ch40-v10-atma-karak-with-benefic-royal-patronage-wealth.step-001

- 动作：先取 Atma Karak 的落宫与吉星名册，核对它是否与吉星同宫，再看它落在五宫、七宫、十宫还是九宫。
- 适用范围：仅限本命盘 Atma Karak 的落宫与同宫关系；原文本偈未给吉星判准，须另按本书第 3 章的吉凶星名册取得；原文未给时间限定。
- 原文最小意思：Atma Karak 落五宫（Putr Bhava）、七宫（Yuvati Bhava）、十宫（Karm Bhava）或九宫（Dharm Bhava），并与吉星同宫时，命主将因王家庇护而得财。
- 本步骤产出事实：["Atma Karak 偕吉星落四宫之一的王家得财判定"]
- 所需事实：["本盘的 Atma Karak 落在哪一宫", "本盘中哪些行星被判为吉星", "Atma Karak 是否与吉星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "Atma Karak 是否与吉星同宫"}]}, {"operator": "OR", "operands": [{"fact_key": "Atma Karak 是否落五宫（Putr Bhava）"}, {"fact_key": "Atma Karak 是否落七宫（Yuvati Bhava）"}, {"fact_key": "Atma Karak 是否落十宫（Karm Bhava）"}, {"fact_key": "Atma Karak 是否落九宫（Dharm Bhava）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "Atma Karak 是否与吉星同宫"}]}, "required_fact_keys": ["Atma Karak 是否落五宫（Putr Bhava）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落五宫（Putr Bhava）"}, "selection_group": "ch40-v10-atma-karak-with-benefic-royal-patronage-wealth.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落五宫（Putr Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "Atma Karak 是否与吉星同宫"}]}, "required_fact_keys": ["Atma Karak 是否落七宫（Yuvati Bhava）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落七宫（Yuvati Bhava）"}, "selection_group": "ch40-v10-atma-karak-with-benefic-royal-patronage-wealth.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落七宫（Yuvati Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "Atma Karak 是否与吉星同宫"}]}, "required_fact_keys": ["Atma Karak 是否落十宫（Karm Bhava）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落十宫（Karm Bhava）"}, "selection_group": "ch40-v10-atma-karak-with-benefic-royal-patronage-wealth.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落十宫（Karm Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "Atma Karak 是否与吉星同宫"}]}, "required_fact_keys": ["Atma Karak 是否落九宫（Dharm Bhava）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落九宫（Dharm Bhava）"}, "selection_group": "ch40-v10-atma-karak-with-benefic-royal-patronage-wealth.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落九宫（Dharm Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写五宫、七宫、十宫、九宫四处，不得把这条断语套到别的落宫。", "不得据此推断财富数额或得财时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Atma Karak 落在哪一宫、本盘中哪些行星被判为吉星、Atma Karak 是否与吉星同宫。
- 缺失即停字段：["本盘的 Atma Karak 落在哪一宫", "本盘中哪些行星被判为吉星", "Atma Karak 是否与吉星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v10`｜PDF [85]｜“Should the Atma Karak be in Putr, Yuvati, Karm, or Dharm Bhava and happen to be with a benefic, one will earn wealth through royal patronage.”


## 四路查书计划

### 支持路

- Should the Atma Karak be in Putr, Yuvati, Karm, or Dharm Bhava and happen to be with a benefic, one will earn wealth through royal patronage
- Atma Karak 与吉星同宫 落五七十九宫 王家得财

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava
- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Karakāńś is the Navāńś, occupied by the Atma Karak Grah

### 判断方法路

- Yogas For Royal Association
- One will gain through royal association, if Labh Bhava is occupied by its own Lord and is devoid of a Drishti from a malefic

## 上游问题

- 无

## 停止条件

- Atma Karak 的落宫事实缺失时停止。
- 吉星名册未定时停止：须先按 BPHS 自己的吉凶星定义取名册。
- Atma Karak 是否与吉星同宫的事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
