---
method: ch36-v13-14-shankh-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Shankh Yog：上升主有力且五宫主与六宫主互为角宫，或上升主与十宫主同落动星座且九宫主有力

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子财富、配偶和子女怎么样
- 我的寿数和福分如何

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）是哪颗行星

## 按情况检查的事实

- 上升主（Lagn's Lord）是否有力
- 五宫主（Putr's Lord）与六宫主（Ari's Lord）是否互为角宫
- 上升主（Lagn's Lord）是否与十宫主（Karm's Lord）同落动星座（Movable Rāśi）
- 九宫主（Dharm's Lord）是否有力

## 依赖方法

- 无

## 执行步骤

### ch36-v13-14-shankh-yog.step-001

- 动作：先确定上升主（Lagn's Lord）是哪颗行星，再核对它是否有力且五宫主（Putr's Lord）与六宫主（Ari's Lord）互为角宫，或它是否与十宫主（Karm's Lord）一同落动星座且九宫主（Dharm's Lord）有力，判定 Shankh Yog 是否成立。
- 适用范围：仅限本命盘 Shankh Yog 的成立判定；原文本句未给出「有力」的判准；原文写 Lagn’s Lord along with Karm’s Lord is in a Movable Rāśi，本步按 along with 的字面取值（两者一同落于动星座）；原文未给时间限定。
- 原文最小意思：上升主（Lagn's Lord）有力且五宫主（Putr's Lord）与六宫主（Ari's Lord）互为角宫，或上升主与十宫主（Karm's Lord）一同落动星座（Movable Rāśi）且九宫主（Dharm's Lord）有力，则 Shankh Yog 成立。
- 本步骤产出事实：["Shankh Yog 成立判定"]
- 所需事实：["本盘上升主（Lagn's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否有力"}, {"fact_key": "五宫主（Putr's Lord）与六宫主（Ari's Lord）是否互为角宫"}]}, {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与十宫主（Karm's Lord）同落动星座（Movable Rāśi）"}, {"fact_key": "九宫主（Dharm's Lord）是否有力"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, "required_fact_keys": ["上升主（Lagn's Lord）是否有力", "五宫主（Putr's Lord）与六宫主（Ari's Lord）是否互为角宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否有力"}, {"fact_key": "五宫主（Putr's Lord）与六宫主（Ari's Lord）是否互为角宫"}]}, "selection_group": "ch36-v13-14-shankh-yog.step-001:shankh-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否有力、五宫主（Putr's Lord）与六宫主（Ari's Lord）是否互为角宫。"}, {"when": {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, "required_fact_keys": ["上升主（Lagn's Lord）是否与十宫主（Karm's Lord）同落动星座（Movable Rāśi）", "九宫主（Dharm's Lord）是否有力"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与十宫主（Karm's Lord）同落动星座（Movable Rāśi）"}, {"fact_key": "九宫主（Dharm's Lord）是否有力"}]}, "selection_group": "ch36-v13-14-shankh-yog.step-001:shankh-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否与十宫主（Karm's Lord）同落动星座（Movable Rāśi）、九宫主（Dharm's Lord）是否有力。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文本句没有给出「有力」的判准，不得自行发明力量算法。", "第一种成立方式原文没有写九宫主有力，第二种没有写五宫主与六宫主互为角宫，不得互相补入。", "原文写 along with（一同），不得放宽成两者各自落在动星座即可。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）是哪颗行星。
- 缺失即停字段：["本盘上升主（Lagn's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v13-14`｜PDF [79]｜“If Lagn’s Lord is strong, while the Lords of Putr and Ari Bhava are in mutual Kendras, then what is known, as Shankh Yog, is produced.”
  - `bphs-97:santhanam:ch36:v13-14`｜PDF [79]｜“Alternatively, if Lagn’s Lord along with Karm’s Lord is in a Movable Rāśi, while Dharm’s Lord is strong, Shankh Yog is obtained.”

### ch36-v13-14-shankh-yog.step-002

- 动作：在 Shankh Yog 成立时读取财富、家室、心性与寿数的断语。
- 适用范围：仅限已判定 Shankh Yog 成立的本命盘；原文以 He 立说（男命框架），未给时间限定。
- 原文最小意思：生于 Shankh Yog 者会有财富、配偶与儿子；他心地和善、吉祥、聪慧、有功德、长寿。
- 本步骤产出事实：["Shankh Yog 效果断语"]
- 所需事实：["Shankh Yog 成立判定"]
- 条件关系：{"fact_key": "Shankh Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文未给子女数目，不得据此推断有几个儿子。", "「长寿」不得换算成具体年数。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Shankh Yog 成立判定。
- 缺失即停字段：["Shankh Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v13-14`｜PDF [79]｜“One born with Shankh Yog will be endowed with wealth, spouse and sons. He will be kindly disposed, propitious, intelligent, meritorious and longlived.”


## 四路查书计划

### 支持路

- If Lagn’s Lord is strong, while the Lords of Putr and Ari Bhava are in mutual Kendras, then what is known, as Shankh Yog, is produced
- Alternatively, if Lagn’s Lord along with Karm’s Lord is in a Movable Rāśi, while Dharm’s Lord is strong, Shankh Yog is obtained
- 上升主有力 五宫主 六宫主 互为角宫 Shankh Yog

### 反例或取消路

- If Lagn’s Lord is yuti with the Lord of Ari, Randhr, or Vyaya Bhava, or with Shani and, if Lagn’s Lord is devoid of a Drishti from a benefic, the native will be penniless
- Should Putr’s and Dharm’s Lords be, respectively, found in Ari and Vyaya Bhava and receive a Drishti from Marak Grahas, the native will be penniless
- If the Lords of a Kendr, or a Kon own simultaneously an evil Bhava, he does not cause a Raj Yog by mere relations stipulated

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Classification of Rāśis. Movable, Fixed and Dual are the names given to the 12 Rāśis in order
- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- Indications of Putr Bhava
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少上升主身份事实时停止。
- 两种成立方式所需的事实都缺失时停止。
- 「有力」的判准由排盘窗口定义，未给出取值时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
