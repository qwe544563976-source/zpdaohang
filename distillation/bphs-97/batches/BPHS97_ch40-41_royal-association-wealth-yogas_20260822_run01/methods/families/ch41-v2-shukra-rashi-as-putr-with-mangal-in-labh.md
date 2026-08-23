---
method: ch41-v2-shukra-rashi-as-putr-with-mangal-in-labh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 大富：五宫为金星星座并被金星占据，火星落十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子能不能大富
- 我的财力能到什么级别

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫（Putr Bhava）落在哪个星座
- 五宫（Putr Bhava）是否为金星（Shukra）主管的星座（Rāśi）
- 五宫（Putr Bhava）是否被金星（Shukra）占据
- 火星（Mangal）是否落十一宫（Labh）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch41-v2-shukra-rashi-as-putr-with-mangal-in-labh.step-001

- 动作：先取五宫所落星座，核对它是否为金星（Shukra）主管、是否被金星本人占据，再看火星（Mangal）是否落十一宫（Labh Bhava）。
- 适用范围：仅限本命盘五宫与十一宫的这一组配置；原文本偈自带小标题「Yogas for Great Affluence (up to Sloka 8)」，说明本条属该组大富格之一；原文未给时间限定，也未给上升限定。
- 原文最小意思：五宫（Putr Bhava）所在星座由金星（Shukra）主管、并被金星本人占据，同时火星（Mangal）落十一宫（Labh Bhava）时，命主将获大富。
- 本步骤产出事实：["金星五宫火星十一宫的大富判定"]
- 所需事实：["本盘五宫（Putr Bhava）落在哪个星座", "五宫（Putr Bhava）是否为金星（Shukra）主管的星座（Rāśi）", "五宫（Putr Bhava）是否被金星（Shukra）占据", "火星（Mangal）是否落十一宫（Labh）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫（Putr Bhava）落在哪个星座"}, {"fact_key": "五宫（Putr Bhava）是否为金星（Shukra）主管的星座（Rāśi）"}, {"fact_key": "五宫（Putr Bhava）是否被金星（Shukra）占据"}, {"fact_key": "火星（Mangal）是否落十一宫（Labh）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文要求五宫既是金星的星座又被金星本人占据，不得只满足其中一项。", "不得据此推断财富数额、来源或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫（Putr Bhava）落在哪个星座、五宫（Putr Bhava）是否为金星（Shukra）主管的星座（Rāśi）、五宫（Putr Bhava）是否被金星（Shukra）占据、火星（Mangal）是否落十一宫（Labh）。
- 缺失即停字段：["本盘五宫（Putr Bhava）落在哪个星座", "五宫（Putr Bhava）是否为金星（Shukra）主管的星座（Rāśi）", "五宫（Putr Bhava）是否被金星（Shukra）占据", "火星（Mangal）是否落十一宫（Labh）"]
- 原文证据：
  - `bphs-97:santhanam:ch41:v2`｜PDF [86]｜“Should a Rashiof Shukra be Putr Bhava and be occupied by Shukra himself, while Mangal is in Labh Bhava, the native will obtain great riches.”


## 四路查书计划

### 支持路

- Should a Rashiof Shukra be Putr Bhava and be occupied by Shukra himself, while Mangal is in Labh Bhava
- 五宫为金星星座并被金星占据 火星十一宫 大富

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava
- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava

### 适用边界路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

### 判断方法路

- Combinations for Wealth
- Should a Rashiof Budh be Putr Bhava and be occupied by Budh himself, as Labh Bhava is occupied by Chandra, Mangal and Guru

## 上游问题

- 无

## 停止条件

- 五宫所落星座未取到时停止。
- 五宫是否被金星占据、火星是否落十一宫的事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
