---
method: ch21-v8-10-karm-labh-lords-happy-life
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 过上幸福的生活：十一宫主落十宫且十宫主落上升宫，或两宫主在角宫同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子过得幸不幸福
- 十宫主与十一宫主互涉有什么效果

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘十宫主（Karm's Lord）落在哪一宫

## 按情况检查的事实

- 十一宫主（Labh's Lord）是否落十宫（Karm）
- 十宫主（Karm's Lord）是否落上升宫（Lagna）
- 十宫主（Karm's Lord）是否与十一宫主（Labh's Lord）同宫
- 十宫主（Karm's Lord）是否落角宫

## 依赖方法

- 无

## 执行步骤

### ch21-v8-10-karm-labh-lords-happy-life.step-001

- 动作：取十宫主（Karm's Lord）所落的宫，核对是十一宫主落十宫且十宫主落上升宫，还是十宫主与十一宫主在角宫同宫。
- 适用范围：仅限原文这一句给出的两种配置；原文未给上升与时间限定，也没有列出角宫的具体宫位。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：十一宫主落十宫且十宫主落上升宫，或十宫主与十一宫主在角宫同宫时，命主会过上幸福的生活。
- 本步骤产出事实：["十宫主与十一宫主互涉的幸福生活判定"]
- 所需事实：["本盘十宫主（Karm's Lord）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落十宫（Karm）"}, {"fact_key": "十宫主（Karm's Lord）是否落上升宫（Lagna）"}]}, {"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否与十一宫主（Labh's Lord）同宫"}, {"fact_key": "十宫主（Karm's Lord）是否落角宫"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落十宫（Karm）", "十宫主（Karm's Lord）是否落上升宫（Lagna）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落十宫（Karm）"}, {"fact_key": "十宫主（Karm's Lord）是否落上升宫（Lagna）"}]}, "selection_group": "ch21-v8-10-karm-labh-lords-happy-life.step-001:karm-labh-configuration", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落十宫（Karm）、十宫主（Karm's Lord）是否落上升宫（Lagna）。"}, {"when": {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, "required_fact_keys": ["十宫主（Karm's Lord）是否与十一宫主（Labh's Lord）同宫", "十宫主（Karm's Lord）是否落角宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否与十一宫主（Labh's Lord）同宫"}, {"fact_key": "十宫主（Karm's Lord）是否落角宫"}]}, "selection_group": "ch21-v8-10-karm-labh-lords-happy-life.step-001:karm-labh-configuration", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否与十一宫主（Labh's Lord）同宫、十宫主（Karm's Lord）是否落角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、婚姻或寿命。", "不得把两种配置里的任一半条件单独当成成立条件。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘十宫主（Karm's Lord）落在哪一宫。
- 缺失即停字段：["本盘十宫主（Karm's Lord）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v8-10`｜PDF [38]｜“One will lead a happy life, if Labh’s Lord is in Karm and Karm’s Lord is in Lagna, or, if the Lord of Karm Bhava is yuti with the Lord of Labh Bhava in an angle.”


## 四路查书计划

### 支持路

- One will lead a happy life, if Labh’s Lord is in Karm and Karm’s Lord is in Lagna, or, if the Lord of Karm Bhava is yuti with the Lord of Labh Bhava in an angle
- 十一宫主落十宫 十宫主落上升 两宫主角宫同宫 幸福生活

### 反例或取消路

- If Karm’s Lord is in Randhr Bhava, the native will be devoid of acts, long-lived and intent on blaming others
- Should Rahu, Surya, Shani and Mangal be in Labh Bhava, the native will incur cessation of his duties
- 十宫主落八宫 无所作为

### 适用边界路

- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- If Labh’s Lord is in Karm Bhava, the native will be honoured by the king, be virtuous, attached to his religion
- Indications of Labh Bhava. All articles, son’s wife, income, prosperity, quadrupeds etc. are to be understood from Labh Bhava

### 判断方法路

- Effects of Karm’s Lord in Various Bhavas
- 判断十宫主与十一宫主互涉要查哪些位置

## 上游问题

- 无

## 停止条件

- 缺少十宫主落宫事实时停止。
- 缺少被命中那一组配置里的任一事实时停止。
- 角宫的宫位界定未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
