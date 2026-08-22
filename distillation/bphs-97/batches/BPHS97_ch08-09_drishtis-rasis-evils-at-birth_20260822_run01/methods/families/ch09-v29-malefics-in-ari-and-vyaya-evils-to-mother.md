---
method: ch09-v29-malefics-in-ari-and-vyaya-evils-to-mother
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶星落六宫与十二宫：给母亲带来凶事

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 凶星落六宫十二宫对母亲有什么影响
- 母亲的凶象怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 六宫（Ari Bhava）是否被凶星占据
- 十二宫（Vyaya Bhava）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v29-malefics-in-ari-and-vyaya-evils-to-mother.step-001

- 动作：核对六宫与十二宫是否被凶星占据。
- 适用范围：仅限本命盘对母亲的凶象；原文只说带来凶事，不给凶事的具体内容。
- 原文最小意思：凶星落六宫（Ari）与十二宫（Vyaya Bhava）时，会给母亲带来凶事。
- 本步骤产出事实：["六宫十二宫凶星的母亲凶象判定"]
- 所需事实：["六宫（Ari Bhava）是否被凶星占据", "十二宫（Vyaya Bhava）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "六宫（Ari Bhava）是否被凶星占据"}, {"fact_key": "十二宫（Vyaya Bhava）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『凶事』补成去世等原文没写的具体结果。", "不得把两宫减为其中一宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：六宫（Ari Bhava）是否被凶星占据、十二宫（Vyaya Bhava）是否被凶星占据。
- 缺失即停字段：["六宫（Ari Bhava）是否被凶星占据", "十二宫（Vyaya Bhava）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v29`｜PDF [24]｜“Malefics in Ari and Vyaya Bhava will bring evils to mother.”


## 四路查书计划

### 支持路

- Malefics in Ari and Vyaya Bhava will bring evils to mother
- 凶星 六宫十二宫 母亲 凶事

### 反例或取消路

- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evils to Mother (up to Sloka 33)
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 母亲用哪颗星看

## 上游问题

- 无

## 停止条件

- 缺少六宫、十二宫的凶星占据事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
