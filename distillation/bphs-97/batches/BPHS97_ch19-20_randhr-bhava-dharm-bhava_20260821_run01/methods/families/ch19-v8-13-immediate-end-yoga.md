---
method: ch19-v8-13-immediate-end-yoga
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 立即终结的瑜伽：凶星在角宫或三角宫、吉星在六宫或八宫、上升宫有落陷八宫主

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 凶星落角宫吉星落六宫是什么组合
- 上升宫里有落陷的八宫主意味着什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫主（Randhr's Lord）是否落上升宫（Lagna）
- 八宫主（Randhr's Lord）是否落陷

## 按情况检查的事实

- 角宫是否被凶星占据
- 三角宫是否被凶星占据
- 六宫（Ari）是否被吉星占据
- 八宫（Randhr）是否被吉星占据

## 依赖方法

- 无

## 执行步骤

### ch19-v8-13-immediate-end-yoga.step-001

- 动作：核对上升宫内是否有落陷的八宫主（Randhr's Lord），再核对凶星是否在角宫或三角宫、吉星是否在六宫或八宫。
- 适用范围：仅限本命盘寿命主题；原文未写明角宫、三角宫从哪一宫起算，本方法照原文不作指定；原文未给时间限定。
- 原文最小意思：凶星落角宫或三角宫、吉星落六宫或八宫，同时上升宫内有落陷的八宫主时，此瑜伽会造成立即终结。
- 本步骤产出事实：["凶星角宫吉星六八宫加落陷八宫主的立即终结判定"]
- 所需事实：["八宫主（Randhr's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落陷"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落陷"}]}, {"operator": "OR", "operands": [{"fact_key": "角宫是否被凶星占据"}, {"fact_key": "三角宫是否被凶星占据"}]}, {"operator": "OR", "operands": [{"fact_key": "六宫（Ari）是否被吉星占据"}, {"fact_key": "八宫（Randhr）是否被吉星占据"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落陷"}]}, "required_fact_keys": ["角宫是否被凶星占据"], "branch_condition_logic": {"fact_key": "角宫是否被凶星占据"}, "selection_group": "ch19-v8-13-immediate-end-yoga.step-001:malefic-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：角宫是否被凶星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落陷"}]}, "required_fact_keys": ["三角宫是否被凶星占据"], "branch_condition_logic": {"fact_key": "三角宫是否被凶星占据"}, "selection_group": "ch19-v8-13-immediate-end-yoga.step-001:malefic-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：三角宫是否被凶星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落陷"}]}, "required_fact_keys": ["六宫（Ari）是否被吉星占据"], "branch_condition_logic": {"fact_key": "六宫（Ari）是否被吉星占据"}, "selection_group": "ch19-v8-13-immediate-end-yoga.step-001:benefic-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫（Ari）是否被吉星占据。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落上升宫（Lagna）"}, {"fact_key": "八宫主（Randhr's Lord）是否落陷"}]}, "required_fact_keys": ["八宫（Randhr）是否被吉星占据"], "branch_condition_logic": {"fact_key": "八宫（Randhr）是否被吉星占据"}, "selection_group": "ch19-v8-13-immediate-end-yoga.step-001:benefic-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫（Randhr）是否被吉星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断终结的具体时刻或原因。", "不得把原文的上升宫落陷八宫主这一条前提略去。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否落上升宫（Lagna）、八宫主（Randhr's Lord）是否落陷。
- 缺失即停字段：["八宫主（Randhr's Lord）是否落上升宫（Lagna）", "八宫主（Randhr's Lord）是否落陷"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v8-13`｜PDF [36]｜“Malefics in angles and/or trines and benefics in Ari and/or Randhr Bhava, while Tanu Bhava has in it Randhr’s Lord in fall: this Yoga will cause immediate end.”


## 四路查书计划

### 支持路

- Malefics in angles and/or trines and benefics in Ari and/or Randhr Bhava, while Tanu Bhava has in it Randhr’s Lord in fall: this Yoga will cause immediate end
- 凶星角宫三角宫 吉星六宫八宫 上升宫落陷八宫主 立即终结

### 反例或取消路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon
- a single, but strong Guru in Lagn will ward off all the evils
- One having benefics in Kendras and/or Konas, while malefics are in Sahaj, Ari and Labh Bhava will obtain super-natural life-span

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- The life-span in Bal Risht is 8 years, in Yog Risht 20 years, in short, medium and long lives, respectively, 32, 64 and 120 years

### 判断方法路

- first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas
- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- 角宫三角宫的吉凶星分布怎么看寿命

## 上游问题

- 无

## 停止条件

- 缺少上升宫内八宫主落宫或落陷事实时停止。
- 凶星落角宫、落三角宫两个分支事实都缺时停止。
- 吉星落六宫、落八宫两个分支事实都缺时停止。
- 吉凶星名册未定时停止（判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
