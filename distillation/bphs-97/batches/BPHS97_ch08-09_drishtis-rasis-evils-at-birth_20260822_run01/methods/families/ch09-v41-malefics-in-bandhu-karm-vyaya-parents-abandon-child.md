---
method: ch09-v41-malefics-in-bandhu-karm-vyaya-parents-abandon-child
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 四宫、十宫与十二宫都被凶星占据：父母双方都把孩子丢给它自己的命运

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 四宫十宫十二宫都有凶星会怎样
- 会不会被父母抛下

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 四宫（Bandhu Bhava）是否被凶星占据
- 十宫（Karm Bhava）是否被凶星占据
- 十二宫（Vyaya Bhava）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v41-malefics-in-bandhu-karm-vyaya-parents-abandon-child.step-001

- 动作：核对四宫、十宫与十二宫是否都被凶星占据。
- 适用范围：仅限本命盘对父母与孩子关系的判断；原文没有指明四处漂泊的是父母还是孩子。
- 原文最小意思：四宫（Bandhu）、十宫（Karm）与十二宫（Vyaya Bhava）都被凶星占据时，父母双方都会把孩子丢给它自己的命运，并四处漂泊。
- 本步骤产出事实：["三宫皆凶的父母弃养判定"]
- 所需事实：["四宫（Bandhu Bhava）是否被凶星占据", "十宫（Karm Bhava）是否被凶星占据", "十二宫（Vyaya Bhava）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "四宫（Bandhu Bhava）是否被凶星占据"}, {"fact_key": "十宫（Karm Bhava）是否被凶星占据"}, {"fact_key": "十二宫（Vyaya Bhava）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文指定四处漂泊的是父母还是孩子——原文的句子没有分清。", "不得把『丢给它自己的命运』改写成父母去世。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：四宫（Bandhu Bhava）是否被凶星占据、十宫（Karm Bhava）是否被凶星占据、十二宫（Vyaya Bhava）是否被凶星占据。
- 缺失即停字段：["四宫（Bandhu Bhava）是否被凶星占据", "十宫（Karm Bhava）是否被凶星占据", "十二宫（Vyaya Bhava）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v41`｜PDF [24]｜“If Bandhu, Karm and Vyaya Bhava are all occupied by malefics, both the parents will leave the child to its own fate and wander from place to place.”


## 四路查书计划

### 支持路

- If Bandhu, Karm and Vyaya Bhava are all occupied by malefics, both the parents will leave the child to its own fate and wander from place to place
- 四宫十宫十二宫 凶星 父母 弃养

### 反例或取消路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.

### 适用边界路

- Evil to Father (up to Sloka 42)
- Evils to Mother (up to Sloka 33)
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- 父母的凶象怎么看

## 上游问题

- 无

## 停止条件

- 缺少四宫、十宫、十二宫的凶星占据事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
