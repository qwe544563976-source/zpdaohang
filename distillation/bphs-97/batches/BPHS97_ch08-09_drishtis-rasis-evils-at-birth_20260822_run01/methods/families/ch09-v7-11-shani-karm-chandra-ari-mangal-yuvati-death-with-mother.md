---
method: ch09-v7-11-shani-karm-chandra-ari-mangal-yuvati-death-with-mother
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 土星落十宫、月亮落六宫、火星落七宫：孩子与母亲当即去世

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 土星落十宫月亮落六宫火星落七宫怎么断
- 孩子与母亲同时的凶象

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 土星（Shani）是否落十宫（Karm Bhava）
- 月亮（Chandra）是否落六宫（Ari Bhava）
- 火星（Mangal）是否落七宫（Yuvati Bhava）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v7-11-shani-karm-chandra-ari-mangal-yuvati-death-with-mother.step-001

- 动作：核对土星、月亮、火星是否分别落十宫、六宫与七宫。
- 适用范围：仅限本命盘出生时的凶象；断语对象是孩子与母亲。
- 原文最小意思：土星（Shani）落十宫（Karm Bhava）、月亮（Chandra）落六宫（Ari Bhava）、火星（Mangal）落七宫（Yuvati Bhava）时，孩子会连同母亲当即去世。
- 本步骤产出事实：["土月火三落宫的母子同殇判定"]
- 所需事实：["土星（Shani）是否落十宫（Karm Bhava）", "月亮（Chandra）是否落六宫（Ari Bhava）", "火星（Mangal）是否落七宫（Yuvati Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否落十宫（Karm Bhava）"}, {"fact_key": "月亮（Chandra）是否落六宫（Ari Bhava）"}, {"fact_key": "火星（Mangal）是否落七宫（Yuvati Bhava）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把三颗行星的落宫拆开单用——原文要求三者同时成立。", "不得把『当即』补成原文没有的具体时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星（Shani）是否落十宫（Karm Bhava）、月亮（Chandra）是否落六宫（Ari Bhava）、火星（Mangal）是否落七宫（Yuvati Bhava）。
- 缺失即停字段：["土星（Shani）是否落十宫（Karm Bhava）", "月亮（Chandra）是否落六宫（Ari Bhava）", "火星（Mangal）是否落七宫（Yuvati Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v7-11`｜PDF [22]｜“Immediate death of the child along with its mother will occur, if Shani is in Karm Bhava, Chandra in Ari Bhava and Mangal in Yuvati Bhava.”


## 四路查书计划

### 支持路

- Immediate death of the child along with its mother will occur, if Shani is in Karm Bhava, Chandra in Ari Bhava and Mangal in Yuvati Bhava
- 土星十宫 月亮六宫 火星七宫 母子

### 反例或取消路

- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.

### 适用边界路

- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.
- Evils to Mother (up to Sloka 33)
- Thanu, Dhan, Sahaj, Bandhu, Putr, Ari, Yuvati, Randhr, Dharm, Karma, Labh and Vyaya are in order the names of Bhavas

### 判断方法路

- Evils at Birth
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 母亲的凶象怎么看

## 上游问题

- 无

## 停止条件

- 缺少土星、月亮、火星任一落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
