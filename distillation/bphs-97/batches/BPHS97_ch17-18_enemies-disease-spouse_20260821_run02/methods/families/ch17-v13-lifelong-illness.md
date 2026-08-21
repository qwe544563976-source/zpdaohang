---
method: ch17-v13-lifelong-illness
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 终生疾病：土星与罗睺同宫、六宫主及六宫皆与凶星同处

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我是不是一辈子病不断
- 我的健康底子怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星
- 土星（Shani）是否与罗睺（Rahu）同宫
- 六宫主（Ari's Lord）是否与凶星同宫
- 六宫（Ari）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v13-lifelong-illness.step-001

- 动作：核对土星与罗睺的同宫，以及六宫主与六宫和凶星的关系。
- 适用范围：仅限本命盘终生疾病主题；原文只说一生受疾病困扰，未指明病名与起病年龄。
- 原文最小意思：土星与罗睺同宫、六宫主与凶星同宫、六宫也被凶星占据时，一生受疾病困扰。
- 本步骤产出事实：["终生疾病判定"]
- 所需事实：["本盘中哪些行星被判为凶星", "土星（Shani）是否与罗睺（Rahu）同宫", "六宫主（Ari's Lord）是否与凶星同宫", "六宫（Ari）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "土星（Shani）是否与罗睺（Rahu）同宫"}, {"fact_key": "六宫主（Ari's Lord）是否与凶星同宫"}, {"fact_key": "六宫（Ari）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断病名、致死与否或具体年龄。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星、土星（Shani）是否与罗睺（Rahu）同宫、六宫主（Ari's Lord）是否与凶星同宫、六宫（Ari）是否被凶星占据。
- 缺失即停字段：["本盘中哪些行星被判为凶星", "土星（Shani）是否与罗睺（Rahu）同宫", "六宫主（Ari's Lord）是否与凶星同宫", "六宫（Ari）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v13-19.5`｜PDF [32, 33]｜“The native will be afflicted by illness throughout life, if Shani is with Rahu, while Ari Lord and 6<sup>th</sup> Bhava are yuti with malefics.”


## 四路查书计划

### 支持路

- The native will be afflicted by illness throughout life, if Shani is with Rahu Ari Lord 6th Bhava yuti with malefics
- 土星罗睺同宫 六宫主凶星 一生疾病

### 反例或取消路

- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age
- Effects of Ari’s Lord in Various Bhavas
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Indications of Ari Bhava doubts about death enemies
- 判断长期健康应检查六宫与哪些凶星的关系

## 上游问题

- 无

## 停止条件

- 缺少本盘凶星名册事实时停止。
- 缺少土星与罗睺同宫事实时停止。
- 缺少六宫主与凶星同宫事实时停止。
- 缺少六宫被凶星占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
