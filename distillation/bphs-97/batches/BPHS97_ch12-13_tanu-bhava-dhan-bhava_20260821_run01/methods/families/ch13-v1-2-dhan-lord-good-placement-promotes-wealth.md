---
method: ch13-v1-2-dhan-lord-good-placement-promotes-wealth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 促进财富：二宫主落二宫、角宫或三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的财运基础怎么样
- 二宫主落哪几宫对钱有利

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘二宫主（Dhan's Lord）是哪颗行星

## 按情况检查的事实

- 二宫主（Dhan's Lord）是否落二宫（Dhan）
- 二宫主（Dhan's Lord）是否落角宫
- 二宫主（Dhan's Lord）是否落三角宫

## 依赖方法

- 无

## 执行步骤

### ch13-v1-2-dhan-lord-good-placement-promotes-wealth.step-001

- 动作：先定出二宫主是哪颗行星，再核对它是否落二宫、角宫或三角宫。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；原文没有给时间限定。
- 原文最小意思：二宫主（Lord of Dhan）落二宫（Dhan）、落角宫或落三角宫时，会促进命主的财富（或经济状况）。
- 本步骤产出事实：["二宫主吉位的财富促进判定"]
- 所需事实：["本盘二宫主（Dhan's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落二宫（Dhan）"}, {"fact_key": "二宫主（Dhan's Lord）是否落角宫"}, {"fact_key": "二宫主（Dhan's Lord）是否落三角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落二宫（Dhan）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落二宫（Dhan）"}, "selection_group": "ch13-v1-2-dhan-lord-good-placement-promotes-wealth.step-001:dhan-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落二宫（Dhan）。"}, {"when": {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落角宫"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落角宫"}, "selection_group": "ch13-v1-2-dhan-lord-good-placement-promotes-wealth.step-001:dhan-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落角宫。"}, {"when": {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落三角宫"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落三角宫"}, "selection_group": "ch13-v1-2-dhan-lord-good-placement-promotes-wealth.step-001:dhan-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财富数额或得财时间，原文只说促进。", "不得把 promote 读成保证富有。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘二宫主（Dhan's Lord）是哪颗行星。
- 缺失即停字段：["本盘二宫主（Dhan's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v1-2`｜PDF [27]｜“If the Lord of Dhan is in Dhan, or is in an angle, or in trine, he will promote one’s wealth (or monetary state).”


## 四路查书计划

### 支持路

- If the Lord of Dhan is in Dhan, or is in an angle, or in trine, he will promote one’s wealth (or monetary state)
- 二宫主落二宫角宫三角宫 促进财富

### 反例或取消路

- Should he be in Ari/8th /12th , financial conditions will decline
- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine). Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava

### 判断方法路

- Effects of Dhan Bhava
- Now I tell you some Yogas for poverty along with conditions of their nullifications
- 判断财运要先看二宫主落在哪一宫

## 上游问题

- 无

## 停止条件

- 缺少二宫主身份事实时停止。
- 三个落宫分支事实全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
