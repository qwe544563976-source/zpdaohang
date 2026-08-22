---
method: ch09-v39-chandra-ari-shani-tanu-mangal-yuvati-father-not-long-lived
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮落六宫、土星落一宫、火星落七宫：父亲难有长寿

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮六宫土星一宫火星七宫怎么断
- 父亲的寿命长不长

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否落六宫（Ari Bhava）
- 土星（Shani）是否落一宫（Tanu Bhava）
- 火星（Mangal）是否落七宫（Yuvati Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v39-chandra-ari-shani-tanu-mangal-yuvati-father-not-long-lived.step-001

- 动作：核对月亮、土星、火星是否分别落六宫、一宫与七宫。
- 适用范围：仅限本命盘对父亲寿命的判断；原文只说不保长寿，未直接断定去世。
- 原文最小意思：月亮（Chandra）落六宫（Ari Bhava）、土星（Shani）落一宫（Tanu Bhava）、火星（Mangal）落七宫（Yuvati Bhava）时，出生时的这一天体排布不保父亲长寿。
- 本步骤产出事实：["月土火三落宫的父亲寿命判定"]
- 所需事实：["月亮（Chandra）是否落六宫（Ari Bhava）", "土星（Shani）是否落一宫（Tanu Bhava）", "火星（Mangal）是否落七宫（Yuvati Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落六宫（Ari Bhava）"}, {"fact_key": "土星（Shani）是否落一宫（Tanu Bhava）"}, {"fact_key": "火星（Mangal）是否落七宫（Yuvati Bhava）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『不保长寿』读成父亲必定早去世。", "不得把三颗行星的落宫拆开单用。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否落六宫（Ari Bhava）、土星（Shani）是否落一宫（Tanu Bhava）、火星（Mangal）是否落七宫（Yuvati Bhava）。
- 缺失即停字段：["月亮（Chandra）是否落六宫（Ari Bhava）", "土星（Shani）是否落一宫（Tanu Bhava）", "火星（Mangal）是否落七宫（Yuvati Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v39`｜PDF [24]｜“Chandra in Ari Bhava, Shani in Tanu Bhava and Mangal in Yuvati Bhava: this array of heavenly bodies at birth will not ensure a long span of life for the father.”


## 四路查书计划

### 支持路

- Chandra in Ari Bhava, Shani in Tanu Bhava and Mangal in Yuvati Bhava: this array of heavenly bodies at birth will not ensure a long span of life for the father
- 月亮六宫 土星一宫 火星七宫 父亲寿命

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils
- Surya in Vyaya will confer a hundred-year life span on one born in Tul Lagn.

### 适用边界路

- Evil to Father (up to Sloka 42)
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Kindly detail methods of ascertaining the life-span of human beings.

### 判断方法路

- Evils at Birth
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- 父亲的寿命怎么看

## 上游问题

- 无

## 停止条件

- 缺少三颗行星任一落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
