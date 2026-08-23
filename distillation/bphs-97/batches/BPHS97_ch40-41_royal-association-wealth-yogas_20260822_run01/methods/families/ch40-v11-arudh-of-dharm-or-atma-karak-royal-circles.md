---
method: ch40-v11-arudh-of-dharm-or-atma-karak-royal-circles
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 与王室圈子相往还：九宫的 Arudh 即本命上升，或 Atma Karak 落九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会跟有权势的圈子搭上关系
- 我的贵人从哪儿来

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘九宫（Dharm Bhava）的 Arudh 落在哪一宫
- 本盘的 Atma Karak 落在哪一宫

## 按情况检查的事实

- 九宫（Dharm Bhava）的 Arudh 是否即本命上升宫（Janm Lagn）
- Atma Karak 是否落九宫（Dharm Bhava）

## 依赖方法

- 无

## 执行步骤

### ch40-v11-arudh-of-dharm-or-atma-karak-royal-circles.step-001

- 动作：先取九宫（Dharm Bhava）的 Arudh 与 Atma Karak 的落宫，再核对该 Arudh 是否落在本命上升宫，或 Atma Karak 是否落九宫。
- 适用范围：仅限本命盘九宫的 Arudh 与 Atma Karak 落宫两支；Arudh 的算法本偈未给，须另按本书 Arudh 一章取得；原文未给时间限定。
- 原文最小意思：九宫（Dharm Bhava）的 Arudh 本身即是本命上升，或 Atma Karak 落九宫（Dharm Bhava）时，命主将与王室圈子相往还。
- 本步骤产出事实：["九宫 Arudh 与 Atma Karak 的王室往还判定"]
- 所需事实：["本盘九宫（Dharm Bhava）的 Arudh 落在哪一宫", "本盘的 Atma Karak 落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘九宫（Dharm Bhava）的 Arudh 落在哪一宫"}, {"fact_key": "本盘的 Atma Karak 落在哪一宫"}]}, {"operator": "OR", "operands": [{"fact_key": "九宫（Dharm Bhava）的 Arudh 是否即本命上升宫（Janm Lagn）"}, {"fact_key": "Atma Karak 是否落九宫（Dharm Bhava）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘九宫（Dharm Bhava）的 Arudh 落在哪一宫"}, {"fact_key": "本盘的 Atma Karak 落在哪一宫"}]}, "required_fact_keys": ["九宫（Dharm Bhava）的 Arudh 是否即本命上升宫（Janm Lagn）"], "branch_condition_logic": {"fact_key": "九宫（Dharm Bhava）的 Arudh 是否即本命上升宫（Janm Lagn）"}, "selection_group": "ch40-v11-arudh-of-dharm-or-atma-karak-royal-circles.step-001:which-route", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫（Dharm Bhava）的 Arudh 是否即本命上升宫（Janm Lagn）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘九宫（Dharm Bhava）的 Arudh 落在哪一宫"}, {"fact_key": "本盘的 Atma Karak 落在哪一宫"}]}, "required_fact_keys": ["Atma Karak 是否落九宫（Dharm Bhava）"], "branch_condition_logic": {"fact_key": "Atma Karak 是否落九宫（Dharm Bhava）"}, "selection_group": "ch40-v11-arudh-of-dharm-or-atma-karak-royal-circles.step-001:which-route", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落九宫（Dharm Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写九宫的 Arudh 与 Atma Karak 两支，不得把别的宫的 Arudh 一并套用。", "不得据此推断具体交往对象、职位或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘九宫（Dharm Bhava）的 Arudh 落在哪一宫、本盘的 Atma Karak 落在哪一宫。
- 缺失即停字段：["本盘九宫（Dharm Bhava）的 Arudh 落在哪一宫", "本盘的 Atma Karak 落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v11`｜PDF [85]｜“If the Arudh of Dharm Bhava happens to be itself the Janm Lagna, or, if Atma Karak is placed in Dharm Bhava, the native will be associated with royal circles.”


## 四路查书计划

### 支持路

- If the Arudh of Dharm Bhava happens to be itself the Janm Lagna, or, if Atma Karak is placed in Dharm Bhava
- 九宫 Arudh 即本命上升 Atma Karak 落九宫 王室圈子

### 反例或取消路

- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- Karakāńś is the Navāńś, occupied by the Atma Karak Grah
- The Grah next to Atma Karak in terms of longitude is called Amatya Karak

### 判断方法路

- Yogas For Royal Association
- one will be related to royal circles, if Shukra is the Karakāńś, or in the 5<sup>th</sup> there from

## 上游问题

- 无

## 停止条件

- 九宫的 Arudh 未按本书 Arudh 一章算出时，该分支停判。
- Atma Karak 的落宫事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
