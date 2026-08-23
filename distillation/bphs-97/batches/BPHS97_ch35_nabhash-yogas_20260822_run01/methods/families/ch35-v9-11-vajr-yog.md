---
method: ch35-v9-11-vajr-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Vajr Yog：吉星全在上升与七宫，或凶星全在四宫与十宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我命里有没有 Vajr Yog
- 我盘上吉星凶星分别挤在哪几个角宫

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 本盘中哪些行星被判为凶星

## 按情况检查的事实

- 本盘所有吉星是否都落在上升宫（Lagn）与七宫（Yuvati Bhava）内
- 本盘所有凶星是否都落在四宫（Bandhu）与十宫（Karm Bhava）内

## 依赖方法

- 无

## 执行步骤

### ch35-v9-11-vajr-yog.step-001

- 动作：核对本盘行星（Grahas）的分布，判定 Vajr Yog 是否成立。
- 适用范围：仅限本命盘 Vajr Yog 的成立判定；原文只给盘面分布条件，没有时间、上升或男女限定。
- 原文最小意思：本盘所有吉星都落在上升宫（Lagn）与七宫（Yuvati Bhava）内，或所有凶星都落在四宫（Bandhu）与十宫（Karm Bhava）内时，构成 Vajr Yog。
- 本步骤产出事实：["Vajr Yog 成立判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "本盘中哪些行星被判为凶星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "本盘中哪些行星被判为凶星"}]}, {"operator": "OR", "operands": [{"fact_key": "本盘所有吉星是否都落在上升宫（Lagn）与七宫（Yuvati Bhava）内"}, {"fact_key": "本盘所有凶星是否都落在四宫（Bandhu）与十宫（Karm Bhava）内"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "本盘中哪些行星被判为凶星"}]}, "required_fact_keys": ["本盘所有吉星是否都落在上升宫（Lagn）与七宫（Yuvati Bhava）内"], "branch_condition_logic": {"fact_key": "本盘所有吉星是否都落在上升宫（Lagn）与七宫（Yuvati Bhava）内"}, "selection_group": "ch35-v9-11-vajr-yog.step-001:vajr-sides", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘所有吉星是否都落在上升宫（Lagn）与七宫（Yuvati Bhava）内。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "本盘中哪些行星被判为凶星"}]}, "required_fact_keys": ["本盘所有凶星是否都落在四宫（Bandhu）与十宫（Karm Bhava）内"], "branch_condition_logic": {"fact_key": "本盘所有凶星是否都落在四宫（Bandhu）与十宫（Karm Bhava）内"}, "selection_group": "ch35-v9-11-vajr-yog.step-001:vajr-sides", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘所有凶星是否都落在四宫（Bandhu）与十宫（Karm Bhava）内。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["吉星一侧与凶星一侧是原文并列的两种成立方式，不得要求两者同时满足。", "不得把吉星侧的宫位与凶星侧的宫位对调——对调后原文写的是 Yav Yog。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、本盘中哪些行星被判为凶星。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "本盘中哪些行星被判为凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v9-11`｜PDF [76]｜“Vajr Yog is caused by all benefics in Lagn and Yuvati Bhava, or all malefics in Bandhu and Karm Bhava.”


## 四路查书计划

### 支持路

- Vajr Yog is caused by all benefics in Lagn and Yuvati Bhava, or all malefics in Bandhu and Karm Bhava.
- Vajr Yog 的成立条件

### 反例或取消路

- In a contrary situation, i.e. all benefics in Bandhu and Karm Bhava, or all malefics in Lagn and Yuvati Bhava, Yav Yog is generated.

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu
- O excellent of the Brahmins, explained below are 32 Nabhash Yogas, which have a total of 1800 different varieties.
- These consist of 3 Asraya Yogas, 2 Dala Yogas, 20 Akriti Yogas and 7 Sankhya Yogas.
- Nabhash 瑜伽全章的总数与分类边界

### 判断方法路

- Names of Nabhash Yogas. The 3 Asraya Yogas are Rajju, Musala and Nala Yogas.
- Effects of Nabhash Yogas (up to Sloka 50).
- 怎么按 Nabhash 瑜伽的分类去查一张盘

## 上游问题

- 无

## 停止条件

- 缺少判定 Vajr Yog 所需的行星分布事实时停止。
- 行星分布事实取不到确定值时停止，不得凭部分行星推定 Vajr Yog 成立。
- 本盘吉星与凶星名册未取得时停止：吉凶归类见第 3 章 Benefics and Malefics 一节。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
