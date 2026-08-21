---
method: ch21-v3-rahu-angle-trine-sacrifices
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 举行宗教祭祀：罗睺落角宫或三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会做祭祀、法事这类宗教活动
- 罗睺落角宫三角宫是什么效果

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘罗睺（Rahu）落在哪一宫

## 按情况检查的事实

- 罗睺（Rahu）是否落角宫
- 罗睺（Rahu）是否落三角宫

## 依赖方法

- 无

## 执行步骤

### ch21-v3-rahu-angle-trine-sacrifices.step-001

- 动作：取罗睺（Rahu）所落的宫，核对它是否落角宫或三角宫。
- 适用范围：仅限原文这一句给出的罗睺落角宫或三角宫与举行宗教祭祀；原文未给上升、时间限定，也没有列出角宫与三角宫的具体宫位。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：罗睺落角宫或落三角宫时，命主会举行像 Jyotishtoma 那样的宗教祭祀。
- 本步骤产出事实：["罗睺落角宫三角宫的宗教祭祀判定"]
- 所需事实：["本盘罗睺（Rahu）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘罗睺（Rahu）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "罗睺（Rahu）是否落角宫"}, {"fact_key": "罗睺（Rahu）是否落三角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘罗睺（Rahu）落在哪一宫"}, "required_fact_keys": ["罗睺（Rahu）是否落角宫"], "branch_condition_logic": {"fact_key": "罗睺（Rahu）是否落角宫"}, "selection_group": "ch21-v3-rahu-angle-trine-sacrifices.step-001:rahu-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：罗睺（Rahu）是否落角宫。"}, {"when": {"fact_key": "本盘罗睺（Rahu）落在哪一宫"}, "required_fact_keys": ["罗睺（Rahu）是否落三角宫"], "branch_condition_logic": {"fact_key": "罗睺（Rahu）是否落三角宫"}, "selection_group": "ch21-v3-rahu-angle-trine-sacrifices.step-001:rahu-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：罗睺（Rahu）是否落三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断祭祀的次数、时间或宗教身份。", "不得把 Jyotishtoma 之外的具体仪式写成原文断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘罗睺（Rahu）落在哪一宫。
- 缺失即停字段：["本盘罗睺（Rahu）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v3`｜PDF [38]｜“If Rahu is in an angle, or in a trine, he will perform religious sacrifices, like Jyotishtoma.”


## 四路查书计划

### 支持路

- If Rahu is in an angle, or in a trine, he will perform religious sacrifices, like Jyotishtoma
- 罗睺 角宫 三角宫 宗教祭祀 Jyotishtoma

### 反例或取消路

- Should Rahu, Surya, Shani and Mangal be in Labh Bhava, the native will incur cessation of his duties
- If the Lord of Karm Bhava is relegated to Randhr Bhava along with Rahu, the native will hate others
- 罗睺 凶星 职务中断 坏事

### 适用边界路

- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine)
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Now I tell you about the effects of nonluminous Grahas
- 判断罗睺（Rahu）落角宫或三角宫要查什么

## 上游问题

- 无

## 停止条件

- 缺少罗睺落宫事实时停止。
- 角宫与三角宫的宫位界定未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
