---
method: ch09-v23-all-weak-grahas-in-apoklima-two-or-six-months
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 所有行星无力且都落 Apoklima 宫：寿命只有 2 个月或 6 个月

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 所有行星都落三六九十二宫会怎样
- 行星无力落 Apoklima 有什么后果

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘所有行星（Grahas）是否都落 Apoklima 宫（Apoklima Bhavas）
- 本盘所有行星（Grahas）是否都无力（devoid of strength）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v23-all-weak-grahas-in-apoklima-two-or-six-months.step-001

- 动作：核对全盘行星是否都无力，并核对它们是否都被安置在 Apoklima 宫。
- 适用范围：仅限本命盘出生时的凶象；原文没有给『无力』的判准（强弱判准见第 27 章 Shad Bal）。
- 原文最小意思：全盘行星（Grahas）都无力（devoid of strength）且都被安置在 Apoklima 宫（Apoklima Bhavas）时，孩子的寿命只有 2 个月或 6 个月。
- 本步骤产出事实：["全盘无力行星落 Apoklima 宫的寿命判定"]
- 所需事实：["本盘所有行星（Grahas）是否都落 Apoklima 宫（Apoklima Bhavas）", "本盘所有行星（Grahas）是否都无力（devoid of strength）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘所有行星（Grahas）是否都落 Apoklima 宫（Apoklima Bhavas）"}, {"fact_key": "本盘所有行星（Grahas）是否都无力（devoid of strength）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得在 2 个月与 6 个月之间替原文选定一个——原文两说并列。", "不得自造『无力』的判准，原文本偈没有给。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘所有行星（Grahas）是否都落 Apoklima 宫（Apoklima Bhavas）、本盘所有行星（Grahas）是否都无力（devoid of strength）。
- 缺失即停字段：["本盘所有行星（Grahas）是否都落 Apoklima 宫（Apoklima Bhavas）", "本盘所有行星（Grahas）是否都无力（devoid of strength）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v23`｜PDF [23]｜“The life span of the child will be either 2 months, or 6 months only, if all Grahas devoid of strength are relegated to Apoklima Bhavas.”


## 四路查书计划

### 支持路

- The life span of the child will be either 2 months, or 6 months only, if all Grahas devoid of strength are relegated to Apoklima Bhavas
- 行星无力 Apoklima 宫 2 个月 6 个月

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- Surya in Vyaya will confer a hundred-year life span on one born in Tul Lagn.
- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Sahaj, Ari, Dharm and Vyaya Bhava are called Apoklimas (cadents)
- Short-life Combinations (up to Sloka 23)

### 判断方法路

- Evils at Birth
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Sahaj, Ari, Dharm and Vyaya Bhava are called Apoklimas (cadents)
- 行星强弱怎么算

## 上游问题

- 无

## 停止条件

- 『无力（devoid of strength）』的判准原文本偈未给，须另查第 27 章 Shad Bal；该事实取不到值时停止。
- 缺少全盘行星落宫事实时停止。
- 原文给出 2 个月与 6 个月两说，需要唯一年限时本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
