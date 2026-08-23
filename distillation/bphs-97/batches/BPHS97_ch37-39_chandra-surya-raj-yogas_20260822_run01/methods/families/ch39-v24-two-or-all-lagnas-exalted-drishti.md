---
method: ch39-v24-two-or-all-lagnas-exalted-drishti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三个上升位中有两个或三个被入旺行星相照：贵格成立

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 入旺的行星照上升位有多大用
- 三个上升位要照到几个才算数

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中有几个被入旺的行星相照

## 按情况检查的事实

- Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中是否恰有两个被入旺的行星相照
- Bhava Lagna、Hora Lagna、Ghatik Lagna 三者是否都被入旺的行星相照

## 依赖方法

- 无

## 执行步骤

### ch39-v24-two-or-all-lagnas-exalted-drishti.step-001

- 动作：数一数 Bhava Lagn、Hora Lagn、Ghatik Lagn 三者中被入旺行星相照的有几个，再核对是两个还是三个全中。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文没有时间限定。
- 原文最小意思：Bhava Lagn、Hora Lagn 与 Ghatik Lagn 之中有两个，或三个全部被入旺的行星相照时，Raj Yog 成立。
- 本步骤产出事实：["三上升位受入旺行星相照的贵格判定"]
- 所需事实：["Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中有几个被入旺的行星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中有几个被入旺的行星相照"}, {"operator": "OR", "operands": [{"fact_key": "Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中是否恰有两个被入旺的行星相照"}, {"fact_key": "Bhava Lagna、Hora Lagna、Ghatik Lagna 三者是否都被入旺的行星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中有几个被入旺的行星相照"}, "required_fact_keys": ["Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中是否恰有两个被入旺的行星相照"], "branch_condition_logic": {"fact_key": "Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中是否恰有两个被入旺的行星相照"}, "selection_group": "ch39-v24-two-or-all-lagnas-exalted-drishti.step-001:how-many-lagnas", "stop_condition": "选中该分支后，缺少以下事实即停止：Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中是否恰有两个被入旺的行星相照。"}, {"when": {"fact_key": "Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中有几个被入旺的行星相照"}, "required_fact_keys": ["Bhava Lagna、Hora Lagna、Ghatik Lagna 三者是否都被入旺的行星相照"], "branch_condition_logic": {"fact_key": "Bhava Lagna、Hora Lagna、Ghatik Lagna 三者是否都被入旺的行星相照"}, "selection_group": "ch39-v24-two-or-all-lagnas-exalted-drishti.step-001:how-many-lagnas", "stop_condition": "选中该分支后，缺少以下事实即停止：Bhava Lagna、Hora Lagna、Ghatik Lagna 三者是否都被入旺的行星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文要求相照者是入旺的行星，不得放宽成任意行星。", "只有一个上升位被照时不得据此下断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中有几个被入旺的行星相照。
- 缺失即停字段：["Bhava Lagna、Hora Lagna、Ghatik Lagna 三者中有几个被入旺的行星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v24`｜PDF [83]｜“If two, or all of Bhava, Hora, Ghatik Lagnas are receiving a Drishti from exalted Grahas, a Raj Yog is formed.”


## 四路查书计划

### 支持路

- If two, or all of Bhava, Hora, Ghatik Lagnas are receiving a Drishti from exalted Grahas, a Raj Yog is formed
- 两个或三个上升位受入旺行星相照 贵格

### 反例或取消路

- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless

### 适用边界路

- I explain below again some special Lagnas, viz. Bhava Lagna, Hora Lagn and Ghati Lagn
- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- From sunrise to the time of birth every 5 Ghatis (or 120 minutes) constitute one Bhava Lagn

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少三个上升位的定位事实时停止。
- 缺少受入旺行星相照的计数事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
