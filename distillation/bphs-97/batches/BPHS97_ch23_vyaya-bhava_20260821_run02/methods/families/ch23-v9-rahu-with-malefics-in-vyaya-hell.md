---
method: ch23-v9-rahu-with-malefics-in-vyaya-hell
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 会下地狱：罗睺与火星、土星、太阳同落十二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我死后会怎么样
- 我盘里十二宫的凶星聚集意味着什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 罗睺（Rahu）是否落十二宫（Vyaya）
- 火星（Mangal）是否落十二宫（Vyaya）
- 土星（Shani）是否落十二宫（Vyaya）
- 太阳（Surya）是否落十二宫（Vyaya）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch23-v9-rahu-with-malefics-in-vyaya-hell.step-001

- 动作：核对罗睺（Rahu）是否落十二宫（Vyaya），并核对火星（Mangal）、土星（Shani）、太阳（Surya）是否同落十二宫。
- 适用范围：仅限本命盘十二宫（Vyaya Bhava）主题；原文要求四颗行星同落十二宫，缺一即不成立；原文未给时间限定。
- 原文最小意思：罗睺（Rahu）与火星（Mangal）、土星（Shani）、太阳（Surya）同落十二宫（Vyaya）时，命主会下地狱。
- 本步骤产出事实：["十二宫四凶聚集的死后去向判定"]
- 所需事实：["罗睺（Rahu）是否落十二宫（Vyaya）", "火星（Mangal）是否落十二宫（Vyaya）", "土星（Shani）是否落十二宫（Vyaya）", "太阳（Surya）是否落十二宫（Vyaya）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "罗睺（Rahu）是否落十二宫（Vyaya）"}, {"fact_key": "火星（Mangal）是否落十二宫（Vyaya）"}, {"fact_key": "土星（Shani）是否落十二宫（Vyaya）"}, {"fact_key": "太阳（Surya）是否落十二宫（Vyaya）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把四星同落缩减为其中任意一两颗落十二宫。", "不得据此推断死亡年份、死因或今生的具体祸福。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：罗睺（Rahu）是否落十二宫（Vyaya）、火星（Mangal）是否落十二宫（Vyaya）、土星（Shani）是否落十二宫（Vyaya）、太阳（Surya）是否落十二宫（Vyaya）。
- 缺失即停字段：["罗睺（Rahu）是否落十二宫（Vyaya）", "火星（Mangal）是否落十二宫（Vyaya）", "土星（Shani）是否落十二宫（Vyaya）", "太阳（Surya）是否落十二宫（Vyaya）"]
- 原文证据：
  - `bphs-97:santhanam:ch23:v9`｜PDF [40]｜“If Rahu is in Vyaya along with Mangal, Shani and Surya, the native will go to hell.”


## 四路查书计划

### 支持路

- If Rahu is in Vyaya along with Mangal, Shani and Surya, the native will go to hell.
- 罗睺 火星 土星 太阳 同落十二宫 下地狱

### 反例或取消路

- If there is a benefic in Vyaya, while its Lord is exalted, or is yuti with, or receives a Drishti from a benefic, one will attain final emancipation.
- Guru heaven, Chandra, or Shukra the world of Manes, Mangal and/or Surya earth (rebirth), Budh and/or Shani hell

### 适用边界路

- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Ascent after Death. According to the following Grahas in Vyaya, Yuvati, Ari, or Randhr Bhava, the native will attain one of the different worlds after death

### 判断方法路

- Just as these effects are derived from Tanu Bhava in regard to the native, similar deductions be made about co-borns etc. from Sahaj and other Bhavas.
- 死后去向要看十二宫里的哪些行星

## 上游问题

- 无

## 停止条件

- 四颗行星的落宫事实缺任意一条即停止。
- 缺少本盘十二宫落宫名单时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
