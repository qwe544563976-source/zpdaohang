---
method: ch24-v15-dhan-lord-sahaj-benefic
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 勇敢、明智、有德而吝啬：二宫主落三宫（Sahaj）并与吉星发生关联

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 二宫主落三宫是什么性格
- 我这个人算不算有胆识

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫主（Dhan's Lord）是否落三宫（Sahaj）
- 二宫主（Dhan's Lord）是否与吉星发生关联（related）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v15-dhan-lord-sahaj-benefic.step-001

- 动作：先核对二宫主（Dhan's Lord）是否落三宫（Sahaj），再核对它是否与吉星发生原文所说的关联（related）。
- 适用范围：仅限本命盘二宫主（Dhan's Lord）落宫主题；原文只写 when related to a benefic，省略了关系的主语，本步把关系的一端写成二宫主本身；原文没有界定关系类型（同宫、相照或其他），关系判准未确定即停判；吉星名册以本书 ch03:v11 的界定为准；原文未给时间限定。
- 原文最小意思：二宫主（Dhan's Lord）落三宫（Sahaj）并与吉星发生关联时，命主会勇敢、明智、有德、好色而吝啬。
- 本步骤产出事实：["二宫主落三宫并与吉星关联的品性判定"]
- 所需事实：["二宫主（Dhan's Lord）是否落三宫（Sahaj）", "二宫主（Dhan's Lord）是否与吉星发生关联（related）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落三宫（Sahaj）"}, {"fact_key": "二宫主（Dhan's Lord）是否与吉星发生关联（related）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自行把 related 限定成某一种关系（例如只算同宫，或只算相照）。", "不得据此推断兄弟数目、财富数额或时间。", "不得把本句的吉星换成凶星来套用（同偈另有凶星一句，另立方法）。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫主（Dhan's Lord）是否落三宫（Sahaj）、二宫主（Dhan's Lord）是否与吉星发生关联（related）。
- 缺失即停字段：["二宫主（Dhan's Lord）是否落三宫（Sahaj）", "二宫主（Dhan's Lord）是否与吉星发生关联（related）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v15`｜PDF [41, 42]｜“If Dhan’s Lord is in Sahaj Bhava, the native will be valorous, wise, virtuous, lustful and miserly; all these, when related to a benefic.”


## 四路查书计划

### 支持路

- If Dhan’s Lord is in Sahaj Bhava, the native will be valorous, wise, virtuous, lustful and miserly; all these, when related to a benefic.
- 二宫主落三宫 与吉星关联 勇敢 明智 吝啬

### 反例或取消路

- If related to a malefic, the native will be
- If Dhan’s Lord is in Vyaya Bhava, the native will be adventurous, be devoid of wealth and be interested in other’s wealth

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Sahaj Bhava. From Sahaj Bhava know of the following: valour, servants (attending etc.), brothers, sisters etc.

### 判断方法路

- Effects of Dhan’s Lord in Various Bhavas (up to Sloka 24)
- 原文说与吉星 related 时，related 在本书里指哪几种关系

## 上游问题

- 无

## 停止条件

- 缺少二宫主是否落三宫（Sahaj）的事实时停止。
- 原文没有给出 related 的关系判准，判准未确定时停止。
- 吉星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
