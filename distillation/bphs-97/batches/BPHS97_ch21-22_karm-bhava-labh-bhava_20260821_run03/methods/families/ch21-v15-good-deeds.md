---
method: ch21-v15-good-deeds
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 喜好善行：十宫主与上升主同落上升宫、月亮落角宫或三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会热衷于做善事
- 我做事的动机是什么样的

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否落上升宫（Lagna）
- 上升主（Lagn's Lord）是否落上升宫（Lagna）

## 按情况检查的事实

- 月亮（Chandra）是否落角宫
- 月亮（Chandra）是否落三角宫

## 依赖方法

- 无

## 执行步骤

### ch21-v15-good-deeds.step-001

- 动作：先核对十宫主（Karm's Lord）与上升主（Lagn's Lord）是否同落上升宫（Lagna），再核对月亮（Chandra）落角宫还是三角宫。
- 适用范围：仅限本命盘十宫（Karm）善行倾向主题；原文里两颗宫主同落上升宫是合取前提，月亮的角宫与三角宫是一组备选；原文未给时间限定。
- 原文最小意思：十宫主与上升主同落上升宫、且月亮落角宫或三角宫时，命主喜好善行。
- 本步骤产出事实：["十宫主与上升主同落上升宫喜好善行判定"]
- 所需事实：["十宫主（Karm's Lord）是否落上升宫（Lagna）", "上升主（Lagn's Lord）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落上升宫（Lagna）"}, {"fact_key": "上升主（Lagn's Lord）是否落上升宫（Lagna）"}]}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否落角宫"}, {"fact_key": "月亮（Chandra）是否落三角宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落上升宫（Lagna）"}, {"fact_key": "上升主（Lagn's Lord）是否落上升宫（Lagna）"}]}, "required_fact_keys": ["月亮（Chandra）是否落角宫"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落角宫"}, "selection_group": "ch21-v15-good-deeds.step-001:chandra-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落上升宫（Lagna）"}, {"fact_key": "上升主（Lagn's Lord）是否落上升宫（Lagna）"}]}, "required_fact_keys": ["月亮（Chandra）是否落三角宫"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落三角宫"}, "selection_group": "ch21-v15-good-deeds.step-001:chandra-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断善行的种类、规模或应期。", "不得把两颗宫主同落上升宫的合取拆成任一颗单独成立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否落上升宫（Lagna）、上升主（Lagn's Lord）是否落上升宫（Lagna）。
- 缺失即停字段：["十宫主（Karm's Lord）是否落上升宫（Lagna）", "上升主（Lagn's Lord）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v15`｜PDF [39]｜“Should Karm’s Lord be in Lagn along with Lagn’s Lord, as Chandra is in an angle, or in a trine, the native will be interested in good deeds.”


## 四路查书计划

### 支持路

- Should Karm’s Lord be in Lagn along with Lagn’s Lord, as Chandra is in an angle, or in a trine, the native will be interested in good deeds
- 十宫主落上升宫 上升主落上升宫 月亮落角宫 三角宫 善行

### 反例或取消路

- One will indulge in bad acts, if Karm’s Lord is in Randhr Bhava, while Randhr’s Lord is in Karm Bhava with a malefic
- Should Karm and Labh Bhava be both occupied by malefics, the native will indulge only in bad deeds and will defile his own men

### 适用边界路

- Kendras, Konas etc. defined. O Maitreya, listen to other matters, which I am explaining. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava

### 判断方法路

- If Karm’s Lord is strong and in exaltation, or in its own Rāśi/Navāńś, the native will derive extreme paternal happiness, will enjoy fame and will perform good deeds
- 判断十宫（Karm）善行倾向应检查哪些行星的落宫

## 上游问题

- 无

## 停止条件

- 缺少十宫主落宫事实时停止。
- 缺少上升主落宫事实时停止。
- 月亮落角宫、落三角宫两个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
