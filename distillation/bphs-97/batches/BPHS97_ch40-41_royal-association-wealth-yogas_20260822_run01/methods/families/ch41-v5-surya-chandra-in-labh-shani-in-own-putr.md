---
method: ch41-v5-surya-chandra-in-labh-shani-in-own-putr
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 极富：日月落十一宫，土星落自己主管的五宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的钱景怎么样
- 我能不能积起大财

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫（Putr Bhava）落在哪个星座
- 太阳（Surya）是否落十一宫（Labh）
- 月亮（Chandra）是否落十一宫（Labh）
- 五宫（Putr Bhava）是否被土星（Shani）占据
- 五宫（Putr Bhava）是否同时是土星（Shani）自己主管的宫（own Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch41-v5-surya-chandra-in-labh-shani-in-own-putr.step-001

- 动作：核对太阳（Surya）与月亮（Chandra）是否都落十一宫（Labh Bhava），再看土星（Shani）是否落在五宫，而该五宫正是土星自己主管的宫。
- 适用范围：仅限本命盘五宫与十一宫的这一组配置；原文此处写的是 his own Bhava（自己主管的宫），本方法照原文用词，不改成别的口径；本条属本章「Yogas for Great Affluence (up to Sloka 8)」一组；原文未给时间限定。
- 原文最小意思：太阳（Surya）与月亮（Chandra）落十一宫（Labh Bhava），同时土星（Shani）落五宫（Putr Bhava），而该宫即是土星自己主管的宫（own Bhava）时，命主将极为富足。
- 本步骤产出事实：["日月十一宫土星本宫五宫的极富判定"]
- 所需事实：["本盘五宫（Putr Bhava）落在哪个星座", "太阳（Surya）是否落十一宫（Labh）", "月亮（Chandra）是否落十一宫（Labh）", "五宫（Putr Bhava）是否被土星（Shani）占据", "五宫（Putr Bhava）是否同时是土星（Shani）自己主管的宫（own Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫（Putr Bhava）落在哪个星座"}, {"fact_key": "太阳（Surya）是否落十一宫（Labh）"}, {"fact_key": "月亮（Chandra）是否落十一宫（Labh）"}, {"fact_key": "五宫（Putr Bhava）是否被土星（Shani）占据"}, {"fact_key": "五宫（Putr Bhava）是否同时是土星（Shani）自己主管的宫（own Bhava）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文要求土星所落的五宫同时是它自己主管的宫，不得只凭土星落五宫就下断。", "不得据此推断财富数额、来源或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫（Putr Bhava）落在哪个星座、太阳（Surya）是否落十一宫（Labh）、月亮（Chandra）是否落十一宫（Labh）、五宫（Putr Bhava）是否被土星（Shani）占据、五宫（Putr Bhava）是否同时是土星（Shani）自己主管的宫（own Bhava）。
- 缺失即停字段：["本盘五宫（Putr Bhava）落在哪个星座", "太阳（Surya）是否落十一宫（Labh）", "月亮（Chandra）是否落十一宫（Labh）", "五宫（Putr Bhava）是否被土星（Shani）占据", "五宫（Putr Bhava）是否同时是土星（Shani）自己主管的宫（own Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch41:v5`｜PDF [86]｜“Should Surya and Chandra be in Labh Bhava, as Shani is in Putr Bhava identical with his own Bhava, the native will be very affluent.”


## 四路查书计划

### 支持路

- Should Surya and Chandra be in Labh Bhava, as Shani is in Putr Bhava identical with his own Bhava
- 日月十一宫 土星落自己主管的五宫 极富

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava

### 适用边界路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

### 判断方法路

- Combinations for Wealth
- Should Guru be in Putr Bhava identical with his own Rāśi, as Budh is in Labh Bhava

## 上游问题

- 无

## 停止条件

- 五宫所落星座未取到时停止。
- 日月是否落十一宫、土星是否落五宫的事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
