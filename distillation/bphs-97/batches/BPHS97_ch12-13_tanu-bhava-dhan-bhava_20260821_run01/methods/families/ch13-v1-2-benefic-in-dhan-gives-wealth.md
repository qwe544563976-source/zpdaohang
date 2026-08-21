---
method: ch13-v1-2-benefic-in-dhan-gives-wealth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 给予财富：二宫内有吉星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 二宫有吉星代表什么
- 我有没有进财的底子

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫（Dhan）是否被吉星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch13-v1-2-benefic-in-dhan-gives-wealth.step-001

- 动作：核对二宫（Dhan）里是否有吉星。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；原文没有说是哪一颗吉星，也没有给数额。
- 原文最小意思：二宫（Dhan）内有吉星时，会给予财富。
- 本步骤产出事实：["二宫吉星的财富判定"]
- 所需事实：["二宫（Dhan）是否被吉星占据"]
- 条件关系：{"fact_key": "二宫（Dhan）是否被吉星占据"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额或来源，原文只说给予财富。", "不得把这条推广到十一宫，本句只写 Dhan。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫（Dhan）是否被吉星占据。
- 缺失即停字段：["二宫（Dhan）是否被吉星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v1-2`｜PDF [27]｜“A benefic in Dhan will give wealth”


## 四路查书计划

### 支持路

- A benefic in Dhan will give wealth, while a malefic instead will destroy wealth
- 二宫有吉星 给予财富

### 反例或取消路

- while a malefic instead will destroy wealth
- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava

### 判断方法路

- Effects of Dhan Bhava
- Now I tell you some Yogas for poverty along with conditions of their nullifications
- 判断财运要看二宫里有吉星还是凶星

## 上游问题

- 无

## 停止条件

- 缺少二宫吉星占据事实时停止。
- 吉星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
