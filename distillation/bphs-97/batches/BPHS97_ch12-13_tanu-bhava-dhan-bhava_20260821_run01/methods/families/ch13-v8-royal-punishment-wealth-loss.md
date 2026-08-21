---
method: ch13-v8-royal-punishment-wealth-loss
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 因王家刑罚失财：二宫主十一宫主落六八十二宫且火星落十一宫、罗睺落二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会因为官非罚没而破财
- 什么组合会因为官方处罚失去钱财

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 火星（Mangal）是否落十一宫（Labh）
- 罗睺（Rahu）是否落二宫（Dhan）
- 本盘二宫主（Dhan's Lord）落在哪一宫
- 本盘十一宫主（Labh's Lord）落在哪一宫

## 按情况检查的事实

- 二宫主（Dhan's Lord）是否落六宫（Ari）
- 二宫主（Dhan's Lord）是否落八宫（Randhr）
- 二宫主（Dhan's Lord）是否落十二宫（Vyaya）
- 十一宫主（Labh's Lord）是否落六宫（Ari）
- 十一宫主（Labh's Lord）是否落八宫（Randhr）
- 十一宫主（Labh's Lord）是否落十二宫（Vyaya）

## 依赖方法

- 无

## 执行步骤

### ch13-v8-royal-punishment-wealth-loss.step-001

- 动作：先核对火星（Mangal）落十一宫、罗睺（Rahu）落二宫，再分别核对二宫主与十一宫主是否落六宫、八宫或十二宫。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；原文未给时间或大运限定，也未说明刑罚的具体形式。
- 原文最小意思：二宫主与十一宫主都落六宫（Ari）、八宫（Randhr）或十二宫（Vyaya）之一，同时火星（Mangal）落十一宫（Labh）、罗睺（Rahu）落二宫（Dhan）时，命主因王家刑罚而失去财富。
- 本步骤产出事实：["王家刑罚失财判定"]
- 所需事实：["火星（Mangal）是否落十一宫（Labh）", "罗睺（Rahu）是否落二宫（Dhan）", "本盘二宫主（Dhan's Lord）落在哪一宫", "本盘十一宫主（Labh's Lord）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落十一宫（Labh）"}, {"fact_key": "罗睺（Rahu）是否落二宫（Dhan）"}, {"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, {"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}]}, {"operator": "OR", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落六宫（Ari）"}, {"fact_key": "二宫主（Dhan's Lord）是否落八宫（Randhr）"}, {"fact_key": "二宫主（Dhan's Lord）是否落十二宫（Vyaya）"}]}, {"operator": "OR", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落六宫（Ari）"}, {"fact_key": "十一宫主（Labh's Lord）是否落八宫（Randhr）"}, {"fact_key": "十一宫主（Labh's Lord）是否落十二宫（Vyaya）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落十一宫（Labh）"}, {"fact_key": "罗睺（Rahu）是否落二宫（Dhan）"}, {"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, {"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}]}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落六宫（Ari）"}, "selection_group": "ch13-v8-royal-punishment-wealth-loss.step-001:dhan-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落十一宫（Labh）"}, {"fact_key": "罗睺（Rahu）是否落二宫（Dhan）"}, {"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, {"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}]}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落八宫（Randhr）"}, "selection_group": "ch13-v8-royal-punishment-wealth-loss.step-001:dhan-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落八宫（Randhr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落十一宫（Labh）"}, {"fact_key": "罗睺（Rahu）是否落二宫（Dhan）"}, {"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, {"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}]}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落十二宫（Vyaya）"}, "selection_group": "ch13-v8-royal-punishment-wealth-loss.step-001:dhan-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落十二宫（Vyaya）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落十一宫（Labh）"}, {"fact_key": "罗睺（Rahu）是否落二宫（Dhan）"}, {"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, {"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}]}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否落六宫（Ari）"}, "selection_group": "ch13-v8-royal-punishment-wealth-loss.step-001:labh-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落十一宫（Labh）"}, {"fact_key": "罗睺（Rahu）是否落二宫（Dhan）"}, {"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, {"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}]}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否落八宫（Randhr）"}, "selection_group": "ch13-v8-royal-punishment-wealth-loss.step-001:labh-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落八宫（Randhr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落十一宫（Labh）"}, {"fact_key": "罗睺（Rahu）是否落二宫（Dhan）"}, {"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, {"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}]}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否落十二宫（Vyaya）"}, "selection_group": "ch13-v8-royal-punishment-wealth-loss.step-001:labh-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落十二宫（Vyaya）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得省去火星落十一宫、罗睺落二宫两个条件，只凭宫主落六八十二宫就下断语。", "不得据此推断失财的时间、金额或刑罚种类。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：火星（Mangal）是否落十一宫（Labh）、罗睺（Rahu）是否落二宫（Dhan）、本盘二宫主（Dhan's Lord）落在哪一宫、本盘十一宫主（Labh's Lord）落在哪一宫。
- 缺失即停字段：["火星（Mangal）是否落十一宫（Labh）", "罗睺（Rahu）是否落二宫（Dhan）", "本盘二宫主（Dhan's Lord）落在哪一宫", "本盘十一宫主（Labh's Lord）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v8`｜PDF [28]｜“Should the Lords of Dhan and Labh Bhava be relegated to Ari, Randhr, or Vyaya Bhava, while Mangal is in Labh Bhava and Rahu is in Dhan Bhava, the native will lose his wealth on account of royal punishments.”


## 四路查书计划

### 支持路

- Should the Lords of Dhan and Labh Bhava be relegated to Ari, Randhr, or Vyaya Bhava, while Mangal is in Labh Bhava and Rahu is in Dhan Bhava, the native will lose his wealth on account of royal punishments
- 二宫主十一宫主落六宫八宫十二宫 火星落十一宫 罗睺落二宫 王家刑罚 失财

### 反例或取消路

- If Dhan Lord is in Labh, while the Lord of Labh in Dhan, wealth will be acquired by the native
- If the Lord of Dhan is in an angle, while Labh Lord is in a trine thereof, or is drishtied by, or yuti with Guru and Shukr, the subject will be wealthy
- If Karm’s Lord is in Dhan Bhava, the native will be wealthy, virtuous, honoured by the king, charitable

### 适用边界路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- Note the Grahas, that are ruling the Rāśis, occupied by the Lords of Ari, Randhr and Vyaya Bhava. If the said dispositors are in such evil Bhavas in turn and are associated with, or receive a Drishti from malefics, the native will be miserable and indigent
- Indications of Labh Bhava

### 判断方法路

- Now I tell you some Yogas for poverty along with conditions of their nullifications
- If the Lord of Dhan is in Dhan, or is in an angle, or in trine, he will promote one’s wealth (or monetary state)
- 判断破财要看二宫主与十一宫主落在哪一宫

## 上游问题

- 无

## 停止条件

- 缺少火星落十一宫、罗睺落二宫任一事实时停止。
- 缺少二宫主或十一宫主落宫事实时停止。
- 二宫主的三个落宫分支事实全缺，或十一宫主的三个落宫分支事实全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
