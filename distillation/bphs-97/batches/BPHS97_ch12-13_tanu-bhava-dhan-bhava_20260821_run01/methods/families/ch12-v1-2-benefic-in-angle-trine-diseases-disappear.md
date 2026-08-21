---
method: ch12-v1-2-benefic-in-angle-trine-diseases-disappear
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 疾病消失：吉星落角宫或三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的病会不会好
- 吉星落角宫三角宫有什么用

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 角宫（Kendr）是否被吉星占据
- 三角宫（Kon）是否被吉星占据

## 依赖方法

- 无

## 执行步骤

### ch12-v1-2-benefic-in-angle-trine-diseases-disappear.step-001

- 动作：核对角宫或三角宫里是否有吉星。
- 适用范围：仅限本命盘一宫（Tanu Bhava）疾病主题；本句没有说所指的是哪一种病，也没有给时间。
- 原文最小意思：有吉星落角宫，或有吉星落三角宫时，所有疾病都会消失。
- 本步骤产出事实：["角宫三角宫吉星的疾病消失判定"]
- 所需事实：["本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"operator": "OR", "operands": [{"fact_key": "角宫（Kendr）是否被吉星占据"}, {"fact_key": "三角宫（Kon）是否被吉星占据"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["角宫（Kendr）是否被吉星占据"], "branch_condition_logic": {"fact_key": "角宫（Kendr）是否被吉星占据"}, "selection_group": "ch12-v1-2-benefic-in-angle-trine-diseases-disappear.step-001:benefic-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：角宫（Kendr）是否被吉星占据。"}, {"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["三角宫（Kon）是否被吉星占据"], "branch_condition_logic": {"fact_key": "三角宫（Kon）是否被吉星占据"}, "selection_group": "ch12-v1-2-benefic-in-angle-trine-diseases-disappear.step-001:benefic-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：三角宫（Kon）是否被吉星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此断出病愈的时间或需要几颗吉星，原文都没有写。", "不得把这条当成对任何一条凶象的通用化解，本句只针对疾病。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v1-2`｜PDF [26]｜“With a benefic in an angle, or trine all diseases will disappear.”


## 四路查书计划

### 支持路

- With a benefic in an angle, or trine all diseases will disappear
- 吉星落角宫或三角宫 所有疾病消失

### 反例或取消路

- If Lagn Lord is in debilitation, combustion, or enemy’s Rāśi, there will be diseases
- When Lagn is occupied by the Lords of Ari and Randhr Bhava along with Surya, the native will be afflicted by fever and tumours

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine). Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava

### 判断方法路

- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- If 3 Kendras are occupied by benefics, Maal Yog is produced, while malefics so placed will cause Bhujang, or Sarpa Yog
- 判断疾病能否消退要看角宫三角宫有没有吉星

## 上游问题

- 无

## 停止条件

- 缺少吉星名册事实时停止。
- 角宫与三角宫两个分支事实全缺时停止。
- 吉星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
