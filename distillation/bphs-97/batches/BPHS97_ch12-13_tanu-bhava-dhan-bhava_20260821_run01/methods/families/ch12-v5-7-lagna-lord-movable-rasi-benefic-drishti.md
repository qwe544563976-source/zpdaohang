---
method: ch12-v5-7-lagna-lord-movable-rasi-benefic-drishti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 名声财富享乐：上升主落动星座并被吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有名声和享受
- 上升主落动星座代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否落动星座（Movable Rāśi）
- 上升主（Lagn's Lord）是否被吉星相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch12-v5-7-lagna-lord-movable-rasi-benefic-drishti.step-001

- 动作：核对上升主是否落在动星座，并核对它是否被吉星相照。
- 适用范围：仅限本命盘一宫（Tanu Bhava）名声与享乐主题；原文两个条件并列，必须同时成立。
- 原文最小意思：上升主（Lagn Lord）落在动星座（Movable Rāśi）并被吉星相照时，会得到名声、财富、丰富的享乐和身体上的舒适。
- 本步骤产出事实：["上升主落动星座得吉照的名声享乐判定"]
- 所需事实：["上升主（Lagn's Lord）是否落动星座（Movable Rāśi）", "上升主（Lagn's Lord）是否被吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落动星座（Movable Rāśi）"}, {"fact_key": "上升主（Lagn's Lord）是否被吉星相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得只凭落动星座一条就下断，原文还要求被吉星相照。", "不得据此推断名声的领域或财富数额。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否落动星座（Movable Rāśi）、上升主（Lagn's Lord）是否被吉星相照。
- 缺失即停字段：["上升主（Lagn's Lord）是否落动星座（Movable Rāśi）", "上升主（Lagn's Lord）是否被吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v5-7`｜PDF [26, 27]｜“Fame, wealth, abundant pleasures and comforts of the body will be acquired, if Lagn Lord is in a Movable Rashiand be drishtied by a benefic Grah.”


## 四路查书计划

### 支持路

- Fame, wealth, abundant pleasures and comforts of the body will be acquired, if Lagn Lord is in a Movable Rashiand be drishtied by a benefic Grah
- 上升主落动星座 被吉星相照 名声财富享乐

### 反例或取消路

- Should Lagn Lord be yuti with a malefic, or be in Randhr, 6th, or 12th, physical felicity will diminish
- If Lagn Lord is in debilitation, combustion, or enemy’s Rāśi, there will be diseases

### 适用边界路

- The Navāńś calculation are for a Movable Rashifrom there itself, for a Fixed Rashifrom the 9th thereof and for a Dual Rashifrom the 5th thereof
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The Sixteen Divisions of a Rāśi

### 判断方法路

- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- Effects of Lagn’s Lord in Various Bhavas (up to Sloka 12). Should Lagn’s Lord be in Lagn itself, the native will be endowed with physical happiness and prowess
- 判断名声享乐要看上升主落哪一类星座并有没有吉星相照

## 上游问题

- 无

## 停止条件

- 缺少上升主落动星座的事实时停止。
- 缺少上升主被吉星相照的事实时停止。
- 吉星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
