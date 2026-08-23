---
method: ch39-v9-10-benefics-in-2-4-5
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 从上升主或 Atma Karak 星座起算的第2、4、5宫皆吉星：成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有当上位者的组合
- 从上升主起算的宫位该怎么用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 本盘上升主（Lagn's Lord）是哪颗行星
- 本盘的 Atma Karak 是哪颗行星

## 按情况检查的事实

- 从上升主（Lagn's Lord）起算的第2宫是否被吉星占据
- 从上升主（Lagn's Lord）起算的第4宫是否被吉星占据
- 从上升主（Lagn's Lord）起算的第5宫是否被吉星占据
- 从 Atma Karak 所在星座（Rāśi）起算的第2宫是否被吉星占据
- 从 Atma Karak 所在星座（Rāśi）起算的第4宫是否被吉星占据
- 从 Atma Karak 所在星座（Rāśi）起算的第5宫是否被吉星占据

## 依赖方法

- 无

## 执行步骤

### ch39-v9-10-benefics-in-2-4-5.step-001

- 动作：取本盘吉星名册，分别以上升主与 Atma Karak 所在星座为起点，核对第2、第4、第5宫内是否都有吉星。
- 适用范围：仅限本命盘；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：从上升主（Lagn's Lord）起算，或从 Atma Karak 所在星座（Atma Karak Rāśi）起算，第2、第4与第5宫内都有吉星时，命主会成为国王。
- 本步骤产出事实：["上升主或 Atma Karak 起算的三宫吉星贵格判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "本盘上升主（Lagn's Lord）是哪颗行星", "本盘的 Atma Karak 是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "从上升主（Lagn's Lord）起算的第2宫是否被吉星占据"}, {"fact_key": "从上升主（Lagn's Lord）起算的第4宫是否被吉星占据"}, {"fact_key": "从上升主（Lagn's Lord）起算的第5宫是否被吉星占据"}]}, {"operator": "AND", "operands": [{"fact_key": "从 Atma Karak 所在星座（Rāśi）起算的第2宫是否被吉星占据"}, {"fact_key": "从 Atma Karak 所在星座（Rāśi）起算的第4宫是否被吉星占据"}, {"fact_key": "从 Atma Karak 所在星座（Rāśi）起算的第5宫是否被吉星占据"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}]}, "required_fact_keys": ["从上升主（Lagn's Lord）起算的第2宫是否被吉星占据", "从上升主（Lagn's Lord）起算的第4宫是否被吉星占据", "从上升主（Lagn's Lord）起算的第5宫是否被吉星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "从上升主（Lagn's Lord）起算的第2宫是否被吉星占据"}, {"fact_key": "从上升主（Lagn's Lord）起算的第4宫是否被吉星占据"}, {"fact_key": "从上升主（Lagn's Lord）起算的第5宫是否被吉星占据"}]}, "selection_group": "ch39-v9-10-benefics-in-2-4-5.step-001:counting-from", "stop_condition": "选中该分支后，缺少以下事实即停止：从上升主（Lagn's Lord）起算的第2宫是否被吉星占据、从上升主（Lagn's Lord）起算的第4宫是否被吉星占据、从上升主（Lagn's Lord）起算的第5宫是否被吉星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}]}, "required_fact_keys": ["从 Atma Karak 所在星座（Rāśi）起算的第2宫是否被吉星占据", "从 Atma Karak 所在星座（Rāśi）起算的第4宫是否被吉星占据", "从 Atma Karak 所在星座（Rāśi）起算的第5宫是否被吉星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "从 Atma Karak 所在星座（Rāśi）起算的第2宫是否被吉星占据"}, {"fact_key": "从 Atma Karak 所在星座（Rāśi）起算的第4宫是否被吉星占据"}, {"fact_key": "从 Atma Karak 所在星座（Rāśi）起算的第5宫是否被吉星占据"}]}, "selection_group": "ch39-v9-10-benefics-in-2-4-5.step-001:counting-from", "stop_condition": "选中该分支后，缺少以下事实即停止：从 Atma Karak 所在星座（Rāśi）起算的第2宫是否被吉星占据、从 Atma Karak 所在星座（Rāśi）起算的第4宫是否被吉星占据、从 Atma Karak 所在星座（Rāśi）起算的第5宫是否被吉星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写第2、4、5 三宫，不得增减宫位，也不得把起算点换成上升宫本身。", "不得据此推断登位时间或具体权位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、本盘上升主（Lagn's Lord）是哪颗行星、本盘的 Atma Karak 是哪颗行星。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "本盘上升主（Lagn's Lord）是哪颗行星", "本盘的 Atma Karak 是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v9-10`｜PDF [82]｜“Should there be benefics in the 2<sup>nd</sup> , the 4<sup>th</sup> and the 5<sup>th</sup> , counted either from Lagn’s Lord, or from Atma Karak Rāśi, one will become a king.”


## 四路查书计划

### 支持路

- Should there be benefics in the 2<sup>nd</sup> , the 4<sup>th</sup> and the 5<sup>th</sup> , counted either from Lagn’s Lord, or from Atma Karak Rāśi, one will become a king
- 上升主起算 2 4 5 宫吉星 成为国王

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Budh, however, is a malefic, if he joins a malefic
- Karakāńś is the Navāńś, occupied by the Atma Karak Grah

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 缺少本盘吉星名册事实时停止。
- 上升主与 Atma Karak 的身份事实缺失时停止。
- 两条起算路线的宫位占据事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
