---
method: ch09-v16-malefics-in-vyaya-ari-or-randhr-dhan-with-lagna-hemmed
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶星落十二宫与六宫、或落八宫与二宫，且上升被凶星夹：早亡

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 凶星落十二宫六宫会怎样
- 上升被凶星夹有什么后果
- 早亡的宫位组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升（Lagn）是否被其他凶星夹（hemmed between malefics）

## 按情况检查的事实

- 十二宫（Vyaya Bhava）是否被凶星占据
- 六宫（Ari Bhava）是否被凶星占据
- 八宫（Randhr Bhava）是否被凶星占据
- 二宫（Dhan Bhava）是否被凶星占据

## 依赖方法

- 无

## 执行步骤

### ch09-v16-malefics-in-vyaya-ari-or-randhr-dhan-with-lagna-hemmed.step-001

- 动作：核对凶星是否落在十二宫与六宫、或八宫与二宫，并核对上升是否被其他凶星夹。
- 适用范围：仅限本命盘出生时的凶象；原文给出两组落宫，任一组成立即可。
- 原文最小意思：凶星落十二宫（Vyaya）与六宫（Ari Bhava）、或落八宫（Randhr）与二宫（Dhan Bhava），同时上升（Lagn）被其他凶星夹时，会带来早亡。
- 本步骤产出事实：["凶星双宫兼上升被夹的早亡判定"]
- 所需事实：["上升（Lagn）是否被其他凶星夹（hemmed between malefics）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升（Lagn）是否被其他凶星夹（hemmed between malefics）"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "十二宫（Vyaya Bhava）是否被凶星占据"}, {"fact_key": "六宫（Ari Bhava）是否被凶星占据"}]}, {"operator": "AND", "operands": [{"fact_key": "八宫（Randhr Bhava）是否被凶星占据"}, {"fact_key": "二宫（Dhan Bhava）是否被凶星占据"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "上升（Lagn）是否被其他凶星夹（hemmed between malefics）"}, "required_fact_keys": ["十二宫（Vyaya Bhava）是否被凶星占据", "六宫（Ari Bhava）是否被凶星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十二宫（Vyaya Bhava）是否被凶星占据"}, {"fact_key": "六宫（Ari Bhava）是否被凶星占据"}]}, "selection_group": "ch09-v16-malefics-in-vyaya-ari-or-randhr-dhan-with-lagna-hemmed.step-001:malefic-bhava-pair", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫（Vyaya Bhava）是否被凶星占据、六宫（Ari Bhava）是否被凶星占据。"}, {"when": {"fact_key": "上升（Lagn）是否被其他凶星夹（hemmed between malefics）"}, "required_fact_keys": ["八宫（Randhr Bhava）是否被凶星占据", "二宫（Dhan Bhava）是否被凶星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "八宫（Randhr Bhava）是否被凶星占据"}, {"fact_key": "二宫（Dhan Bhava）是否被凶星占据"}]}, "selection_group": "ch09-v16-malefics-in-vyaya-ari-or-randhr-dhan-with-lagna-hemmed.step-001:malefic-bhava-pair", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫（Randhr Bhava）是否被凶星占据、二宫（Dhan Bhava）是否被凶星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把两组落宫混搭成原文没写的第三组。", "不得把『早亡』补成具体年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升（Lagn）是否被其他凶星夹（hemmed between malefics）。
- 缺失即停字段：["上升（Lagn）是否被其他凶星夹（hemmed between malefics）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v16`｜PDF [23]｜“Malefic in Vyaya and Ari Bhava, or in Randhr and Dhan Bhava, while Lagn is hemmed between other malefics, will bring early death.”


## 四路查书计划

### 支持路

- Malefic in Vyaya and Ari Bhava, or in Randhr and Dhan Bhava, while Lagn is hemmed between other malefics, will bring early death
- 凶星 十二宫六宫 八宫二宫 上升被夹 早亡

### 反例或取消路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- Short-life Combinations (up to Sloka 23)

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- 上升被夹怎么看

## 上游问题

- 无

## 停止条件

- 缺少各宫凶星占据事实时停止。
- 缺少上升是否被凶星夹的事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
