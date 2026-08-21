---
method: ch14-v7-elder-sister-younger-brothers
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Budh 落三宫、三宫主与 Chandra 同宫、Mangal 与 Shani 同宫：有姐姐与弟弟，第三个弟弟去世

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我上面有没有姐姐
- 我下面会不会有弟弟
- 我的弟弟会不会出事

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Budh 是否落三宫
- 三宫主是否与 Chandra 同宫
- Mangal 是否与 Shani 同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch14-v7-elder-sister-younger-brothers.step-001

- 动作：核对 Budh 是否落三宫、三宫主是否与 Chandra 同宫、指示星 Mangal 是否与 Shani 同宫，判断姐姐与弟弟。
- 适用范围：仅限本命盘三宫兄弟姐妹主题；本条只讲这一组三星条件下的姐姐与弟弟，原文未给时间限定。
- 原文最小意思：Budh 落三宫、三宫主与 Chandra 同宫、指示星 Mangal 与 Shani 同宫时，已有一位姐姐出生，并且会有弟弟。
- 本步骤产出事实：["有姐姐并有弟弟的判定"]
- 所需事实：["Budh 是否落三宫", "三宫主是否与 Chandra 同宫", "Mangal 是否与 Shani 同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "Budh 是否落三宫"}, {"fact_key": "三宫主是否与 Chandra 同宫"}, {"fact_key": "Mangal 是否与 Shani 同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断姐姐与弟弟的具体数目或出生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Budh 是否落三宫、三宫主是否与 Chandra 同宫、Mangal 是否与 Shani 同宫。
- 缺失即停字段：["Budh 是否落三宫", "三宫主是否与 Chandra 同宫", "Mangal 是否与 Shani 同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v7-11`｜PDF [29]｜“If Budh is in Sahaj Bhava, while Sahaj’s Lord and Chandra are together, as the indicator (Mangal) joins Shani, the effects are: there occurred the birth of an elder sister and there will be younger brothers.”

### ch14-v7-elder-sister-younger-brothers.step-002

- 动作：在同一组三星条件成立时，核对第三个弟弟的去世结论。
- 适用范围：仅限本命盘三宫兄弟姐妹主题；本条只针对同偈同一组条件下排行第三的弟弟，原文未给去世的年龄或年份。
- 原文最小意思：Budh 落三宫、三宫主与 Chandra 同宫、指示星 Mangal 与 Shani 同宫时，第三个弟弟会去世。
- 本步骤产出事实：["第三个弟弟去世的判定"]
- 所需事实：["Budh 是否落三宫", "三宫主是否与 Chandra 同宫", "Mangal 是否与 Shani 同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "Budh 是否落三宫"}, {"fact_key": "三宫主是否与 Chandra 同宫"}, {"fact_key": "Mangal 是否与 Shani 同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把第三个弟弟的去世推广到其他排行的兄弟姐妹。", "不得据此推断去世发生的年龄或年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Budh 是否落三宫、三宫主是否与 Chandra 同宫、Mangal 是否与 Shani 同宫。
- 缺失即停字段：["Budh 是否落三宫", "三宫主是否与 Chandra 同宫", "Mangal 是否与 Shani 同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v7-11`｜PDF [29]｜“If Budh is in Sahaj Bhava, while Sahaj’s Lord and Chandra are together, as the indicator (Mangal) joins Shani, the effects are: there occurred the birth of an elder sister and there will be younger brothers. Furthermore, the third brother will die.”


## 四路查书计划

### 支持路

- 水星落三宫 三宫主与月亮同宫 火星土星同宫 姐姐 弟弟

### 反例或取消路

- 三宫吉星 兄弟姐妹得保全

### 适用边界路

- 兄弟姐妹数目判断的适用边界

### 判断方法路

- 判断兄弟姐妹人数与排行的步骤

## 上游问题

- 无

## 停止条件

- 缺少 Budh 落宫事实时停止。
- 缺少三宫主与 Chandra 的同宫事实时停止。
- 缺少 Mangal 与 Shani 的同宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
