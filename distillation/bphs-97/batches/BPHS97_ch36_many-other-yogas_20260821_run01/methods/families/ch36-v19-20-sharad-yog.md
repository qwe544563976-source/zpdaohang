---
method: ch36-v19-20-sharad-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Sharad Yog：十宫主落五宫、水星落角宫且有力的太阳落狮子座，或木星与水星之一落月亮起的三角宫且火星落十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子财富、配偶和子女怎么样
- 我有没有受上位者赏识的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘十宫主（Karm's Lord）是哪颗行星
- 本盘月亮（Chandra）落在哪一宫

## 按情况检查的事实

- 十宫主（Karm's Lord）是否落五宫（Putr）
- 水星（Budh）是否落角宫
- 太阳（Surya）是否有力
- 太阳（Surya）是否落狮子座（Simh）
- 木星（Guru）是否落从月亮（Chandra）起算的三角宫
- 水星（Budh）是否落从月亮（Chandra）起算的三角宫
- 火星（Mangal）是否落十一宫（Labh）

## 依赖方法

- 无

## 执行步骤

### ch36-v19-20-sharad-yog.step-001

- 动作：先确定十宫主（Karm's Lord）是哪颗行星、月亮（Chandra）落在哪一宫，再核对十宫主是否落五宫（Putr）、水星（Budh）是否落角宫、有力的太阳（Surya）是否落狮子座（Simh），或木星（Guru）与水星之一是否落月亮起的三角宫且火星（Mangal）是否落十一宫（Labh），判定 Sharad Yog 是否成立。
- 适用范围：仅限本命盘 Sharad Yog 的成立判定；原文本句未给出「有力」的判准，也没有时间限定。
- 原文最小意思：十宫主（Karm's Lord）落五宫（Putr）、水星（Budh）落角宫且有力的太阳（Surya）落狮子座（Simh），或木星（Guru）或水星落月亮（Chandra）起的三角宫且火星（Mangal）落十一宫（Labh），则 Sharad Yog 成立。
- 本步骤产出事实：["Sharad Yog 成立判定"]
- 所需事实：["本盘十宫主（Karm's Lord）是哪颗行星", "本盘月亮（Chandra）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘月亮（Chandra）落在哪一宫"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落五宫（Putr）"}, {"fact_key": "水星（Budh）是否落角宫"}, {"fact_key": "太阳（Surya）是否有力"}, {"fact_key": "太阳（Surya）是否落狮子座（Simh）"}]}, {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落从月亮（Chandra）起算的三角宫"}, {"fact_key": "火星（Mangal）是否落十一宫（Labh）"}]}, {"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落从月亮（Chandra）起算的三角宫"}, {"fact_key": "火星（Mangal）是否落十一宫（Labh）"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘月亮（Chandra）落在哪一宫"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否落五宫（Putr）", "水星（Budh）是否落角宫", "太阳（Surya）是否有力", "太阳（Surya）是否落狮子座（Simh）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落五宫（Putr）"}, {"fact_key": "水星（Budh）是否落角宫"}, {"fact_key": "太阳（Surya）是否有力"}, {"fact_key": "太阳（Surya）是否落狮子座（Simh）"}]}, "selection_group": "ch36-v19-20-sharad-yog.step-001:sharad-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否落五宫（Putr）、水星（Budh）是否落角宫、太阳（Surya）是否有力、太阳（Surya）是否落狮子座（Simh）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘月亮（Chandra）落在哪一宫"}]}, "required_fact_keys": ["木星（Guru）是否落从月亮（Chandra）起算的三角宫", "火星（Mangal）是否落十一宫（Labh）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落从月亮（Chandra）起算的三角宫"}, {"fact_key": "火星（Mangal）是否落十一宫（Labh）"}]}, "selection_group": "ch36-v19-20-sharad-yog.step-001:sharad-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落从月亮（Chandra）起算的三角宫、火星（Mangal）是否落十一宫（Labh）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘月亮（Chandra）落在哪一宫"}]}, "required_fact_keys": ["水星（Budh）是否落从月亮（Chandra）起算的三角宫", "火星（Mangal）是否落十一宫（Labh）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落从月亮（Chandra）起算的三角宫"}, {"fact_key": "火星（Mangal）是否落十一宫（Labh）"}]}, "selection_group": "ch36-v19-20-sharad-yog.step-001:sharad-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落从月亮（Chandra）起算的三角宫、火星（Mangal）是否落十一宫（Labh）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文本句没有给出「有力」的判准，不得自行发明力量算法。", "第二种成立方式的三角宫原文从月亮（Chandra）起算，不得改从上升宫起算。", "第一种成立方式的三项条件是并列必需，不得只取其中一两项。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘十宫主（Karm's Lord）是哪颗行星、本盘月亮（Chandra）落在哪一宫。
- 缺失即停字段：["本盘十宫主（Karm's Lord）是哪颗行星", "本盘月亮（Chandra）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v19-20`｜PDF [80]｜“Should Karm’s Lord be in Putr Bhava, while Budh is in a Kendr, as Surya with strength is in Simh, Sharad Yog is formed.”
  - `bphs-97:santhanam:ch36:v19-20`｜PDF [80]｜“This will again be obtained, if Guru, or Budh is in a Kon to Chandra, while Mangal is in Labh Bhava.”

### ch36-v19-20-sharad-yog.step-002

- 动作：在 Sharad Yog 成立时读取财富、家室、学识与受赏识的断语。
- 适用范围：仅限已判定 Sharad Yog 成立的本命盘；原文断语对两种成立方式一并适用，未给时间限定。
- 原文最小意思：生于两种 Sharad Yog 中任一种者会得到财富、配偶与儿子，并且快乐、博学、为国王所喜爱、虔诚而有德行。
- 本步骤产出事实：["Sharad Yog 效果断语"]
- 所需事实：["Sharad Yog 成立判定"]
- 条件关系：{"fact_key": "Sharad Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文未给子女数目，不得据此推断有几个儿子。", "不得把「为国王所喜爱」推广成一定得到官职或封赏。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Sharad Yog 成立判定。
- 缺失即停字段：["Sharad Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v19-20`｜PDF [80]｜“One born in either kind of Yog will obtain wealth, spouse and sons, be happy, scholarly, dear to the king, pious and virtuous.”


## 四路查书计划

### 支持路

- Should Karm’s Lord be in Putr Bhava, while Budh is in a Kendr, as Surya with strength is in Simh, Sharad Yog is formed
- This will again be obtained, if Guru, or Budh is in a Kon to Chandra, while Mangal is in Labh Bhava
- 十宫主落五宫 水星落角宫 太阳落狮子 Sharad Yog

### 反例或取消路

- Excluding Surya, should there be no Grah with Chandra, or in the 2nd and/or 12th from Chandra, or in a Kendr from Lagna, Kema Drum Yog is formed
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- If inauspicious Bhavas are occupied by benefics, while auspicious Bhavas are occupied by malefics, the native will be indigent

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula

### 判断方法路

- Indications of Putr Bhava
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少十宫主身份或月亮落宫事实时停止。
- 两种成立方式所需的事实都缺失时停止。
- 「有力」的判准由排盘窗口定义，未给出取值时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
