---
method: ch24-v19-malefic-related-wife-character
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 妻子品行受质疑：二宫主落七宫（Yuvati）且凶星与该配置发生关系

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我妻子的名声会不会有问题
- 二宫主落七宫又被凶星影响会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫主（Dhan's Lord）是否落七宫（Yuvati）

## 按情况检查的事实

- 二宫主（Dhan's Lord）是否与凶星同宫
- 二宫主（Dhan's Lord）是否被凶星相照

## 依赖方法

- 无

## 执行步骤

### ch24-v19-malefic-related-wife-character.step-001

- 动作：先核对二宫主（Dhan's Lord）是否落七宫（Yuvati），再核对是否有凶星以与二宫主同宫，或以相照的方式与该配置发生关系。
- 适用范围：仅限本命盘二宫主（Dhan's Lord）落宫主题；the said placement 承同偈前句的「二宫主落七宫（Yuvati）」；原文把凶星与该配置的关系明写成两种（与二宫主同宫、相照），本步照此拆成两个并列分支；第二种原文只写 by Drishti，未写明相照的落点是二宫主本身还是它所落的七宫，本步按相照二宫主写入事实名；原文以 the native’s wife 立说，属男命框架；凶星名册以本书 ch03:v11 的界定为准；原文未给时间限定。
- 原文最小意思：承同偈「二宫主（Dhan's Lord）落七宫（Yuvati）」的配置，若有凶星与二宫主同宫，或以相照的方式与该配置发生关系，命主的妻子品行会受到质疑。
- 本步骤产出事实：["二宫主落七宫遇凶星的配偶品行判定"]
- 所需事实：["二宫主（Dhan's Lord）是否落七宫（Yuvati）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落七宫（Yuvati）"}, {"operator": "OR", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否与凶星同宫"}, {"fact_key": "二宫主（Dhan's Lord）是否被凶星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "二宫主（Dhan's Lord）是否落七宫（Yuvati）"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否与凶星同宫"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否与凶星同宫"}, "selection_group": "ch24-v19-malefic-related-wife-character.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否与凶星同宫。"}, {"when": {"fact_key": "二宫主（Dhan's Lord）是否落七宫（Yuvati）"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否被凶星相照"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否被凶星相照"}, "selection_group": "ch24-v19-malefic-related-wife-character.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否被凶星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「品行受到质疑」写成已经出轨的事实断语。", "不得据此推断离婚、婚期或妻子人数。", "不得在原文写明的同宫与相照两种关系之外，另加别的关系类型。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫主（Dhan's Lord）是否落七宫（Yuvati）。
- 缺失即停字段：["二宫主（Dhan's Lord）是否落七宫（Yuvati）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v19`｜PDF [42]｜“If Dhan’s Lord is in Yuvati Bhava, the native will be addicted to others’ wives and he will be a doctor. If a malefic is related to the said placement by yuti with Dhan’s Lord, or by Drishti, the native’s wife will be of questionable character.”


## 四路查书计划

### 支持路

- If a malefic is related to the said placement by yuti with Dhan’s Lord, or by Drishti, the native’s wife will be of questionable character
- 二宫主落七宫 凶星同宫 相照 妻子品行

### 反例或取消路

- If Dharm’s Lord is in Dhan Bhava, the native will be a scholar, be dear to all, wealthy, sensuous and endowed with happiness from wife, sons etc.
- The native will beget a spouse endowed with (the seven principal) virtues

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Yuvati Bhava. Wife, travel, trade, loss of sight, death etc. be known from Yuvati Bhava
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- Effects of Dhan’s Lord in Various Bhavas (up to Sloka 24)
- 判断配偶品行要核对七宫与哪些凶星关系

## 上游问题

- 无

## 停止条件

- 缺少二宫主是否落七宫（Yuvati）的事实时停止。
- 凶星名册未确定时，两个凶星关系分支停止。
- 二宫主与凶星同宫、被凶星相照两项事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
