---
method: ch29-v18-chandra-drishti-more-losses
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮相照该三星所在之宫：损失更多

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮会不会加重我的破财
- 损失还会不会更大

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
- 月亮（Chandra）是否相照上升 Pad（Lagn Pad）起第 12 宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch29-v18-chandra-drishti-more-losses.step-001

- 动作：在三星同处上升 Pad（Lagn Pad）起第 12 宫成立之后，再看月亮（Chandra）是否相照该宫。
- 适用范围：原文的「the said trio in the said Bhava」承同偈前句同处上升 Pad 起第 12 宫的太阳、金星、罗睺三星。
- 原文最小意思：上升 Pad（Lagn Pad）起第 12 宫与太阳（Surya）、金星（Shukra）、罗睺（Rahu）同处，而月亮（Chandra）相照该宫中的这三颗行星时，特别会造成更多这类损失。
- 本步骤产出事实：["月亮相照上升 Pad 起第 12 宫三星的加重判定"]
- 所需事实：["太阳（Surya）是否落上升 Pad（Lagn Pad）起第 12 宫", "金星（Shukra）是否落上升 Pad（Lagn Pad）起第 12 宫", "罗睺（Rahu）是否落上升 Pad（Lagn Pad）起第 12 宫", "月亮（Chandra）是否相照上升 Pad（Lagn Pad）起第 12 宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落上升 Pad（Lagn Pad）起第 12 宫"}, {"fact_key": "金星（Shukra）是否落上升 Pad（Lagn Pad）起第 12 宫"}, {"fact_key": "罗睺（Rahu）是否落上升 Pad（Lagn Pad）起第 12 宫"}, {"fact_key": "月亮（Chandra）是否相照上升 Pad（Lagn Pad）起第 12 宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断损失金额或年份。", "月亮相照只在三星同处成立时加重，不得单独用月亮相照断失财。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落上升 Pad（Lagn Pad）起第 12 宫、金星（Shukra）是否落上升 Pad（Lagn Pad）起第 12 宫、罗睺（Rahu）是否落上升 Pad（Lagn Pad）起第 12 宫、月亮（Chandra）是否相照上升 Pad（Lagn Pad）起第 12 宫。
- 缺失即停字段：["太阳（Surya）是否落上升 Pad（Lagn Pad）起第 12 宫", "金星（Shukra）是否落上升 Pad（Lagn Pad）起第 12 宫", "罗睺（Rahu）是否落上升 Pad（Lagn Pad）起第 12 宫", "月亮（Chandra）是否相照上升 Pad（Lagn Pad）起第 12 宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v18`｜PDF [62]｜“If the 12<sup>th</sup> from Lagn Pad is conjunct Surya, Shukra and Rahu, there will be loss of wealth through the king.”
  - `bphs-97:santhanam:ch29:v18`｜PDF [62]｜“Chandra, giving a Drishti to (the said trio in the said Bhava), will specifically cause more such losses.”


## 四路查书计划

### 支持路

- Chandra, giving a Drishti to (the said trio in the said Bhava), will specifically cause more such losses.
- 月亮相照上升 Pad 起第 12 宫三星 损失更多

### 反例或取消路

- 无

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 上升 Pad 怎么求

## 上游问题

- 无

## 停止条件

- 缺少三星同处上升 Pad 起第 12 宫的事实时停止。
- 缺少月亮是否相照该宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
