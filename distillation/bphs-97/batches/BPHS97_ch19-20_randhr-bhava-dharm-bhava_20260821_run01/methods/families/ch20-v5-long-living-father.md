---
method: ch20-v5-long-living-father
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲长寿：九宫主深度入旺、金星落上升起的角宫、木星落九分盘上升起的第九宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲寿命长不长
- 九宫主深度入旺代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否深度入旺
- 金星（Shukra）是否落上升宫（Tanu Bhava）起算的角宫
- 木星（Guru）是否落九分盘（Navamsa D9）上升起算的第九宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v5-long-living-father.step-001

- 动作：核对九宫主（Dharm's Lord）是否深度入旺、金星（Shukra）是否落自上升宫起算的角宫、木星（Guru）是否落自九分盘上升起算的第九宫。
- 适用范围：仅限本命盘九宫（Dharm Bhava）主题下父亲的寿命；原文把角宫的起算宫位写明为 Tanu Bhava，把第九宫的起算点写明为 Navāńś Lagna（九分盘上升）；原文未给具体寿数。
- 原文最小意思：九宫主深度入旺、金星落自上升宫（Tanu Bhava）起算的角宫、木星落自九分盘上升起算的第九宫时，命主的父亲享长寿。
- 本步骤产出事实：["九宫主深度入旺金木得位的父亲长寿判定"]
- 所需事实：["九宫主（Dharm's Lord）是否深度入旺", "金星（Shukra）是否落上升宫（Tanu Bhava）起算的角宫", "木星（Guru）是否落九分盘（Navamsa D9）上升起算的第九宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否深度入旺"}, {"fact_key": "金星（Shukra）是否落上升宫（Tanu Bhava）起算的角宫"}, {"fact_key": "木星（Guru）是否落九分盘（Navamsa D9）上升起算的第九宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把木星的第九宫改从本命上升起算——原文写明从九分盘上升起。", "不得把「深度入旺」放宽成一般的入旺。", "不得据此推出父亲的具体寿数年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否深度入旺、金星（Shukra）是否落上升宫（Tanu Bhava）起算的角宫、木星（Guru）是否落九分盘（Navamsa D9）上升起算的第九宫。
- 缺失即停字段：["九宫主（Dharm's Lord）是否深度入旺", "金星（Shukra）是否落上升宫（Tanu Bhava）起算的角宫", "木星（Guru）是否落九分盘（Navamsa D9）上升起算的第九宫"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v5`｜PDF [36]｜“Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life.”


## 四路查书计划

### 支持路

- Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9th from Navāńś Lagna, the father of the native will enjoy a long span of life
- 九宫主深度入旺 金星角宫 木星九分盘上升起第九宫 父亲长寿

### 反例或取消路

- Combinations for Father’s Death. The father of the native would have passed away prior to the native’s birth, if Surya is in Ari, Randhr, or Vyaya Bhava
- If Dharm’s Lord is debilitated, while the 2nd and/or the 4th from Dharm Bhava is occupied by Mangal, the native’s father is poor

### 适用边界路

- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines
- The Sixteen Divisions of a Rāśi Navāńś

### 判断方法路

- these are the effects related to Dharm Bhava. I have explained briefly. These may be estimated with the help of the state of the Lords of Lagn and Dharm Bhava
- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- 九分盘上升怎么起算

## 上游问题

- 无

## 停止条件

- 缺少九宫主深度入旺事实时停止。
- 缺少金星或木星落宫事实时停止。
- 九分盘（Navamsa D9）盘面缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
