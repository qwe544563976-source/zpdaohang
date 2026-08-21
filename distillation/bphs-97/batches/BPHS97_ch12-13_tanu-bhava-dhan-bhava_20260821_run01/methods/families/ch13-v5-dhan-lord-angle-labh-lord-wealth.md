---
method: ch13-v5-dhan-lord-angle-labh-lord-wealth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 富有：二宫主落角宫，十一宫主落其三角宫或得木星金星相照、同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的财富状况好不好
- 二宫主落角宫时财运怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫主（Dhan's Lord）是否落角宫

## 按情况检查的事实

- 十一宫主（Labh's Lord）是否落从二宫主（Dhan's Lord）所在宫起算的三角宫
- 十一宫主（Labh's Lord）是否被木星（Guru）相照
- 十一宫主（Labh's Lord）是否被金星（Shukra）相照
- 十一宫主（Labh's Lord）是否与木星（Guru）同宫
- 十一宫主（Labh's Lord）是否与金星（Shukra）同宫

## 依赖方法

- 无

## 执行步骤

### ch13-v5-dhan-lord-angle-labh-lord-wealth.step-001

- 动作：先核对二宫主是否落角宫，再核对十一宫主是否落其三角宫、是否被木星与金星相照、是否与木星与金星同宫。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；原文 in a trine thereof 的起点是二宫主所落的那个角宫，drishtied by 与 yuti with 两种情形按原文承接同一主语十一宫主（Labh Lord）。
- 原文最小意思：二宫主（Lord of Dhan）落角宫，同时十一宫主（Labh Lord）落其三角宫，或被木星（Guru）与金星（Shukr）相照，或与木星和金星同宫时，命主富有。
- 本步骤产出事实：["二宫主落角宫的富有判定"]
- 所需事实：["二宫主（Dhan's Lord）是否落角宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落角宫"}, {"operator": "OR", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落从二宫主（Dhan's Lord）所在宫起算的三角宫"}, {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否被木星（Guru）相照"}, {"fact_key": "十一宫主（Labh's Lord）是否被金星（Shukra）相照"}]}, {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否与木星（Guru）同宫"}, {"fact_key": "十一宫主（Labh's Lord）是否与金星（Shukra）同宫"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "二宫主（Dhan's Lord）是否落角宫"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落从二宫主（Dhan's Lord）所在宫起算的三角宫"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否落从二宫主（Dhan's Lord）所在宫起算的三角宫"}, "selection_group": "ch13-v5-dhan-lord-angle-labh-lord-wealth.step-001:labh-lord-support", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落从二宫主（Dhan's Lord）所在宫起算的三角宫。"}, {"when": {"fact_key": "二宫主（Dhan's Lord）是否落角宫"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否被木星（Guru）相照", "十一宫主（Labh's Lord）是否被金星（Shukra）相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否被木星（Guru）相照"}, {"fact_key": "十一宫主（Labh's Lord）是否被金星（Shukra）相照"}]}, "selection_group": "ch13-v5-dhan-lord-angle-labh-lord-wealth.step-001:labh-lord-support", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否被木星（Guru）相照、十一宫主（Labh's Lord）是否被金星（Shukra）相照。"}, {"when": {"fact_key": "二宫主（Dhan's Lord）是否落角宫"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否与木星（Guru）同宫", "十一宫主（Labh's Lord）是否与金星（Shukra）同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否与木星（Guru）同宫"}, {"fact_key": "十一宫主（Labh's Lord）是否与金星（Shukra）同宫"}]}, "selection_group": "ch13-v5-dhan-lord-angle-labh-lord-wealth.step-001:labh-lord-support", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否与木星（Guru）同宫、十一宫主（Labh's Lord）是否与金星（Shukra）同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额或得财时间。", "不得把原文要求的「木星与金星」两颗行星减成任一颗。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫主（Dhan's Lord）是否落角宫。
- 缺失即停字段：["二宫主（Dhan's Lord）是否落角宫"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v5`｜PDF [28]｜“If the Lord of Dhan is in an angle, while Labh Lord is in a trine thereof, or is drishtied by, or yuti with Guru and Shukr, the subject will be wealthy.”


## 四路查书计划

### 支持路

- If the Lord of Dhan is in an angle, while Labh Lord is in a trine thereof, or is drishtied by, or yuti with Guru and Shukr, the subject will be wealthy
- 二宫主落角宫 十一宫主落三角宫 木星金星相照 富有

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- Should he be in Ari/8

### 适用边界路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- If the Lord of Dhan is in Dhan, or is in an angle, or in trine, he will promote one’s wealth (or monetary state)
- Indications of Labh Bhava

### 判断方法路

- I now tell you of special combinations, giving wealth. One born to these Yogas will surely become wealthy
- The native will be wealthy, if one among Chandra, Guru, Shukra and Budh is exalted in Dhan Bhava
- 判断财富要看二宫主与十一宫主是否落角宫三角宫

## 上游问题

- 无

## 停止条件

- 缺少二宫主是否落角宫的事实时停止。
- 十一宫主的三个分支事实（落三角宫、被木星金星相照、与木星金星同宫）全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
