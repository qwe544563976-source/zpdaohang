---
method: ch41-v4-simh-as-putr-with-surya-and-three-in-labh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 极富：五宫为狮子座并被太阳占据，土月木三星落十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子财上到什么份儿
- 我能不能挣下大家业

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫（Putr Bhava）落在哪个星座
- 五宫（Putr Bhava）是否落在狮子座（Simh）
- 五宫（Putr Bhava）是否被太阳（Surya）占据
- 土星（Shani）是否落十一宫（Labh）
- 月亮（Chandra）是否落十一宫（Labh）
- 木星（Guru）是否落十一宫（Labh）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch41-v4-simh-as-putr-with-surya-and-three-in-labh.step-001

- 动作：先取五宫所落星座，核对它是否为狮子座（Simh）、是否被太阳（Surya）本人占据，再看十一宫（Labh Bhava）是否同时有土星、月亮与木星。
- 适用范围：仅限本命盘五宫与十一宫的这一组配置；本条属本章「Yogas for Great Affluence (up to Sloka 8)」一组；原文未给时间限定，也未给上升限定。
- 原文最小意思：五宫（Putr Bhava）即狮子座（Simh）并被太阳（Surya）本人占据，同时土星（Shani）、月亮（Chandra）与木星（Guru）落十一宫（Labh Bhava）时，命主将极为富足。
- 本步骤产出事实：["狮子座五宫太阳与三星十一宫的极富判定"]
- 所需事实：["本盘五宫（Putr Bhava）落在哪个星座", "五宫（Putr Bhava）是否落在狮子座（Simh）", "五宫（Putr Bhava）是否被太阳（Surya）占据", "土星（Shani）是否落十一宫（Labh）", "月亮（Chandra）是否落十一宫（Labh）", "木星（Guru）是否落十一宫（Labh）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫（Putr Bhava）落在哪个星座"}, {"fact_key": "五宫（Putr Bhava）是否落在狮子座（Simh）"}, {"fact_key": "五宫（Putr Bhava）是否被太阳（Surya）占据"}, {"fact_key": "土星（Shani）是否落十一宫（Labh）"}, {"fact_key": "月亮（Chandra）是否落十一宫（Labh）"}, {"fact_key": "木星（Guru）是否落十一宫（Labh）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文点名狮子座（Simh），不得换成太阳主管的别的位置。", "不得据此推断财富数额、来源或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫（Putr Bhava）落在哪个星座、五宫（Putr Bhava）是否落在狮子座（Simh）、五宫（Putr Bhava）是否被太阳（Surya）占据、土星（Shani）是否落十一宫（Labh）、月亮（Chandra）是否落十一宫（Labh）、木星（Guru）是否落十一宫（Labh）。
- 缺失即停字段：["本盘五宫（Putr Bhava）落在哪个星座", "五宫（Putr Bhava）是否落在狮子座（Simh）", "五宫（Putr Bhava）是否被太阳（Surya）占据", "土星（Shani）是否落十一宫（Labh）", "月亮（Chandra）是否落十一宫（Labh）", "木星（Guru）是否落十一宫（Labh）"]
- 原文证据：
  - `bphs-97:santhanam:ch41:v4`｜PDF [86]｜“Should Simh be Putr Bhava and be occupied by Surya himself, as Shani, Chandra and Guru are in Labh Bhava, the native will be very affluent.”


## 四路查书计划

### 支持路

- Should Simh be Putr Bhava and be occupied by Surya himself, as Shani, Chandra and Guru are in Labh Bhava
- 五宫狮子座被太阳占据 土月木在十一宫 极富

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava

### 适用边界路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

### 判断方法路

- Combinations for Wealth
- Should Surya and Chandra be in Labh Bhava, as Shani is in Putr Bhava identical with his own Bhava

## 上游问题

- 无

## 停止条件

- 五宫所落星座未取到时停止。
- 十一宫三颗行星的落宫事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
