---
method: ch18-v19-21-many-wives
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 多位妻子：金星落双体星座、该星座主星入旺、七宫主有力

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有很多位妻子
- 金星落双体星座主什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘金星（Shukra）落在哪个星座
- 金星（Shukra）是否落双体星座（Dual Rāśi）
- 金星（Shukra）所落星座的主星是否入旺
- 七宫主（Yuvati's Lord）是否有力

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v19-21-many-wives.step-001

- 动作：取出金星所落星座，核对它是否为双体星座、该星座主星是否入旺，并核对七宫主是否有力。
- 适用范围：仅限本命盘七宫（Yuvati）妻子数目主题；原文以「wives」立说，属男命框架；「its Lord」指金星所落双体星座的主星；原文只说 endowed with strength，未给强弱判准。
- 原文最小意思：金星落双体星座、其所落星座的主星入旺、且七宫主有力时，会有多位妻子。
- 本步骤产出事实：["多位妻子判定"]
- 所需事实：["本盘金星（Shukra）落在哪个星座", "金星（Shukra）是否落双体星座（Dual Rāśi）", "金星（Shukra）所落星座的主星是否入旺", "七宫主（Yuvati's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘金星（Shukra）落在哪个星座"}, {"fact_key": "金星（Shukra）是否落双体星座（Dual Rāśi）"}, {"fact_key": "金星（Shukra）所落星座的主星是否入旺"}, {"fact_key": "七宫主（Yuvati's Lord）是否有力"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断妻子的具体人数、婚期或婚姻质量。", "不得自行发明「有力」的判准。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘金星（Shukra）落在哪个星座、金星（Shukra）是否落双体星座（Dual Rāśi）、金星（Shukra）所落星座的主星是否入旺、七宫主（Yuvati's Lord）是否有力。
- 缺失即停字段：["本盘金星（Shukra）落在哪个星座", "金星（Shukra）是否落双体星座（Dual Rāśi）", "金星（Shukra）所落星座的主星是否入旺", "七宫主（Yuvati's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v19-21`｜PDF [34]｜“There will be many wives, if Shukra is in a Dual Rāśi, while its Lord is in exaltation, as Yuvati Lord is endowed with strength.”


## 四路查书计划

### 支持路

- There will be many wives, if Shukra is in a Dual Rāśi, while its Lord is in exaltation, as Yuvati Lord is endowed with strength
- 金星落双体星座 星座主星入旺 七宫主有力 多妻

### 反例或取消路

- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)
- If Yuvati Lord is devoid of strength and is relegated to Ari, 8th, or Vyaya the native’s wife will be destroyed

### 适用边界路

- If Yuvati Lord is in a Rashi of Shani, or of Shukra and be drishtied by a benefic, there will be many wives
- Conversely, if Yuvati Lord is in fall, or is combust, or is in an enemy’s Rāśi, one will acquire sick wives and many wives

### 判断方法路

- PLURALITY OF WIVES Shukra Dual Rāśi dispositor exaltation
- 判断妻子数目要看金星所落星座与其主星

## 上游问题

- 无

## 停止条件

- 缺少金星所落星座事实时停止。
- 缺少该星座主星是否入旺的事实时停止。
- 缺少七宫主强弱事实时停止（该判准待排盘窗口定义）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
