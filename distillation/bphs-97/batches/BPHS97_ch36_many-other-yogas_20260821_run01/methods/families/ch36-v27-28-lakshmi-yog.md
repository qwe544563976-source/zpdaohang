---
method: ch36-v27-28-lakshmi-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Lakshmi Yog：九宫主落角宫且据根本三角、本星座或入旺，上升主有力

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子的福气和财富怎么样
- 我的社会地位能到什么程度

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否落角宫（Kendr）
- 上升主（Lagn's Lord）是否有力

## 按情况检查的事实

- 九宫主（Dharm's Lord）所落星座是否为其根本三角星座（Mooltrikon Rāśi）
- 九宫主（Dharm's Lord）所落星座是否为其本星座（own Rāśi）
- 九宫主（Dharm's Lord）是否入旺

## 依赖方法

- 无

## 执行步骤

### ch36-v27-28-lakshmi-yog.step-001

- 动作：先核对九宫主（Dharm's Lord）是否落角宫（Kendr）、上升主（Lagn's Lord）是否有力，再核对九宫主该处是其根本三角星座（Mooltrikon Rāśi）、本星座（own Rāśi）还是入旺。
- 适用范围：仅限本命盘 Lakshmi Yog 的成立与效果；原文把三种尊贵与角宫写在同一句里，「有力」的判准原文本句未给，需另查本书的力量章节。原文未给时间限定。
- 原文最小意思：九宫主（Dharm's Lord）落角宫（Kendr），且落在其根本三角星座（Mooltrikon Rāśi）、其本星座（own Rāśi）或入旺，同时上升主（Lagn's Lord）有力时，成立 Lakshmi Yog，命主会有魅力、有德、地位如王、子女众多、财富丰厚，并会有名、道德高尚。
- 本步骤产出事实：["Lakshmi Yog 成立判定"]
- 所需事实：["九宫主（Dharm's Lord）是否落角宫（Kendr）", "上升主（Lagn's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落角宫（Kendr）"}, {"fact_key": "上升主（Lagn's Lord）是否有力"}]}, {"operator": "OR", "operands": [{"fact_key": "九宫主（Dharm's Lord）所落星座是否为其根本三角星座（Mooltrikon Rāśi）"}, {"fact_key": "九宫主（Dharm's Lord）所落星座是否为其本星座（own Rāśi）"}, {"fact_key": "九宫主（Dharm's Lord）是否入旺"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落角宫（Kendr）"}, {"fact_key": "上升主（Lagn's Lord）是否有力"}]}, "required_fact_keys": ["九宫主（Dharm's Lord）所落星座是否为其根本三角星座（Mooltrikon Rāśi）"], "branch_condition_logic": {"fact_key": "九宫主（Dharm's Lord）所落星座是否为其根本三角星座（Mooltrikon Rāśi）"}, "selection_group": "ch36-v27-28-lakshmi-yog.step-001:dharm-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫主（Dharm's Lord）所落星座是否为其根本三角星座（Mooltrikon Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落角宫（Kendr）"}, {"fact_key": "上升主（Lagn's Lord）是否有力"}]}, "required_fact_keys": ["九宫主（Dharm's Lord）所落星座是否为其本星座（own Rāśi）"], "branch_condition_logic": {"fact_key": "九宫主（Dharm's Lord）所落星座是否为其本星座（own Rāśi）"}, "selection_group": "ch36-v27-28-lakshmi-yog.step-001:dharm-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫主（Dharm's Lord）所落星座是否为其本星座（own Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落角宫（Kendr）"}, {"fact_key": "上升主（Lagn's Lord）是否有力"}]}, "required_fact_keys": ["九宫主（Dharm's Lord）是否入旺"], "branch_condition_logic": {"fact_key": "九宫主（Dharm's Lord）是否入旺"}, "selection_group": "ch36-v27-28-lakshmi-yog.step-001:dharm-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫主（Dharm's Lord）是否入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断子女的确切数目或财富数额。", "原文本句没有给出「有力」的判准，不得自行发明力量算法。", "不得把九宫主的尊贵条件挪到上升主身上，也不得把「有力」改写成入旺。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否落角宫（Kendr）、上升主（Lagn's Lord）是否有力。
- 缺失即停字段：["九宫主（Dharm's Lord）是否落角宫（Kendr）", "上升主（Lagn's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v27-28`｜PDF [80]｜“If Dharm’s Lord is in a Kendr identical with his Mooltrikon Rāśi, or own Rāśi, or in exaltation, while Lagn’s Lord is endowed with strength, Lakshmi Yog occurs. The native with Lakshmi Yog will be charming, virtuous, kingly in status, endowed with many sons and abundant wealth. He will be famous and of high moral merits.”


## 四路查书计划

### 支持路

- Lakshmi Yog. If Dharm’s Lord is in a Kendr identical with his Mooltrikon Rāśi, or own Rāśi, or in exaltation
- Lakshmi Yog 九宫主落角宫 根本三角 本星座 入旺 上升主有力

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- If Lagn’s Lord is yuti with the Lord of Ari, Randhr, or Vyaya Bhava, or with Shani and, if Lagn’s Lord is devoid of a Drishti from a benefic, the native will be penniless

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Additional Dignities. In Simh the first 20 degrees are Surya’s Mooltrikon, while the rest is his own Bhava
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- Ratio of Effects. A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

## 上游问题

- 无

## 停止条件

- 缺少九宫主落角宫事实或上升主力量事实时停止。
- 「有力」的判准由排盘窗口按本书 ch27 的 Shad Bal 定义，未取到取值时停止。
- 命中九宫主尊贵分支后，缺少该分支对应的根本三角、本星座或入旺事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
