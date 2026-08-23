---
method: ch39-v38-putr-lord-placement-and-yuti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 五宫主居上升、四宫或十宫并与九宫主或上升主同宫：成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 五宫主落哪里最有力
- 我有没有当上位者的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫主（Putr's Lord）是哪颗行星
- 本盘九宫主（Dharm's Lord）是哪颗行星
- 本盘上升主（Lagn's Lord）是哪颗行星

## 按情况检查的事实

- 五宫主（Putr's Lord）是否落上升宫（Lagna）
- 五宫主（Putr's Lord）是否落四宫（Bandhu）
- 五宫主（Putr's Lord）是否落十宫（Karm）
- 五宫主（Putr's Lord）是否与九宫主（Dharm's Lord）同宫
- 五宫主（Putr's Lord）是否与上升主（Lagn's Lord）同宫

## 依赖方法

- 无

## 执行步骤

### ch39-v38-putr-lord-placement-and-yuti.step-001

- 动作：先认出五宫主、九宫主与上升主，再核对五宫主落在哪一宫，以及它与九宫主或上升主是否同宫。
- 适用范围：仅限本命盘；原文没有时间限定。
- 原文最小意思：五宫主（Putr's Lord）落上升宫（Lagna）、四宫（Bandhu）或十宫（Karm Bhava），并与九宫主（Dharm's Lord）或上升主（Lagn Lord）同宫时，命主会成为国王。
- 本步骤产出事实：["五宫主落宫并与九宫主上升主同宫的贵格判定"]
- 所需事实：["本盘五宫主（Putr's Lord）是哪颗行星", "本盘九宫主（Dharm's Lord）是哪颗行星", "本盘上升主（Lagn's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "五宫主（Putr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "五宫主（Putr's Lord）是否落四宫（Bandhu）"}, {"fact_key": "五宫主（Putr's Lord）是否落十宫（Karm）"}]}, {"operator": "OR", "operands": [{"fact_key": "五宫主（Putr's Lord）是否与九宫主（Dharm's Lord）同宫"}, {"fact_key": "五宫主（Putr's Lord）是否与上升主（Lagn's Lord）同宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}]}, "required_fact_keys": ["五宫主（Putr's Lord）是否落上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "五宫主（Putr's Lord）是否落上升宫（Lagna）"}, "selection_group": "ch39-v38-putr-lord-placement-and-yuti.step-001:putr-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主（Putr's Lord）是否落上升宫（Lagna）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}]}, "required_fact_keys": ["五宫主（Putr's Lord）是否落四宫（Bandhu）"], "branch_condition_logic": {"fact_key": "五宫主（Putr's Lord）是否落四宫（Bandhu）"}, "selection_group": "ch39-v38-putr-lord-placement-and-yuti.step-001:putr-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主（Putr's Lord）是否落四宫（Bandhu）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}]}, "required_fact_keys": ["五宫主（Putr's Lord）是否落十宫（Karm）"], "branch_condition_logic": {"fact_key": "五宫主（Putr's Lord）是否落十宫（Karm）"}, "selection_group": "ch39-v38-putr-lord-placement-and-yuti.step-001:putr-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主（Putr's Lord）是否落十宫（Karm）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}]}, "required_fact_keys": ["五宫主（Putr's Lord）是否与九宫主（Dharm's Lord）同宫"], "branch_condition_logic": {"fact_key": "五宫主（Putr's Lord）是否与九宫主（Dharm's Lord）同宫"}, "selection_group": "ch39-v38-putr-lord-placement-and-yuti.step-001:yuti-with", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主（Putr's Lord）是否与九宫主（Dharm's Lord）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}]}, "required_fact_keys": ["五宫主（Putr's Lord）是否与上升主（Lagn's Lord）同宫"], "branch_condition_logic": {"fact_key": "五宫主（Putr's Lord）是否与上升主（Lagn's Lord）同宫"}, "selection_group": "ch39-v38-putr-lord-placement-and-yuti.step-001:yuti-with", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主（Putr's Lord）是否与上升主（Lagn's Lord）同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写上升宫、四宫、十宫三处，不得把别的宫位也算进来。", "原文写的是同宫（yuti），不得把相照也算作成立条件。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫主（Putr's Lord）是哪颗行星、本盘九宫主（Dharm's Lord）是哪颗行星、本盘上升主（Lagn's Lord）是哪颗行星。
- 缺失即停字段：["本盘五宫主（Putr's Lord）是哪颗行星", "本盘九宫主（Dharm's Lord）是哪颗行星", "本盘上升主（Lagn's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v38`｜PDF [84]｜“If Putr’s Lord is in Lagna, Bandhu, or Karm Bhava, yuti with Dharm’s Lord, or Lagn Lord, the native will become a king.”


## 四路查书计划

### 支持路

- If Putr’s Lord is in Lagna, Bandhu, or Karm Bhava, yuti with Dharm’s Lord, or Lagn Lord, the native will become a king
- 五宫主落上升四宫十宫 与九宫主同宫 国王

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- Should Putr’s and Dharm’s Lords be, respectively, found in Ari and Vyaya Bhava and receive a Drishti from Marak Grahas, the native will be penniless

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine)

### 判断方法路

- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- 五宫主、九宫主或上升主的身份事实缺失时停止。
- 三处落宫事实全部缺失时停止。
- 两种同宫关系事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
