---
method: ch35-v14-ardh-chandraa-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Ardh Chandraa Yoga：7 颗行星从一个非角宫起连续占据七宫（引自 Saravali）

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我命里有没有 Ardh Chandra Yog
- 我盘上行星从非角宫起连排七个宫算什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘7颗行星（Grahas）是否从对上升宫（Lagna）而言非角宫的某一宫（Bhava）起连续占据七个宫（Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch35-v14-ardh-chandraa-yog.step-001

- 动作：核对本盘行星（Grahas）的分布，判定 Ardh Chandraa Yoga 是否成立。
- 适用范围：仅限本命盘 Ardh Chandraa Yoga 的成立判定；原文这一段标明 Quoted from Saravali，是转引他书，结论强度不等同本书自断；原文没有时间限定。
- 原文最小意思：本盘7颗行星（Grahas）从对上升宫（Lagna）而言非角宫的某一宫（Bhava）起连续占据七个宫（Bhava）时，构成 Ardh Chandraa Yoga。
- 本步骤产出事实：["Ardh Chandraa Yoga 成立判定"]
- 所需事实：["本盘7颗行星（Grahas）是否从对上升宫（Lagna）而言非角宫的某一宫（Bhava）起连续占据七个宫（Bhava）"]
- 条件关系：{"fact_key": "本盘7颗行星（Grahas）是否从对上升宫（Lagna）而言非角宫的某一宫（Bhava）起连续占据七个宫（Bhava）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得丢掉 not angular to the Lagna 这个限定——起算宫必须不是上升宫（Lagna）的角宫。", "不得把这条按 Parashar 自断使用——原文标明 Quoted from Saravali。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘7颗行星（Grahas）是否从对上升宫（Lagna）而言非角宫的某一宫（Bhava）起连续占据七个宫（Bhava）。
- 缺失即停字段：["本盘7颗行星（Grahas）是否从对上升宫（Lagna）而言非角宫的某一宫（Bhava）起连续占据七个宫（Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v14`｜PDF [76]｜“If the seven Grahas occupy continuously seven Bhavas, commencing from a Bhava, which is not angular to the Lagna, the Yoga produced is known, as Ardh Chandraa Yoga.”


## 四路查书计划

### 支持路

- If the seven Grahas occupy continuously seven Bhavas, commencing from a Bhava, which is not angular to the Lagna, the Yoga produced is known, as Ardh Chandraa Yoga.
- Ardh Chandraa Yoga 的成立条件

### 反例或取消路

- 无

### 适用边界路

- Quoted from Saravali. If the seven Grahas occupy continuously seven Bhavas, commencing from a Bhava, which is not angular to the Lagna, the Yoga produced is known, as Ardh Chandraa Yoga.
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

- 缺少判定 Ardh Chandraa Yoga 所需的行星分布事实时停止。
- 行星分布事实取不到确定值时停止，不得凭部分行星推定 Ardh Chandraa Yoga 成立。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
