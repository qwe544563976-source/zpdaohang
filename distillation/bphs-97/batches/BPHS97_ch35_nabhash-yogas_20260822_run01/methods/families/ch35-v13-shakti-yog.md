---
method: ch35-v13-shakti-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Shakti Yog：7 颗行星都落在从七宫（Yuvati）起算的 4 个宫内

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我命里有没有 Shakti Yog
- 我盘上 7 颗行星是不是都挤在从七宫（Yuvati）起的 4 个宫里

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘7颗行星（Grahas）是否都落在从七宫（Yuvati）起算的4个宫（Bhava）内

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch35-v13-shakti-yog.step-001

- 动作：核对本盘行星（Grahas）的分布，判定 Shakti Yog 是否成立。
- 适用范围：仅限本命盘 Shakti Yog 的成立判定；原文只给盘面分布条件，没有时间、上升或男女限定。
- 原文最小意思：本盘7颗行星（Grahas）都落在4个宫（Bhava）内、从七宫（Yuvati）起算时，构成 Shakti Yog。
- 本步骤产出事实：["Shakti Yog 成立判定"]
- 所需事实：["本盘7颗行星（Grahas）是否都落在从七宫（Yuvati）起算的4个宫（Bhava）内"]
- 条件关系：{"fact_key": "本盘7颗行星（Grahas）是否都落在从七宫（Yuvati）起算的4个宫（Bhava）内"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把起算宫从七宫（Yuvati）换成别的宫——原文逐个点名了起算宫。", "不得把 4 个宫放宽成任意 4 个宫——原文要求从起算宫连排。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘7颗行星（Grahas）是否都落在从七宫（Yuvati）起算的4个宫（Bhava）内。
- 缺失即停字段：["本盘7颗行星（Grahas）是否都落在从七宫（Yuvati）起算的4个宫（Bhava）内"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v13`｜PDF [76]｜“If all the 7 Grahas are in the 4 Bhavas”
  - `bphs-97:santhanam:ch35:v13`｜PDF [76]｜“if from Yuvati, Shakti Yog occurs”


## 四路查书计划

### 支持路

- If all the 7 Grahas are in the 4 Bhavas
- if from Yuvati, Shakti Yog occurs
- Shakti Yog 的成立条件

### 反例或取消路

- 无

### 适用边界路

- If all the 7 Grahas are in the 4 Bhavas, commencing from Lagna, they cause Yup Yog, if from Bandhu, Shar Yog occurs, if from Yuvati, Shakti Yog occurs and, if from Karm, Danda Yog is formed.
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

- 缺少判定 Shakti Yog 所需的行星分布事实时停止。
- 行星分布事实取不到确定值时停止，不得凭部分行星推定 Shakti Yog 成立。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
