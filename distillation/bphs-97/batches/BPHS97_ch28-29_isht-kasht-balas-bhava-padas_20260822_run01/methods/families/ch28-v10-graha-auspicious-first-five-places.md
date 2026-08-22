---
method: ch28-v10-graha-auspicious-first-five-places
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 尊贵位次定吉：行星落前五种位置为吉

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我盘里这颗行星算吉还是算凶
- 行星入旺或落友星座算不算好

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 所考察行星（Grah）所落星座（Rāśi）的尊贵位次是九种中的哪一种

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch28-v10-graha-auspicious-first-five-places.step-001

- 动作：先定出所考察行星落在原文所列九种尊贵位次中的哪一种，再按本步断其吉凶。
- 适用范围：仅限本章 Isht 与 Kasht 体系内行星尊贵位次的吉凶定性；原文未给时间、上升或事项限定。原文另说“in other Vargas these are halved”，本步不替它改定分盘下的取值。
- 原文最小意思：行星（Grah）依其落在入旺、Mooltrikon、本星座、大友星座、友星座、中性星座、敌星座、大敌星座、落陷星座（Rāśi）这九种位置定其吉凶；落在所述前五种位置时，该行星视为吉。
- 本步骤产出事实：["所考察行星的尊贵位次吉凶定性"]
- 所需事实：["所考察行星（Grah）所落星座（Rāśi）的尊贵位次是九种中的哪一种"]
- 条件关系：{"fact_key": "所考察行星（Grah）所落星座（Rāśi）的尊贵位次是九种中的哪一种"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断具体应验事项、程度或时间。", "原文只说前五种位置为吉，不得把它改读成行星本身的吉凶星身份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所考察行星（Grah）所落星座（Rāśi）的尊贵位次是九种中的哪一种。
- 缺失即停字段：["所考察行星（Grah）所落星座（Rāśi）的尊贵位次是九种中的哪一种"]
- 原文证据：
  - `bphs-97:santhanam:ch28:v7-9`｜PDF [61]｜“due to a Grah’s placement, respectively, in exaltation, Mooltrikon, own, great friend’s, friend’s, neutral, enemy’s, great enemy’s and debilitation Rāśi”
  - `bphs-97:santhanam:ch28:v10`｜PDF [61]｜“A Grah is considered auspicious in the first five of the said places.”


## 四路查书计划

### 支持路

- A Grah is considered auspicious in the first five of the said places
- due to a Grah’s placement, respectively, in exaltation, Mooltrikon, own, great friend’s, friend’s, neutral, enemy’s, great enemy’s and debilitation Rāśi
- 行星尊贵位次 吉凶定性

### 反例或取消路

- And in the other three places it is inauspicious
- In the sixth place it is neutral, i.e. neither good nor bad
- 行星落敌星座或落陷时的凶性定性

### 适用边界路

- O Brahmin, in other Vargas these are halved
- Isht and Kasht Balas
- 尊贵位次吉凶判定在其他分盘下的取值差异

### 判断方法路

- If Subhanka is deducted from 60, Asubhanka (Asubh Pankthi, inauspicious points) will emerge
- 怎样算行星的 Subhanka 与 Asubhanka

## 上游问题

- 无

## 停止条件

- 无法确定所考察行星落在哪一种尊贵位次时停止。
- 所考察对象不在原文所列九种位置之内时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
