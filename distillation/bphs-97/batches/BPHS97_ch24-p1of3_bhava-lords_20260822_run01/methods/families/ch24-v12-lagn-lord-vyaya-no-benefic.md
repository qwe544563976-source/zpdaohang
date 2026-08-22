---
method: ch24-v12-lagn-lord-vyaya-no-benefic
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 身体不快、花费无果与易怒：上升主落十二宫（Vyaya）且得不到吉星相照或吉星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我为什么总是钱花了没结果
- 上升主落十二宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否落十二宫（Vyaya）

## 按情况检查的事实

- 上升主（Lagn's Lord）是否被吉星相照
- 上升主（Lagn's Lord）是否与吉星同宫

## 依赖方法

- 无

## 执行步骤

### ch24-v12-lagn-lord-vyaya-no-benefic.step-001

- 动作：先核对上升主（Lagn's Lord）是否落十二宫（Vyaya），再核对它是否得不到吉星相照、是否得不到吉星同宫。
- 适用范围：仅限本命盘上升主（Lagn's Lord）落宫主题；原文把吉星的相照与同宫并列写作 and/or，本步按并列择一拆成两个分支；吉星名册以本书 ch03:v11 的界定为准；原文未给花费数额、疾病内容或时间限定。
- 原文最小意思：上升主（Lagn's Lord）落十二宫（Vyaya），并且得不到吉星相照，或得不到吉星同宫时，命主没有身体上的快乐、花费没有成果，并且很爱发怒。
- 本步骤产出事实：["上升主落十二宫无吉星支持的身体快乐与花费判定"]
- 所需事实：["上升主（Lagn's Lord）是否落十二宫（Vyaya）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落十二宫（Vyaya）"}, {"operator": "OR", "operands": [{"operator": "NOT", "operands": [{"fact_key": "上升主（Lagn's Lord）是否被吉星相照"}]}, {"operator": "NOT", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与吉星同宫"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "上升主（Lagn's Lord）是否落十二宫（Vyaya）"}, "required_fact_keys": ["上升主（Lagn's Lord）是否被吉星相照"], "branch_condition_logic": {"operator": "NOT", "operands": [{"fact_key": "上升主（Lagn's Lord）是否被吉星相照"}]}, "selection_group": "ch24-v12-lagn-lord-vyaya-no-benefic.step-001:no-benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否被吉星相照。"}, {"when": {"fact_key": "上升主（Lagn's Lord）是否落十二宫（Vyaya）"}, "required_fact_keys": ["上升主（Lagn's Lord）是否与吉星同宫"], "branch_condition_logic": {"operator": "NOT", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与吉星同宫"}]}, "selection_group": "ch24-v12-lagn-lord-vyaya-no-benefic.step-001:no-benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否与吉星同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断花费金额、疾病名称或发生时间。", "不得把「没有身体上的快乐」扩大成短寿或重病。", "不得把原文的吉星换成凶星来套用本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否落十二宫（Vyaya）。
- 缺失即停字段：["上升主（Lagn's Lord）是否落十二宫（Vyaya）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v12`｜PDF [41]｜“If Lagn’s Lord is in Vyaya Bhava and is devoid of benefic Drishti and/or Yuti, the native will be bereft of physical happiness, will spend unfruitfully and be given to much anger.”


## 四路查书计划

### 支持路

- If Lagn’s Lord is in Vyaya Bhava and is devoid of benefic Drishti and/or Yuti, the native will be bereft of physical happiness, will spend unfruitfully and be given to much anger.
- 上升主落十二宫 没有吉星相照 花费无果 易怒

### 反例或取消路

- Should Lagn’s Lord be in Lagn itself, the native will be endowed with physical happiness and prowess
- There will be expenses on good accounts, if Vyaya’s Lord is with a benefic, or in his own Bhava, or exalted
- If Lagn’s Lord is in Ari Bhava and related to a malefic the native will be devoid of physical happiness and will be troubled by enemies, if there is no benefic Drishti

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.

### 判断方法路

- Effects of Lagn’s Lord in Various Bhavas (up to Sloka 12)
- 判断上升主落十二宫时要核对有没有吉星相照或同宫

## 上游问题

- 无

## 停止条件

- 缺少上升主是否落十二宫（Vyaya）的事实时停止。
- 吉星名册未确定时，两个吉星关系分支停止。
- 上升主的吉星相照与吉星同宫两项事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
