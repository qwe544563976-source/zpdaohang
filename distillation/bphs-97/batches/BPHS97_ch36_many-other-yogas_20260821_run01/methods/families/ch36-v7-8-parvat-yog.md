---
method: ch36-v7-8-parvat-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Parvat Yog：角宫内有吉星，且七宫与八宫空无行星或只被吉星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子财富和名声怎么样
- 我有没有当一方领袖的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘角宫（Kendra）是否被吉星占据

## 按情况检查的事实

- 七宫（Yuvati）是否空无行星
- 八宫（Randhr）是否空无行星
- 七宫（Yuvati）是否只被吉星占据
- 八宫（Randhr）是否只被吉星占据

## 依赖方法

- 无

## 执行步骤

### ch36-v7-8-parvat-yog.step-001

- 动作：先核对角宫（Kendras）内是否有吉星，再核对七宫（Yuvati）与八宫（Randhr）是空无行星还是只被吉星占据，判定 Parvat Yog 是否成立。
- 适用范围：仅限本命盘 Parvat Yog 的成立判定；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：角宫（Kendras）内有吉星，且七宫（Yuvati）与八宫（Randhr）空无行星，或只被吉星占据，则 Parvat Yog 成立。
- 本步骤产出事实：["Parvat Yog 成立判定"]
- 所需事实：["本盘角宫（Kendra）是否被吉星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘角宫（Kendra）是否被吉星占据"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "七宫（Yuvati）是否空无行星"}, {"fact_key": "八宫（Randhr）是否空无行星"}]}, {"operator": "AND", "operands": [{"fact_key": "七宫（Yuvati）是否只被吉星占据"}, {"fact_key": "八宫（Randhr）是否只被吉星占据"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘角宫（Kendra）是否被吉星占据"}, "required_fact_keys": ["七宫（Yuvati）是否空无行星", "八宫（Randhr）是否空无行星"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "七宫（Yuvati）是否空无行星"}, {"fact_key": "八宫（Randhr）是否空无行星"}]}, "selection_group": "ch36-v7-8-parvat-yog.step-001:yuvati-randhr-state", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫（Yuvati）是否空无行星、八宫（Randhr）是否空无行星。"}, {"when": {"fact_key": "本盘角宫（Kendra）是否被吉星占据"}, "required_fact_keys": ["七宫（Yuvati）是否只被吉星占据", "八宫（Randhr）是否只被吉星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "七宫（Yuvati）是否只被吉星占据"}, {"fact_key": "八宫（Randhr）是否只被吉星占据"}]}, "selection_group": "ch36-v7-8-parvat-yog.step-001:yuvati-randhr-state", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫（Yuvati）是否只被吉星占据、八宫（Randhr）是否只被吉星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把七宫与八宫的条件放宽成只核对其中一宫。", "原文未说明角宫内需要几颗吉星，不得自行加上数量要求。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘角宫（Kendra）是否被吉星占据。
- 缺失即停字段：["本盘角宫（Kendra）是否被吉星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v7-8`｜PDF [79]｜“Benefics in Kendras will produce Parvat Yog, as Yuvati and Randhr Bhava are vacant, or are occupied by only benefics.”

### ch36-v7-8-parvat-yog.step-002

- 动作：在 Parvat Yog 成立时读取财富、学识与领袖地位的断语。
- 适用范围：仅限已判定 Parvat Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：生于 Parvat Yog 者富有、能言善辩、乐善好施、通晓经论（Shastras）、喜好欢乐、有名声、光彩照人，并会成为一城之领袖。
- 本步骤产出事实：["Parvat Yog 效果断语"]
- 所需事实：["Parvat Yog 成立判定"]
- 条件关系：{"fact_key": "Parvat Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「一城之领袖」升格成国王或某个具体官职。", "不得据此推断寿命、婚姻或子女。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Parvat Yog 成立判定。
- 缺失即停字段：["Parvat Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v7-8`｜PDF [79]｜“One born in Parvat Yog will be wealthy, eloquent, charitable, learned in Shastras, fond of mirth, famous, splendourous and be the leader of a city.”


## 四路查书计划

### 支持路

- Benefics in Kendras will produce Parvat Yog, as Yuvati and Randhr Bhava are vacant
- One born in Parvat Yog will be wealthy, eloquent, charitable, learned in Shastras
- 角宫吉星 七宫八宫空 Parvat Yog

### 反例或取消路

- If inauspicious Bhavas are occupied by benefics, while auspicious Bhavas are occupied by malefics, the native will be indigent
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- 七宫八宫有凶星 破格

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu
- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Benefics, owning Kendras, will not give benefic effects, while malefics, owning Kendras, will not remain inauspicious

### 判断方法路

- Indications of Randhr Bhava
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少角宫吉星占据事实时停止。
- 七宫与八宫的空宫事实与只被吉星占据事实都缺失时停止。
- 原文本句未给出吉星判准，吉星名册未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
