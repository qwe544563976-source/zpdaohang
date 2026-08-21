---
method: ch18-v7-8-5-shani-rahu-ketu-base-females
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 交往卑贱女性与已行经女性：土星、罗睺或计都落七宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 土星或罗睺计都落七宫说明我会和什么样的人来往
- 我的交往对象是什么阶层

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘七宫（Yuvati）内有哪些行星

## 按情况检查的事实

- 土星（Shani）是否落七宫（Yuvati）
- 罗睺（Rahu）是否落七宫（Yuvati）
- 计都（Ketu）是否落七宫（Yuvati）

## 依赖方法

- 无

## 执行步骤

### ch18-v7-8-5-shani-rahu-ketu-base-females.step-001

- 动作：取出七宫（Yuvati）内的行星，核对其中是否有土星（Shani）、罗睺（Rahu）或计都（Ketu）。
- 适用范围：仅限本命盘七宫（Yuvati）交往对象主题；原文以命主与女性交往立说，属男命框架；原文未给时间。
- 原文最小意思：土星、罗睺或计都落七宫时，命主交往的是卑贱女性以及已行经的女性。
- 本步骤产出事实：["土星罗睺计都落七宫主交往对象判定"]
- 所需事实：["本盘七宫（Yuvati）内有哪些行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, {"operator": "OR", "operands": [{"fact_key": "土星（Shani）是否落七宫（Yuvati）"}, {"fact_key": "罗睺（Rahu）是否落七宫（Yuvati）"}, {"fact_key": "计都（Ketu）是否落七宫（Yuvati）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, "required_fact_keys": ["土星（Shani）是否落七宫（Yuvati）"], "branch_condition_logic": {"fact_key": "土星（Shani）是否落七宫（Yuvati）"}, "selection_group": "ch18-v7-8-5-shani-rahu-ketu-base-females.step-001:occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：土星（Shani）是否落七宫（Yuvati）。"}, {"when": {"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, "required_fact_keys": ["罗睺（Rahu）是否落七宫（Yuvati）"], "branch_condition_logic": {"fact_key": "罗睺（Rahu）是否落七宫（Yuvati）"}, "selection_group": "ch18-v7-8-5-shani-rahu-ketu-base-females.step-001:occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：罗睺（Rahu）是否落七宫（Yuvati）。"}, {"when": {"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, "required_fact_keys": ["计都（Ketu）是否落七宫（Yuvati）"], "branch_condition_logic": {"fact_key": "计都（Ketu）是否落七宫（Yuvati）"}, "selection_group": "ch18-v7-8-5-shani-rahu-ketu-base-females.step-001:occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：计都（Ketu）是否落七宫（Yuvati）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断婚姻成立与否、婚期或配偶人数。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘七宫（Yuvati）内有哪些行星。
- 缺失即停字段：["本盘七宫（Yuvati）内有哪些行星"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v7-8.5`｜PDF [33, 34]｜“Base females and females, having attained their courses, are denoted by Shani, Rahu/Ketu in Yuvati.”


## 四路查书计划

### 支持路

- Base females and females, having attained their courses, are denoted by Shani, Rahu/Ketu in Yuvati
- 土星 罗睺 计都 落七宫 卑贱女性

### 反例或取消路

- The native will beget a spouse endowed with (the seven principal) virtues who will expand his dynasty
- Wife of a Brahmin, or a pregnant female will be in the native’s association, if Guru is in Yuvati

### 适用边界路

- Shani indicates sick and weak spouse
- If Yuvati Bhava is occupied, or owned by Shani/Mangal, the native will beget a harlot, as his spouse
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- 判断七宫（Yuvati）内的行星应检查什么

## 上游问题

- 无

## 停止条件

- 缺少七宫内行星事实时停止。
- 土星、罗睺、计都三个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
