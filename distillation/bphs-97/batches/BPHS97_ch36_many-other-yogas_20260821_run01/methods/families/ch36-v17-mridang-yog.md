---
method: ch36-v17-mridang-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Mridang Yog：上升主有力，其余行星落角宫、三角宫、本宫或入旺星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有当王者或与王者相等的组合
- 我这辈子过得快不快乐

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否有力

## 按情况检查的事实

- 其余行星（others）是否落角宫
- 其余行星（others）是否落三角宫
- 其余行星（others）是否落本宫（own Bhava）
- 其余行星（others）是否落入旺星座

## 依赖方法

- 无

## 执行步骤

### ch36-v17-mridang-yog.step-001

- 动作：先核对上升主（Lagn's Lord）是否有力，再核对原文所称的其余行星（others）是否落角宫、三角宫、本宫或入旺星座，判定 Mridang Yog 是否成立。
- 适用范围：仅限本命盘 Mridang Yog 的成立判定；原文本句只写 others（其余行星），既未界定指哪几颗，也未说明需几颗满足，全书本处未见界定，未确定即停判；原文也未给出「有力」的判准与时间限定。
- 原文最小意思：上升主（Lagn's Lord）有力，且其余行星（others）落角宫、三角宫、本宫（own Bhava）或入旺星座，则 Mridang Yog 成立。
- 本步骤产出事实：["Mridang Yog 成立判定"]
- 所需事实：["上升主（Lagn's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否有力"}, {"operator": "OR", "operands": [{"fact_key": "其余行星（others）是否落角宫"}, {"fact_key": "其余行星（others）是否落三角宫"}, {"fact_key": "其余行星（others）是否落本宫（own Bhava）"}, {"fact_key": "其余行星（others）是否落入旺星座"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "上升主（Lagn's Lord）是否有力"}, "required_fact_keys": ["其余行星（others）是否落角宫"], "branch_condition_logic": {"fact_key": "其余行星（others）是否落角宫"}, "selection_group": "ch36-v17-mridang-yog.step-001:others-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：其余行星（others）是否落角宫。"}, {"when": {"fact_key": "上升主（Lagn's Lord）是否有力"}, "required_fact_keys": ["其余行星（others）是否落三角宫"], "branch_condition_logic": {"fact_key": "其余行星（others）是否落三角宫"}, "selection_group": "ch36-v17-mridang-yog.step-001:others-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：其余行星（others）是否落三角宫。"}, {"when": {"fact_key": "上升主（Lagn's Lord）是否有力"}, "required_fact_keys": ["其余行星（others）是否落本宫（own Bhava）"], "branch_condition_logic": {"fact_key": "其余行星（others）是否落本宫（own Bhava）"}, "selection_group": "ch36-v17-mridang-yog.step-001:others-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：其余行星（others）是否落本宫（own Bhava）。"}, {"when": {"fact_key": "上升主（Lagn's Lord）是否有力"}, "required_fact_keys": ["其余行星（others）是否落入旺星座"], "branch_condition_logic": {"fact_key": "其余行星（others）是否落入旺星座"}, "selection_group": "ch36-v17-mridang-yog.step-001:others-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：其余行星（others）是否落入旺星座。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文未界定 others（其余行星）指哪几颗行星、也未给数量，不得自行指定范围或补上数量。", "原文本句没有给出「有力」的判准，不得自行发明力量算法。", "原文这一支写的是 own Bhavas（本宫），不得改读成本星座（own Rāśi）。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否有力。
- 缺失即停字段：["上升主（Lagn's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v17`｜PDF [79, 80]｜“If Lagn’s Lord is strong and others occupy Kendras, Konas, own Bhavas, or exaltation Rāśis, Mridang Yog is formed.”

### ch36-v17-mridang-yog.step-002

- 动作：在 Mridang Yog 成立时读取地位与快乐的断语。
- 适用范围：仅限已判定 Mridang Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：Mridang Yog 成立时，命主会成为国王，或与国王相等，并且快乐。
- 本步骤产出事实：["Mridang Yog 效果断语"]
- 所需事实：["Mridang Yog 成立判定"]
- 条件关系：{"fact_key": "Mridang Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文把「成为国王」与「与国王相等」并列写在结果里，不得据此断定必属其中哪一种。", "不得据此推断财富数额、寿命或子女。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Mridang Yog 成立判定。
- 缺失即停字段：["Mridang Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v17`｜PDF [79, 80]｜“Mridang Yog is formed”
  - `bphs-97:santhanam:ch36:v17`｜PDF [79, 80]｜“The native concerned will be a king, or equal to a king and be happy.”


## 四路查书计划

### 支持路

- If Lagn’s Lord is strong and others occupy Kendras, Konas, own Bhavas, or exaltation Rāśis, Mridang Yog is formed
- The native concerned will be a king, or equal to a king and be happy
- 上升主有力 其余行星落角宫三角宫 Mridang Yog

### 反例或取消路

- If Lagn’s Lord is yuti with the Lord of Ari, Randhr, or Vyaya Bhava, or with Shani and, if Lagn’s Lord is devoid of a Drishti from a benefic, the native will be penniless
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- If the Lords of a Kendr, or a Kon own simultaneously an evil Bhava, he does not cause a Raj Yog by mere relations stipulated

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula

### 判断方法路

- If one and the same Grah gets the lordships of a Kon, as well as a Kendr, or, if a Grah is in a Kendr, or in a Kon, it will prove specially a Yog Karak
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少上升主力量事实时停止。
- 「有力」的判准由排盘窗口定义，未给出取值时停止。
- 原文未界定 others（其余行星）指哪些行星，未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
