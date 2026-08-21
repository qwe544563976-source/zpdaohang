---
method: ch13-v6-7-lords-in-evil-bhava-penniless
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 贫穷：二宫主与十一宫主同落凶宫且二宫被凶星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会一直没钱
- 什么样的盘会贫穷

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫主（Dhan's Lord）是否落凶宫（evil Bhava）
- 十一宫主（Labh's Lord）是否落凶宫（evil Bhava）
- 二宫（Dhan）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch13-v6-7-lords-in-evil-bhava-penniless.step-001

- 动作：核对二宫主与十一宫主是否都落凶宫（evil Bhava），并核对二宫是否被凶星占据。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；原文只写 evil Bhava，本句没有列出具体是哪几宫，凶宫范围未确定即停判。
- 原文最小意思：二宫主落凶宫（evil Bhava）、十一宫主也落凶宫，且二宫（Dhan Bhava）被凶星占据时，命主没有钱财。
- 本步骤产出事实：["二宫主与十一宫主落凶宫的贫穷判定"]
- 所需事实：["二宫主（Dhan's Lord）是否落凶宫（evil Bhava）", "十一宫主（Labh's Lord）是否落凶宫（evil Bhava）", "二宫（Dhan）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落凶宫（evil Bhava）"}, {"fact_key": "十一宫主（Labh's Lord）是否落凶宫（evil Bhava）"}, {"fact_key": "二宫（Dhan）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自行把 evil Bhava 认定为某几个宫位，本句没有列举，未确定即停判。", "不得据此推断贫穷的起止时间或程度。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫主（Dhan's Lord）是否落凶宫（evil Bhava）、十一宫主（Labh's Lord）是否落凶宫（evil Bhava）、二宫（Dhan）是否被凶星占据。
- 缺失即停字段：["二宫主（Dhan's Lord）是否落凶宫（evil Bhava）", "十一宫主（Labh's Lord）是否落凶宫（evil Bhava）", "二宫（Dhan）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v6-7`｜PDF [28]｜“One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic.”


## 四路查书计划

### 支持路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic
- 二宫主 十一宫主 落凶宫 二宫有凶星 贫穷

### 反例或取消路

- If Dhan Lord is in Labh, while the Lord of Labh in Dhan, wealth will be acquired by the native
- Surya in Dhan Bhava, receiving a Drishti from Shani, will cause penury, while, if Surya is in Dhan Bhava and does not receive a Drishti from Shani, riches and fame will be obtained
- Should Budh give a Drishti to Mangal and Shani in Dhan Bhava, there will be great wealth

### 适用边界路

- Note the Grahas, that are ruling the Rāśis, occupied by the Lords of Ari, Randhr and Vyaya Bhava. If the said dispositors are in such evil Bhavas in turn and are associated with, or receive a Drishti from malefics, the native will be miserable and indigent
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava

### 判断方法路

- Now I tell you some Yogas for poverty along with conditions of their nullifications
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- 判断贫穷要看二宫主与十一宫主落在哪一宫

## 上游问题

- 无

## 停止条件

- 凶宫（evil Bhava）的宫位范围原文本句未界定，未确定即停判。
- 缺少二宫主或十一宫主落宫事实时停止。
- 缺少二宫是否被凶星占据的事实时停止。
- 凶星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
