---
method: ch36-v21-22-matsya-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Matsya Yog：吉星落九宫与一宫、五宫吉凶混杂、凶星落四宫与八宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有做占星师这一行的命
- 我的性情与名望怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫（Dharm）是否被吉星占据
- 一宫（Tanu）是否被吉星占据
- 五宫（Putr）是否被吉凶混杂的行星占据
- 四宫（Bandhu）是否被凶星占据
- 八宫（Randhr）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch36-v21-22-matsya-yog.step-001

- 动作：核对九宫（Dharm）与一宫（Tanu）内的吉星、五宫（Putr）内吉凶混杂的行星、四宫（Bandhu）与八宫（Randhr）内的凶星，判断 Matsya Yog 是否成立及其效果。
- 适用范围：仅限本命盘 Matsya Yog 的成立与效果；原文把五项宫位条件并列成同一组盘面配置，未给上升限定，也未给时间限定。吉星与凶星的名册按本书 ch03:v11 的界定取值。
- 原文最小意思：吉星落九宫（Dharm）与一宫（Tanu）、五宫（Putr）内是吉凶混杂的行星、凶星落四宫（Bandhu）与八宫（Randhr）时，出生盘会形成 Matsya Yog，命主会成为占星师（Jyotishi）、是仁慈的同义词、有德、强壮、美貌、有名、有学问、虔诚。
- 本步骤产出事实：["Matsya Yog 成立判定"]
- 所需事实：["九宫（Dharm）是否被吉星占据", "一宫（Tanu）是否被吉星占据", "五宫（Putr）是否被吉凶混杂的行星占据", "四宫（Bandhu）是否被凶星占据", "八宫（Randhr）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫（Dharm）是否被吉星占据"}, {"fact_key": "一宫（Tanu）是否被吉星占据"}, {"fact_key": "五宫（Putr）是否被吉凶混杂的行星占据"}, {"fact_key": "四宫（Bandhu）是否被凶星占据"}, {"fact_key": "八宫（Randhr）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断收入数额、寿命或事件发生的时间。", "不得把五项盘面条件拆开单用；原文把它们写成同一组配置。", "原文只说五宫内是吉凶混杂的行星，不得改写成某颗特定行星落五宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫（Dharm）是否被吉星占据、一宫（Tanu）是否被吉星占据、五宫（Putr）是否被吉凶混杂的行星占据、四宫（Bandhu）是否被凶星占据、八宫（Randhr）是否被凶星占据。
- 缺失即停字段：["九宫（Dharm）是否被吉星占据", "一宫（Tanu）是否被吉星占据", "五宫（Putr）是否被吉凶混杂的行星占据", "四宫（Bandhu）是否被凶星占据", "八宫（Randhr）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v21-22`｜PDF [80]｜“Benefics in Dharm and Tanu Bhava, mixed Grahas in Putr Bhava and malefics in Bandhu and Randhr Bhava: this array of Grahas at birth will produce Matsya Yog. In effect the native will be a Jyotishi, be a synonym of kindness, be virtuous, strong, beautiful, famous, learned and pious.”


## 四路查书计划

### 支持路

- Matsya Yog. Benefics in Dharm and Tanu Bhava, mixed Grahas in Putr Bhava and malefics in Bandhu and Randhr Bhava
- Matsya Yog 占星师 Jyotishi 吉星九宫一宫 凶星四宫八宫

### 反例或取消路

- If there be a benefic in Lagna, Subh Yog is produced, while a malefic in Lagn causes Asubh Yog
- Budh in Dhan Bhava, while malefics occupy Tanu and Vyaya Bhava: this Yoga will destroy the entire family
- The Bhava, which is not drishtied by its Lord, or, whose Lord is with a malefic Grah, or with one of the Lords of evil and such other Bhavas

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 判断方法路

- Prosperity, or Annihilation of a Bhava. Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

## 上游问题

- 无

## 停止条件

- 缺少九宫、一宫、五宫、四宫、八宫任一项占据事实时停止。
- 吉星与凶星名册未按本书 ch03:v11 取到时停止。
- 原文未定义「吉凶混杂的行星」的最少颗数，取值口径未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
