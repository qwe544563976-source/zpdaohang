---
method: ch41-v20-22-putr-lord-iravatamsa
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 五宫主（Putr's Lord）落 Iravatāńś 的效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的学业与见识怎么样
- 五宫主的分盘等级说明我什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫主（Putr's Lord）是哪颗行星
- 五宫主（Putr's Lord）的分盘尊贵是否为 Iravatāńś

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch41-v20-22-putr-lord-iravatamsa.step-001

- 动作：核对五宫主（Putr's Lord）的分盘尊贵是否为 Iravatāńś，据以取本偈对应的一句效果。
- 适用范围：仅限本命盘五宫主的分盘尊贵这一支；原文本偈以「Effects of the Divisional Dignities of Putr’s Lord」立题，八种分盘尊贵共用同一主语、各自结果不同且互斥，本方法只取其中一种；Paravatāńś 一档原文印作「if in also Paravatāńś」，此处照录；分盘尊贵的名目见本书第 6 章 Dasha Varg 的等级表；原文未给时间限定。
- 原文最小意思：本偈判的是五宫主（Putr's Lord）的分盘尊贵：五宫主落 Iravatāńś 时，命主将虔敬。
- 本步骤产出事实：["五宫主（Putr's Lord）落 Iravatāńś 的判定"]
- 所需事实：["本盘五宫主（Putr's Lord）是哪颗行星", "五宫主（Putr's Lord）的分盘尊贵是否为 Iravatāńś"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "五宫主（Putr's Lord）的分盘尊贵是否为 Iravatāńś"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把本条效果与本偈其他分盘尊贵档的效果合并或互换。", "不得据此推断发生时间、程度或具体事件。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫主（Putr's Lord）是哪颗行星、五宫主（Putr's Lord）的分盘尊贵是否为 Iravatāńś。
- 缺失即停字段：["本盘五宫主（Putr's Lord）是哪颗行星", "五宫主（Putr's Lord）的分盘尊贵是否为 Iravatāńś"]
- 原文证据：
  - `bphs-97:santhanam:ch41:v20-22`｜PDF [87]｜“Effects of the Divisional Dignities of Putr’s Lord”
  - `bphs-97:santhanam:ch41:v20-22`｜PDF [87]｜“if in Iravatāńś”
  - `bphs-97:santhanam:ch41:v20-22`｜PDF [87]｜“will be pious”


## 四路查书计划

### 支持路

- Effects of the Divisional Dignities of Putr’s Lord. If Putr’s Lord is in Parijatāńś, the native will take to the branch of learning
- 五宫主 分盘尊贵 Iravatāńś 效果

### 反例或取消路

- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- In the Dasha Varg scheme the designations commence from Parijata etc., such as 2 good Vargas - Parijatha, 3 Uttama, 4 Gopur, 5 Simhasan, 6 Paravata, 7 Devaloka, 8 Brahmaloka, 9 Sakravahana and 10 Vargas - Shridham
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

### 判断方法路

- Combinations for Wealth
- Other Qualified Grahas. Dharm’s Lord and Putr’s Lord are capable of bestowing wealth

## 上游问题

- 无

## 停止条件

- 五宫主（Putr's Lord）的身份事实缺失时停止。
- 分盘尊贵是否为 Iravatāńś 的事实缺失时停止。
- 分盘尊贵的判定口径未按本书第 6 章 Dasha Varg 的等级表取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
