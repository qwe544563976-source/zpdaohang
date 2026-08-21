---
method: ch18-v42-wife-short-life
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 妻子不能久活：六宫、七宫、八宫依次被火星、罗睺、土星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我妻子的寿命长不长
- 火星、罗睺、土星分别落六宫七宫八宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 火星（Mangal）是否落六宫（Ari）
- 罗睺（Rahu）是否落七宫（Yuvati）
- 土星（Shani）是否落八宫（Randhr）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v42-wife-short-life.step-001

- 动作：核对六宫（Ari）、七宫（Yuvati）、八宫（Randhr）是否依次由火星（Mangal）、罗睺（Rahu）、土星（Shani）占据，判断妻子的存活。
- 适用范围：仅限本命盘七宫（Yuvati）配偶存亡主题；原文以「the native’s wife」立说，属男命框架；原文没有给年份或年龄。
- 原文最小意思：六宫（Ari）、七宫、八宫依次被火星（Mangal）、罗睺（Rahu）、土星（Shani）占据时，命主的妻子不能长久活着。
- 本步骤产出事实：["六七八宫依次被火星罗睺土星占据主妻子不能久活判定"]
- 所需事实：["火星（Mangal）是否落六宫（Ari）", "罗睺（Rahu）是否落七宫（Yuvati）", "土星（Shani）是否落八宫（Randhr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落六宫（Ari）"}, {"fact_key": "罗睺（Rahu）是否落七宫（Yuvati）"}, {"fact_key": "土星（Shani）是否落八宫（Randhr）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断具体去世年份或死因——原文只说不能长久活着。", "不得把三颗行星的对应宫位互换后仍套用本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：火星（Mangal）是否落六宫（Ari）、罗睺（Rahu）是否落七宫（Yuvati）、土星（Shani）是否落八宫（Randhr）。
- 缺失即停字段：["火星（Mangal）是否落六宫（Ari）", "罗睺（Rahu）是否落七宫（Yuvati）", "土星（Shani）是否落八宫（Randhr）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v42`｜PDF [35]｜“DEATH OF WlFE. lf Ari, 7<sup>th</sup> and 8<sup>th</sup> are in their order occupied by Mangal, Rahu and Shani, the native’s wife will not live (long).”


## 四路查书计划

### 支持路

- DEATH OF WlFE lf Ari, 7th and 8th are in their order occupied by Mangal, Rahu and Shani, the native’s wife will not live (long)
- 六宫火星 七宫罗睺 八宫土星 妻子不能久活

### 反例或取消路

- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)
- WORTHY SPOUSE the 7th Lord is exalted, while Yuvati is occupied by strong Lagna Lord and a benefic

### 适用边界路

- If Lagn’s Lord is a malefic and is placed in Yuvati Bhava, the natives wife will not live (long)
- LOSS OF SPOUSE Yuvati Lord is devoid of strength and is relegated to Ari, 8th, or Vyaya

### 判断方法路

- Effects of Yuvati Bhava malefics occupying Ari 7th 8th wife
- 判断妻子寿命应检查哪几宫

## 上游问题

- 无

## 停止条件

- 缺少火星（Mangal）落宫事实时停止。
- 缺少罗睺（Rahu）落宫事实时停止。
- 缺少土星（Shani）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
