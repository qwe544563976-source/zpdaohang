---
method: ch41-v8-kark-as-putr-with-chandra-and-shani-in-labh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 极富：五宫为巨蟹座并有月亮在内，土星落十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的财路顺不顺
- 我能不能积下大财

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫（Putr Bhava）落在哪个星座
- 五宫（Putr Bhava）是否落在巨蟹座（Kark）
- 五宫（Putr Bhava）是否被月亮（Chandra）占据
- 土星（Shani）是否落十一宫（Labh）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch41-v8-kark-as-putr-with-chandra-and-shani-in-labh.step-001

- 动作：先取五宫所落星座，核对它是否为巨蟹座（Kark）、其中是否有月亮（Chandra），再看土星（Shani）是否落十一宫（Labh Bhava）。
- 适用范围：仅限本命盘五宫与十一宫的这一组配置；本条属本章「Yogas for Great Affluence (up to Sloka 8)」一组；原文未给时间限定，也未给上升限定。
- 原文最小意思：五宫（Putr Bhava）即巨蟹座（Kark）并有月亮（Chandra）在其中，同时土星（Shani）落十一宫（Labh Bhava）时，命主将变得极为富足。
- 本步骤产出事实：["巨蟹座五宫月亮土星十一宫的极富判定"]
- 所需事实：["本盘五宫（Putr Bhava）落在哪个星座", "五宫（Putr Bhava）是否落在巨蟹座（Kark）", "五宫（Putr Bhava）是否被月亮（Chandra）占据", "土星（Shani）是否落十一宫（Labh）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫（Putr Bhava）落在哪个星座"}, {"fact_key": "五宫（Putr Bhava）是否落在巨蟹座（Kark）"}, {"fact_key": "五宫（Putr Bhava）是否被月亮（Chandra）占据"}, {"fact_key": "土星（Shani）是否落十一宫（Labh）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文点名巨蟹座（Kark），不得换成月亮主管的别的位置。", "不得据此推断财富数额、来源或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫（Putr Bhava）落在哪个星座、五宫（Putr Bhava）是否落在巨蟹座（Kark）、五宫（Putr Bhava）是否被月亮（Chandra）占据、土星（Shani）是否落十一宫（Labh）。
- 缺失即停字段：["本盘五宫（Putr Bhava）落在哪个星座", "五宫（Putr Bhava）是否落在巨蟹座（Kark）", "五宫（Putr Bhava）是否被月亮（Chandra）占据", "土星（Shani）是否落十一宫（Labh）"]
- 原文证据：
  - `bphs-97:santhanam:ch41:v8`｜PDF [86]｜“If Kark happens to be Putr Bhava, containing Chandra therein, while Shani is in Labh Bhava, the native will become very affluent.”


## 四路查书计划

### 支持路

- If Kark happens to be Putr Bhava, containing Chandra therein, while Shani is in Labh Bhava
- 五宫巨蟹座有月亮 土星十一宫 极富

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava

### 适用边界路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

### 判断方法路

- Combinations for Wealth
- Should Surya be in Simh identical with Lagn and be yuti with, or receiving a Drishti from Mangal and Guru

## 上游问题

- 无

## 停止条件

- 五宫所落星座未取到时停止。
- 五宫是否有月亮、土星是否落十一宫的事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
