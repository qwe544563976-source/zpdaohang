---
method: ch39-v3-5-raj-yog-frame
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Raj Yog 总纲：两组要素与效果的全、半、四分之一分档

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 看贵格该从哪几个点入手
- 为什么同样的贵格有人应验有人不应

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Atma Karak 是哪颗行星
- 本盘的 Putr Karak 是哪颗行星
- 本盘上升主（Lagn's Lord）是哪颗行星
- 本盘五宫主（Putr's Lord）是哪颗行星
- 参与 Raj Yog 关联的行星力量如何

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v3-5-raj-yog-frame.step-001

- 动作：按原文总纲取齐四个要素：Atma Karak、Putr Karak、本命上升主与五宫主，并按其力量确定效果的分档。
- 适用范围：本偈是 Raj Yog 章的总纲：只指明要从 Karakāńś Lagn 与本命上升考察的两组要素，以及效果按力量分为全、一半、四分之一，未给出关联成立的具体条件，也未给出力量的判准。
- 原文最小意思：Raj Yog 要从 Karakāńś Lagn 与本命上升（natal Lagn）来判断：一方面考察 Atma Karak 与 Putr Karak 这一对，另一方面考察本命上升主（natal Lagn's Lord）与五宫主（Putr's Lord）；由这种关联而来的效果，按其力量为全、一半或四分之一。
- 本步骤产出事实：["Raj Yog 考察要素与效果分档"]
- 所需事实：["本盘的 Atma Karak 是哪颗行星", "本盘的 Putr Karak 是哪颗行星", "本盘上升主（Lagn's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星", "参与 Raj Yog 关联的行星力量如何"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Putr Karak 是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "参与 Raj Yog 关联的行星力量如何"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文规定 association（关联）如何才算成立。", "不得替原文规定多大力量对应全、一半或四分之一。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Atma Karak 是哪颗行星、本盘的 Putr Karak 是哪颗行星、本盘上升主（Lagn's Lord）是哪颗行星、本盘五宫主（Putr's Lord）是哪颗行星、参与 Raj Yog 关联的行星力量如何。
- 缺失即停字段：["本盘的 Atma Karak 是哪颗行星", "本盘的 Putr Karak 是哪颗行星", "本盘上升主（Lagn's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星", "参与 Raj Yog 关联的行星力量如何"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v3-5`｜PDF [82]｜“Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn. On the one hand the pair of Atma Karak and Putr Karak should be considered and on the other hand the natal Lagn’s Lord and Putr’s Lord should be taken into consideration. The effects, due to such association, will be full, or a half, or a quarter, according to their strengths.”


## 四路查书计划

### 支持路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The effects, due to such association, will be full, or a half, or a quarter, according to their strengths
- 贵格总纲 Karakāńś 与本命上升 两组要素

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Karakāńś is the Navāńś, occupied by the Atma Karak Grah
- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth

### 判断方法路

- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 四个要素（Atma Karak、Putr Karak、上升主、五宫主）缺任一项时停止。
- 原文未给出关联（association）的成立条件与力量判准，未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
