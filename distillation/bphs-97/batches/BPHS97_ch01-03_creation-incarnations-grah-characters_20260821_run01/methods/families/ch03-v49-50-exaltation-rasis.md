---
method: ch03-v49-50-exaltation-rasis
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 入旺：七曜各自的入旺星座与深度入旺度数

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我盘里哪颗行星入旺
- 各行星在哪个星座入旺 深度入旺是几度

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中待判定尊贵的行星落在哪个星座（Rāśi）
- 本盘中待判定尊贵的行星在该星座内的度数是多少

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v49-50-exaltation-rasis.step-001

- 动作：取待判定行星所落星座，对照七曜的入旺星座表，判断它是否入旺。
- 适用范围：第3章入旺与落陷条；本表只列自太阳起的七曜，未列 Rahu、Ketu。
- 原文最小意思：七曜（seven Grahas）自太阳（Surya）起，入旺星座依次是 Mesh、Vrishabh、Makar、Kanya、Kark、Meen 与 Tula。
- 本步骤产出事实：["行星入旺星座判定"]
- 所需事实：["本盘中待判定尊贵的行星落在哪个星座（Rāśi）"]
- 条件关系：{"fact_key": "本盘中待判定尊贵的行星落在哪个星座（Rāśi）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把入旺读成本星座（own Bhava）或 Mooltrikon——本偈只给入旺星座。", "不得据本条推出 Rahu 与 Ketu 的入旺星座——本表只列七曜。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中待判定尊贵的行星落在哪个星座（Rāśi）。
- 缺失即停字段：["本盘中待判定尊贵的行星落在哪个星座（Rāśi）"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v49-50`｜PDF [12]｜“For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula.”

### ch03-v49-50-exaltation-rasis.step-002

- 动作：取待判定行星在该星座内的度数，对照深度入旺度数表，判断它是否处于深度入旺。
- 适用范围：第3章入旺与落陷条；度数次序承本偈前句自太阳起的七曜次序。
- 原文最小意思：深度入旺的度数（degrees）依次是 10、3、28、15、5、27 与 20。
- 本步骤产出事实：["行星深度入旺度数判定"]
- 所需事实：["本盘中待判定尊贵的行星在该星座内的度数是多少", "行星入旺星座判定"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中待判定尊贵的行星在该星座内的度数是多少"}, {"fact_key": "行星入旺星座判定"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出偏离深度入旺度数后吉效如何递减——本偈只给度数本身。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中待判定尊贵的行星在该星座内的度数是多少、行星入旺星座判定。
- 缺失即停字段：["本盘中待判定尊贵的行星在该星座内的度数是多少", "行星入旺星座判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v49-50`｜PDF [12]｜“The deepest exaltation degrees are, respectively, 10, 3, 28, 15, 5, 27 and 20 in those Rāśis.”


## 四路查书计划

### 支持路

- For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula
- The deepest exaltation degrees are, respectively, 10, 3, 28, 15, 5, 27 and 20 in those Rāśis
- 七曜入旺星座 深度入旺度数

### 反例或取消路

- 无

### 适用边界路

- From Surya to Shani no one is exalted in the above-mentioned exaltation Rāśis, nor debilitated in the above-mentioned debilitation Rāśis
- 影曜的入旺表不适用于七曜

### 判断方法路

- 60, 45, 30, 22, 15, 8, 4, 2 and 0 are the Subhankas (Subha Griha Pankthis, benefic points), due to a Grah’s placement, respectively, in exaltation, Mooltrikon, own, great friend’s, friend’s, neutral, enemy’s, great enemy’s and debilitation Rāśi
- A Grah in exaltation gives fully good effects
- 入旺之后怎么折算吉效

## 上游问题

- 无

## 停止条件

- 缺少待判定行星所落星座时停止。
- 缺少行星在星座内的度数时，深度入旺一步停止。
- 本条只给入旺状态，没有给吉凶结果，要下断语必须另找原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
