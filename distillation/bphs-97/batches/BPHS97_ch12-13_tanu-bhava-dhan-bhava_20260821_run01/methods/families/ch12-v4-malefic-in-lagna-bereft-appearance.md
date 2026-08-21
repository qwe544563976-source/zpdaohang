---
method: ch12-v4-malefic-in-lagna-bereft-appearance
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 没有好相貌：一宫内有凶星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我相貌上有没有欠缺
- 一宫有凶星代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 一宫（Tanu）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch12-v4-malefic-in-lagna-bereft-appearance.step-001

- 动作：核对一宫（Lagn）里是否有凶星。
- 适用范围：仅限本命盘一宫（Tanu Bhava）相貌主题；本句的 a malefic 承接同句前半的 in Lagn，落宫来自前半句。
- 原文最小意思：一宫（Lagn）内有凶星时，会使人没有好相貌。
- 本步骤产出事实：["一宫凶星的相貌判定"]
- 所需事实：["一宫（Tanu）是否被凶星占据"]
- 条件关系：{"fact_key": "一宫（Tanu）是否被凶星占据"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断残疾、伤痕或具体缺陷，原文只说没有好相貌。", "不得据此推断相貌变化的时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：一宫（Tanu）是否被凶星占据。
- 缺失即停字段：["一宫（Tanu）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v4`｜PDF [26]｜“A benefic in Lagn will give a pleasing appearance, while a malefic will make one bereft of good appearance.”


## 四路查书计划

### 支持路

- A benefic in Lagn will give a pleasing appearance, while a malefic will make one bereft of good appearance
- 一宫有凶星 没有好相貌

### 反例或取消路

- A benefic in Lagn will give a pleasing appearance
- Felicity of the body will be enjoyed, if Lagn is drishtied by, or yuti with a benefic

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi

### 判断方法路

- Effects of Tanu Bhava
- Now I will describe to you the effects of moles, marks, spots and signs, found on the body of women and men
- 判断相貌要看一宫里有吉星还是凶星

## 上游问题

- 无

## 停止条件

- 缺少一宫凶星占据事实时停止。
- 凶星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
