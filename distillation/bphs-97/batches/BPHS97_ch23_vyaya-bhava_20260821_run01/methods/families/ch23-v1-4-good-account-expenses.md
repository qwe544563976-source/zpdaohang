---
method: ch23-v1-4-good-account-expenses
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 开支花在好用途上：十二宫主与吉星同宫、落自己主管的宫位或入旺，或十二宫被吉星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的钱都花到哪里去了
- 我这辈子的开销是好是坏

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘十二宫主（Vyaya's Lord）是哪颗行星

## 按情况检查的事实

- 十二宫主（Vyaya's Lord）是否与吉星同宫
- 十二宫主（Vyaya's Lord）是否落自己主管的宫位（own Bhava）
- 十二宫主（Vyaya's Lord）是否入旺
- 十二宫（Vyaya）是否被吉星占据

## 依赖方法

- 无

## 执行步骤

### ch23-v1-4-good-account-expenses.step-001

- 动作：先取本盘十二宫主（Vyaya's Lord）是哪颗行星，再逐一核对它是否与吉星同宫、是否落自己主管的宫位、是否入旺，以及十二宫（Vyaya）内是否有吉星。
- 适用范围：仅限本命盘十二宫（Vyaya Bhava）的开支性质主题；原文只给出四个并列择一条件，未给时间限定，也未给开支的数额或对象。
- 原文最小意思：十二宫主（Vyaya's Lord）与吉星同宫，或落自己主管的宫位（own Bhava），或入旺，或者十二宫（Vyaya）被吉星占据时，开支会花在好的用途上。
- 本步骤产出事实：["十二宫主状态下的开支性质判定"]
- 所需事实：["本盘十二宫主（Vyaya's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否与吉星同宫"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落自己主管的宫位（own Bhava）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否入旺"}, {"fact_key": "十二宫（Vyaya）是否被吉星占据"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否与吉星同宫"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否与吉星同宫"}, "selection_group": "ch23-v1-4-good-account-expenses.step-001:good-expense-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否与吉星同宫。"}, {"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否落自己主管的宫位（own Bhava）"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否落自己主管的宫位（own Bhava）"}, "selection_group": "ch23-v1-4-good-account-expenses.step-001:good-expense-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否落自己主管的宫位（own Bhava）。"}, {"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否入旺"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否入旺"}, "selection_group": "ch23-v1-4-good-account-expenses.step-001:good-expense-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否入旺。"}, {"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, "required_fact_keys": ["十二宫（Vyaya）是否被吉星占据"], "branch_condition_logic": {"fact_key": "十二宫（Vyaya）是否被吉星占据"}, "selection_group": "ch23-v1-4-good-account-expenses.step-001:good-expense-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫（Vyaya）是否被吉星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断开支的金额、时间或具体项目。", "不得把「好的用途」扩大成发财、致富或进项增加。", "不得把四个择一条件改写成必须同时成立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘十二宫主（Vyaya's Lord）是哪颗行星。
- 缺失即停字段：["本盘十二宫主（Vyaya's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch23:v1-4`｜PDF [40]｜“There will be expenses on good accounts, if Vyaya’s Lord is with a benefic, or in his own Bhava, or exalted, or, if a benefic occupies Vyaya.”


## 四路查书计划

### 支持路

- There will be expenses on good accounts, if Vyaya’s Lord is with a benefic, or in his own Bhava, or exalted
- 十二宫主 与吉星同宫 入旺 开支 好的用途

### 反例或取消路

- If Vyaya’s Lord is in Vyaya Bhava, the native will only face heavy expenditure, will not have physical felicity, be irritable and spiteful.
- Earnings will be through sinful measures, if Vyaya is occupied by Shani, or Mangal etc. and is not receiving a Drishti from a benefic.
- If Lagn’s Lord is in Vyaya Bhava and is devoid of benefic Drishti and/or Yuti, the native will be bereft of physical happiness, will spend unfruitfully and be given to much anger.

### 适用边界路

- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula
- It is half beneficial in its own Bhava

### 判断方法路

- Effects of Vyaya’s Lord in Various Bhavas
- 判断十二宫开支要先看十二宫主与吉星的关系

## 上游问题

- 无

## 停止条件

- 缺少本盘十二宫主是哪颗行星的事实时停止。
- 四个择一条件的事实全部缺失时停止。
- 吉星名册未确定时，与吉星有关的两个分支停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
