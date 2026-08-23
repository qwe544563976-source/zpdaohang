---
method: ch39-v45-four-or-five-exalted-or-mooltrikon
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 四或五颗行星居入旺星座或 Mooltrikon 星座：出身低微也成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 出身普通还能不能大富大贵
- Mooltrikon 和入旺一样有力吗

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘落自己入旺星座（exaltation Rāśi）的行星有几颗
- 本盘落自己 Mooltrikon 星座的行星有几颗

## 按情况检查的事实

- 本盘落自己入旺星座（exaltation Rāśi）的行星是否有四颗
- 本盘落自己入旺星座（exaltation Rāśi）的行星是否有五颗
- 本盘落自己 Mooltrikon 星座的行星是否有四颗
- 本盘落自己 Mooltrikon 星座的行星是否有五颗

## 依赖方法

- 无

## 执行步骤

### ch39-v45-four-or-five-exalted-or-mooltrikon.step-001

- 动作：分别数落自己入旺星座与落自己 Mooltrikon 星座的行星颗数，核对是否达到四颗或五颗。
- 适用范围：仅限本命盘；原文没有时间限定。
- 原文最小意思：有四颗或五颗行星落自己的入旺星座（exaltation Rāśis），或落自己的 Mooltrikon 星座时，即使出身低微者也会成为国王。
- 本步骤产出事实：["四五颗行星得地的成王判定"]
- 所需事实：["本盘落自己入旺星座（exaltation Rāśi）的行星有几颗", "本盘落自己 Mooltrikon 星座的行星有几颗"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘落自己入旺星座（exaltation Rāśi）的行星有几颗"}, {"fact_key": "本盘落自己 Mooltrikon 星座的行星有几颗"}]}, {"operator": "OR", "operands": [{"fact_key": "本盘落自己入旺星座（exaltation Rāśi）的行星是否有四颗"}, {"fact_key": "本盘落自己入旺星座（exaltation Rāśi）的行星是否有五颗"}, {"fact_key": "本盘落自己 Mooltrikon 星座的行星是否有四颗"}, {"fact_key": "本盘落自己 Mooltrikon 星座的行星是否有五颗"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘落自己入旺星座（exaltation Rāśi）的行星有几颗"}, {"fact_key": "本盘落自己 Mooltrikon 星座的行星有几颗"}]}, "required_fact_keys": ["本盘落自己入旺星座（exaltation Rāśi）的行星是否有四颗"], "branch_condition_logic": {"fact_key": "本盘落自己入旺星座（exaltation Rāśi）的行星是否有四颗"}, "selection_group": "ch39-v45-four-or-five-exalted-or-mooltrikon.step-001:dignity-and-count", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘落自己入旺星座（exaltation Rāśi）的行星是否有四颗。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘落自己入旺星座（exaltation Rāśi）的行星有几颗"}, {"fact_key": "本盘落自己 Mooltrikon 星座的行星有几颗"}]}, "required_fact_keys": ["本盘落自己入旺星座（exaltation Rāśi）的行星是否有五颗"], "branch_condition_logic": {"fact_key": "本盘落自己入旺星座（exaltation Rāśi）的行星是否有五颗"}, "selection_group": "ch39-v45-four-or-five-exalted-or-mooltrikon.step-001:dignity-and-count", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘落自己入旺星座（exaltation Rāśi）的行星是否有五颗。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘落自己入旺星座（exaltation Rāśi）的行星有几颗"}, {"fact_key": "本盘落自己 Mooltrikon 星座的行星有几颗"}]}, "required_fact_keys": ["本盘落自己 Mooltrikon 星座的行星是否有四颗"], "branch_condition_logic": {"fact_key": "本盘落自己 Mooltrikon 星座的行星是否有四颗"}, "selection_group": "ch39-v45-four-or-five-exalted-or-mooltrikon.step-001:dignity-and-count", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘落自己 Mooltrikon 星座的行星是否有四颗。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘落自己入旺星座（exaltation Rāśi）的行星有几颗"}, {"fact_key": "本盘落自己 Mooltrikon 星座的行星有几颗"}]}, "required_fact_keys": ["本盘落自己 Mooltrikon 星座的行星是否有五颗"], "branch_condition_logic": {"fact_key": "本盘落自己 Mooltrikon 星座的行星是否有五颗"}, "selection_group": "ch39-v45-four-or-five-exalted-or-mooltrikon.step-001:dignity-and-count", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘落自己 Mooltrikon 星座的行星是否有五颗。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写四颗与五颗两档，不得把三颗或六颗也按这一条判。", "入旺与 Mooltrikon 是两种不同的得地状态，不得混为一谈。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘落自己入旺星座（exaltation Rāśi）的行星有几颗、本盘落自己 Mooltrikon 星座的行星有几颗。
- 缺失即停字段：["本盘落自己入旺星座（exaltation Rāśi）的行星有几颗", "本盘落自己 Mooltrikon 星座的行星有几颗"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v45`｜PDF [84]｜“If four, or five Grahas occupy their exaltation Rāśis, or Mooltrikon Rāśis, even a person of base birth will become king.”


## 四路查书计划

### 支持路

- If four, or five Grahas occupy their exaltation Rāśis, or Mooltrikon Rāśis, even a person of base birth will become king
- 四颗五颗行星入旺或根本三角 出身低微成王

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- In Simh the first 20 degrees are Surya’s Mooltrikon, while the rest is his own Bhava

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少入旺或 Mooltrikon 行星计数事实时停止。
- 四条分支的计数判定事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
