---
method: ch18-v35-39-wife-loss-13
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第13年失去妻子：上升主落陷、二宫主落八宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我第13年会不会失去妻子
- 上升主落陷对妻子有什么妨害

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagna's Lord）是否落陷
- 二宫主（Dhan's Lord）是否落八宫（Randhr）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v35-39-wife-loss-13.step-001

- 动作：核对上升主（Lagna's Lord）是否落在自己的落陷星座，并核对二宫主（Dhan's Lord）是否落八宫（Randhr），判断失去妻子的年份。
- 适用范围：仅限本命盘七宫（Yuvati）配偶存亡主题；原文以「wife」立说，属男命框架；原文只给第13年一个年份。
- 原文最小意思：上升主（Lagna's Lord）落在自己的落陷星座，且二宫主（Dhan's Lord）落八宫（Randhr）时，命主在第13年（年龄）失去妻子。
- 本步骤产出事实：["上升主落陷且二宫主落八宫主第13年失去妻子判定"]
- 所需事实：["上升主（Lagna's Lord）是否落陷", "二宫主（Dhan's Lord）是否落八宫（Randhr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagna's Lord）是否落陷"}, {"fact_key": "二宫主（Dhan's Lord）是否落八宫（Randhr）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断死因或再婚。", "不得把第13年之外的年份也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagna's Lord）是否落陷、二宫主（Dhan's Lord）是否落八宫（Randhr）。
- 缺失即停字段：["上升主（Lagna's Lord）是否落陷", "二宫主（Dhan's Lord）是否落八宫（Randhr）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v35-39`｜PDF [35]｜“Should the ascendat Lord be in his Rashiof debilitation, as Dhan Lord is in Randhr, loss of wife will occur in the 13<sup>th</sup> year of age.”


## 四路查书计划

### 支持路

- Should the ascendat Lord be in his Rashiof debilitation, as Dhan Lord is in Randhr, loss of wife will occur in the 13th year of age
- 上升主落陷 二宫主落八宫 第13年 失去妻子

### 反例或取消路

- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)
- THREE MARRIAGES Should Chandra be in Yuvati from Shukr, while Budh is in Yuvati from Chandra

### 适用边界路

- If Lagn’s Lord is a malefic and is placed in Yuvati Bhava, the natives wife will not live (long)
- LOSS OF SPOUSE Yuvati Lord is in fall the native’s wife will be destroyed

### 判断方法路

- Effects of Yuvati Bhava Lagna Lord debilitation wife loss
- 判断上升主落陷会带来什么

## 上游问题

- 无

## 停止条件

- 缺少上升主（Lagna's Lord）是否落陷的事实时停止。
- 缺少二宫主（Dhan's Lord）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
