---
method: ch39-v43-lagn-uttamansa-four-drishtis
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升落 Uttamāńś 并受四颗以上行星（不含月亮）相照：成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 上升受多颗行星相照好不好
- 为什么月亮相照要排除

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 相照上升宫（Lagna）的行星有几颗
- 上升（Lagna）是否落 Uttamāńś
- 相照上升宫（Lagna）的行星是否不少于四颗
- 月亮（Chandra）是否相照上升宫（Lagna）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v43-lagn-uttamansa-four-drishtis.step-001

- 动作：核对上升（Lagn）是否落 Uttamāńś，数相照上升的行星是否不少于四颗，并确认其中不含月亮（Chandra）。
- 适用范围：仅限本命盘；原文没有时间限定。
- 原文最小意思：上升（Lagn）落 Uttamāńś，并受四颗或更多行星相照、其中不包括月亮（Chandra）时，命主会成为国王。
- 本步骤产出事实：["上升 Uttamāńś 受多照的贵格判定"]
- 所需事实：["相照上升宫（Lagna）的行星有几颗", "上升（Lagna）是否落 Uttamāńś", "相照上升宫（Lagna）的行星是否不少于四颗", "月亮（Chandra）是否相照上升宫（Lagna）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "相照上升宫（Lagna）的行星有几颗"}, {"fact_key": "上升（Lagna）是否落 Uttamāńś"}, {"fact_key": "相照上升宫（Lagna）的行星是否不少于四颗"}, {"operator": "NOT", "operands": [{"fact_key": "月亮（Chandra）是否相照上升宫（Lagna）"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文明确把月亮排除在这四颗之外，不得把月亮算进相照行星。", "原文没有限定相照的行星是吉是凶，不得自行加上吉星限定。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：相照上升宫（Lagna）的行星有几颗、上升（Lagna）是否落 Uttamāńś、相照上升宫（Lagna）的行星是否不少于四颗、月亮（Chandra）是否相照上升宫（Lagna）。
- 缺失即停字段：["相照上升宫（Lagna）的行星有几颗", "上升（Lagna）是否落 Uttamāńś", "相照上升宫（Lagna）的行星是否不少于四颗", "月亮（Chandra）是否相照上升宫（Lagna）"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v43`｜PDF [84]｜“One will become a king, if Lagn in Uttamāńś receives a Drishti from four, or more Grahas, out of which Chandra should not be one.”


## 四路查书计划

### 支持路

- One will become a king, if Lagn in Uttamāńś receives a Drishti from four, or more Grahas, out of which Chandra should not be one
- 上升 Uttamāńś 四颗行星相照 不含月亮 国王

### 反例或取消路

- One born in Kema Drum Yog will be very much reproached, will be bereft of intelligence, learning, reduced to penury and perils
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- In the Dasha Varg scheme the designations commence from Parijata etc., such as 2 good Vargas - Parijatha, 3 Uttama, 4 Gopur, 5 Simhasan
- This happens, when Lagn in the RashiKundali and the Navāńś Lagn are in the same Rāśi
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少上升 Uttamāńś 事实时停止。
- 缺少相照上升的行星计数事实时停止。
- 缺少月亮是否相照上升的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
