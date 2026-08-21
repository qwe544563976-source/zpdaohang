---
method: ch22-v3-labh-lord-in-dhan-great-gains
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 收获甚大：十一宫主落二宫、二宫主落角宫并与木星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子的进项大不大
- 我的收获能不能很大

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十一宫主（Labh's Lord）是否落二宫（Dhan）
- 二宫主（Dhan's Lord）是否落角宫
- 二宫主（Dhan's Lord）是否与木星（Guru）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch22-v3-labh-lord-in-dhan-great-gains.step-001

- 动作：核对十一宫主（Labh's Lord）是否落二宫（Dhan），同时核对二宫主（Dhan's Lord）是否落角宫并与木星（Guru）同宫。
- 适用范围：仅限本命盘十一宫（Labh）收获主题；原文三个条件是并列前提，须同时成立；原文未给收获数额与应期。
- 原文最小意思：十一宫主落二宫、二宫主落角宫并与木星同宫时，收获甚大。
- 本步骤产出事实：["十一宫主落二宫收获甚大判定"]
- 所需事实：["十一宫主（Labh's Lord）是否落二宫（Dhan）", "二宫主（Dhan's Lord）是否落角宫", "二宫主（Dhan's Lord）是否与木星（Guru）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落二宫（Dhan）"}, {"fact_key": "二宫主（Dhan's Lord）是否落角宫"}, {"fact_key": "二宫主（Dhan's Lord）是否与木星（Guru）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断收获的数额、来源或应期。", "不得把「落角宫」与「与木星同宫」拆成任选其一：原文两者并列。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十一宫主（Labh's Lord）是否落二宫（Dhan）、二宫主（Dhan's Lord）是否落角宫、二宫主（Dhan's Lord）是否与木星（Guru）同宫。
- 缺失即停字段：["十一宫主（Labh's Lord）是否落二宫（Dhan）", "二宫主（Dhan's Lord）是否落角宫", "二宫主（Dhan's Lord）是否与木星（Guru）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch22:v3`｜PDF [39]｜“If Labh’s Lord is in Dhan Bhava, while Dhan’s Lord is in an angle along with Guru, the gains will be great.”


## 四路查书计划

### 支持路

- If Labh’s Lord is in Dhan Bhava, while Dhan’s Lord is in an angle along with Guru, the gains will be great
- 十一宫主落二宫（Dhan） 二宫主落角宫 与木星（Guru）同宫 收获甚大

### 反例或取消路

- There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic
- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava

### 判断方法路

- If Dhan Lord is in Labh, while the Lord of Labh in Dhan, wealth will be acquired by the native. Alternately these two Lords may join in an angle, or in a trine
- If Labh’s Lord is in Labh Bhava, the native will gain in all his undertakings, while his learning and happiness will be on the increase day by day

## 上游问题

- 无

## 停止条件

- 缺少十一宫主落宫事实时停止。
- 缺少二宫主落角宫事实时停止。
- 缺少二宫主与木星同宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
