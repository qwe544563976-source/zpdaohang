---
method: ch39-v29-31-debilitated-in-ari-randhr-drishti-lagn
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 落陷行星居六宫或八宫并相照上升：同样成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 落陷的行星在坏宫里反而好吗
- 六宫八宫的落陷行星有什么用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘六宫（Ari）内有哪些行星
- 本盘八宫（Randhr）内有哪些行星

## 按情况检查的事实

- 落六宫（Ari）的落陷行星是否相照上升宫（Lagna）
- 落八宫（Randhr）的落陷行星是否相照上升宫（Lagna）

## 依赖方法

- 无

## 执行步骤

### ch39-v29-31-debilitated-in-ari-randhr-drishti-lagn.step-001

- 动作：看六宫与八宫内有哪些行星，核对其中是否有落陷的行星相照上升宫。
- 适用范围：仅限本命盘；原文的 The same effect 承同偈前句的国王断语；原文没有时间限定。
- 原文最小意思：有落陷的行星相照上升（Lagn）并落在六宫（Ari），或落在八宫（Randhr）时，同样会成为国王。
- 本步骤产出事实：["六宫八宫落陷行星相照上升的贵格判定"]
- 所需事实：["本盘六宫（Ari）内有哪些行星", "本盘八宫（Randhr）内有哪些行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘六宫（Ari）内有哪些行星"}, {"fact_key": "本盘八宫（Randhr）内有哪些行星"}]}, {"operator": "OR", "operands": [{"fact_key": "落六宫（Ari）的落陷行星是否相照上升宫（Lagna）"}, {"fact_key": "落八宫（Randhr）的落陷行星是否相照上升宫（Lagna）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫（Ari）内有哪些行星"}, {"fact_key": "本盘八宫（Randhr）内有哪些行星"}]}, "required_fact_keys": ["落六宫（Ari）的落陷行星是否相照上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "落六宫（Ari）的落陷行星是否相照上升宫（Lagna）"}, "selection_group": "ch39-v29-31-debilitated-in-ari-randhr-drishti-lagn.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：落六宫（Ari）的落陷行星是否相照上升宫（Lagna）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘六宫（Ari）内有哪些行星"}, {"fact_key": "本盘八宫（Randhr）内有哪些行星"}]}, "required_fact_keys": ["落八宫（Randhr）的落陷行星是否相照上升宫（Lagna）"], "branch_condition_logic": {"fact_key": "落八宫（Randhr）的落陷行星是否相照上升宫（Lagna）"}, "selection_group": "ch39-v29-31-debilitated-in-ari-randhr-drishti-lagn.step-001:which-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：落八宫（Randhr）的落陷行星是否相照上升宫（Lagna）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写六宫与八宫两处，不得把十二宫或别的宫位也算进来。", "不得据此推断疾病、损失或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘六宫（Ari）内有哪些行星、本盘八宫（Randhr）内有哪些行星。
- 缺失即停字段：["本盘六宫（Ari）内有哪些行星", "本盘八宫（Randhr）内有哪些行星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v29-31`｜PDF [83]｜“The same effect will be obtained, if a debilitated Grah gives a Drishti to Lagn and is placed in Ari, or Randhr Bhava.”
  - `bphs-97:santhanam:ch39:v29-31`｜PDF [83]｜“The native will become a king”


## 四路查书计划

### 支持路

- The same effect will be obtained, if a debilitated Grah gives a Drishti to Lagn and is placed in Ari, or Randhr Bhava
- 落陷行星在六宫八宫相照上升 国王

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- The native will be penniless, if Lagn’s Lord is in Ari Bhava, while Ari’s Lord is in Lagna, yuti with, or receiving a Drishti from a Marak Lord

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- 缺少六宫或八宫的占据事实时停止。
- 两条分支的落陷行星相照事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
