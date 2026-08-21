---
method: ch36-v11-12-chamar-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Chamar Yog：上升主在角宫入旺并受木星相照，或上升、九宫、十宫、七宫之一内有两颗吉星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有当官或受权贵尊敬的组合
- 我这辈子学问和口才怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）是哪颗行星
- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 上升主（Lagn's Lord）是否入旺
- 上升主（Lagn's Lord）是否落角宫
- 上升主（Lagn's Lord）是否被木星（Guru）相照
- 上升宫（Lagna）内是否有两颗吉星
- 九宫（Dharm）内是否有两颗吉星
- 十宫（Karm）内是否有两颗吉星
- 七宫（Yuvati）内是否有两颗吉星

## 依赖方法

- 无

## 执行步骤

### ch36-v11-12-chamar-yog.step-001

- 动作：先确定上升主（Lagn's Lord）是哪颗行星并取吉星名册，再核对上升主是否在角宫入旺且受木星（Guru）相照，或上升宫（Lagna）、九宫（Dharm）、十宫（Karm）、七宫（Yuvati）之一内是否有两颗吉星，判定 Chamar Yog 是否成立。
- 适用范围：仅限本命盘 Chamar Yog 的成立判定；原文写 two benefics are in Lagna, or Dharm, or Karm, or Yuvati Bhava，本步按「同一宫内有两颗吉星」取值；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：上升主（Lagn's Lord）在角宫入旺并受木星（Guru）相照，或上升宫（Lagna）、九宫（Dharm）、十宫（Karm）、七宫（Yuvati）之一内有两颗吉星，则 Chamar Yog 成立。
- 本步骤产出事实：["Chamar Yog 成立判定"]
- 所需事实：["本盘上升主（Lagn's Lord）是哪颗行星", "本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否入旺"}, {"fact_key": "上升主（Lagn's Lord）是否落角宫"}, {"fact_key": "上升主（Lagn's Lord）是否被木星（Guru）相照"}]}, {"fact_key": "上升宫（Lagna）内是否有两颗吉星"}, {"fact_key": "九宫（Dharm）内是否有两颗吉星"}, {"fact_key": "十宫（Karm）内是否有两颗吉星"}, {"fact_key": "七宫（Yuvati）内是否有两颗吉星"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否入旺", "上升主（Lagn's Lord）是否落角宫", "上升主（Lagn's Lord）是否被木星（Guru）相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否入旺"}, {"fact_key": "上升主（Lagn's Lord）是否落角宫"}, {"fact_key": "上升主（Lagn's Lord）是否被木星（Guru）相照"}]}, "selection_group": "ch36-v11-12-chamar-yog.step-001:chamar-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否入旺、上升主（Lagn's Lord）是否落角宫、上升主（Lagn's Lord）是否被木星（Guru）相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["上升宫（Lagna）内是否有两颗吉星"], "branch_condition_logic": {"fact_key": "上升宫（Lagna）内是否有两颗吉星"}, "selection_group": "ch36-v11-12-chamar-yog.step-001:chamar-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升宫（Lagna）内是否有两颗吉星。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["九宫（Dharm）内是否有两颗吉星"], "branch_condition_logic": {"fact_key": "九宫（Dharm）内是否有两颗吉星"}, "selection_group": "ch36-v11-12-chamar-yog.step-001:chamar-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫（Dharm）内是否有两颗吉星。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["十宫（Karm）内是否有两颗吉星"], "branch_condition_logic": {"fact_key": "十宫（Karm）内是否有两颗吉星"}, "selection_group": "ch36-v11-12-chamar-yog.step-001:chamar-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫（Karm）内是否有两颗吉星。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}, "required_fact_keys": ["七宫（Yuvati）内是否有两颗吉星"], "branch_condition_logic": {"fact_key": "七宫（Yuvati）内是否有两颗吉星"}, "selection_group": "ch36-v11-12-chamar-yog.step-001:chamar-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫（Yuvati）内是否有两颗吉星。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文第二种成立方式写的是两颗吉星，不得放宽成一颗或不限颗数。", "原文只列上升宫、九宫、十宫、七宫四处，不得把两颗吉星的条件挪到别的宫位。", "第一种成立方式的相照者原文限定为木星（Guru），不得换成别的吉星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）是哪颗行星、本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘上升主（Lagn's Lord）是哪颗行星", "本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v11-12`｜PDF [79]｜“If Lagn’s Lord is exalted in a Kendr and receives a Drishti from Guru, Chamar Yog is formed.”
  - `bphs-97:santhanam:ch36:v11-12`｜PDF [79]｜“This Yog also occurs, if two benefics are in Lagna, or Dharm, or Karm, or Yuvati Bhava.”

### ch36-v11-12-chamar-yog.step-002

- 动作：在 Chamar Yog 成立时读取地位、寿数、学问与技艺的断语。
- 适用范围：仅限已判定 Chamar Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：Chamar Yog 的效果是：命主会成为国王，或受国王尊敬，长寿、博学、能言善辩，并精通一切技艺。
- 本步骤产出事实：["Chamar Yog 效果断语"]
- 所需事实：["Chamar Yog 成立判定"]
- 条件关系：{"fact_key": "Chamar Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文把「成为国王」与「受国王尊敬」并列写在结果里，不得据此断定必属其中哪一种。", "「长寿」不得换算成具体年数。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Chamar Yog 成立判定。
- 缺失即停字段：["Chamar Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v11-12`｜PDF [79]｜“The effects of Chamar Yog are: the native will be a king, or honoured by the king, long lived, scholarly, eloquent and versed in all arts.”


## 四路查书计划

### 支持路

- If Lagn’s Lord is exalted in a Kendr and receives a Drishti from Guru, Chamar Yog is formed
- This Yog also occurs, if two benefics are in Lagna, or Dharm, or Karm, or Yuvati Bhava
- 上升主入旺角宫 木星相照 Chamar Yog

### 反例或取消路

- If the Lords of a Kendr, or a Kon own simultaneously an evil Bhava, he does not cause a Raj Yog by mere relations stipulated
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- Lordship of Kendr. It has been said, that a malefic, owning a Kendr, will become auspicious, which is true, only when it simultaneously Lords over a Kon

### 适用边界路

- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula
- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu

### 判断方法路

- Evaluation of the Drishtis of the Grahas. Deduct the longitude of the Grah (or Bhava), that receives a Drishti, from that of the Grah, which gives the Drishti
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少上升主身份或吉星名册事实时停止。
- 上升主入旺、落角宫、受木星相照三项与四处两颗吉星事实全部缺失时停止。
- 原文本句未给出吉星判准，吉星名册未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
