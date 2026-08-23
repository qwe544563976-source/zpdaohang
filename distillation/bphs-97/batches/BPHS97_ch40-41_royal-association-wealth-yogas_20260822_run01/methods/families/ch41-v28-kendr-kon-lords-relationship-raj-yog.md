---
method: ch41-v28-kendr-kon-lords-relationship-raj-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Raj Yog：角宫之主与三角宫之主之间建立关联

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有贵格
- 什么样的组合才算贵格

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘各角宫（Kendr）之主分别是哪颗行星
- 本盘各三角宫（Kon）之主分别是哪颗行星
- 角宫之主（Kendr's Lord）与三角宫之主（Kon's Lord）之间是否建立关联（relationship）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch41-v28-kendr-kon-lords-relationship-raj-yog.step-001

- 动作：先认出各角宫之主与各三角宫之主，再核对其中是否有一位角宫之主与一位三角宫之主建立了关联。
- 适用范围：仅限本命盘角宫之主与三角宫之主的关联；原文本偈没有给出「关联（relationship）」的判准，须另按本书第 3 章 Natural／Temporary／Compound Relationships 的界定取得，未取到即停判；本偈括注中另提的第六种关联（Navāńś 位置互涉）是英译者补充，并自陈 there is no specific classic sanction for this，本方法不采；原文未给时间限定。
- 原文最小意思：角宫之主（Kendr's Lord）与三角宫之主（Kon's Lord）之间建立关联时，即成 Raj Yog。
- 本步骤产出事实：["角宫主三角宫主关联的 Raj Yog 判定"]
- 所需事实：["本盘各角宫（Kendr）之主分别是哪颗行星", "本盘各三角宫（Kon）之主分别是哪颗行星", "角宫之主（Kendr's Lord）与三角宫之主（Kon's Lord）之间是否建立关联（relationship）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘各角宫（Kendr）之主分别是哪颗行星"}, {"fact_key": "本盘各三角宫（Kon）之主分别是哪颗行星"}, {"fact_key": "角宫之主（Kendr's Lord）与三角宫之主（Kon's Lord）之间是否建立关联（relationship）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把英译者补出的第六种 Navāńś 关联当成本书正文的判准（原文自陈 there is no specific classic sanction for this）。", "原文只说成就 Raj Yog，不得据此推断地位高低、财富数额或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘各角宫（Kendr）之主分别是哪颗行星、本盘各三角宫（Kon）之主分别是哪颗行星、角宫之主（Kendr's Lord）与三角宫之主（Kon's Lord）之间是否建立关联（relationship）。
- 缺失即停字段：["本盘各角宫（Kendr）之主分别是哪颗行星", "本盘各三角宫（Kon）之主分别是哪颗行星", "角宫之主（Kendr's Lord）与三角宫之主（Kon's Lord）之间是否建立关联（relationship）"]
- 原文证据：
  - `bphs-97:santhanam:ch41:v28`｜PDF [87]｜“If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained.”


## 四路查书计划

### 支持路

- Lords of Kendras and Konas Related
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained
- 角宫主与三角宫主关联 Raj Yog

### 反例或取消路

- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Natural Relationships. Note the Rāśis, which are the 2nd , 4th , 5th , 8th , 9th and 12th from the Mooltrikon of a Grah
- Temporary Relationships. The Grah, posited in the 2nd , 3rd , 4th , 10th , 11th , or the 12th from another, becomes a mutual friend
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- Combinations for Wealth
- If the Lord of a Kendr and the Lord of a Kon, having a relationship, as indicated in Sloka 28, happen to be in Parijatāńś

## 上游问题

- 无

## 停止条件

- 角宫之主或三角宫之主的身份事实缺失时停止。
- 「关联（relationship）」的判准未按本书第 3 章的 Grah 关系界定取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
