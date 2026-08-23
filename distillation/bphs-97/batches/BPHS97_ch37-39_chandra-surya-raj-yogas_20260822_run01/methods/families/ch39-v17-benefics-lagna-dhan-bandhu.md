---
method: ch39-v17-benefics-lagna-dhan-bandhu
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升、二宫、四宫皆吉星而三宫有凶星：成为国王或与国王相当

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有当上位者的组合
- 吉星凶星分别落哪些宫才算好

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 本盘中哪些行星被判为凶星
- 上升宫（Lagna）是否被吉星占据
- 二宫（Dhan）是否被吉星占据
- 四宫（Bandhu）是否被吉星占据
- 三宫（Sahaj）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v17-benefics-lagna-dhan-bandhu.step-001

- 动作：取本盘吉星与凶星名册，核对上升宫、二宫、四宫是否都被吉星占据，同时三宫内是否有凶星。
- 适用范围：仅限本命盘；原文本句未给出吉凶星的判准，也没有时间限定。
- 原文最小意思：上升宫（Lagna）、二宫（Dhan）与四宫（Bandhu）都被吉星占据，同时三宫（Sahaj）内有凶星时，命主会成为国王，或与国王相当。
- 本步骤产出事实：["上升二宫四宫吉星三宫凶星的贵格判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "本盘中哪些行星被判为凶星", "上升宫（Lagna）是否被吉星占据", "二宫（Dhan）是否被吉星占据", "四宫（Bandhu）是否被吉星占据", "三宫（Sahaj）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "上升宫（Lagna）是否被吉星占据"}, {"fact_key": "二宫（Dhan）是否被吉星占据"}, {"fact_key": "四宫（Bandhu）是否被吉星占据"}, {"fact_key": "三宫（Sahaj）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文四项条件并列，不得只满足其中几项就下断语。", "不得据此推断登位时间或具体权位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、本盘中哪些行星被判为凶星、上升宫（Lagna）是否被吉星占据、二宫（Dhan）是否被吉星占据、四宫（Bandhu）是否被吉星占据、三宫（Sahaj）是否被凶星占据。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "本盘中哪些行星被判为凶星", "上升宫（Lagna）是否被吉星占据", "二宫（Dhan）是否被吉星占据", "四宫（Bandhu）是否被吉星占据", "三宫（Sahaj）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v17`｜PDF [83]｜“If Lagna, Dhan and Bandhu Bhava are occupied by benefics, while a malefic is in Sahaj Bhava, one will become a king, or equal to a king.”


## 四路查书计划

### 支持路

- If Lagna, Dhan and Bandhu Bhava are occupied by benefics, while a malefic is in Sahaj Bhava, one will become a king, or equal to a king
- 上升二宫四宫吉星 三宫凶星 成为国王

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- If inauspicious Bhavas are occupied by benefics, while auspicious Bhavas are occupied by malefics, the native will be indigent and will be distressed even in the matter of food

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Budh, however, is a malefic, if he joins a malefic
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 缺少吉星或凶星名册事实时停止。
- 四宫位的占据事实缺任一项时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
