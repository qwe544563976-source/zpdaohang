---
method: ch12-v12-14-first-decanate-limb-order
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第一个三分盘上升：各宫对应头眼耳鼻太阳穴下巴脸

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身上哪些部位由哪一宫管
- 上升第一个三分盘代表哪些身体部位

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘一宫（Lagn）是否落在所在星座的第一个三分盘（Drekkana D3）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch12-v12-14-first-decanate-limb-order.step-001

- 动作：核对上升是否落在所在星座的第一个三分盘（Drekkana D3），若是则取这一组宫位与肢体的对应。
- 适用范围：仅限本命盘上升三分盘（Drekkana D3）与身体部位的对应；原文只给出肢体次序，没有说这一串从哪一宫起算。
- 原文最小意思：上升落在星座的第一个三分盘（first decanate）时，各宫依次代表头、眼、耳、鼻、太阳穴、下巴和脸。
- 本步骤产出事实：["第一个三分盘上升时的宫位肢体对应"]
- 所需事实：["本盘一宫（Lagn）是否落在所在星座的第一个三分盘（Drekkana D3）"]
- 条件关系：{"fact_key": "本盘一宫（Lagn）是否落在所在星座的第一个三分盘（Drekkana D3）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这一组肢体次序用在其他三分盘上升的盘上。", "不得自行指定这一串肢体从哪一宫起算，原文没有写。", "不得据此直接断出疾病或吉凶，本偈只给对应关系。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘一宫（Lagn）是否落在所在星座的第一个三分盘（Drekkana D3）。
- 缺失即停字段：["本盘一宫（Lagn）是否落在所在星座的第一个三分盘（Drekkana D3）"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v12-14`｜PDF [27]｜“Head, eyes, ears, nose, temple, chin and face is the order of limbs, denoted (by the various Bhavas), when the first decanate of a Rashiascends.”


## 四路查书计划

### 支持路

- Head, eyes, ears, nose, temple, chin and face is the order of limbs, denoted (by the various Bhavas), when the first decanate of a Rashiascends.
- 上升第一个三分盘 宫位与肢体对应

### 反例或取消路

- 无

### 适用边界路

- One third of a Rashiis called Dreshkan. These are totally 36, counted from Mesh, repeating thrice at the rate of 12 per round
- Dreshkan Bal. Male, female and hermaphrodite Grahas, respectively, get a quarter Rupa according to placements in the first, second and third decanates
- The Sixteen Divisions of a Rāśi

### 判断方法路

- The physique from Lagna, wealth from Hora, happiness through co-born from Dreshkan
- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- 判断身体部位要先看上升落第几个三分盘

## 上游问题

- 无

## 停止条件

- 缺少上升是否落第一个三分盘的事实时停止。
- 肢体次序的起算宫位原文未给，具体宫位对应未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
