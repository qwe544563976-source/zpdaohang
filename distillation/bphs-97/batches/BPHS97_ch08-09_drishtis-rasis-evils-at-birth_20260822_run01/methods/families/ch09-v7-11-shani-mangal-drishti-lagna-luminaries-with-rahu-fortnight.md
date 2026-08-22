---
method: ch09-v7-11-shani-mangal-drishti-lagna-luminaries-with-rahu-fortnight
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 土星与火星相照上升、二曜与罗睺同宫：孩子只活半个月

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 土星火星照上升会怎样
- 日月与罗睺同宫有什么凶
- 孩子能活多久

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 土星（Shani）是否相照上升（Lagna）
- 火星（Mangal）是否相照上升（Lagna）
- 太阳（Surya）是否与罗睺（Rahu）同宫
- 月亮（Chandra）是否与罗睺（Rahu）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v7-11-shani-mangal-drishti-lagna-luminaries-with-rahu-fortnight.step-001

- 动作：核对土星与火星是否相照上升，以及二曜是否与罗睺同宫（在别处）。
- 适用范围：仅限本命盘出生时的凶象；原文写 the luminaries（二曜），本方法按二曜为太阳与月亮取事实。
- 原文最小意思：土星（Shani）与火星（Mangal）相照上升（Lagna），同时二曜（太阳 Surya 与月亮 Chandra）在别处与罗睺（Rahu）同宫时，孩子只活半个月。
- 本步骤产出事实：["土火照上升兼二曜会罗睺的存活期判定"]
- 所需事实：["土星（Shani）是否相照上升（Lagna）", "火星（Mangal）是否相照上升（Lagna）", "太阳（Surya）是否与罗睺（Rahu）同宫", "月亮（Chandra）是否与罗睺（Rahu）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否相照上升（Lagna）"}, {"fact_key": "火星（Mangal）是否相照上升（Lagna）"}, {"fact_key": "太阳（Surya）是否与罗睺（Rahu）同宫"}, {"fact_key": "月亮（Chandra）是否与罗睺（Rahu）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把半个月改成原文没写的其他期限。", "不得漏掉二曜与罗睺同宫这一前提。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星（Shani）是否相照上升（Lagna）、火星（Mangal）是否相照上升（Lagna）、太阳（Surya）是否与罗睺（Rahu）同宫、月亮（Chandra）是否与罗睺（Rahu）同宫。
- 缺失即停字段：["土星（Shani）是否相照上升（Lagna）", "火星（Mangal）是否相照上升（Lagna）", "太阳（Surya）是否与罗睺（Rahu）同宫", "月亮（Chandra）是否与罗睺（Rahu）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v7-11`｜PDF [22]｜“If Shani and Mangal give a Drishti to Lagna, as the luminaries are yuti with Rahu (elsewhere), the child will live a fortnight.”


## 四路查书计划

### 支持路

- If Shani and Mangal give a Drishti to Lagna, as the luminaries are yuti with Rahu (elsewhere), the child will live a fortnight
- 土星火星照上升 日月会罗睺 半月

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils
- All evils are destroyed, if a benefic drishties Lagn of one born during the night in the bright half.
- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Short-life Combinations (up to Sloka 23)

### 判断方法路

- Evils at Birth
- O Brahmin, I have earlier stated Drishtis, based on Rāśis. The other kind is between Grahas, which I detail below.
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 相照怎么算

## 上游问题

- 无

## 停止条件

- 缺少土星、火星对上升的相照事实时停止。
- 缺少太阳、月亮与罗睺的同宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
