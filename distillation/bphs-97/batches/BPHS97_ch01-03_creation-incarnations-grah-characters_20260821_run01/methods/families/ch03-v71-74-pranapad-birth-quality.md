---
method: ch03-v71-74-pranapad-birth-quality
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 出生吉凶：Pranapad 自上升起落第 2、5、9、4、10、11 宫为吉，余宫为凶

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这个出生本身吉不吉
- Pranapad 落哪几宫算吉

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘 Pranapad 落在从上升（Lagn）起的第几宫

## 按情况检查的事实

- 本盘 Pranapad 是否落在从上升（Lagn）起第2宫
- 本盘 Pranapad 是否落在从上升（Lagn）起第5宫
- 本盘 Pranapad 是否落在从上升（Lagn）起第9宫
- 本盘 Pranapad 是否落在从上升（Lagn）起第4宫
- 本盘 Pranapad 是否落在从上升（Lagn）起第10宫
- 本盘 Pranapad 是否落在从上升（Lagn）起第11宫

## 依赖方法

- ch03-v71-74-pranapad-calculation

## 执行步骤

### ch03-v71-74-pranapad-birth-quality.step-001

- 动作：数出 Pranapad 自本命上升起落在第几宫，落在第 2、5、9、4、10、11 宫时判为吉。
- 适用范围：第3章 Pranapad 推算条；本原子后附 Santhanam 译注，本方法只据偈文正文。
- 原文最小意思：若 Pranapad 落在从本命上升（Lagn）起的第 2、5、9、4、10、11 宫，出生为吉。
- 本步骤产出事实：["Pranapad 主出生为吉判定"]
- 所需事实：["本盘 Pranapad 落在从上升（Lagn）起的第几宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘 Pranapad 落在从上升（Lagn）起的第几宫"}, {"operator": "OR", "operands": [{"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第2宫"}, {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第5宫"}, {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第9宫"}, {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第4宫"}, {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第10宫"}, {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第11宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘 Pranapad 落在从上升（Lagn）起的第几宫"}, "required_fact_keys": ["本盘 Pranapad 是否落在从上升（Lagn）起第2宫"], "branch_condition_logic": {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第2宫"}, "selection_group": "ch03-v71-74-pranapad-birth-quality.step-001:auspicious-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘 Pranapad 是否落在从上升（Lagn）起第2宫。"}, {"when": {"fact_key": "本盘 Pranapad 落在从上升（Lagn）起的第几宫"}, "required_fact_keys": ["本盘 Pranapad 是否落在从上升（Lagn）起第5宫"], "branch_condition_logic": {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第5宫"}, "selection_group": "ch03-v71-74-pranapad-birth-quality.step-001:auspicious-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘 Pranapad 是否落在从上升（Lagn）起第5宫。"}, {"when": {"fact_key": "本盘 Pranapad 落在从上升（Lagn）起的第几宫"}, "required_fact_keys": ["本盘 Pranapad 是否落在从上升（Lagn）起第9宫"], "branch_condition_logic": {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第9宫"}, "selection_group": "ch03-v71-74-pranapad-birth-quality.step-001:auspicious-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘 Pranapad 是否落在从上升（Lagn）起第9宫。"}, {"when": {"fact_key": "本盘 Pranapad 落在从上升（Lagn）起的第几宫"}, "required_fact_keys": ["本盘 Pranapad 是否落在从上升（Lagn）起第4宫"], "branch_condition_logic": {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第4宫"}, "selection_group": "ch03-v71-74-pranapad-birth-quality.step-001:auspicious-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘 Pranapad 是否落在从上升（Lagn）起第4宫。"}, {"when": {"fact_key": "本盘 Pranapad 落在从上升（Lagn）起的第几宫"}, "required_fact_keys": ["本盘 Pranapad 是否落在从上升（Lagn）起第10宫"], "branch_condition_logic": {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第10宫"}, "selection_group": "ch03-v71-74-pranapad-birth-quality.step-001:auspicious-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘 Pranapad 是否落在从上升（Lagn）起第10宫。"}, {"when": {"fact_key": "本盘 Pranapad 落在从上升（Lagn）起的第几宫"}, "required_fact_keys": ["本盘 Pranapad 是否落在从上升（Lagn）起第11宫"], "branch_condition_logic": {"fact_key": "本盘 Pranapad 是否落在从上升（Lagn）起第11宫"}, "selection_group": "ch03-v71-74-pranapad-birth-quality.step-001:auspicious-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘 Pranapad 是否落在从上升（Lagn）起第11宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「出生为吉」扩成具体的富贵、寿命或事业断语。", "不得给这六宫之外的宫补上吉断——原文另有交代。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘 Pranapad 落在从上升（Lagn）起的第几宫。
- 缺失即停字段：["本盘 Pranapad 落在从上升（Lagn）起的第几宫"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v71-74`｜PDF [13, 14]｜“The birth will be auspicious, if Pranapad falls in the 2<sup>nd</sup> , 5<sup>th</sup> , 9<sup>th</sup> , 4<sup>th</sup> , 10<sup>th</sup> , or 11<sup>th</sup> from the natal Lagn.”

### ch03-v71-74-pranapad-birth-quality.step-002

- 动作：Pranapad 落在上述六宫之外的宫时，判为出生不吉。
- 适用范围：第3章 Pranapad 推算条；「其余各宫」承本方法第一步列出的六宫。
- 原文最小意思：落在其余各宫（other Bhavas）时，Pranapad 主出生不吉。
- 本步骤产出事实：["Pranapad 主出生不吉判定"]
- 所需事实：["Pranapad 主出生为吉判定"]
- 条件关系：{"operator": "NOT", "operands": [{"fact_key": "Pranapad 主出生为吉判定"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「出生不吉」扩成夭寿、贫病等具体断语——原文只说不吉。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Pranapad 主出生为吉判定。
- 缺失即停字段：["Pranapad 主出生为吉判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v71-74`｜PDF [13, 14]｜“In other Bhavas Pranapad indicates an inauspicious birth.”


## 四路查书计划

### 支持路

- The birth will be auspicious, if Pranapad falls in the 2<sup>nd</sup> , 5<sup>th</sup> , 9<sup>th</sup> , 4<sup>th</sup> , 10<sup>th</sup> , or 11<sup>th</sup> from the natal Lagn. In other Bhavas Pranapad indicates an inauspicious birth
- Pranapad 落宫 出生吉凶

### 反例或取消路

- If Pranapad is in Dhan Bhava, the native will be endowed with abundant grains, abundant wealth, abundant attendants, abundant children and be fortunate
- 别处按逐宫给 Pranapad 的具体效应

### 适用边界路

- Effects of Pranapad’s Position with reference to Lagn and in Various Bhavas (up to Sloka 85)
- Pranapad 逐宫效应另有专章

### 判断方法路

- Convert the given time into Vighatis and divide the same by 15
- 先算出 Pranapad 才能定落宫

## 上游问题

- 无

## 停止条件

- 缺少 Pranapad 自上升起的落宫时停止。
- Pranapad 没有算出来时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
