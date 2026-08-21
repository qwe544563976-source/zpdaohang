---
method: ch17-v27-inimical-sons
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 亲生子成仇：五宫主落六宫、六宫主与木星同宫、十二宫主落上升宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我和儿子会不会反目
- 子女将来会不会成为我的对头

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫主（Putr's Lord）是否落六宫（Ari）
- 六宫主（Ari's Lord）是否与木星（Guru）同宫
- 十二宫主（Vyaya's Lord）是否落上升宫（Lagna）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v27-inimical-sons.step-001

- 动作：核对五宫主落宫、六宫主与木星的同宫、十二宫主落宫三项是否同时成立。
- 适用范围：原文以男命立说（his enemies），三项条件须同时成立；未给时间限定。
- 原文最小意思：五宫主落六宫、六宫主与木星同宫、同时十二宫主落上升宫时，自己的儿子会成为他的仇敌。
- 本步骤产出事实：["亲生子成仇判定"]
- 所需事实：["五宫主（Putr's Lord）是否落六宫（Ari）", "六宫主（Ari's Lord）是否与木星（Guru）同宫", "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫主（Putr's Lord）是否落六宫（Ari）"}, {"fact_key": "六宫主（Ari's Lord）是否与木星（Guru）同宫"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断子女数目、成仇的时间或后果。", "不得在三项条件不全时套用本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主（Putr's Lord）是否落六宫（Ari）、六宫主（Ari's Lord）是否与木星（Guru）同宫、十二宫主（Vyaya's Lord）是否落上升宫（Lagna）。
- 缺失即停字段：["五宫主（Putr's Lord）是否落六宫（Ari）", "六宫主（Ari's Lord）是否与木星（Guru）同宫", "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v27`｜PDF [33]｜“One’s own sons will be his enemies, if Putr Lord is in Ari, while Ari Lord is with Guru.”
  - `bphs-97:santhanam:ch17:v27`｜PDF [33]｜“Simultaneously Vyaya Lord should be in Lagn.”


## 四路查书计划

### 支持路

- One’s own sons will be his enemies, if Putr Lord is in Ari, while Ari Lord is with Guru
- 五宫主落六宫 六宫主木星同宫 十二宫主上升 子成仇

### 反例或取消路

- Effects of Putr Bhava 子女幸福 五宫主入旺
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Female Horoscopy 女命的判法差异
- Effects of Putr’s Lord in Various Bhavas 五宫主落各宫

### 判断方法路

- 判断亲子关系应检查五宫与六宫的哪些关系

## 上游问题

- 无

## 停止条件

- 缺少五宫主落六宫事实时停止。
- 缺少六宫主与木星同宫事实时停止。
- 缺少十二宫主落上升宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
