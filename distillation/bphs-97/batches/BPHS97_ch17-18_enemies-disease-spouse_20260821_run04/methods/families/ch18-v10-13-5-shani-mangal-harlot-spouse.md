---
method: ch18-v10-13-5-shani-mangal-harlot-spouse
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 娶妓女为配偶或与他人非法私通：七宫被土星或火星占据或主管

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的配偶会是什么样的人
- 我会不会有非法私通的事

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘七宫（Yuvati）内有哪些行星
- 本盘七宫主是哪颗行星

## 按情况检查的事实

- 土星（Shani）是否落七宫（Yuvati）
- 火星（Mangal）是否落七宫（Yuvati）
- 七宫主（Yuvati's Lord）是否为土星（Shani）
- 七宫主（Yuvati's Lord）是否为火星（Mangal）

## 依赖方法

- 无

## 执行步骤

### ch18-v10-13-5-shani-mangal-harlot-spouse.step-001

- 动作：取出七宫（Yuvati）内的行星与七宫主身份，核对土星（Shani）或火星（Mangal）是占据七宫还是主管七宫。
- 适用范围：仅限本命盘七宫（Yuvati）配偶与私通主题；原文以「his spouse」立说，属男命框架；原文未给时间。
- 原文最小意思：七宫被土星或火星占据、或由土星或火星主管时，命主会娶妓女为配偶，或与他人非法私通。
- 本步骤产出事实：["七宫逢土火主配偶为妓或私通判定"]
- 所需事实：["本盘七宫（Yuvati）内有哪些行星", "本盘七宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, {"fact_key": "本盘七宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "土星（Shani）是否落七宫（Yuvati）"}, {"fact_key": "火星（Mangal）是否落七宫（Yuvati）"}, {"fact_key": "七宫主（Yuvati's Lord）是否为土星（Shani）"}, {"fact_key": "七宫主（Yuvati's Lord）是否为火星（Mangal）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, {"fact_key": "本盘七宫主是哪颗行星"}]}, "required_fact_keys": ["土星（Shani）是否落七宫（Yuvati）"], "branch_condition_logic": {"fact_key": "土星（Shani）是否落七宫（Yuvati）"}, "selection_group": "ch18-v10-13-5-shani-mangal-harlot-spouse.step-001:shani-mangal-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：土星（Shani）是否落七宫（Yuvati）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, {"fact_key": "本盘七宫主是哪颗行星"}]}, "required_fact_keys": ["火星（Mangal）是否落七宫（Yuvati）"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否落七宫（Yuvati）"}, "selection_group": "ch18-v10-13-5-shani-mangal-harlot-spouse.step-001:shani-mangal-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否落七宫（Yuvati）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, {"fact_key": "本盘七宫主是哪颗行星"}]}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否为土星（Shani）"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否为土星（Shani）"}, "selection_group": "ch18-v10-13-5-shani-mangal-harlot-spouse.step-001:shani-mangal-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否为土星（Shani）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, {"fact_key": "本盘七宫主是哪颗行星"}]}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否为火星（Mangal）"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否为火星（Mangal）"}, "selection_group": "ch18-v10-13-5-shani-mangal-harlot-spouse.step-001:shani-mangal-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否为火星（Mangal）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自行判定两种结果取哪一种，原文没给判准。", "不得据此推断婚期、配偶人数或离异。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘七宫（Yuvati）内有哪些行星、本盘七宫主是哪颗行星。
- 缺失即停字段：["本盘七宫（Yuvati）内有哪些行星", "本盘七宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v10-13.5`｜PDF [34]｜“If Yuvati Bhava is occupied, or owned by Shani/Mangal, the native will beget a harlot, as his spouse, or he will be attached to other illegally.”


## 四路查书计划

### 支持路

- If Yuvati Bhava is occupied, or owned by Shani/Mangal, the native will beget a harlot, as his spouse
- 七宫被土星火星占据 主管 妓女配偶 非法私通

### 反例或取消路

- Yuvati Lord is in his own Rāśi, or in exaltation full happiness through his wife

### 适用边界路

- Budh indicates harlots, mean females and females, belonging to traders’ community
- Base females and females, having attained their courses, are denoted by Shani, Rahu/Ketu in Yuvati
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- effects of Yuvati Bhava occupied or owned by Shani Mangal
- 判断七宫（Yuvati）的占据与主管应检查什么

## 上游问题

- 无

## 停止条件

- 缺少七宫内行星或七宫主身份事实时停止。
- 占据与主管四个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
