---
method: ch39-v26-27-arudh-pad-exalted-graha
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Arudh Pad 有入旺行星（尤其入旺月亮）或木星金星，且无凶星 Argala：成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Arudh Pad 上有什么星才算好
- 我有没有靠声望上位的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Arudh Pad 落在哪个星座
- Arudh Pad 是否受到凶星的 Argala

## 按情况检查的事实

- Arudh Pad 是否被入旺的行星占据
- Arudh Pad 是否被木星（Guru）占据
- Arudh Pad 是否被金星（Shukra）占据

## 依赖方法

- 无

## 执行步骤

### ch39-v26-27-arudh-pad-exalted-graha.step-001

- 动作：先定出 Arudh Pad，核对它是被入旺的行星占据，还是被木星（Guru）或金星（Shukra）占据，再核对是否没有凶星对它形成 Argala。
- 适用范围：仅限本命盘；原文对木星与金星特别注明不论是否入旺；原文没有时间限定。
- 原文最小意思：Arudh Pad 被入旺的行星占据（尤其是入旺的月亮 Chandra），或被木星（Guru）和／或金星（Shukra）占据（不论是否入旺），同时没有凶星对它形成 Argala 时，命主会成为国王。
- 本步骤产出事实：["Arudh Pad 得地无凶 Argala 的贵格判定"]
- 所需事实：["本盘的 Arudh Pad 落在哪个星座", "Arudh Pad 是否受到凶星的 Argala"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘的 Arudh Pad 落在哪个星座"}, {"operator": "NOT", "operands": [{"fact_key": "Arudh Pad 是否受到凶星的 Argala"}]}]}, {"operator": "OR", "operands": [{"fact_key": "Arudh Pad 是否被入旺的行星占据"}, {"fact_key": "Arudh Pad 是否被木星（Guru）占据"}, {"fact_key": "Arudh Pad 是否被金星（Shukra）占据"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Arudh Pad 落在哪个星座"}, {"operator": "NOT", "operands": [{"fact_key": "Arudh Pad 是否受到凶星的 Argala"}]}]}, "required_fact_keys": ["Arudh Pad 是否被入旺的行星占据"], "branch_condition_logic": {"fact_key": "Arudh Pad 是否被入旺的行星占据"}, "selection_group": "ch39-v26-27-arudh-pad-exalted-graha.step-001:arudh-pad-occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：Arudh Pad 是否被入旺的行星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Arudh Pad 落在哪个星座"}, {"operator": "NOT", "operands": [{"fact_key": "Arudh Pad 是否受到凶星的 Argala"}]}]}, "required_fact_keys": ["Arudh Pad 是否被木星（Guru）占据"], "branch_condition_logic": {"fact_key": "Arudh Pad 是否被木星（Guru）占据"}, "selection_group": "ch39-v26-27-arudh-pad-exalted-graha.step-001:arudh-pad-occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：Arudh Pad 是否被木星（Guru）占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Arudh Pad 落在哪个星座"}, {"operator": "NOT", "operands": [{"fact_key": "Arudh Pad 是否受到凶星的 Argala"}]}]}, "required_fact_keys": ["Arudh Pad 是否被金星（Shukra）占据"], "branch_condition_logic": {"fact_key": "Arudh Pad 是否被金星（Shukra）占据"}, "selection_group": "ch39-v26-27-arudh-pad-exalted-graha.step-001:arudh-pad-occupant", "stop_condition": "选中该分支后，缺少以下事实即停止：Arudh Pad 是否被金星（Shukra）占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文的 particularly Chandra in exaltation 是对入旺行星一路的强调，不得把它读成必须是月亮。", "不得据此推断登位时间或具体权位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Arudh Pad 落在哪个星座、Arudh Pad 是否受到凶星的 Argala。
- 缺失即停字段：["本盘的 Arudh Pad 落在哪个星座", "Arudh Pad 是否受到凶星的 Argala"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v26-27`｜PDF [83]｜“If Arudh Pad is occupied by an exalted Grah, particularly Chandra in exaltation, or by Guru and/or Shukra (with, or without exaltation), while there is no Argala by a malefic, the native will become a king.”


## 四路查书计划

### 支持路

- If Arudh Pad is occupied by an exalted Grah, particularly Chandra in exaltation, or by Guru and/or Shukra (with, or without exaltation), while there is no Argala by a malefic, the native will become a king
- Arudh Pad 入旺行星 木星金星 无凶星 Argala 国王

### 反例或取消路

- If malefics be in Karakāńś, Arudh Lagn and the 2<sup>nd</sup> and 8<sup>th</sup> from these places, there will be Kemadrum Yog
- If there is Argala for the said 11<sup>th</sup> , there will be more gains

### 适用边界路

- Grahas in the 4<sup>th</sup> , 2<sup>nd</sup> and the 11<sup>th</sup> cause Argalas, while obstructors of the Argala will be those in the 10<sup>th</sup> , 12<sup>th</sup> and 3<sup>rd</sup> from a Bhava, or a Grah
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Should there be Argala for the Arudh Pad, for the natal Lagn and for the 7<sup>th</sup> from both, the native will be famous and fortunate
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- 缺少 Arudh Pad 定位事实时停止。
- 缺少凶星 Argala 的事实时停止。
- 三种占据情形的事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
