---
method: ch18-v14-15-worthy-spouse
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 贤德配偶：七宫主入旺且七宫被有力上升主与吉星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的配偶品行怎么样
- 我家会不会因为这门婚事而兴旺

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 七宫主（Yuvati's Lord）是否入旺
- 上升主（Lagn's Lord）是否落七宫（Yuvati）
- 上升主（Lagn's Lord）是否有力
- 七宫（Yuvati）是否被吉星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v14-15-worthy-spouse.step-001

- 动作：核对七宫主（Yuvati's Lord）是否入旺，并核对七宫（Yuvati）是否被有力的上升主（Lagn's Lord）与一颗吉星占据。
- 适用范围：仅限本命盘七宫（Yuvati）配偶品行主题；原文以「his dynasty」立说，属男命框架；原文只说 strong Lagna Lord，未给有力的判准。
- 原文最小意思：七宫主入旺、且七宫被有力的上升主与一颗吉星占据时，命主会得到具备（七种主要）美德的配偶，该配偶以儿子与孙子扩大其家族。
- 本步骤产出事实：["七宫主入旺得上升主吉星主贤德配偶判定"]
- 所需事实：["七宫主（Yuvati's Lord）是否入旺", "上升主（Lagn's Lord）是否落七宫（Yuvati）", "上升主（Lagn's Lord）是否有力", "七宫（Yuvati）是否被吉星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否入旺"}, {"fact_key": "上升主（Lagn's Lord）是否落七宫（Yuvati）"}, {"fact_key": "上升主（Lagn's Lord）是否有力"}, {"fact_key": "七宫（Yuvati）是否被吉星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断子孙数目、婚期或配偶家世。", "不得自行发明「有力」的判准。", "不得替原文列举那七种美德的具体内容。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：七宫主（Yuvati's Lord）是否入旺、上升主（Lagn's Lord）是否落七宫（Yuvati）、上升主（Lagn's Lord）是否有力、七宫（Yuvati）是否被吉星占据。
- 缺失即停字段：["七宫主（Yuvati's Lord）是否入旺", "上升主（Lagn's Lord）是否落七宫（Yuvati）", "上升主（Lagn's Lord）是否有力", "七宫（Yuvati）是否被吉星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v14-15`｜PDF [34]｜“The native will beget a spouse endowed with (the seven principal) virtues, who will expand his dynasty by sons and grandsons, if the 7<sup>th</sup> Lord is exalted, while Yuvati is occupied by strong Lagna Lord and a benefic.”


## 四路查书计划

### 支持路

- The native will beget a spouse endowed with (the seven principal) virtues 7th Lord is exalted Yuvati occupied by strong Lagna Lord and a benefic
- 七宫主入旺 上升主有力落七宫 吉星占据 贤德配偶

### 反例或取消路

- If Yuvati Bhava, or its Lord is yuti with a malefic the native’s wife will incur evils
- If Yuvati Bhava is occupied, or owned by Shani/Mangal, the native will beget a harlot, as his spouse

### 适用边界路

- Yuvati Bhava, or its Lord is bereft of strength
- Yuvati Lord is devoid of strength and is relegated to Ari, 8th, or Vyaya

### 判断方法路

- WORTHY SPOUSE Yuvati occupied by Lagna Lord benefic
- 判断配偶品行应检查什么

## 上游问题

- 无

## 停止条件

- 缺少七宫主入旺事实时停止。
- 缺少上升主落七宫或其强弱事实时停止（强弱判准待排盘窗口定义）。
- 缺少七宫吉星占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
