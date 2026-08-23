---
method: ch37-v2-4-day-birth-chandra-navamsa
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 白天生：月亮居本九分盘或友星九分盘并受木星相照，得财富与快乐

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我白天出生 命里财运和心情怎么样
- 月亮的九分盘位置对我的财富有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘是否为白天出生
- 月亮（Chandra）是否被木星（Guru）相照

## 按情况检查的事实

- 月亮（Chandra）在九分盘（Navāńś D9）中是否落自己主管的星座
- 月亮（Chandra）在九分盘（Navāńś D9）中是否落友星主管的星座

## 依赖方法

- 无

## 执行步骤

### ch37-v2-4-day-birth-chandra-navamsa.step-001

- 动作：先确认是否白天出生，再核对月亮（Chandra）的九分盘星座归属与木星（Guru）的相照，判定财富与快乐的断语。
- 适用范围：仅限白天出生的本命盘；原文没有时间限定。
- 原文最小意思：白天出生者，若月亮（Chandra）落在自己主管的九分盘（Navāńś）星座，或落在友星的九分盘（Navāńś）星座，并受木星（Guru）相照，则会有财富与快乐。
- 本步骤产出事实：["白天生的月亮九分盘财富快乐判定"]
- 所需事实：["本盘是否为白天出生", "月亮（Chandra）是否被木星（Guru）相照"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘是否为白天出生"}, {"fact_key": "月亮（Chandra）是否被木星（Guru）相照"}]}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）在九分盘（Navāńś D9）中是否落自己主管的星座"}, {"fact_key": "月亮（Chandra）在九分盘（Navāńś D9）中是否落友星主管的星座"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘是否为白天出生"}, {"fact_key": "月亮（Chandra）是否被木星（Guru）相照"}]}, "required_fact_keys": ["月亮（Chandra）在九分盘（Navāńś D9）中是否落自己主管的星座"], "branch_condition_logic": {"fact_key": "月亮（Chandra）在九分盘（Navāńś D9）中是否落自己主管的星座"}, "selection_group": "ch37-v2-4-day-birth-chandra-navamsa.step-001:chandra-navamsa", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）在九分盘（Navāńś D9）中是否落自己主管的星座。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘是否为白天出生"}, {"fact_key": "月亮（Chandra）是否被木星（Guru）相照"}]}, "required_fact_keys": ["月亮（Chandra）在九分盘（Navāńś D9）中是否落友星主管的星座"], "branch_condition_logic": {"fact_key": "月亮（Chandra）在九分盘（Navāńś D9）中是否落友星主管的星座"}, "selection_group": "ch37-v2-4-day-birth-chandra-navamsa.step-001:chandra-navamsa", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）在九分盘（Navāńś D9）中是否落友星主管的星座。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、来源或得财时间。", "原文本句只对白天出生立说，不得把它直接用于夜间出生。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘是否为白天出生、月亮（Chandra）是否被木星（Guru）相照。
- 缺失即停字段：["本盘是否为白天出生", "月亮（Chandra）是否被木星（Guru）相照"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v2-4`｜PDF [81]｜“In the case of a day birth, if Chandra, placed in its own Navāńś, or in a friendly Navāńś, receives a Drishti from Guru, one will be endowed with wealth and happiness.”


## 四路查书计划

### 支持路

- In the case of a day birth, if Chandra, placed in its own Navāńś, or in a friendly Navāńś, receives a Drishti from Guru, one will be endowed with wealth and happiness
- 白天出生 月亮本九分盘 木星相照 财富快乐

### 反例或取消路

- In a contrary situation, the Drishti from Guru, or from Shukra on Chandra will make one go with little wealth, or even without that
- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- This happens, when Lagn in the RashiKundali and the Navāńś Lagn are in the same Rāśi
- 九分盘（Navāńś D9）的主管与友星判定

### 判断方法路

- Should Guru be in a Kendr from Lagna, or from Chandra and be yuti with, or receiving a Drishti from benefic, avoiding at the same time debilitation, combustion and inimical Rāśi, Gaj Kesari Yog is caused
- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn

## 上游问题

- 无

## 停止条件

- 缺少昼夜出生事实时停止。
- 缺少月亮受木星相照的事实时停止。
- 月亮的九分盘星座归属两项事实全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
