---
method: ch09-v29-malefics-in-bandhu-and-karm-evils-to-father
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶星占据四宫与十宫：父亲得到同样的（凶）效果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 凶星落四宫十宫对父亲有什么影响
- 父亲的凶象怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 四宫（Bandhu Bhava）是否被凶星占据
- 十宫（Karm Bhava）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v29-malefics-in-bandhu-and-karm-evils-to-father.step-001

- 动作：核对四宫与十宫是否被凶星占据。
- 适用范围：仅限本命盘对父亲的凶象；原文以『同样的效果』承接同偈前句『给母亲带来凶事』，本身不另给内容。
- 原文最小意思：凶星落六宫 Ari 与十二宫 Vyaya Bhava 给母亲带来凶事；四宫（Bandhu）与十宫（Karm Bhava）被凶星占据时，孩子的父亲会得到相同的效果。
- 本步骤产出事实：["四宫十宫凶星的父亲凶象判定"]
- 所需事实：["四宫（Bandhu Bhava）是否被凶星占据", "十宫（Karm Bhava）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "四宫（Bandhu Bhava）是否被凶星占据"}, {"fact_key": "十宫（Karm Bhava）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『同样的效果』展开成原文没写的具体结果（去世、疾病或分离）。", "不得把两宫减为其中一宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：四宫（Bandhu Bhava）是否被凶星占据、十宫（Karm Bhava）是否被凶星占据。
- 缺失即停字段：["四宫（Bandhu Bhava）是否被凶星占据", "十宫（Karm Bhava）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v29`｜PDF [24]｜“Malefics in Ari and Vyaya Bhava will bring evils to mother. The child’s father will receive similar effects, if Bandhu and Karm Bhava are captured by malefics.”


## 四路查书计划

### 支持路

- The child’s father will receive similar effects, if Bandhu and Karm Bhava are captured by malefics
- 凶星 四宫十宫 父亲 凶事

### 反例或取消路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.

### 适用边界路

- Evil to Father (up to Sloka 42)
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 父亲用哪颗星看

## 上游问题

- 无

## 停止条件

- 缺少四宫、十宫的凶星占据事实时停止。
- 『同样的效果』所指的内容由同偈前句给出，前句结论未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
