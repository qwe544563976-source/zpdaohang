---
method: ch36-v29-30-kusum-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Kusum Yog：固定星座上升，金星落角宫、月亮偕吉星落三角宫、土星落十宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有做大人物的命
- 我这辈子的享受和地位怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 金星（Shukra）是否落角宫（Kendr）
- 月亮（Chandra）是否落三角宫（Kon）
- 月亮（Chandra）是否与吉星同宫
- 土星（Shani）是否落十宫（Karm）
- 上升星座是否为固定星座（Fixed Rāśi）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch36-v29-30-kusum-yog.step-001

- 动作：核对上升是否为固定星座（Fixed Rāśi），再核对金星（Shukra）落角宫、月亮（Chandra）偕吉星落三角宫、土星（Shani）落十宫（Karm）三项配置。
- 适用范围：仅限本命盘 Kusum Yog 的成立与效果；原文明确限定为固定星座上升的命盘，不适用于其他上升。原文未给时间限定。
- 原文最小意思：金星（Shukra）落角宫（Kendr）、月亮（Chandra）与一颗吉星同落三角宫（Kon）、土星（Shani）落十宫（Karm），并且上升为固定星座（Fixed Rāśi）时，这些行星造成 Kusum Yog，命主会成为国王或与国王相当、乐善好施、享受快乐、幸福、在族人中居首、有德、并为 red-lettered。
- 本步骤产出事实：["Kusum Yog 成立判定"]
- 所需事实：["金星（Shukra）是否落角宫（Kendr）", "月亮（Chandra）是否落三角宫（Kon）", "月亮（Chandra）是否与吉星同宫", "土星（Shani）是否落十宫（Karm）", "上升星座是否为固定星座（Fixed Rāśi）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升星座是否为固定星座（Fixed Rāśi）"}, {"fact_key": "金星（Shukra）是否落角宫（Kendr）"}, {"fact_key": "月亮（Chandra）是否落三角宫（Kon）"}, {"fact_key": "月亮（Chandra）是否与吉星同宫"}, {"fact_key": "土星（Shani）是否落十宫（Karm）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把固定星座上升的限定去掉后套用到其他上升。", "原文的 red-lettered 未作解释，不得引申成具体的头衔、荣誉或事件。", "不得据此推断王位的形式或获得时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：金星（Shukra）是否落角宫（Kendr）、月亮（Chandra）是否落三角宫（Kon）、月亮（Chandra）是否与吉星同宫、土星（Shani）是否落十宫（Karm）、上升星座是否为固定星座（Fixed Rāśi）。
- 缺失即停字段：["金星（Shukra）是否落角宫（Kendr）", "月亮（Chandra）是否落三角宫（Kon）", "月亮（Chandra）是否与吉星同宫", "土星（Shani）是否落十宫（Karm）", "上升星座是否为固定星座（Fixed Rāśi）"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v29-30`｜PDF [80]｜“Shukra in a Kendr, Chandra in a Kon along with a benefic and Shani in Karm Bhava: these Grahas thus cause Kusum Yog for one born in a Fixed Rashiascending. Such a native will be a king, or equal to him, be charitable, will enjoy pleasures, be happy, prime among his race men, virtuous and red-lettered.”


## 四路查书计划

### 支持路

- Kusum Yog. Shukra in a Kendr, Chandra in a Kon along with a benefic and Shani in Karm Bhava
- Kusum Yog 固定星座上升 金星角宫 月亮三角宫 土星十宫

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- Budh in Dhan Bhava, while malefics occupy Tanu and Vyaya Bhava: this Yoga will destroy the entire family

### 适用边界路

- Classification of Rāśis. Movable, Fixed and Dual are the names given to the 12 Rāśis in order
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Putr and Dharm Bhava are known by the name Kon (or trine)
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father

## 上游问题

- 无

## 停止条件

- 缺少上升星座三分类事实时停止。
- 缺少金星落角宫、月亮落三角宫、月亮与吉星同宫或土星落十宫任一事实时停止。
- 吉星名册未按本书 ch03:v11 取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
