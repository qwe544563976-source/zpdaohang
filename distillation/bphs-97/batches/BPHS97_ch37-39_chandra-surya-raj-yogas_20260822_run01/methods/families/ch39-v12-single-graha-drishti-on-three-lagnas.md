---
method: ch39-v12-single-graha-drishti-on-three-lagnas
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 哪怕一颗行星相照本命上升、Hora Lagna 或 Ghatik Lagna：成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 只有一颗行星照上升也算贵格吗
- Hora Lagna 和 Ghatik Lagna 有什么用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘本命上升（natal Lagna）落在哪个星座
- 本盘的 Hora Lagna 落在哪个星座
- 本盘的 Ghatik Lagna 落在哪个星座

## 按情况检查的事实

- 本命上升宫（natal Lagna）是否被行星相照
- Hora Lagna 是否被行星相照
- Ghatik Lagna 是否被行星相照

## 依赖方法

- 无

## 执行步骤

### ch39-v12-single-graha-drishti-on-three-lagnas.step-001

- 动作：先定出本命上升、Hora Lagna 与 Ghatik Lagna 三个上升位，再核对是否有行星相照其中之一。
- 适用范围：仅限本命盘；原文强调即使只有一颗行星相照也成立，没有时间限定。
- 原文最小意思：即使只有一颗行星（a single Grah）相照本命上升宫（natal Lagna）、Hora Lagna 或 Ghatik Lagna，命主也会成为国王。
- 本步骤产出事实：["三上升位受照的贵格判定"]
- 所需事实：["本盘本命上升（natal Lagna）落在哪个星座", "本盘的 Hora Lagna 落在哪个星座", "本盘的 Ghatik Lagna 落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘本命上升（natal Lagna）落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, {"operator": "OR", "operands": [{"fact_key": "本命上升宫（natal Lagna）是否被行星相照"}, {"fact_key": "Hora Lagna 是否被行星相照"}, {"fact_key": "Ghatik Lagna 是否被行星相照"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘本命上升（natal Lagna）落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, "required_fact_keys": ["本命上升宫（natal Lagna）是否被行星相照"], "branch_condition_logic": {"fact_key": "本命上升宫（natal Lagna）是否被行星相照"}, "selection_group": "ch39-v12-single-graha-drishti-on-three-lagnas.step-001:which-lagna", "stop_condition": "选中该分支后，缺少以下事实即停止：本命上升宫（natal Lagna）是否被行星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘本命上升（natal Lagna）落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, "required_fact_keys": ["Hora Lagna 是否被行星相照"], "branch_condition_logic": {"fact_key": "Hora Lagna 是否被行星相照"}, "selection_group": "ch39-v12-single-graha-drishti-on-three-lagnas.step-001:which-lagna", "stop_condition": "选中该分支后，缺少以下事实即停止：Hora Lagna 是否被行星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘本命上升（natal Lagna）落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, "required_fact_keys": ["Ghatik Lagna 是否被行星相照"], "branch_condition_logic": {"fact_key": "Ghatik Lagna 是否被行星相照"}, "selection_group": "ch39-v12-single-graha-drishti-on-three-lagnas.step-001:which-lagna", "stop_condition": "选中该分支后，缺少以下事实即停止：Ghatik Lagna 是否被行星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文没有限定相照的行星是吉是凶，不得自行加上吉星限定。", "不得据此推断登位时间或具体权位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘本命上升（natal Lagna）落在哪个星座、本盘的 Hora Lagna 落在哪个星座、本盘的 Ghatik Lagna 落在哪个星座。
- 缺失即停字段：["本盘本命上升（natal Lagna）落在哪个星座", "本盘的 Hora Lagna 落在哪个星座", "本盘的 Ghatik Lagna 落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v12`｜PDF [82]｜“Even, if a single Grah gives a Drishti to the natal Lagna, or Hora Lagna, or Ghatik Lagna, the native will become a king.”


## 四路查书计划

### 支持路

- Even, if a single Grah gives a Drishti to the natal Lagna, or Hora Lagna, or Ghatik Lagna, the native will become a king
- 一颗行星相照三个上升位 成为国王

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- I explain below again some special Lagnas, viz. Bhava Lagna, Hora Lagn and Ghati Lagn
- This Lagn changes along with every Ghati (24 minutes) from the sunrise

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 缺少 Hora Lagna 或 Ghatik Lagna 的定位事实时停止。
- 三个上升位的受照事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
