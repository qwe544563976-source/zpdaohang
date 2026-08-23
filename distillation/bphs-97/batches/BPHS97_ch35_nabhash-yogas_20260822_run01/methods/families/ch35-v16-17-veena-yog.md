---
method: ch35-v16-17-veena-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Veena Yog：所有行星共占据 7 个星座，且本盘没有别的 Nabhash 瑜伽

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我命里有没有 Veena Yog
- 我盘上行星一共挤在几个星座里

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘所有行星（Grahas）共占据几个星座（Rāśi）
- 本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch35-v16-17-veena-yog.step-001

- 动作：核对本盘行星（Grahas）的分布，判定 Veena Yog 是否成立。
- 适用范围：仅限本命盘 Veena Yog（Sankhya Yogas 之一）的成立判定；原文同偈写明这七个瑜伽在另有别的 Nabhash 瑜伽可成立时不起作用；原文没有时间限定。
- 原文最小意思：本盘没有别的 Nabhash Yog 可成立、且本盘所有行星（Grahas）都落在星座（Rāśi）内、所占星座数为7时，构成 Veena Yog。
- 本步骤产出事实：["Veena Yog 成立判定"]
- 所需事实：["本盘所有行星（Grahas）共占据几个星座（Rāśi）", "本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘所有行星（Grahas）共占据几个星座（Rāśi）"}, {"operator": "NOT", "operands": [{"fact_key": "本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[{"type": "limitation", "evidence_atom_ids": ["bphs-97:santhanam:ch35:v16-17"], "condition_logic": {"fact_key": "本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立"}}]
- 禁止扩大：["不得把「共占据7个星座」换算成宫（Bhava）的个数——原文这一句说的是星座。", "不得丢掉 None of these seven Yogas will be operable 这条限制——另有别的 Nabhash 瑜伽可成立时本瑜伽不起作用。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘所有行星（Grahas）共占据几个星座（Rāśi）、本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立。
- 缺失即停字段：["本盘所有行星（Grahas）共占据几个星座（Rāśi）", "本盘是否另有别的 Nabhash 瑜伽（Nabhash Yog）可成立"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v16-17`｜PDF [76]｜“If all Grahas are in one Rāśi”
  - `bphs-97:santhanam:ch35:v16-17`｜PDF [76]｜“if in 7, Veena Yog is produced”
  - `bphs-97:santhanam:ch35:v16-17`｜PDF [76]｜“None of these seven Yogas will be operable, if another Nabhash Yog is derivable.”


## 四路查书计划

### 支持路

- If all Grahas are in one Rāśi
- if in 7, Veena Yog is produced
- None of these seven Yogas will be operable, if another Nabhash Yog is derivable.
- Veena Yog 的成立条件

### 反例或取消路

- None of these seven Yogas will be operable, if another Nabhash Yog is derivable.

### 适用边界路

- O excellent of the Brahmins, explained below are 32 Nabhash Yogas, which have a total of 1800 different varieties.
- These consist of 3 Asraya Yogas, 2 Dala Yogas, 20 Akriti Yogas and 7 Sankhya Yogas.
- Nabhash 瑜伽全章的总数与分类边界

### 判断方法路

- Names of Nabhash Yogas. The 3 Asraya Yogas are Rajju, Musala and Nala Yogas.
- Effects of Nabhash Yogas (up to Sloka 50).
- 怎么按 Nabhash 瑜伽的分类去查一张盘

## 上游问题

- 无

## 停止条件

- 缺少判定 Veena Yog 所需的行星分布事实时停止。
- 行星分布事实取不到确定值时停止，不得凭部分行星推定 Veena Yog 成立。
- 无法确定本盘是否另有别的 Nabhash 瑜伽可成立时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
