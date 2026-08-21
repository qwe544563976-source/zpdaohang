---
method: ch36-v25-26-khadg-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Khadg Yog：二宫主与九宫主互换星座，上升主落角宫或三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子的财运与福气怎么样
- 我在学问和本事上能到什么程度

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫主（Dhan's Lord）与九宫主（Dharm's Lord）是否互换星座

## 按情况检查的事实

- 上升主（Lagn's Lord）是否落角宫（Kendr）
- 上升主（Lagn's Lord）是否落三角宫（Kon）

## 依赖方法

- 无

## 执行步骤

### ch36-v25-26-khadg-yog.step-001

- 动作：先核对二宫主（Dhan's Lord）与九宫主（Dharm's Lord）是否互换星座，再核对上升主（Lagn's Lord）落角宫（Kendr）还是三角宫（Kon）。
- 适用范围：仅限本命盘 Khadg Yog 的成立与效果；原文只给出这一组条件，未给上升限定，也未给时间限定。角宫与三角宫的宫位名单按本书 ch07:v33-36 的界定取值。
- 原文最小意思：二宫主（Dhan's Lord）与九宫主（Dharm's Lord）互换星座（Rāśis），并且上升主（Lagn's Lord）落角宫（Kendr）或落三角宫（Kon）时，成立 Khadg Yog，命主会拥有财富、福运与快乐，通晓经论（Shastras），聪明、强大、知恩图报、技艺精湛。
- 本步骤产出事实：["Khadg Yog 成立判定"]
- 所需事实：["二宫主（Dhan's Lord）与九宫主（Dharm's Lord）是否互换星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）与九宫主（Dharm's Lord）是否互换星座"}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落角宫（Kendr）"}, {"fact_key": "上升主（Lagn's Lord）是否落三角宫（Kon）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "二宫主（Dhan's Lord）与九宫主（Dharm's Lord）是否互换星座"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落角宫（Kendr）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落角宫（Kendr）"}, "selection_group": "ch36-v25-26-khadg-yog.step-001:lagn-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落角宫（Kendr）。"}, {"when": {"fact_key": "二宫主（Dhan's Lord）与九宫主（Dharm's Lord）是否互换星座"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落三角宫（Kon）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落三角宫（Kon）"}, "selection_group": "ch36-v25-26-khadg-yog.step-001:lagn-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落三角宫（Kon）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额、来源或获得时间。", "不得把互换星座换成两星同宫或互相相照。", "不得把上升主的角宫/三角宫条件挪到二宫主或九宫主身上。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫主（Dhan's Lord）与九宫主（Dharm's Lord）是否互换星座。
- 缺失即停字段：["二宫主（Dhan's Lord）与九宫主（Dharm's Lord）是否互换星座"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v25-26`｜PDF [80]｜“Should there be an exchange of Rāśis between the Lords of Dhan and Dharm Bhava, as Lagn’s Lord is in a Kendr, or in a Kon, Khadg Yog is obtained. One with Khadg Yog will be endowed with wealth, fortunes and happiness, be learned in Shastras, be intelligent, mighty, grateful and skilful.”


## 四路查书计划

### 支持路

- Khadg Yog. Should there be an exchange of Rāśis between the Lords of Dhan and Dharm Bhava
- Khadg Yog 二宫主 九宫主 互换星座 上升主落角宫

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- If Lagn’s Lord is yuti with the Lord of Ari, Randhr, or Vyaya Bhava, or with Shani and, if Lagn’s Lord is devoid of a Drishti from a benefic, the native will be penniless

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine)

### 判断方法路

- An exchange of Rāśis between Karm’s Lord and Lagn’s Lord will make the native associated with the king in a great manner
- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava

## 上游问题

- 无

## 停止条件

- 缺少二宫主与九宫主互换星座事实时停止。
- 命中上升主分支后，缺少该分支对应的角宫或三角宫落宫事实时停止。
- 角宫与三角宫的宫位名单未按本书 ch07:v33-36 取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
