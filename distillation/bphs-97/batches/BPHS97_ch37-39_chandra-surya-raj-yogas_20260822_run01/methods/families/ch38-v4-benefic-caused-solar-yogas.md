---
method: ch38-v4-benefic-caused-solar-yogas
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 造成 Vesi、Vosi、Ubhayachari 的是吉星：给出上文所说的效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这三种太阳组合到底是好是坏
- 造成瑜伽的那颗星是吉是凶要紧吗

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 造成 Vesi Yog 的行星是否为吉星
- 造成 Vosi Yog 的行星是否为吉星
- 造成 Ubhayachari Yog 的行星是否为吉星

## 依赖方法

- 无

## 执行步骤

### ch38-v4-benefic-caused-solar-yogas.step-001

- 动作：先取本盘吉星名册，再核对造成 Vesi、Vosi 或 Ubhayachari 瑜伽的那颗行星是否为吉星，据此决定是否给出上文所说的效果。
- 适用范围：原文的 the above-mentioned effects 指同章前两偈：ch38:v1 的三种瑜伽定义与 ch38:v2-3 各自的效果；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：由吉星造成的 Vesi、Vosi 或 Ubhayachari 瑜伽，会给出上文所说的那些效果。
- 本步骤产出事实：["三种太阳瑜伽的吉星致格判定"]
- 所需事实：["本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"operator": "OR", "operands": [{"fact_key": "造成 Vesi Yog 的行星是否为吉星"}, {"fact_key": "造成 Vosi Yog 的行星是否为吉星"}, {"fact_key": "造成 Ubhayachari Yog 的行星是否为吉星"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["造成 Vesi Yog 的行星是否为吉星"], "branch_condition_logic": {"fact_key": "造成 Vesi Yog 的行星是否为吉星"}, "selection_group": "ch38-v4-benefic-caused-solar-yogas.step-001:which-yoga", "stop_condition": "选中该分支后，缺少以下事实即停止：造成 Vesi Yog 的行星是否为吉星。"}, {"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["造成 Vosi Yog 的行星是否为吉星"], "branch_condition_logic": {"fact_key": "造成 Vosi Yog 的行星是否为吉星"}, "selection_group": "ch38-v4-benefic-caused-solar-yogas.step-001:which-yoga", "stop_condition": "选中该分支后，缺少以下事实即停止：造成 Vosi Yog 的行星是否为吉星。"}, {"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["造成 Ubhayachari Yog 的行星是否为吉星"], "branch_condition_logic": {"fact_key": "造成 Ubhayachari Yog 的行星是否为吉星"}, "selection_group": "ch38-v4-benefic-caused-solar-yogas.step-001:which-yoga", "stop_condition": "选中该分支后，缺少以下事实即停止：造成 Ubhayachari Yog 的行星是否为吉星。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 the above-mentioned effects 扩大到 ch38 前两偈以外的内容。", "不得据此为三种瑜伽增补原文没有的效果条目。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch38:v4`｜PDF [82]｜“Benefics, causing Vesi, Vosi, or Ubhayachari Yogas, will give the above-mentioned effects”


## 四路查书计划

### 支持路

- Benefics, causing Vesi, Vosi, or Ubhayachari Yogas, will give the above-mentioned effects
- 吉星造成 Vesi Vosi Ubhayachari 给出上述效果

### 反例或取消路

- while malefics will produce contrary effects
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Budh, however, is a malefic, if he joins a malefic

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn

## 上游问题

- 无

## 停止条件

- 缺少本盘吉星名册事实时停止。
- 无法确认造成该瑜伽的是哪颗行星时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
