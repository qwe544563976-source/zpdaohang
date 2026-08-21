---
method: ch12-v5-7-budh-guru-shukra-royal-marks
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 具王者标记：水木金与月亮同落一宫，或落从上升起算的角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身上有没有贵气的标记
- 水星木星金星与月亮同宫代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘一宫（Lagn）落在哪个星座

## 按情况检查的事实

- 水星（Budh）是否落一宫（Tanu）
- 木星（Guru）是否落一宫（Tanu）
- 金星（Shukra）是否落一宫（Tanu）
- 月亮（Chandra）是否落一宫（Tanu）
- 水星（Budh）是否落角宫
- 木星（Guru）是否落角宫
- 金星（Shukra）是否落角宫

## 依赖方法

- 无

## 执行步骤

### ch12-v5-7-budh-guru-shukra-royal-marks.step-001

- 动作：核对水星、木星、金星是否与月亮同落一宫，或是否落在从上升起算的角宫。
- 适用范围：仅限本命盘一宫（Tanu Bhava）王者标记主题；原文没有说明这些标记具体是什么形状或在哪个部位。
- 原文最小意思：水星（Budh）、木星（Guru）或金星（Shukra）与月亮（Chandra）一同落一宫（Lagn），或落从上升起算的角宫时，命主会具备王者的（吉祥）标记。
- 本步骤产出事实：["水木金与月亮同宫或落角宫的王者标记判定"]
- 所需事实：["本盘一宫（Lagn）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘一宫（Lagn）落在哪个星座"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, {"fact_key": "水星（Budh）是否落角宫"}, {"fact_key": "木星（Guru）是否落角宫"}, {"fact_key": "金星（Shukra）是否落角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["水星（Budh）是否落一宫（Tanu）", "月亮（Chandra）是否落一宫（Tanu）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-marks.step-001:royal-mark-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落一宫（Tanu）、月亮（Chandra）是否落一宫（Tanu）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["木星（Guru）是否落一宫（Tanu）", "月亮（Chandra）是否落一宫（Tanu）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-marks.step-001:royal-mark-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落一宫（Tanu）、月亮（Chandra）是否落一宫（Tanu）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落一宫（Tanu）", "月亮（Chandra）是否落一宫（Tanu）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-marks.step-001:royal-mark-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落一宫（Tanu）、月亮（Chandra）是否落一宫（Tanu）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["水星（Budh）是否落角宫"], "branch_condition_logic": {"fact_key": "水星（Budh）是否落角宫"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-marks.step-001:royal-mark-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落角宫。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["木星（Guru）是否落角宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落角宫"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-marks.step-001:royal-mark-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落角宫。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落角宫"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落角宫"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-marks.step-001:royal-mark-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 royal marks 读成实际的王位或官职，本句只说标记。", "不得指定标记的部位或形状，原文没有写。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘一宫（Lagn）落在哪个星座。
- 缺失即停字段：["本盘一宫（Lagn）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v5-7`｜PDF [26, 27]｜“One will be endowed with royal marks (of fortune), if Budh, Guru, or Shukra be in Lagn along with the Chandra, or be in angle from Lagn.”


## 四路查书计划

### 支持路

- One will be endowed with royal marks (of fortune), if Budh, Guru, or Shukra be in Lagn along with the Chandra, or be in angle from Lagn
- 水星木星金星与月亮同落一宫 或落角宫 王者标记

### 反例或取消路

- Should Lagn Lord be yuti with a malefic, or be in Randhr, 6th, or 12th, physical felicity will diminish
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- A mole, spot, or figure, formed by hair on the left side of a woman and right side of a man is auspicious

### 判断方法路

- Now I will describe to you the effects of moles, marks, spots and signs, found on the body of women and men
- Effects of Moles, Marks, Signs etc. for Men and Women
- 判断王者标记要看水木金与月亮的位置

## 上游问题

- 无

## 停止条件

- 缺少上升星座事实时停止。
- 六个分支事实全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
