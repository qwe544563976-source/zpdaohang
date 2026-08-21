---
method: ch13-v1-2-malefic-in-dhan-destroys-wealth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 毁掉财富：二宫内有凶星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 二宫有凶星代表什么
- 我的钱会不会守不住

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫（Dhan）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch13-v1-2-malefic-in-dhan-destroys-wealth.step-001

- 动作：核对二宫（Dhan）里是否有凶星。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；本句的 a malefic 承接同句前半的 in Dhan，落宫来自前半句。
- 原文最小意思：二宫（Dhan）内有凶星时，会毁掉财富。
- 本步骤产出事实：["二宫凶星的破财判定"]
- 所需事实：["二宫（Dhan）是否被凶星占据"]
- 条件关系：{"fact_key": "二宫（Dhan）是否被凶星占据"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断破财的时间或数额。", "不得把 destroy wealth 读成终身贫穷。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫（Dhan）是否被凶星占据。
- 缺失即停字段：["二宫（Dhan）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v1-2`｜PDF [27]｜“A benefic in Dhan will give wealth, while a malefic instead will destroy wealth.”


## 四路查书计划

### 支持路

- A benefic in Dhan will give wealth, while a malefic instead will destroy wealth
- 二宫有凶星 毁掉财富

### 反例或取消路

- Should Budh give a Drishti to Mangal and Shani in Dhan Bhava, there will be great wealth
- Surya in Dhan Bhava, receiving a Drishti from Shani, will cause penury, while, if Surya is in Dhan Bhava and does not receive a Drishti from Shani, riches and fame will be obtained

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava

### 判断方法路

- Effects of Dhan Bhava
- Now I tell you some Yogas for poverty along with conditions of their nullifications
- 判断破财要看二宫里有没有凶星

## 上游问题

- 无

## 停止条件

- 缺少二宫凶星占据事实时停止。
- 凶星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
