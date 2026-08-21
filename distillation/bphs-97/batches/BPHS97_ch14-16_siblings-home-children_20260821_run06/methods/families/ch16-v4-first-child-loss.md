---
method: ch16-v4-first-child-loss
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 长子去世：五宫主落六宫且上升主与火星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的第一个孩子会不会有事
- 我还能不能再生

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫主是否落在第六宫（Ari Bhava）
- 上升主是否与火星（Mangal）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch16-v4-first-child-loss.step-001

- 动作：核对五宫主是否落第六宫，同时核对上升主是否与火星同宫。
- 适用范围：仅限本命盘五宫子女主题；原文只给这一组条件，未给孩子出生或去世的年份。
- 原文最小意思：五宫主落六宫、且上升主与火星（Mangal）同宫时，会失去第一个孩子。
- 本步骤产出事实：["第一个孩子去世判定"]
- 所需事实：["五宫主是否落在第六宫（Ari Bhava）", "上升主是否与火星（Mangal）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫主是否落在第六宫（Ari Bhava）"}, {"fact_key": "上升主是否与火星（Mangal）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断去世发生的年龄或年份。", "不得把这条断语扩大到第一个之外的其他子女。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否落在第六宫（Ari Bhava）、上升主是否与火星（Mangal）同宫。
- 缺失即停字段：["五宫主是否落在第六宫（Ari Bhava）", "上升主是否与火星（Mangal）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v4`｜PDF [30]｜“If Putr’s Lord is in Ari Bhava, as Lagn’s Lord is yuti with Mangal, the native will lose his very first child, whereafter his female will not be fertile to yield an offspring.”

### ch16-v4-first-child-loss.step-002

- 动作：在已判定第一个孩子去世的前提下，按原文接续判断此后的生育。
- 适用范围：仅限本命盘五宫子女主题；原文只说此后不再生育，未给时间跨度或医学解释。
- 原文最小意思：五宫主落六宫、上升主与火星（Mangal）同宫而失去第一个孩子之后，其女子不再能生育。
- 本步骤产出事实：["长子去世后不再生育判定"]
- 所需事实：["第一个孩子去世判定"]
- 条件关系：{"fact_key": "第一个孩子去世判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把不再生育解释成疾病诊断或医学结论。", "不得据此推断配偶更换后的生育情况。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：第一个孩子去世判定。
- 缺失即停字段：["第一个孩子去世判定"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v4`｜PDF [30]｜“If Putr’s Lord is in Ari Bhava, as Lagn’s Lord is yuti with Mangal, the native will lose his very first child, whereafter his female will not be fertile to yield an offspring.”


## 四路查书计划

### 支持路

- 五宫主落六宫 上升主与火星同宫 失去长子

### 反例或取消路

- 五宫得力 多子 反例

### 适用边界路

- 长子去世断语的适用边界

### 判断方法路

- 怎样查上升主与火星是否同宫

## 上游问题

- 无

## 停止条件

- 缺少五宫主落宫事实时停止。
- 缺少上升主与火星是否同宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
