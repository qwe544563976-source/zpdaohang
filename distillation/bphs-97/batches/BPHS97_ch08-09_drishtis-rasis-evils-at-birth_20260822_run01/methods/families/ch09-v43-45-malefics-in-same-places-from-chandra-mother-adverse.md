---
method: ch09-v43-45-malefics-in-same-places-from-chandra-mother-adverse
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶星落自月亮起算的同样位次：对母亲不利

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 自月亮起第六第八第四位有凶星怎么断
- 母亲的不利之象

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘月亮（Chandra）落在哪一宫

## 按情况检查的事实

- 自月亮（Chandra）起算的第 6 位是否有凶星
- 自月亮（Chandra）起算的第 8 位是否有凶星
- 自月亮（Chandra）起算的第 4 位是否有凶星

## 依赖方法

- 无

## 执行步骤

### ch09-v43-45-malefics-in-same-places-from-chandra-mother-adverse.step-001

- 动作：以月亮为起点，核对与上句相同的第 6、第 8 与第 4 位有无凶星。
- 适用范围：仅限本命盘对母亲的判断；原文的『同样的位置』承接同偈上句自太阳起算的第 6、第 8、第 4 位。
- 原文最小意思：凶星落在自太阳（Surya）起算的第 6、第 8 或第 4 位主父亲不吉；凶星落在自月亮（Chandra）起算的这些同样位置，则对母亲不利。
- 本步骤产出事实：["自月亮起特定位次有凶星的母亲不利判定"]
- 所需事实：["本盘月亮（Chandra）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘月亮（Chandra）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "自月亮（Chandra）起算的第 6 位是否有凶星"}, {"fact_key": "自月亮（Chandra）起算的第 8 位是否有凶星"}, {"fact_key": "自月亮（Chandra）起算的第 4 位是否有凶星"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘月亮（Chandra）落在哪一宫"}, "required_fact_keys": ["自月亮（Chandra）起算的第 6 位是否有凶星"], "branch_condition_logic": {"fact_key": "自月亮（Chandra）起算的第 6 位是否有凶星"}, "selection_group": "ch09-v43-45-malefics-in-same-places-from-chandra-mother-adverse.step-001:malefic-place-from-chandra", "stop_condition": "选中该分支后，缺少以下事实即停止：自月亮（Chandra）起算的第 6 位是否有凶星。"}, {"when": {"fact_key": "本盘月亮（Chandra）落在哪一宫"}, "required_fact_keys": ["自月亮（Chandra）起算的第 8 位是否有凶星"], "branch_condition_logic": {"fact_key": "自月亮（Chandra）起算的第 8 位是否有凶星"}, "selection_group": "ch09-v43-45-malefics-in-same-places-from-chandra-mother-adverse.step-001:malefic-place-from-chandra", "stop_condition": "选中该分支后，缺少以下事实即停止：自月亮（Chandra）起算的第 8 位是否有凶星。"}, {"when": {"fact_key": "本盘月亮（Chandra）落在哪一宫"}, "required_fact_keys": ["自月亮（Chandra）起算的第 4 位是否有凶星"], "branch_condition_logic": {"fact_key": "自月亮（Chandra）起算的第 4 位是否有凶星"}, "selection_group": "ch09-v43-45-malefics-in-same-places-from-chandra-mother-adverse.step-001:malefic-place-from-chandra", "stop_condition": "选中该分支后，缺少以下事实即停止：自月亮（Chandra）起算的第 4 位是否有凶星。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『同样的位置』扩大到第 6、第 8、第 4 位以外。", "不得把『对母亲不利』补成去世等原文没写的具体结果。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘月亮（Chandra）落在哪一宫。
- 缺失即停字段：["本盘月亮（Chandra）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v43-45`｜PDF [24, 25]｜“Malefics in the 6<sup>th</sup> , the 8<sup>th</sup> , or the 4<sup>th</sup> from Surya will bring inauspicious results about the father. Malefics in such places from Chandra will be adverse for the mother.”


## 四路查书计划

### 支持路

- Malefics in such places from Chandra will be adverse for the mother
- 自月亮起第六第八第四位 凶星 母亲不利

### 反例或取消路

- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Evils to Mother (up to Sloka 33)
- Parents

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 母亲用哪颗星看

## 上游问题

- 无

## 停止条件

- 缺少自月亮起算各位次的占据者事实时停止。
- 『同样的位置』所指由同偈上句给出，上句位次未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
