---
method: ch24-v7-malefic-lagn-lord-in-yuvati-wife
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶星上升主落七宫：妻子不会长寿

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我妻子的健康和寿数怎么样
- 我的婚姻会不会中途断掉

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星
- 上升主（Lagn's Lord）是否被判为凶星
- 上升主（Lagn's Lord）是否落七宫（Yuvati）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v7-malefic-lagn-lord-in-yuvati-wife.step-001

- 动作：先确定本盘凶星名册，再核对上升主（Lagn's Lord）本身是否为凶星、是否落七宫（Yuvati）。
- 适用范围：仅限本命盘上升主落七宫（Yuvati Bhava）且本身为凶星一条；原文以男命立说（the natives wife），女命命中时结论不能照搬；原文只说 will not live (long)，未给年龄、死因或时间。
- 原文最小意思：上升主（Lagn's Lord）是凶星且落七宫（Yuvati）时，本人的妻子不会长寿。
- 本步骤产出事实：["凶星上升主落七宫的配偶寿数判定"]
- 所需事实：["本盘中哪些行星被判为凶星", "上升主（Lagn's Lord）是否被判为凶星", "上升主（Lagn's Lord）是否落七宫（Yuvati）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "上升主（Lagn's Lord）是否被判为凶星"}, {"fact_key": "上升主（Lagn's Lord）是否落七宫（Yuvati）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断妻子去世的年龄、原因或时间。", "不得据此推断本人是否再婚或有几位配偶。", "不得把本条套用到吉星上升主落七宫——原文对那一侧另有断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星、上升主（Lagn's Lord）是否被判为凶星、上升主（Lagn's Lord）是否落七宫（Yuvati）。
- 缺失即停字段：["本盘中哪些行星被判为凶星", "上升主（Lagn's Lord）是否被判为凶星", "上升主（Lagn's Lord）是否落七宫（Yuvati）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v7`｜PDF [41]｜“If Lagn’s Lord is a malefic and is placed in Yuvati Bhava, the natives wife will not live (long).”


## 四路查书计划

### 支持路

- If Lagn’s Lord is a malefic and is placed in Yuvati Bhava, the natives wife will not live (long)
- 凶星上升主 落七宫 妻子不长寿

### 反例或取消路

- The native will beget a spouse endowed with (the seven principal) virtues, who will expand his dynasty by sons and grandsons, if the 7th Lord is exalted, while Yuvati is occupied by strong Lagna Lord and a benefic
- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)

### 适用边界路

- Indications of Yuvati Bhava. Wife, travel, trade, loss of sight, death etc. be known from Yuvati Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- Effects of Yuvati’s Lord in Various Bhavas
- lf Ari, 7th and 8th are in their order occupied by Mangal, Rahu and Shani, the native’s wife will not live (long)

## 上游问题

- 无

## 停止条件

- 缺少上升主是否落七宫的事实时停止。
- 凶星名册未确定时停止。
- 缺少上升主本身是否为凶星的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
