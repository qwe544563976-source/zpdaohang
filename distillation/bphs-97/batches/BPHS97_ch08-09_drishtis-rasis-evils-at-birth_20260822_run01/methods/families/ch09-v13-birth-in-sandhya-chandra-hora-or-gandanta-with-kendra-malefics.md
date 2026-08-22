---
method: ch09-v13-birth-in-sandhya-chandra-hora-or-gandanta-with-kendra-malefics
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 生于晨昏交界、月亮的 Horā 或 Gandanta，且月亮与凶星占据自上升起的角宫：早亡

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 出生时辰不好会怎样
- 生在晨昏交界有什么凶
- Gandanta 出生怎么断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否落自上升（Lagn）起算的角宫（Kendra）
- 是否有凶星落自上升（Lagn）起算的角宫（Kendra）

## 按情况检查的事实

- 本盘出生是否在晨交界（morning junction）
- 本盘出生是否在昏交界（evening junction）
- 本盘出生是否在月亮（Chandra）所主的 Horā 内
- 本盘出生是否在 Gandanta 内

## 依赖方法

- 无

## 执行步骤

### ch09-v13-birth-in-sandhya-chandra-hora-or-gandanta-with-kendra-malefics.step-001

- 动作：核对出生时辰是否落在晨昏交界、月亮所主的 Horā 或 Gandanta，并核对月亮与凶星是否占据自上升起算的角宫。
- 适用范围：仅限出生时辰与角宫占据的合断；晨昏交界的界定见紧接的下一偈（Definition of Sandhya）。
- 原文最小意思：出生在晨交界或昏交界、或在月亮（Chandra）所主的 Horā、或在 Gandanta，同时月亮与凶星占据自上升（Lagn）起算的角宫（Kendras）时，会有早亡。
- 本步骤产出事实：["出生时辰兼角宫凶象的早亡判定"]
- 所需事实：["月亮（Chandra）是否落自上升（Lagn）起算的角宫（Kendra）", "是否有凶星落自上升（Lagn）起算的角宫（Kendra）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落自上升（Lagn）起算的角宫（Kendra）"}, {"fact_key": "是否有凶星落自上升（Lagn）起算的角宫（Kendra）"}]}, {"operator": "OR", "operands": [{"fact_key": "本盘出生是否在晨交界（morning junction）"}, {"fact_key": "本盘出生是否在昏交界（evening junction）"}, {"fact_key": "本盘出生是否在月亮（Chandra）所主的 Horā 内"}, {"fact_key": "本盘出生是否在 Gandanta 内"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落自上升（Lagn）起算的角宫（Kendra）"}, {"fact_key": "是否有凶星落自上升（Lagn）起算的角宫（Kendra）"}]}, "required_fact_keys": ["本盘出生是否在晨交界（morning junction）"], "branch_condition_logic": {"fact_key": "本盘出生是否在晨交界（morning junction）"}, "selection_group": "ch09-v13-birth-in-sandhya-chandra-hora-or-gandanta-with-kendra-malefics.step-001:birth-time", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘出生是否在晨交界（morning junction）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落自上升（Lagn）起算的角宫（Kendra）"}, {"fact_key": "是否有凶星落自上升（Lagn）起算的角宫（Kendra）"}]}, "required_fact_keys": ["本盘出生是否在昏交界（evening junction）"], "branch_condition_logic": {"fact_key": "本盘出生是否在昏交界（evening junction）"}, "selection_group": "ch09-v13-birth-in-sandhya-chandra-hora-or-gandanta-with-kendra-malefics.step-001:birth-time", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘出生是否在昏交界（evening junction）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落自上升（Lagn）起算的角宫（Kendra）"}, {"fact_key": "是否有凶星落自上升（Lagn）起算的角宫（Kendra）"}]}, "required_fact_keys": ["本盘出生是否在月亮（Chandra）所主的 Horā 内"], "branch_condition_logic": {"fact_key": "本盘出生是否在月亮（Chandra）所主的 Horā 内"}, "selection_group": "ch09-v13-birth-in-sandhya-chandra-hora-or-gandanta-with-kendra-malefics.step-001:birth-time", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘出生是否在月亮（Chandra）所主的 Horā 内。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落自上升（Lagn）起算的角宫（Kendra）"}, {"fact_key": "是否有凶星落自上升（Lagn）起算的角宫（Kendra）"}]}, "required_fact_keys": ["本盘出生是否在 Gandanta 内"], "branch_condition_logic": {"fact_key": "本盘出生是否在 Gandanta 内"}, "selection_group": "ch09-v13-birth-in-sandhya-chandra-hora-or-gandanta-with-kendra-malefics.step-001:birth-time", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘出生是否在 Gandanta 内。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『早亡』补成具体年岁。", "不得省略月亮与凶星占据角宫这一前提——只有出生时辰不构成本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否落自上升（Lagn）起算的角宫（Kendra）、是否有凶星落自上升（Lagn）起算的角宫（Kendra）。
- 缺失即停字段：["月亮（Chandra）是否落自上升（Lagn）起算的角宫（Kendra）", "是否有凶星落自上升（Lagn）起算的角宫（Kendra）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v13`｜PDF [23]｜“Early death will come to pass, if there be a birth in the morning, or evening junctions, or in a Hora, ruled by Chandra, or in Gandanta, while Chandra and malefics occupy Kendras from Lagn.”


## 四路查书计划

### 支持路

- Early death will come to pass, if there be a birth in the morning, or evening junctions, or in a Hora, ruled by Chandra, or in Gandanta
- 晨昏交界出生 月亮 Horā Gandanta 早亡

### 反例或取消路

- All evils are destroyed, if a benefic drishties Lagn of one born during the night in the bright half.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- 3 Ghatis before the sight of the semi disc (half) of the rising Surya and a similar duration, following Surya’s set, are called, as morning twilight and evening twilight, respectively.
- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- Evils at Birth
- Definition of Sandhya
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 晨昏交界怎么定

## 上游问题

- 无

## 停止条件

- 缺少出生时刻与日出日落时刻时停止（晨昏交界的界定见下一偈）。
- 缺少自上升起算角宫的占据事实时停止。
- Gandanta 的界定原文本偈未给，该事实取不到值时该分支停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
