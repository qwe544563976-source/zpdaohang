---
method: ch29-v18-surya-shukra-rahu-loss-through-king
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 太阳、金星、罗睺同处上升 Pad 起第 12 宫：因国王而失去财富

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会因为官方而破财
- 什么组合会让我损财

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否落上升 Pad（Lagn Pad）起第 12 宫
- 金星（Shukra）是否落上升 Pad（Lagn Pad）起第 12 宫
- 罗睺（Rahu）是否落上升 Pad（Lagn Pad）起第 12 宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch29-v18-surya-shukra-rahu-loss-through-king.step-001

- 动作：核对太阳（Surya）、金星（Shukra）、罗睺（Rahu）是否同处上升 Pad（Lagn Pad）起第 12 宫。
- 适用范围：本条以上升 Pad（Lagn Pad）为起算点；原文以国王（the king）立说，没有给时间或适用人群限定。
- 原文最小意思：上升 Pad（Lagn Pad）起第 12 宫与太阳（Surya）、金星（Shukra）、罗睺（Rahu）同处时，因国王而失去财富。
- 本步骤产出事实：["上升 Pad 起第 12 宫三星同处的失财判定"]
- 所需事实：["太阳（Surya）是否落上升 Pad（Lagn Pad）起第 12 宫", "金星（Shukra）是否落上升 Pad（Lagn Pad）起第 12 宫", "罗睺（Rahu）是否落上升 Pad（Lagn Pad）起第 12 宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落上升 Pad（Lagn Pad）起第 12 宫"}, {"fact_key": "金星（Shukra）是否落上升 Pad（Lagn Pad）起第 12 宫"}, {"fact_key": "罗睺（Rahu）是否落上升 Pad（Lagn Pad）起第 12 宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断损失金额或年份。", "原文要求三颗行星同处，不得只凭其中一颗成立本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落上升 Pad（Lagn Pad）起第 12 宫、金星（Shukra）是否落上升 Pad（Lagn Pad）起第 12 宫、罗睺（Rahu）是否落上升 Pad（Lagn Pad）起第 12 宫。
- 缺失即停字段：["太阳（Surya）是否落上升 Pad（Lagn Pad）起第 12 宫", "金星（Shukra）是否落上升 Pad（Lagn Pad）起第 12 宫", "罗睺（Rahu）是否落上升 Pad（Lagn Pad）起第 12 宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v18`｜PDF [62]｜“If the 12<sup>th</sup> from Lagn Pad is conjunct Surya, Shukra and Rahu, there will be loss of wealth through the king.”


## 四路查书计划

### 支持路

- If the 12<sup>th</sup> from Lagn Pad is conjunct Surya, Shukra and Rahu, there will be loss of wealth through the king.
- 太阳金星罗睺同处上升 Pad 起第 12 宫 因国王失财

### 反例或取消路

- O excellent of the Brahmins, if the 12<sup>th</sup> from Lagn Pad does not receive a Drishti, as the 11<sup>th</sup> from Lagn Pad receives a Drishti from a Grah, then the gains will be uninterrupted
- 第 12 宫不受照时得益不中断

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 上升 Pad 怎么求

## 上游问题

- 无

## 停止条件

- 缺少太阳、金星、罗睺相对上升 Pad 起第 12 宫的落宫事实时停止。
- 缺少本盘上升 Pad（Lagn Pad）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
