---
method: ch18-v1-marital-happiness
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 婚姻幸福：七宫主落本星座（own Rāśi，即金星主管的星座）或入旺

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的婚姻幸福吗
- 我能不能通过配偶得到幸福

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘七宫主是哪颗行星

## 按情况检查的事实

- 七宫主（Yuvati's Lord）是否落本星座（own Rāśi）
- 七宫主（Yuvati's Lord）是否入旺

## 依赖方法

- 无

## 执行步骤

### ch18-v1-marital-happiness.step-001

- 动作：先定出七宫主（Yuvati's Lord）是哪颗行星，再核对它是否落本星座（own Rāśi）或入旺。
- 适用范围：仅限本命盘七宫（Yuvati）婚姻主题；原文以「his wife」立说，属男命框架；原文未给婚期或配偶数目。
- 原文最小意思：七宫主落本星座（own Rāśi，即金星主管的星座）或入旺时，命主通过妻子（与婚姻）得到圆满幸福。
- 本步骤产出事实：["七宫主尊贵主婚姻圆满判定"]
- 所需事实：["本盘七宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘七宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落本星座（own Rāśi）"}, {"fact_key": "七宫主（Yuvati's Lord）是否入旺"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘七宫主是哪颗行星"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落本星座（own Rāśi）"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落本星座（own Rāśi）"}, "selection_group": "ch18-v1-marital-happiness.step-001:dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落本星座（own Rāśi）。"}, {"when": {"fact_key": "本盘七宫主是哪颗行星"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否入旺"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否入旺"}, "selection_group": "ch18-v1-marital-happiness.step-001:dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断结婚时间、配偶人数或子女。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘七宫主是哪颗行星。
- 缺失即停字段：["本盘七宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v1`｜PDF [33]｜“If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage).”


## 四路查书计划

### 支持路

- Yuvati Lord is in his own Rāśi, or in exaltation full happiness through his wife
- 七宫主落本星座（own Rāśi，即金星主管的星座） 入旺 婚姻圆满幸福

### 反例或取消路

- Chandra is in Yuvati, Yuvati Lord is in Vyaya Karaka bereft of strength not endowed with marital happiness
- Yuvati Lord be in Ari, 8th, or Vyaya the wife will be sickly

### 适用边界路

- This however does not apply to own Bhava, or exaltation placement, as above
- Yuvati Lord is devoid of strength and is relegated to Ari, 8th, or Vyaya loss of spouse
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- effects of the 7th Bhava Yuvati Lord placement
- 判断七宫（Yuvati）婚姻应检查什么

## 上游问题

- 无

## 停止条件

- 缺少七宫主身份事实时停止。
- 七宫主落本星座（own Rāśi，即金星主管的星座）与入旺两个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
