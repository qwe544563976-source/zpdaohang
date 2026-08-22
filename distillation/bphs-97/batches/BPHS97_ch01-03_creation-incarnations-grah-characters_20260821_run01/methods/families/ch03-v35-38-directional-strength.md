---
method: ch03-v35-38-directional-strength
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 方位强弱：东、南、西、北各有得力之曜

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我盘里哪颗行星因所处方位而有力
- 东南西北各是哪颗行星得力

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星处于东方（East）
- 本盘中哪些行星处于南方（South）
- 本盘中哪些行星处于西方（West）
- 本盘中哪些行星处于北方（North）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v35-38-directional-strength.step-001

- 动作：核对本盘中处于东方（East）的行星，判断哪些行星因该方位而有力。
- 适用范围：第3章诸曜强弱条；原文只列各方位得力之曜，未给判定方位的算法，也未给强弱的量值。
- 原文最小意思：在东方（East）有力的是水星（Budh）与木星（Guru）。
- 本步骤产出事实：["东方（East）方位有力之曜判定"]
- 所需事实：["本盘中哪些行星处于东方（East）"]
- 条件关系：{"fact_key": "本盘中哪些行星处于东方（East）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条自行认定方位对应哪几个宫——本偈没有给方位的判定法。", "不得据本条推出方位强弱的具体分值或与其他强弱来源的合并算法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星处于东方（East）。
- 缺失即停字段：["本盘中哪些行星处于东方（East）"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v35-38`｜PDF [11]｜“Strong in the East are Budh and Guru.”

### ch03-v35-38-directional-strength.step-002

- 动作：核对本盘中处于南方（South）与西方（West）的行星，判断哪些行星因该方位而有力。
- 适用范围：第3章诸曜强弱条；原文只列各方位得力之曜，未给判定方位的算法，也未给强弱的量值。
- 原文最小意思：在南方（South）有力的是太阳（Surya）与火星（Mangal），而在西方（West）得力的只有土星（Shani）。
- 本步骤产出事实：["南方（South）与西方（West）方位有力之曜判定"]
- 所需事实：["本盘中哪些行星处于南方（South）", "本盘中哪些行星处于西方（West）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星处于南方（South）"}, {"fact_key": "本盘中哪些行星处于西方（West）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条自行认定方位对应哪几个宫——本偈没有给方位的判定法。", "不得把「西方唯有土星」读成土星在别处一定无力。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星处于南方（South）、本盘中哪些行星处于西方（West）。
- 缺失即停字段：["本盘中哪些行星处于南方（South）", "本盘中哪些行星处于西方（West）"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v35-38`｜PDF [11]｜“Surya and Mangal are so in the South, while Shani is the only Grah, that derives strength in the West.”

### ch03-v35-38-directional-strength.step-003

- 动作：核对本盘中处于北方（North）的行星，判断哪些行星因该方位而具足强力。
- 适用范围：第3章诸曜强弱条；原文只列各方位得力之曜，未给判定方位的算法，也未给强弱的量值。
- 原文最小意思：在北方（North）时，月亮（Chandra）与金星（Shukra）具足强力。
- 本步骤产出事实：["北方（North）方位有力之曜判定"]
- 所需事实：["本盘中哪些行星处于北方（North）"]
- 条件关系：{"fact_key": "本盘中哪些行星处于北方（North）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条自行认定方位对应哪几个宫——本偈没有给方位的判定法。", "不得据本条推出交点（Rahu、Ketu）的方位强弱——本偈只列七曜。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星处于北方（North）。
- 缺失即停字段：["本盘中哪些行星处于北方（North）"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v35-38`｜PDF [11]｜“Chandra and Shukra are endowed with vigour, when in the North.”


## 四路查书计划

### 支持路

- Strong in the East are Budh and Guru
- Chandra and Shukra are endowed with vigour, when in the North
- 诸曜方位强弱 东方 南方 西方 北方

### 反例或取消路

- 无

### 适用边界路

- These strengths are computed for the seven Grahas from Surya to Shani. The nodes are not considered
- 方位强弱只算七曜 不含交点

### 判断方法路

- Dig Bal. Deduct Bandhu Bhava (Nadir) from the longitudes of Surya and Mangal, Yuvati Bhava from that of Guru and Budh
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional)
- 方位强弱怎么算 Dig Bal

## 上游问题

- 无

## 停止条件

- 缺少本盘各方位所处行星的事实时停止。
- 原文没有给方位的判定法，方位无法确定即停判。
- 本条只说哪几颗曜在该方位有力，没有给强弱数值，要量化必须另查 Shad Bal 原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
