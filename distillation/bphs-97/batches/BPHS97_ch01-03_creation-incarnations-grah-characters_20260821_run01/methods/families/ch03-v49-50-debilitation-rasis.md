---
method: ch03-v49-50-debilitation-rasis
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 落陷：入旺星座起第七个星座与深度落陷度数

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我盘里哪颗行星落陷
- 落陷星座怎么定 深度落陷是几度

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中待判定尊贵的行星落在哪个星座（Rāśi）
- 本盘中待判定尊贵的行星的入旺星座是哪个星座
- 本盘中待判定尊贵的行星在该星座内的度数是多少

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v49-50-debilitation-rasis.step-001

- 动作：自待判定行星的入旺星座起数到第七个星座，判断它是否落陷。
- 适用范围：第3章入旺与落陷条；落陷星座由入旺星座推出，本偈只给这一种推法。
- 原文最小意思：从其入旺星座起的第七个（seventh）星座，每颗行星在该处落陷。
- 本步骤产出事实：["行星落陷星座判定"]
- 所需事实：["本盘中待判定尊贵的行星落在哪个星座（Rāśi）", "本盘中待判定尊贵的行星的入旺星座是哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中待判定尊贵的行星落在哪个星座（Rāśi）"}, {"fact_key": "本盘中待判定尊贵的行星的入旺星座是哪个星座"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出落陷可被什么化解——本偈没有给任何取消条款。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中待判定尊贵的行星落在哪个星座（Rāśi）、本盘中待判定尊贵的行星的入旺星座是哪个星座。
- 缺失即停字段：["本盘中待判定尊贵的行星落在哪个星座（Rāśi）", "本盘中待判定尊贵的行星的入旺星座是哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v49-50`｜PDF [12]｜“And in the seventh Rashifrom the said exaltation Rashieach Grah has its own debilitation.”

### ch03-v49-50-debilitation-rasis.step-002

- 动作：取待判定行星在该星座内的度数，按深度入旺的同一组度数判断它是否处于深度落陷。
- 适用范围：第3章入旺与落陷条；度数表承本偈前句的深度入旺度数。
- 原文最小意思：深度入旺的同一组度数（degrees）同样适用于深度落陷。
- 本步骤产出事实：["行星深度落陷度数判定"]
- 所需事实：["本盘中待判定尊贵的行星在该星座内的度数是多少", "行星落陷星座判定"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中待判定尊贵的行星在该星座内的度数是多少"}, {"fact_key": "行星落陷星座判定"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出偏离深度落陷度数后凶效如何递减——本偈只给度数本身。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中待判定尊贵的行星在该星座内的度数是多少、行星落陷星座判定。
- 缺失即停字段：["本盘中待判定尊贵的行星在该星座内的度数是多少", "行星落陷星座判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v49-50`｜PDF [12]｜“The same degrees of deep exaltation apply to deep fall.”


## 四路查书计划

### 支持路

- And in the seventh Rashifrom the said exaltation Rashieach Grah has its own debilitation. The same degrees of deep exaltation apply to deep fall
- 落陷星座 入旺起第七个星座 深度落陷

### 反例或取消路

- In this case Surya, being exalted, or in a friendly Rāśi, is not a malefic. He is a malefic, if in debilitation, or in an enemy’s Rāśi
- 落陷与入旺在断吉凶时的相反用法

### 适用边界路

- From Surya to Shani no one is exalted in the above-mentioned exaltation Rāśis, nor debilitated in the above-mentioned debilitation Rāśis
- 影曜的落陷表不适用于七曜

### 判断方法路

- The good effects are nil in debilitation, or enemy’s camp
- 落陷之后吉效怎么折算

## 上游问题

- 无

## 停止条件

- 缺少待判定行星的入旺星座时停止。
- 缺少行星在星座内的度数时，深度落陷一步停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
