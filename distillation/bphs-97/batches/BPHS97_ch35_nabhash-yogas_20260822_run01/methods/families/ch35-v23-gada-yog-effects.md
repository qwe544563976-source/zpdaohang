---
method: ch35-v23-gada-yog-effects
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Gada Yog 的效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Gada Yog 的人一生是什么样
- 我盘里的 Gada Yog 会带来什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Gada Yog 成立判定

## 按情况检查的事实

- 无

## 依赖方法

- ch35-v9-11-gada-yog

## 执行步骤

### ch35-v23-gada-yog-effects.step-001

- 动作：在 Gada Yog 已判定成立时，读取本偈给出的效果断语。
- 适用范围：仅限已判定 Gada Yog 成立的本命盘；成立条件来自本章前面的定义偈，本偈只给效果，原文没有时间限定。
- 原文最小意思：本盘所有行星（Grahas）落在相邻的两个角宫（Kendra）内而构成 Gada Yog 时，生于 Gada Yog 者一直努力赚取财富，会举行祭祀仪式，精通经论与歌唱，拥有财富、黄金与宝石。
- 本步骤产出事实：["Gada Yog 效果断语"]
- 所需事实：["Gada Yog 成立判定"]
- 条件关系：{"fact_key": "Gada Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 endowed with wealth 换算成具体财富数额。", "不得把 skilful in Shastras and songs 引申成具体职业。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Gada Yog 成立判定。
- 缺失即停字段：["Gada Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v9-11`｜PDF [76]｜“all the Grahas occupy two successive Kendras, Gada Yog is formed”
  - `bphs-97:santhanam:ch35:v23`｜PDF [77]｜“One born in Gada Yog”
  - `bphs-97:santhanam:ch35:v23`｜PDF [77]｜“will always make efforts to earn wealth, will perform sacrificial rites, be skilful in Shastras and songs and endowed with wealth, gold and precious stones”


## 四路查书计划

### 支持路

- One born in Gada Yog
- will always make efforts to earn wealth, will perform sacrificial rites, be skilful in Shastras and songs and endowed with wealth, gold and precious stones
- Gada Yog 的效果断语

### 反例或取消路

- 无

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

- Gada Yog 是否成立尚未判定时停止：成立条件由方法 ch35-v9-11-gada-yog 给出。
- 不得在 Gada Yog 未成立时套用本条断语。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
