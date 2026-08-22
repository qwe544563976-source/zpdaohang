---
method: ch29-v13-15-quantum-of-gains-by-count
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 得益多寡与上升 Pad 起第 11 宫的行星数目相应

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能赚多少
- 进项的大小怎么估

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联

## 按情况检查的事实

- 上升 Pad（Lagn Pad）起第 11 宫内有几颗行星（Grah）
- 有几颗行星（Grah）相照上升 Pad（Lagn Pad）起第 11 宫

## 依赖方法

- 无

## 执行步骤

### ch29-v13-15-quantum-of-gains-by-count.step-001

- 动作：先确认上升 Pad（Lagn Pad）起第 12 宫不与凶星关联，再数落在其起第 11 宫内以及相照该宫的行星数目。
- 适用范围：原文本段以「In all these cases」统摄本段各得益条，故第 12 宫不与凶星关联是本条的同时前提；原文只给数目与得益多寡相应，没有给换算比例。
- 原文最小意思：上升 Pad（Lagn Pad）起第 12 宫同时不与凶星关联的前提下，得益的多寡与落在上升 Pad（Lagn Pad）起第 11 宫内、或相照该宫的行星数目相应。
- 本步骤产出事实：["上升 Pad 起第 11 宫的得益多寡判定"]
- 所需事实：["上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"}]}, {"operator": "OR", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 11 宫内有几颗行星（Grah）"}, {"fact_key": "有几颗行星（Grah）相照上升 Pad（Lagn Pad）起第 11 宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "NOT", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"}]}, "required_fact_keys": ["上升 Pad（Lagn Pad）起第 11 宫内有几颗行星（Grah）"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫内有几颗行星（Grah）"}, "selection_group": "ch29-v13-15-quantum-of-gains-by-count.step-001:count-source", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）起第 11 宫内有几颗行星（Grah）。"}, {"when": {"operator": "NOT", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"}]}, "required_fact_keys": ["有几颗行星（Grah）相照上升 Pad（Lagn Pad）起第 11 宫"], "branch_condition_logic": {"fact_key": "有几颗行星（Grah）相照上升 Pad（Lagn Pad）起第 11 宫"}, "selection_group": "ch29-v13-15-quantum-of-gains-by-count.step-001:count-source", "stop_condition": "选中该分支后，缺少以下事实即停止：有几颗行星（Grah）相照上升 Pad（Lagn Pad）起第 11 宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把行星数目换算成具体金额或倍数。", "不得据此推断得益的时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联。
- 缺失即停字段：["上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v13-15`｜PDF [62]｜“O Brahmin, the quantum of gains will correspond to the number of Grahas in, or giving a Drishti to the 11<sup>th</sup> from Lagn Pad.”
  - `bphs-97:santhanam:ch29:v13-15`｜PDF [62]｜“In all these cases, the 12<sup>th</sup> from Pad should simultaneously be free from malefic association.”


## 四路查书计划

### 支持路

- the quantum of gains will correspond to the number of Grahas in, or giving a Drishti to the 11<sup>th</sup> from Lagn Pad
- 上升 Pad 起第 11 宫行星数目 得益多寡

### 反例或取消路

- If the 12<sup>th</sup> from Lagn Pad receives a Drishti from, or is yuti with both benefics and malefics, there will be abundant earnings, but plenty of expenses.
- 上升 Pad 起第 12 宫带来的开销

### 适用边界路

- In all these cases, the 12<sup>th</sup> from Pad should simultaneously be free from malefic association.
- 本段各条共有的第 12 宫前提

### 判断方法路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics.
- 上升 Pad 怎么求

## 上游问题

- 无

## 停止条件

- 缺少上升 Pad 起第 12 宫与凶星关联与否的事实时停止。
- 缺少上升 Pad 起第 11 宫内行星数目或相照行星数目时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
