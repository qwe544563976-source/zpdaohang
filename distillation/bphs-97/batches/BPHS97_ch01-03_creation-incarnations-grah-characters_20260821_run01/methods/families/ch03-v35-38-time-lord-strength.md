---
method: ch03-v35-38-time-lord-strength
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 年主、月主、日主、时主的强弱升序

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 年主 月主 日主 时主 哪个更有力
- 我盘里的时主是不是比日主更强

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的年主（year Lord）是哪颗行星
- 本盘的月主（month Lord）是哪颗行星
- 本盘的日主（day Lord）是哪颗行星
- 本盘的时主（Hora Lord）是哪颗行星

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v35-38-time-lord-strength.step-001

- 动作：取本盘的年主、月主、日主与时主，按原文给的升序比较四者强弱。
- 适用范围：第3章诸曜强弱条；原文只给四者的相对次序，未给分值，也未说这四主怎么定。
- 原文最小意思：年（year）、月（month）、日（day）与时（Hora）之主，按此升序一个比一个更强。
- 本步骤产出事实：["年月日时四主强弱次序判定"]
- 所需事实：["本盘的年主（year Lord）是哪颗行星", "本盘的月主（month Lord）是哪颗行星", "本盘的日主（day Lord）是哪颗行星", "本盘的时主（Hora Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘的年主（year Lord）是哪颗行星"}, {"fact_key": "本盘的月主（month Lord）是哪颗行星"}, {"fact_key": "本盘的日主（day Lord）是哪颗行星"}, {"fact_key": "本盘的时主（Hora Lord）是哪颗行星"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出四主之外其他时段之主的强弱次序。", "不得据本条推出四主强弱的具体分值。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的年主（year Lord）是哪颗行星、本盘的月主（month Lord）是哪颗行星、本盘的日主（day Lord）是哪颗行星、本盘的时主（Hora Lord）是哪颗行星。
- 缺失即停字段：["本盘的年主（year Lord）是哪颗行星", "本盘的月主（month Lord）是哪颗行星", "本盘的日主（day Lord）是哪颗行星", "本盘的时主（Hora Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v35-38`｜PDF [11]｜“The Lords of the year, month, day and Hora (hour of Grah) are stronger than the other in ascending order.”


## 四路查书计划

### 支持路

- The Lords of the year, month, day and Hora (hour of Grah) are stronger than the other in ascending order
- 年主 月主 日主 时主 强弱升序

### 反例或取消路

- 无

### 适用边界路

- The Varsh Lord is the Lord of the day, on which the astrological year of birth starts
- 年主怎么定

### 判断方法路

- Varsh-Maas-Dina-Hora Bal. 15, 30, 45 and 60 Virupas are in order given to Varsh Lord, Maas Lord, Dina Lord and Hora Lord
- 四时之主强弱的具体分值怎么算

## 上游问题

- 无

## 停止条件

- 缺少本盘年主、月主、日主或时主中任何一个的事实时停止。
- 原文没有说这四主如何确定，四主无法确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
