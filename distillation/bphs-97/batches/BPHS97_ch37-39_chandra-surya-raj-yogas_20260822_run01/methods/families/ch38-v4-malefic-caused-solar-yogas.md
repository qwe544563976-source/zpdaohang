---
method: ch38-v4-malefic-caused-solar-yogas
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 造成 Vesi、Vosi、Ubhayachari 的是凶星：产生相反的效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 凶星造成的瑜伽还算好格局吗
- 我这组太阳瑜伽为什么不灵

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星

## 按情况检查的事实

- 造成 Vesi Yog 的行星是否为凶星
- 造成 Vosi Yog 的行星是否为凶星
- 造成 Ubhayachari Yog 的行星是否为凶星

## 依赖方法

- 无

## 执行步骤

### ch38-v4-malefic-caused-solar-yogas.step-001

- 动作：先取本盘凶星名册，再核对造成 Vesi、Vosi 或 Ubhayachari 瑜伽的那颗行星是否为凶星，据此判定会产生相反的效果。
- 适用范围：原文只说 contrary effects（相反的效果），并未逐项列出相反效果的内容；相反效果的具体内容未确定即停判。本句的对照对象是同章 ch38:v1 与 ch38:v2-3。
- 原文最小意思：由凶星造成的 Vesi、Vosi 或 Ubhayachari 瑜伽，会产生相反的效果。
- 本步骤产出事实：["三种太阳瑜伽的凶星致格判定"]
- 所需事实：["本盘中哪些行星被判为凶星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"operator": "OR", "operands": [{"fact_key": "造成 Vesi Yog 的行星是否为凶星"}, {"fact_key": "造成 Vosi Yog 的行星是否为凶星"}, {"fact_key": "造成 Ubhayachari Yog 的行星是否为凶星"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些行星被判为凶星"}, "required_fact_keys": ["造成 Vesi Yog 的行星是否为凶星"], "branch_condition_logic": {"fact_key": "造成 Vesi Yog 的行星是否为凶星"}, "selection_group": "ch38-v4-malefic-caused-solar-yogas.step-001:which-yoga", "stop_condition": "选中该分支后，缺少以下事实即停止：造成 Vesi Yog 的行星是否为凶星。"}, {"when": {"fact_key": "本盘中哪些行星被判为凶星"}, "required_fact_keys": ["造成 Vosi Yog 的行星是否为凶星"], "branch_condition_logic": {"fact_key": "造成 Vosi Yog 的行星是否为凶星"}, "selection_group": "ch38-v4-malefic-caused-solar-yogas.step-001:which-yoga", "stop_condition": "选中该分支后，缺少以下事实即停止：造成 Vosi Yog 的行星是否为凶星。"}, {"when": {"fact_key": "本盘中哪些行星被判为凶星"}, "required_fact_keys": ["造成 Ubhayachari Yog 的行星是否为凶星"], "branch_condition_logic": {"fact_key": "造成 Ubhayachari Yog 的行星是否为凶星"}, "selection_group": "ch38-v4-malefic-caused-solar-yogas.step-001:which-yoga", "stop_condition": "选中该分支后，缺少以下事实即停止：造成 Ubhayachari Yog 的行星是否为凶星。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文把 contrary effects 展开成 ch38:v2-3 各项效果的逐条否定。", "不得据此推断贫穷、疾病或寿命等原文没写的内容。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星。
- 缺失即停字段：["本盘中哪些行星被判为凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch38:v4`｜PDF [82]｜“Benefics, causing Vesi, Vosi, or Ubhayachari Yogas, will give the above-mentioned effects, while malefics will produce contrary effects.”


## 四路查书计划

### 支持路

- while malefics will produce contrary effects
- 凶星造成 Vesi Vosi Ubhayachari 相反效果

### 反例或取消路

- Benefics, causing Vesi, Vosi, or Ubhayachari Yogas, will give the above-mentioned effects

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Budh, however, is a malefic, if he joins a malefic
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn

## 上游问题

- 无

## 停止条件

- 缺少本盘凶星名册事实时停止。
- 无法确认造成该瑜伽的是哪颗行星时停止。
- 原文未列出 contrary effects 的具体内容，需要展开为逐项断语时停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
