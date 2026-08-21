---
method: ch36-v5-6-amal-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Amal Yog：从上升或月亮起算的第十宫内只有吉星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子名声怎么样
- 我在外面能不能受人尊敬

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 从上升宫（Lagna）起算的第十宫是否只被吉星占据
- 从月亮（Chandra）起算的第十宫是否只被吉星占据

## 依赖方法

- 无

## 执行步骤

### ch36-v5-6-amal-yog.step-001

- 动作：先取本盘的吉星名册，再核对从上升宫（Lagna）起算的第十宫、从月亮（Chandra）起算的第十宫内是否只有吉星，判定 Amal Yog 是否成立。
- 适用范围：仅限本命盘 Amal Yog 的成立判定；原文写 exclusively a benefic（只有吉星），未给出吉星的判准，也没有时间限定。
- 原文最小意思：从上升宫（Lagna）起算的第十宫内只有吉星，或从月亮（Chandra）起算的第十宫内只有吉星，则 Amal Yog 成立。
- 本步骤产出事实：["Amal Yog 成立判定"]
- 所需事实：["本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"operator": "OR", "operands": [{"fact_key": "从上升宫（Lagna）起算的第十宫是否只被吉星占据"}, {"fact_key": "从月亮（Chandra）起算的第十宫是否只被吉星占据"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["从上升宫（Lagna）起算的第十宫是否只被吉星占据"], "branch_condition_logic": {"fact_key": "从上升宫（Lagna）起算的第十宫是否只被吉星占据"}, "selection_group": "ch36-v5-6-amal-yog.step-001:tenth-reference", "stop_condition": "选中该分支后，缺少以下事实即停止：从上升宫（Lagna）起算的第十宫是否只被吉星占据。"}, {"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["从月亮（Chandra）起算的第十宫是否只被吉星占据"], "branch_condition_logic": {"fact_key": "从月亮（Chandra）起算的第十宫是否只被吉星占据"}, "selection_group": "ch36-v5-6-amal-yog.step-001:tenth-reference", "stop_condition": "选中该分支后，缺少以下事实即停止：从月亮（Chandra）起算的第十宫是否只被吉星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 exclusively（只有吉星）放宽成「有吉星即可」。", "原文只写第十宫这一处，不得改到别的宫位起算。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v5-6`｜PDF [79]｜“If there be exclusively a benefic in the 10<sup>th</sup> from Lagna, or Chandra, Amal Yog exists.”

### ch36-v5-6-amal-yog.step-002

- 动作：在 Amal Yog 成立时读取名声与相关效果的断语。
- 适用范围：仅限已判定 Amal Yog 成立的本命盘；原文以「持续到月亮与群星存在为止」形容名声的久远，未给具体年数。
- 原文最小意思：Amal Yog 成立时，给予名声，持续到月亮（Chandra）与群星存在为止，并使命主受国王尊敬、享有丰盛的享乐、乐善好施、亲近亲属、乐于助人、虔诚而有德行。
- 本步骤产出事实：["Amal Yog 名声效果断语"]
- 所需事实：["Amal Yog 成立判定"]
- 条件关系：{"fact_key": "Amal Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「持续到月亮与群星存在为止」换算成具体年数或某段大运。", "不得据此推断财富数额、官职或寿命。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Amal Yog 成立判定。
- 缺失即停字段：["Amal Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v5-6`｜PDF [79]｜“Amal Yog exists”
  - `bphs-97:santhanam:ch36:v5-6`｜PDF [79]｜“Amal Yog will confer fame, lasting till Chandra and stars exist and will make the native honoured by the king, enjoy abundant pleasures, charitable, fond of relatives, helpful to others, pious and virtuous.”


## 四路查书计划

### 支持路

- If there be exclusively a benefic in the 10<sup>th</sup> from Lagna, or Chandra, Amal Yog exists
- Amal Yog will confer fame, lasting till Chandra and stars exist
- 第十宫只有吉星 Amal Yog 名声

### 反例或取消路

- If inauspicious Bhavas are occupied by benefics, while auspicious Bhavas are occupied by malefics, the native will be indigent
- If malefics, excepting the Lords of Karm and Dharm Bhava, happen to be in Lagna, associated with, or receiving a Drishti from Marak Grahas, one will become penniless
- 十宫有凶星 名声受损

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu
- Guru and Shukra are benefics, while Chandra is mediocre in benefice and Budh is neutral
- Benefics, owning Kendras, will not give benefic effects, while malefics, owning Kendras, will not remain inauspicious

### 判断方法路

- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少本盘吉星名册事实时停止。
- 从上升起与从月亮起两种第十宫的占据事实都缺失时停止。
- 原文本句未给出吉星判准，吉星名册未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
