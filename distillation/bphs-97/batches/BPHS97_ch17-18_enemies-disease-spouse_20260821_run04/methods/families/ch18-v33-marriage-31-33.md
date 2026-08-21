---
method: ch18-v33-marriage-31-33
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 婚期第31年与第33年：金星落九宫起第九宫（即五宫）、罗睺落五宫或九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会在第31年还是第33年结婚
- 罗睺落五宫或九宫对婚期有什么说法

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 金星（Shukra）是否落五宫（Putr）

## 按情况检查的事实

- 罗睺（Rahu）是否落五宫（Putr）
- 罗睺（Rahu）是否落九宫（Dharm）

## 依赖方法

- 无

## 执行步骤

### ch18-v33-marriage-31-33.step-001

- 动作：核对金星（Shukra）是否落在从九宫（Dharm）起算的第九宫、即五宫（Putr），再看罗睺（Rahu）是否落在原文所说的两宫之一，判断婚期。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；本句「the said Bhavas」由原文自注为 Putr／Dharm 两宫；原文只给第31与第33年。
- 原文最小意思：金星（Shukra）落在从九宫（Dharm）起算的第九宫、即五宫（Putr），且罗睺（Rahu）落在上述两宫之一、即五宫（Putr）或九宫（Dharm）时，婚期在第31或第33年。
- 本步骤产出事实：["金星落五宫且罗睺落五宫或九宫主第31或第33年成婚判定"]
- 所需事实：["金星（Shukra）是否落五宫（Putr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落五宫（Putr）"}, {"operator": "OR", "operands": [{"fact_key": "罗睺（Rahu）是否落五宫（Putr）"}, {"fact_key": "罗睺（Rahu）是否落九宫（Dharm）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "金星（Shukra）是否落五宫（Putr）"}, "required_fact_keys": ["罗睺（Rahu）是否落五宫（Putr）"], "branch_condition_logic": {"fact_key": "罗睺（Rahu）是否落五宫（Putr）"}, "selection_group": "ch18-v33-marriage-31-33.step-001:rahu-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：罗睺（Rahu）是否落五宫（Putr）。"}, {"when": {"fact_key": "金星（Shukra）是否落五宫（Putr）"}, "required_fact_keys": ["罗睺（Rahu）是否落九宫（Dharm）"], "branch_condition_logic": {"fact_key": "罗睺（Rahu）是否落九宫（Dharm）"}, "selection_group": "ch18-v33-marriage-31-33.step-001:rahu-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：罗睺（Rahu）是否落九宫（Dharm）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把罗睺（Rahu）落五宫与落九宫合并成两者都要——原文是两宫之一。", "不得据此推断婚姻次数或配偶身份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：金星（Shukra）是否落五宫（Putr）。
- 缺失即停字段：["金星（Shukra）是否落五宫（Putr）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v33`｜PDF [35]｜“Should Shukra be in Dharm from Dharm (i.e. in Putr Bhava), while Rahu is in one of the said Bhavas (i.e. in Putr/Dharm), marriage will take place during 31<sup>st</sup> , or 33<sup>rd</sup> year.”


## 四路查书计划

### 支持路

- 金星落九宫起第九宫 即五宫 罗睺落五宫或九宫 第31年 第33年 婚期

### 反例或取消路

- The native will marry at 30, or 27, if Shukra is in Lagna, while the 7th Lord is in Yuvati itself
- If Surya is in Yuvati, while his dispositor is yuti with Shukr, there will be marriage at 7th, or 11th year of age

### 适用边界路

- Dharm from Dharm (i.e. in Putr Bhava) 从某宫起算另一宫的算法
- TIME OF MARRIAGE (upto Sloka 34)

### 判断方法路

- 判断婚期时罗睺（Rahu）落宫怎么用

## 上游问题

- 无

## 停止条件

- 缺少金星（Shukra）落宫事实时停止。
- 选中罗睺（Rahu）分支后缺少该分支落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
