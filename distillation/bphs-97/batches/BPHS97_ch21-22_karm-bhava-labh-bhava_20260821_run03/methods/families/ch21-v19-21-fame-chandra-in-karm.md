---
method: ch21-v19-21-fame-chandra-in-karm
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 享有名声：月亮落十宫、十宫主落十宫起的三角宫、上升主落角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子会不会出名
- 我的名声运怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否落十宫（Karm）
- 十宫主（Karm's Lord）是否落从十宫（Karm）起算的三角宫
- 上升主（Lagn's Lord）是否落角宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v19-21-fame-chandra-in-karm.step-001

- 动作：核对月亮（Chandra）是否落十宫（Karm）、十宫主是否落从十宫起算的三角宫、上升主（Lagn's Lord）是否落上升起算的角宫。
- 适用范围：仅限本命盘十宫（Karm）名声主题；本条是同偈三组名声组合中的第一组，三个条件同时成立才下断语；原文的三角宫明写为从十宫起算，角宫明写为从上升起算；原文未给时间限定。
- 原文最小意思：月亮落十宫、十宫主落从十宫起算的三角宫、上升主落上升起算的角宫时，命主享有名声。
- 本步骤产出事实：["月亮落十宫得名声判定"]
- 所需事实：["月亮（Chandra）是否落十宫（Karm）", "十宫主（Karm's Lord）是否落从十宫（Karm）起算的三角宫", "上升主（Lagn's Lord）是否落角宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落十宫（Karm）"}, {"fact_key": "十宫主（Karm's Lord）是否落从十宫（Karm）起算的三角宫"}, {"fact_key": "上升主（Lagn's Lord）是否落角宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断名声的领域、大小或应期。", "不得把三个条件中的任何一个单独当成有名声的判据。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否落十宫（Karm）、十宫主（Karm's Lord）是否落从十宫（Karm）起算的三角宫、上升主（Lagn's Lord）是否落角宫。
- 缺失即停字段：["月亮（Chandra）是否落十宫（Karm）", "十宫主（Karm's Lord）是否落从十宫（Karm）起算的三角宫", "上升主（Lagn's Lord）是否落角宫"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v19-21`｜PDF [39]｜“One will be endowed with fame, if Chandra is in Karm Bhava, while Karm’s Lord is in a trine from Karm Bhava and Lagn’s Lord is in Lagn’s angle.”


## 四路查书计划

### 支持路

- One will be endowed with fame, if Chandra is in Karm Bhava, while Karm’s Lord is in a trine from Karm Bhava and Lagn’s Lord is in Lagn’s angle
- 月亮落十宫 十宫主落十宫起三角宫 上升主落角宫 名声

### 反例或取消路

- If Shani is in Karm Bhava along with a debilitated Grah, while Karm Bhava in the Navāńś Kundali is occupied by a malefic, the native will be bereft of acts
- Obstructions to the native’s acts will crop up, if Karm’s Lord is in fall, as both Karm Bhava and the 10th from Karm Bhava have malefic occupations

### 适用边界路

- Kendras, Konas etc. defined. O Maitreya, listen to other matters, which I am explaining. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava

### 判断方法路

- Prosperity, or Annihilation of a Bhava. Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic
- 判断名声应检查十宫（Karm）与上升主的哪些位置

## 上游问题

- 无

## 停止条件

- 缺少月亮落宫事实时停止。
- 缺少十宫主是否落从十宫起算的三角宫的事实时停止。
- 缺少上升主是否落角宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
