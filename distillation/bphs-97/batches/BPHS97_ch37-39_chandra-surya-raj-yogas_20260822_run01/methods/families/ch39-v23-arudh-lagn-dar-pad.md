---
method: ch39-v23-arudh-lagn-dar-pad
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Arudh Lagn 与 Dar Pad 互成角宫、三宫十一宫或三角宫：无疑成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Arudh Lagna 和配偶宫的 Pad 有什么关系
- 我有没有一定应验的贵格

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Arudh Lagna 落在哪个星座
- 本盘的 Dar Pad 落在哪个星座

## 按情况检查的事实

- Arudh Lagn 与 Dar Pad 是否互成角宫（Kendras）
- Arudh Lagn 与 Dar Pad 是否互成三宫十一宫关系（Sahaj/Labh）
- Arudh Lagn 与 Dar Pad 是否互成三角宫（Konas）

## 依赖方法

- 无

## 执行步骤

### ch39-v23-arudh-lagn-dar-pad.step-001

- 动作：先定出 Arudh Lagn 与 Dar Pad 两个 Pad 的位置，再核对两者之间是哪一种相互关系。
- 适用范围：仅限本命盘；原文没有时间限定。
- 原文最小意思：Arudh Lagn 与 Dar Pad 互成角宫（Kendras），或互成三宫与十一宫的关系（Sahaj/Labh Bhavas），或互成三角宫（Konas）时，命主无疑会成为国王。
- 本步骤产出事实：["Arudh Lagn 与 Dar Pad 互位的贵格判定"]
- 所需事实：["本盘的 Arudh Lagna 落在哪个星座", "本盘的 Dar Pad 落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘的 Arudh Lagna 落在哪个星座"}, {"fact_key": "本盘的 Dar Pad 落在哪个星座"}]}, {"operator": "OR", "operands": [{"fact_key": "Arudh Lagn 与 Dar Pad 是否互成角宫（Kendras）"}, {"fact_key": "Arudh Lagn 与 Dar Pad 是否互成三宫十一宫关系（Sahaj/Labh）"}, {"fact_key": "Arudh Lagn 与 Dar Pad 是否互成三角宫（Konas）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Arudh Lagna 落在哪个星座"}, {"fact_key": "本盘的 Dar Pad 落在哪个星座"}]}, "required_fact_keys": ["Arudh Lagn 与 Dar Pad 是否互成角宫（Kendras）"], "branch_condition_logic": {"fact_key": "Arudh Lagn 与 Dar Pad 是否互成角宫（Kendras）"}, "selection_group": "ch39-v23-arudh-lagn-dar-pad.step-001:mutual-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：Arudh Lagn 与 Dar Pad 是否互成角宫（Kendras）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Arudh Lagna 落在哪个星座"}, {"fact_key": "本盘的 Dar Pad 落在哪个星座"}]}, "required_fact_keys": ["Arudh Lagn 与 Dar Pad 是否互成三宫十一宫关系（Sahaj/Labh）"], "branch_condition_logic": {"fact_key": "Arudh Lagn 与 Dar Pad 是否互成三宫十一宫关系（Sahaj/Labh）"}, "selection_group": "ch39-v23-arudh-lagn-dar-pad.step-001:mutual-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：Arudh Lagn 与 Dar Pad 是否互成三宫十一宫关系（Sahaj/Labh）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Arudh Lagna 落在哪个星座"}, {"fact_key": "本盘的 Dar Pad 落在哪个星座"}]}, "required_fact_keys": ["Arudh Lagn 与 Dar Pad 是否互成三角宫（Konas）"], "branch_condition_logic": {"fact_key": "Arudh Lagn 与 Dar Pad 是否互成三角宫（Konas）"}, "selection_group": "ch39-v23-arudh-lagn-dar-pad.step-001:mutual-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：Arudh Lagn 与 Dar Pad 是否互成三角宫（Konas）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写这三种相互关系，不得把别的宫位关系也算进来。", "不得据此推断配偶、婚姻或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Arudh Lagna 落在哪个星座、本盘的 Dar Pad 落在哪个星座。
- 缺失即停字段：["本盘的 Arudh Lagna 落在哪个星座", "本盘的 Dar Pad 落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v23`｜PDF [83]｜“If the Arudh Lagn and Dar Pad are in mutual Kendras, or in mutual Sahaj/Labh Bhavas, or in mutual Konas, the native will doubtlessly become a king.”


## 四路查书计划

### 支持路

- If the Arudh Lagn and Dar Pad are in mutual Kendras, or in mutual Sahaj/Labh Bhavas, or in mutual Konas, the native will doubtlessly become a king
- Arudh Lagn 与 Dar Pad 互成角宫 三角宫 国王

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- If malefics be in Karakāńś, Arudh Lagn and the 2<sup>nd</sup> and 8<sup>th</sup> from these places, there will be Kemadrum Yog

### 适用边界路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad

### 判断方法路

- Names of the 12 Arudhas are Lagn Pad - Arudh of Tanu Bhava, Dhan of Dhan, Vikram (Bhratru) of Sahaj
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- 缺少 Arudh Lagn 或 Dar Pad 的定位事实时停止。
- 三种相互关系事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
