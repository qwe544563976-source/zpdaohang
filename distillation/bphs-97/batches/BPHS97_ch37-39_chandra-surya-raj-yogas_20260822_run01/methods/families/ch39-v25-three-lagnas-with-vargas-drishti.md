---
method: ch39-v25-three-lagnas-with-vargas-drishti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三个上升位连同其三分盘、九分盘位置受行星相照：贵格成立

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 分盘上的上升位也要看相照吗
- 我有没有靠分盘成立的贵格

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Bhava Lagna 落在哪个星座
- 本盘的 Hora Lagna 落在哪个星座
- 本盘的 Ghatik Lagna 落在哪个星座

## 按情况检查的事实

- Bhava Lagna 是否被行星相照
- Hora Lagna 是否被行星相照
- Ghatik Lagna 是否被行星相照
- Bhava Lagna 的三分盘（Dreshkana D3）位置是否被行星相照
- Hora Lagna 的三分盘（Dreshkana D3）位置是否被行星相照
- Ghatik Lagna 的三分盘（Dreshkana D3）位置是否被行星相照
- Bhava Lagna 的九分盘（Navāńś D9）位置是否被行星相照
- Hora Lagna 的九分盘（Navāńś D9）位置是否被行星相照
- Ghatik Lagna 的九分盘（Navāńś D9）位置是否被行星相照

## 依赖方法

- 无

## 执行步骤

### ch39-v25-three-lagnas-with-vargas-drishti.step-001

