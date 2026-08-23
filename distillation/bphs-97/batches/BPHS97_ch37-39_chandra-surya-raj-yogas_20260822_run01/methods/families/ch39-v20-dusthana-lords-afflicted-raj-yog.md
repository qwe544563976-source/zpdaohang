---
method: ch39-v20-dusthana-lords-afflicted-raj-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 六、八、十二宫主落陷、居敌座或燃烧，上升主居本星座或入旺并相照上升

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 凶宫主变弱反而好吗
- 我盘里几个坏宫主都很弱说明什么

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
- 本盘上升主（Lagn's Lord）是哪颗行星
- 上升主（Lagn's Lord）是否相照上升宫（Lagna）

## 按情况检查的事实

- 六宫主（Ari's Lord）是否落陷
- 六宫主（Ari's Lord）是否落敌星座（inimical Rāśi）
- 六宫主（Ari's Lord）是否燃烧
- 八宫主（Randhr's Lord）是否落陷
- 八宫主（Randhr's Lord）是否落敌星座（inimical Rāśi）
- 八宫主（Randhr's Lord）是否燃烧
- 十二宫主（Vyaya's Lord）是否落陷
- 十二宫主（Vyaya's Lord）是否落敌星座（inimical Rāśi）
- 十二宫主（Vyaya's Lord）是否燃烧
- 上升主（Lagn's Lord）是否落自己主管的星座（own Rāśi）
- 上升主（Lagn's Lord）是否入旺

## 依赖方法

- 无

## 执行步骤

### ch39-v20-dusthana-lords-afflicted-raj-yog.step-001

- 动作：先认出六宫主、八宫主、十二宫主与上升主，再核对三个宫主各自是落陷、落敌星座还是燃烧，并核对上升主的星座状态与它对上升宫的相照。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文以复数写三个宫主的状态，未指明三者是否须处于同一种状态，本方法按每个宫主各自满足三种状态之一处理；原文没有时间限定。
- 原文最小意思：六宫主（Ari's Lord）、八宫主（Randhr's Lord）与十二宫主（Vyaya's Lord）落陷、落敌星座（inimical Rāśis）或燃烧（combustion），同时上升主（Lagn's Lord）落自己主管的星座（own Rāśi）或入旺星座（exaltation Rāśi）并相照上升（Lagn）时，Raj Yog 成立。
- 本步骤产出事实：["三凶宫主受损与上升主得地的贵格判定"]
- 所需事实：["本盘六宫主（Ari's Lord）是哪颗行星", "本盘八宫主（Randhr's Lord）是哪颗行星", "本盘十二宫主（Vyaya's Lord）是哪颗行星", "本盘上升主（Lagn's Lord）是哪颗行星", "上升主（Lagn's Lord）是否相照上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, {"operator": "OR", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落陷"}, {"fact_key": "六宫主（Ari's Lord）是否落敌星座（inimical Rāśi）"}, {"fact_key": "六宫主（Ari's Lord）是否燃烧"}]}, {"operator": "OR", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落陷"}, {"fact_key": "八宫主（Randhr's Lord）是否落敌星座（inimical Rāśi）"}, {"fact_key": "八宫主（Randhr's Lord）是否燃烧"}]}, {"operator": "OR", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否落陷"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落敌星座（inimical Rāśi）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否燃烧"}]}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落自己主管的星座（own Rāśi）"}, {"fact_key": "上升主（Lagn's Lord）是否入旺"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["六宫主（Ari's Lord）是否落陷"], "branch_condition_logic": {"fact_key": "六宫主（Ari's Lord）是否落陷"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:ari-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫主（Ari's Lord）是否落陷。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["六宫主（Ari's Lord）是否落敌星座（inimical Rāśi）"], "branch_condition_logic": {"fact_key": "六宫主（Ari's Lord）是否落敌星座（inimical Rāśi）"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:ari-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫主（Ari's Lord）是否落敌星座（inimical Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["六宫主（Ari's Lord）是否燃烧"], "branch_condition_logic": {"fact_key": "六宫主（Ari's Lord）是否燃烧"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:ari-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫主（Ari's Lord）是否燃烧。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["八宫主（Randhr's Lord）是否落陷"], "branch_condition_logic": {"fact_key": "八宫主（Randhr's Lord）是否落陷"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:randhr-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）是否落陷。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["八宫主（Randhr's Lord）是否落敌星座（inimical Rāśi）"], "branch_condition_logic": {"fact_key": "八宫主（Randhr's Lord）是否落敌星座（inimical Rāśi）"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:randhr-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）是否落敌星座（inimical Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["八宫主（Randhr's Lord）是否燃烧"], "branch_condition_logic": {"fact_key": "八宫主（Randhr's Lord）是否燃烧"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:randhr-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）是否燃烧。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否落陷"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否落陷"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:vyaya-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否落陷。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否落敌星座（inimical Rāśi）"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否落敌星座（inimical Rāśi）"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:vyaya-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否落敌星座（inimical Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否燃烧"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否燃烧"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:vyaya-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否燃烧。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否落自己主管的星座（own Rāśi）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落自己主管的星座（own Rāśi）"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:lagn-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落自己主管的星座（own Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）是哪颗行星"}, {"fact_key": "本盘八宫主（Randhr's Lord）是哪颗行星"}, {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否入旺"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否入旺"}, "selection_group": "ch39-v20-dusthana-lords-afflicted-raj-yog.step-001:lagn-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["own Rāśi 是行星自己主管的星座，不得读成落本宫。", "不得据此推断疾病、损失或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘六宫主（Ari's Lord）是哪颗行星、本盘八宫主（Randhr's Lord）是哪颗行星、本盘十二宫主（Vyaya's Lord）是哪颗行星、本盘上升主（Lagn's Lord）是哪颗行星、上升主（Lagn's Lord）是否相照上升宫（Lagna）。
- 缺失即停字段：["本盘六宫主（Ari's Lord）是哪颗行星", "本盘八宫主（Randhr's Lord）是哪颗行星", "本盘十二宫主（Vyaya's Lord）是哪颗行星", "本盘上升主（Lagn's Lord）是哪颗行星", "上升主（Lagn's Lord）是否相照上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v20`｜PDF [83]｜“Again a Raj Yog is formed, if Ari’s, Randhr’s and Vyaya’s Lords are in fall, or in inimical Rāśis, or in combustion, as Lagn’s Lord, placed in his own Rāśi, or in its exaltation Rāśi, gives a Drishti to Lagn.”


## 四路查书计划

### 支持路

- Again a Raj Yog is formed, if Ari’s, Randhr’s and Vyaya’s Lords are in fall, or in inimical Rāśis, or in combustion, as Lagn’s Lord, placed in his own Rāśi, or in its exaltation Rāśi, gives a Drishti to Lagn
- 六八十二宫主落陷燃烧 上升主相照上升 贵格

### 反例或取消路

- Note the Grahas, that are ruling the Rāśis, occupied by the Lords of Ari, Randhr and Vyaya Bhava. If the said dispositors are in such evil Bhavas in turn and are associated with, or receive a Drishti from malefics, the native will be miserable and indigent
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 四个宫主的身份事实缺任一项时停止。
- 任一宫主的三种状态事实全部缺失时停止。
- 上升主的居本星座与入旺两项事实全部缺失时停止。
- 缺少上升主相照上升宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
