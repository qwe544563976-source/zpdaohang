---
method: ch13-v1-2-dhan-lord-dusthana-financial-decline
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 经济衰退：二宫主落六宫、八宫或十二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会破财
- 二宫主落六八十二宫代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘二宫主（Dhan's Lord）是哪颗行星

## 按情况检查的事实

- 二宫主（Dhan's Lord）是否落六宫（Ari）
- 二宫主（Dhan's Lord）是否落八宫（Randhr）
- 二宫主（Dhan's Lord）是否落十二宫（Vyaya）

## 依赖方法

- 无

## 执行步骤

### ch13-v1-2-dhan-lord-dusthana-financial-decline.step-001

- 动作：先定出二宫主是哪颗行星，再核对它是否落六宫、八宫或十二宫。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；本句的 he 承接同偈前句的 the Lord of Dhan。
- 原文最小意思：二宫主（the Lord of Dhan）落六宫（Ari）、八宫或十二宫时，经济状况会衰退。
- 本步骤产出事实：["二宫主落凶宫的经济衰退判定"]
- 所需事实：["本盘二宫主（Dhan's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落六宫（Ari）"}, {"fact_key": "二宫主（Dhan's Lord）是否落八宫（Randhr）"}, {"fact_key": "二宫主（Dhan's Lord）是否落十二宫（Vyaya）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落六宫（Ari）"}, "selection_group": "ch13-v1-2-dhan-lord-dusthana-financial-decline.step-001:dhan-lord-dusthana", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落六宫（Ari）。"}, {"when": {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落八宫（Randhr）"}, "selection_group": "ch13-v1-2-dhan-lord-dusthana-financial-decline.step-001:dhan-lord-dusthana", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落八宫（Randhr）。"}, {"when": {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落十二宫（Vyaya）"}, "selection_group": "ch13-v1-2-dhan-lord-dusthana-financial-decline.step-001:dhan-lord-dusthana", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落十二宫（Vyaya）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 decline 读成一贫如洗，原文只说经济状况衰退。", "不得据此推断衰退的年份或大运。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘二宫主（Dhan's Lord）是哪颗行星。
- 缺失即停字段：["本盘二宫主（Dhan's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v1-2`｜PDF [27]｜“Should he be in Ari/8<sup>th</sup> /12<sup>th</sup> , financial conditions will decline.”


## 四路查书计划

### 支持路

- Should he be in Ari/8th /12th , financial conditions will decline
- 二宫主落六宫八宫十二宫 经济衰退

### 反例或取消路

- If the Lord of Dhan is in Dhan, or is in an angle, or in trine, he will promote one’s wealth (or monetary state)
- Should Budh give a Drishti to Mangal and Shani in Dhan Bhava, there will be great wealth

### 适用边界路

- Putr and Dharm Bhava are known by the name Kon (or trine). Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Effects of Dhan Bhava
- Now I tell you some Yogas for poverty along with conditions of their nullifications
- 判断破财要看二宫主落不落六八十二宫

## 上游问题

- 无

## 停止条件

- 缺少二宫主身份事实时停止。
- 三个落宫分支事实全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
