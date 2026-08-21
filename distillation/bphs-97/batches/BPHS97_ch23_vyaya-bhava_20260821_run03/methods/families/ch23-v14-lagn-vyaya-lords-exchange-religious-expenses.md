---
method: ch23-v14-lagn-vyaya-lords-exchange-religious-expenses
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 开支花在宗教上：上升主落十二宫、十二宫主落上升宫并与金星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的钱会不会花在宗教上
- 我是不是会为信仰花钱

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否落十二宫（Vyaya）
- 十二宫主（Vyaya's Lord）是否落上升宫（Lagna）
- 十二宫主（Vyaya's Lord）是否与金星（Shukra）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch23-v14-lagn-vyaya-lords-exchange-religious-expenses.step-001

- 动作：核对上升主（Lagn's Lord）是否落十二宫（Vyaya），并核对十二宫主（Vyaya's Lord）是否落上升宫且与金星（Shukra）同宫。
- 适用范围：仅限本命盘十二宫（Vyaya Bhava）的开支用途主题；原文三项条件同时成立才下断语；原文未给时间限定，也未给开支金额。
- 原文最小意思：上升主（Lagn's Lord）落十二宫（Vyaya），同时十二宫主（Vyaya's Lord）落上升宫（Lagn）并与金星（Shukr）同宫时，开支会花在宗教方面。
- 本步骤产出事实：["上升主与十二宫主互换加金星的宗教开支判定"]
- 所需事实：["上升主（Lagn's Lord）是否落十二宫（Vyaya）", "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）", "十二宫主（Vyaya's Lord）是否与金星（Shukra）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落十二宫（Vyaya）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否与金星（Shukra）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得缺少金星（Shukra）同宫这一条就下断语。", "不得把「宗教方面的开支」读成必定虔诚、出家或破财。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否落十二宫（Vyaya）、十二宫主（Vyaya's Lord）是否落上升宫（Lagna）、十二宫主（Vyaya's Lord）是否与金星（Shukra）同宫。
- 缺失即停字段：["上升主（Lagn's Lord）是否落十二宫（Vyaya）", "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）", "十二宫主（Vyaya's Lord）是否与金星（Shukra）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch23:v14`｜PDF [40]｜“If Lagn’s Lord is in Vyaya, while Vyaya’s Lord is in Lagn with Shukr, expenses will be on religious grounds.”


## 四路查书计划

### 支持路

- If Lagn’s Lord is in Vyaya, while Vyaya’s Lord is in Lagn with Shukr, expenses will be on religious grounds.
- 上升主落十二宫 十二宫主落上升 金星同宫 宗教开支

### 反例或取消路

- If Lagn’s Lord is in Vyaya Bhava and is devoid of benefic Drishti and/or Yuti, the native will be bereft of physical happiness, will spend unfruitfully and be given to much anger.
- If Vyaya’s Lord is in Tanu Bhava, the native will be a spendthrift, be weak in constitution, will suffer from phlegmatic disorders and be devoid of wealth and learning.

### 适用边界路

- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Tanu Bhava

### 判断方法路

- Effects of Vyaya’s Lord in Various Bhavas
- 上升主与十二宫主互换宫位怎么判断

## 上游问题

- 无

## 停止条件

- 三项落宫与同宫事实缺任意一条即停止。
- 缺少本盘上升主与十二宫主身份时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
