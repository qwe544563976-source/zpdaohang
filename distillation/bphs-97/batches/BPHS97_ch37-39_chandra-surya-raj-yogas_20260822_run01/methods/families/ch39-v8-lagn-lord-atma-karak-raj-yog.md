---
method: ch39-v8-lagn-lord-atma-karak-raj-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升主与 Atma Karak 同落一宫、五宫或七宫并与吉星同宫或受吉照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有贵格
- 上升主和 Atma Karak 走到一起说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）是哪颗行星
- 本盘的 Atma Karak 是哪颗行星
- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 上升主（Lagn's Lord）是否落一宫（Tanu Bhava）
- Atma Karak 是否落一宫（Tanu Bhava）
- 上升主（Lagn's Lord）是否落五宫（Putr Bhava）
- Atma Karak 是否落五宫（Putr Bhava）
- 上升主（Lagn's Lord）是否落七宫（Yuvati Bhava）
- Atma Karak 是否落七宫（Yuvati Bhava）
- 上升主（Lagn's Lord）是否与吉星同宫
- Atma Karak 是否与吉星同宫
- 上升主（Lagn's Lord）是否被吉星相照
- Atma Karak 是否被吉星相照

## 依赖方法

- 无

## 执行步骤

### ch39-v8-lagn-lord-atma-karak-raj-yog.step-001

- 动作：先认出上升主与 Atma Karak 并取吉星名册，再核对两者同落的宫位以及与吉星的同宫或相照关系，判定 Raj Yog 是否成立。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：上升主（Lagn's Lord）与 Atma Karak 同落一宫（Tanu Bhava）、五宫（Putr Bhava）或七宫（Yuvati Bhava），并与吉星同宫或受吉星相照时，Raj Yog 成立。
- 本步骤产出事实：["上升主与 Atma Karak 同居三宫之一的贵格判定"]
- 所需事实：["本盘上升主（Lagn's Lord）是哪颗行星", "本盘的 Atma Karak 是哪颗行星", "本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落一宫（Tanu Bhava）"}, {"fact_key": "Atma Karak 是否落一宫（Tanu Bhava）"}]}, {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落五宫（Putr Bhava）"}, {"fact_key": "Atma Karak 是否落五宫（Putr Bhava）"}]}, {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落七宫（Yuvati Bhava）"}, {"fact_key": "Atma Karak 是否落七宫（Yuvati Bhava）"}]}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与吉星同宫"}, {"fact_key": "Atma Karak 是否与吉星同宫"}]}, {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否被吉星相照"}, {"fact_key": "Atma Karak 是否被吉星相照"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否落一宫（Tanu Bhava）", "Atma Karak 是否落一宫（Tanu Bhava）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落一宫（Tanu Bhava）"}, {"fact_key": "Atma Karak 是否落一宫（Tanu Bhava）"}]}, "selection_group": "ch39-v8-lagn-lord-atma-karak-raj-yog.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落一宫（Tanu Bhava）、Atma Karak 是否落一宫（Tanu Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否落五宫（Putr Bhava）", "Atma Karak 是否落五宫（Putr Bhava）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落五宫（Putr Bhava）"}, {"fact_key": "Atma Karak 是否落五宫（Putr Bhava）"}]}, "selection_group": "ch39-v8-lagn-lord-atma-karak-raj-yog.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落五宫（Putr Bhava）、Atma Karak 是否落五宫（Putr Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否落七宫（Yuvati Bhava）", "Atma Karak 是否落七宫（Yuvati Bhava）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落七宫（Yuvati Bhava）"}, {"fact_key": "Atma Karak 是否落七宫（Yuvati Bhava）"}]}, "selection_group": "ch39-v8-lagn-lord-atma-karak-raj-yog.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落七宫（Yuvati Bhava）、Atma Karak 是否落七宫（Yuvati Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否与吉星同宫", "Atma Karak 是否与吉星同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与吉星同宫"}, {"fact_key": "Atma Karak 是否与吉星同宫"}]}, "selection_group": "ch39-v8-lagn-lord-atma-karak-raj-yog.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否与吉星同宫、Atma Karak 是否与吉星同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否被吉星相照", "Atma Karak 是否被吉星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否被吉星相照"}, {"fact_key": "Atma Karak 是否被吉星相照"}]}, "selection_group": "ch39-v8-lagn-lord-atma-karak-raj-yog.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否被吉星相照、Atma Karak 是否被吉星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写一宫、五宫、七宫三处，不得把落宫条件扩大到别的宫位。", "不得据此推断具体职位、财富或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）是哪颗行星、本盘的 Atma Karak 是哪颗行星、本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘上升主（Lagn's Lord）是哪颗行星", "本盘的 Atma Karak 是哪颗行星", "本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v8`｜PDF [82]｜“If Lagn’s Lord and Atma Karak are in Tanu, Putr, or Yuvati Bhava, yuti with, or receiving a Drishti from a benefic, a Raj Yog is formed.”


## 四路查书计划

### 支持路

- If Lagn’s Lord and Atma Karak are in Tanu, Putr, or Yuvati Bhava, yuti with, or receiving a Drishti from a benefic, a Raj Yog is formed
- 上升主与 Atma Karak 同宫 吉星相照 贵格

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Budh, however, is a malefic, if he joins a malefic
- Karakāńś is the Navāńś, occupied by the Atma Karak Grah

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 上升主或 Atma Karak 的身份事实缺失时停止。
- 三处落宫事实全部缺失时停止。
- 与吉星的同宫、相照两项关系事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
