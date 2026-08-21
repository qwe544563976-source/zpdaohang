---
method: ch12-v1-2-lagna-lord-weak-diseases
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 有疾病：上升主落陷、燃烧或落敌星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有病
- 上升主落陷燃烧代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）是哪颗行星

## 按情况检查的事实

- 上升主（Lagn's Lord）是否落陷
- 上升主（Lagn's Lord）是否燃烧
- 上升主（Lagn's Lord）是否落敌星座（enemy's Rāśi）

## 依赖方法

- 无

## 执行步骤

### ch12-v1-2-lagna-lord-weak-diseases.step-001

- 动作：核对上升主是否落陷、是否燃烧、是否落在敌方主管的星座。
- 适用范围：仅限本命盘一宫（Tanu Bhava）疾病主题；原文没有指明是哪一类疾病，也没有给发病时间。
- 原文最小意思：上升主（Lagn Lord）落陷、燃烧，或落敌星座（enemy’s Rāśi）时，会有疾病。
- 本步骤产出事实：["上升主失位的疾病判定"]
- 所需事实：["本盘上升主（Lagn's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落陷"}, {"fact_key": "上升主（Lagn's Lord）是否燃烧"}, {"fact_key": "上升主（Lagn's Lord）是否落敌星座（enemy's Rāśi）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落陷"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落陷"}, "selection_group": "ch12-v1-2-lagna-lord-weak-diseases.step-001:weakness", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落陷。"}, {"when": {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, "required_fact_keys": ["上升主（Lagn's Lord）是否燃烧"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否燃烧"}, "selection_group": "ch12-v1-2-lagna-lord-weak-diseases.step-001:weakness", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否燃烧。"}, {"when": {"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落敌星座（enemy's Rāśi）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落敌星座（enemy's Rāśi）"}, "selection_group": "ch12-v1-2-lagna-lord-weak-diseases.step-001:weakness", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落敌星座（enemy's Rāśi）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得指名具体病症或部位，原文只写 diseases。", "不得把 enemy’s Rāśi 读成本星座或本宫，它指行星所落的敌方星座。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）是哪颗行星。
- 缺失即停字段：["本盘上升主（Lagn's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v1-2`｜PDF [26]｜“If Lagn Lord is in debilitation, combustion, or enemy’s Rāśi, there will be diseases.”


## 四路查书计划

### 支持路

- If Lagn Lord is in debilitation, combustion, or enemy’s Rāśi, there will be diseases
- 上升主落陷 燃烧 敌星座 疾病

### 反例或取消路

- With a benefic in an angle, or trine all diseases will disappear
- Lagn’s angles (i.e. Bandhu, Yuvati, or the 10th), or its trine (Putr, Dharm), containing a benefic, is a powerful remedy for all, related to health

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- O Brahmin, following are the effects, produced by Ari Bhava, relating to diseases, ulcers etc. Listen to this attentively

### 判断方法路

- When Lagn is occupied by the Lords of Ari and Randhr Bhava along with Surya, the native will be afflicted by fever and tumours
- Should Lagn’s Lord be in a Rashiof Mangal, or of Budh and has a Drishti on Budh, there will be diseases of the face
- 判断疾病要看上升主的旺弱与燃烧

## 上游问题

- 无

## 停止条件

- 缺少上升主身份事实时停止。
- 三个分支事实全缺时停止。
- 落陷、燃烧、敌星座的判准未定时停止（强弱判准见第27章 Shad Bal）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
