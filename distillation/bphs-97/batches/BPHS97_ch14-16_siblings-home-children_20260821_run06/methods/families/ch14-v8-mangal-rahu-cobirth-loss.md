---
method: ch14-v8-mangal-rahu-cobirth-loss
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Mangal 与 Rahu 同宫、三宫主落弱宫星座：失去弟妹而已得三位兄姐

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会失去弟弟妹妹
- 我上面有几个哥哥姐姐

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Mangal 是否与 Rahu 同宫
- 三宫主是否落入其弱宫星座

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch14-v8-mangal-rahu-cobirth-loss.step-001

- 动作：核对 Mangal 是否与 Rahu 同宫、三宫主是否落入弱宫星座，判断弟妹的丧失。
- 适用范围：仅限本命盘三宫兄弟姐妹存亡主题；原文未给丧失的年龄、年份或人数。
- 原文最小意思：Mangal 与 Rahu 同宫、三宫主落入弱宫星座时，会失去弟弟和／或妹妹。
- 本步骤产出事实：["弟妹丧失判定"]
- 所需事实：["Mangal 是否与 Rahu 同宫", "三宫主是否落入其弱宫星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "Mangal 是否与 Rahu 同宫"}, {"fact_key": "三宫主是否落入其弱宫星座"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断丧失的弟妹人数或发生时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Mangal 是否与 Rahu 同宫、三宫主是否落入其弱宫星座。
- 缺失即停字段：["Mangal 是否与 Rahu 同宫", "三宫主是否落入其弱宫星座"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v7-11`｜PDF [29]｜“Should Mangal be yuti with Rahu, while Sahaj’s Lord is in his debilitation Rāśi, there will be loss of younger brothers and/or sisters”

### ch14-v8-mangal-rahu-cobirth-loss.step-002

- 动作：在同一组条件成立时，核对命主已得到三位兄姐的结论。
- 适用范围：仅限本命盘三宫兄长与姐姐主题；本条只说已经得到的三位兄姐，原文未给其存亡与时间。
- 原文最小意思：Mangal 与 Rahu 同宫、三宫主落入弱宫星座时，命主已得到三位兄姐。
- 本步骤产出事实：["三位兄姐已得判定"]
- 所需事实：["Mangal 是否与 Rahu 同宫", "三宫主是否落入其弱宫星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "Mangal 是否与 Rahu 同宫"}, {"fact_key": "三宫主是否落入其弱宫星座"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把三位兄姐的数目改写成其他数目，也不得推断他们的性别比例。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Mangal 是否与 Rahu 同宫、三宫主是否落入其弱宫星座。
- 缺失即停字段：["Mangal 是否与 Rahu 同宫", "三宫主是否落入其弱宫星座"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v7-11`｜PDF [29]｜“Should Mangal be yuti with Rahu, while Sahaj’s Lord is in his debilitation Rāśi, there will be loss of younger brothers and/or sisters, while three elder brothers and/or sisters were attained by the native.”


## 四路查书计划

### 支持路

- 火星与罗睺同宫 三宫主落陷 失去弟妹

### 反例或取消路

- 三宫主入角宫 火星入旺 兄弟姐妹众多

### 适用边界路

- 弟妹丧失判断的适用边界

### 判断方法路

- 判断弟妹丧失与兄姐人数的步骤

## 上游问题

- 无

## 停止条件

- 缺少 Mangal 与 Rahu 的同宫事实时停止。
- 缺少三宫主是否落弱宫星座的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
