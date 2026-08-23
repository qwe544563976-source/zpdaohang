---
method: ch39-v13-14-shad-varga-raj-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升六分盘被同一行星占据或相照：贵格无疑，效果随相照分数分档

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的贵格到底有多强
- 六分盘同一颗星管着上升说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升（Lagna）的六分盘（Shad Vargas）分别落在哪些星座

## 按情况检查的事实

- 上升（Lagna）的六分盘（Shad Vargas）是否被同一颗行星占据
- 上升（Lagna）的六分盘（Shad Vargas）是否被同一颗行星相照
- 该行星对上升六分盘（Shad Vargas）的相照是否为全相照
- 该行星对上升六分盘（Shad Vargas）的相照是否为半相照
- 该行星对上升六分盘（Shad Vargas）的相照是否为 1/4 相照

## 依赖方法

- 无

## 执行步骤

### ch39-v13-14-shad-varga-raj-yog.step-001

- 动作：先取上升（Lagn）的六分盘（Shad Vargas）诸位置，再核对它们是否被同一颗行星占据，或受同一颗行星相照。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文没有时间限定。
- 原文最小意思：上升（Lagn）的六分盘（Shad Vargas）被同一颗行星占据，或受同一颗行星相照时，Raj Yog 无疑成立。
- 本步骤产出事实：["上升六分盘同一行星的贵格判定"]
- 所需事实：["本盘上升（Lagna）的六分盘（Shad Vargas）分别落在哪些星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagna）的六分盘（Shad Vargas）分别落在哪些星座"}, {"operator": "OR", "operands": [{"fact_key": "上升（Lagna）的六分盘（Shad Vargas）是否被同一颗行星占据"}, {"fact_key": "上升（Lagna）的六分盘（Shad Vargas）是否被同一颗行星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升（Lagna）的六分盘（Shad Vargas）分别落在哪些星座"}, "required_fact_keys": ["上升（Lagna）的六分盘（Shad Vargas）是否被同一颗行星占据"], "branch_condition_logic": {"fact_key": "上升（Lagna）的六分盘（Shad Vargas）是否被同一颗行星占据"}, "selection_group": "ch39-v13-14-shad-varga-raj-yog.step-001:occupied-or-drishti", "stop_condition": "选中该分支后，缺少以下事实即停止：上升（Lagna）的六分盘（Shad Vargas）是否被同一颗行星占据。"}, {"when": {"fact_key": "本盘上升（Lagna）的六分盘（Shad Vargas）分别落在哪些星座"}, "required_fact_keys": ["上升（Lagna）的六分盘（Shad Vargas）是否被同一颗行星相照"], "branch_condition_logic": {"fact_key": "上升（Lagna）的六分盘（Shad Vargas）是否被同一颗行星相照"}, "selection_group": "ch39-v13-14-shad-varga-raj-yog.step-001:occupied-or-drishti", "stop_condition": "选中该分支后，缺少以下事实即停止：上升（Lagna）的六分盘（Shad Vargas）是否被同一颗行星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文要求是同一颗行星，不得改成几颗行星分别占据或相照。", "不得据此推断具体权位或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagna）的六分盘（Shad Vargas）分别落在哪些星座。
- 缺失即停字段：["本盘上升（Lagna）的六分盘（Shad Vargas）分别落在哪些星座"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v13-14`｜PDF [82]｜“If the Shad Vargas of Lagn are occupied, or receive a Drishti from one and the same Grah, a Raj Yog is doubtlessly formed.”

### ch39-v13-14-shad-varga-raj-yog.step-002

- 动作：在该贵格成立后，按这颗行星相照的分数（全、半、四分之一）读取效果档次。
- 适用范围：仅限已判定该 Raj Yog 成立的本命盘；原文只给出三档相照与三档结果的次序对应，未给出别的分档。
- 原文最小意思：该 Raj Yog 成立后，相照为全相照、半相照或四分之一相照时，结果依次为全、中等与微小。
- 本步骤产出事实：["上升六分盘贵格的效果档次"]
- 所需事实：["上升六分盘同一行星的贵格判定"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升六分盘同一行星的贵格判定"}, {"operator": "OR", "operands": [{"fact_key": "该行星对上升六分盘（Shad Vargas）的相照是否为全相照"}, {"fact_key": "该行星对上升六分盘（Shad Vargas）的相照是否为半相照"}, {"fact_key": "该行星对上升六分盘（Shad Vargas）的相照是否为 1/4 相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "上升六分盘同一行星的贵格判定"}, "required_fact_keys": ["该行星对上升六分盘（Shad Vargas）的相照是否为全相照"], "branch_condition_logic": {"fact_key": "该行星对上升六分盘（Shad Vargas）的相照是否为全相照"}, "selection_group": "ch39-v13-14-shad-varga-raj-yog.step-002:drishti-share", "stop_condition": "选中该分支后，缺少以下事实即停止：该行星对上升六分盘（Shad Vargas）的相照是否为全相照。"}, {"when": {"fact_key": "上升六分盘同一行星的贵格判定"}, "required_fact_keys": ["该行星对上升六分盘（Shad Vargas）的相照是否为半相照"], "branch_condition_logic": {"fact_key": "该行星对上升六分盘（Shad Vargas）的相照是否为半相照"}, "selection_group": "ch39-v13-14-shad-varga-raj-yog.step-002:drishti-share", "stop_condition": "选中该分支后，缺少以下事实即停止：该行星对上升六分盘（Shad Vargas）的相照是否为半相照。"}, {"when": {"fact_key": "上升六分盘同一行星的贵格判定"}, "required_fact_keys": ["该行星对上升六分盘（Shad Vargas）的相照是否为 1/4 相照"], "branch_condition_logic": {"fact_key": "该行星对上升六分盘（Shad Vargas）的相照是否为 1/4 相照"}, "selection_group": "ch39-v13-14-shad-varga-raj-yog.step-002:drishti-share", "stop_condition": "选中该分支后，缺少以下事实即停止：该行星对上升六分盘（Shad Vargas）的相照是否为 1/4 相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只列全、半、四分之一三档，不得自行插入四分之三等别的档次。", "不得把「微小」加重成没有效果或凶应。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升六分盘同一行星的贵格判定。
- 缺失即停字段：["上升六分盘同一行星的贵格判定"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v13-14`｜PDF [82]｜“Accordingly, if the Drishti is full, half, or one fourth, results will be in order full, medium and negligible.”


## 四路查书计划

### 支持路

- If the Shad Vargas of Lagn are occupied, or receive a Drishti from one and the same Grah, a Raj Yog is doubtlessly formed
- Accordingly, if the Drishti is full, half, or one fourth, results will be in order full, medium and negligible
- 上升六分盘同一行星 贵格分档

### 反例或取消路

- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas
- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak

### 适用边界路

- In the ShadVarg classification the Varg designations are Kimshuk, Vyanjan, Chamar, Chatr and Kundal, according to a Grah being in 2 to 6 combinations of good Vargas
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少上升六分盘定位事实时停止。
- 占据与相照两项事实全部缺失时停止。
- 缺少相照分数事实时停在效果档次一步。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
