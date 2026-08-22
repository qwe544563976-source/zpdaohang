---
method: ch09-v33-mangal-shani-in-kendra-from-chandra-same-navamsa-two-mothers
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 火星与土星同处自月亮起的角宫且同一九分盘分段：命主有两位母亲，且短寿

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 会不会有两个母亲
- 火星土星同宫在九分盘同段怎么断

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 火星（Mangal）是否与土星（Shani）同宫
- 火星（Mangal）是否落自月亮（Chandra）起算的角宫（Kendra）
- 火星（Mangal）与土星（Shani）是否落在同一个九分盘（Navāńś D9）分段

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v33-mangal-shani-in-kendra-from-chandra-same-navamsa-two-mothers.step-001

- 动作：核对火星与土星是否同处自月亮起算的角宫，并核对两者是否落在同一个九分盘分段。
- 适用范围：仅限本命盘对母亲与寿命的判断；角宫以月亮为起算点。
- 原文最小意思：火星（Mangal）与土星（Shani）同处自月亮（Chandra）起算的角宫（Kendra）、又落在同一个九分盘（Navāńś D9）分段时，孩子会有两位母亲，且仍然短寿。
- 本步骤产出事实：["火土同角宫同九分盘的两位母亲与短寿判定"]
- 所需事实：["火星（Mangal）是否与土星（Shani）同宫", "火星（Mangal）是否落自月亮（Chandra）起算的角宫（Kendra）", "火星（Mangal）与土星（Shani）是否落在同一个九分盘（Navāńś D9）分段"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否与土星（Shani）同宫"}, {"fact_key": "火星（Mangal）是否落自月亮（Chandra）起算的角宫（Kendra）"}, {"fact_key": "火星（Mangal）与土星（Shani）是否落在同一个九分盘（Navāńś D9）分段"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把九分盘（Navāńś D9）换成三分盘或十分盘。", "不得把角宫的起算点从月亮换成上升。", "不得把『两位母亲』解释成原文没写的具体缘由。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：火星（Mangal）是否与土星（Shani）同宫、火星（Mangal）是否落自月亮（Chandra）起算的角宫（Kendra）、火星（Mangal）与土星（Shani）是否落在同一个九分盘（Navāńś D9）分段。
- 缺失即停字段：["火星（Mangal）是否与土星（Shani）同宫", "火星（Mangal）是否落自月亮（Chandra）起算的角宫（Kendra）", "火星（Mangal）与土星（Shani）是否落在同一个九分盘（Navāńś D9）分段"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v33`｜PDF [24]｜“If Mangal and Shani are together in a Kendra with reference to Chandra and occupy one and the same Navāńś, the child will have two mothers. Yet it will be short-lived.”


## 四路查书计划

### 支持路

- If Mangal and Shani are together in a Kendra with reference to Chandra and occupy one and the same Navāńś, the child will have two mothers
- 火星土星 自月亮角宫 同一九分盘 两位母亲

### 反例或取消路

- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- Surya in Vyaya will confer a hundred-year life span on one born in Tul Lagn.

### 适用边界路

- Evils to Mother (up to Sloka 33)
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.

### 判断方法路

- Evils at Birth
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Navāńś. The Navāńś calculation are for a Movable Rashifrom there itself, for a Fixed Rashifrom the 9<sup>th</sup> thereof
- 九分盘怎么起

## 上游问题

- 无

## 停止条件

- 缺少火星、土星的落宫与同宫事实时停止。
- 缺少两者的九分盘（Navāńś D9）分段时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
