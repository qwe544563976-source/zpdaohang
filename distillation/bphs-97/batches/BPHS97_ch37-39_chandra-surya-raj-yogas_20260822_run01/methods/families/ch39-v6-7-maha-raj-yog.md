---
method: ch39-v6-7-maha-raj-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Maha Raj Yog：上升主与五宫主互换星座，或 Atma Karak 与 Putr Karak 居五处之一并受吉照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有大贵格
- 我会不会出名又过得快乐

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）是哪颗行星
- 本盘五宫主（Putr's Lord）是哪颗行星
- 本盘的 Atma Karak 是哪颗行星
- 本盘的 Putr Karak 是哪颗行星

## 按情况检查的事实

- 上升主（Lagn's Lord）与五宫主（Putr's Lord）是否互换星座（Rāśi）
- Atma Karak 是否落上升宫（Lagna）
- Putr Karak 是否落上升宫（Lagna）
- Atma Karak 是否落五宫（Putr Bhava）
- Putr Karak 是否落五宫（Putr Bhava）
- Atma Karak 是否入旺
- Putr Karak 是否入旺
- Atma Karak 是否落自己主管的星座（own Rāśi）
- Putr Karak 是否落自己主管的星座（own Rāśi）
- Atma Karak 在九分盘（Navāńś D9）中是否落自己主管的星座
- Putr Karak 在九分盘（Navāńś D9）中是否落自己主管的星座
- Atma Karak 是否被吉星相照
- Putr Karak 是否被吉星相照

## 依赖方法

- 无

## 执行步骤

### ch39-v6-7-maha-raj-yog.step-001

