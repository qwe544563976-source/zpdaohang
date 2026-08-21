---
method: ch36-v1-2-subh-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Subh Yog：上升宫内有吉星，或十二宫与二宫内都有吉星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这个人口才和品行怎么样
- 我命里有没有吉利的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 上升宫（Lagna）是否被吉星占据
- 十二宫（Vyaya）是否被吉星占据
- 二宫（Dhan）是否被吉星占据

## 依赖方法

- 无

## 执行步骤

### ch36-v1-2-subh-yog.step-001

- 动作：先取本盘的吉星名册，再核对上升宫（Lagna）内是否有吉星、十二宫（Vyaya）与二宫（Dhan）内是否都有吉星，判定 Subh Yog 是否成立。
- 适用范围：仅限本命盘 Subh Yog 的成立判定；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：上升宫（Lagna）内有吉星，或十二宫（Vyaya）与二宫（Dhan）内都有吉星，则 Subh Yog 成立。
- 本步骤产出事实：["Subh Yog 成立判定"]
- 所需事实：["本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"operator": "OR", "operands": [{"fact_key": "上升宫（Lagna）是否被吉星占据"}, {"operator": "AND", "operands": [{"fact_key": "十二宫（Vyaya）是否被吉星占据"}, {"fact_key": "二宫（Dhan）是否被吉星占据"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["上升宫（Lagna）是否被吉星占据"], "branch_condition_logic": {"fact_key": "上升宫（Lagna）是否被吉星占据"}, "selection_group": "ch36-v1-2-subh-yog.step-001:subh-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升宫（Lagna）是否被吉星占据。"}, {"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["十二宫（Vyaya）是否被吉星占据", "二宫（Dhan）是否被吉星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十二宫（Vyaya）是否被吉星占据"}, {"fact_key": "二宫（Dhan）是否被吉星占据"}]}, "selection_group": "ch36-v1-2-subh-yog.step-001:subh-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫（Vyaya）是否被吉星占据、二宫（Dhan）是否被吉星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、寿命或具体事件。", "原文本句只写上升宫、十二宫与二宫三处，不得把 Subh Yog 的成立条件扩大到别的宫位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v1-2`｜PDF [79]｜“If there be a benefic in Lagna, Subh Yog is produced”
  - `bphs-97:santhanam:ch36:v1-2`｜PDF [79]｜“Benefics in both Vyaya and Dhan Bhava cause Subh Yog.”

### ch36-v1-2-subh-yog.step-002

- 动作：在 Subh Yog 成立时读取命主口才与品行的断语。
- 适用范围：仅限已判定 Subh Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：生于 Subh Yog 者能言善辩、有魅力、有德行。
- 本步骤产出事实：["Subh Yog 口才品行断语"]
- 所需事实：["Subh Yog 成立判定"]
- 条件关系：{"fact_key": "Subh Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富、寿命、婚姻或子女。", "原文只写这三项品性，不得据此扩展成其他人生领域的吉断。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Subh Yog 成立判定。
- 缺失即停字段：["Subh Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v1-2`｜PDF [79]｜“One born in Subh Yog will be eloquent, charming and virtuous”


## 四路查书计划

### 支持路

- If there be a benefic in Lagna, Subh Yog is produced
- Benefics in both Vyaya and Dhan Bhava cause Subh Yog
- 上升宫有吉星 Subh Yog 能言善辩 有德行

### 反例或取消路

- Malefics in both Vyaya and Dhan Bhava cause Asubh Yog
- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- 十二宫 二宫 凶星 Asubh Yog

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu
- Guru and Shukra are benefics, while Chandra is mediocre in benefice and Budh is neutral
- Budh, however, is a malefic, if he joins a malefic

### 判断方法路

- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少本盘吉星名册事实时停止。
- 上升宫、十二宫与二宫三项吉星占据事实全部缺失时停止。
- 原文本句未给出吉星判准，吉星名册未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
