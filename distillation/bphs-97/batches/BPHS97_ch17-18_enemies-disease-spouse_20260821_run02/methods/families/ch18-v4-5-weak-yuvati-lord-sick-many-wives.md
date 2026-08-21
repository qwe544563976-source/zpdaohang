---
method: ch18-v4-5-weak-yuvati-lord-sick-many-wives
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 妻多病且多妻：七宫主落陷、燃烧或落敌方行星的星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有多个配偶
- 七宫主落陷或燃烧对婚姻有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘七宫主是哪颗行星

## 按情况检查的事实

- 七宫主（Yuvati's Lord）是否落陷
- 七宫主（Yuvati's Lord）是否燃烧
- 七宫主（Yuvati's Lord）是否落敌方行星主管的星座

## 依赖方法

- 无

## 执行步骤

### ch18-v4-5-weak-yuvati-lord-sick-many-wives.step-001

- 动作：先定出七宫主（Yuvati's Lord）是哪颗行星，再核对它是否落陷、燃烧或落敌方行星主管的星座。
- 适用范围：仅限本命盘七宫（Yuvati）婚姻主题；原文以「wives」立说，属男命框架；原文未给妻子数目与时间。
- 原文最小意思：七宫主落陷、燃烧或落敌方行星主管的星座时，命主会得到多病的妻子与多位妻子。
- 本步骤产出事实：["七宫主失格主妻病多妻判定"]
- 所需事实：["本盘七宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘七宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落陷"}, {"fact_key": "七宫主（Yuvati's Lord）是否燃烧"}, {"fact_key": "七宫主（Yuvati's Lord）是否落敌方行星主管的星座"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘七宫主是哪颗行星"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落陷"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落陷"}, "selection_group": "ch18-v4-5-weak-yuvati-lord-sick-many-wives.step-001:dignity-loss", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落陷。"}, {"when": {"fact_key": "本盘七宫主是哪颗行星"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否燃烧"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否燃烧"}, "selection_group": "ch18-v4-5-weak-yuvati-lord-sick-many-wives.step-001:dignity-loss", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否燃烧。"}, {"when": {"fact_key": "本盘七宫主是哪颗行星"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落敌方行星主管的星座"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落敌方行星主管的星座"}, "selection_group": "ch18-v4-5-weak-yuvati-lord-sick-many-wives.step-001:dignity-loss", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落敌方行星主管的星座。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断具体妻子人数、婚期或离异。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘七宫主是哪颗行星。
- 缺失即停字段：["本盘七宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v4-5`｜PDF [33]｜“Conversely, if Yuvati Lord is in fall, or is combust, or is in an enemy’s Rāśi, one will acquire sick wives and many wives.”


## 四路查书计划

### 支持路

- Yuvati Lord is in fall, or is combust, or is in an enemy’s Rāśi sick wives and many wives
- 七宫主落陷 燃烧 敌方星座 多妻 妻子多病

### 反例或取消路

- Yuvati Lord be endowed with strength be drishtied by a benefic wealthy honourable happy fortunate
- Yuvati Lord is in his own Rāśi, or in exaltation full happiness through his wife

### 适用边界路

- One will have two wives, if Yuvati Lord is in fall, or in a malefic Rashialong with a malefic
- If Mangal and Shukra are in Yuvati, or, if Shani is Yuvati the native will have 3 wives
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- THE 7th LORD fall combust enemy Rāśi effects
- 判断七宫主失格应检查什么

## 上游问题

- 无

## 停止条件

- 缺少七宫主身份事实时停止。
- 落陷、燃烧、落敌方星座三个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
