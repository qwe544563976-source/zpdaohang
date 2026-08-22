---
method: ch09-v7-11-surya-dharm-mangal-yuvati-guru-shukra-labh-one-month
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 太阳落九宫、火星落七宫、木星与金星落十一宫：寿命只有一个月

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 太阳落九宫火星落七宫木星金星落十一宫怎么断
- 只有一个月寿命的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）是否落九宫（Dharm Bhava）
- 火星（Mangal）是否落七宫（Yuvati Bhava）
- 木星（Guru）是否落十一宫（Labh Bhava）
- 金星（Shukra）是否落十一宫（Labh Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v7-11-surya-dharm-mangal-yuvati-guru-shukra-labh-one-month.step-001

- 动作：核对太阳、火星、木星与金星是否分别落九宫、七宫与十一宫。
- 适用范围：仅限本命盘出生时的凶象；原文给出四颗行星的落宫。
- 原文最小意思：太阳（Surya）落九宫（Dharm Bhava）、火星（Mangal）落七宫（Yuvati Bhava）、木星（Guru）与金星（Shukra）落十一宫（Labh Bhava）时，人的寿命只有一个月。
- 本步骤产出事实：["四星落宫的一个月寿命判定"]
- 所需事实：["太阳（Surya）是否落九宫（Dharm Bhava）", "火星（Mangal）是否落七宫（Yuvati Bhava）", "木星（Guru）是否落十一宫（Labh Bhava）", "金星（Shukra）是否落十一宫（Labh Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "太阳（Surya）是否落九宫（Dharm Bhava）"}, {"fact_key": "火星（Mangal）是否落七宫（Yuvati Bhava）"}, {"fact_key": "木星（Guru）是否落十一宫（Labh Bhava）"}, {"fact_key": "金星（Shukra）是否落十一宫（Labh Bhava）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把一个月改成原文没写的其他期限。", "不得把木星与金星拆成只需其中一颗落十一宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）是否落九宫（Dharm Bhava）、火星（Mangal）是否落七宫（Yuvati Bhava）、木星（Guru）是否落十一宫（Labh Bhava）、金星（Shukra）是否落十一宫（Labh Bhava）。
- 缺失即停字段：["太阳（Surya）是否落九宫（Dharm Bhava）", "火星（Mangal）是否落七宫（Yuvati Bhava）", "木星（Guru）是否落十一宫（Labh Bhava）", "金星（Shukra）是否落十一宫（Labh Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v7-11`｜PDF [22]｜“Only a month will be the span of one’s life, who had Surya in Dharm Bhava, Mangal in Yuvati Bhava and Guru and Shukra in Labh Bhava.”


## 四路查书计划

### 支持路

- Only a month will be the span of one’s life, who had Surya in Dharm Bhava, Mangal in Yuvati Bhava and Guru and Shukra in Labh Bhava
- 太阳九宫 火星七宫 木星金星十一宫 一个月

### 反例或取消路

- Surya in Vyaya will confer a hundred-year life span on one born in Tul Lagn.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Short-life Combinations (up to Sloka 23)
- Kindly detail methods of ascertaining the life-span of human beings.

### 判断方法路

- Evils at Birth
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 短寿组合怎么看

## 上游问题

- 无

## 停止条件

- 缺少四颗行星任一落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
