---
method: ch22-v8-labh-lagn-lords-interchange-1000-nishkas
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第33年得1000 Nishkas：十一宫主落上升宫、上升主落十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我三十出头能不能进一笔钱
- 上升主与十一宫主互换有什么效果

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十一宫主（Labh's Lord）是否落上升宫（Lagna）
- 上升主（Lagn's Lord）是否落十一宫（Labh）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch22-v8-labh-lagn-lords-interchange-1000-nishkas.step-001

- 动作：核对十一宫主（Labh's Lord）是否落上升宫（Lagna），同时核对上升主（Lagn's Lord）是否落十一宫（Labh）。
- 适用范围：仅限本命盘十一宫（Labh）收获主题；两宫主须互换落宫，缺一不成立；原文以 his 指称本人；正式原文在 Lagn’s Lord 之后印有分页标记 ####，不影响句意。
- 原文最小意思：十一宫主落上升宫、上升主落十一宫时，本人在第33年获得1000 Nishkas。
- 本步骤产出事实：["十一宫主上升主互换第33年收获判定"]
- 所需事实：["十一宫主（Labh's Lord）是否落上升宫（Lagna）", "上升主（Lagn's Lord）是否落十一宫（Labh）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落上升宫（Lagna）"}, {"fact_key": "上升主（Lagn's Lord）是否落十一宫（Labh）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得只凭单向落宫（只有一方换过去）就下断：原文要求两宫主互换。", "不得把 1000 Nishkas 换算成任何现代货币金额，也不得挪动第33年这一年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十一宫主（Labh's Lord）是否落上升宫（Lagna）、上升主（Lagn's Lord）是否落十一宫（Labh）。
- 缺失即停字段：["十一宫主（Labh's Lord）是否落上升宫（Lagna）", "上升主（Lagn's Lord）是否落十一宫（Labh）"]
- 原文证据：
  - `bphs-97:santhanam:ch22:v8`｜PDF [39, 40]｜“One will gain 1000 Nishkas in his 33<sup>rd</sup> year, if Labh’s Lord is in Lagn and Lagn’s Lord #### is in Labh Bhava.”


## 四路查书计划

### 支持路

- One will gain 1000 Nishkas in his 33rd year, if Labh’s Lord is in Lagn and Lagn’s Lord is in Labh Bhava
- 十一宫主落上升宫 上升主落十一宫（Labh） 第33年 1000 Nishkas

### 反例或取消路

- There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic
- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic

### 适用边界路

- Indications of Labh Bhava. All articles, son’s wife, income, prosperity, quadrupeds etc. are to be understood from Labh Bhava
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- If Lagn’s Lord is in Labh Bhava, the native will always be endowed with gains, good qualities, fame and many wives
- If Labh’s Lord is in Labh Bhava, the native will gain in all his undertakings, while his learning and happiness will be on the increase day by day

## 上游问题

- 无

## 停止条件

- 缺少十一宫主落上升宫事实时停止。
- 缺少上升主落十一宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
