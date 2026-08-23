---
method: ch40-v6-karaks-in-kendr-or-kon-royal-mercy
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 得王之恩宠与庇护：Atma Karak 或 Amatya Karak 落角宫、三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 上面的人会不会关照我
- 我能不能得到当权者的庇护

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Atma Karak 落在哪一宫
- 本盘的 Amatya Karak 落在哪一宫

## 按情况检查的事实

- Atma Karak 是否落角宫（Kendr）
- Atma Karak 是否落三角宫（Kon）
- Amatya Karak 是否落角宫（Kendr）
- Amatya Karak 是否落三角宫（Kon）

## 依赖方法

- 无

## 执行步骤

### ch40-v6-karaks-in-kendr-or-kon-royal-mercy.step-001

- 动作：先取 Atma Karak 与 Amatya Karak 的落宫，再核对其中任一颗是否落角宫（Kendr）或三角宫（Kon）。
- 适用范围：仅限本命盘两个 Char Karak 的落宫；角宫与三角宫的名目本偈未列，须另按本书第 7 章 Kendras、Konas 的界定取得；原文未给时间限定。
- 原文最小意思：Atma Karak 落角宫（Kendr）或三角宫（Kon），或 Amatya Karak 落角宫（Kendr）或三角宫（Kon）时，命主将得到王之恩宠、王之庇护以及由此而来的安乐。
- 本步骤产出事实：["两个 Char Karak 落角宫三角宫的王家恩宠判定"]
- 所需事实：["本盘的 Atma Karak 落在哪一宫", "本盘的 Amatya Karak 落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"fact_key": "本盘的 Amatya Karak 落在哪一宫"}]}, {"operator": "OR", "operands": [{"fact_key": "Atma Karak 是否落角宫（Kendr）"}, {"fact_key": "Atma Karak 是否落三角宫（Kon）"}, {"fact_key": "Amatya Karak 是否落角宫（Kendr）"}, {"fact_key": "Amatya Karak 是否落三角宫（Kon）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"fact_key": "本盘的 Amatya Karak 落在哪一宫"}]}, "required_fact_keys": ["Atma Karak 是否落角宫（Kendr）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落角宫（Kendr）"}, "selection_group": "ch40-v6-karaks-in-kendr-or-kon-royal-mercy.step-001:which-karak-and-place", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落角宫（Kendr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"fact_key": "本盘的 Amatya Karak 落在哪一宫"}]}, "required_fact_keys": ["Atma Karak 是否落三角宫（Kon）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落三角宫（Kon）"}, "selection_group": "ch40-v6-karaks-in-kendr-or-kon-royal-mercy.step-001:which-karak-and-place", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落三角宫（Kon）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"fact_key": "本盘的 Amatya Karak 落在哪一宫"}]}, "required_fact_keys": ["Amatya Karak 是否落角宫（Kendr）"], "branch_condition_logic": {"fact_key": "Amatya Karak 是否落角宫（Kendr）"}, "selection_group": "ch40-v6-karaks-in-kendr-or-kon-royal-mercy.step-001:which-karak-and-place", "stop_condition": "选中该分支后，缺少以下事实即停止：Amatya Karak 是否落角宫（Kendr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"fact_key": "本盘的 Amatya Karak 落在哪一宫"}]}, "required_fact_keys": ["Amatya Karak 是否落三角宫（Kon）"], "branch_condition_logic": {"fact_key": "Amatya Karak 是否落三角宫（Kon）"}, "selection_group": "ch40-v6-karaks-in-kendr-or-kon-royal-mercy.step-001:which-karak-and-place", "stop_condition": "选中该分支后，缺少以下事实即停止：Amatya Karak 是否落三角宫（Kon）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写角宫与三角宫两类位置，不得扩大到续宫、果宫或别的宫位。", "不得据此推断恩宠来自谁、以什么形式出现或在何时出现。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Atma Karak 落在哪一宫、本盘的 Amatya Karak 落在哪一宫。
- 缺失即停字段：["本盘的 Atma Karak 落在哪一宫", "本盘的 Amatya Karak 落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v6`｜PDF [85]｜“If Atma Karak, or Amatya Karak is placed in a Kendr, or in a Kon, the native will beget royal mercy, royal patronage and happiness thereof.”


## 四路查书计划

### 支持路

- If Atma Karak, or Amatya Karak is placed in a Kendr, or in a Kon, the native will beget royal mercy, royal patronage and happiness thereof
- Atma Karak Amatya Karak 落角宫三角宫 王之恩宠

### 反例或取消路

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

- 两个 Char Karak 的落宫事实全部缺失时停止。
- 角宫、三角宫的名目未按本书第 7 章界定取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
