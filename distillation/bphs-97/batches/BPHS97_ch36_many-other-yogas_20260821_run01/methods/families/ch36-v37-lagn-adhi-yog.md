---
method: ch36-v37-lagn-adhi-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Lagn Adhi Yog：从上升起算的七宫与八宫有吉星且不受凶星同宫与相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子能不能成为有分量的人
- 我的学问和心境怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 七宫（Yuvati）是否被吉星占据
- 八宫（Randhr）是否被吉星占据
- 七宫（Yuvati）与八宫（Randhr）内的吉星是否与凶星同宫
- 七宫（Yuvati）与八宫（Randhr）内的吉星是否被凶星相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch36-v37-lagn-adhi-yog.step-001

- 动作：先核对从上升起算的七宫（Yuvati）与八宫（Randhr）内是否有吉星，再逐条核对这些吉星是否与凶星同宫、是否被凶星相照，两条都必须落空。
- 适用范围：仅限本命盘 Lagn Adhi Yog 的成立与效果；原文写的是 devoid of Yuti with and/or Drishti from malefics，两条侵扰通道都落在 devoid of 的否定辖域内，因此基座条件按合取接线（同宫与相照都必须不成立）；选择组只用来登记原文并列的这两条必查通道，在合取的基座条件下被吸收，不会放宽成立面。原文未给时间限定。
- 原文最小意思：从上升（Lagn）起算的七宫（Yuvati）与八宫（Randhr）内有吉星，且这些吉星不与凶星同宫、也不被凶星相照时，成立 Lagn Adhi Yog，命主会成为伟人、通晓经论（Shastras）、快乐。
- 本步骤产出事实：["Lagn Adhi Yog 成立判定"]
- 所需事实：["七宫（Yuvati）是否被吉星占据", "八宫（Randhr）是否被吉星占据", "七宫（Yuvati）与八宫（Randhr）内的吉星是否与凶星同宫", "七宫（Yuvati）与八宫（Randhr）内的吉星是否被凶星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "七宫（Yuvati）是否被吉星占据"}, {"fact_key": "八宫（Randhr）是否被吉星占据"}, {"operator": "NOT", "operands": [{"fact_key": "七宫（Yuvati）与八宫（Randhr）内的吉星是否与凶星同宫"}]}, {"operator": "NOT", "operands": [{"fact_key": "七宫（Yuvati）与八宫（Randhr）内的吉星是否被凶星相照"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写了七宫与八宫，不得比照别处的 Adhi Yog 补出六宫。", "不得把「不与凶星同宫」与「不被凶星相照」改成二选一；两条都必须落空。", "不得据此推断具体的地位、职衔或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：七宫（Yuvati）是否被吉星占据、八宫（Randhr）是否被吉星占据、七宫（Yuvati）与八宫（Randhr）内的吉星是否与凶星同宫、七宫（Yuvati）与八宫（Randhr）内的吉星是否被凶星相照。
- 缺失即停字段：["七宫（Yuvati）是否被吉星占据", "八宫（Randhr）是否被吉星占据", "七宫（Yuvati）与八宫（Randhr）内的吉星是否与凶星同宫", "七宫（Yuvati）与八宫（Randhr）内的吉星是否被凶星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v37`｜PDF [81]｜“Should benefics be in Yuvati and Randhr Bhava, counted from Lagn and be devoid of Yuti with and/or Drishti from malefics, Lagn Adhi Yog is produced, making one a great person, learned in Shastras and happy.”


## 四路查书计划

### 支持路

- Lagn Adhi Yog. Should benefics be in Yuvati and Randhr Bhava, counted from Lagn and be devoid of Yuti with and/or Drishti from malefics
- Lagn Adhi Yog 七宫八宫吉星 无凶星同宫 无凶星相照

### 反例或取消路

- If there be a benefic in Lagna, Subh Yog is produced, while a malefic in Lagn causes Asubh Yog
- The Bhava, which is not drishtied by its Lord, or, whose Lord is with a malefic Grah, or with one of the Lords of evil and such other Bhavas
- If Lagn’s Lord is yuti with the Lord of Ari, Randhr, or Vyaya Bhava, or with Shani and, if Lagn’s Lord is devoid of a Drishti from a benefic, the native will be penniless

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Drishtis of the Grahas. O Brahmin, I have earlier stated Drishtis, based on Rāśis. The other kind is between Grahas

### 判断方法路

- Prosperity, or Annihilation of a Bhava. Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic
- Indications of Randhr Bhava. Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead

## 上游问题

- 无

## 停止条件

- 缺少七宫或八宫吉星占据事实时停止。
- 缺少吉星与凶星同宫事实或吉星被凶星相照事实时停止。
- 吉星与凶星名册未按本书 ch03:v11 取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
