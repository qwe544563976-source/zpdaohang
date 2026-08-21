---
method: ch12-v1-2-lagna-lord-afflicted-felicity-diminish
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 身体安适减少：上升主与凶星同宫，或落八宫、六宫、十二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身体上的舒服程度怎么样
- 上升主落六八十二宫会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）是哪颗行星

## 按情况检查的事实

- 上升主（Lagn's Lord）是否与凶星同宫
- 上升主（Lagn's Lord）是否落八宫（Randhr）
- 上升主（Lagn's Lord）是否落六宫（Ari）
- 上升主（Lagn's Lord）是否落十二宫（Vyaya）

## 依赖方法

- 无

## 执行步骤

### ch12-v1-2-lagna-lord-afflicted-felicity-diminish.step-001

- 动作：先定出上升主是哪颗行星，再核对它是否与凶星同宫，或落在八宫、六宫、十二宫其中之一。
- 适用范围：仅限本命盘一宫（Tanu Bhava）身体安适主题；原文没有给时间限定，也没有限定上升星座。
- 原文最小意思：上升主（Lagn Lord）与凶星同宫，或落八宫（Randhr）、六宫、十二宫时，身体上的安适会减少。
- 本步骤产出事实：["上升主受克的身体安适判定"]
- 所需事实：["本盘上升主（Lagn's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagn's Lord）是否与凶星同宫"}, {"fact_key": "上升主（Lagn's Lord）是否落八宫（Randhr）"}, {"fact_key": "上升主（Lagn's Lord）是否落六宫（Ari）"}, {"fact_key": "上升主（Lagn's Lord）是否落十二宫（Vyaya）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, "required_fact_keys": ["上升主（Lagn's Lord）是否与凶星同宫"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否与凶星同宫"}, "selection_group": "ch12-v1-2-lagna-lord-afflicted-felicity-diminish.step-001:affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否与凶星同宫。"}, {"when": {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落八宫（Randhr）"}, "selection_group": "ch12-v1-2-lagna-lord-afflicted-felicity-diminish.step-001:affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落八宫（Randhr）。"}, {"when": {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落六宫（Ari）"}, "selection_group": "ch12-v1-2-lagna-lord-afflicted-felicity-diminish.step-001:affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落六宫（Ari）。"}, {"when": {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落十二宫（Vyaya）"}, "selection_group": "ch12-v1-2-lagna-lord-afflicted-felicity-diminish.step-001:affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落十二宫（Vyaya）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断具体疾病、部位或发病时间，本句只说安适减少。", "不得把 diminish 读成失去或危及性命。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）是哪颗行星。
- 缺失即停字段：["本盘上升主（Lagn's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v1-2`｜PDF [26]｜“Should Lagn Lord be yuti with a malefic, or be in Randhr, 6<sup>th</sup> , or 12<sup>th</sup> , physical felicity will diminish.”


## 四路查书计划

### 支持路

- Should Lagn Lord be yuti with a malefic, or be in Randhr, 6th, or 12th, physical felicity will diminish
- 上升主与凶星同宫或落八宫六宫十二宫 身体安适减少

### 反例或取消路

- If he is in an angle, or trine there will be at all times comforts of the body
- With a benefic in an angle, or trine all diseases will disappear
- Effects of Lagn’s Lord in Various Bhavas (up to Sloka 12). Should Lagn’s Lord be in Lagn itself, the native will be endowed with physical happiness and prowess

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Putr and Dharm Bhava are known by the name Kon (or trine). Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- Effects of Tanu Bhava
- 判断身体安适要先看上升主落在哪一宫

## 上游问题

- 无

## 停止条件

- 缺少上升主身份事实时停止。
- 四个分支事实全缺时停止。
- 凶星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
