---
method: ch39-v44-one-two-or-three-exalted
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 一至三颗行星入旺：王族出身者成为国王，另一人与国王相当或富有

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 盘里有几颗入旺的行星才算好
- 入旺行星不多还有希望吗

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘入旺的行星有几颗

## 按情况检查的事实

- 本盘入旺的行星是否恰有一颗
- 本盘入旺的行星是否恰有两颗
- 本盘入旺的行星是否恰有三颗

## 依赖方法

- 无

## 执行步骤

### ch39-v44-one-two-or-three-exalted.step-001

- 动作：数本盘入旺的行星有几颗，再核对是一颗、两颗还是三颗。
- 适用范围：仅限本命盘；原文把结果分给两个人（one of a royal scion 与 another），既未说明哪一档入旺颗数对应哪一种结果，也未界定 another 指谁；原文没有时间限定。
- 原文最小意思：有一颗、两颗或三颗行星入旺时，王族出身者会成为国王，另一人则与国王相当，或者富有。
- 本步骤产出事实：["一至三颗行星入旺的身份判定"]
- 所需事实：["本盘入旺的行星有几颗"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘入旺的行星有几颗"}, {"operator": "OR", "operands": [{"fact_key": "本盘入旺的行星是否恰有一颗"}, {"fact_key": "本盘入旺的行星是否恰有两颗"}, {"fact_key": "本盘入旺的行星是否恰有三颗"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘入旺的行星有几颗"}, "required_fact_keys": ["本盘入旺的行星是否恰有一颗"], "branch_condition_logic": {"fact_key": "本盘入旺的行星是否恰有一颗"}, "selection_group": "ch39-v44-one-two-or-three-exalted.step-001:how-many-exalted", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘入旺的行星是否恰有一颗。"}, {"when": {"fact_key": "本盘入旺的行星有几颗"}, "required_fact_keys": ["本盘入旺的行星是否恰有两颗"], "branch_condition_logic": {"fact_key": "本盘入旺的行星是否恰有两颗"}, "selection_group": "ch39-v44-one-two-or-three-exalted.step-001:how-many-exalted", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘入旺的行星是否恰有两颗。"}, {"when": {"fact_key": "本盘入旺的行星有几颗"}, "required_fact_keys": ["本盘入旺的行星是否恰有三颗"], "branch_condition_logic": {"fact_key": "本盘入旺的行星是否恰有三颗"}, "selection_group": "ch39-v44-one-two-or-three-exalted.step-001:how-many-exalted", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘入旺的行星是否恰有三颗。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文指定 another 的所指，也不得把入旺颗数与两种结果一一对应。", "不得去掉 royal scion（王族出身）这一限定。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘入旺的行星有几颗。
- 缺失即停字段：["本盘入旺的行星有几颗"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v44`｜PDF [84]｜“If one, or two, or three Grahas are in exaltation, one of a royal scion will become a king, while another will be equal to a king, or be wealthy.”


## 四路查书计划

### 支持路

- If one, or two, or three Grahas are in exaltation, one of a royal scion will become a king, while another will be equal to a king, or be wealthy
- 一颗两颗三颗行星入旺 王族出身 国王

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

- 缺少本盘入旺行星计数事实时停止。
- 命主是否为王族出身未确定时，国王一档断语停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
