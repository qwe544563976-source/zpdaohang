---
method: ch39-v21-karm-lord-drishti-raj-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 十宫主落本宫或入旺并相照上升宫：贵格成立

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的事业宫主管得好不好
- 十宫主照上升说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘十宫主（Karm's Lord）是哪颗行星
- 十宫主（Karm's Lord）是否相照上升宫（Lagna）

## 按情况检查的事实

- 十宫主（Karm's Lord）是否落本宫（own Bhava）
- 十宫主（Karm's Lord）是否入旺

## 依赖方法

- 无

## 执行步骤

### ch39-v21-karm-lord-drishti-raj-yog.step-001

- 动作：先认出十宫主（Karm's Lord），核对它是落本宫还是入旺，再核对它是否相照上升宫。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文没有时间限定。
- 原文最小意思：十宫主（Karm's Lord）落本宫（own Bhava）或落入旺星座（exaltation Rāśi），并相照上升宫（Lagna）时，Raj Yog 成立。
- 本步骤产出事实：["十宫主相照上升的贵格判定"]
- 所需事实：["本盘十宫主（Karm's Lord）是哪颗行星", "十宫主（Karm's Lord）是否相照上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "十宫主（Karm's Lord）是否相照上升宫（Lagna）"}]}, {"operator": "OR", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落本宫（own Bhava）"}, {"fact_key": "十宫主（Karm's Lord）是否入旺"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "十宫主（Karm's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否落本宫（own Bhava）"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否落本宫（own Bhava）"}, "selection_group": "ch39-v21-karm-lord-drishti-raj-yog.step-001:karm-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否落本宫（own Bhava）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "十宫主（Karm's Lord）是否相照上升宫（Lagna）"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否入旺"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否入旺"}, "selection_group": "ch39-v21-karm-lord-drishti-raj-yog.step-001:karm-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文写的是 own Bhava（本宫），不得换成自己主管的星座。", "不得据此推断职位、收入或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘十宫主（Karm's Lord）是哪颗行星、十宫主（Karm's Lord）是否相照上升宫（Lagna）。
- 缺失即停字段：["本盘十宫主（Karm's Lord）是哪颗行星", "十宫主（Karm's Lord）是否相照上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v21`｜PDF [83]｜“If Karm’s Lord, placed in his own Bhava, or in its exaltation Rāśi, gives a Drishti to Lagna, a Raj Yog is formed.”


## 四路查书计划

### 支持路

- If Karm’s Lord, placed in his own Bhava, or in its exaltation Rāśi, gives a Drishti to Lagna, a Raj Yog is formed
- 十宫主落本宫入旺 相照上升 贵格

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少十宫主身份事实时停止。
- 十宫主落本宫与入旺两项事实全部缺失时停止。
- 缺少十宫主相照上升宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
