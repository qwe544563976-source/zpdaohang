---
method: ch17-v23-smallpox-karm-year
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Karm 年与第30岁的天花：土星落八宫、火星落七宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会出天花一类的急性病
- 三十岁前后健康怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 土星（Shani）是否落八宫（Randhr）
- 火星（Mangal）是否落七宫（Yuvati）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v23-smallpox-karm-year.step-001

- 动作：核对土星是否落八宫、火星是否落七宫。
- 适用范围：仅限本命盘天花主题；原文以 Karm 年称呼年份，未换算成具体年岁，另给第30岁。
- 原文最小意思：土星落八宫、火星落七宫时，Karm 年与第30岁会出天花。
- 本步骤产出事实：["天花凶年判定"]
- 所需事实：["土星（Shani）是否落八宫（Randhr）", "火星（Mangal）是否落七宫（Yuvati）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否落八宫（Randhr）"}, {"fact_key": "火星（Mangal）是否落七宫（Yuvati）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 Karm 年自行换算成本条没写出的年岁。", "不得据此推断轻重与转归。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星（Shani）是否落八宫（Randhr）、火星（Mangal）是否落七宫（Yuvati）。
- 缺失即停字段：["土星（Shani）是否落八宫（Randhr）", "火星（Mangal）是否落七宫（Yuvati）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v23-25`｜PDF [33]｜“Shani in Randhr, as Mangal is in Yuvati, all cause small-pox in Karm year and in 30<sup>th</sup> year of age.”


## 四路查书计划

### 支持路

- Shani in Randhr, as Mangal is in Yuvati, all cause small-pox in Karm year and in 30th year of age
- 土星八宫 火星七宫 天花 Karm 年

### 反例或取消路

- Guru in similar case will destroy any disease
- Lagn Lord is singly capable of counteracting all evils

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age
- Effects of Dashas 急病发作按大运定时

### 判断方法路

- 判断急性病年份应检查土星火星落宫

## 上游问题

- 无

## 停止条件

- 缺少土星落八宫事实时停止。
- 缺少火星落七宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
