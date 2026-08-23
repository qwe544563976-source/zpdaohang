---
method: ch39-v22-benefics-in-kendras-from-karakamsa
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Karakāńś Lagna 起算的角宫内有吉星：成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Karakāńś 该怎么用
- 我有没有登顶的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Karakāńś 是哪个星座
- 本盘中哪些行星被判为吉星
- 从 Karakāńś Lagna 起算的角宫（Kendras）内是否有吉星

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v22-benefics-in-kendras-from-karakamsa.step-001

- 动作：先取本盘 Karakāńś Lagna 与吉星名册，再核对从 Karakāńś Lagna 起算的角宫内是否有吉星。
- 适用范围：仅限本命盘；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：从 Karakāńś Lagna 起算的角宫（Kendras）内有吉星时，命主会成为国王。
- 本步骤产出事实：["Karakāńś 角宫吉星的贵格判定"]
- 所需事实：["本盘的 Karakāńś 是哪个星座", "本盘中哪些行星被判为吉星", "从 Karakāńś Lagna 起算的角宫（Kendras）内是否有吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘的 Karakāńś 是哪个星座"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "从 Karakāńś Lagna 起算的角宫（Kendras）内是否有吉星"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写角宫，不得把三角宫等别的宫位也算进来。", "不得据此推断登位时间或具体权位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Karakāńś 是哪个星座、本盘中哪些行星被判为吉星、从 Karakāńś Lagna 起算的角宫（Kendras）内是否有吉星。
- 缺失即停字段：["本盘的 Karakāńś 是哪个星座", "本盘中哪些行星被判为吉星", "从 Karakāńś Lagna 起算的角宫（Kendras）内是否有吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v22`｜PDF [83]｜“If there are benefics in Kendras from Karakāńś Lagna, he will become a king.”


## 四路查书计划

### 支持路

- If there are benefics in Kendras from Karakāńś Lagna, he will become a king
- Karakāńś 起算角宫吉星 成为国王

### 反例或取消路

- If malefics be in Karakāńś, Arudh Lagn and the 2<sup>nd</sup> and 8<sup>th</sup> from these places, there will be Kemadrum Yog
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Karakāńś is the Navāńś, occupied by the Atma Karak Grah
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Should the Kendras/Konas from the Karakāńś be occupied by benefics, devoid
- The Yogas so far stated by me with reference to Lagn Pad be similarly evaluated from Karakāńś as well

## 上游问题

- 无

## 停止条件

- 缺少 Karakāńś 定位事实时停止。
- 缺少本盘吉星名册事实时停止。
- 缺少角宫吉星占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
