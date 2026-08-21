---
method: ch17-v9-relatives-similar-estimate
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 亲属的同类推断：从各自的指示星与宫位照此估量

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 同样的病能不能推到我父亲身上
- 亲属的疾病该从哪里看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 所论亲属的指示星（Karak）是哪颗行星
- 所论亲属对应的宫位（Bhava）是第几宫

## 按情况检查的事实

- 无

## 依赖方法

- ch17-v9-lagna-lords-graha-diseases
- ch17-v9-chandra-water-danger

## 执行步骤

### ch17-v9-relatives-similar-estimate.step-001

- 动作：换用所论亲属的指示星与对应宫位，照本章的同一套估量方式推断该亲属。
- 适用范围：原文为方法性指示，举父亲为例；未说明可推到哪些亲属，也未给时间限定。
- 原文最小意思：对亲属（如父亲），应从各自的指示星与宫位作同样的推断。
- 本步骤产出事实：["亲属同类推断的适用判定"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应的宫位（Bhava）是第几宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应的宫位（Bhava）是第几宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此为亲属新增本章没有列出的病症或年份。", "不得据此把本人的结论直接当作亲属的结论。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应的宫位（Bhava）是第几宫。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应的宫位（Bhava）是第几宫"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v9-12.5`｜PDF [32]｜“Similar estimates be made from the respective significators and Bhavas for relatives, like father.”


## 四路查书计划

### 支持路

- Similar estimates be made from the respective significators and Bhavas for relatives, like father
- 亲属 指示星 宫位 同样推断

### 反例或取消路

- The limb, related to a benefic, will have a mark (like moles etc)
- Guru in similar case will destroy any disease

### 适用边界路

- Constant Karakatwas the stronger among Surya and Shukra indicates the father
- The 9th from Surya denotes father, the 4th from Chandra mother

### 判断方法路

- Bhavas Related these constant significances are derivable from the Bhavas, counted from the said constant Karakatwas
- 如何换算亲属的宫位与指示星

## 上游问题

- 无

## 停止条件

- 缺少所论亲属的指示星身份事实时停止。
- 缺少所论亲属对应宫位事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
