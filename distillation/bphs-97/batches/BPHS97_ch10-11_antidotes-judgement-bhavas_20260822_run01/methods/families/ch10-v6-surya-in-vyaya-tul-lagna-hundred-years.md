---
method: ch10-v6-surya-in-vyaya-tul-lagna-hundred-years
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 百年寿命：天秤上升者太阳落十二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能活多久
- 天秤上升太阳落十二宫怎么看寿命

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升（Lagna）所在星座是否为天秤座（Tul）
- 太阳（Surya）是否落十二宫（Vyaya）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch10-v6-surya-in-vyaya-tul-lagna-hundred-years.step-001

- 动作：核对上升是否为天秤（Tul Lagn），并核对太阳（Surya）是否落十二宫（Vyaya）。
- 适用范围：仅限天秤上升（Tul Lagn）的本命盘；原文只给这一组条件与百年寿命的断语，未给别的上升或别的寿命档次。
- 原文最小意思：生于天秤上升（Tul Lagn）者，太阳（Surya）落十二宫（Vyaya）时，得百年寿命。
- 本步骤产出事实：["天秤上升太阳落十二宫百年寿命判定"]
- 所需事实：["本盘上升（Lagna）所在星座是否为天秤座（Tul）", "太阳（Surya）是否落十二宫（Vyaya）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagna）所在星座是否为天秤座（Tul）"}, {"fact_key": "太阳（Surya）是否落十二宫（Vyaya）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把本条推广到天秤以外的上升。", "不得把百年改写成别的年数或寿命档次。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagna）所在星座是否为天秤座（Tul）、太阳（Surya）是否落十二宫（Vyaya）。
- 缺失即停字段：["本盘上升（Lagna）所在星座是否为天秤座（Tul）", "太阳（Surya）是否落十二宫（Vyaya）"]
- 原文证据：
  - `bphs-97:santhanam:ch10:v6`｜PDF [25]｜“Surya in Vyaya will confer a hundred-year life span on one born in Tul Lagn.”


## 四路查书计划

### 支持路

- Surya in Vyaya will confer a hundred-year life span on one born in Tul Lagn
- 天秤上升 太阳落十二宫 百年寿命

### 反例或取消路

- If Lagn’s Lord is in Ari, Randhr, or Vyaya Bhava, yuti with malefics and devoid of Yuti with and/or Drishti from a benefic, short life will come to pass
- If malefics are in Kendras, devoid of Yuti with, or a Drishti from benefics, while Lagn’s Lord is not strong, only short life will result

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age
- The life-span in Bal Risht is 8 years, in Yog Risht 20 years, in short, medium and long lives, respectively, 32, 64 and 120 years

### 判断方法路

- O Brahmin, for the benefit of mankind I narrate methods of ascertaining longevity
- Longevity
- 怎样推算寿命

## 上游问题

- 无

## 停止条件

- 缺少上升星座事实时停止。
- 缺少太阳落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
