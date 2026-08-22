---
method: ch29-v13-15-drishti-from-ninth-much-more-gains
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 相照来自上升起第 9 宫：得益远为丰厚

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 九宫的吉星照财位有多好
- 什么位置照过来最旺财

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联
- 上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）起第 9 宫的吉星相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch29-v13-15-drishti-from-ninth-much-more-gains.step-001

- 动作：先确认上升 Pad（Lagn Pad）起第 12 宫不与凶星关联，再看相照上升 Pad 起第 11 宫的吉星是否来自上升起第 9 宫。
- 适用范围：原文的「the Drishti」承同偈前句落在上升（Lagna）的吉星对上升 Pad 起第 11 宫的相照；原文的「In all these cases」一句出现在本句之前，本条按同段各得益条共有的前提处理，原文没有再逐句重申。
- 原文最小意思：上升 Pad（Lagn Pad）起第 12 宫同时不与凶星关联的前提下，相照上升 Pad（Arudh Lagn）起第 11 宫的吉星来自上升（Lagna）起第 9 宫时，得益远为丰厚。
- 本步骤产出事实：["上升起第 9 宫吉星相照上升 Pad 起第 11 宫的判定"]
- 所需事实：["上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联", "上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）起第 9 宫的吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联"}]}, {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）起第 9 宫的吉星相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断得益数额或时间。", "不得把上升起第 9 宫改读成上升 Pad 起第 9 宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联、上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）起第 9 宫的吉星相照。
- 缺失即停字段：["上升 Pad（Lagn Pad）起第 12 宫是否与凶星发生关联", "上升 Pad（Lagn Pad）起第 11 宫是否被落在上升（Lagna）起第 9 宫的吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v13-15`｜PDF [62]｜“A benefic, placed in Lagna, giving a Drishti to the 11<sup>th</sup> from Arudh Lagn will be still beneficial.”
  - `bphs-97:santhanam:ch29:v13-15`｜PDF [62]｜“If the Drishti is from the 9<sup>th</sup> from Lagna, it will confer much more gains.”
  - `bphs-97:santhanam:ch29:v13-15`｜PDF [62]｜“In all these cases, the 12<sup>th</sup> from Pad should simultaneously be free from malefic association.”


## 四路查书计划

### 支持路

- If the Drishti is from the 9<sup>th</sup> from Lagna, it will confer much more gains
- 第 9 宫吉星相照 得益远为丰厚

### 反例或取消路

- If the 12<sup>th</sup> from Lagn Pad receives a Drishti from, or is yuti with both benefics and malefics, there will be abundant earnings, but plenty of expenses.
- 第 12 宫方向的开销条

### 适用边界路

- In all these cases, the 12<sup>th</sup> from Pad should simultaneously be free from malefic association.
- 本段各条共有的第 12 宫前提

### 判断方法路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics.
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 吉星相照怎么判

## 上游问题

- 无

## 停止条件

- 缺少相照来源宫位的事实时停止。
- 缺少上升 Pad 起第 12 宫与凶星关联与否的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
