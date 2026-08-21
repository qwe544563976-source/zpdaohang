---
method: ch23-v13-shani-mangal-in-vyaya-sinful-earnings
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 收入靠罪恶手段：十二宫被土星或火星占据且无吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的钱是怎么来的
- 我会不会走上不正当的路子

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十二宫（Vyaya）是否被吉星相照

## 按情况检查的事实

- 土星（Shani）是否落十二宫（Vyaya）
- 火星（Mangal）是否落十二宫（Vyaya）

## 依赖方法

- 无

## 执行步骤

### ch23-v13-shani-mangal-in-vyaya-sinful-earnings.step-001

- 动作：先核对十二宫（Vyaya）是否受吉星相照，确认没有吉星相照后，再核对十二宫内是否有土星（Shani）或火星（Mangal）。
- 适用范围：仅限本命盘十二宫（Vyaya Bhava）的收入来源主题；原文占据者只写出 Shani, or Mangal etc.，etc. 所指未列出，未列出的行星不确定即停判；原文未给时间限定。
- 原文最小意思：十二宫（Vyaya）被土星（Shani）占据，或被火星（Mangal）占据，且没有受到吉星相照时，收入将通过罪恶的手段取得。
- 本步骤产出事实：["十二宫凶星占据无吉照的收入来源判定"]
- 所需事实：["十二宫（Vyaya）是否被吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "十二宫（Vyaya）是否被吉星相照"}]}, {"operator": "OR", "operands": [{"fact_key": "土星（Shani）是否落十二宫（Vyaya）"}, {"fact_key": "火星（Mangal）是否落十二宫（Vyaya）"}]}]}
- 按分支必查事实：[{"when": {"operator": "NOT", "operands": [{"fact_key": "十二宫（Vyaya）是否被吉星相照"}]}, "required_fact_keys": ["土星（Shani）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "土星（Shani）是否落十二宫（Vyaya）"}, "selection_group": "ch23-v13-shani-mangal-in-vyaya-sinful-earnings.step-001:vyaya-occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：土星（Shani）是否落十二宫（Vyaya）。"}, {"when": {"operator": "NOT", "operands": [{"fact_key": "十二宫（Vyaya）是否被吉星相照"}]}, "required_fact_keys": ["火星（Mangal）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否落十二宫（Vyaya）"}, "selection_group": "ch23-v13-shani-mangal-in-vyaya-sinful-earnings.step-001:vyaya-occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否落十二宫（Vyaya）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把原文的 etc. 自行补成全部凶星或某几颗指定行星。", "不得省掉「没有吉星相照」这一前提。", "不得据此推断犯罪、刑罚或收入数额。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十二宫（Vyaya）是否被吉星相照。
- 缺失即停字段：["十二宫（Vyaya）是否被吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch23:v13`｜PDF [40]｜“Earnings will be through sinful measures, if Vyaya is occupied by Shani, or Mangal etc. and is not receiving a Drishti from a benefic.”


## 四路查书计划

### 支持路

- Earnings will be through sinful measures, if Vyaya is occupied by Shani, or Mangal etc. and is not receiving a Drishti from a benefic.
- 十二宫 土星 火星 占据 没有吉星相照 罪恶的收入

### 反例或取消路

- There will be expenses on good accounts, if Vyaya’s Lord is with a benefic, or in his own Bhava, or exalted, or, if a benefic occupies Vyaya.
- If Gulik is in Vyaya Bhava, the native will indulge in base deeds, be sinful, defectivelimbed, unfortunate, indolent and will join mean people.
- If Vyaya’s Lord is in Ari Bhava, the native will incur enmity with his own men, be given to anger, be sinful, miserable and will go to others’ wives.

### 适用边界路

- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Benefics in both Vyaya and Dhan Bhava cause Subh Yog. Malefics in both Vyaya and Dhan Bhava cause Asubh Yog.

### 判断方法路

- Just as these effects are derived from Tanu Bhava in regard to the native, similar deductions be made about co-borns etc. from Sahaj and other Bhavas.
- 十二宫被凶星占据又无吉照该怎么判断

## 上游问题

- 无

## 停止条件

- 缺少十二宫是否被吉星相照的事实时停止。
- 土星与火星的十二宫落宫事实都缺失时停止。
- 原文 etc. 所指的其余行星未确定时，对这些行星停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
