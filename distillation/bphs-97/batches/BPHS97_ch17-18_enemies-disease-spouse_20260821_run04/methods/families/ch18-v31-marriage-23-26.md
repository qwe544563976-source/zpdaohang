---
method: ch18-v31-marriage-23-26
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 婚期第23年与第26年：七宫主落十二宫、本命主星在九分盘落七宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 七宫主落十二宫时婚期在哪一年
- 我的婚期是不是在第23年或第26年

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 七宫主（Yuvati's Lord）是否落十二宫（Vyaya）
- 本命主星（natal Lord）在九分盘（Navamsa D9）中是否落七宫（Yuvati）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v31-marriage-23-26.step-001

- 动作：核对七宫主（Yuvati's Lord）是否落十二宫（Vyaya），并核对本命主星在九分盘（Navamsa D9）中是否落七宫（Yuvati），判断婚期。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；原文只写 the natal Lord，未指明它是哪一宫之主，该指代在本批范围内无法确定，本步因此停判；原文只给第23与第26年。
- 原文最小意思：七宫主（Yuvati's Lord）落十二宫（Vyaya），且本命主星（natal Lord）在九分盘（Navamsa D9）中落七宫（Yuvati）时，婚期在第23或第26年（年龄）。
- 本步骤产出事实：["七宫主落十二宫且本命主星九分盘落七宫主第23或第26年成婚判定"]
- 所需事实：["七宫主（Yuvati's Lord）是否落十二宫（Vyaya）", "本命主星（natal Lord）在九分盘（Navamsa D9）中是否落七宫（Yuvati）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落十二宫（Vyaya）"}, {"fact_key": "本命主星（natal Lord）在九分盘（Navamsa D9）中是否落七宫（Yuvati）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断婚姻的好坏或配偶健康。", "不得把 the natal Lord 坐实为任何一宫之主（含上升主）：原文未指明，全书亦仅此一处出现该词，须经原书核对确定指代后才可绑定；未确定前本步停判。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：七宫主（Yuvati's Lord）是否落十二宫（Vyaya）、本命主星（natal Lord）在九分盘（Navamsa D9）中是否落七宫（Yuvati）。
- 缺失即停字段：["七宫主（Yuvati's Lord）是否落十二宫（Vyaya）", "本命主星（natal Lord）在九分盘（Navamsa D9）中是否落七宫（Yuvati）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v31`｜PDF [35]｜“Should Yuvati Lord be in Vyaya, while the natal Lord is in Yuvati in Navamsa, marriage will be in 23<sup>rd</sup> /26<sup>th</sup> year of age.”


## 四路查书计划

### 支持路

- 七宫主落十二宫 本命主星九分盘落七宫 第23年 第26年 婚期

### 反例或取消路

- Marriage will take place during the 11th year, if Shukra is in an angle from Lagna, while Lagn Lord is in Makar, or Kumbh
- If Chandra is in Yuvati, as Yuvati Lord is in Vyaya the native will not be endowed with marital happiness

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34)
- natal Lord Lagn Lord Navamsa 七宫 判定口径 版本差异

### 判断方法路

- 判断婚期时怎么用九分盘（Navamsa D9）

## 上游问题

- 无

## 停止条件

- 缺少七宫主（Yuvati's Lord）落宫事实时停止。
- the natal Lord 指代未确定时停止：原文未指明它是哪一宫之主，不得自行绑定为上升主或任何别的宫主。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
