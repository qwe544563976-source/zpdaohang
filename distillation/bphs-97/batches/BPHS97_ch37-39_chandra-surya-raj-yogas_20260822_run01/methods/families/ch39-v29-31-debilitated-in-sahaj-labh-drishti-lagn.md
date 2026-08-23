---
method: ch39-v29-31-debilitated-in-sahaj-labh-drishti-lagn
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 落陷行星居三宫或十一宫并相照上升：同样成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 三宫十一宫的落陷行星说明什么
- 落陷行星还能成贵格吗

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘三宫（Sahaj）内有哪些行星
- 本盘十一宫（Labh）内有哪些行星

## 按情况检查的事实

- 落三宫（Sahaj）的落陷行星是否相照上升宫（Lagna）
- 落十一宫（Labh）的落陷行星是否相照上升宫（Lagna）

## 依赖方法

- 无

## 执行步骤

### ch39-v29-31-debilitated-in-sahaj-labh-drishti-lagn.step-001

- 动作：看三宫与十一宫内有哪些行星，核对其中是否有落陷的行星相照上升宫。
- 适用范围：仅限本命盘；原文的 Again similar result 承同偈前面的国王断语；原文没有时间限定。
- 原文最小意思：落陷的行星落三宫（Sahaj）或十一宫（Labh）并相照上升（Lagn）时，同样的结果成立，即会成为国王。
- 本步骤产出事实：["三宫十一宫落陷行星相照上升的贵格判定"]
- 所需事实：["本盘三宫（Sahaj）内有哪些行星", "本盘十一宫（Labh）内有哪些行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘三宫（Sahaj）内有哪些行星"}, {"fact_key": "本盘十一宫（Labh）内有哪些行星"}]}, {"operator": "OR", "operands": [{"fact_key": "落三宫（Sahaj）的落陷行星是否相照上升宫（Lagna）"}, {"fact_key": "落十一宫（Labh）的落陷行星是否相照上升宫（Lagna）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘三宫（Sahaj）内有哪些行星"}, {"fact_key": "本盘十一宫（Labh）内有哪些行星"}]}, "required_fact_keys": ["落三宫（Sahaj）的落陷行星是否相照上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "落三宫（Sahaj）的落陷行星是否相照上升宫（Lagna）"}, "selection_group": "ch39-v29-31-debilitated-in-sahaj-labh-drishti-lagn.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：落三宫（Sahaj）的落陷行星是否相照上升宫（Lagna）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘三宫（Sahaj）内有哪些行星"}, {"fact_key": "本盘十一宫（Labh）内有哪些行星"}]}, "required_fact_keys": ["落十一宫（Labh）的落陷行星是否相照上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "落十一宫（Labh）的落陷行星是否相照上升宫（Lagna）"}, "selection_group": "ch39-v29-31-debilitated-in-sahaj-labh-drishti-lagn.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：落十一宫（Labh）的落陷行星是否相照上升宫（Lagna）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写三宫与十一宫两处，不得把六宫、八宫等别的宫位也算进来。", "不得据此推断收益数额或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘三宫（Sahaj）内有哪些行星、本盘十一宫（Labh）内有哪些行星。
- 缺失即停字段：["本盘三宫（Sahaj）内有哪些行星", "本盘十一宫（Labh）内有哪些行星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v29-31`｜PDF [83]｜“Again similar result will prevail, if a debilitated Grah, placed in Sahaj, or Labh Bhava, gives a Drishti to Lagn.”
  - `bphs-97:santhanam:ch39:v29-31`｜PDF [83]｜“The native will become a king”


## 四路查书计划

### 支持路

- Again similar result will prevail, if a debilitated Grah, placed in Sahaj, or Labh Bhava, gives a Drishti to Lagn
- 落陷行星在三宫十一宫相照上升 国王

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Sahaj, Ari, Karm and Labh Bhava are Upachaya Bhavas

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- 缺少三宫或十一宫的占据事实时停止。
- 两条分支的落陷行星相照事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
