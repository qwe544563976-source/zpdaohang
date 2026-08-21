---
method: ch20-v13-25-father-died-before-birth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲在命主出生前已去世：太阳落六宫、八宫或十二宫，八宫主落九宫、十二宫主落上升宫、六宫主落五宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲是不是在我出生前就不在了
- 太阳落六宫、八宫或十二宫又几个宫主如此排列说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘太阳（Surya）落在哪一宫
- 八宫主（Randhr's Lord）是否落九宫（Dharm）
- 十二宫主（Vyaya's Lord）是否落上升宫（Lagna）
- 六宫主（Ari's Lord）是否落五宫（Putr）

## 按情况检查的事实

- 太阳（Surya）是否落六宫（Ari）
- 太阳（Surya）是否落八宫（Randhr）
- 太阳（Surya）是否落十二宫（Vyaya）

## 依赖方法

- 无

## 执行步骤

### ch20-v13-25-father-died-before-birth.step-001

- 动作：先取太阳（Surya）落在哪一宫，再核对八宫主（Randhr's Lord）落九宫（Dharm）、十二宫主（Vyaya's Lord）落上升宫（Tanu）、六宫主（Ari's Lord）落五宫（Putr）三项是否同时成立。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文以「Combinations for Father’s Death」立目，末句「Thus the Jyotishis may know the effects」把这组组合交由 Jyotishis 判读；原文未给上升限定。
- 原文最小意思：太阳（Surya）落六宫（Ari）、八宫（Randhr）或十二宫（Vyaya），同时八宫主（Randhr's Lord）落九宫（Dharm）、十二宫主（Vyaya's Lord）落上升宫（Tanu）、六宫主（Ari's Lord）落五宫（Putr）时，命主的父亲在命主出生之前就已去世。
- 本步骤产出事实：["太阳落六宫八宫或十二宫且三个宫主如此排列主父亲出生前去世判定"]
- 所需事实：["本盘太阳（Surya）落在哪一宫", "八宫主（Randhr's Lord）是否落九宫（Dharm）", "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）", "六宫主（Ari's Lord）是否落五宫（Putr）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）落在哪一宫"}, {"fact_key": "八宫主（Randhr's Lord）是否落九宫（Dharm）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"}, {"fact_key": "六宫主（Ari's Lord）是否落五宫（Putr）"}]}, {"operator": "OR", "operands": [{"fact_key": "太阳（Surya）是否落六宫（Ari）"}, {"fact_key": "太阳（Surya）是否落八宫（Randhr）"}, {"fact_key": "太阳（Surya）是否落十二宫（Vyaya）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）落在哪一宫"}, {"fact_key": "八宫主（Randhr's Lord）是否落九宫（Dharm）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"}, {"fact_key": "六宫主（Ari's Lord）是否落五宫（Putr）"}]}, "required_fact_keys": ["太阳（Surya）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否落六宫（Ari）"}, "selection_group": "ch20-v13-25-father-died-before-birth.step-001:surya-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）落在哪一宫"}, {"fact_key": "八宫主（Randhr's Lord）是否落九宫（Dharm）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"}, {"fact_key": "六宫主（Ari's Lord）是否落五宫（Putr）"}]}, "required_fact_keys": ["太阳（Surya）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否落八宫（Randhr）"}, "selection_group": "ch20-v13-25-father-died-before-birth.step-001:surya-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否落八宫（Randhr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘太阳（Surya）落在哪一宫"}, {"fact_key": "八宫主（Randhr's Lord）是否落九宫（Dharm）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）"}, {"fact_key": "六宫主（Ari's Lord）是否落五宫（Putr）"}]}, "required_fact_keys": ["太阳（Surya）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否落十二宫（Vyaya）"}, "selection_group": "ch20-v13-25-father-died-before-birth.step-001:surya-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否落十二宫（Vyaya）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的死因或命主出生前多久去世。", "不得把太阳落其他宫位的情形也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘太阳（Surya）落在哪一宫、八宫主（Randhr's Lord）是否落九宫（Dharm）、十二宫主（Vyaya's Lord）是否落上升宫（Lagna）、六宫主（Ari's Lord）是否落五宫（Putr）。
- 缺失即停字段：["本盘太阳（Surya）落在哪一宫", "八宫主（Randhr's Lord）是否落九宫（Dharm）", "十二宫主（Vyaya's Lord）是否落上升宫（Lagna）", "六宫主（Ari's Lord）是否落五宫（Putr）"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v13-25`｜PDF [37]｜“The father of the native would have passed away prior to the native’s birth, if Surya is in Ari, Randhr, or Vyaya Bhava, as Randhr’s Lord is in Dharm Bhava, Vyaya’s Lord is in Tanu Bhava and Ari’s Lord is in Putr Bhava.”


## 四路查书计划

### 支持路

- The father of the native would have passed away prior to the native’s birth, if Surya is in Ari, Randhr, or Vyaya Bhava, as Randhr’s Lord is in Dharm Bhava, Vyaya’s Lord is in Tanu Bhava and Ari’s Lord is in Putr Bhava.
- 太阳落六宫 八宫 十二宫 八宫主落九宫 十二宫主落上升宫 六宫主落五宫 父亲出生前去世

### 反例或取消路

- Long-living Father. Should Dharm’s Lord be in deep exaltation, while Shukra is in an angle from Tanu Bhava and Guru is in the 9<sup>th</sup> from Navāńś Lagna, the father of the native will enjoy a long span of life
- If Dharm’s Lord is an angle and receives a Drishti from Guru, the native’s father will be a king endowed with conveyances, or be equal to a king

### 适用边界路

- If Surya receives a Drishti from Shani and be in Mesh, or in Vrischik Navāńś, the father would have given up the family before birth of the child, or would have passed away
- Should Dhan Bhava be occupied by Rahu, Budh, Shukr, Surya and Shani, the child’s birth has been after its father’s death
- The 9<sup>th</sup> from Surya denotes father

### 判断方法路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- 判断父亲存亡要看太阳（Surya）与九宫（Dharm）的哪些配置

## 上游问题

- 无

## 停止条件

- 缺少太阳（Surya）落宫事实时停止。
- 缺少八宫主、十二宫主或六宫主任何一项落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
