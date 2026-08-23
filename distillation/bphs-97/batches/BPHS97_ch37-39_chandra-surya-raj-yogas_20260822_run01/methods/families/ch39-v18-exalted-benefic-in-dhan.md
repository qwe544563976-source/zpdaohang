---
method: ch39-v18-exalted-benefic-in-dhan
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮、木星、金星、水星之一在二宫入旺：富有

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的财运怎么样
- 二宫里有入旺的行星说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘二宫（Dhan Bhava）内有哪些行星

## 按情况检查的事实

- 月亮（Chandra）是否落二宫（Dhan）
- 月亮（Chandra）是否入旺
- 木星（Guru）是否落二宫（Dhan）
- 木星（Guru）是否入旺
- 金星（Shukra）是否落二宫（Dhan）
- 金星（Shukra）是否入旺
- 水星（Budh）是否落二宫（Dhan）
- 水星（Budh）是否入旺

## 依赖方法

- 无

## 执行步骤

### ch39-v18-exalted-benefic-in-dhan.step-001

- 动作：先看二宫（Dhan Bhava）内有哪些行星，再核对其中是否有月亮、木星、金星或水星入旺。
- 适用范围：仅限本命盘财富主题；原文只列这四颗行星，没有时间限定。
- 原文最小意思：月亮（Chandra）、木星（Guru）、金星（Shukra）与水星（Budh）之中有一颗在二宫（Dhan Bhava）入旺时，命主会富有。
- 本步骤产出事实：["二宫入旺吉星的富有判定"]
- 所需事实：["本盘二宫（Dhan Bhava）内有哪些行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘二宫（Dhan Bhava）内有哪些行星"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落二宫（Dhan）"}, {"fact_key": "月亮（Chandra）是否入旺"}]}, {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落二宫（Dhan）"}, {"fact_key": "木星（Guru）是否入旺"}]}, {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落二宫（Dhan）"}, {"fact_key": "金星（Shukra）是否入旺"}]}, {"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落二宫（Dhan）"}, {"fact_key": "水星（Budh）是否入旺"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘二宫（Dhan Bhava）内有哪些行星"}, "required_fact_keys": ["月亮（Chandra）是否落二宫（Dhan）", "月亮（Chandra）是否入旺"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落二宫（Dhan）"}, {"fact_key": "月亮（Chandra）是否入旺"}]}, "selection_group": "ch39-v18-exalted-benefic-in-dhan.step-001:which-graha", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落二宫（Dhan）、月亮（Chandra）是否入旺。"}, {"when": {"fact_key": "本盘二宫（Dhan Bhava）内有哪些行星"}, "required_fact_keys": ["木星（Guru）是否落二宫（Dhan）", "木星（Guru）是否入旺"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落二宫（Dhan）"}, {"fact_key": "木星（Guru）是否入旺"}]}, "selection_group": "ch39-v18-exalted-benefic-in-dhan.step-001:which-graha", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落二宫（Dhan）、木星（Guru）是否入旺。"}, {"when": {"fact_key": "本盘二宫（Dhan Bhava）内有哪些行星"}, "required_fact_keys": ["金星（Shukra）是否落二宫（Dhan）", "金星（Shukra）是否入旺"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落二宫（Dhan）"}, {"fact_key": "金星（Shukra）是否入旺"}]}, "selection_group": "ch39-v18-exalted-benefic-in-dhan.step-001:which-graha", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落二宫（Dhan）、金星（Shukra）是否入旺。"}, {"when": {"fact_key": "本盘二宫（Dhan Bhava）内有哪些行星"}, "required_fact_keys": ["水星（Budh）是否落二宫（Dhan）", "水星（Budh）是否入旺"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落二宫（Dhan）"}, {"fact_key": "水星（Budh）是否入旺"}]}, "selection_group": "ch39-v18-exalted-benefic-in-dhan.step-001:which-graha", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落二宫（Dhan）、水星（Budh）是否入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只列四颗行星，不得把别的行星在二宫入旺也算进来。", "不得据此推断财富数额或发财时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘二宫（Dhan Bhava）内有哪些行星。
- 缺失即停字段：["本盘二宫（Dhan Bhava）内有哪些行星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v18`｜PDF [83]｜“The native will be wealthy, if one among Chandra, Guru, Shukra and Budh is exalted in Dhan Bhava.”


## 四路查书计划

### 支持路

- The native will be wealthy, if one among Chandra, Guru, Shukra and Budh is exalted in Dhan Bhava
- 二宫入旺 月亮木星金星水星 富有

### 反例或取消路

- Should Mangal and Shani be together in Dhan Bhava, the native’s wealth will be destroyed
- Surya in Dhan Bhava, receiving a Drishti from Shani, will cause penury

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- Dharm’s Lord and Putr’s Lord are capable of bestowing wealth

## 上游问题

- 无

## 停止条件

- 缺少二宫占据事实时停止。
- 四颗行星的落宫与入旺事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
