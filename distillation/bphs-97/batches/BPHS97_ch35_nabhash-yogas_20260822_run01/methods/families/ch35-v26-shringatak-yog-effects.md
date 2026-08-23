---
method: ch35-v26-shringatak-yog-effects
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Shringatak Yog 的效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Shringatak Yog 的人一生是什么样
- 我盘里的 Shringatak Yog 会带来什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Shringatak Yog 成立判定

## 按情况检查的事实

- 无

## 依赖方法

- ch35-v9-11-shringatak-yog

## 执行步骤

### ch35-v26-shringatak-yog-effects.step-001

- 动作：在 Shringatak Yog 已判定成立时，读取本偈给出的效果断语。
- 适用范围：仅限已判定 Shringatak Yog 成立的本命盘；成立条件来自本章前面的定义偈，本偈只给效果，原文没有时间限定。原文以 endowed with an auspicious wife、will hate women 立说，是男命框架的写法，女命命主命中时须另行核对。
- 原文最小意思：本盘所有行星（Grahas）落在上升宫（Lagna）、五宫（Putr）与九宫（Dharm Bhava）内而构成 Shringatak Yog 时，生于 Shringatak Yog 者喜好争吵与战斗，快乐，受国王喜爱，有一位吉利的妻子，富有，并且憎恶女性。
- 本步骤产出事实：["Shringatak Yog 效果断语"]
- 所需事实：["Shringatak Yog 成立判定"]
- 条件关系：{"fact_key": "Shringatak Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 an auspicious wife 换算成结婚次数或婚期。", "不得把 rich 换算成具体财富数额。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Shringatak Yog 成立判定。
- 缺失即停字段：["Shringatak Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v9-11`｜PDF [76]｜“All Grahas in Lagna, Putr and Dharm Bhava cause Shringatak Yog”
  - `bphs-97:santhanam:ch35:v26`｜PDF [77]｜“One born in Shringatak Yog”
  - `bphs-97:santhanam:ch35:v26`｜PDF [77]｜“will be fond of quarrels and battles, be happy, dear to king, endowed with an auspicious wife, be rich and will hate women”


## 四路查书计划

### 支持路

- One born in Shringatak Yog
- will be fond of quarrels and battles, be happy, dear to king, endowed with an auspicious wife, be rich and will hate women
- Shringatak Yog 的效果断语

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

- Shringatak Yog 是否成立尚未判定时停止：成立条件由方法 ch35-v9-11-shringatak-yog 给出。
- 不得在 Shringatak Yog 未成立时套用本条断语。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