- 动作：先认出上升主、五宫主、Atma Karak 与 Putr Karak 四颗行星，再核对是否有宫主互换星座，或 Atma Karak 与 Putr Karak 同落原文所列五处之一并受吉星相照，判定 Maha Raj Yog 是否成立。
- 适用范围：仅限本命盘 Maha Raj Yog 的成立判定；原文把 receiving a Drishti from a benefic 写在 Atma Karak 与 Putr Karak 那一串位置之后，未言明这项吉照是否同样适用于宫主互换一路，本方法照原文位置只挂在 Atma Karak 与 Putr Karak 一路；原文没有时间限定。
- 原文最小意思：上升主（Lagn's Lord）与五宫主（Putr's Lord）互换星座（Rāśis）；或 Atma Karak 与 Putr Karak 同落上升宫（Lagna）、落五宫（Putr Bhava）、落入旺星座（exaltation Rāśi）、落自己主管的星座（own Rāśi）或落自己主管的九分盘（own Navāńś）星座，并受吉星相照——两路之一成立时，Maha Raj Yog 成立。
- 本步骤产出事实：["Maha Raj Yog 成立判定"]
- 所需事实：["本盘上升主（Lagn's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星", "本盘的 Atma Karak 是哪颗行星", "本盘的 Putr Karak 是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Putr Karak 是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagn's Lord）与五宫主（Putr's Lord）是否互换星座（Rāśi）"}, {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否落上升宫（Lagna）"}, {"fact_key": "Putr Karak 是否落上升宫（Lagna）"}, {"fact_key": "Atma Karak 是否被吉星相照"}, {"fact_key": "Putr Karak 是否被吉星相照"}]}, {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否落五宫（Putr Bhava）"}, {"fact_key": "Putr Karak 是否落五宫（Putr Bhava）"}, {"fact_key": "Atma Karak 是否被吉星相照"}, {"fact_key": "Putr Karak 是否被吉星相照"}]}, {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否入旺"}, {"fact_key": "Putr Karak 是否入旺"}, {"fact_key": "Atma Karak 是否被吉星相照"}, {"fact_key": "Putr Karak 是否被吉星相照"}]}, {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否落自己主管的星座（own Rāśi）"}, {"fact_key": "Putr Karak 是否落自己主管的星座（own Rāśi）"}, {"fact_key": "Atma Karak 是否被吉星相照"}, {"fact_key": "Putr Karak 是否被吉星相照"}]}, {"operator": "AND", "operands": [{"fact_key": "Atma Karak 在九分盘（Navāńś D9）中是否落自己主管的星座"}, {"fact_key": "Putr Karak 在九分盘（Navāńś D9）中是否落自己主管的星座"}, {"fact_key": "Atma Karak 是否被吉星相照"}, {"fact_key": "Putr Karak 是否被吉星相照"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Putr Karak 是哪颗行星"}]}, "required_fact_keys": ["上升主（Lagn's Lord）与五宫主（Putr's Lord）是否互换星座（Rāśi）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）与五宫主（Putr's Lord）是否互换星座（Rāśi）"}, "selection_group": "ch39-v6-7-maha-raj-yog.step-001:maha-raj-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）与五宫主（Putr's Lord）是否互换星座（Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Putr Karak 是哪颗行星"}]}, "required_fact_keys": ["Atma Karak 是否落上升宫（Lagna）", "Putr Karak 是否落上升宫（Lagna）", "Atma Karak 是否被吉星相照", "Putr Karak 是否被吉星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否落上升宫（Lagna）"}, {"fact_key": "Putr Karak 是否落上升宫（Lagna）"}, {"fact_key": "Atma Karak 是否被吉星相照"}, {"fact_key": "Putr Karak 是否被吉星相照"}]}, "selection_group": "ch39-v6-7-maha-raj-yog.step-001:maha-raj-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落上升宫（Lagna）、Putr Karak 是否落上升宫（Lagna）、Atma Karak 是否被吉星相照、Putr Karak 是否被吉星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Putr Karak 是哪颗行星"}]}, "required_fact_keys": ["Atma Karak 是否落五宫（Putr Bhava）", "Putr Karak 是否落五宫（Putr Bhava）", "Atma Karak 是否被吉星相照", "Putr Karak 是否被吉星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否落五宫（Putr Bhava）"}, {"fact_key": "Putr Karak 是否落五宫（Putr Bhava）"}, {"fact_key": "Atma Karak 是否被吉星相照"}, {"fact_key": "Putr Karak 是否被吉星相照"}]}, "selection_group": "ch39-v6-7-maha-raj-yog.step-001:maha-raj-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落五宫（Putr Bhava）、Putr Karak 是否落五宫（Putr Bhava）、Atma Karak 是否被吉星相照、Putr Karak 是否被吉星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Putr Karak 是哪颗行星"}]}, "required_fact_keys": ["Atma Karak 是否入旺", "Putr Karak 是否入旺", "Atma Karak 是否被吉星相照", "Putr Karak 是否被吉星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否入旺"}, {"fact_key": "Putr Karak 是否入旺"}, {"fact_key": "Atma Karak 是否被吉星相照"}, {"fact_key": "Putr Karak 是否被吉星相照"}]}, "selection_group": "ch39-v6-7-maha-raj-yog.step-001:maha-raj-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否入旺、Putr Karak 是否入旺、Atma Karak 是否被吉星相照、Putr Karak 是否被吉星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Putr Karak 是哪颗行星"}]}, "required_fact_keys": ["Atma Karak 是否落自己主管的星座（own Rāśi）", "Putr Karak 是否落自己主管的星座（own Rāśi）", "Atma Karak 是否被吉星相照", "Putr Karak 是否被吉星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Atma Karak 是否落自己主管的星座（own Rāśi）"}, {"fact_key": "Putr Karak 是否落自己主管的星座（own Rāśi）"}, {"fact_key": "Atma Karak 是否被吉星相照"}, {"fact_key": "Putr Karak 是否被吉星相照"}]}, "selection_group": "ch39-v6-7-maha-raj-yog.step-001:maha-raj-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 是否落自己主管的星座（own Rāśi）、Putr Karak 是否落自己主管的星座（own Rāśi）、Atma Karak 是否被吉星相照、Putr Karak 是否被吉星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "本盘的 Putr Karak 是哪颗行星"}]}, "required_fact_keys": ["Atma Karak 在九分盘（Navāńś D9）中是否落自己主管的星座", "Putr Karak 在九分盘（Navāńś D9）中是否落自己主管的星座", "Atma Karak 是否被吉星相照", "Putr Karak 是否被吉星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Atma Karak 在九分盘（Navāńś D9）中是否落自己主管的星座"}, {"fact_key": "Putr Karak 在九分盘（Navāńś D9）中是否落自己主管的星座"}, {"fact_key": "Atma Karak 是否被吉星相照"}, {"fact_key": "Putr Karak 是否被吉星相照"}]}, "selection_group": "ch39-v6-7-maha-raj-yog.step-001:maha-raj-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 在九分盘（Navāńś D9）中是否落自己主管的星座、Putr Karak 在九分盘（Navāńś D9）中是否落自己主管的星座、Atma Karak 是否被吉星相照、Putr Karak 是否被吉星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["own Rāśi 是行星自己主管的星座，不得读成落本宫。", "不得把吉照要求扩大到宫主互换一路，也不得把它从 Atma Karak 与 Putr Karak 一路删去。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）是哪颗行星、本盘五宫主（Putr's Lord）是哪颗行星、本盘的 Atma Karak 是哪颗行星、本盘的 Putr Karak 是哪颗行星。
- 缺失即停字段：["本盘上升主（Lagn's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星", "本盘的 Atma Karak 是哪颗行星", "本盘的 Putr Karak 是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v6-7`｜PDF [82]｜“Should Lagn’s Lord and Putr’s Lord exchange their Rāśis, or, if Atma Karak and Putr Karak (Char) are in Lagna, or in Putr Bhava, or in the exaltation Rāśi, or in own Rāśi, or in own Navāńś, receiving a Drishti from a benefic, Maha Raj Yog is produced.”

### ch39-v6-7-maha-raj-yog.step-002

- 动作：在 Maha Raj Yog 成立时读取名声与快乐断语。
- 适用范围：仅限已判定 Maha Raj Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：这样出生的命主（Maha Raj Yog 成立者）会有名声且快乐。
- 本步骤产出事实：["Maha Raj Yog 效果断语"]
- 所需事实：["Maha Raj Yog 成立判定"]
- 条件关系：{"fact_key": "Maha Raj Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断王位、官职或成名时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Maha Raj Yog 成立判定。
- 缺失即停字段：["Maha Raj Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v6-7`｜PDF [82]｜“The native so born will be famous and happy.”


## 四路查书计划

### 支持路

- Should Lagn’s Lord and Putr’s Lord exchange their Rāśis, or, if Atma Karak and Putr Karak (Char) are in Lagna, or in Putr Bhava, or in the exaltation Rāśi, or in own Rāśi, or in own Navāńś, receiving a Drishti from a benefic, Maha Raj Yog is produced
- 上升主五宫主互换星座 Maha Raj Yog 有名声快乐

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Karakāńś is the Navāńś, occupied by the Atma Karak Grah
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 上升主、五宫主、Atma Karak、Putr Karak 四项身份事实缺任一项时停止。
- 两路成立条件的分支事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
