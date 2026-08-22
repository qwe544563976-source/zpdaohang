---
method: ch24-v92-weak-randhr-lord-in-randhr
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 无力的八宫主落八宫：寿命中等、为盗受责也指责他人

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的寿元大概是什么档次
- 我性格里有哪些容易惹祸的地方

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫主（Randhr's Lord）是否落八宫（Randhr）
- 八宫主（Randhr's Lord）是否无力（weak）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v92-weak-randhr-lord-in-randhr.step-001

- 动作：核对八宫主（Randhr's Lord）是否落八宫（Randhr Bhava）、该行星是否无力，据此判断寿命档次与品行。
- 适用范围：仅限本命盘八宫主落八宫（Randhr Bhava）且该行星无力一条；「the said Grah」承同偈前句所说的八宫主，逐字短引已把整偈一并给出；原文只说 weak，未在本偈给出强弱判准，判准未确定即停判；本段原文自标「Effects of Randhr’s Lord in Various Bhavas (up to Sloka 96)」；原文未给寿数年份。
- 原文最小意思：八宫主（Randhr's Lord）无力（weak）、且落八宫（Randhr Bhava）时，寿命为中等，本人会成为盗贼、受人指责，也会指责他人。
- 本步骤产出事实：["无力八宫主落八宫的寿命与品行判定"]
- 所需事实：["八宫主（Randhr's Lord）是否落八宫（Randhr）", "八宫主（Randhr's Lord）是否无力（weak）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "八宫主（Randhr's Lord）是否落八宫（Randhr）"}, {"fact_key": "八宫主（Randhr's Lord）是否无力（weak）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自行为 weak 补一套强弱算法。", "不得把「中等寿命」换算成具体岁数或年份。", "不得把同偈前句无条件的「长寿」结论并入本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否落八宫（Randhr）、八宫主（Randhr's Lord）是否无力（weak）。
- 缺失即停字段：["八宫主（Randhr's Lord）是否落八宫（Randhr）", "八宫主（Randhr's Lord）是否无力（weak）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v92`｜PDF [46]｜“If Randhr’s Lord is in Randhr Bhava, the native will be long-lived. If the said Grah is weak, being in Randhr Bhava, the longevity will be medium, while the native will be a thief, be blameworthy and will blame others as well.”


## 四路查书计划

### 支持路

- If the said Grah is weak, being in Randhr Bhava, the longevity will be medium
- 无力的八宫主落八宫 中等寿命 盗贼

### 反例或取消路

- If Randhr’s Lord is in an angle, long life is indicated

### 适用边界路

- Indications of Randhr Bhava. Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead and things, that have happened and are to happen
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- Effects of Randhr’s Lord in Various Bhavas
- Effects of Randhr Bhava

## 上游问题

- 无

## 停止条件

- 缺少八宫主是否落八宫的事实时停止。
- 原文未给 weak 的判准，该强弱事实未确定即停止（判准待排盘窗口定义）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
