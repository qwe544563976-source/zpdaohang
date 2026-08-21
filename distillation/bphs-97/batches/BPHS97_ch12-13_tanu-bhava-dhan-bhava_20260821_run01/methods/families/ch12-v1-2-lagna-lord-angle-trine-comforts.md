---
method: ch12-v1-2-lagna-lord-angle-trine-comforts
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 身体舒适：上升主落角宫或三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身体一直舒不舒服
- 上升主落角宫三角宫代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）落在哪一宫

## 按情况检查的事实

- 上升主（Lagn's Lord）是否落角宫
- 上升主（Lagn's Lord）是否落三角宫

## 依赖方法

- 无

## 执行步骤

### ch12-v1-2-lagna-lord-angle-trine-comforts.step-001

- 动作：核对上升主落在角宫还是三角宫。
- 适用范围：仅限本命盘一宫（Tanu Bhava）身体舒适主题；本句的 he 承接同偈前句的 Lagn Lord。
- 原文最小意思：上升主（Lagn Lord）落角宫或落三角宫时，随时都有身体上的舒适。
- 本步骤产出事实：["上升主落角宫三角宫的身体舒适判定"]
- 所需事实：["本盘上升主（Lagn's Lord）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落角宫"}, {"fact_key": "上升主（Lagn's Lord）是否落三角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落角宫"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落角宫"}, "selection_group": "ch12-v1-2-lagna-lord-angle-trine-comforts.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落角宫。"}, {"when": {"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落三角宫"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落三角宫"}, "selection_group": "ch12-v1-2-lagna-lord-angle-trine-comforts.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断寿命、财富或疾病，本句只说身体舒适。", "不得把角宫或三角宫换成从上升以外的位置起算，原文本句没有另给起点。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）落在哪一宫。
- 缺失即停字段：["本盘上升主（Lagn's Lord）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v1-2`｜PDF [26]｜“If he is in an angle, or trine there will be at all times comforts of the body.”


## 四路查书计划

### 支持路

- If he is in an angle, or trine there will be at all times comforts of the body
- 上升主落角宫或三角宫 随时有身体舒适

### 反例或取消路

- Should Lagn Lord be yuti with a malefic, or be in Randhr, 6th, or 12th, physical felicity will diminish
- If Lagn Lord is in debilitation, combustion, or enemy’s Rāśi, there will be diseases

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine). Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- Effects of Lagn’s Lord in Various Bhavas (up to Sloka 12). Should Lagn’s Lord be in Lagn itself, the native will be endowed with physical happiness and prowess
- 判断身体舒适要看上升主落角宫还是三角宫

## 上游问题

- 无

## 停止条件

- 缺少上升主落宫事实时停止。
- 角宫与三角宫两个分支事实全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
