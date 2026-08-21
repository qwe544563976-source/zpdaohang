---
method: ch23-v5-6-vyaya-lord-angle-trine-spouse
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 会得到配偶：十二宫主落角宫或三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能不能成家
- 我会不会有配偶

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘十二宫主（Vyaya's Lord）落在哪一宫

## 按情况检查的事实

- 十二宫主（Vyaya's Lord）是否落角宫
- 十二宫主（Vyaya's Lord）是否落三角宫

## 依赖方法

- 无

## 执行步骤

### ch23-v5-6-vyaya-lord-angle-trine-spouse.step-001

- 动作：取本盘十二宫主（Vyaya's Lord）落在哪一宫，再判断它是否落角宫或三角宫。
- 适用范围：仅限本命盘十二宫（Vyaya Bhava）主题下的得配偶断语；原文本句用代词 he，承接同偈前句的 Vyaya’s Lord，未另指其他行星；原文未给结婚时间。
- 原文最小意思：十二宫主（Vyaya's Lord）落角宫或三角宫时，命主会得到配偶。
- 本步骤产出事实：["十二宫主落角宫三角宫的得配偶判定"]
- 所需事实：["本盘十二宫主（Vyaya's Lord）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘十二宫主（Vyaya's Lord）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否落角宫"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落三角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）落在哪一宫"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否落角宫"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否落角宫"}, "selection_group": "ch23-v5-6-vyaya-lord-angle-trine-spouse.step-001:angle-or-trine", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否落角宫。"}, {"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）落在哪一宫"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否落三角宫"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否落三角宫"}, "selection_group": "ch23-v5-6-vyaya-lord-angle-trine-spouse.step-001:angle-or-trine", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否落三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断结婚年份、配偶人数或配偶特征。", "不得把代词 he 改挂到同偈前句主语 Vyaya’s Lord 以外的行星。", "不得把角宫与三角宫改写成必须同时成立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘十二宫主（Vyaya's Lord）落在哪一宫。
- 缺失即停字段：["本盘十二宫主（Vyaya's Lord）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch23:v5-6`｜PDF [40]｜“If he be in an angle, or trine, the native will beget a spouse.”


## 四路查书计划

### 支持路

- If he be in an angle, or trine, the native will beget a spouse.
- 十二宫主 落角宫 三角宫 得配偶

### 反例或取消路

- If Yuvati Lord is devoid of strength and is relegated to Ari, 8<sup>th</sup> , or Vyaya, or, if Yuvati Lord is in fall, the native’s wife will be destroyed
- And, if Vyaya’s Lord is in Ari, or Randhr Bhava, or be in enemy’s Navāńś, in debilitation Navāńś, or in Randhr Bhava in Navāńś, one will be devoid of happiness from wife

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine)
- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.

### 判断方法路

- Effects of Vyaya’s Lord in Various Bhavas
- 判断婚姻要看哪一宫的宫主落在角宫或三角宫

## 上游问题

- 无

## 停止条件

- 缺少本盘十二宫主落在哪一宫的事实时停止。
- 角宫与三角宫两个分支事实都缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
