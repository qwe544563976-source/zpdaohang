---
method: ch41-v11-mangal-in-own-lagn-with-budh-shukra-shani
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 富有：上升为火星自己的星座并有火星，火星与水金土同宫或受其相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的钱能挣到什么程度
- 我的财靠自己打拼得来吗

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升（Lagn）落在哪个星座
- 上升（Lagn）是否为火星（Mangal）主管的星座（Rāśi）
- 火星（Mangal）是否落上升宫（Lagna）

## 按情况检查的事实

- 火星（Mangal）是否与水星（Budh）同宫
- 火星（Mangal）是否与金星（Shukra）同宫
- 火星（Mangal）是否与土星（Shani）同宫
- 火星（Mangal）是否被水星（Budh）相照
- 火星（Mangal）是否被金星（Shukra）相照
- 火星（Mangal）是否被土星（Shani）相照

## 依赖方法

- 无

## 执行步骤

### ch41-v11-mangal-in-own-lagn-with-budh-shukra-shani.step-001

- 动作：先取上升所落星座并核对火星（Mangal）的落宫，再看它与原文点名的诸行星是同宫还是受其相照。
- 适用范围：仅限本命盘上升为火星自己主管的星座且火星在上升宫的配置；原文此处写的是 his own Rāśi（自己主管的星座），不是本宫；本条属本章「Yogas for Wealth (up to Sloka 15)」一组；原文的关系一句同时管三颗行星，本方法按同宫与相照两条分支处理，三颗行星在同一分支内同时成立；原文未给时间限定。
- 原文最小意思：上升（Lagn）即火星（Mangal）自己主管的星座（own Rāśi）并有火星在其中，且火星与水星（Budh）、金星（Shukra）和土星（Shani）同宫或受三者相照时，命主将富有。
- 本步骤产出事实：["火星（Mangal）落上升宫的富有判定"]
- 所需事实：["本盘上升（Lagn）落在哪个星座", "上升（Lagn）是否为火星（Mangal）主管的星座（Rāśi）", "火星（Mangal）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）落在哪个星座"}, {"fact_key": "上升（Lagn）是否为火星（Mangal）主管的星座（Rāśi）"}, {"fact_key": "火星（Mangal）是否落上升宫（Lagna）"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否与水星（Budh）同宫"}, {"fact_key": "火星（Mangal）是否与金星（Shukra）同宫"}, {"fact_key": "火星（Mangal）是否与土星（Shani）同宫"}]}, {"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否被水星（Budh）相照"}, {"fact_key": "火星（Mangal）是否被金星（Shukra）相照"}, {"fact_key": "火星（Mangal）是否被土星（Shani）相照"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）落在哪个星座"}, {"fact_key": "上升（Lagn）是否为火星（Mangal）主管的星座（Rāśi）"}, {"fact_key": "火星（Mangal）是否落上升宫（Lagna）"}]}, "required_fact_keys": ["火星（Mangal）是否与水星（Budh）同宫", "火星（Mangal）是否与金星（Shukra）同宫", "火星（Mangal）是否与土星（Shani）同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否与水星（Budh）同宫"}, {"fact_key": "火星（Mangal）是否与金星（Shukra）同宫"}, {"fact_key": "火星（Mangal）是否与土星（Shani）同宫"}]}, "selection_group": "ch41-v11-mangal-in-own-lagn-with-budh-shukra-shani.step-001:relation-kind", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否与水星（Budh）同宫、火星（Mangal）是否与金星（Shukra）同宫、火星（Mangal）是否与土星（Shani）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）落在哪个星座"}, {"fact_key": "上升（Lagn）是否为火星（Mangal）主管的星座（Rāśi）"}, {"fact_key": "火星（Mangal）是否落上升宫（Lagna）"}]}, "required_fact_keys": ["火星（Mangal）是否被水星（Budh）相照", "火星（Mangal）是否被金星（Shukra）相照", "火星（Mangal）是否被土星（Shani）相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否被水星（Budh）相照"}, {"fact_key": "火星（Mangal）是否被金星（Shukra）相照"}, {"fact_key": "火星（Mangal）是否被土星（Shani）相照"}]}, "selection_group": "ch41-v11-mangal-in-own-lagn-with-budh-shukra-shani.step-001:relation-kind", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否被水星（Budh）相照、火星（Mangal）是否被金星（Shukra）相照、火星（Mangal）是否被土星（Shani）相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文点名水星、金星与土星三颗，不得少一颗就下断。", "不得据此推断财富数额、来源或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagn）落在哪个星座、上升（Lagn）是否为火星（Mangal）主管的星座（Rāśi）、火星（Mangal）是否落上升宫（Lagna）。
- 缺失即停字段：["本盘上升（Lagn）落在哪个星座", "上升（Lagn）是否为火星（Mangal）主管的星座（Rāśi）", "火星（Mangal）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch41:v11`｜PDF [86]｜“Should Mangal be in Lagn identical with his own Rashiand be yuti with, or receiving a Drishti from Budh, Shukra and Shani, the native will be rich.”


## 四路查书计划

### 支持路

- Should Mangal be in Lagn identical with his own Rashiand be yuti with, or receiving a Drishti from Budh, Shukra and Shani, the native will be rich
- 上升为火星星座有火星 水金土同宫或相照 富有

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava

### 适用边界路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

### 判断方法路

- Combinations for Wealth
- Should Budh’s Rashibe Lagn with Budh therein and should Budh be yuti with, or receiving a Drishti from Shani and Guru

## 上游问题

- 无

## 停止条件

- 上升所落星座未取到时停止。
- 火星是否落上升宫的事实缺失时停止。
- 同宫与相照两类关系事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
