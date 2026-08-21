---
method: ch13-v3-guru-in-dhan-wealth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 富有：木星身为二宫主落二宫，或木星与火星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子有没有钱
- 木星落二宫对我的财富意味着什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘木星（Guru）落在哪一宫

## 按情况检查的事实

- 木星（Guru）是否落二宫（Dhan）
- 木星（Guru）是否为二宫主（Dhan's Lord）
- 木星（Guru）是否与火星（Mangal）同宫

## 依赖方法

- 无

## 执行步骤

### ch13-v3-guru-in-dhan-wealth.step-001

- 动作：先取木星（Guru）的落宫，再分别核对「木星身为二宫主落二宫」与「木星与火星同宫」两种情形，判断财富。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；原文第二个可选条件写作 or is with Mangal，只说木星与火星同宫、未复述落宫，此处按原文字面处理，不补落宫限定。
- 原文最小意思：木星（Guru）身为二宫主（Lord of Dhan）落二宫（Dhan），或木星与火星（Mangal）同宫时，命主富有。
- 本步骤产出事实：["木星与二宫的富有判定"]
- 所需事实：["本盘木星（Guru）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘木星（Guru）落在哪一宫"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落二宫（Dhan）"}, {"fact_key": "木星（Guru）是否为二宫主（Dhan's Lord）"}]}, {"fact_key": "木星（Guru）是否与火星（Mangal）同宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘木星（Guru）落在哪一宫"}, "required_fact_keys": ["木星（Guru）是否落二宫（Dhan）", "木星（Guru）是否为二宫主（Dhan's Lord）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落二宫（Dhan）"}, {"fact_key": "木星（Guru）是否为二宫主（Dhan's Lord）"}]}, "selection_group": "ch13-v3-guru-in-dhan-wealth.step-001:guru-wealth-configuration", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落二宫（Dhan）、木星（Guru）是否为二宫主（Dhan's Lord）。"}, {"when": {"fact_key": "本盘木星（Guru）落在哪一宫"}, "required_fact_keys": ["木星（Guru）是否与火星（Mangal）同宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否与火星（Mangal）同宫"}, "selection_group": "ch13-v3-guru-in-dhan-wealth.step-001:guru-wealth-configuration", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否与火星（Mangal）同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、来源或得财时间。", "不得把两个可选条件合并成必须同时成立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘木星（Guru）落在哪一宫。
- 缺失即停字段：["本盘木星（Guru）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v3`｜PDF [27]｜“One will be wealthy, if Guru is in Dhan, as the Lord of Dhan, or is with Mangal.”


## 四路查书计划

### 支持路

- One will be wealthy, if Guru is in Dhan, as the Lord of Dhan, or is with Mangal
- 木星身为二宫主落二宫 木星与火星同宫 富有

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic
- Should Mangal and Shani be together in Dhan Bhava, the native’s wealth will be destroyed
- A benefic in Dhan will give wealth, while a malefic instead will destroy wealth

### 适用边界路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- If the Lord of Dhan is in Dhan, or is in an angle, or in trine, he will promote one’s wealth (or monetary state)

### 判断方法路

- If Dhan’s Lord is in Dhan Bhava, the native will be wealthy, proud, will have two, or more wives and be bereft of progeny
- The native will be wealthy, if one among Chandra, Guru, Shukra and Budh is exalted in Dhan Bhava
- 判断财富要看二宫和二宫主落在哪里

## 上游问题

- 无

## 停止条件

- 缺少木星（Guru）落宫事实时停止。
- 「木星身为二宫主落二宫」与「木星与火星同宫」两个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
