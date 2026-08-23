---
method: ch35-v39-chap-yog-effects
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Chap Yog 的效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Chap Yog 的人一生是什么样
- 我盘里的 Chap Yog 会带来什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Chap Yog 成立判定

## 按情况检查的事实

- 无

## 依赖方法

- ch35-v14-chap-yog

## 执行步骤

### ch35-v39-chap-yog-effects.step-001

- 动作：在 Chap Yog 已判定成立时，读取本偈给出的效果断语。
- 适用范围：仅限已判定 Chap Yog 成立的本命盘；成立条件来自本章前面的定义偈，本偈只给效果，原文没有时间限定。
- 原文最小意思：从十宫（Karm）起算而构成 Chap Yog 时，生于 Chap Yog 者说谎，守得住秘密，做贼，喜好游荡与森林，没有运气，在人生中段快乐。
- 本步骤产出事实：["Chap Yog 效果断语"]
- 所需事实：["Chap Yog 成立判定"]
- 条件关系：{"fact_key": "Chap Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 the middle of the life 换算成具体年岁或某段大运。", "不得据此推断寿命或刑狱的具体时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Chap Yog 成立判定。
- 缺失即停字段：["Chap Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v14`｜PDF [76]｜“if from Karm, Chap Yog occurs”
  - `bphs-97:santhanam:ch35:v39`｜PDF [78]｜“One born in Chap Yog”
  - `bphs-97:santhanam:ch35:v39`｜PDF [78]｜“will be liar, will protect secrets, be a thief, be fond of wandering, forests, be devoid of luck and be happy in the middle of the life”


## 四路查书计划

### 支持路

- One born in Chap Yog
- will be liar, will protect secrets, be a thief, be fond of wandering, forests, be devoid of luck and be happy in the middle of the life
- Chap Yog 的效果断语

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

- Chap Yog 是否成立尚未判定时停止：成立条件由方法 ch35-v14-chap-yog 给出。
- 不得在 Chap Yog 未成立时套用本条断语。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
