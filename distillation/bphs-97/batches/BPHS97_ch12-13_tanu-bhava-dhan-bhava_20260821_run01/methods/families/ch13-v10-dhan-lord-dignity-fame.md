---
method: ch13-v10-dhan-lord-dignity-fame
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 照顾族人并成名：二宫主落本星座或入旺

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会出名
- 二宫主入旺或落本星座代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘二宫主（Dhan's Lord）是哪颗行星

## 按情况检查的事实

- 二宫主（Dhan's Lord）是否落本星座（own Rāśi）
- 二宫主（Dhan's Lord）是否入旺

## 依赖方法

- 无

## 执行步骤

### ch13-v10-dhan-lord-dignity-fame.step-001

- 动作：先确定二宫主是哪颗行星，再核对它是否落本星座（own Rāśi），或是否入旺。
- 适用范围：仅限本命盘二宫（Dhan Bhava）主题；原文未给时间限定，也未说明成名的领域。
- 原文最小意思：二宫主（Dhan’s Lord）落本星座（own Rāśi），或入旺时，命主照顾自己的人、帮助他人，并且成名。
- 本步骤产出事实：["二宫主得位的名声判定"]
- 所需事实：["本盘二宫主（Dhan's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落本星座（own Rāśi）"}, {"fact_key": "二宫主（Dhan's Lord）是否入旺"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落本星座（own Rāśi）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落本星座（own Rāśi）"}, "selection_group": "ch13-v10-dhan-lord-dignity-fame.step-001:dhan-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落本星座（own Rāśi）。"}, {"when": {"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否入旺"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否入旺"}, "selection_group": "ch13-v10-dhan-lord-dignity-fame.step-001:dhan-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 own Rāśi（本星座）当成本宫（Bhava）来判。", "不得据此推断名声的领域、范围或成名时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘二宫主（Dhan's Lord）是哪颗行星。
- 缺失即停字段：["本盘二宫主（Dhan's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v10`｜PDF [28]｜“If Dhan’s Lord is in own Rāśi, or is exalted, the native will look after his people, will help others and also will become famous.”


## 四路查书计划

### 支持路

- If Dhan’s Lord is in own Rāśi, or is exalted, the native will look after his people, will help others and also will become famous
- 二宫主落本星座 入旺 照顾族人 成名

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed
- If Dhan Bhava and its Lord are yuti with malefics, the native will be a talebearer, will speak untruth
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless

### 适用边界路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- If the Lord of Dhan is in Dhan, or is in an angle, or in trine, he will promote one’s wealth (or monetary state)
- The native will be wealthy, if one among Chandra, Guru, Shukra and Budh is exalted in Dhan Bhava

### 判断方法路

- If Dhan’s Lord is in Dhan Bhava, the native will be wealthy, proud, will have two, or more wives and be bereft of progeny
- If Dhan’s Lord is in Putr Bhava, the native will be wealthy
- 判断名声要看二宫主的庙旺状态

## 上游问题

- 无

## 停止条件

- 缺少二宫主行星身份事实时停止。
- 落本星座与入旺两个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
