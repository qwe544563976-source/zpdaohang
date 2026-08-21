---
method: ch18-v35-39-wife-snake-bite
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 妻子婚后三日内因蛇咬去世：罗睺落二宫、火星落七宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我妻子会不会有性命之忧
- 罗睺落二宫、火星落七宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 罗睺（Rahu）是否落二宫（Dhan）
- 火星（Mangal）是否落七宫（Yuvati）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v35-39-wife-snake-bite.step-001

- 动作：核对罗睺（Rahu）是否落二宫（Dhan），并核对火星（Mangal）是否落七宫（Yuvati）。
- 适用范围：仅限本命盘七宫（Yuvati）配偶存亡主题；原文以「the native’s wife」立说，属男命框架；原文把时间限定在婚后三日内。
- 原文最小意思：罗睺（Rahu）落二宫（Dhan），且火星（Mangal）落七宫（Yuvati）时，命主的妻子在婚后三日内因蛇咬去世。
- 本步骤产出事实：["罗睺落二宫且火星落七宫主妻子婚后三日内蛇咬去世判定"]
- 所需事实：["罗睺（Rahu）是否落二宫（Dhan）", "火星（Mangal）是否落七宫（Yuvati）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "罗睺（Rahu）是否落二宫（Dhan）"}, {"fact_key": "火星（Mangal）是否落七宫（Yuvati）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把蛇咬扩大成其他死因或其他事故。", "不得把婚后三日之外的时间也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：罗睺（Rahu）是否落二宫（Dhan）、火星（Mangal）是否落七宫（Yuvati）。
- 缺失即停字段：["罗睺（Rahu）是否落二宫（Dhan）", "火星（Mangal）是否落七宫（Yuvati）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v35-39`｜PDF [35]｜“The native’s wife will die within three days of marriage due to snake bite, if the native has Rahu in Dhan and Mangal in Yuvati.”


## 四路查书计划

### 支持路

- The native’s wife will die within three days of marriage due to snake bite, Rahu in Dhan and Mangal in Yuvati
- 罗睺落二宫 火星落七宫 婚后三日 蛇咬 妻子去世

### 反例或取消路

- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)
- WORTHY SPOUSE The native will beget a spouse endowed with (the seven principal) virtues, who will expand his dynasty by sons and grandsons

### 适用边界路

- DEATH OF WlFE lf Ari, 7th and 8th are in their order occupied by Mangal, Rahu and Shani, the native’s wife will not live (long)
- If Mangal and Shukra are in Yuvati, or, if Shani is Yuvati, while the Lord of Lagn is in Randhr, the native will have 3 wives
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- 判断配偶灾厄应检查什么

## 上游问题

- 无

## 停止条件

- 缺少罗睺（Rahu）落宫事实时停止。
- 缺少火星（Mangal）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
