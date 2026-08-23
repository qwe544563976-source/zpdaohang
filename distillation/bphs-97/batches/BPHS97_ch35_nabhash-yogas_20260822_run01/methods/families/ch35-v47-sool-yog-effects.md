---
method: ch35-v47-sool-yog-effects
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Sool Yog 的效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Sool Yog 的人一生是什么样
- 我盘里的 Sool Yog 会带来什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Sool Yog 成立判定
- 本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立

## 按情况检查的事实

- 无

## 依赖方法

- ch35-v16-17-sool-yog

## 执行步骤

### ch35-v47-sool-yog-effects.step-001

- 动作：在 Sool Yog 已判定成立时，读取本偈给出的效果断语。
- 适用范围：仅限已判定 Sool Yog 成立的本命盘；成立条件来自本章前面的定义偈，本偈只给效果，原文没有时间限定。
- 原文最小意思：本盘没有别的 Nabhash Yog 可成立、本盘所有行星（Grahas）都落在星座（Rāśi）内、所占星座数为3而构成 Sool Yog 时，生于 Sool Yog 者敏锐，懒散，没有财富，行事曲折，被禁止，英勇，并因战争而有名。
- 本步骤产出事实：["Sool Yog 效果断语"]
- 所需事实：["Sool Yog 成立判定", "本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "Sool Yog 成立判定"}, {"operator": "NOT", "operands": [{"fact_key": "本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[{"type": "limitation", "evidence_atom_ids": ["bphs-97:santhanam:ch35:v16-17"], "condition_logic": {"fact_key": "本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立"}}]
- 禁止扩大：["不得给 prohibited 补上原文没有解释的具体含义。", "不得把 famous through war 换成具体战功或年代。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Sool Yog 成立判定、本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立。
- 缺失即停字段：["Sool Yog 成立判定", "本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v16-17`｜PDF [76]｜“If all Grahas are in one Rāśi”
  - `bphs-97:santhanam:ch35:v16-17`｜PDF [76]｜“if in 3, Sool Yog occurs”
  - `bphs-97:santhanam:ch35:v47`｜PDF [78]｜“One born in Sool Yog”
  - `bphs-97:santhanam:ch35:v47`｜PDF [78]｜“will be sharp, indolent, bereft of wealth, be tortuous, prohibited, valiant and famous through war”
  - `bphs-97:santhanam:ch35:v16-17`｜PDF [76]｜“None of these seven Yogas will be operable, if another Nabhash Yog is derivable.”


## 四路查书计划

### 支持路

- One born in Sool Yog
- will be sharp, indolent, bereft of wealth, be tortuous, prohibited, valiant and famous through war
- Sool Yog 的效果断语

### 反例或取消路

- None of these seven Yogas will be operable, if another Nabhash Yog is derivable.

### 适用边界路

- Ancestors say, that the results, due to said (Nabhash) Yogas, will be felt throughout in all the Dasha periods.
- O excellent of the Brahmins, explained below are 32 Nabhash Yogas, which have a total of 1800 different varieties.
- Nabhash 瑜伽效果的时间范围与全章边界

### 判断方法路

- Names of Nabhash Yogas. The 3 Asraya Yogas are Rajju, Musala and Nala Yogas.
- Effects of Nabhash Yogas (up to Sloka 50).
- 怎么按 Nabhash 瑜伽的分类去查一张盘

## 上游问题

- 无

## 停止条件

- Sool Yog 是否成立尚未判定时停止：成立条件由方法 ch35-v16-17-sool-yog 给出。
- 不得在 Sool Yog 未成立时套用本条断语。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
