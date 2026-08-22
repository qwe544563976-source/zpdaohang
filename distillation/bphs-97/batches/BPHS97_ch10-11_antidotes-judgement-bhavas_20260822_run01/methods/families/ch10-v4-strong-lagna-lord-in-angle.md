---
method: ch10-v4-strong-lagna-lord-in-angle
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 消解凶恶：上升主有力地落在角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 上升主落角宫有什么用
- 我盘里的凶象有没有被抵消

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否落角宫
- 上升主（Lagn's Lord）是否有力

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch10-v4-strong-lagna-lord-in-angle.step-001

- 动作：核对上升主（Lagn Lord）是否有力地落在角宫。
- 适用范围：仅限第 10 章消解凶恶（Antidotes for Evils）主题；原文只说 strongly placed，未给强弱判准；原文未指定是哪一个角宫，也未给时间限定。
- 原文最小意思：上升主（Lagn Lord）有力地落在角宫时，上升主（Lagn Lord）单独一颗即足以抵消一切凶恶。
- 本步骤产出事实：["有力上升主落角宫抵消凶恶判定"]
- 所需事实：["上升主（Lagn's Lord）是否落角宫", "上升主（Lagn's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落角宫"}, {"fact_key": "上升主（Lagn's Lord）是否有力"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自行发明「有力」的判准。", "不得据此推断被抵消的是哪一类凶恶、何时抵消。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否落角宫、上升主（Lagn's Lord）是否有力。
- 缺失即停字段：["上升主（Lagn's Lord）是否落角宫", "上升主（Lagn's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch10:v4`｜PDF [25]｜“Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle”


## 四路查书计划

### 支持路

- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle
- 上升主有力落角宫 抵消一切凶恶

### 反例或取消路

- If malefics are in Kendras, devoid of Yuti with, or a Drishti from benefics, while Lagn’s Lord is not strong, only short life will result
- If Lagn’s Lord is in Ari, Randhr, or Vyaya Bhava, yuti with malefics and devoid of Yuti with and/or Drishti from a benefic, short life will come to pass

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- 「有力」的判准出自六力（Shad Bal）章

### 判断方法路

- If the stronger among Lagn’s Lord and Randhr’s Lord is placed in a Kendr, long life is indicated
- O Brahmin, first of all estimate the evils and checking factors thereof through Lagn and then declare the effects of the 12 Bhavas
- 怎样判断上升主是否有力、是否落角宫

## 上游问题

- 无

## 停止条件

- 缺少上升主落角宫事实时停止。
- 缺少上升主强弱事实时停止（「有力」的判准由排盘窗口定义）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
