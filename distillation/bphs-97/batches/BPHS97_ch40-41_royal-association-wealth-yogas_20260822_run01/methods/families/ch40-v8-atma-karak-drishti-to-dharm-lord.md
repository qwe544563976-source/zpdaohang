---
method: ch40-v8-atma-karak-drishti-to-dharm-lord
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 成为王之大臣：Atma Karak 落角宫、三角宫、入旺或本宫并相照九宫主

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有当参谋辅政的命
- 我的机遇靠什么打开

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Atma Karak 是哪颗行星
- 本盘九宫主（Dharm's Lord）是哪颗行星
- Atma Karak 是否相照九宫主（Dharm's Lord）

## 按情况检查的事实

- Atma Karak 是否落角宫（Kendr）
- Atma Karak 是否落三角宫（Kon）
- Atma Karak 是否入旺
- Atma Karak 是否落本宫（own Bhava）

## 依赖方法

- 无

## 执行步骤

### ch40-v8-atma-karak-drishti-to-dharm-lord.step-001

- 动作：先认出 Atma Karak 与九宫主，核对 Atma Karak 是否相照九宫主，再看它落角宫、三角宫、入旺还是落本宫。
- 适用范围：仅限本命盘 Atma Karak 与九宫主一线；原文「and gives a Drishti to Dharm’s Lord」一句紧接在四项择一之后，本方法按它与四项择一并列成立的读法处理，原文本身没有写明它是否只限最后一项；原文未给时间限定。
- 原文最小意思：Atma Karak 落角宫（Kendr）、落三角宫（Kon）、入旺或落本宫（own Bhava），并相照九宫主时，命主将成为王之大臣。
- 本步骤产出事实：["Atma Karak 相照九宫主的大臣判定"]
- 所需事实：["本盘的 Atma Karak 是哪颗行星", "本盘九宫主（Dharm's Lord）是哪颗行星", "Atma Karak 是否相照九宫主（Dharm's Lord）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "Atma Karak 是否相照九宫主（Dharm's Lord）"}]}, {"operator": "OR", "operands": [{"fact_key": "Atma Karak 是否落角宫（Kendr）"}, {"fact_key": "Atma Karak 是否落三角宫（Kon）"}, {"fact_key": "Atma Karak 是否入旺"}, {"fact_key": "Atma Karak 是否落本宫（own Bhava）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "Atma Karak 是否相照九宫主（Dharm's Lord）"}]}, "required_fact_keys": ["Atma Karak 是否落角宫（Kendr）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落角宫（Kendr）"}, "selection_group": "ch40-v8-atma-karak-drishti-to-dharm-lord.step-001:atma-karak-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落角宫（Kendr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "Atma Karak 是否相照九宫主（Dharm's Lord）"}]}, "required_fact_keys": ["Atma Karak 是否落三角宫（Kon）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落三角宫（Kon）"}, "selection_group": "ch40-v8-atma-karak-drishti-to-dharm-lord.step-001:atma-karak-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落三角宫（Kon）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "Atma Karak 是否相照九宫主（Dharm's Lord）"}]}, "required_fact_keys": ["Atma Karak 是否入旺"], "branch_condition_logic": {"fact_key": "Atma Karak 是否入旺"}, "selection_group": "ch40-v8-atma-karak-drishti-to-dharm-lord.step-001:atma-karak-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否入旺。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "Atma Karak 是否相照九宫主（Dharm's Lord）"}]}, "required_fact_keys": ["Atma Karak 是否落本宫（own Bhava）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落本宫（own Bhava）"}, "selection_group": "ch40-v8-atma-karak-drishti-to-dharm-lord.step-001:atma-karak-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落本宫（own Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文写的是 Atma Karak 相照九宫主，不得反向当成九宫主相照 Atma Karak。", "不得据此推断职衔、俸禄或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Atma Karak 是哪颗行星、本盘九宫主（Dharm's Lord）是哪颗行星、Atma Karak 是否相照九宫主（Dharm's Lord）。
- 缺失即停字段：["本盘的 Atma Karak 是哪颗行星", "本盘九宫主（Dharm's Lord）是哪颗行星", "Atma Karak 是否相照九宫主（Dharm's Lord）"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v8`｜PDF [85]｜“If Atma Karak is in a Kendr, or in a Kon, or in exaltation, or in its own Bhava and gives a Drishti to Dharm’s Lord, the native will be a king’s minister.”


## 四路查书计划

### 支持路

- If Atma Karak is in a Kendr, or in a Kon, or in exaltation, or in its own Bhava and gives a Drishti to Dharm’s Lord
- Atma Karak 落角宫三角宫入旺本宫 相照九宫主 大臣

### 反例或取消路

- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- Yogas For Royal Association
- If Atma Karak is strong and is with a benefic, or Amatya Karak is in its own Bhava, or in exaltation

## 上游问题

- 无

## 停止条件

- Atma Karak 或九宫主的身份事实缺失时停止。
- Atma Karak 是否相照九宫主的事实缺失时停止。
- 四项落宫与尊贵事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
