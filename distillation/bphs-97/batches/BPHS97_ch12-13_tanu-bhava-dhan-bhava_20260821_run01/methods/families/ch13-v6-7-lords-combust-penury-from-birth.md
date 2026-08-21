---
method: ch13-v6-7-lords-combust-penury-from-birth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 自幼贫困行乞：二宫主与十一宫主都燃烧或都与凶星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我是不是从小就穷
- 二宫主十一宫主受克会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘二宫主（Dhan's Lord）是哪颗行星
- 本盘十一宫主（Labh's Lord）是哪颗行星

## 按情况检查的事实

- 二宫主（Dhan's Lord）是否燃烧
- 十一宫主（Labh's Lord）是否燃烧
- 二宫主（Dhan's Lord）是否与凶星同宫
- 十一宫主（Labh's Lord）是否与凶星同宫

## 依赖方法

- 无

## 执行步骤

### ch13-v6-7-lords-combust-penury-from-birth.step-001

- 动作：先确定二宫主与十一宫主是哪两颗行星，再核对两者是否都燃烧，或都与凶星同宫。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；原文两个条件都要求两个宫主同时成立，不是任一宫主成立即可。
- 原文最小意思：二宫主与十一宫主都燃烧，或都与凶星同宫时，命主自出生起即贫困，甚至要乞讨食物。
- 本步骤产出事实：["二宫主与十一宫主受克的自幼贫困判定"]
- 所需事实：["本盘二宫主（Dhan's Lord）是哪颗行星", "本盘十一宫主（Labh's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}]}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否燃烧"}, {"fact_key": "十一宫主（Labh's Lord）是否燃烧"}]}, {"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否与凶星同宫"}, {"fact_key": "十一宫主（Labh's Lord）是否与凶星同宫"}]}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}]}, "required_fact_keys": ["二宫主（Dhan's Lord）是否燃烧", "十一宫主（Labh's Lord）是否燃烧"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否燃烧"}, {"fact_key": "十一宫主（Labh's Lord）是否燃烧"}]}, "selection_group": "ch13-v6-7-lords-combust-penury-from-birth.step-001:both-lords-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否燃烧、十一宫主（Labh's Lord）是否燃烧。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）是哪颗行星"}, {"fact_key": "本盘十一宫主（Labh's Lord）是哪颗行星"}]}, "required_fact_keys": ["二宫主（Dhan's Lord）是否与凶星同宫", "十一宫主（Labh's Lord）是否与凶星同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否与凶星同宫"}, {"fact_key": "十一宫主（Labh's Lord）是否与凶星同宫"}]}, "selection_group": "ch13-v6-7-lords-combust-penury-from-birth.step-001:both-lords-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否与凶星同宫、十一宫主（Labh's Lord）是否与凶星同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「两个宫主都燃烧」减成只有一个宫主燃烧。", "不得据此推断贫困持续多久或何时结束。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘二宫主（Dhan's Lord）是哪颗行星、本盘十一宫主（Labh's Lord）是哪颗行星。
- 缺失即停字段：["本盘二宫主（Dhan's Lord）是哪颗行星", "本盘十一宫主（Labh's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v6-7`｜PDF [28]｜“There will be penury right from birth and the native will have to beg even for his food, if the Lords of Dhan and Labh Bhava are both combust, or with malefics.”


## 四路查书计划

### 支持路

- There will be penury right from birth and the native will have to beg even for his food, if the Lords of Dhan and Labh Bhava are both combust, or with malefics
- 二宫主 十一宫主 燃烧 与凶星同宫 自幼贫困 乞讨

### 反例或取消路

- If Dhan Lord is in Labh, while the Lord of Labh in Dhan, wealth will be acquired by the native
- One will be wealthy, if Guru is in Dhan, as the Lord of Dhan, or is with Mangal
- Surya in Dhan Bhava, receiving a Drishti from Shani, will cause penury, while, if Surya is in Dhan Bhava and does not receive a Drishti from Shani, riches and fame will be obtained

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- Note the Grahas, that are ruling the Rāśis, occupied by the Lords of Ari, Randhr and Vyaya Bhava. If the said dispositors are in such evil Bhavas in turn and are associated with, or receive a Drishti from malefics, the native will be miserable and indigent

### 判断方法路

- Now I tell you some Yogas for poverty along with conditions of their nullifications
- If inauspicious Bhavas are occupied by benefics, while auspicious Bhavas are occupied by malefics, the native will be indigent and will be distressed even in the matter of food
- 判断贫困要看二宫主与十一宫主是否燃烧或与凶星同宫

## 上游问题

- 无

## 停止条件

- 缺少二宫主、十一宫主的行星身份事实时停止。
- 燃烧与凶星同宫两个分支事实都缺时停止。
- 凶星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
