---
method: ch41-v9-surya-in-simh-lagn-with-mangal-guru
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 富有：上升为狮子座并有太阳，太阳与火星木星同宫或受其相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子会不会有钱
- 我的财力靠什么起来

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升（Lagn）落在哪个星座
- 上升（Lagn）是否落在狮子座（Simh）
- 太阳（Surya）是否落上升宫（Lagna）

## 按情况检查的事实

- 太阳（Surya）是否与火星（Mangal）同宫
- 太阳（Surya）是否与木星（Guru）同宫
- 太阳（Surya）是否被火星（Mangal）相照
- 太阳（Surya）是否被木星（Guru）相照

## 依赖方法

- 无

## 执行步骤

### ch41-v9-surya-in-simh-lagn-with-mangal-guru.step-001

- 动作：先取上升所落星座并核对太阳（Surya）的落宫，再看它与原文点名的诸行星是同宫还是受其相照。
- 适用范围：仅限本命盘上升为狮子座且太阳在上升宫的配置；原文本组自带小标题「Yogas for Wealth (up to Sloka 15)」；原文的「yuti with, or receiving a Drishti from Mangal and Guru」一句同时管两颗行星，本方法按同宫与相照两条分支处理，两颗行星在同一分支内同时成立；原文未给时间限定。
- 原文最小意思：上升（Lagn）即狮子座（Simh）并有太阳（Surya）在其中，且太阳与火星（Mangal）和木星（Guru）同宫或受二者相照时，命主将富有。
- 本步骤产出事实：["太阳（Surya）落上升宫的富有判定"]
- 所需事实：["本盘上升（Lagn）落在哪个星座", "上升（Lagn）是否落在狮子座（Simh）", "太阳（Surya）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）落在哪个星座"}, {"fact_key": "上升（Lagn）是否落在狮子座（Simh）"}, {"fact_key": "太阳（Surya）是否落上升宫（Lagna）"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否与火星（Mangal）同宫"}, {"fact_key": "太阳（Surya）是否与木星（Guru）同宫"}]}, {"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否被火星（Mangal）相照"}, {"fact_key": "太阳（Surya）是否被木星（Guru）相照"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）落在哪个星座"}, {"fact_key": "上升（Lagn）是否落在狮子座（Simh）"}, {"fact_key": "太阳（Surya）是否落上升宫（Lagna）"}]}, "required_fact_keys": ["太阳（Surya）是否与火星（Mangal）同宫", "太阳（Surya）是否与木星（Guru）同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否与火星（Mangal）同宫"}, {"fact_key": "太阳（Surya）是否与木星（Guru）同宫"}]}, "selection_group": "ch41-v9-surya-in-simh-lagn-with-mangal-guru.step-001:relation-kind", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否与火星（Mangal）同宫、太阳（Surya）是否与木星（Guru）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）落在哪个星座"}, {"fact_key": "上升（Lagn）是否落在狮子座（Simh）"}, {"fact_key": "太阳（Surya）是否落上升宫（Lagna）"}]}, "required_fact_keys": ["太阳（Surya）是否被火星（Mangal）相照", "太阳（Surya）是否被木星（Guru）相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否被火星（Mangal）相照"}, {"fact_key": "太阳（Surya）是否被木星（Guru）相照"}]}, "selection_group": "ch41-v9-surya-in-simh-lagn-with-mangal-guru.step-001:relation-kind", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否被火星（Mangal）相照、太阳（Surya）是否被木星（Guru）相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文点名火星与木星两颗，不得只有其中一颗就下断。", "不得据此推断财富数额、来源或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagn）落在哪个星座、上升（Lagn）是否落在狮子座（Simh）、太阳（Surya）是否落上升宫（Lagna）。
- 缺失即停字段：["本盘上升（Lagn）落在哪个星座", "上升（Lagn）是否落在狮子座（Simh）", "太阳（Surya）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch41:v9`｜PDF [86]｜“Should Surya be in Simh identical with Lagn and be yuti with, or receiving a Drishti from Mangal and Guru, one will be wealthy.”


## 四路查书计划

### 支持路

- Should Surya be in Simh identical with Lagn and be yuti with, or receiving a Drishti from Mangal and Guru, one will be wealthy
- 上升狮子座有太阳 火星木星同宫或相照 富有

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava

### 适用边界路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

### 判断方法路

- Combinations for Wealth
- Should Chandra be in Kark identical with Lagn and be yuti with, or receiving a Drishti from Budh and Guru

## 上游问题

- 无

## 停止条件

- 上升所落星座未取到时停止。
- 太阳是否落上升宫的事实缺失时停止。
- 同宫与相照两类关系事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
