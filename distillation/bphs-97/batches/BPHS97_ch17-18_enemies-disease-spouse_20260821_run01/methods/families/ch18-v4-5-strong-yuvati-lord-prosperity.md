---
method: ch18-v4-5-strong-yuvati-lord-prosperity
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 富有有荣誉：七宫主有力且与吉星同宫或受吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子会不会富有体面
- 七宫主有力对我意味着什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 七宫主（Yuvati's Lord）是否有力

## 按情况检查的事实

- 七宫主（Yuvati's Lord）是否与吉星同宫
- 七宫主（Yuvati's Lord）是否被吉星相照

## 依赖方法

- 无

## 执行步骤

### ch18-v4-5-strong-yuvati-lord-prosperity.step-001

- 动作：核对七宫主（Yuvati's Lord）是否有力，并核对它与吉星是同宫还是受吉星相照。
- 适用范围：仅限本命盘七宫（Yuvati）主星强弱主题；原文只说 endowed with strength，未给判准；原文未给时间。
- 原文最小意思：七宫主有力，并与吉星同宫或受吉星相照时，命主富有、有荣誉、幸福且幸运。
- 本步骤产出事实：["七宫主有力得吉主富贵判定"]
- 所需事实：["七宫主（Yuvati's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否有力"}, {"operator": "OR", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否与吉星同宫"}, {"fact_key": "七宫主（Yuvati's Lord）是否被吉星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "七宫主（Yuvati's Lord）是否有力"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否与吉星同宫"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否与吉星同宫"}, "selection_group": "ch18-v4-5-strong-yuvati-lord-prosperity.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否与吉星同宫。"}, {"when": {"fact_key": "七宫主（Yuvati's Lord）是否有力"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否被吉星相照"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否被吉星相照"}, "selection_group": "ch18-v4-5-strong-yuvati-lord-prosperity.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否被吉星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、职位或应期。", "不得自行发明「有力」的判准。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：七宫主（Yuvati's Lord）是否有力。
- 缺失即停字段：["七宫主（Yuvati's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v4-5`｜PDF [33]｜“Should Yuvati Lord be endowed with strength and be yuti with, or be drishtied by a benefic, the native will be wealthy, honourable, happy and fortunate.”


## 四路查书计划

### 支持路

- Yuvati Lord be endowed with strength be yuti with, or be drishtied by a benefic wealthy honourable happy fortunate
- 七宫主有力 与吉星同宫 受吉星相照 富有

### 反例或取消路

- Conversely, if Yuvati Lord is in fall, or is combust, or is in an enemy’s Rāśi sick wives and many wives
- If Yuvati Bhava, or its Lord is yuti with a malefic the native’s wife will incur evils

### 适用边界路

- Yuvati Bhava, or its Lord is bereft of strength
- Yuvati Lord is devoid of strength and is relegated to Ari, 8th, or Vyaya

### 判断方法路

- THE 7th LORD effects strength benefic drishti
- 判断七宫主强弱应检查什么

## 上游问题

- 无

## 停止条件

- 缺少七宫主强弱事实时停止（该事实的判准待排盘窗口定义）。
- 与吉星同宫、受吉星相照两个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
