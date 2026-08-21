---
method: ch36-v1-2-asubh-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Asubh Yog：上升宫内有凶星，或十二宫与二宫内都有凶星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我命里有没有不吉的组合
- 我为什么总被人说品行不好

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星

## 按情况检查的事实

- 上升宫（Lagna）是否被凶星占据
- 十二宫（Vyaya）是否被凶星占据
- 二宫（Dhan）是否被凶星占据

## 依赖方法

- 无

## 执行步骤

### ch36-v1-2-asubh-yog.step-001

- 动作：先取本盘的凶星名册，再核对上升宫（Lagn）内是否有凶星、十二宫（Vyaya）与二宫（Dhan）内是否都有凶星，判定 Asubh Yog 是否成立。
- 适用范围：仅限本命盘 Asubh Yog 的成立判定；原文本句未给出凶星的判准，也没有时间限定。
- 原文最小意思：上升宫（Lagn）内有凶星，或十二宫（Vyaya）与二宫（Dhan）内都有凶星，则 Asubh Yog 成立。
- 本步骤产出事实：["Asubh Yog 成立判定"]
- 所需事实：["本盘中哪些行星被判为凶星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"operator": "OR", "operands": [{"fact_key": "上升宫（Lagna）是否被凶星占据"}, {"operator": "AND", "operands": [{"fact_key": "十二宫（Vyaya）是否被凶星占据"}, {"fact_key": "二宫（Dhan）是否被凶星占据"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些行星被判为凶星"}, "required_fact_keys": ["上升宫（Lagna）是否被凶星占据"], "branch_condition_logic": {"fact_key": "上升宫（Lagna）是否被凶星占据"}, "selection_group": "ch36-v1-2-asubh-yog.step-001:asubh-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升宫（Lagna）是否被凶星占据。"}, {"when": {"fact_key": "本盘中哪些行星被判为凶星"}, "required_fact_keys": ["十二宫（Vyaya）是否被凶星占据", "二宫（Dhan）是否被凶星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十二宫（Vyaya）是否被凶星占据"}, {"fact_key": "二宫（Dhan）是否被凶星占据"}]}, "selection_group": "ch36-v1-2-asubh-yog.step-001:asubh-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫（Vyaya）是否被凶星占据、二宫（Dhan）是否被凶星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断寿命、疾病或具体灾祸。", "原文本句只写上升宫、十二宫与二宫三处，不得把 Asubh Yog 的成立条件扩大到别的宫位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星。
- 缺失即停字段：["本盘中哪些行星被判为凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v1-2`｜PDF [79]｜“while a malefic in Lagn causes Asubh Yog”
  - `bphs-97:santhanam:ch36:v1-2`｜PDF [79]｜“Malefics in both Vyaya and Dhan Bhava cause Asubh Yog.”

### ch36-v1-2-asubh-yog.step-002

- 动作：在 Asubh Yog 成立时读取与 Subh Yog 者相对的那一侧断语。
- 适用范围：仅限已判定 Asubh Yog 成立的本命盘；原文此处只写 his counterpart（与生于 Subh Yog 者相对的那一位），并未重复写出 Asubh Yog 之名，本步按同一偈内 Subh／Asubh 的对照关系挂在 Asubh Yog 下；原文未给时间限定。
- 原文最小意思：与生于 Subh Yog 者相对，其对立者耽于感官享乐、会做罪恶之事、并享用（吞没）他人的财富。
- 本步骤产出事实：["Asubh Yog 品行断语"]
- 所需事实：["Asubh Yog 成立判定"]
- 条件关系：{"fact_key": "Asubh Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断具体罪名、财物数额或事发时间。", "原文只写这三项，不得据此扩展成寿命、疾病或婚姻的断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Asubh Yog 成立判定。
- 缺失即停字段：["Asubh Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v1-2`｜PDF [79]｜“One born in Subh Yog will be eloquent, charming and virtuous, while his counterpart will be sensuous, will do sinful acts and will enjoy (swallow) others’ wealth.”


## 四路查书计划

### 支持路

- while a malefic in Lagn causes Asubh Yog
- Malefics in both Vyaya and Dhan Bhava cause Asubh Yog
- 上升宫有凶星 Asubh Yog 罪恶 吞没他人财富

### 反例或取消路

- Benefics in both Vyaya and Dhan Bhava cause Subh Yog
- Should Budh give a Drishti to Mangal and Shani in Dhan Bhava, there will be great wealth
- 凶星在二宫 木星相照 化解

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu
- Guru and Shukra are benefics, while Chandra is mediocre in benefice and Budh is neutral
- Budh, however, is a malefic, if he joins a malefic

### 判断方法路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少本盘凶星名册事实时停止。
- 上升宫、十二宫与二宫三项凶星占据事实全部缺失时停止。
- 原文本句未给出凶星判准，凶星名册未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
