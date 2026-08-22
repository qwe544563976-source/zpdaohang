---
method: ch09-v28-malefic-in-fourth-from-chandra-inimical-rasi-no-benefic-in-kendra
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 自月亮起第 4 位为敌星座且有凶星、角宫无吉星：孩子早失母亲

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 自月亮起第四宫有凶星怎么断
- 角宫没有吉星会怎样
- 会不会早年失去母亲

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 自月亮（Chandra）起算的第 4 位是否有凶星
- 自月亮（Chandra）起算的第 4 个星座（Rāśi）是否为敌星座（inimical Rāśi）
- 是否有吉星落角宫（Kendra）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v28-malefic-in-fourth-from-chandra-inimical-rasi-no-benefic-in-kendra.step-001

- 动作：核对自月亮起算第 4 位的凶星与星座属性，并核对角宫内有无吉星。
- 适用范围：仅限本命盘对母亲的凶象；原文只写 an inimical Rāśi，没有指明是与谁为敌，未确定即停判。
- 原文最小意思：自月亮（Chandra）起算的第 4 位有凶星、该处又是敌星座（inimical Rāśi），同时没有吉星落角宫（Kendra）时，孩子会提早失去母亲。
- 本步骤产出事实：["自月亮起第四位受克的母亲凶象判定"]
- 所需事实：["自月亮（Chandra）起算的第 4 位是否有凶星", "自月亮（Chandra）起算的第 4 个星座（Rāśi）是否为敌星座（inimical Rāśi）", "是否有吉星落角宫（Kendra）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "自月亮（Chandra）起算的第 4 位是否有凶星"}, {"fact_key": "自月亮（Chandra）起算的第 4 个星座（Rāśi）是否为敌星座（inimical Rāśi）"}, {"operator": "NOT", "operands": [{"fact_key": "是否有吉星落角宫（Kendra）"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文指定敌星座（inimical Rāśi）是与哪一颗行星为敌——原文没有写，未确定即停判。", "不得把角宫（Kendra）的起算点改成月亮——原文这一句只说『没有吉星落角宫』。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：自月亮（Chandra）起算的第 4 位是否有凶星、自月亮（Chandra）起算的第 4 个星座（Rāśi）是否为敌星座（inimical Rāśi）、是否有吉星落角宫（Kendra）。
- 缺失即停字段：["自月亮（Chandra）起算的第 4 位是否有凶星", "自月亮（Chandra）起算的第 4 个星座（Rāśi）是否为敌星座（inimical Rāśi）", "是否有吉星落角宫（Kendra）"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v28`｜PDF [23, 24]｜“Should a malefic be in the 4<sup>th</sup> , identical with an inimical Rāśi, counted from Chandra, while there is no benefic in a Kendra, the child will lose its mother in a premature manner.”


## 四路查书计划

### 支持路

- Should a malefic be in the 4<sup>th</sup> , identical with an inimical Rāśi, counted from Chandra, while there is no benefic in a Kendra, the child will lose its mother in a premature manner
- 自月亮第四位 敌星座 凶星 角宫无吉星 失母

### 反例或取消路

- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed, as Surya eliminates darkness.

### 适用边界路

- Evils to Mother (up to Sloka 33)
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- The 9<sup>th</sup> from Surya denotes father, the 4<sup>th</sup> from Chandra mother

### 判断方法路

- Evils at Birth
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- 敌星座怎么定

## 上游问题

- 无

## 停止条件

- 原文只写 an inimical Rāśi，未指明与谁为敌；该判准未确定即停判。
- 缺少自月亮起算第 4 位的占据者事实时停止。
- 缺少角宫内吉星事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
