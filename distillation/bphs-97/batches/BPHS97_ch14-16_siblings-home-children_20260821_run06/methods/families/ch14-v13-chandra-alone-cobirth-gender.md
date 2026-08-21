---
method: ch14-v13-chandra-alone-cobirth-gender
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Chandra 单独落三宫：受阳性行星相照主弟弟，受 Shukra 相照主妹妹

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会有弟弟还是妹妹
- 月亮单独落在三宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Chandra 是否单独落三宫
- 三宫是否受阳性行星相照
- 三宫是否受 Shukra 相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch14-v13-chandra-alone-cobirth-gender.step-001

- 动作：核对 Chandra 是否单独落三宫并受阳性行星相照。
- 适用范围：仅限本命盘三宫兄弟姐妹性别主题；原文未给弟弟的数目与时间。
- 原文最小意思：Chandra 单独落三宫并受阳性行星相照时，会有弟弟。
- 本步骤产出事实：["Chandra 单独落三宫主有弟弟判定"]
- 所需事实：["Chandra 是否单独落三宫", "三宫是否受阳性行星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "Chandra 是否单独落三宫"}, {"fact_key": "三宫是否受阳性行星相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断弟弟的数目或出生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Chandra 是否单独落三宫、三宫是否受阳性行星相照。
- 缺失即停字段：["Chandra 是否单独落三宫", "三宫是否受阳性行星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v12-13`｜PDF [29]｜“If Chandra is lonely placed in Sahaj Bhava with Drishti of male Grahas, there will be younger brothers”

### ch14-v13-chandra-alone-cobirth-gender.step-002

- 动作：核对 Chandra 单独落三宫时是否受 Shukra 相照。
- 适用范围：仅限本命盘三宫兄弟姐妹性别主题；本条承接同句“Chandra 单独落三宫”的前提，原文未给妹妹的数目与时间。
- 原文最小意思：Chandra 单独落三宫，受 Shukra 相照时，主有妹妹。
- 本步骤产出事实：["Chandra 单独落三宫主有妹妹判定"]
- 所需事实：["Chandra 是否单独落三宫", "三宫是否受 Shukra 相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "Chandra 是否单独落三宫"}, {"fact_key": "三宫是否受 Shukra 相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断妹妹的数目或出生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Chandra 是否单独落三宫、三宫是否受 Shukra 相照。
- 缺失即停字段：["Chandra 是否单独落三宫", "三宫是否受 Shukra 相照"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v12-13`｜PDF [29]｜“If Chandra is lonely placed in Sahaj Bhava with Drishti of male Grahas, there will be younger brothers, while the Drishti of Shukra denotes younger sisters.”


## 四路查书计划

### 支持路

- 月亮单独落三宫 阳性行星相照 弟弟 金星相照 妹妹

### 反例或取消路

- 三宫凶星 弟妹被毁

### 适用边界路

- 月亮独落三宫判断的适用边界

### 判断方法路

- 判断弟妹性别的步骤

## 上游问题

- 无

## 停止条件

- 缺少 Chandra 是否单独落三宫的事实时停止。
- 缺少三宫相照行星的阴阳与 Shukra 相照事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
