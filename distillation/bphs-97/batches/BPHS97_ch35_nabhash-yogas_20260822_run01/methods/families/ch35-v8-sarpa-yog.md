---
method: ch35-v8-sarpa-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Bhujang（又名 Sarpa）Yog：3 个角宫被凶星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我命里有没有 Sarpa Yog
- 我盘上角宫里的凶星算什么格局

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星
- 本盘是否有3个角宫（Kendra）被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch35-v8-sarpa-yog.step-001

- 动作：核对本盘行星（Grahas）的分布，判定 Sarpa Yog 是否成立。
- 适用范围：仅限本命盘 Bhujang（又名 Sarpa）Yog 的成立判定；原文的 so placed 承接前半句的 3 Kendras，用 respectively 把吉、凶两种结果依次对应 Maal 与 Sarpa，本条只取 Sarpa 这一侧；原文未给凶星判准，也没有时间限定。
- 原文最小意思：本盘有3个角宫（Kendra）被凶星占据时，构成 Bhujang（又名 Sarpa）Yog，这个瑜伽产生凶的结果。
- 本步骤产出事实：["Sarpa Yog 成立判定"]
- 所需事实：["本盘中哪些行星被判为凶星", "本盘是否有3个角宫（Kendra）被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "本盘是否有3个角宫（Kendra）被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 3 个角宫放宽成任意角宫有凶星——原文写的是 3 Kendras。", "不得据 respectively 反推 Maal Yog 的具体结果内容——本条只取 Sarpa Yog 这一侧。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星、本盘是否有3个角宫（Kendra）被凶星占据。
- 缺失即停字段：["本盘中哪些行星被判为凶星", "本盘是否有3个角宫（Kendra）被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v8`｜PDF [76]｜“If 3 Kendras are occupied by benefics, Maal Yog is produced, while malefics so placed will cause Bhujang, or Sarpa Yog.”
  - `bphs-97:santhanam:ch35:v8`｜PDF [76]｜“These Yogas, respectively, produce benefic and malefic results.”


## 四路查书计划

### 支持路

- If 3 Kendras are occupied by benefics, Maal Yog is produced, while malefics so placed will cause Bhujang, or Sarpa Yog.
- These Yogas, respectively, produce benefic and malefic results.
- Sarpa Yog 的成立条件

### 反例或取消路

- If 3 Kendras are occupied by benefics, Maal Yog is produced

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

- 缺少判定 Sarpa Yog 所需的行星分布事实时停止。
- 行星分布事实取不到确定值时停止，不得凭部分行星推定 Sarpa Yog 成立。
- 本盘凶星名册未取得时停止：吉凶归类见第 3 章 Benefics and Malefics 一节。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
