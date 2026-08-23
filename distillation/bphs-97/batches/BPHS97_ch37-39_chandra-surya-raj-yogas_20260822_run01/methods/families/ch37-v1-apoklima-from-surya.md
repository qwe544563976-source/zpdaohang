---
method: ch37-v1-apoklima-from-surya
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮相对太阳落果宫：结果优异

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的财力和才智会不会很好
- 月亮离太阳的位置对我有利吗

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘月亮（Chandra）以太阳（Surya）为参照落在哪一宫
- 月亮（Chandra）以太阳（Surya）为参照是否落果宫（Apoklima）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch37-v1-apoklima-from-surya.step-001

- 动作：以太阳（Surya）为起点数月亮（Chandra）的位置，核对它是否落果宫（Apoklima），据此读取原文这一档的断语。
- 适用范围：仅限本命盘中以太阳为参照的月亮位置；原文此分句承前省略主语，主语是前半句的 one’s wealth, intelligence and skill。
- 原文最小意思：月亮（Chandra）以太阳（Surya）为参照落在果宫（Apoklima）时，其财富、智力与技能会很优异。
- 本步骤产出事实：["月亮相对太阳落果宫的断语"]
- 所需事实：["本盘月亮（Chandra）以太阳（Surya）为参照落在哪一宫", "月亮（Chandra）以太阳（Surya）为参照是否落果宫（Apoklima）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘月亮（Chandra）以太阳（Surya）为参照落在哪一宫"}, {"fact_key": "月亮（Chandra）以太阳（Surya）为参照是否落果宫（Apoklima）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断具体财富数额、名位或事件时间。", "原文本句只写果宫（Apoklima）一档，不得把这条断语套到角宫（Kendr）或续宫（Panaphara）。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘月亮（Chandra）以太阳（Surya）为参照落在哪一宫、月亮（Chandra）以太阳（Surya）为参照是否落果宫（Apoklima）。
- 缺失即停字段：["本盘月亮（Chandra）以太阳（Surya）为参照落在哪一宫", "月亮（Chandra）以太阳（Surya）为参照是否落果宫（Apoklima）"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v1`｜PDF [81]｜“If Chandra with reference to Surya is in a Kendr, one’s wealth, intelligence and skill will be little, if in a Panaphara, will be meddling, if in a Apoklima, will be excellent.”


## 四路查书计划

### 支持路

- if in a Apoklima, will be excellent
- 月亮距太阳落果宫 财富智力技能优异

### 反例或取消路

- If Chandra with reference to Surya is in a Kendr, one’s wealth, intelligence and skill will be little
- The life span of the child will be either 2 months, or 6 months only, if all Grahas devoid of strength are relegated to Apoklima Bhavas

### 适用边界路

- Dhan, Putr, Randhr and Labh Bhava are Panapharas (succedents), while Sahaj, Ari, Dharm and Vyaya Bhava are called Apoklimas (cadents)
- A Grah in a Kon gets full strength, while one in Panaphara Bhava gets half and the one in Apoklima Bhava gets a quarter, as Kendradi Bal
- 果宫（Apoklima）在本书里的定义

### 判断方法路

- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn
- 从月亮与太阳起算的宫位该怎么读

## 上游问题

- 无

## 停止条件

- 缺少月亮以太阳为参照的落宫事实时停止。
- 无法判定该位置是否属于果宫（Apoklima）时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
