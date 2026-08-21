---
method: ch18-v16-evils-to-spouse
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 妻子遭灾：七宫或其宫主与凶星同宫，无力时尤甚

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我配偶会不会遇到灾祸
- 七宫逢凶星对配偶有多大影响

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

- 七宫（Yuvati）是否被凶星占据
- 七宫主（Yuvati's Lord）是否与凶星同宫
- 七宫（Yuvati）是否有力
- 七宫主（Yuvati's Lord）是否有力

## 依赖方法

- 无

## 执行步骤

### ch18-v16-evils-to-spouse.step-001

- 动作：取出七宫（Yuvati）内的行星与七宫主身份，核对是七宫被凶星占据还是七宫主与凶星同宫。
- 适用范围：仅限本命盘七宫（Yuvati）配偶灾厄主题；原文以「the native’s wife」立说，属男命框架；原文未给灾厄种类与时间。
- 原文最小意思：七宫被凶星占据或其宫主与凶星同宫时，妻子遭遇灾厄。
- 本步骤产出事实：["七宫逢凶主妻遭灾判定"]
- 所需事实：["本盘七宫（Yuvati）内有哪些行星", "本盘七宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, {"fact_key": "本盘七宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "七宫（Yuvati）是否被凶星占据"}, {"fact_key": "七宫主（Yuvati's Lord）是否与凶星同宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, {"fact_key": "本盘七宫主是哪颗行星"}]}, "required_fact_keys": ["七宫（Yuvati）是否被凶星占据"], "branch_condition_logic": {"fact_key": "七宫（Yuvati）是否被凶星占据"}, "selection_group": "ch18-v16-evils-to-spouse.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫（Yuvati）是否被凶星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫（Yuvati）内有哪些行星"}, {"fact_key": "本盘七宫主是哪颗行星"}]}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否与凶星同宫"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否与凶星同宫"}, "selection_group": "ch18-v16-evils-to-spouse.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否与凶星同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断灾厄的种类、轻重或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘七宫（Yuvati）内有哪些行星、本盘七宫主是哪颗行星。
- 缺失即停字段：["本盘七宫（Yuvati）内有哪些行星", "本盘七宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v16`｜PDF [34]｜“If Yuvati Bhava, or its Lord is yuti with a malefic the native’s wife will incur evils”

### ch18-v16-evils-to-spouse.step-002

- 动作：在上一步成立的基础上，核对七宫（Yuvati）或其宫主是否无力。
- 适用范围：仅限上一步已成立的配偶灾厄判定；原文只说 bereft of strength，未给有力的判准。
- 原文最小意思：在上一步成立的基础上，七宫或其宫主无力时，妻子所遭灾厄尤甚。
- 本步骤产出事实：["七宫逢凶无力主妻遭灾加重判定"]
- 所需事实：["七宫逢凶主妻遭灾判定"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "七宫逢凶主妻遭灾判定"}, {"operator": "OR", "operands": [{"operator": "NOT", "operands": [{"fact_key": "七宫（Yuvati）是否有力"}]}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否有力"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "七宫逢凶主妻遭灾判定"}, "required_fact_keys": ["七宫（Yuvati）是否有力"], "branch_condition_logic": {"operator": "NOT", "operands": [{"fact_key": "七宫（Yuvati）是否有力"}]}, "selection_group": "ch18-v16-evils-to-spouse.step-002:weakness", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫（Yuvati）是否有力。"}, {"when": {"fact_key": "七宫逢凶主妻遭灾判定"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否有力"], "branch_condition_logic": {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否有力"}]}, "selection_group": "ch18-v16-evils-to-spouse.step-002:weakness", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否有力。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自行发明「无力」的判准。", "不得据此推断配偶死亡或离异。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：七宫逢凶主妻遭灾判定。
- 缺失即停字段：["七宫逢凶主妻遭灾判定"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v16`｜PDF [34]｜“the native’s wife will incur evils, especially, if Yuvati Bhava, or its Lord is bereft of strength.”


## 四路查书计划

### 支持路

- If Yuvati Bhava, or its Lord is yuti with a malefic the native’s wife will incur evils
- 七宫与凶星同宫 七宫主与凶星同宫 妻子遭灾

### 反例或取消路

- Yuvati Lord is in his own Rāśi, or in exaltation full happiness through his wife
- The native will beget a spouse endowed with (the seven principal) virtues 7th Lord is exalted

### 适用边界路

- Yuvati Lord is devoid of strength and is relegated to Ari, 8th, or Vyaya the native’s wife will be destroyed
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- 判断配偶灾厄应检查什么

## 上游问题

- 无

## 停止条件

- 缺少七宫内行星或七宫主身份事实时停止。
- 七宫逢凶与七宫主逢凶两个分支事实都缺时停止。
- 缺少七宫或七宫主的强弱事实时第二步停止（该判准待排盘窗口定义）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
