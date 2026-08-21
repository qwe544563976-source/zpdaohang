---
method: ch13-v4-dhan-labh-lords-wealth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 得财：二宫主与十一宫主互居，或会合于角宫、三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能不能挣到钱
- 二宫主和十一宫主的关系对财运有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘二宫主（Dhan's Lord）是哪颗行星
- 本盘十一宫主（Labh's Lord）是哪颗行星

## 按情况检查的事实

- 二宫主（Dhan's Lord）是否落十一宫（Labh）
- 十一宫主（Labh's Lord）是否落二宫（Dhan）
- 二宫主（Dhan's Lord）与十一宫主（Labh's Lord）会合之处是否为角宫
- 二宫主（Dhan's Lord）与十一宫主（Labh's Lord）会合之处是否为三角宫

## 依赖方法

- 无

## 执行步骤

### ch13-v4-dhan-labh-lords-wealth.step-001

- 动作：先确定二宫主与十一宫主分别是哪颗行星，再核对两者互居，或两者会合于角宫、会合于三角宫。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；原文未给时间、上升或数额限定。
- 原文最小意思：二宫主（Dhan Lord）落十一宫（Labh）、十一宫主（Lord of Labh）落二宫（Dhan）时，命主获得财富；这两个宫主也可以会合于角宫，或会合于三角宫。
- 本步骤产出事实：["二宫主与十一宫主的得财判定"]
- 所需事实：["本盘二宫主（Dhan's Lord）是哪颗行星", "本盘十一宫主（Labh's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落十一宫（Labh）"}, {"fact_key": "十一宫主（Labh's Lord）是否落二宫（Dhan）"}]}, {"fact_key": "二宫主（Dhan's Lord）与十一宫主（Labh's Lord）会合之处是否为角宫"}, {"fact_key": "二宫主（Dhan's Lord）与十一宫主（Labh's Lord）会合之处是否为三角宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}]}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落十一宫（Labh）", "十一宫主（Labh's Lord）是否落二宫（Dhan）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落十一宫（Labh）"}, {"fact_key": "十一宫主（Labh's Lord）是否落二宫（Dhan）"}]}, "selection_group": "ch13-v4-dhan-labh-lords-wealth.step-001:dhan-labh-lord-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落十一宫（Labh）、十一宫主（Labh's Lord）是否落二宫（Dhan）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}]}, "required_fact_keys": ["二宫主（Dhan's Lord）与十一宫主（Labh's Lord）会合之处是否为角宫"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）与十一宫主（Labh's Lord）会合之处是否为角宫"}, "selection_group": "ch13-v4-dhan-labh-lords-wealth.step-001:dhan-labh-lord-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）与十一宫主（Labh's Lord）会合之处是否为角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}]}, "required_fact_keys": ["二宫主（Dhan's Lord）与十一宫主（Labh's Lord）会合之处是否为三角宫"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）与十一宫主（Labh's Lord）会合之处是否为三角宫"}, "selection_group": "ch13-v4-dhan-labh-lords-wealth.step-001:dhan-labh-lord-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）与十一宫主（Labh's Lord）会合之处是否为三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、来源或得财时间。", "不得把「互居」与「会合」两种情形合并成必须同时成立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘二宫主（Dhan's Lord）是哪颗行星、本盘十一宫主（Labh's Lord）是哪颗行星。
- 缺失即停字段：["本盘二宫主（Dhan's Lord）是哪颗行星", "本盘十一宫主（Labh's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v4`｜PDF [27]｜“If Dhan Lord is in Labh, while the Lord of Labh in Dhan, wealth will be acquired by the native. Alternately these two Lords may join in an angle, or in a trine.”


## 四路查书计划

### 支持路

- If Dhan Lord is in Labh, while the Lord of Labh in Dhan, wealth will be acquired by the native
- Alternately these two Lords may join in an angle, or in a trine
- 二宫主落十一宫 十一宫主落二宫 得财

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed
- Should the Lords of Dhan and Labh Bhava be relegated to Ari, Randhr, or Vyaya Bhava
- There will be penury right from birth and the native will have to beg even for his food, if the Lords of Dhan and Labh Bhava are both combust, or with malefics

### 适用边界路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- Indications of Labh Bhava
- If the Lord of Dhan is in Dhan, or is in an angle, or in trine, he will promote one’s wealth (or monetary state)

### 判断方法路

- I now tell you of special combinations, giving wealth. One born to these Yogas will surely become wealthy
- If Dhan’s Lord is in Dhan Bhava, the native will be wealthy, proud, will have two, or more wives and be bereft of progeny
- 判断财富要看二宫主与十一宫主的关系

## 上游问题

- 无

## 停止条件

- 缺少二宫主、十一宫主的行星身份事实时停止。
- 互居、会合角宫、会合三角宫三个分支事实全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
