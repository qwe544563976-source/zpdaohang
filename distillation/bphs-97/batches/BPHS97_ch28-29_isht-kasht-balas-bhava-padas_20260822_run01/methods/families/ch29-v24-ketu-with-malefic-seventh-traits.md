---
method: ch29-v24-ketu-with-malefic-seventh-traits
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 计都在上升 Pad 起第 7 宫且与凶星关联：冒险、白发、男根粗大

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这个人是不是爱冒险
- 我为什么这么早就白头

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 计都（Ketu）是否落上升 Pad（Lagn Pad）起第 7 宫

## 按情况检查的事实

- 计都（Ketu）是否被其他凶星相照
- 计都（Ketu）是否与其他凶星同宫

## 依赖方法

- 无

## 执行步骤

### ch29-v24-ketu-with-malefic-seventh-traits.step-001

- 动作：先看计都（Ketu）是否落上升 Pad（Lagn Pad）起第 7 宫，再看它是否受另一凶星相照或与之同宫。
- 适用范围：原文以男性身体特征（a big male organ）立说，女命命中时须提示；本条以上升 Pad（Lagn Pad）为起算点。
- 原文最小意思：计都（Ketu）落上升 Pad（Lagn Pad）起第 7 宫，并受另一凶星相照、或与另一凶星同宫时，命主富于冒险，（过早）生白发，男根粗大。
- 本步骤产出事实：["计都在上升 Pad 起第 7 宫的体貌与性情判定"]
- 所需事实：["计都（Ketu）是否落上升 Pad（Lagn Pad）起第 7 宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "计都（Ketu）是否落上升 Pad（Lagn Pad）起第 7 宫"}, {"operator": "OR", "operands": [{"fact_key": "计都（Ketu）是否被其他凶星相照"}, {"fact_key": "计都（Ketu）是否与其他凶星同宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "计都（Ketu）是否落上升 Pad（Lagn Pad）起第 7 宫"}, "required_fact_keys": ["计都（Ketu）是否被其他凶星相照"], "branch_condition_logic": {"fact_key": "计都（Ketu）是否被其他凶星相照"}, "selection_group": "ch29-v24-ketu-with-malefic-seventh-traits.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：计都（Ketu）是否被其他凶星相照。"}, {"when": {"fact_key": "计都（Ketu）是否落上升 Pad（Lagn Pad）起第 7 宫"}, "required_fact_keys": ["计都（Ketu）是否与其他凶星同宫"], "branch_condition_logic": {"fact_key": "计都（Ketu）是否与其他凶星同宫"}, "selection_group": "ch29-v24-ketu-with-malefic-seventh-traits.step-001:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：计都（Ketu）是否与其他凶星同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断白发的具体年龄。", "不得把身体特征断语套到女命而不加说明。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：计都（Ketu）是否落上升 Pad（Lagn Pad）起第 7 宫。
- 缺失即停字段：["计都（Ketu）是否落上升 Pad（Lagn Pad）起第 7 宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v24`｜PDF [63]｜“Should there be Ketu in the 7<sup>th</sup> from Lagn Pad, receiving a Drishti from, or being yuti with another malefic, the native will be adventurous, will have (prematurely) grey hair and a big male organ.”


## 四路查书计划

### 支持路

- Should there be Ketu in the 7<sup>th</sup> from Lagn Pad, receiving a Drishti from, or being yuti with another malefic, the native will be adventurous, will have (prematurely) grey hair and a big male organ.
- 计都在上升 Pad 起第 7 宫与凶星关联 冒险白发

### 反例或取消路

- 无

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- O Brahmin, these Yogas, as narrated by me with reference to the 7<sup>th</sup> from Lagn Pad, should also be considered from the 2<sup>nd</sup> of Lagn Pad.
- 同一批断语也从上升 Pad 起第 2 宫考察

### 判断方法路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics.
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 哪些行星算凶星

## 上游问题

- 无

## 停止条件

- 缺少计都相对上升 Pad 起第 7 宫的落宫事实时停止。
- 缺少计都与其他凶星的相照或同宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
