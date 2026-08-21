---
method: ch22-v5-labh-lord-with-benefic-500-nishkas
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第40年得500 Nishkas：十一宫主与吉星同宫并落角宫或三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我四十岁前后有没有进账
- 十一宫主与吉星同宫是什么效果

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十一宫主（Labh's Lord）是否与吉星同宫

## 按情况检查的事实

- 十一宫主（Labh's Lord）是否落角宫
- 十一宫主（Labh's Lord）是否落三角宫

## 依赖方法

- 无

## 执行步骤

### ch22-v5-labh-lord-with-benefic-500-nishkas.step-001

- 动作：核对十一宫主（Labh's Lord）是否与吉星同宫；成立时再看这一同宫落在角宫还是三角宫。
- 适用范围：仅限本命盘十一宫（Labh）收获主题；原文 in an angle, or in a trine 是两个并列备选，任一成立即可；同宫双方同落一宫，故按十一宫主的落宫取值；原文以 his 指称本人。
- 原文最小意思：十一宫主与吉星同宫，并落角宫或落三角宫时，本人在第40年获得500 Nishkas。
- 本步骤产出事实：["十一宫主与吉星同宫第40年收获判定"]
- 所需事实：["十一宫主（Labh's Lord）是否与吉星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否与吉星同宫"}, {"operator": "OR", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落角宫"}, {"fact_key": "十一宫主（Labh's Lord）是否落三角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "十一宫主（Labh's Lord）是否与吉星同宫"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落角宫"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否落角宫"}, "selection_group": "ch22-v5-labh-lord-with-benefic-500-nishkas.step-001:labh-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落角宫。"}, {"when": {"fact_key": "十一宫主（Labh's Lord）是否与吉星同宫"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落三角宫"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否落三角宫"}, "selection_group": "ch22-v5-labh-lord-with-benefic-500-nishkas.step-001:labh-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得要求角宫与三角宫同时成立：原文两者任选其一。", "不得把 500 Nishkas 换算成任何现代货币金额，也不得挪动第40年这一年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十一宫主（Labh's Lord）是否与吉星同宫。
- 缺失即停字段：["十一宫主（Labh's Lord）是否与吉星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch22:v5`｜PDF [39]｜“If Labh’s Lord is yuti with a benefic in an angle, or in a trine, the native will acquire 500 Nishkas in his 40<sup>th</sup> year.”


## 四路查书计划

### 支持路

- If Labh’s Lord is yuti with a benefic in an angle, or in a trine, the native will acquire 500 Nishkas in his 40th year
- 十一宫主（Labh's Lord）与吉星同宫 角宫 三角宫 第40年 500 Nishkas

### 反例或取消路

- There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic
- There will be penury right from birth and the native will have to beg even for his food, if the Lords of Dhan and Labh Bhava are both combust, or with malefics

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Putr and Dharm Bhava are known by the name Kon (or trine)

### 判断方法路

- If the Lord of Dhan is in an angle, while Labh Lord is in a trine thereof, or is drishtied by, or yuti with Guru and Shukr, the subject will be wealthy
- If Labh’s Lord is in Labh Bhava, the native will gain in all his undertakings, while his learning and happiness will be on the increase day by day

## 上游问题

- 无

## 停止条件

- 缺少十一宫主与吉星同宫事实时停止。
- 落角宫与落三角宫两个分支事实都缺时停止。
- 吉星名册未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
