---
method: ch18-v10-13-5-malefics-controlled-by-spouse
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 受配偶控制且配偶与家族为敌：凶星落十二宫与七宫、减光月落五宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会被配偶压制
- 配偶和我家里人合不合得来

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十二宫（Vyaya）是否被凶星占据
- 七宫（Yuvati）是否被凶星占据
- 月亮（Chandra）是否落五宫（Putr）
- 月亮（Chandra）是否为减光月

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v10-13-5-malefics-controlled-by-spouse.step-001

- 动作：核对十二宫（Vyaya）与七宫（Yuvati）是否被凶星占据，并核对月亮（Chandra）是否为减光月且落五宫（Putr）。
- 适用范围：仅限本命盘配偶关系主题；原文以「his spouse」立说，属男命框架；原文未给时间。
- 原文最小意思：凶星落十二宫与七宫、且减光月落五宫时，命主受配偶控制，该配偶与其族（或家族）为敌。
- 本步骤产出事实：["凶星落十二七宫减光月落五宫主受配偶控制判定"]
- 所需事实：["十二宫（Vyaya）是否被凶星占据", "七宫（Yuvati）是否被凶星占据", "月亮（Chandra）是否落五宫（Putr）", "月亮（Chandra）是否为减光月"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十二宫（Vyaya）是否被凶星占据"}, {"fact_key": "七宫（Yuvati）是否被凶星占据"}, {"fact_key": "月亮（Chandra）是否落五宫（Putr）"}, {"fact_key": "月亮（Chandra）是否为减光月"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断离异、婚期或配偶寿数。", "不得把三项前提拆开单用，原文是同时成立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十二宫（Vyaya）是否被凶星占据、七宫（Yuvati）是否被凶星占据、月亮（Chandra）是否落五宫（Putr）、月亮（Chandra）是否为减光月。
- 缺失即停字段：["十二宫（Vyaya）是否被凶星占据", "七宫（Yuvati）是否被凶星占据", "月亮（Chandra）是否落五宫（Putr）", "月亮（Chandra）是否为减光月"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v10-13.5`｜PDF [34]｜“Malefics in Vyaya and 7<sup>th</sup> , while decreasing Chandra is in Putr denote, that the native will be controlled by spouse, who will be inimical to the race (or family).”


## 四路查书计划

### 支持路

- Malefics in Vyaya and 7th, while decreasing Chandra is in Putr controlled by spouse inimical to the race
- 凶星落十二宫 七宫 减光月落五宫 受配偶控制

### 反例或取消路

- The native will beget a spouse endowed with (the seven principal) virtues who will expand his dynasty by sons and grandsons
- Yuvati Lord is in his own Rāśi, or in exaltation full happiness through his wife

### 适用边界路

- If Yuvati Bhava, or its Lord is yuti with a malefic the native’s wife will incur evils
- If Yuvati Bhava is occupied, or owned by Shani/Mangal, the native will beget a harlot, as his spouse
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- effects of Yuvati Bhava malefics spouse control
- 判断配偶关系应检查什么

## 上游问题

- 无

## 停止条件

- 缺少十二宫或七宫的凶星占据事实时停止。
- 缺少月亮减光与落五宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
