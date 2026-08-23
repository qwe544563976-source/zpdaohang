---
method: ch35-v32-yup-yog-effects
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Yup Yog 的效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Yup Yog 的人一生是什么样
- 我盘里的 Yup Yog 会带来什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Yup Yog 成立判定

## 按情况检查的事实

- 无

## 依赖方法

- ch35-v13-yup-yog

## 执行步骤

### ch35-v32-yup-yog-effects.step-001

- 动作：在 Yup Yog 已判定成立时，读取本偈给出的效果断语。
- 适用范围：仅限已判定 Yup Yog 成立的本命盘；成立条件来自本章前面的定义偈，本偈只给效果，原文没有时间限定。原文以 He will be endowed with a wife 立说，是男命框架的写法，女命命主命中时须另行核对。
- 原文最小意思：本盘7颗行星（Grahas）落在从上升宫（Lagna）起算的4个宫（Bhava）内而构成 Yup Yog 时，生于 Yup Yog 者拥有灵性知识，热衷祭祀仪式，会有妻子，强壮，热衷斋戒与其他宗教修持，出众。
- 本步骤产出事实：["Yup Yog 效果断语"]
- 所需事实：["Yup Yog 成立判定"]
- 条件关系：{"fact_key": "Yup Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 endowed with a wife 换算成婚期或婚姻次数。", "不得据此推断财富数额或寿命。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Yup Yog 成立判定。
- 缺失即停字段：["Yup Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v13`｜PDF [76]｜“If all the 7 Grahas are in the 4 Bhavas, commencing from Lagna, they cause Yup Yog”
  - `bphs-97:santhanam:ch35:v32`｜PDF [77]｜“One born in Yup Yog”
  - `bphs-97:santhanam:ch35:v32`｜PDF [77]｜“will have spiritual knowledge and will be interested in sacrificial rites”
  - `bphs-97:santhanam:ch35:v32`｜PDF [77]｜“He will be endowed with a wife, be strong, interested in fasts and other religious observations and be distinguished”


## 四路查书计划

### 支持路

- One born in Yup Yog
- will have spiritual knowledge and will be interested in sacrificial rites
- He will be endowed with a wife, be strong, interested in fasts and other religious observations and be distinguished
- Yup Yog 的效果断语

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

- Yup Yog 是否成立尚未判定时停止：成立条件由方法 ch35-v13-yup-yog 给出。
- 不得在 Yup Yog 未成立时套用本条断语。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
