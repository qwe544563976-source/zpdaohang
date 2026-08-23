---
method: ch41-v6-guru-in-own-putr-with-budh-in-labh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 极富：木星落自己主管的五宫，水星落十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的家业能做多大
- 我这辈子财上顺不顺

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫（Putr Bhava）落在哪个星座
- 五宫（Putr Bhava）是否为木星（Guru）主管的星座（Rāśi）
- 五宫（Putr Bhava）是否被木星（Guru）占据
- 水星（Budh）是否落十一宫（Labh）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch41-v6-guru-in-own-putr-with-budh-in-labh.step-001

- 动作：核对木星（Guru）是否落五宫，而该五宫所在星座正是木星自己主管的星座，再看水星（Budh）是否落十一宫（Labh Bhava）。
- 适用范围：仅限本命盘五宫与十一宫的这一组配置；原文此处写的是 his own Rāśi（自己主管的星座），不是本宫；本条属本章「Yogas for Great Affluence (up to Sloka 8)」一组；原文未给时间限定。
- 原文最小意思：木星（Guru）落五宫（Putr Bhava），而该宫所在星座即是木星自己主管的星座（own Rāśi），同时水星（Budh）落十一宫（Labh Bhava）时，命主将极为富足。
- 本步骤产出事实：["木星本星座五宫水星十一宫的极富判定"]
- 所需事实：["本盘五宫（Putr Bhava）落在哪个星座", "五宫（Putr Bhava）是否为木星（Guru）主管的星座（Rāśi）", "五宫（Putr Bhava）是否被木星（Guru）占据", "水星（Budh）是否落十一宫（Labh）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫（Putr Bhava）落在哪个星座"}, {"fact_key": "五宫（Putr Bhava）是否为木星（Guru）主管的星座（Rāśi）"}, {"fact_key": "五宫（Putr Bhava）是否被木星（Guru）占据"}, {"fact_key": "水星（Budh）是否落十一宫（Labh）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文说的是木星自己主管的星座（own Rāśi），不得换成入旺或别的尊贵状态。", "不得据此推断财富数额、来源或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫（Putr Bhava）落在哪个星座、五宫（Putr Bhava）是否为木星（Guru）主管的星座（Rāśi）、五宫（Putr Bhava）是否被木星（Guru）占据、水星（Budh）是否落十一宫（Labh）。
- 缺失即停字段：["本盘五宫（Putr Bhava）落在哪个星座", "五宫（Putr Bhava）是否为木星（Guru）主管的星座（Rāśi）", "五宫（Putr Bhava）是否被木星（Guru）占据", "水星（Budh）是否落十一宫（Labh）"]
- 原文证据：
  - `bphs-97:santhanam:ch41:v6`｜PDF [86]｜“Should Guru be in Putr Bhava identical with his own Rāśi, as Budh is in Labh Bhava, the native will be very affluent.”


## 四路查书计划

### 支持路

- Should Guru be in Putr Bhava identical with his own Rāśi, as Budh is in Labh Bhava
- 木星落自己星座的五宫 水星十一宫 极富

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava

### 适用边界路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

### 判断方法路

- Combinations for Wealth
- If a Rashiof Mangal happens to be Putr Bhava with Mangal therein, while Shukra is in Labh Bhava

## 上游问题

- 无

## 停止条件

- 五宫所落星座未取到时停止。
- 木星是否落五宫、水星是否落十一宫的事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
