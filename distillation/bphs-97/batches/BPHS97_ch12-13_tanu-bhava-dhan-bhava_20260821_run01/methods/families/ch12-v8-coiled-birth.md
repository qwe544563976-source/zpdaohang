---
method: ch12-v8-coiled-birth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 出生带缠绕：上升为白羊金牛狮子之一且宫内有土星或火星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我出生时是不是有脐带绕身的情况
- 上升白羊金牛狮子加土星火星代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘一宫（Lagn）内有哪些行星

## 按情况检查的事实

- 本盘一宫（Lagn）所在星座是否为白羊座（Mesh）
- 本盘一宫（Lagn）所在星座是否为金牛座（Vrishabh）
- 本盘一宫（Lagn）所在星座是否为狮子座（Simh）
- 土星（Shani）是否落一宫（Tanu）
- 火星（Mangal）是否落一宫（Tanu）
- 本盘一宫（Lagn）落在哪个星座
- 本盘一宫（Lagn）在九分盘（Navamsa D9）中落在哪个星座

## 依赖方法

- 无

## 执行步骤

### ch12-v8-coiled-birth.step-001

- 动作：核对上升星座是否为白羊、金牛、狮子之一，并核对该宫内是否有土星或火星。
- 适用范围：仅限本命盘一宫（Tanu Bhava）出生情形主题；原文只列了这三个上升星座与这两颗行星。
- 原文最小意思：上升落白羊座（Mesh）、金牛座（Vrishabh）或狮子座（Simh）之一，且该上升宫内有土星（Shani）或火星（Mangal）时，孩子出生时有缠绕物绕在某一肢体上。
- 本步骤产出事实：["上升星座与土火占据的缠绕出生判定"]
- 所需事实：["本盘一宫（Lagn）内有哪些行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘一宫（Lagn）内有哪些行星"}, {"operator": "OR", "operands": [{"fact_key": "本盘一宫（Lagn）所在星座是否为白羊座（Mesh）"}, {"fact_key": "本盘一宫（Lagn）所在星座是否为金牛座（Vrishabh）"}, {"fact_key": "本盘一宫（Lagn）所在星座是否为狮子座（Simh）"}]}, {"operator": "OR", "operands": [{"fact_key": "土星（Shani）是否落一宫（Tanu）"}, {"fact_key": "火星（Mangal）是否落一宫（Tanu）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘一宫（Lagn）内有哪些行星"}, "required_fact_keys": ["本盘一宫（Lagn）所在星座是否为白羊座（Mesh）"], "branch_condition_logic": {"fact_key": "本盘一宫（Lagn）所在星座是否为白羊座（Mesh）"}, "selection_group": "ch12-v8-coiled-birth.step-001:lagna-rasi", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘一宫（Lagn）所在星座是否为白羊座（Mesh）。"}, {"when": {"fact_key": "本盘一宫（Lagn）内有哪些行星"}, "required_fact_keys": ["本盘一宫（Lagn）所在星座是否为金牛座（Vrishabh）"], "branch_condition_logic": {"fact_key": "本盘一宫（Lagn）所在星座是否为金牛座（Vrishabh）"}, "selection_group": "ch12-v8-coiled-birth.step-001:lagna-rasi", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘一宫（Lagn）所在星座是否为金牛座（Vrishabh）。"}, {"when": {"fact_key": "本盘一宫（Lagn）内有哪些行星"}, "required_fact_keys": ["本盘一宫（Lagn）所在星座是否为狮子座（Simh）"], "branch_condition_logic": {"fact_key": "本盘一宫（Lagn）所在星座是否为狮子座（Simh）"}, "selection_group": "ch12-v8-coiled-birth.step-001:lagna-rasi", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘一宫（Lagn）所在星座是否为狮子座（Simh）。"}, {"when": {"fact_key": "本盘一宫（Lagn）内有哪些行星"}, "required_fact_keys": ["土星（Shani）是否落一宫（Tanu）"], "branch_condition_logic": {"fact_key": "土星（Shani）是否落一宫（Tanu）"}, "selection_group": "ch12-v8-coiled-birth.step-001:occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：土星（Shani）是否落一宫（Tanu）。"}, {"when": {"fact_key": "本盘一宫（Lagn）内有哪些行星"}, "required_fact_keys": ["火星（Mangal）是否落一宫（Tanu）"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否落一宫（Tanu）"}, "selection_group": "ch12-v8-coiled-birth.step-001:occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否落一宫（Tanu）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把缠绕物指名为脐带，原文只写 a coil。", "不得把这三个上升星座之外的星座也算进来。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘一宫（Lagn）内有哪些行星。
- 缺失即停字段：["本盘一宫（Lagn）内有哪些行星"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v8`｜PDF [27]｜“If there be a birth in one of Mesh, Vrishabh and Simh Lagnas, containing either Shani, or Mangal, the birth of the child is with a coil around a limb.”

### ch12-v8-coiled-birth.step-002

- 动作：在已判出缠绕出生的盘上，按上升所落的星座或上升的九分盘定出对应的肢体。
- 适用范围：仅限本命盘缠绕出生的部位判定；原文给了星座与九分盘两个参照，没有说何时用哪一个，也没有给出肢体与宫位的对照表。
- 原文最小意思：缠绕所在的对应肢体，按上升的星座（Rāśi）或上升的九分盘（Navāńś）确定。
- 本步骤产出事实：["缠绕所在肢体的参照判定"]
- 所需事实：["上升星座与土火占据的缠绕出生判定"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升星座与土火占据的缠绕出生判定"}, {"operator": "OR", "operands": [{"fact_key": "本盘一宫（Lagn）落在哪个星座"}, {"fact_key": "本盘一宫（Lagn）在九分盘（Navamsa D9）中落在哪个星座"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "上升星座与土火占据的缠绕出生判定"}, "required_fact_keys": ["本盘一宫（Lagn）落在哪个星座"], "branch_condition_logic": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "selection_group": "ch12-v8-coiled-birth.step-002:limb-reference", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘一宫（Lagn）落在哪个星座。"}, {"when": {"fact_key": "上升星座与土火占据的缠绕出生判定"}, "required_fact_keys": ["本盘一宫（Lagn）在九分盘（Navamsa D9）中落在哪个星座"], "branch_condition_logic": {"fact_key": "本盘一宫（Lagn）在九分盘（Navamsa D9）中落在哪个星座"}, "selection_group": "ch12-v8-coiled-birth.step-002:limb-reference", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘一宫（Lagn）在九分盘（Navamsa D9）中落在哪个星座。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自行规定星座或九分盘与哪个肢体对应，本偈没有给对照表，未确定即停判。", "不得在两个参照之间自行指定优先次序，原文没有说。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升星座与土火占据的缠绕出生判定。
- 缺失即停字段：["上升星座与土火占据的缠绕出生判定"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v8`｜PDF [27]｜“The corresponding limb will be in accordance with the Rāśi, or Navāńś, rising.”


## 四路查书计划

### 支持路

- If there be a birth in one of Mesh, Vrishabh and Simh Lagnas, containing either Shani, or Mangal, the birth of the child is with a coil around a limb
- 上升白羊金牛狮子 土星火星在一宫 出生带缠绕

### 反例或取消路

- 无

### 适用边界路

- It is a quadruped Rashiand strong during night
- The Navāńś calculation are for a Movable Rashifrom there itself, for a Fixed Rashifrom the 9th thereof and for a Dual Rashifrom the 5th thereof
- The Sixteen Divisions of a Rāśi

### 判断方法路

- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- One third of a Rashiis called Dreshkan. These are totally 36, counted from Mesh, repeating thrice at the rate of 12 per round
- 判断出生时的缠绕要看上升星座和其中的土星火星

## 上游问题

- 无

## 停止条件

- 缺少一宫行星名单事实时停止。
- 三个上升星座分支事实全缺时停止。
- 土星与火星两个占据分支事实全缺时停止。
- 肢体与星座、九分盘的对照关系原文未给，部位判定未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
