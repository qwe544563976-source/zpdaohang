---
method: ch19-v4-7-four-grahas-angle-trine-labh-long-life
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 长寿：上升主、八宫主、十宫主与土星各落角宫、三角宫或十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 上升主八宫主十宫主土星都落得好我会长寿吗
- 土星落角宫对寿命有没有帮助

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）落在哪一宫
- 本盘八宫主（Randhr's Lord）落在哪一宫
- 本盘十宫主（Karm's Lord）落在哪一宫
- 本盘土星（Shani）落在哪一宫

## 按情况检查的事实

- 上升主（Lagn's Lord）是否落角宫
- 上升主（Lagn's Lord）是否落三角宫
- 上升主（Lagn's Lord）是否落十一宫（Labh）
- 八宫主（Randhr's Lord）是否落角宫
- 八宫主（Randhr's Lord）是否落三角宫
- 八宫主（Randhr's Lord）是否落十一宫（Labh）
- 十宫主（Karm's Lord）是否落角宫
- 十宫主（Karm's Lord）是否落三角宫
- 十宫主（Karm's Lord）是否落十一宫（Labh）
- 土星（Shani）是否落角宫
- 土星（Shani）是否落三角宫
- 土星（Shani）是否落十一宫（Labh）

## 依赖方法

- 无

## 执行步骤

### ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001

- 动作：逐一核对上升主（Lagn's Lord）、八宫主（Randhr's Lord）、十宫主（Karm's Lord）与土星（Shani）是否各自落角宫、三角宫或十一宫（Labh）。
- 适用范围：仅限本命盘寿命主题；原文 severally 指四者各自落入这三处之一，未指定何者落何处；原文未写明角宫、三角宫从哪一宫起算，本方法照原文不作指定；原文未给时间限定。
- 原文最小意思：上升主、八宫主、十宫主与土星各自落角宫、三角宫或十一宫时，命主长寿。
- 本步骤产出事实：["四星各落角宫三角宫或十一宫的长寿判定"]
- 所需事实：["本盘上升主（Lagn's Lord）落在哪一宫", "本盘八宫主（Randhr's Lord）落在哪一宫", "本盘十宫主（Karm's Lord）落在哪一宫", "本盘土星（Shani）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落角宫"}, {"fact_key": "上升主（Lagn's Lord）是否落三角宫"}, {"fact_key": "上升主（Lagn's Lord）是否落十一宫（Labh）"}]}, {"operator": "OR", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落角宫"}, {"fact_key": "八宫主（Randhr's Lord）是否落三角宫"}, {"fact_key": "八宫主（Randhr's Lord）是否落十一宫（Labh）"}]}, {"operator": "OR", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落角宫"}, {"fact_key": "十宫主（Karm's Lord）是否落三角宫"}, {"fact_key": "十宫主（Karm's Lord）是否落十一宫（Labh）"}]}, {"operator": "OR", "operands": [{"fact_key": "土星（Shani）是否落角宫"}, {"fact_key": "土星（Shani）是否落三角宫"}, {"fact_key": "土星（Shani）是否落十一宫（Labh）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否落角宫"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落角宫"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:lagn-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否落三角宫"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落三角宫"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:lagn-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落三角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["上升主（Lagn's Lord）是否落十一宫（Labh）"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落十一宫（Labh）"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:lagn-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落十一宫（Labh）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["八宫主（Randhr's Lord）是否落角宫"], "branch_condition_logic": {"fact_key": "八宫主（Randhr's Lord）是否落角宫"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:randhr-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）是否落角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["八宫主（Randhr's Lord）是否落三角宫"], "branch_condition_logic": {"fact_key": "八宫主（Randhr's Lord）是否落三角宫"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:randhr-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）是否落三角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["八宫主（Randhr's Lord）是否落十一宫（Labh）"], "branch_condition_logic": {"fact_key": "八宫主（Randhr's Lord）是否落十一宫（Labh）"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:randhr-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：八宫主（Randhr's Lord）是否落十一宫（Labh）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否落角宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否落角宫"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:karm-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否落角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否落三角宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否落三角宫"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:karm-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否落三角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否落十一宫（Labh）"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否落十一宫（Labh）"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:karm-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否落十一宫（Labh）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["土星（Shani）是否落角宫"], "branch_condition_logic": {"fact_key": "土星（Shani）是否落角宫"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:shani-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：土星（Shani）是否落角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["土星（Shani）是否落三角宫"], "branch_condition_logic": {"fact_key": "土星（Shani）是否落三角宫"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:shani-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：土星（Shani）是否落三角宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）落在哪一宫"}, {"fact_key": "本盘八宫主（Randhr's Lord）落在哪一宫"}, {"fact_key": "本盘十宫主（Karm's Lord）落在哪一宫"}, {"fact_key": "本盘土星（Shani）落在哪一宫"}]}, "required_fact_keys": ["土星（Shani）是否落十一宫（Labh）"], "branch_condition_logic": {"fact_key": "土星（Shani）是否落十一宫（Labh）"}, "selection_group": "ch19-v4-7-four-grahas-angle-trine-labh-long-life.step-001:shani-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：土星（Shani）是否落十一宫（Labh）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得指定四者中谁必须落角宫、谁必须落三角宫——原文只说各自落其一。", "不得据此推出具体寿数年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）落在哪一宫、本盘八宫主（Randhr's Lord）落在哪一宫、本盘十宫主（Karm's Lord）落在哪一宫、本盘土星（Shani）落在哪一宫。
- 缺失即停字段：["本盘上升主（Lagn's Lord）落在哪一宫", "本盘八宫主（Randhr's Lord）落在哪一宫", "本盘十宫主（Karm's Lord）落在哪一宫", "本盘土星（Shani）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v4-7`｜PDF [36]｜“Should the Lords of Lagna, Randhr and Karm Bhava and Shani are all disposed severally in an angle, in a trine, or in Labh Bhava, the subject will live long.”


## 四路查书计划

### 支持路

- Should the Lords of Lagna, Randhr and Karm Bhava and Shani are all disposed severally in an angle, in a trine, or in Labh Bhava, the subject will live long
- 上升主 八宫主 十宫主 土星 角宫 三角宫 十一宫 长寿

### 反例或取消路

- Malefics in angles and/or trines and benefics in Ari and/or Randhr Bhava, while Tanu Bhava has in it Randhr’s Lord in fall: this Yoga will cause immediate end
- Should Shani be a contributor, the class of longevity declines

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- The life-span in Bal Risht is 8 years, in Yog Risht 20 years, in short, medium and long lives, respectively, 32, 64 and 120 years
- One having benefics in Kendras and/or Konas, while malefics are in Sahaj, Ari and Labh Bhava will obtain super-natural life-span

### 判断方法路

- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- Similarly consider Shani and Karm’s Lord in the matter of longevity
- 寿命判断里角宫三角宫十一宫各起什么作用

## 上游问题

- 无

## 停止条件

- 缺少上升主、八宫主、十宫主或土星的落宫事实时停止。
- 四者中任何一位的三个落宫分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
