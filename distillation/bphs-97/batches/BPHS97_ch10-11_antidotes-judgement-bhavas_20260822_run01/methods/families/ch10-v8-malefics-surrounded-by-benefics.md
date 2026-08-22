---
method: ch10-v8-malefics-surrounded-by-benefics
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶恶速消：凶星被吉星包围且角宫或三角宫被吉星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我盘里的凶象会不会很快过去
- 凶星被吉星夹住有什么用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中的凶星是否被吉星包围（surrounded by benefics）

## 按情况检查的事实

- 角宫（Kendr）是否被吉星占据
- 三角宫（Kon）是否被吉星占据

## 依赖方法

- 无

## 执行步骤

### ch10-v8-malefics-surrounded-by-benefics.step-001

- 动作：核对凶星是否被吉星包围，并核对角宫或三角宫本身是否被吉星占据。
- 适用范围：仅限第 10 章消解凶恶（Antidotes for Evils）主题；原文只说 soon，没有给具体时间。
- 原文最小意思：凶星被吉星包围，同时角宫或三角宫本身被吉星占据时，凶恶很快消失，而且相关诸宫不再产生凶恶。
- 本步骤产出事实：["凶星受吉星包围凶恶速消判定"]
- 所需事实：["本盘中的凶星是否被吉星包围（surrounded by benefics）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中的凶星是否被吉星包围（surrounded by benefics）"}, {"operator": "OR", "operands": [{"fact_key": "角宫（Kendr）是否被吉星占据"}, {"fact_key": "三角宫（Kon）是否被吉星占据"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中的凶星是否被吉星包围（surrounded by benefics）"}, "required_fact_keys": ["角宫（Kendr）是否被吉星占据"], "branch_condition_logic": {"fact_key": "角宫（Kendr）是否被吉星占据"}, "selection_group": "ch10-v8-malefics-surrounded-by-benefics.step-001:kendra-or-trine-benefic-occupied", "stop_condition": "选中该分支后，缺少以下事实即停止：角宫（Kendr）是否被吉星占据。"}, {"when": {"fact_key": "本盘中的凶星是否被吉星包围（surrounded by benefics）"}, "required_fact_keys": ["三角宫（Kon）是否被吉星占据"], "branch_condition_logic": {"fact_key": "三角宫（Kon）是否被吉星占据"}, "selection_group": "ch10-v8-malefics-surrounded-by-benefics.step-001:kendra-or-trine-benefic-occupied", "stop_condition": "选中该分支后，缺少以下事实即停止：三角宫（Kon）是否被吉星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 soon 折算成具体年数或大运。", "不得把「相关诸宫」扩大成全盘所有宫位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中的凶星是否被吉星包围（surrounded by benefics）。
- 缺失即停字段：["本盘中的凶星是否被吉星包围（surrounded by benefics）"]
- 原文证据：
  - `bphs-97:santhanam:ch10:v8`｜PDF [25]｜“If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon. Not only this, evils will not follow from the Bhavas concerned.”


## 四路查书计划

### 支持路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon
- 凶星被吉星包围 角宫三角宫被吉星占据 凶恶很快消失

### 反例或取消路

- Malefic in Vyaya and Ari Bhava, or in Randhr and Dhan Bhava, while Lagn is hemmed between other malefics, will bring early death
- Chandra in Tanu, Randhr, Vyaya, or Yuvati Bhava and hemmed between malefics will confer premature death

### 适用边界路

- O Brahmin, first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas
- 凶恶与消解因素的先后次序

### 判断方法路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness
- 怎样判断吉星凶星的分布

## 上游问题

- 无

## 停止条件

- 缺少凶星是否被吉星包围的事实时停止。
- 角宫与三角宫的吉星占据事实都取不到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
