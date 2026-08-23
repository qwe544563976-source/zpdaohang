---
method: ch39-v11-shukra-royal-circles
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 金星居 Karakāńś、其第5宫、上升或 Arudh Lagna 并与木星或月亮成关系：与王室圈子有关

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会跟上层圈子有来往
- 金星在我盘里代表什么机会

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Karakāńś 是哪个星座

## 按情况检查的事实

- 金星（Shukra）是否即 Karakāńś
- 金星（Shukra）是否落 Karakāńś 起算的第5宫
- 金星（Shukra）是否落上升宫（Lagna）
- 金星（Shukra）是否落 Arudh Lagna
- 金星（Shukra）是否被木星（Guru）相照
- 金星（Shukra）是否被月亮（Chandra）相照
- 金星（Shukra）是否与木星（Guru）同宫
- 金星（Shukra）是否与月亮（Chandra）同宫

## 依赖方法

- 无

## 执行步骤

### ch39-v11-shukra-royal-circles.step-001

- 动作：先取本盘 Karakāńś，再核对金星（Shukra）落在原文所列四处中的哪一处，以及它与木星（Guru）或月亮（Chandra）的相照或同宫关系。
- 适用范围：仅限本命盘与王室圈子关联的判断；原文没有时间限定。
- 原文最小意思：金星（Shukra）即 Karakāńś，或落其起算的第5宫，或落上升宫（Lagna），或落 Arudh Lagna，并受木星（Guru）或月亮（Chandra）相照或与之同宫时，命主会与王室圈子有关联。
- 本步骤产出事实：["金星与王室圈子关联判定"]
- 所需事实：["本盘的 Karakāńś 是哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘的 Karakāńś 是哪个星座"}, {"operator": "OR", "operands": [{"fact_key": "金星（Shukra）是否即 Karakāńś"}, {"fact_key": "金星（Shukra）是否落 Karakāńś 起算的第5宫"}, {"fact_key": "金星（Shukra）是否落上升宫（Lagna）"}, {"fact_key": "金星（Shukra）是否落 Arudh Lagna"}]}, {"operator": "OR", "operands": [{"fact_key": "金星（Shukra）是否被木星（Guru）相照"}, {"fact_key": "金星（Shukra）是否被月亮（Chandra）相照"}, {"fact_key": "金星（Shukra）是否与木星（Guru）同宫"}, {"fact_key": "金星（Shukra）是否与月亮（Chandra）同宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘的 Karakāńś 是哪个星座"}, "required_fact_keys": ["金星（Shukra）是否即 Karakāńś"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否即 Karakāńś"}, "selection_group": "ch39-v11-shukra-royal-circles.step-001:shukra-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否即 Karakāńś。"}, {"when": {"fact_key": "本盘的 Karakāńś 是哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落 Karakāńś 起算的第5宫"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落 Karakāńś 起算的第5宫"}, "selection_group": "ch39-v11-shukra-royal-circles.step-001:shukra-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落 Karakāńś 起算的第5宫。"}, {"when": {"fact_key": "本盘的 Karakāńś 是哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落上升宫（Lagna）"}, "selection_group": "ch39-v11-shukra-royal-circles.step-001:shukra-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落上升宫（Lagna）。"}, {"when": {"fact_key": "本盘的 Karakāńś 是哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落 Arudh Lagna"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落 Arudh Lagna"}, "selection_group": "ch39-v11-shukra-royal-circles.step-001:shukra-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落 Arudh Lagna。"}, {"when": {"fact_key": "本盘的 Karakāńś 是哪个星座"}, "required_fact_keys": ["金星（Shukra）是否被木星（Guru）相照"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否被木星（Guru）相照"}, "selection_group": "ch39-v11-shukra-royal-circles.step-001:guru-or-chandra-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否被木星（Guru）相照。"}, {"when": {"fact_key": "本盘的 Karakāńś 是哪个星座"}, "required_fact_keys": ["金星（Shukra）是否被月亮（Chandra）相照"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否被月亮（Chandra）相照"}, "selection_group": "ch39-v11-shukra-royal-circles.step-001:guru-or-chandra-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否被月亮（Chandra）相照。"}, {"when": {"fact_key": "本盘的 Karakāńś 是哪个星座"}, "required_fact_keys": ["金星（Shukra）是否与木星（Guru）同宫"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否与木星（Guru）同宫"}, "selection_group": "ch39-v11-shukra-royal-circles.step-001:guru-or-chandra-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否与木星（Guru）同宫。"}, {"when": {"fact_key": "本盘的 Karakāńś 是哪个星座"}, "required_fact_keys": ["金星（Shukra）是否与月亮（Chandra）同宫"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否与月亮（Chandra）同宫"}, "selection_group": "ch39-v11-shukra-royal-circles.step-001:guru-or-chandra-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否与月亮（Chandra）同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["「与王室圈子有关联」不得加码成成为国王、获得官职或财富。", "原文只写木星与月亮两颗行星，不得换成别的行星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Karakāńś 是哪个星座。
- 缺失即停字段：["本盘的 Karakāńś 是哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v11`｜PDF [82]｜“One will be related to royal circles, if Shukra is the Karakāńś, or in the 5<sup>th</sup> there from, or in Lagna, or in Arudh Lagna, receiving a Drishti from, or yuti with Guru, or Chandra.”


## 四路查书计划

### 支持路

- One will be related to royal circles, if Shukra is the Karakāńś, or in the 5<sup>th</sup> there from, or in Lagna, or in Arudh Lagna, receiving a Drishti from, or yuti with Guru, or Chandra
- 金星在 Karakāńś 木星月亮 王室圈子

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Karakāńś is the Navāńś, occupied by the Atma Karak Grah
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas so far stated by me with reference to Lagn Pad be similarly evaluated from Karakāńś as well

## 上游问题

- 无

## 停止条件

- 缺少本盘 Karakāńś 事实时停止。
- 金星四处落点事实全部缺失时停止。
- 金星与木星或月亮的相照、同宫事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
