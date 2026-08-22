---
method: ch09-v42-rahu-guru-in-inimical-rasi-in-tanu-or-bandhu-father-absent
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 罗睺与木星同落敌星座且该宫为一宫或四宫：父亲到命主 23 岁才见到他

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 罗睺木星同宫在敌星座怎么断
- 什么时候能见到父亲

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 罗睺（Rahu）是否与木星（Guru）同宫
- 罗睺（Rahu）与木星（Guru）所在星座（Rāśi）是否为敌星座（inimical Rashi）

## 按情况检查的事实

- 罗睺（Rahu）与木星（Guru）是否同落一宫（Tanu Bhava）
- 罗睺（Rahu）与木星（Guru）是否同落四宫（Bandhu Bhava）

## 依赖方法

- 无

## 执行步骤

### ch09-v42-rahu-guru-in-inimical-rasi-in-tanu-or-bandhu-father-absent.step-001

- 动作：核对罗睺与木星是否同处敌星座，并核对该处是一宫还是四宫。
- 适用范围：仅限本命盘对父子相见的判断；原文只写敌星座，未指明与谁为敌，未确定即停判。
- 原文最小意思：罗睺（Rahu）与木星（Guru）同处一个敌星座（inimical Rashi）、且该处即一宫（Tanu）或四宫（Bandhu Bhava）时，父亲要到命主 23 岁才会见到他。
- 本步骤产出事实：["罗睺木星同落敌星座的父子相见时点判定"]
- 所需事实：["罗睺（Rahu）是否与木星（Guru）同宫", "罗睺（Rahu）与木星（Guru）所在星座（Rāśi）是否为敌星座（inimical Rashi）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "罗睺（Rahu）是否与木星（Guru）同宫"}, {"fact_key": "罗睺（Rahu）与木星（Guru）所在星座（Rāśi）是否为敌星座（inimical Rashi）"}]}, {"operator": "OR", "operands": [{"fact_key": "罗睺（Rahu）与木星（Guru）是否同落一宫（Tanu Bhava）"}, {"fact_key": "罗睺（Rahu）与木星（Guru）是否同落四宫（Bandhu Bhava）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "罗睺（Rahu）是否与木星（Guru）同宫"}, {"fact_key": "罗睺（Rahu）与木星（Guru）所在星座（Rāśi）是否为敌星座（inimical Rashi）"}]}, "required_fact_keys": ["罗睺（Rahu）与木星（Guru）是否同落一宫（Tanu Bhava）"], "branch_condition_logic": {"fact_key": "罗睺（Rahu）与木星（Guru）是否同落一宫（Tanu Bhava）"}, "selection_group": "ch09-v42-rahu-guru-in-inimical-rasi-in-tanu-or-bandhu-father-absent.step-001:yuti-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：罗睺（Rahu）与木星（Guru）是否同落一宫（Tanu Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "罗睺（Rahu）是否与木星（Guru）同宫"}, {"fact_key": "罗睺（Rahu）与木星（Guru）所在星座（Rāśi）是否为敌星座（inimical Rashi）"}]}, "required_fact_keys": ["罗睺（Rahu）与木星（Guru）是否同落四宫（Bandhu Bhava）"], "branch_condition_logic": {"fact_key": "罗睺（Rahu）与木星（Guru）是否同落四宫（Bandhu Bhava）"}, "selection_group": "ch09-v42-rahu-guru-in-inimical-rasi-in-tanu-or-bandhu-father-absent.step-001:yuti-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：罗睺（Rahu）与木星（Guru）是否同落四宫（Bandhu Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文指定敌星座（inimical Rashi）是与哪一颗行星为敌——原文没有写，未确定即停判。", "不得把 23 岁改成原文没写的其他年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：罗睺（Rahu）是否与木星（Guru）同宫、罗睺（Rahu）与木星（Guru）所在星座（Rāśi）是否为敌星座（inimical Rashi）。
- 缺失即停字段：["罗睺（Rahu）是否与木星（Guru）同宫", "罗睺（Rahu）与木星（Guru）所在星座（Rāśi）是否为敌星座（inimical Rashi）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v42`｜PDF [24]｜“The father will not see the native till his (the native’s) 23<sup>rd</sup> year, if Rahu and Guru are together in an inimical Rashiidentical with Tanu, or Bandhu Bhava.”


## 四路查书计划

### 支持路

- The father will not see the native till his (the native’s) 23<sup>rd</sup> year, if Rahu and Guru are together in an inimical Rashiidentical with Tanu, or Bandhu Bhava
- 罗睺木星 敌星座 一宫四宫 23 岁 父亲

### 反例或取消路

- a single, but strong Guru in Lagn will ward off all the evils
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.

### 适用边界路

- Evil to Father (up to Sloka 42)
- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- 敌星座怎么定

## 上游问题

- 无

## 停止条件

- 原文只写 an inimical Rashi，未指明与谁为敌；该判准未确定即停判。
- 缺少罗睺与木星的同宫与落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
