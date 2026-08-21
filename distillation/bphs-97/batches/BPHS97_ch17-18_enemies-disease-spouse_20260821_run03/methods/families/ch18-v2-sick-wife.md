---
method: ch18-v2-sick-wife
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 妻子多病：七宫主落六宫、八宫或十二宫（落本宫或入旺时不适用）

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我配偶的身体健康吗
- 我妻子会不会常年生病

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘七宫主落在哪一宫
- 七宫主（Yuvati's Lord）是否落本宫
- 七宫主（Yuvati's Lord）是否入旺

## 按情况检查的事实

- 七宫主（Yuvati's Lord）是否落六宫（Ari）
- 七宫主（Yuvati's Lord）是否落八宫（Randhr）
- 七宫主（Yuvati's Lord）是否落十二宫（Vyaya）

## 依赖方法

- 无

## 执行步骤

### ch18-v2-sick-wife.step-001

- 动作：核对七宫主（Yuvati's Lord）落在哪一宫，并先排除它落本宫或入旺的情形。
- 适用范围：仅限本命盘七宫（Yuvati）配偶健康主题；原文以「the wife」立说，属男命框架；原文未给发病时间。
- 原文最小意思：七宫主落六宫、八宫或十二宫时妻子多病；但七宫主落本宫或入旺时不适用。
- 本步骤产出事实：["七宫主落凶宫主妻多病判定"]
- 所需事实：["本盘七宫主落在哪一宫", "七宫主（Yuvati's Lord）是否落本宫", "七宫主（Yuvati's Lord）是否入旺"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘七宫主落在哪一宫"}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落本宫"}]}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否入旺"}]}]}, {"operator": "OR", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落六宫（Ari）"}, {"fact_key": "七宫主（Yuvati's Lord）是否落八宫（Randhr）"}, {"fact_key": "七宫主（Yuvati's Lord）是否落十二宫（Vyaya）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫主落在哪一宫"}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落本宫"}]}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否入旺"}]}]}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落六宫（Ari）"}, "selection_group": "ch18-v2-sick-wife.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫主落在哪一宫"}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落本宫"}]}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否入旺"}]}]}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落八宫（Randhr）"}, "selection_group": "ch18-v2-sick-wife.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落八宫（Randhr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘七宫主落在哪一宫"}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落本宫"}]}, {"operator": "NOT", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否入旺"}]}]}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落十二宫（Vyaya）"}, "selection_group": "ch18-v2-sick-wife.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落十二宫（Vyaya）。"}]
- 例外、取消或缓解：[{"type": "exception", "evidence_atom_ids": ["bphs-97:santhanam:ch18:v2", "bphs-97:santhanam:ch18:v1"], "condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落本宫"}}, {"type": "exception", "evidence_atom_ids": ["bphs-97:santhanam:ch18:v2", "bphs-97:santhanam:ch18:v1"], "condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否入旺"}}]
- 禁止扩大：["不得据此推断病名、病程或配偶寿命。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘七宫主落在哪一宫、七宫主（Yuvati's Lord）是否落本宫、七宫主（Yuvati's Lord）是否入旺。
- 缺失即停字段：["本盘七宫主落在哪一宫", "七宫主（Yuvati's Lord）是否落本宫", "七宫主（Yuvati's Lord）是否入旺"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v2`｜PDF [33]｜“Should Yuvati Lord be in Ari, 8<sup>th</sup> , or Vyaya, the wife will be sickly. This however does not apply to own Bhava, or exaltation placement, as above.”


## 四路查书计划

### 支持路

- Should Yuvati Lord be in Ari, 8th, or Vyaya, the wife will be sickly
- 七宫主落六宫 八宫 十二宫 妻子多病

### 反例或取消路

- Yuvati Lord is in his own Rāśi, or in exaltation full happiness through his wife
- Yuvati Lord be endowed with strength drishtied by a benefic wealthy honourable happy

### 适用边界路

- This however does not apply to own Bhava, or exaltation placement, as above
- Yuvati Lord is devoid of strength and is relegated to Ari, 8th, or Vyaya the native’s wife will be destroyed
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- effects of the 7th Bhava Yuvati Lord placement sick wife
- 判断七宫（Yuvati）配偶健康应检查什么

## 上游问题

- 无

## 停止条件

- 缺少七宫主落宫事实时停止。
- 缺少七宫主落本宫或入旺的排除事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
