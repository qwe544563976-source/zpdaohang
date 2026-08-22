---
method: ch09-v38-mangal-in-karm-in-enemy-rasi-father-troubled-death
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 火星落十宫且该处为其敌星座：父亲之死既早且多苦

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 火星落十宫在敌星座怎么断
- 父亲去世的情形

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 火星（Mangal）是否落十宫（Karm Bhava）
- 火星（Mangal）所落星座（Rāśi）是否为其敌星座（enemy’s Rāśi）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v38-mangal-in-karm-in-enemy-rasi-father-troubled-death.step-001

- 动作：核对火星是否落十宫，并核对该宫所在星座是否为火星的敌星座。
- 适用范围：仅限本命盘对父亲的凶象；原文的 his enemy 指火星自己的敌星座。
- 原文最小意思：火星（Mangal）落十宫（Karm Bhava）、且该处即其敌星座（enemy’s Rāśi）时，父亲之死既早且多苦。
- 本步骤产出事实：["火星落十宫敌星座的父亲凶象判定"]
- 所需事实：["火星（Mangal）是否落十宫（Karm Bhava）", "火星（Mangal）所落星座（Rāśi）是否为其敌星座（enemy’s Rāśi）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落十宫（Karm Bhava）"}, {"fact_key": "火星（Mangal）所落星座（Rāśi）是否为其敌星座（enemy’s Rāśi）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把敌星座（enemy’s Rāśi）换成落陷或燃烧等原文没写的状态。", "不得把『既早且多苦』补成具体年岁或死因。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：火星（Mangal）是否落十宫（Karm Bhava）、火星（Mangal）所落星座（Rāśi）是否为其敌星座（enemy’s Rāśi）。
- 缺失即停字段：["火星（Mangal）是否落十宫（Karm Bhava）", "火星（Mangal）所落星座（Rāśi）是否为其敌星座（enemy’s Rāśi）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v38`｜PDF [24]｜“Early and troubled will be one’s father’s death, if Mangal is in Karm Bhava identical with his enemy’s Rāśi.”


## 四路查书计划

### 支持路

- Early and troubled will be one’s father’s death, if Mangal is in Karm Bhava identical with his enemy’s Rāśi
- 火星十宫 敌星座 父亲 早亡

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils
- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.

### 适用边界路

- Evil to Father (up to Sloka 42)
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- 敌星座怎么定

## 上游问题

- 无

## 停止条件

- 缺少火星落宫事实时停止。
- 缺少行星敌友星座关系的取值时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
