---
method: ch17-v9-lagna-lords-graha-diseases
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 疾病总论：上升宫聚六宫主与八宫主时，同落其中的行星各主一类病害

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我容易得哪一类病
- 上升宫聚了六宫主八宫主会怎么样
- 哪颗星在上升会带来什么病

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 六宫主（Ari's Lord）是否落上升宫（Lagna）
- 八宫主（Randhr's Lord）是否落上升宫（Lagna）
- 太阳（Surya）是否落上升宫（Lagna）
- 火星（Mangal）是否落上升宫（Lagna）
- 水星（Budh）是否落上升宫（Lagna）
- 木星（Guru）是否落上升宫（Lagna）
- 金星（Shukra）是否落上升宫（Lagna）
- 土星（Shani）是否落上升宫（Lagna）
- 罗睺（Rahu）是否落上升宫（Lagna）
- 计都（Ketu）是否落上升宫（Lagna）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v9-lagna-lords-graha-diseases.step-001

- 动作：核对上升宫（Lagn）是否被六宫主与八宫主占据，并核对太阳（Surya）是否同落其中。
- 适用范围：仅限本命盘上升宫聚六宫主与八宫主的情形；原文未给时间限定，各行星的结果只在本条列举范围内。
- 原文最小意思：上升宫被六宫主与八宫主占据、太阳同落其中时，会有发热与肿瘤。
- 本步骤产出事实：["上升宫聚六八宫主与太阳的判定"]
- 所需事实：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "太阳（Surya）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "太阳（Surya）是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把太阳的这项结果扩大到上升宫没有六宫主与八宫主的情形。", "不得据此推断发病年龄或病程。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：六宫主（Ari's Lord）是否落上升宫（Lagna）、八宫主（Randhr's Lord）是否落上升宫（Lagna）、太阳（Surya）是否落上升宫（Lagna）。
- 缺失即停字段：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "太阳（Surya）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“When Lagn is occupied by the Lords of Ari and Randhr Bhava along with Surya, the native will be afflicted by fever and tumours.”

### ch17-v9-lagna-lords-graha-diseases.step-002

- 动作：核对上升宫（Lagn）是否被六宫主与八宫主占据，并核对火星（Mangal）是否同落其中。
- 适用范围：仅限本命盘上升宫聚六宫主与八宫主的情形；原文未给时间限定，各行星的结果只在本条列举范围内。
- 原文最小意思：上升宫被六宫主与八宫主占据、火星取代太阳同落其中时，会有血管肿胀变硬、外伤与兵器所伤。
- 本步骤产出事实：["上升宫聚六八宫主与火星的判定"]
- 所需事实：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "火星（Mangal）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "火星（Mangal）是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把火星的这项结果扩大到上升宫没有六宫主与八宫主的情形。", "不得据此推断发病年龄或病程。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：六宫主（Ari's Lord）是否落上升宫（Lagna）、八宫主（Randhr's Lord）是否落上升宫（Lagna）、火星（Mangal）是否落上升宫（Lagna）。
- 缺失即停字段：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "火星（Mangal）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Lagn is occupied by the Lords of Ari and Randhr Bhava”
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Mangal, replacing Surya, will cause swelling and hardening of the blood vessels and wounds and hits by weapons.”

### ch17-v9-lagna-lords-graha-diseases.step-003

- 动作：核对上升宫（Lagn）是否被六宫主与八宫主占据，并核对水星（Budh）是否同落其中。
- 适用范围：仅限本命盘上升宫聚六宫主与八宫主的情形；原文未给时间限定，各行星的结果只在本条列举范围内。
- 原文最小意思：上升宫被六宫主与八宫主占据、水星以同样方式同落其中时，会有胆汁性疾病。
- 本步骤产出事实：["上升宫聚六八宫主与水星的判定"]
- 所需事实：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "水星（Budh）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "水星（Budh）是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把水星的这项结果扩大到上升宫没有六宫主与八宫主的情形。", "不得据此推断发病年龄或病程。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：六宫主（Ari's Lord）是否落上升宫（Lagna）、八宫主（Randhr's Lord）是否落上升宫（Lagna）、水星（Budh）是否落上升宫（Lagna）。
- 缺失即停字段：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "水星（Budh）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Lagn is occupied by the Lords of Ari and Randhr Bhava”
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Budh so featuring will bring in billious diseases”

### ch17-v9-lagna-lords-graha-diseases.step-004

- 动作：核对上升宫（Lagn）是否被六宫主与八宫主占据，并核对木星（Guru）是否同落其中。
- 适用范围：仅限本命盘上升宫聚六宫主与八宫主的情形；原文未给时间限定，各行星的结果只在本条列举范围内。
- 原文最小意思：上升宫被六宫主与八宫主占据、木星以同样方式同落其中时，能消除任何疾病。
- 本步骤产出事实：["上升宫聚六八宫主与木星的判定"]
- 所需事实：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "木星（Guru）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "木星（Guru）是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把木星的这项结果扩大到上升宫没有六宫主与八宫主的情形。", "不得据此推断发病年龄或病程。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：六宫主（Ari's Lord）是否落上升宫（Lagna）、八宫主（Randhr's Lord）是否落上升宫（Lagna）、木星（Guru）是否落上升宫（Lagna）。
- 缺失即停字段：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "木星（Guru）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Lagn is occupied by the Lords of Ari and Randhr Bhava”
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Guru in similar case will destroy any disease”

