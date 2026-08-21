---
method: ch20-v13-25-lose-father-age-26-30
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 命主26岁或30岁失去父亲：九宫主落陷、其星座主落九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 父亲会在我二三十岁时离开吗
- 九宫主落陷又其星座主落九宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否落陷
- 九宫主（Dharm's Lord）的星座主是否落九宫（Dharm）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v13-25-lose-father-age-26-30.step-001

- 动作：核对九宫主（Dharm's Lord）是否落在自己落陷的星座（Rāśi），并核对九宫主的星座主是否落九宫（Dharm）。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文以「Combinations for Father’s Death」立目，末句「Thus the Jyotishis may know the effects」把这组组合交由 Jyotishis 判读；原文未给上升限定。原文「his dispositor」的 his，句内先行词是九宫主（Dharm's Lord）。
- 原文最小意思：九宫主（Dharm's Lord）落自己落陷的星座（Rāśi）、且其星座主落九宫（Dharm）时，命主在26岁或30岁失去父亲。
- 本步骤产出事实：["九宫主落陷且其星座主落九宫主26岁或30岁失去父亲判定"]
- 所需事实：["九宫主（Dharm's Lord）是否落陷", "九宫主（Dharm's Lord）的星座主是否落九宫（Dharm）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否落陷"}, {"fact_key": "九宫主（Dharm's Lord）的星座主是否落九宫（Dharm）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的死因。", "不得把26岁与30岁之外的年岁也算进本条。", "不得把落陷星座（Rāśi）读成落陷九分盘（Navamsa D9）星座。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否落陷、九宫主（Dharm's Lord）的星座主是否落九宫（Dharm）。
- 缺失即停字段：["九宫主（Dharm's Lord）是否落陷", "九宫主（Dharm's Lord）的星座主是否落九宫（Dharm）"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v13-25`｜PDF [37]｜“If Dharm’s Lord is in its debilitation Rāśi, while his dispositor is in Dharm Bhava, the native will lose his father at the age of 26, or 30.”


## 四路查书计划

### 支持路

- If Dharm’s Lord is in its debilitation Rāśi, while his dispositor is in Dharm Bhava, the native will lose his father at the age of 26, or 30.
- 九宫主落陷星座 星座主落九宫 26岁 30岁 失去父亲

### 反例或取消路

- Long-living Father. Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life
- Fortunate (Affluent) Father. If Dharm’s Lord is with strength, as Shukra is in Dharm, while Guru is in an angle from Tanu Bhava, the native’s father is fortunate

### 适用边界路

- If the Lord of Vyaya Bhava is in Dharm Bhava, while Dharm’s Lord is in its debilitation Navāńś, the native’s father will face his end during the 3<sup>rd</sup> , or the 16<sup>th</sup> year of the native
- Indigent Father. If Dharm’s Lord is debilitated, while the 2<sup>nd</sup> and/or the 4<sup>th</sup> from Dharm Bhava is occupied by Mangal, the native’s father is poor

### 判断方法路

- Dharm Bhava and the 9<sup>th</sup> from Surya deal with one’s father
- 判断失去父亲的年岁要看九宫主（Dharm's Lord）落陷与其星座主的位置

## 上游问题

- 无

## 停止条件

- 缺少九宫主（Dharm's Lord）是否落陷的事实时停止。
- 缺少九宫主星座主落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
