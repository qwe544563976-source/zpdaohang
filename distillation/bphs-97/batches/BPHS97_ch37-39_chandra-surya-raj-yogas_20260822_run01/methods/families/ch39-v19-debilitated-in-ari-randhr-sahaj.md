---
method: ch39-v19-debilitated-in-ari-randhr-sahaj
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 六宫、八宫、三宫皆落陷行星，上升主入旺或落本宫并相照上升

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 落陷的行星一定不好吗
- 上升主相照上升宫有多重要

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 六宫（Ari）是否被落陷的行星占据
- 八宫（Randhr）是否被落陷的行星占据
- 三宫（Sahaj）是否被落陷的行星占据
- 上升主（Lagn's Lord）是否相照上升宫（Lagna）
- 本盘上升主（Lagn's Lord）是哪颗行星

## 按情况检查的事实

- 上升主（Lagn's Lord）是否入旺
- 上升主（Lagn's Lord）是否落本宫（own Bhava）

## 依赖方法

- 无

## 执行步骤

### ch39-v19-debilitated-in-ari-randhr-sahaj.step-001

- 动作：核对六宫、八宫、三宫是否都被落陷的行星占据，再核对上升主是入旺还是落本宫，并核对它是否相照上升宫。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文没有时间限定。
- 原文最小意思：六宫（Ari）、八宫（Randhr）与三宫（Sahaj）都被落陷的行星占据，同时上升主（Lagn's Lord）入旺或落本宫（own Bhava）并相照上升宫（Lagna）时，Raj Yog 成立。
- 本步骤产出事实：["三凶宫落陷行星与上升主的贵格判定"]
- 所需事实：["六宫（Ari）是否被落陷的行星占据", "八宫（Randhr）是否被落陷的行星占据", "三宫（Sahaj）是否被落陷的行星占据", "上升主（Lagn's Lord）是否相照上升宫（Lagna）", "本盘上升主（Lagn's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "六宫（Ari）是否被落陷的行星占据"}, {"fact_key": "八宫（Randhr）是否被落陷的行星占据"}, {"fact_key": "三宫（Sahaj）是否被落陷的行星占据"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagn's Lord）是否入旺"}, {"fact_key": "上升主（Lagn's Lord）是否落本宫（own Bhava）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "六宫（Ari）是否被落陷的行星占据"}, {"fact_key": "八宫（Randhr）是否被落陷的行星占据"}, {"fact_key": "三宫（Sahaj）是否被落陷的行星占据"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否入旺"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否入旺"}, "selection_group": "ch39-v19-debilitated-in-ari-randhr-sahaj.step-001:lagn-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否入旺。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "六宫（Ari）是否被落陷的行星占据"}, {"fact_key": "八宫（Randhr）是否被落陷的行星占据"}, {"fact_key": "三宫（Sahaj）是否被落陷的行星占据"}, {"fact_key": "上升主（Lagn's Lord）是否相照上升宫（Lagna）"}, {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否落本宫（own Bhava）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落本宫（own Bhava）"}, "selection_group": "ch39-v19-debilitated-in-ari-randhr-sahaj.step-001:lagn-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落本宫（own Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文的落陷行星只写六宫、八宫、三宫三处，不得增减宫位。", "不得据此推断疾病、债务或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：六宫（Ari）是否被落陷的行星占据、八宫（Randhr）是否被落陷的行星占据、三宫（Sahaj）是否被落陷的行星占据、上升主（Lagn's Lord）是否相照上升宫（Lagna）、本盘上升主（Lagn's Lord）是哪颗行星。
- 缺失即停字段：["六宫（Ari）是否被落陷的行星占据", "八宫（Randhr）是否被落陷的行星占据", "三宫（Sahaj）是否被落陷的行星占据", "上升主（Lagn's Lord）是否相照上升宫（Lagna）", "本盘上升主（Lagn's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v19`｜PDF [83]｜“If Ari, Randhr and Sahaj Bhava are occupied by debilitated Grahas, as Lagn’s Lord is exalted, or is in own Bhava and gives a Drishti to Lagna, there is a Raj Yog.”


## 四路查书计划

### 支持路

- If Ari, Randhr and Sahaj Bhava are occupied by debilitated Grahas, as Lagn’s Lord is exalted, or is in own Bhava and gives a Drishti to Lagna, there is a Raj Yog
- 六宫八宫三宫落陷行星 上升主入旺 贵格

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- If Lagn’s Lord is yuti with the Lord of Ari, Randhr, or Vyaya Bhava, or with Shani and, if Lagn’s Lord is devoid of a Drishti from a benefic, the native will be penniless

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 三个宫位的落陷占据事实缺任一项时停止。
- 上升主入旺与落本宫两项事实全部缺失时停止。
- 缺少上升主相照上升宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
