---
method: ch16-v10-three-mothers-two-fathers
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 由三母或两父抚养：太阳与月亮同星座且同九分盘

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我小时候是不是被别人带大的
- 我会不会有继父继母

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）与月亮（Chandra）是否同落一个星座
- 太阳（Surya）与月亮（Chandra）是否同落一个九分盘（Navāńś）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch16-v10-three-mothers-two-fathers.step-001

- 动作：核对太阳与月亮是否同落一个星座，并核对两者是否同落一个九分盘。
- 适用范围：仅限本命盘抚养者主题；原文只说三位母亲或两位父亲，未给年龄、年份或原因。
- 原文最小意思：太阳（Surya）与月亮（Chandra）同落一个星座、并同落同一九分盘（Navāńś）时，此人由三位母亲、或两位父亲抚养。
- 本步骤产出事实：["日月同座同九分盘多抚养者判定"]
- 所需事实：["太阳（Surya）与月亮（Chandra）是否同落一个星座", "太阳（Surya）与月亮（Chandra）是否同落一个九分盘（Navāńś）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）与月亮（Chandra）是否同落一个星座"}, {"fact_key": "太阳（Surya）与月亮（Chandra）是否同落一个九分盘（Navāńś）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把三位母亲或两位父亲的人数改成其他数字。", "不得据此推断父母的生死或婚姻状况。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）与月亮（Chandra）是否同落一个星座、太阳（Surya）与月亮（Chandra）是否同落一个九分盘（Navāńś）。
- 缺失即停字段：["太阳（Surya）与月亮（Chandra）是否同落一个星座", "太阳（Surya）与月亮（Chandra）是否同落一个九分盘（Navāńś）"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v10`｜PDF [30, 31]｜“Should Surya and Chandra be together in a Rashiand in the same Navāńś, the native will be brought up by three mothers, or two fathers.”


## 四路查书计划

### 支持路

- Surya and Chandra together in same Navāńś three mothers two fathers
- 太阳月亮同星座 同九分盘 三位母亲 两位父亲

### 反例或取消路

- Surya Chandra in different Rāśis parents
- 日月不同星座 抚养者 反例

### 适用边界路

- Navāńś sameness requirement scope
- 同九分盘条件的适用边界

### 判断方法路

- how to compare Rāśi and Navāńś of Surya and Chandra
- 怎样比对太阳与月亮的星座和九分盘

## 上游问题

- 无

## 停止条件

- 缺少太阳与月亮的星座事实时停止。
- 缺少太阳与月亮的九分盘事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