### ch17-v9-lagna-lords-graha-diseases.step-005

- 动作：核对上升宫（Lagn）是否被六宫主与八宫主占据，并核对金星（Shukra）是否同落其中。
- 适用范围：仅限本命盘上升宫聚六宫主与八宫主的情形；原文未给时间限定，各行星的结果只在本条列举范围内。
- 原文最小意思：上升宫被六宫主与八宫主占据、金星以同样方式同落其中时，会有因女性而来的疾病。
- 本步骤产出事实：["上升宫聚六八宫主与金星的判定"]
- 所需事实：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "金星（Shukra）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "金星（Shukra）是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把金星的这项结果扩大到上升宫没有六宫主与八宫主的情形。", "不得据此推断发病年龄或病程。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：六宫主（Ari's Lord）是否落上升宫（Lagna）、八宫主（Randhr's Lord）是否落上升宫（Lagna）、金星（Shukra）是否落上升宫（Lagna）。
- 缺失即停字段：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "金星（Shukra）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Lagn is occupied by the Lords of Ari and Randhr Bhava”
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Similarly Shukra will cause diseases through females”

### ch17-v9-lagna-lords-graha-diseases.step-006

- 动作：核对上升宫（Lagn）是否被六宫主与八宫主占据，并核对土星（Shani）是否同落其中。
- 适用范围：仅限本命盘上升宫聚六宫主与八宫主的情形；原文未给时间限定，各行星的结果只在本条列举范围内。
- 原文最小意思：上升宫被六宫主与八宫主占据、土星以同样方式同落其中时，会有风性疾病。
- 本步骤产出事实：["上升宫聚六八宫主与土星的判定"]
- 所需事实：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "土星（Shani）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "土星（Shani）是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把土星的这项结果扩大到上升宫没有六宫主与八宫主的情形。", "不得据此推断发病年龄或病程。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：六宫主（Ari's Lord）是否落上升宫（Lagna）、八宫主（Randhr's Lord）是否落上升宫（Lagna）、土星（Shani）是否落上升宫（Lagna）。
- 缺失即停字段：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "土星（Shani）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Lagn is occupied by the Lords of Ari and Randhr Bhava”
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Shani windy diseases”

### ch17-v9-lagna-lords-graha-diseases.step-007

- 动作：核对上升宫（Lagn）是否被六宫主与八宫主占据，并核对罗睺（Rahu）是否同落其中。
- 适用范围：仅限本命盘上升宫聚六宫主与八宫主的情形；原文未给时间限定，各行星的结果只在本条列举范围内。
- 原文最小意思：上升宫被六宫主与八宫主占据、罗睺以同样方式同落其中时，会有来自低种姓者的危险。
- 本步骤产出事实：["上升宫聚六八宫主与罗睺的判定"]
- 所需事实：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "罗睺（Rahu）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "罗睺（Rahu）是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把罗睺的这项结果扩大到上升宫没有六宫主与八宫主的情形。", "不得据此推断发病年龄或病程。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：六宫主（Ari's Lord）是否落上升宫（Lagna）、八宫主（Randhr's Lord）是否落上升宫（Lagna）、罗睺（Rahu）是否落上升宫（Lagna）。
- 缺失即停字段：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "罗睺（Rahu）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Lagn is occupied by the Lords of Ari and Randhr Bhava”
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Rahu danger through low-caste-men”

### ch17-v9-lagna-lords-graha-diseases.step-008

- 动作：核对上升宫（Lagn）是否被六宫主与八宫主占据，并核对计都（Ketu）是否同落其中。
- 适用范围：仅限本命盘上升宫聚六宫主与八宫主的情形；原文未给时间限定，各行星的结果只在本条列举范围内。
- 原文最小意思：上升宫被六宫主与八宫主占据、计都以同样方式同落其中时，会有脐部疾病。
- 本步骤产出事实：["上升宫聚六八宫主与计都的判定"]
- 所需事实：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "计都（Ketu）是否落上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "计都（Ketu）是否落上升宫（Lagna）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把计都的这项结果扩大到上升宫没有六宫主与八宫主的情形。", "不得据此推断发病年龄或病程。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：六宫主（Ari's Lord）是否落上升宫（Lagna）、八宫主（Randhr's Lord）是否落上升宫（Lagna）、计都（Ketu）是否落上升宫（Lagna）。
- 缺失即停字段：["六宫主（Ari's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落上升宫（Lagna）", "计都（Ketu）是否落上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Lagn is occupied by the Lords of Ari and Randhr Bhava”
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Ketu navel diseases”


## 四路查书计划

### 支持路

- When Lagn is occupied by the Lords of Ari and Randhr Bhava along with Surya fever and tumours
- 上升宫 六宫主 八宫主 同宫 发热 肿瘤 风疾

### 反例或取消路

- Guru in similar case will destroy any disease
- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle

### 适用边界路

- Effects of Ari’s Lord in Various Bhavas 六宫主落各宫的效果
- Evils, causing premature end, exist up to the 24th year of one’s age

### 判断方法路

- Indications of Ari Bhava doubts about death enemies ulcers
- 判断疾病种类应看上升宫里有哪些行星

## 上游问题

- 无

## 停止条件

- 缺少六宫主落上升宫事实时停止。
- 缺少八宫主落上升宫事实时停止。
- 缺少各行星是否落上升宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
