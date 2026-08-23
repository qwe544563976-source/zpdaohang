---
method: ch39-v15-three-lagnas-exalted-or-own
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三个上升位皆入旺或皆居本星座，或本命、三分盘、九分盘上升皆有入旺行星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 入旺的行星落在上升位上有多大用
- 分盘上升也要看吗

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

- 本命上升（natal Lagna）是否被入旺的行星占据
- Hora Lagna 是否被入旺的行星占据
- Ghatik Lagna 是否被入旺的行星占据
- 本命上升（natal Lagna）是否被落自己主管星座（own Rāśi）的行星占据
- Hora Lagna 是否被落自己主管星座（own Rāśi）的行星占据
- Ghatik Lagna 是否被落自己主管星座（own Rāśi）的行星占据
- 三分盘上升（Dreshkan Lagn）是否被入旺的行星占据
- 九分盘上升（Navāńś Lagn）是否被入旺的行星占据

## 依赖方法

- 无

## 执行步骤

### ch39-v15-three-lagnas-exalted-or-own.step-001

- 动作：先定出三个上升位，再核对它们是否都被入旺行星或都被落自己主管星座的行星占据；另一路核对本命上升、三分盘上升与九分盘上升是否都有入旺行星。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文没有时间限定。
- 原文最小意思：本命上升、Hora Lagna 与 Ghatik Lagna 三个上升位都被入旺的行星占据，或都被落自己主管星座（own Rāśi）的行星占据；或本命上升（natal Lagna）、三分盘上升（Dreshkan Lagn）与九分盘上升（Navāńś Lagn）都有入旺的行星时，Raj Yog 成立。
- 本步骤产出事实：["三上升位入旺或居本星座的贵格判定"]
- 所需事实：["本盘本命上升（natal Lagna）落在哪个星座", "本盘的 Hora Lagna 落在哪个星座", "本盘的 Ghatik Lagna 落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘本命上升（natal Lagna）落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "本命上升（natal Lagna）是否被入旺的行星占据"}, {"fact_key": "Hora Lagna 是否被入旺的行星占据"}, {"fact_key": "Ghatik Lagna 是否被入旺的行星占据"}]}, {"operator": "AND", "operands": [{"fact_key": "本命上升（natal Lagna）是否被落自己主管星座（own Rāśi）的行星占据"}, {"fact_key": "Hora Lagna 是否被落自己主管星座（own Rāśi）的行星占据"}, {"fact_key": "Ghatik Lagna 是否被落自己主管星座（own Rāśi）的行星占据"}]}, {"operator": "AND", "operands": [{"fact_key": "本命上升（natal Lagna）是否被入旺的行星占据"}, {"fact_key": "三分盘上升（Dreshkan Lagn）是否被入旺的行星占据"}, {"fact_key": "九分盘上升（Navāńś Lagn）是否被入旺的行星占据"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘本命上升（natal Lagna）落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, "required_fact_keys": ["本命上升（natal Lagna）是否被入旺的行星占据", "Hora Lagna 是否被入旺的行星占据", "Ghatik Lagna 是否被入旺的行星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "本命上升（natal Lagna）是否被入旺的行星占据"}, {"fact_key": "Hora Lagna 是否被入旺的行星占据"}, {"fact_key": "Ghatik Lagna 是否被入旺的行星占据"}]}, "selection_group": "ch39-v15-three-lagnas-exalted-or-own.step-001:three-lagnas-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：本命上升（natal Lagna）是否被入旺的行星占据、Hora Lagna 是否被入旺的行星占据、Ghatik Lagna 是否被入旺的行星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘本命上升（natal Lagna）落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, "required_fact_keys": ["本命上升（natal Lagna）是否被落自己主管星座（own Rāśi）的行星占据", "Hora Lagna 是否被落自己主管星座（own Rāśi）的行星占据", "Ghatik Lagna 是否被落自己主管星座（own Rāśi）的行星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "本命上升（natal Lagna）是否被落自己主管星座（own Rāśi）的行星占据"}, {"fact_key": "Hora Lagna 是否被落自己主管星座（own Rāśi）的行星占据"}, {"fact_key": "Ghatik Lagna 是否被落自己主管星座（own Rāśi）的行星占据"}]}, "selection_group": "ch39-v15-three-lagnas-exalted-or-own.step-001:three-lagnas-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：本命上升（natal Lagna）是否被落自己主管星座（own Rāśi）的行星占据、Hora Lagna 是否被落自己主管星座（own Rāśi）的行星占据、Ghatik Lagna 是否被落自己主管星座（own Rāśi）的行星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘本命上升（natal Lagna）落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, "required_fact_keys": ["本命上升（natal Lagna）是否被入旺的行星占据", "三分盘上升（Dreshkan Lagn）是否被入旺的行星占据", "九分盘上升（Navāńś Lagn）是否被入旺的行星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "本命上升（natal Lagna）是否被入旺的行星占据"}, {"fact_key": "三分盘上升（Dreshkan Lagn）是否被入旺的行星占据"}, {"fact_key": "九分盘上升（Navāńś Lagn）是否被入旺的行星占据"}]}, "selection_group": "ch39-v15-three-lagnas-exalted-or-own.step-001:three-lagnas-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：本命上升（natal Lagna）是否被入旺的行星占据、三分盘上升（Dreshkan Lagn）是否被入旺的行星占据、九分盘上升（Navāńś Lagn）是否被入旺的行星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["own Rāśi 是行星自己主管的星座，不得读成落本宫。", "Dreshkan 是三分盘（D3）、Navāńś 是九分盘（D9），不得换成别的分盘。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘本命上升（natal Lagna）落在哪个星座、本盘的 Hora Lagna 落在哪个星座、本盘的 Ghatik Lagna 落在哪个星座。
- 缺失即停字段：["本盘本命上升（natal Lagna）落在哪个星座", "本盘的 Hora Lagna 落在哪个星座", "本盘的 Ghatik Lagna 落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v15`｜PDF [82, 83]｜“If the 3 Lagnas (natal, Hora and Ghatik) are occupied by Grahas in exaltation, or in own Rāśi, or, if the natal Lagna, the Dreshkan Lagn and the Navāńś Lagn have exalted Grahas, Raj Yog is formed.”


## 四路查书计划

### 支持路

- If the 3 Lagnas (natal, Hora and Ghatik) are occupied by Grahas in exaltation, or in own Rāśi, or, if the natal Lagna, the Dreshkan Lagn and the Navāńś Lagn have exalted Grahas, Raj Yog is formed
- 三个上升位入旺 三分盘九分盘上升 贵格

### 反例或取消路

- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless

### 适用边界路

- I explain below again some special Lagnas, viz. Bhava Lagna, Hora Lagn and Ghati Lagn
- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- This happens, when Lagn in the RashiKundali and the Navāńś Lagn are in the same Rāśi

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少 Hora Lagna 或 Ghatik Lagna 的定位事实时停止。
- 三条成立路线的占据事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
