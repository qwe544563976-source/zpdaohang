---
method: ch20-v12-begged-food
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 靠乞讨得食：十宫主与三宫主皆无力、九宫主落陷或燃烧

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会穷到要靠人接济
- 十宫主三宫主都无力又九宫主受损说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否有力
- 三宫主（Sahaj's Lord）是否有力

## 按情况检查的事实

- 九宫主（Dharm's Lord）是否落陷
- 九宫主（Dharm's Lord）是否燃烧

## 依赖方法

- 无

## 执行步骤

### ch20-v12-begged-food.step-001

- 动作：核对十宫主（Karm's Lord）与三宫主（Sahaj's Lord）是否都没有力量，再看九宫主（Dharm's Lord）是落陷还是燃烧。
- 适用范围：仅限本命盘九宫（Dharm）生计主题；原文未给时间限定；行星强弱须按本书自己的力量判准取得。
- 原文最小意思：十宫主（Karm's Lord）与三宫主（Sahaj's Lord）都没有力量、且九宫主（Dharm's Lord）落陷，或燃烧时，命主要靠乞讨得食。
- 本步骤产出事实：["十宫主三宫主无力且九宫主落陷或燃烧主乞食判定"]
- 所需事实：["十宫主（Karm's Lord）是否有力", "三宫主（Sahaj's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "十宫主（Karm's Lord）是否有力"}]}, {"operator": "NOT", "operands": [{"fact_key": "三宫主（Sahaj's Lord）是否有力"}]}]}, {"operator": "OR", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落陷"}, {"fact_key": "九宫主（Dharm's Lord）是否燃烧"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "十宫主（Karm's Lord）是否有力"}]}, {"operator": "NOT", "operands": [{"fact_key": "三宫主（Sahaj's Lord）是否有力"}]}]}, "required_fact_keys": ["九宫主（Dharm's Lord）是否落陷"], "branch_condition_logic": {"fact_key": "九宫主（Dharm's Lord）是否落陷"}, "selection_group": "ch20-v12-begged-food.step-001:dharm-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫主（Dharm's Lord）是否落陷。"}, {"when": {"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "十宫主（Karm's Lord）是否有力"}]}, {"operator": "NOT", "operands": [{"fact_key": "三宫主（Sahaj's Lord）是否有力"}]}]}, "required_fact_keys": ["九宫主（Dharm's Lord）是否燃烧"], "branch_condition_logic": {"fact_key": "九宫主（Dharm's Lord）是否燃烧"}, "selection_group": "ch20-v12-begged-food.step-001:dharm-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫主（Dharm's Lord）是否燃烧。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断乞讨发生的年岁或时长。", "不得把落陷与燃烧合并成一个条件。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否有力、三宫主（Sahaj's Lord）是否有力。
- 缺失即停字段：["十宫主（Karm's Lord）是否有力", "三宫主（Sahaj's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v12`｜PDF [37]｜“If Karm’s Lord and Sahaj’s Lord are bereft of strength, while Dharm’s Lord is in fall, or combust the native will go begging for his food.”


## 四路查书计划

### 支持路

- If Karm’s Lord and Sahaj’s Lord are bereft of strength, while Dharm’s Lord is in fall, or combust the native will go begging for his food.
- 十宫主无力 三宫主无力 九宫主落陷 燃烧 乞讨得食

### 反例或取消路

- One will be fortunate (or affluent), if Dharm’s Lord is in Dharm Bhava with strength
- One will enjoy abundant fortunes, if Shukra is in deep exaltation and be in the company of Dharm’s Lord, as Shani is in Sahaj

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Should Shani be in Dharm Bhava along with Chandra, as Lagn’s Lord is in fall, the native will acquire food by begging
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

### 判断方法路

- These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava and in other manners as well
- 判断生计困顿要看十宫主（Karm's Lord）、三宫主（Sahaj's Lord）与九宫主（Dharm's Lord）的哪些状态

## 上游问题

- 无

## 停止条件

- 缺少十宫主（Karm's Lord）强弱事实时停止。
- 缺少三宫主（Sahaj's Lord）强弱事实时停止。
- 行星强弱判准未按本书力量定义确定时停止。
- 落陷与燃烧两个分支事实都缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
