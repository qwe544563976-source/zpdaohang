---
method: ch22-v11-labh-lord-afflicted-no-gains
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 纵然多方努力也没有收获：十一宫主落陷、燃烧，或与凶星同落六宫八宫十二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我为什么努力了也没有进项
- 十一宫主落陷或燃烧会怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘十一宫主（Labh's Lord）是哪颗行星

## 按情况检查的事实

- 十一宫主（Labh's Lord）是否落陷
- 十一宫主（Labh's Lord）是否燃烧
- 十一宫主（Labh's Lord）是否落六宫（Ari）
- 十一宫主（Labh's Lord）是否落八宫（Randhr）
- 十一宫主（Labh's Lord）是否落十二宫（Vyaya）
- 十一宫主（Labh's Lord）是否与凶星同宫

## 依赖方法

- 无

## 执行步骤

### ch22-v11-labh-lord-afflicted-no-gains.step-001

- 动作：先取本盘十一宫主（Labh's Lord）是哪颗行星，再逐个核对它是否落陷、是否燃烧、是否与凶星同落六宫（Ari）、八宫（Randhr）或十二宫（Vyaya）。
- 适用范围：仅限本命盘十一宫（Labh）收获主题；原文三种情形是并列备选，任一成立即可；「与凶星同宫」只挂在六宫、八宫、十二宫这一支，不挂在落陷与燃烧两支；凶星名册按 BPHS 自己的界定取。
- 原文最小意思：十一宫主落陷、燃烧，或与凶星一同落于六宫（Ari）、八宫（Randhr）或十二宫（Vyaya）时，纵然多方努力也没有收获。
- 本步骤产出事实：["十一宫主受损无收获判定"]
- 所需事实：["本盘十一宫主（Labh's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落陷"}, {"fact_key": "十一宫主（Labh's Lord）是否燃烧"}, {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落六宫（Ari）"}, {"fact_key": "十一宫主（Labh's Lord）是否与凶星同宫"}]}, {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落八宫（Randhr）"}, {"fact_key": "十一宫主（Labh's Lord）是否与凶星同宫"}]}, {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落十二宫（Vyaya）"}, {"fact_key": "十一宫主（Labh's Lord）是否与凶星同宫"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落陷"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否落陷"}, "selection_group": "ch22-v11-labh-lord-afflicted-no-gains.step-001:labh-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落陷。"}, {"when": {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否燃烧"], "branch_condition_logic": {"fact_key": "十一宫主（Labh's Lord）是否燃烧"}, "selection_group": "ch22-v11-labh-lord-afflicted-no-gains.step-001:labh-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否燃烧。"}, {"when": {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落六宫（Ari）", "十一宫主（Labh's Lord）是否与凶星同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落六宫（Ari）"}, {"fact_key": "十一宫主（Labh's Lord）是否与凶星同宫"}]}, "selection_group": "ch22-v11-labh-lord-afflicted-no-gains.step-001:labh-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落六宫（Ari）、十一宫主（Labh's Lord）是否与凶星同宫。"}, {"when": {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落八宫（Randhr）", "十一宫主（Labh's Lord）是否与凶星同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落八宫（Randhr）"}, {"fact_key": "十一宫主（Labh's Lord）是否与凶星同宫"}]}, "selection_group": "ch22-v11-labh-lord-afflicted-no-gains.step-001:labh-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落八宫（Randhr）、十一宫主（Labh's Lord）是否与凶星同宫。"}, {"when": {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}, "required_fact_keys": ["十一宫主（Labh's Lord）是否落十二宫（Vyaya）", "十一宫主（Labh's Lord）是否与凶星同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落十二宫（Vyaya）"}, {"fact_key": "十一宫主（Labh's Lord）是否与凶星同宫"}]}, "selection_group": "ch22-v11-labh-lord-afflicted-no-gains.step-001:labh-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：十一宫主（Labh's Lord）是否落十二宫（Vyaya）、十一宫主（Labh's Lord）是否与凶星同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「与凶星同宫」加到落陷与燃烧两支上：原文只把它挂在六宫、八宫、十二宫这一支。", "不得据此推断贫穷程度、负债或收获中断的年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘十一宫主（Labh's Lord）是哪颗行星。
- 缺失即停字段：["本盘十一宫主（Labh's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch22:v11`｜PDF [40]｜“There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic.”


## 四路查书计划

### 支持路

- There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic
- 十一宫主（Labh's Lord）落陷 燃烧 落六宫 八宫 十二宫 与凶星同宫 没有收获

### 反例或取消路

- Similarly, if Labh’s Lord is exalted, though in combustion there will be many gains
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava

### 判断方法路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic
- If Labh’s Lord is in Labh Bhava, the native will gain in all his undertakings, while his learning and happiness will be on the increase day by day

## 上游问题

- 无

## 停止条件

- 缺少十一宫主身份事实时停止。
- 落陷、燃烧、与凶星同落六宫八宫十二宫三支事实全缺时停止。
- 凶星名册未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
