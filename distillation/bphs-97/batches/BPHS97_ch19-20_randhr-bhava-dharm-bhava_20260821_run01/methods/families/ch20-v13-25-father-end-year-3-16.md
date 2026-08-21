---
method: ch20-v13-25-father-end-year-3-16
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲在命主第3年或第16年走到生命终点：十二宫主落九宫、九宫主落自己落陷的九分盘星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲的寿限大概在什么时候
- 九宫主在九分盘落陷说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十二宫主（Vyaya's Lord）是否落九宫（Dharm）
- 九宫主（Dharm's Lord）是否落自己落陷的九分盘（Navamsa D9）星座

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v13-25-father-end-year-3-16.step-001

- 动作：核对十二宫主（Vyaya's Lord）是否落九宫（Dharm），并核对九宫主（Dharm's Lord）是否落在自己落陷的九分盘（Navamsa D9）星座。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文以「Combinations for Father’s Death」立目，末句「Thus the Jyotishis may know the effects」把这组组合交由 Jyotishis 判读；原文未给上升限定。
- 原文最小意思：十二宫主（Vyaya's Lord）落九宫（Dharm）、且九宫主（Dharm's Lord）落自己落陷的九分盘（Navamsa D9）星座时，命主的父亲在命主第3年或第16年走到生命终点。
- 本步骤产出事实：["十二宫主落九宫且九宫主九分盘落陷主父亲第3或16年终判定"]
- 所需事实：["十二宫主（Vyaya's Lord）是否落九宫（Dharm）", "九宫主（Dharm's Lord）是否落自己落陷的九分盘（Navamsa D9）星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否落九宫（Dharm）"}, {"fact_key": "九宫主（Dharm's Lord）是否落自己落陷的九分盘（Navamsa D9）星座"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的死因。", "不得把第3年与第16年之外的年份也算进本条。", "不得把九分盘（Navamsa D9）的落陷换成本盘星座的落陷。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十二宫主（Vyaya's Lord）是否落九宫（Dharm）、九宫主（Dharm's Lord）是否落自己落陷的九分盘（Navamsa D9）星座。
- 缺失即停字段：["十二宫主（Vyaya's Lord）是否落九宫（Dharm）", "九宫主（Dharm's Lord）是否落自己落陷的九分盘（Navamsa D9）星座"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v13-25`｜PDF [37]｜“If the Lord of Vyaya Bhava is in Dharm Bhava, while Dharm’s Lord is in its debilitation Navāńś, the native’s father will face his end during the 3<sup>rd</sup> , or the 16<sup>th</sup> year of the native.”


## 四路查书计划

### 支持路

- If the Lord of Vyaya Bhava is in Dharm Bhava, while Dharm’s Lord is in its debilitation Navāńś, the native’s father will face his end during the 3<sup>rd</sup> , or the 16<sup>th</sup> year of the native.
- 十二宫主落九宫 九宫主落陷九分盘 父亲第3年 第16年

### 反例或取消路

- Long-living Father. Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life
- If Dharm’s Lord is an angle and receives a Drishti from Guru, the native’s father will be a king endowed with conveyances, or be equal to a king

### 适用边界路

- If Dharm’s Lord is in its debilitation Rāśi, while his dispositor is in Dharm Bhava, the native will lose his father at the age of 26, or 30
- Evil to Father (up to Sloka 42). One’s father will incur early death, if Shani, Mangal and Chandra in their orders are in Tanu, Yuvati and Ari Bhava

### 判断方法路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- 判断父亲寿限要看九宫主（Dharm's Lord）在九分盘（Navamsa D9）中的状态

## 上游问题

- 无

## 停止条件

- 缺少十二宫主（Vyaya's Lord）落宫事实时停止。
- 缺少九宫主（Dharm's Lord）在九分盘（Navamsa D9）中的星座事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
