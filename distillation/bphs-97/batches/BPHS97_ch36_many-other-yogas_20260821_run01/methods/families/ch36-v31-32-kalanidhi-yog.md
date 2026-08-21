---
method: ch36-v31-32-kalanidhi-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Kalanidhi Yog：木星落二宫或五宫并受水星与金星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的健康和学问怎么样
- 我有没有受贵人尊重的命

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否被水星（Budh）相照
- 木星（Guru）是否被金星（Shukr）相照

## 按情况检查的事实

- 木星（Guru）是否落二宫（Dhan）
- 木星（Guru）是否落五宫（Putr）

## 依赖方法

- 无

## 执行步骤

### ch36-v31-32-kalanidhi-yog.step-001

- 动作：先核对木星（Guru）是否同时受到水星（Budh）与金星（Shukr）的相照，再核对木星落二宫（Dhan）还是五宫（Putr）。
- 适用范围：仅限本命盘 Kalanidhi Yog 的成立与效果；原文要求两颗行星的相照同时具备，落宫则是二选一。原文未给上升限定，也未给时间限定。
- 原文最小意思：木星（Guru）落二宫（Dhan）或五宫（Putr），并且受到水星（Budh）与金星（Shukr）的相照时，成立 Kalanidhi Yog，命主会有德、受诸王尊敬、没有疾病、快乐、富有、有学问。
- 本步骤产出事实：["Kalanidhi Yog 成立判定"]
- 所需事实：["木星（Guru）是否被水星（Budh）相照", "木星（Guru）是否被金星（Shukr）相照"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否被水星（Budh）相照"}, {"fact_key": "木星（Guru）是否被金星（Shukr）相照"}]}, {"operator": "OR", "operands": [{"fact_key": "木星（Guru）是否落二宫（Dhan）"}, {"fact_key": "木星（Guru）是否落五宫（Putr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否被水星（Budh）相照"}, {"fact_key": "木星（Guru）是否被金星（Shukr）相照"}]}, "required_fact_keys": ["木星（Guru）是否落二宫（Dhan）"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落二宫（Dhan）"}, "selection_group": "ch36-v31-32-kalanidhi-yog.step-001:guru-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落二宫（Dhan）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否被水星（Budh）相照"}, {"fact_key": "木星（Guru）是否被金星（Shukr）相照"}]}, "required_fact_keys": ["木星（Guru）是否落五宫（Putr）"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落五宫（Putr）"}, "selection_group": "ch36-v31-32-kalanidhi-yog.step-001:guru-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落五宫（Putr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文说 bereft of diseases，只能写成没有疾病，不得引申为长寿或某种具体病症的免疫。", "不得把水星与金星的相照改成二选一；原文用 and 并列。", "不得据此推断财富数额或受尊敬的具体场合。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否被水星（Budh）相照、木星（Guru）是否被金星（Shukr）相照。
- 缺失即停字段：["木星（Guru）是否被水星（Budh）相照", "木星（Guru）是否被金星（Shukr）相照"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v31-32`｜PDF [80]｜“If Guru is placed in Dhan, or Putr Bhava and receives a Drishti from Budh and Shukr, Kalanidhi Yog is caused. In effect the native will be virtuous, honoured by the kings, bereft of diseases, be happy, wealthy and learned.”


## 四路查书计划

### 支持路

- Kalanidhi Yog. If Guru is placed in Dhan, or Putr Bhava and receives a Drishti from Budh and Shukr
- Kalanidhi Yog 木星落二宫五宫 水星金星相照 无疾病

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Ari Bhava, while Ari’s Lord is in Lagna, yuti with, or receiving a Drishti from a Marak Lord
- The Bhava, which is not drishtied by its Lord, or, whose Lord is with a malefic Grah, or with one of the Lords of evil and such other Bhavas

### 适用边界路

- Drishtis of the Grahas. O Brahmin, I have earlier stated Drishtis, based on Rāśis. The other kind is between Grahas
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- Indications of Putr Bhava. The learned should deduce from Putr Bhava amulets, sacred spells, learning, knowledge, sons, royalty (or authority), fall of position etc

## 上游问题

- 无

## 停止条件

- 缺少木星被水星相照或被金星相照任一事实时停止。
- 命中木星落宫分支后，缺少该分支对应的二宫或五宫落宫事实时停止。
- 相照的取值口径未按本书 ch26 的 Drishti 章节取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
