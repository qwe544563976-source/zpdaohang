---
method: ch17-v23-blood-vessel-age-18-22
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第18年与第22年的血管与泌尿疾病：八宫主与罗睺会于八宫起的角宫或三角宫、且八宫主在九分盘落八宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我十八到二十二岁健康怎么样
- 血管和泌尿方面会不会出问题

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫主（Randhr's Lord）是否与罗睺（Rahu）同宫
- 八宫主（Randhr's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）

## 按情况检查的事实

- 八宫主（Randhr's Lord）与罗睺（Rahu）会合之处是否为八宫（Randhr）起的角宫
- 八宫主（Randhr's Lord）与罗睺（Rahu）会合之处是否为八宫（Randhr）起的三角宫

## 依赖方法

- 无

## 执行步骤

### ch17-v23-blood-vessel-age-18-22.step-001

- 动作：核对八宫主与罗睺的会合位置（自八宫起算）以及八宫主在九分盘（Navamsa D9）中的落宫。
- 适用范围：仅限本命盘血管与泌尿疾病主题；原文的角宫、三角宫自八宫起算，年份写作第18年与第22年。
- 原文最小意思：八宫主与罗睺在八宫起的角宫或三角宫会合、且八宫主在九分盘中落八宫时，第18年与第22年会有血管肿胀、泌尿疾病等。
- 本步骤产出事实：["八宫主罗睺会合的血管泌尿疾病判定"]
- 所需事实：["八宫主（Randhr's Lord）是否与罗睺（Rahu）同宫", "八宫主（Randhr's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否与罗睺（Rahu）同宫"}, {"fact_key": "八宫主（Randhr's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）"}]}, {"operator": "OR", "operands": [{"fact_key": "八宫主（Randhr's Lord）与罗睺（Rahu）会合之处是否为八宫（Randhr）起的角宫"}, {"fact_key": "八宫主（Randhr's Lord）与罗睺（Rahu）会合之处是否为八宫（Randhr）起的三角宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否与罗睺（Rahu）同宫"}, {"fact_key": "八宫主（Randhr's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）"}]}, "required_fact_keys": ["八宫主（Randhr's Lord）与罗睺（Rahu）会合之处是否为八宫（Randhr）起的角宫"], "branch_condition_logic": {"fact_key": "八宫主（Randhr's Lord）与罗睺（Rahu）会合之处是否为八宫（Randhr）起的角宫"}, "selection_group": "ch17-v23-blood-vessel-age-18-22.step-001:join-position", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）与罗睺（Rahu）会合之处是否为八宫（Randhr）起的角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否与罗睺（Rahu）同宫"}, {"fact_key": "八宫主（Randhr's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）"}]}, "required_fact_keys": ["八宫主（Randhr's Lord）与罗睺（Rahu）会合之处是否为八宫（Randhr）起的三角宫"], "branch_condition_logic": {"fact_key": "八宫主（Randhr's Lord）与罗睺（Rahu）会合之处是否为八宫（Randhr）起的三角宫"}, "selection_group": "ch17-v23-blood-vessel-age-18-22.step-001:join-position", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）与罗睺（Rahu）会合之处是否为八宫（Randhr）起的三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把角宫、三角宫改从上升起算。", "不得据此推断病症名称之外的其他疾病或年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否与罗睺（Rahu）同宫、八宫主（Randhr's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）。
- 缺失即停字段：["八宫主（Randhr's Lord）是否与罗睺（Rahu）同宫", "八宫主（Randhr's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v23-25`｜PDF [33]｜“If 8<sup>th</sup> Lord joins Rahu in an angle/trine from Randhr Bhava and be in Randhr in Navamsa, the subject will be troubled by swelling of blood vessels, urinary disorders etc. during the 18<sup>th</sup> year and the 22<sup>nd</sup> year.”


## 四路查书计划

### 支持路

- If 8th Lord joins Rahu in an angle/trine from Randhr Bhava and be in Randhr in Navamsa swelling of blood vessels urinary disorders
- 八宫主 罗睺 角宫 三角宫 九分盘 血管 泌尿

### 反例或取消路

- Guru in similar case will destroy any disease
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed

### 适用边界路

- Divisional Considerations Navamsa 九分盘的取用范围
- Evils, causing premature end, exist up to the 24th year of one’s age

### 判断方法路

- 判断分盘落宫应怎样与本命盘配合

## 上游问题

- 无

## 停止条件

- 缺少八宫主与罗睺同宫事实时停止。
- 缺少八宫主在九分盘落宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
