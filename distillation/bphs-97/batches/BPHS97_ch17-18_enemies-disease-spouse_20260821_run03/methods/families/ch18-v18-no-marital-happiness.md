---
method: ch18-v18-no-marital-happiness
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 没有婚姻幸福：月亮落七宫、七宫主落十二宫、指示星金星无力

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的婚姻会不会幸福
- 月亮落七宫又七宫主落十二宫会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否落七宫（Yuvati）
- 七宫主（Yuvati's Lord）是否落十二宫（Vyaya）
- 金星（Shukra）是否有力

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v18-no-marital-happiness.step-001

- 动作：同时核对月亮是否落七宫、七宫主是否落十二宫、以及原文点名的指示星金星（Shukr）是否无力。
- 适用范围：仅限本命盘七宫（Yuvati）婚姻幸福主题；原文把 Karaka（指示星）明写为金星（Shukr）；原文只说 bereft of strength，未给强弱判准；三个条件在原文里是同时成立的合取。
- 原文最小意思：月亮落七宫、七宫主落十二宫、且作为指示星的金星无力时，命主不会有婚姻幸福。
- 本步骤产出事实：["婚姻幸福缺失判定"]
- 所需事实：["月亮（Chandra）是否落七宫（Yuvati）", "七宫主（Yuvati's Lord）是否落十二宫（Vyaya）", "金星（Shukra）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "月亮（Chandra）是否落七宫（Yuvati）"}, {"fact_key": "七宫主（Yuvati's Lord）是否落十二宫（Vyaya）"}, {"operator": "NOT", "operands": [{"fact_key": "金星（Shukra）是否有力"}]}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断离异、丧偶或婚姻次数。", "不得自行发明「无力」的判准。", "不得把三个条件拆成任一成立即可。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否落七宫（Yuvati）、七宫主（Yuvati's Lord）是否落十二宫（Vyaya）、金星（Shukra）是否有力。
- 缺失即停字段：["月亮（Chandra）是否落七宫（Yuvati）", "七宫主（Yuvati's Lord）是否落十二宫（Vyaya）", "金星（Shukra）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v18`｜PDF [34]｜“If Chandra is in Yuvati, as Yuvati Lord is in Vyaya and the Karaka (indicator Shukr) is bereft of strength, the native will not be endowed with marital happiness.”


## 四路查书计划

### 支持路

- If Chandra is in Yuvati, as Yuvati Lord is in Vyaya and the Karaka (indicator Shukr) is bereft of strength
- 月亮落七宫 七宫主落十二宫 金星无力 没有婚姻幸福

### 反例或取消路

- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)
- The native will beget a spouse endowed with (the seven principal) virtues, who will expand his dynasty by sons and grandsons

### 适用边界路

- If Yuvati Bhava, or its Lord is yuti with a malefic the native’s wife will incur evils, especially, if bereft of strength
- Malefics in Vyaya and 7th, while decreasing Chandra is in Putr the native will be controlled by spouse
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- LACK OF CONJUGAL FELICITY Karaka Shukr 7th lord judgment
- 判断婚姻幸福要看月亮、七宫主与指示星金星

## 上游问题

- 无

## 停止条件

- 缺少月亮落宫事实时停止。
- 缺少七宫主落宫事实时停止。
- 缺少金星强弱事实时停止（该判准待排盘窗口定义）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
