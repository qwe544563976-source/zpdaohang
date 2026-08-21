---
method: ch36-v9-10-kahal-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Kahal Yog：四宫主与木星互为角宫且上升主有力，或四宫主落本星座或入旺并与十宫主同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有掌管人马、统领一方的组合
- 我这个人有没有干劲和胆量

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘四宫主（Bandhu's Lord）是哪颗行星

## 按情况检查的事实

- 四宫主（Bandhu's Lord）与木星（Guru）是否互为角宫
- 上升主（Lagn's Lord）是否有力
- 四宫主（Bandhu's Lord）是否落本星座（own Rāśi）
- 四宫主（Bandhu's Lord）是否入旺
- 四宫主（Bandhu's Lord）是否与十宫主（Karm's Lord）同宫

## 依赖方法

- 无

## 执行步骤

### ch36-v9-10-kahal-yog.step-001

- 动作：先确定四宫主（Bandhu's Lord）是哪颗行星，再核对它与木星（Guru）是否互为角宫、上升主（Lagn's Lord）是否有力，或它是否落本星座或入旺并与十宫主（Karm's Lord）同宫，判定 Kahal Yog 是否成立。
- 适用范围：仅限本命盘 Kahal Yog 的成立判定；原文本句未给出「有力」的判准，也没有时间限定。
- 原文最小意思：四宫主（Bandhu's Lord）与木星（Guru）互为角宫且上升主（Lagn's Lord）有力，或四宫主落本星座（own Rāśi）或入旺星座并与十宫主（Karm's Lord）同宫，则 Kahal Yog 成立。
- 本步骤产出事实：["Kahal Yog 成立判定"]
- 所需事实：["本盘四宫主（Bandhu's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "四宫主（Bandhu's Lord）与木星（Guru）是否互为角宫"}, {"fact_key": "上升主（Lagn's Lord）是否有力"}]}, {"operator": "AND", "operands": [{"fact_key": "四宫主（Bandhu's Lord）是否落本星座（own Rāśi）"}, {"fact_key": "四宫主（Bandhu's Lord）是否与十宫主（Karm's Lord）同宫"}]}, {"operator": "AND", "operands": [{"fact_key": "四宫主（Bandhu's Lord）是否入旺"}, {"fact_key": "四宫主（Bandhu's Lord）是否与十宫主（Karm's Lord）同宫"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, "required_fact_keys": ["四宫主（Bandhu's Lord）与木星（Guru）是否互为角宫", "上升主（Lagn's Lord）是否有力"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "四宫主（Bandhu's Lord）与木星（Guru）是否互为角宫"}, {"fact_key": "上升主（Lagn's Lord）是否有力"}]}, "selection_group": "ch36-v9-10-kahal-yog.step-001:kahal-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫主（Bandhu's Lord）与木星（Guru）是否互为角宫、上升主（Lagn's Lord）是否有力。"}, {"when": {"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, "required_fact_keys": ["四宫主（Bandhu's Lord）是否落本星座（own Rāśi）", "四宫主（Bandhu's Lord）是否与十宫主（Karm's Lord）同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "四宫主（Bandhu's Lord）是否落本星座（own Rāśi）"}, {"fact_key": "四宫主（Bandhu's Lord）是否与十宫主（Karm's Lord）同宫"}]}, "selection_group": "ch36-v9-10-kahal-yog.step-001:kahal-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫主（Bandhu's Lord）是否落本星座（own Rāśi）、四宫主（Bandhu's Lord）是否与十宫主（Karm's Lord）同宫。"}, {"when": {"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, "required_fact_keys": ["四宫主（Bandhu's Lord）是否入旺", "四宫主（Bandhu's Lord）是否与十宫主（Karm's Lord）同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "四宫主（Bandhu's Lord）是否入旺"}, {"fact_key": "四宫主（Bandhu's Lord）是否与十宫主（Karm's Lord）同宫"}]}, "selection_group": "ch36-v9-10-kahal-yog.step-001:kahal-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫主（Bandhu's Lord）是否入旺、四宫主（Bandhu's Lord）是否与十宫主（Karm's Lord）同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文本句没有给出「有力」的判准，不得自行发明力量算法。", "第二种成立方式原文没有再写上升主有力，不得把它补进这一支。", "不得据此推断具体官阶、军队规模或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘四宫主（Bandhu's Lord）是哪颗行星。
- 缺失即停字段：["本盘四宫主（Bandhu's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v9-10`｜PDF [79]｜“Should Bandhu’s Lord and Guru be in mutual Kendras, while Lagn’s Lord is strong, Kahal Yog occurs.”
  - `bphs-97:santhanam:ch36:v9-10`｜PDF [79]｜“Alternatively Bandhu’s Lord, being in his own, or exaltation Rāśi, should be yuti with Karm’s Lord.”

### ch36-v9-10-kahal-yog.step-002

- 动作：在 Kahal Yog 成立时读取干劲、军队与统辖村庄的断语。
- 适用范围：仅限已判定 Kahal Yog 成立的本命盘；原文以 he 立说，未给时间限定。
- 原文最小意思：Kahal Yog 成立时，命主精力充沛、有冒险精神、有魅力，拥有由战车、象、马与步兵组成的完整军队，并会统辖若干村庄。
- 本步骤产出事实：["Kahal Yog 效果断语"]
- 所需事实：["Kahal Yog 成立判定"]
- 条件关系：{"fact_key": "Kahal Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文写 a few villages（若干村庄），不得换算成具体数目或指定地域。", "不得据此推断寿命、婚姻或子女。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Kahal Yog 成立判定。
- 缺失即停字段：["Kahal Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v9-10`｜PDF [79]｜“Kahal Yog occurs”
  - `bphs-97:santhanam:ch36:v9-10`｜PDF [79]｜“In effect the native will be energetic, adventurous, charming, endowed with a complete Army, consisting of chariots, elephants, horses and infantry and he will Lord over a few villages.”


## 四路查书计划

### 支持路

- Should Bandhu’s Lord and Guru be in mutual Kendras, while Lagn’s Lord is strong, Kahal Yog occurs
- Alternatively Bandhu’s Lord, being in his own, or exaltation Rāśi, should be yuti with Karm’s Lord
- 四宫主 木星 互为角宫 Kahal Yog

### 反例或取消路

- If Lagn’s Lord is yuti with the Lord of Ari, Randhr, or Vyaya Bhava, or with Shani and, if Lagn’s Lord is devoid of a Drishti from a benefic, the native will be penniless
- If the Lords of a Kendr, or a Kon own simultaneously an evil Bhava, he does not cause a Raj Yog by mere relations stipulated
- 上升主无力 破格

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula

### 判断方法路

- Indications of Bandhu Bhava. Conveyances, relatives, mother, happiness, treasure, lands and buildings are to be consulted through Bandhu Bhava
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少四宫主身份事实时停止。
- 两种成立方式所需的事实都缺失时停止。
- 「有力」的判准由排盘窗口定义，未给出取值时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
