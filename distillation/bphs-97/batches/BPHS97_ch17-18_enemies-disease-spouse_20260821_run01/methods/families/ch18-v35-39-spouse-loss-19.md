---
method: ch18-v35-39-spouse-loss-19
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第19年失去配偶：七宫主落八宫、十二宫主落七宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我第19年会不会失去配偶
- 七宫主落八宫对配偶有什么妨害

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 七宫主（Yuvati's Lord）是否落八宫（Randhr）
- 十二宫主（Vyaya's Lord）是否落七宫（Yuvati）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v35-39-spouse-loss-19.step-001

- 动作：核对七宫主（Yuvati's Lord）是否落八宫（Randhr），并核对十二宫主（Vyaya's Lord）是否落七宫（Yuvati），判断失去配偶的年份。
- 适用范围：仅限本命盘七宫（Yuvati）配偶存亡主题；原文以「his spouse」立说，属男命框架；原文只给第19年一个年份。
- 原文最小意思：七宫主（Yuvati's Lord）落八宫，且十二宫主（Vyaya's Lord）落七宫（Yuvati）时，命主在第19年失去配偶。
- 本步骤产出事实：["七宫主落八宫且十二宫主落七宫主第19年失去配偶判定"]
- 所需事实：["七宫主（Yuvati's Lord）是否落八宫（Randhr）", "十二宫主（Vyaya's Lord）是否落七宫（Yuvati）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落八宫（Randhr）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落七宫（Yuvati）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断死因或再婚。", "不得把第19年之外的年份也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：七宫主（Yuvati's Lord）是否落八宫（Randhr）、十二宫主（Vyaya's Lord）是否落七宫（Yuvati）。
- 缺失即停字段：["七宫主（Yuvati's Lord）是否落八宫（Randhr）", "十二宫主（Vyaya's Lord）是否落七宫（Yuvati）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v35-39`｜PDF [35]｜“One will lose his spouse in his 19<sup>th</sup> year, if Yuvati Lord is in the 8<sup>th</sup> , while Vyaya Lord is in Yuvati.”


## 四路查书计划

### 支持路

- One will lose his spouse in his 19th year, if Yuvati Lord is in the 8th, while Vyaya Lord is in Yuvati
- 七宫主落八宫 十二宫主落七宫 第19年 失去配偶

### 反例或取消路

- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)
- THREE MARRIAGES there will be marriage in Karm year followed by another in the 22nd year and yet another in the 33rd year

### 适用边界路

- SICK WIFE Should Yuvati Lord be in Ari, 8th, or Vyaya, the wife will be sickly. This however does not apply to own Bhava, or exaltation placement
- LOSS OF SPOUSE Yuvati Lord is devoid of strength and is relegated to Ari, 8th, or Vyaya

### 判断方法路

- Effects of Yuvati Bhava Vyaya Lord placement spouse
- 判断配偶存亡应检查哪些宫主

## 上游问题

- 无

## 停止条件

- 缺少七宫主（Yuvati's Lord）落宫事实时停止。
- 缺少十二宫主（Vyaya's Lord）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
