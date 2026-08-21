---
method: ch22-v2-labh-lord-placement-gains
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 收获甚多：十一宫主落十一宫、角宫或从上升起算的三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子的收入进项怎么样
- 我能不能有很多收获

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘十一宫主（Labh's Lord）落在哪一宫

## 按情况检查的事实

- 十一宫主（Labh's Lord）是否落十一宫（Labh）
- 十一宫主（Labh's Lord）是否落角宫
- 十一宫主（Labh's Lord）是否落三角宫

## 依赖方法

- 无

## 执行步骤

### ch22-v2-labh-lord-placement-gains.step-001

- 动作：核对十一宫主（Labh's Lord）落在哪一宫，看它是否落十一宫（Labh）本身、落角宫、或落从上升（Lagna）起算的三角宫。
- 适用范围：仅限本命盘十一宫（Labh）收获主题；原文三个落宫是并列备选，任一成立即可；原文未给收获数额与时间。
- 原文最小意思：十一宫主落十一宫、落角宫或落从上升起算的三角宫时，收获甚多。
- 本步骤产出事实：["十一宫主落宫收获甚多判定"]
- 所需事实：["本盘十一宫主（Labh's Lord）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落十一宫（Labh）"}, {"fact_key": "十一宫主（Labh's Lord）是否落角宫"}, {"fact_key": "十一宫主（Labh's Lord）是否落三角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落十一宫（Labh）"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否落十一宫（Labh）"}, "selection_group": "ch22-v2-labh-lord-placement-gains.step-001:labh-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落十一宫（Labh）。"}, {"when": {"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落角宫"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否落角宫"}, "selection_group": "ch22-v2-labh-lord-placement-gains.step-001:labh-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落角宫。"}, {"when": {"fact_key": "本盘十一宫主（Labh's Lord）落在哪一宫"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落三角宫"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否落三角宫"}, "selection_group": "ch22-v2-labh-lord-placement-gains.step-001:labh-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断收获的数额、来源或应期。", "不得要求三个落宫同时成立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘十一宫主（Labh's Lord）落在哪一宫。
- 缺失即停字段：["本盘十一宫主（Labh's Lord）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch22:v2`｜PDF [39]｜“Should Labh’s Lord be in Labh itself, or be in an angle, or in a trine from Lagna, there will be many gains.”


## 四路查书计划

### 支持路

- Should Labh’s Lord be in Labh itself, or be in an angle, or in a trine from Lagna, there will be many gains
- 十一宫主落十一宫 落角宫 落三角宫 收获甚多

### 反例或取消路

- There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic
- If Labh’s Lord is in Sahaj Bhava, while Labh Bhava is occupied by a benefic, the native will gain 2000 Nishkas in his 36th year

### 适用边界路

- Kendras, Konas etc. defined. O Maitreya, listen to other matters, which I am explaining. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Indications of Labh Bhava. All articles, son’s wife, income, prosperity, quadrupeds etc. are to be understood from Labh Bhava

### 判断方法路

- If Labh’s Lord is in Labh Bhava, the native will gain in all his undertakings, while his learning and happiness will be on the increase day by day
- 判断十一宫（Labh）收获应检查十一宫主落在哪一宫

## 上游问题

- 无

## 停止条件

- 缺少十一宫主落宫事实时停止。
- 落十一宫、落角宫、落三角宫三个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
