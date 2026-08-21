---
method: ch19-v4-7-ari-vyaya-lords-long-life
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 长寿：六宫主与十二宫主的三种安排

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 六宫主落十二宫我会不会长寿
- 六宫主与十二宫主怎么摆算长寿

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘六宫主（Ari's Lord）落在哪一宫

## 按情况检查的事实

- 六宫主（Ari's Lord）是否落十二宫（Vyaya）
- 六宫主（Ari's Lord）是否落六宫（Ari）
- 十二宫主（Vyaya's Lord）是否落十二宫（Vyaya）
- 六宫主（Ari's Lord）与十二宫主（Vyaya's Lord）是否共同占据上升宫（Lagna）与八宫（Randhr）

## 依赖方法

- 无

## 执行步骤

### ch19-v4-7-ari-vyaya-lords-long-life.step-001

- 动作：核对六宫主（Ari's Lord）与十二宫主（Vyaya's Lord）的落宫，看是否落入原文列出的三种长寿安排之一。
- 适用范围：仅限本命盘寿命主题；原文第三种安排只说六宫主与十二宫主落在上升宫与八宫，没有写明何者落哪一宫（同章 v14-15 要指明对应时会写 respectively），故本方法不作指定；原文未给时间限定。
- 原文最小意思：六宫主落十二宫，或六宫主落六宫而十二宫主落十二宫，或六宫主与十二宫主共同占据上升宫与八宫时，主长寿。
- 本步骤产出事实：["六宫主与十二宫主安排的长寿判定"]
- 所需事实：["本盘六宫主（Ari's Lord）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘六宫主（Ari's Lord）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落十二宫（Vyaya）"}, {"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落六宫（Ari）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落十二宫（Vyaya）"}]}, {"fact_key": "六宫主（Ari's Lord）与十二宫主（Vyaya's Lord）是否共同占据上升宫（Lagna）与八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘六宫主（Ari's Lord）落在哪一宫"}, "required_fact_keys": ["六宫主（Ari's Lord）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "六宫主（Ari's Lord）是否落十二宫（Vyaya）"}, "selection_group": "ch19-v4-7-ari-vyaya-lords-long-life.step-001:ari-vyaya-long-life-yoga", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫主（Ari's Lord）是否落十二宫（Vyaya）。"}, {"when": {"fact_key": "本盘六宫主（Ari's Lord）落在哪一宫"}, "required_fact_keys": ["六宫主（Ari's Lord）是否落六宫（Ari）", "十二宫主（Vyaya's Lord）是否落十二宫（Vyaya）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "六宫主（Ari's Lord）是否落六宫（Ari）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落十二宫（Vyaya）"}]}, "selection_group": "ch19-v4-7-ari-vyaya-lords-long-life.step-001:ari-vyaya-long-life-yoga", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫主（Ari's Lord）是否落六宫（Ari）、十二宫主（Vyaya's Lord）是否落十二宫（Vyaya）。"}, {"when": {"fact_key": "本盘六宫主（Ari's Lord）落在哪一宫"}, "required_fact_keys": ["六宫主（Ari's Lord）与十二宫主（Vyaya's Lord）是否共同占据上升宫（Lagna）与八宫（Randhr）"], "branch_condition_logic": {"fact_key": "六宫主（Ari's Lord）与十二宫主（Vyaya's Lord）是否共同占据上升宫（Lagna）与八宫（Randhr）"}, "selection_group": "ch19-v4-7-ari-vyaya-lords-long-life.step-001:ari-vyaya-long-life-yoga", "stop_condition": "选中该分支后，缺少以下事实即停止：六宫主（Ari's Lord）与十二宫主（Vyaya's Lord）是否共同占据上升宫（Lagna）与八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得指定六宫主与十二宫主各自落上升宫还是八宫——原文没写。", "不得据此推出具体寿数年岁。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘六宫主（Ari's Lord）落在哪一宫。
- 缺失即停字段：["本盘六宫主（Ari's Lord）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v4-7`｜PDF [36]｜“There will be long life, if Ari’s Lord is in Vyaya, or, if Ari’s Lord is in Ari, as Vyaya’s Lord is in Vyaya, or, if Ari’s Lord and Vyaya’s Lord are in Lagn and Randhr.”


## 四路查书计划

### 支持路

- There will be long life, if Ari’s Lord is in Vyaya, or, if Ari’s Lord is in Ari, as Vyaya’s Lord is in Vyaya
- 六宫主落十二宫 十二宫主落十二宫 上升 八宫 长寿

### 反例或取消路

- Malefics in angles and/or trines and benefics in Ari and/or Randhr Bhava, while Tanu Bhava has in it Randhr’s Lord in fall: this Yoga will cause immediate end
- Should Chandra be in Ari, Randhr, or Vyaya Bhava and receives a Drishti from a malefic, the child will die soon
- Good Yogas increase the life-span and bad Yogas decrease the same

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- The life-span in Bal Risht is 8 years, in Yog Risht 20 years, in short, medium and long lives, respectively, 32, 64 and 120 years
- Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead

### 判断方法路

- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- The strength and weakness of the Grahas concerned be estimated in deciding longevity
- 长寿瑜伽要看六宫主与十二宫主的哪几种落宫

## 上游问题

- 无

## 停止条件

- 缺少六宫主落宫事实时停止。
- 三个分支事实都缺时停止。
- 原文未写明第三种安排里两位宫主各落哪一宫，需要指定落宫时停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