- 动作：先定出三个上升位及其三分盘与九分盘位置，再核对原文所列三种组合中是否有一组全部受行星相照。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文的 the said Lagnas 指同句前面的 Bhava、Hora、Ghatik 三个上升位；原文没有时间限定。
- 原文最小意思：Bhava Lagna、Hora Lagna 与 Ghatik Lagn 连同它们的三分盘（Dreshkanas D3）与九分盘（Navāńśas D9）位置，或这三个上升位连同它们的九分盘位置，或这三个上升位连同它们的三分盘位置，都受一颗行星相照时，Raj Yog 成立。
- 本步骤产出事实：["三上升位连同分盘受照的贵格判定"]
- 所需事实：["本盘的 Bhava Lagna 落在哪个星座", "本盘的 Hora Lagna 落在哪个星座", "本盘的 Ghatik Lagna 落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘的 Bhava Lagna 落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "Bhava Lagna 是否被行星相照"}, {"fact_key": "Hora Lagna 是否被行星相照"}, {"fact_key": "Ghatik Lagna 是否被行星相照"}, {"fact_key": "Bhava Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}, {"fact_key": "Hora Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}, {"fact_key": "Ghatik Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}, {"fact_key": "Bhava Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}, {"fact_key": "Hora Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}, {"fact_key": "Ghatik Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}]}, {"operator": "AND", "operands": [{"fact_key": "Bhava Lagna 是否被行星相照"}, {"fact_key": "Hora Lagna 是否被行星相照"}, {"fact_key": "Ghatik Lagna 是否被行星相照"}, {"fact_key": "Bhava Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}, {"fact_key": "Hora Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}, {"fact_key": "Ghatik Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}]}, {"operator": "AND", "operands": [{"fact_key": "Bhava Lagna 是否被行星相照"}, {"fact_key": "Hora Lagna 是否被行星相照"}, {"fact_key": "Ghatik Lagna 是否被行星相照"}, {"fact_key": "Bhava Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}, {"fact_key": "Hora Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}, {"fact_key": "Ghatik Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Bhava Lagna 落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, "required_fact_keys": ["Bhava Lagna 是否被行星相照", "Hora Lagna 是否被行星相照", "Ghatik Lagna 是否被行星相照", "Bhava Lagna 的三分盘（Dreshkana D3）位置是否被行星相照", "Hora Lagna 的三分盘（Dreshkana D3）位置是否被行星相照", "Ghatik Lagna 的三分盘（Dreshkana D3）位置是否被行星相照", "Bhava Lagna 的九分盘（Navāńś D9）位置是否被行星相照", "Hora Lagna 的九分盘（Navāńś D9）位置是否被行星相照", "Ghatik Lagna 的九分盘（Navāńś D9）位置是否被行星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Bhava Lagna 是否被行星相照"}, {"fact_key": "Hora Lagna 是否被行星相照"}, {"fact_key": "Ghatik Lagna 是否被行星相照"}, {"fact_key": "Bhava Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}, {"fact_key": "Hora Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}, {"fact_key": "Ghatik Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}, {"fact_key": "Bhava Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}, {"fact_key": "Hora Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}, {"fact_key": "Ghatik Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}]}, "selection_group": "ch39-v25-three-lagnas-with-vargas-drishti.step-001:which-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：Bhava Lagna 是否被行星相照、Hora Lagna 是否被行星相照、Ghatik Lagna 是否被行星相照、Bhava Lagna 的三分盘（Dreshkana D3）位置是否被行星相照、Hora Lagna 的三分盘（Dreshkana D3）位置是否被行星相照、Ghatik Lagna 的三分盘（Dreshkana D3）位置是否被行星相照、Bhava Lagna 的九分盘（Navāńś D9）位置是否被行星相照、Hora Lagna 的九分盘（Navāńś D9）位置是否被行星相照、Ghatik Lagna 的九分盘（Navāńś D9）位置是否被行星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Bhava Lagna 落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, "required_fact_keys": ["Bhava Lagna 是否被行星相照", "Hora Lagna 是否被行星相照", "Ghatik Lagna 是否被行星相照", "Bhava Lagna 的九分盘（Navāńś D9）位置是否被行星相照", "Hora Lagna 的九分盘（Navāńś D9）位置是否被行星相照", "Ghatik Lagna 的九分盘（Navāńś D9）位置是否被行星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Bhava Lagna 是否被行星相照"}, {"fact_key": "Hora Lagna 是否被行星相照"}, {"fact_key": "Ghatik Lagna 是否被行星相照"}, {"fact_key": "Bhava Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}, {"fact_key": "Hora Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}, {"fact_key": "Ghatik Lagna 的九分盘（Navāńś D9）位置是否被行星相照"}]}, "selection_group": "ch39-v25-three-lagnas-with-vargas-drishti.step-001:which-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：Bhava Lagna 是否被行星相照、Hora Lagna 是否被行星相照、Ghatik Lagna 是否被行星相照、Bhava Lagna 的九分盘（Navāńś D9）位置是否被行星相照、Hora Lagna 的九分盘（Navāńś D9）位置是否被行星相照、Ghatik Lagna 的九分盘（Navāńś D9）位置是否被行星相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘的 Bhava Lagna 落在哪个星座"}, {"fact_key": "本盘的 Hora Lagna 落在哪个星座"}, {"fact_key": "本盘的 Ghatik Lagna 落在哪个星座"}]}, "required_fact_keys": ["Bhava Lagna 是否被行星相照", "Hora Lagna 是否被行星相照", "Ghatik Lagna 是否被行星相照", "Bhava Lagna 的三分盘（Dreshkana D3）位置是否被行星相照", "Hora Lagna 的三分盘（Dreshkana D3）位置是否被行星相照", "Ghatik Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Bhava Lagna 是否被行星相照"}, {"fact_key": "Hora Lagna 是否被行星相照"}, {"fact_key": "Ghatik Lagna 是否被行星相照"}, {"fact_key": "Bhava Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}, {"fact_key": "Hora Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}, {"fact_key": "Ghatik Lagna 的三分盘（Dreshkana D3）位置是否被行星相照"}]}, "selection_group": "ch39-v25-three-lagnas-with-vargas-drishti.step-001:which-combination", "stop_condition": "选中该分支后，缺少以下事实即停止：Bhava Lagna 是否被行星相照、Hora Lagna 是否被行星相照、Ghatik Lagna 是否被行星相照、Bhava Lagna 的三分盘（Dreshkana D3）位置是否被行星相照、Hora Lagna 的三分盘（Dreshkana D3）位置是否被行星相照、Ghatik Lagna 的三分盘（Dreshkana D3）位置是否被行星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["Dreshkana 是三分盘（D3）、Navāńś 是九分盘（D9），不得换成别的分盘。", "原文没有限定相照的行星是吉是凶，不得自行加上吉星限定。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Bhava Lagna 落在哪个星座、本盘的 Hora Lagna 落在哪个星座、本盘的 Ghatik Lagna 落在哪个星座。
- 缺失即停字段：["本盘的 Bhava Lagna 落在哪个星座", "本盘的 Hora Lagna 落在哪个星座", "本盘的 Ghatik Lagna 落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v25`｜PDF [83]｜“If Bhava, Hora and Ghatik Lagnas, their Dreshkanas and Navāńśas, or the said Lagnas and their Navāńśas, or the said Lagnas and their Dreshkanas receive a Drishti from a Grah, a Raj Yog is formed.”


## 四路查书计划

### 支持路

- If Bhava, Hora and Ghatik Lagnas, their Dreshkanas and Navāńśas, or the said Lagnas and their Navāńśas, or the said Lagnas and their Dreshkanas receive a Drishti from a Grah, a Raj Yog is formed
- 三个上升位及其三分盘九分盘受相照 贵格

### 反例或取消路

- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas
- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak

### 适用边界路

- I explain below again some special Lagnas, viz. Bhava Lagna, Hora Lagn and Ghati Lagn
- This happens, when Lagn in the RashiKundali and the Navāńś Lagn are in the same Rāśi
- In the Dasha Varg scheme the designations commence from Parijata etc., such as 2 good Vargas - Parijatha, 3 Uttama, 4 Gopur, 5 Simhasan

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少三个上升位的定位事实时停止。
- 三种组合的受照事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
