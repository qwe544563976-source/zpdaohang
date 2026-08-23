---
method: ch35-v35-danda-yog-effects
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Danda Yog 的效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Danda Yog 的人一生是什么样
- 我盘里的 Danda Yog 会带来什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Danda Yog 成立判定

## 按情况检查的事实

- 无

## 依赖方法

- ch35-v13-danda-yog

## 执行步骤

### ch35-v35-danda-yog-effects.step-001

- 动作：在 Danda Yog 已判定成立时，读取本偈给出的效果断语。
- 适用范围：仅限已判定 Danda Yog 成立的本命盘；成立条件来自本章前面的定义偈，本偈只给效果，原文没有时间限定。原文以 will lose sons and wife、away from his men 立说，是男命框架的写法，女命命主命中时须另行核对。
- 原文最小意思：从十宫（Karm）起算而构成 Danda Yog 时，生于 Danda Yog 者失去子女与妻子，贫困，不仁厚，远离自己的人，并且服侍卑下的人。
- 本步骤产出事实：["Danda Yog 效果断语"]
- 所需事实：["Danda Yog 成立判定"]
- 条件关系：{"fact_key": "Danda Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写 lose，中文只能写「失去」，不得补上年龄、死因或绝嗣的含义。", "不得把 lose sons and wife 换算成具体人数或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Danda Yog 成立判定。
- 缺失即停字段：["Danda Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v13`｜PDF [76]｜“if from Karm, Danda Yog is formed”
  - `bphs-97:santhanam:ch35:v35`｜PDF [77]｜“One born in Danda Yog”
  - `bphs-97:santhanam:ch35:v35`｜PDF [77]｜“will lose sons and wife, will be indigent, unkind, away from his men and will serve mean people”


## 四路查书计划

### 支持路

- One born in Danda Yog
- will lose sons and wife, will be indigent, unkind, away from his men and will serve mean people
- Danda Yog 的效果断语

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

- Danda Yog 是否成立尚未判定时停止：成立条件由方法 ch35-v13-danda-yog 给出。
- 不得在 Danda Yog 未成立时套用本条断语。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
