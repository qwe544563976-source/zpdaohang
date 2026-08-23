---
method: ch39-v28-debilitated-dusthana-lord-drishti-lagna
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 六、八、十二宫主之一落陷并相照上升宫：贵格成立

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 坏宫主落陷照上升算好事吗
- 我盘里落陷的宫主有没有用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘六宫主（Ari's Lord）是哪颗行星
- 本盘八宫主（Randhr's Lord）是哪颗行星
- 本盘十二宫主（Vyaya's Lord）是哪颗行星

## 按情况检查的事实

- 六宫主（Ari's Lord）是否落陷
- 八宫主（Randhr's Lord）是否落陷
- 十二宫主（Vyaya's Lord）是否落陷
- 六宫主（Ari's Lord）是否相照上升宫（Lagna）
- 八宫主（Randhr's Lord）是否相照上升宫（Lagna）
- 十二宫主（Vyaya's Lord）是否相照上升宫（Lagna）

## 依赖方法

- 无

## 执行步骤

### ch39-v28-debilitated-dusthana-lord-drishti-lagna.step-001

- 动作：先认出六宫主、八宫主与十二宫主，再核对其中是否有一个落陷并相照上升宫。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文没有时间限定。
- 原文最小意思：六宫主（Ari's Lord）、八宫主（Randhr's Lord）与十二宫主（Vyaya's Lord）之中，有一个落陷并相照上升宫（Lagna）时，Raj Yog 成立。
- 本步骤产出事实：["落陷凶宫主相照上升的贵格判定"]
- 所需事实：["本盘六宫主（Ari's Lord）是哪颗行星", "本盘八宫主（Randhr's Lord）是哪颗行星", "本盘十二宫主（Vyaya's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落陷"}, {"fact_key": "六宫主（Ari's Lord）是否相照上升宫（Lagna）"}]}, {"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落陷"}, {"fact_key": "八宫主（Randhr's Lord）是否相照上升宫（Lagna）"}]}, {"operator": "AND", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否落陷"}, {"fact_key": "十二宫主（Vyaya's Lord）是否相照上升宫（Lagna）"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}]}, "required_fact_keys": ["六宫主（Ari's Lord）是否落陷", "六宫主（Ari's Lord）是否相照上升宫（Lagna）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落陷"}, {"fact_key": "六宫主（Ari's Lord）是否相照上升宫（Lagna）"}]}, "selection_group": "ch39-v28-debilitated-dusthana-lord-drishti-lagna.step-001:which-lord", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫主（Ari's Lord）是否落陷、六宫主（Ari's Lord）是否相照上升宫（Lagna）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}]}, "required_fact_keys": ["八宫主（Randhr's Lord）是否落陷", "八宫主（Randhr's Lord）是否相照上升宫（Lagna）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落陷"}, {"fact_key": "八宫主（Randhr's Lord）是否相照上升宫（Lagna）"}]}, "selection_group": "ch39-v28-debilitated-dusthana-lord-drishti-lagna.step-001:which-lord", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）是否落陷、八宫主（Randhr's Lord）是否相照上升宫（Lagna）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}]}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否落陷", "十二宫主（Vyaya's Lord）是否相照上升宫（Lagna）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否落陷"}, {"fact_key": "十二宫主（Vyaya's Lord）是否相照上升宫（Lagna）"}]}, "selection_group": "ch39-v28-debilitated-dusthana-lord-drishti-lagna.step-001:which-lord", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否落陷、十二宫主（Vyaya's Lord）是否相照上升宫（Lagna）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写六宫、八宫、十二宫三个宫主，不得把别的宫主也算进来。", "不得据此推断疾病、损失或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘六宫主（Ari's Lord）是哪颗行星、本盘八宫主（Randhr's Lord）是哪颗行星、本盘十二宫主（Vyaya's Lord）是哪颗行星。
- 缺失即停字段：["本盘六宫主（Ari's Lord）是哪颗行星", "本盘八宫主（Randhr's Lord）是哪颗行星", "本盘十二宫主（Vyaya's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v28`｜PDF [83]｜“Even, if one among Ari’s, Randhr’s and Vyaya’s Lords, being in debilitation, gives a Drishti to Lagna, there will be a Raj Yog.”


## 四路查书计划

### 支持路

- Even, if one among Ari’s, Randhr’s and Vyaya’s Lords, being in debilitation, gives a Drishti to Lagna, there will be a Raj Yog
- 六八十二宫主落陷相照上升 贵格

### 反例或取消路

- A Grah, associated with one of the Lords of Ari, Randhr and Vyaya Bhava, being bereft of a Drishti from the Lord of a Kon, will in its Dasha periods cause harm to the native’s financial aspects
- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 三个宫主的身份事实缺任一项时停止。
- 三条分支的落陷与相照事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
