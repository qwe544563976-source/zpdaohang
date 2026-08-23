---
method: ch40-v5-atma-karak-in-tanu-putr-dharm
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 必为王之大臣并有名声：Atma Karak 落一宫、五宫或九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会出名
- 我有没有辅政的机会

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Atma Karak 落在哪一宫

## 按情况检查的事实

- Atma Karak 是否落一宫（Tanu Bhava）
- Atma Karak 是否落五宫（Putr Bhava）
- Atma Karak 是否落九宫（Dharm Bhava）

## 依赖方法

- 无

## 执行步骤

### ch40-v5-atma-karak-in-tanu-putr-dharm.step-001

- 动作：先取 Atma Karak 的落宫，再核对它是否落在一宫（Tanu Bhava）、五宫（Putr Bhava）或九宫（Dharm Bhava）。
- 适用范围：仅限本命盘 Atma Karak 的落宫一项；原文本偈以「There is no doubt」立说，未附任何附加条件、时间限定或上升限定。
- 原文最小意思：Atma Karak 落一宫（Tanu Bhava）、五宫（Putr Bhava）或九宫（Dharm Bhava）时，命主成为王之大臣并有名声，此事无疑。
- 本步骤产出事实：["Atma Karak 三宫落宫的大臣与名声判定"]
- 所需事实：["本盘的 Atma Karak 落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "Atma Karak 是否落一宫（Tanu Bhava）"}, {"fact_key": "Atma Karak 是否落五宫（Putr Bhava）"}, {"fact_key": "Atma Karak 是否落九宫（Dharm Bhava）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘的 Atma Karak 落在哪一宫"}, "required_fact_keys": ["Atma Karak 是否落一宫（Tanu Bhava）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落一宫（Tanu Bhava）"}, "selection_group": "ch40-v5-atma-karak-in-tanu-putr-dharm.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落一宫（Tanu Bhava）。"}, {"when": {"fact_key": "本盘的 Atma Karak 落在哪一宫"}, "required_fact_keys": ["Atma Karak 是否落五宫（Putr Bhava）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落五宫（Putr Bhava）"}, "selection_group": "ch40-v5-atma-karak-in-tanu-putr-dharm.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落五宫（Putr Bhava）。"}, {"when": {"fact_key": "本盘的 Atma Karak 落在哪一宫"}, "required_fact_keys": ["Atma Karak 是否落九宫（Dharm Bhava）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落九宫（Dharm Bhava）"}, "selection_group": "ch40-v5-atma-karak-in-tanu-putr-dharm.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落九宫（Dharm Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写一宫、五宫、九宫三处，不得把这条断语套到 Atma Karak 落别的宫位。", "不得据此推断名声的领域、职衔或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Atma Karak 落在哪一宫。
- 缺失即停字段：["本盘的 Atma Karak 落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v5`｜PDF [85]｜“There is no doubt in one’s becoming a king’s minister and famous, if Atma Karak is in Tanu, or Putr, or Dharm Bhava.”


## 四路查书计划

### 支持路

- There is no doubt in one’s becoming a king’s minister and famous, if Atma Karak is in Tanu, or Putr, or Dharm Bhava
- Atma Karak 落一宫五宫九宫 大臣 有名

### 反例或取消路

- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- Karakāńś is the Navāńś, occupied by the Atma Karak Grah
- The Grah next to Atma Karak in terms of longitude is called Amatya Karak

### 判断方法路

- Yogas For Royal Association
- If Atma Karak, or Amatya Karak is placed in a Kendr, or in a Kon, the native will beget royal mercy

## 上游问题

- 无

## 停止条件

- Atma Karak 的落宫事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
