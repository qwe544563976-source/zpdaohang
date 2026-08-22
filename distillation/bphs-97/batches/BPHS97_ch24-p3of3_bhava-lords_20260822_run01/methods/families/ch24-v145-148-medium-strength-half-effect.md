---
method: ch24-v145-148-medium-strength-half-effect
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 宫主星力量为中等：给出一半效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 力量中等的宫主星效果打几折
- 我这颗宫主星不强不弱该怎么断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 该宫主行星（Grah）的力量档次是否为中等

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v145-148-medium-strength-half-effect.step-001

- 动作：核对该宫主行星（Grah）的力量档次是否为中等，据此判断它交出多少比例的效果。
- 适用范围：适用于本章各宫主落各宫的效果推断（同偈自述「those are the effects of Bhava Lords」）；原文用「respectively」把满、中等、微弱三档力量与全部、一半、四分之一三档效果一一对应，本方法只取其中一档，另两档另立方法；原文没有给出这三档力量的判准，未确定即停判；原文未给时间限定。
- 原文最小意思：该宫主行星（Grah）的力量档次为中等时，该行星给出一半的效果。
- 本步骤产出事实：["宫主行星力量为中等时的效果比例判定"]
- 所需事实：["该宫主行星（Grah）的力量档次是否为中等"]
- 条件关系：{"fact_key": "该宫主行星（Grah）的力量档次是否为中等"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文定义满、中等、微弱三档力量的算法；未确定即停判。", "不得把比例换算成具体分数以外的强度描述或时间。", "不得把本条只取的这一档套到另外两档上。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：该宫主行星（Grah）的力量档次是否为中等。
- 缺失即停字段：["该宫主行星（Grah）的力量档次是否为中等"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v145-148`｜PDF [50]｜“The Grah will yield full, half, or a quarter of the effects according to its strength being full, medium and negligible, respectively.”


## 四路查书计划

### 支持路

- The Grah will yield full, half, or a quarter of the effects according to its strength being full, medium and negligible, respectively.
- 宫主行星力量中等 效果比例

### 反例或取消路

- 无

### 适用边界路

- those are the effects of Bhava Lords, which are to be deduced, considering their strengths and weaknesses
- Effects of the Bhava Lords
- 宫主效果按力量打折的适用范围

### 判断方法路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Effects of the Bhava Lords
- 怎么判断一颗行星的强弱

## 上游问题

- 无

## 停止条件

- 缺少该宫主行星力量档次的事实时停止。
- 原文未给满、中等、微弱三档的判准，未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
