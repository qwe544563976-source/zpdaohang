---
method: ch18-v7-8-5-chandra-rasi-female
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 交往女性与七宫星座相应：月亮落七宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮落七宫说明我会和什么样的人来往
- 我配偶或交往对象是什么类型

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否落七宫（Yuvati）
- 本盘七宫（Yuvati）落在哪个星座

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v7-8-5-chandra-rasi-female.step-001

- 动作：核对月亮（Chandra）是否落七宫（Yuvati），并取七宫所落星座。
- 适用范围：仅限本命盘七宫（Yuvati）交往对象主题；「therein」承接同偈前句的落七宫框架；原文以命主与女性交往立说，属男命框架；原文只说与星座相应，未给具体女性特征。
- 原文最小意思：月亮落七宫时，命主交往的女性与七宫（Yuvati）所落星座相应。
- 本步骤产出事实：["月亮落七宫主交往对象随星座判定"]
- 所需事实：["月亮（Chandra）是否落七宫（Yuvati）", "本盘七宫（Yuvati）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落七宫（Yuvati）"}, {"fact_key": "本盘七宫（Yuvati）落在哪个星座"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文补出各星座对应的具体女性特征。", "不得据此推断婚期或婚姻成立与否。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否落七宫（Yuvati）、本盘七宫（Yuvati）落在哪个星座。
- 缺失即停字段：["月亮（Chandra）是否落七宫（Yuvati）", "本盘七宫（Yuvati）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v7-8.5`｜PDF [33, 34]｜“Chandra therein will cause association with such female, as corresponding to the Rāśi, becoming Yuvati.”


## 四路查书计划

### 支持路

- Chandra therein will cause association with such female, as corresponding to the Rāśi, becoming Yuvati
- 月亮落七宫 交往女性 与七宫星座相应

### 反例或取消路

- Shani indicates sick and weak spouse
- Base females and females, having attained their courses, are denoted by Shani, Rahu/Ketu in Yuvati

### 适用边界路

- The Rāśi, becoming Ari Bhava, will lead to the knowledge of the concerned limb
- MlSCELLANEOUS MATTERS Yuvati Rāśi becoming Yuvati
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- effects of Grahas placed in Yuvati Bhava
- 判断七宫（Yuvati）所落星座应检查什么

## 上游问题

- 无

## 停止条件

- 缺少月亮落宫事实时停止。
- 缺少七宫所落星座事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
