---
method: ch40-v15-lagn-lord-or-atma-karak-with-putr-lord
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 成为王或大臣：上升主或 Atma Karak 与五宫主同宫并落角宫、三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能走到多高的位置
- 我有没有掌权的命

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）是哪颗行星
- 本盘的 Atma Karak 是哪颗行星
- 本盘五宫主（Putr's Lord）是哪颗行星

## 按情况检查的事实

- 上升主（Lagn's Lord）是否与五宫主（Putr's Lord）同宫
- Atma Karak 是否与五宫主（Putr's Lord）同宫
- 上升主（Lagn's Lord）是否落角宫（Kendr）
- 上升主（Lagn's Lord）是否落三角宫（Kon）
- Atma Karak 是否落角宫（Kendr）
- Atma Karak 是否落三角宫（Kon）

## 依赖方法

- 无

## 执行步骤

### ch40-v15-lagn-lord-or-atma-karak-with-putr-lord.step-001

- 动作：先认出上升主、Atma Karak 与五宫主，再核对上升主或 Atma Karak 是否与五宫主同宫、并且落在角宫（Kendr）或三角宫（Kon）。
- 适用范围：仅限本命盘上升主或 Atma Karak 与五宫主的同宫关系；原文的同宫与落宫两项加在同一颗行星身上，故每条分支内两项事实必须指向同一颗行星；角宫与三角宫的名目须另按本书第 7 章取得；原文未给时间限定。
- 原文最小意思：上升主（Lagn's Lord）与五宫主（Putr's Lord）同宫并落角宫（Kendr）或三角宫（Kon），或 Atma Karak 与五宫主同宫并落角宫（Kendr）或三角宫（Kon）时，命主将成为王，或成为大臣。
- 本步骤产出事实：["上升主或 Atma Karak 与五宫主同宫的王与大臣判定"]
- 所需事实：["本盘上升主（Lagn's Lord）是哪颗行星", "本盘的 Atma Karak 是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与五宫主（Putr's Lord）同宫"}, {"fact_key": "上升主（Lagn's Lord）是否落角宫（Kendr）"}]}, {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与五宫主（Putr's Lord）同宫"}, {"fact_key": "上升主（Lagn's Lord）是否落三角宫（Kon）"}]}, {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否与五宫主（Putr's Lord）同宫"}, {"fact_key": "Atma Karak 是否落角宫（Kendr）"}]}, {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否与五宫主（Putr's Lord）同宫"}, {"fact_key": "Atma Karak 是否落三角宫（Kon）"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否与五宫主（Putr's Lord）同宫", "上升主（Lagn's Lord）是否落角宫（Kendr）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与五宫主（Putr's Lord）同宫"}, {"fact_key": "上升主（Lagn's Lord）是否落角宫（Kendr）"}]}, "selection_group": "ch40-v15-lagn-lord-or-atma-karak-with-putr-lord.step-001:subject-and-place", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否与五宫主（Putr's Lord）同宫、上升主（Lagn's Lord）是否落角宫（Kendr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否与五宫主（Putr's Lord）同宫", "上升主（Lagn's Lord）是否落三角宫（Kon）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与五宫主（Putr's Lord）同宫"}, {"fact_key": "上升主（Lagn's Lord）是否落三角宫（Kon）"}]}, "selection_group": "ch40-v15-lagn-lord-or-atma-karak-with-putr-lord.step-001:subject-and-place", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否与五宫主（Putr's Lord）同宫、上升主（Lagn's Lord）是否落三角宫（Kon）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, "required_fact_keys": ["Atma Karak 是否与五宫主（Putr's Lord）同宫", "Atma Karak 是否落角宫（Kendr）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否与五宫主（Putr's Lord）同宫"}, {"fact_key": "Atma Karak 是否落角宫（Kendr）"}]}, "selection_group": "ch40-v15-lagn-lord-or-atma-karak-with-putr-lord.step-001:subject-and-place", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否与五宫主（Putr's Lord）同宫、Atma Karak 是否落角宫（Kendr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, "required_fact_keys": ["Atma Karak 是否与五宫主（Putr's Lord）同宫", "Atma Karak 是否落三角宫（Kon）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否与五宫主（Putr's Lord）同宫"}, {"fact_key": "Atma Karak 是否落三角宫（Kon）"}]}, "selection_group": "ch40-v15-lagn-lord-or-atma-karak-with-putr-lord.step-001:subject-and-place", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否与五宫主（Putr's Lord）同宫、Atma Karak 是否落三角宫（Kon）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把同宫的一方与落角宫、三角宫的另一方拆成两颗不同的行星来凑条件。", "不得据此推断是王还是大臣、也不得推断应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）是哪颗行星、本盘的 Atma Karak 是哪颗行星、本盘五宫主（Putr's Lord）是哪颗行星。
- 缺失即停字段：["本盘上升主（Lagn's Lord）是哪颗行星", "本盘的 Atma Karak 是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v15`｜PDF [85, 86]｜“Should Lagn’s Lord, or the Atma Karak be yuti with Putr’s Lord and be in a Kendr, or in a Kon, the native will be a king, or minister.”


## 四路查书计划

### 支持路

- Should Lagn’s Lord, or the Atma Karak be yuti with Putr’s Lord and be in a Kendr, or in a Kon, the native will be a king, or minister
- 上升主或 Atma Karak 与五宫主同宫 落角宫三角宫 王或大臣

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava
- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- The Grah next to Atma Karak in terms of longitude is called Amatya Karak

### 判断方法路

- Yogas For Royal Association
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 上升主、Atma Karak 或五宫主的身份事实缺失时停止。
- 同宫与落宫两类事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
