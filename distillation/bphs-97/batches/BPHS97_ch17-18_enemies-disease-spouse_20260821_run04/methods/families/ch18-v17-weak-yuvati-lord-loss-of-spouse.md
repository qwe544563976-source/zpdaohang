---
method: ch18-v17-weak-yuvati-lord-loss-of-spouse
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 失去妻子：七宫主无力并被贬落六宫、八宫或十二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我妻子会不会早早去世
- 七宫主无力又落凶宫对配偶意味着什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘七宫主落在哪一宫
- 七宫主（Yuvati's Lord）是否有力

## 按情况检查的事实

- 七宫主（Yuvati's Lord）是否落六宫（Ari）
- 七宫主（Yuvati's Lord）是否落八宫（Randhr）
- 七宫主（Yuvati's Lord）是否落十二宫（Vyaya）

## 依赖方法

- 无

## 执行步骤

### ch18-v17-weak-yuvati-lord-loss-of-spouse.step-001

- 动作：先核对七宫主（Yuvati's Lord）是否无力，再核对它被贬落的是六宫、八宫还是十二宫。
- 适用范围：仅限本命盘七宫（Yuvati）配偶存殁主题；原文以「the native’s wife」立说，属男命框架；括号内「i.e. she will die early」是译本的解释性夹注，原文断语为 will be destroyed；原文只说 devoid of strength，未给强弱判准。
- 原文最小意思：七宫主无力并被贬落六宫、八宫或十二宫时，命主的妻子将被毁灭，即她会早早去世。
- 本步骤产出事实：["七宫主无力落凶宫主失妻判定"]
- 所需事实：["本盘七宫主落在哪一宫", "七宫主（Yuvati's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘七宫主落在哪一宫"}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否有力"}]}]}, {"operator": "OR", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落六宫（Ari）"}, {"fact_key": "七宫主（Yuvati's Lord）是否落八宫（Randhr）"}, {"fact_key": "七宫主（Yuvati's Lord）是否落十二宫（Vyaya）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫主落在哪一宫"}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否有力"}]}]}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落六宫（Ari）"}, "selection_group": "ch18-v17-weak-yuvati-lord-loss-of-spouse.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫主落在哪一宫"}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否有力"}]}]}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落八宫（Randhr）"}, "selection_group": "ch18-v17-weak-yuvati-lord-loss-of-spouse.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落八宫（Randhr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫主落在哪一宫"}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否有力"}]}]}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落十二宫（Vyaya）"}, "selection_group": "ch18-v17-weak-yuvati-lord-loss-of-spouse.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落十二宫（Vyaya）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断妻子去世的具体年龄、死因或命主是否再婚。", "不得自行发明「无力」的判准。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘七宫主落在哪一宫、七宫主（Yuvati's Lord）是否有力。
- 缺失即停字段：["本盘七宫主落在哪一宫", "七宫主（Yuvati's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v17`｜PDF [34]｜“If Yuvati Lord is devoid of strength and is relegated to Ari, 8<sup>th</sup> , or Vyaya”
  - `bphs-97:santhanam:ch18:v17`｜PDF [34]｜“the native’s wife will be destroyed (i.e. she will die early).”


## 四路查书计划

### 支持路

- If Yuvati Lord is devoid of strength and is relegated to Ari, 8th, or Vyaya the native’s wife will be destroyed
- 七宫主无力 落六宫 八宫 十二宫 失去妻子

### 反例或取消路

- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife

### 适用边界路

- Should Yuvati Lord be in Ari, 8th, or Vyaya, the wife will be sickly This however does not apply to own Bhava, or exaltation placement
- TIMING OF WIFE’S DEATH Loss of wife will occur in the 18th year, or 33rd year of age of the native
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- 判断配偶存殁要看七宫主的强弱与落宫

## 上游问题

- 无

## 停止条件

- 缺少七宫主落宫事实时停止。
- 缺少七宫主强弱事实时停止（该判准待排盘窗口定义）。
- 六宫、八宫、十二宫三个落宫分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
