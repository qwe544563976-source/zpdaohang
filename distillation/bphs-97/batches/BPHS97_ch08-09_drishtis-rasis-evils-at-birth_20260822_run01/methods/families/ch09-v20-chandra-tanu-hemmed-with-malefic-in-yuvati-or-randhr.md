---
method: ch09-v20-chandra-tanu-hemmed-with-malefic-in-yuvati-or-randhr
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮落一宫被凶星夹，且七宫或八宫有凶星：连同母亲当即去世

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮落一宫被夹又有凶星占七宫八宫怎么断
- 母子同时的凶象

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否落一宫（Tanu Bhava）
- 月亮（Chandra）是否被凶星夹（hemmed between malefics）

## 按情况检查的事实

- 七宫（Yuvati Bhava）是否被凶星占据
- 八宫（Randhr Bhava）是否被凶星占据

## 依赖方法

- 无

## 执行步骤

### ch09-v20-chandra-tanu-hemmed-with-malefic-in-yuvati-or-randhr.step-001

- 动作：核对月亮是否落一宫且被凶星夹，并核对七宫或八宫内有无凶星。
- 适用范围：仅限本命盘出生时的凶象；断语对象是命主与其母亲。
- 原文最小意思：月亮（Chandra）落一宫（Tanu Bhava）并被凶星夹，同时七宫（Yuvati）或八宫（Randhr Bhava）内有凶星时，他会连同母亲当即去世。
- 本步骤产出事实：["月亮落一宫被夹的母子同殇判定"]
- 所需事实：["月亮（Chandra）是否落一宫（Tanu Bhava）", "月亮（Chandra）是否被凶星夹（hemmed between malefics）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落一宫（Tanu Bhava）"}, {"fact_key": "月亮（Chandra）是否被凶星夹（hemmed between malefics）"}]}, {"operator": "OR", "operands": [{"fact_key": "七宫（Yuvati Bhava）是否被凶星占据"}, {"fact_key": "八宫（Randhr Bhava）是否被凶星占据"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落一宫（Tanu Bhava）"}, {"fact_key": "月亮（Chandra）是否被凶星夹（hemmed between malefics）"}]}, "required_fact_keys": ["七宫（Yuvati Bhava）是否被凶星占据"], "branch_condition_logic": {"fact_key": "七宫（Yuvati Bhava）是否被凶星占据"}, "selection_group": "ch09-v20-chandra-tanu-hemmed-with-malefic-in-yuvati-or-randhr.step-001:malefic-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫（Yuvati Bhava）是否被凶星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落一宫（Tanu Bhava）"}, {"fact_key": "月亮（Chandra）是否被凶星夹（hemmed between malefics）"}]}, "required_fact_keys": ["八宫（Randhr Bhava）是否被凶星占据"], "branch_condition_logic": {"fact_key": "八宫（Randhr Bhava）是否被凶星占据"}, "selection_group": "ch09-v20-chandra-tanu-hemmed-with-malefic-in-yuvati-or-randhr.step-001:malefic-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫（Randhr Bhava）是否被凶星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『当即』补成原文没有的具体时间。", "不得把断语对象从命主与母亲换成其他亲属。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否落一宫（Tanu Bhava）、月亮（Chandra）是否被凶星夹（hemmed between malefics）。
- 缺失即停字段：["月亮（Chandra）是否落一宫（Tanu Bhava）", "月亮（Chandra）是否被凶星夹（hemmed between malefics）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v20`｜PDF [23]｜“Should Chandra be in Tanu Bhava, hemmed between malefics, while Yuvati, or Randhr Bhava has a malefic in it, he will face immediate death along with his mother.”


## 四路查书计划

### 支持路

- Should Chandra be in Tanu Bhava, hemmed between malefics, while Yuvati, or Randhr Bhava has a malefic in it, he will face immediate death along with his mother
- 月亮一宫 被夹 七宫八宫凶星 母子

### 反例或取消路

- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Evils to Mother (up to Sloka 33)
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas

### 判断方法路

- Evils at Birth
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 母亲的凶象怎么看

## 上游问题

- 无

## 停止条件

- 缺少月亮所落宫位或被夹事实时停止。
- 缺少七宫、八宫的凶星占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
