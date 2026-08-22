---
method: ch29-v25-guru-shukra-chandra-seventh-very-wealthy
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 木星、金星、月亮居上升 Pad 起第 7 宫：极为富有

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会很有钱
- 哪些星在财位最旺

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升 Pad（Lagn Pad）落在哪一宫

## 按情况检查的事实

- 木星（Guru）是否落上升 Pad（Lagn Pad）起第 7 宫
- 金星（Shukra）是否落上升 Pad（Lagn Pad）起第 7 宫
- 月亮（Chandra）是否落上升 Pad（Lagn Pad）起第 7 宫

## 依赖方法

- 无

## 执行步骤

### ch29-v25-guru-shukra-chandra-seventh-very-wealthy.step-001

- 动作：先定出本盘上升 Pad（Lagn Pad）落在哪一宫，再看木星（Guru）、金星（Shukra）、月亮（Chandra）之中有哪几颗落其起第 7 宫。
- 适用范围：本条以上升 Pad（Lagn Pad）为起算点；原文说三者中有一颗、两颗或三颗都可，未给三者之间的轻重差别。
- 原文最小意思：木星（Guru）、金星（Shukra）、月亮（Chandra）三者之中有一颗、两颗、或三颗都落上升 Pad（Lagn Pad）起第 7 宫时，命主极为富有。
- 本步骤产出事实：["上升 Pad 起第 7 宫三吉星的富有判定"]
- 所需事实：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "木星（Guru）是否落上升 Pad（Lagn Pad）起第 7 宫"}, {"fact_key": "金星（Shukra）是否落上升 Pad（Lagn Pad）起第 7 宫"}, {"fact_key": "月亮（Chandra）是否落上升 Pad（Lagn Pad）起第 7 宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["木星（Guru）是否落上升 Pad（Lagn Pad）起第 7 宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落上升 Pad（Lagn Pad）起第 7 宫"}, "selection_group": "ch29-v25-guru-shukra-chandra-seventh-very-wealthy.step-001:occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落上升 Pad（Lagn Pad）起第 7 宫。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["金星（Shukra）是否落上升 Pad（Lagn Pad）起第 7 宫"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落上升 Pad（Lagn Pad）起第 7 宫"}, "selection_group": "ch29-v25-guru-shukra-chandra-seventh-very-wealthy.step-001:occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落上升 Pad（Lagn Pad）起第 7 宫。"}, {"when": {"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, "required_fact_keys": ["月亮（Chandra）是否落上升 Pad（Lagn Pad）起第 7 宫"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落上升 Pad（Lagn Pad）起第 7 宫"}, "selection_group": "ch29-v25-guru-shukra-chandra-seventh-very-wealthy.step-001:occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落上升 Pad（Lagn Pad）起第 7 宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额或来源。", "原文未给三者的轻重差别，不得自行排出强弱次序。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升 Pad（Lagn Pad）落在哪一宫。
- 缺失即停字段：["本盘上升 Pad（Lagn Pad）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v25`｜PDF [63]｜“Should one, two, or all three of Guru, Shukra and Chandra be in the 7<sup>th</sup> from Lagn Pad, the native will be very wealthy.”


## 四路查书计划

### 支持路

- Should one, two, or all three of Guru, Shukra and Chandra be in the 7<sup>th</sup> from Lagn Pad, the native will be very wealthy.
- 木星金星月亮落上升 Pad 起第 7 宫 极为富有

### 反例或取消路

- If the Dar Pad falls in the 6<sup>th</sup> / 8<sup>th</sup> /12<sup>th</sup> from Lagn Pad, then the native will be poor.
- Dar Pad 落 6、8、12 宫时的贫穷条

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- O Brahmin, these Yogas, as narrated by me with reference to the 7<sup>th</sup> from Lagn Pad, should also be considered from the 2<sup>nd</sup> of Lagn Pad.
- 同一批断语也从上升 Pad 起第 2 宫考察

### 判断方法路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 上升 Pad 怎么求

## 上游问题

- 无

## 停止条件

- 缺少本盘上升 Pad（Lagn Pad）落宫事实时停止。
- 缺少木星、金星、月亮相对上升 Pad 起第 7 宫的落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
