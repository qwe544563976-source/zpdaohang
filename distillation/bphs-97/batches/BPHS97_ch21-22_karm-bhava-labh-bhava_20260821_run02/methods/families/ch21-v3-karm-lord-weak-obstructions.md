---
method: ch21-v3-karm-lord-weak-obstructions
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 工作上的阻碍：十宫主没有力量

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我做事为什么总是受阻
- 我的事业顺不顺

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否有力

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v3-karm-lord-weak-obstructions.step-001

- 动作：核对十宫主（Karm's Lord）是否有力，若没有力量则判为工作上会遇到阻碍。
- 适用范围：仅限本命盘十宫（Karm Bhava）的工作阻碍主题；「没有力量」按原文 devoid of strength 接线，判准原文本句未给；原文未给时间限定。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：十宫主没有力量时，命主在工作上会遇到阻碍。
- 本步骤产出事实：["十宫主无力的工作阻碍判定"]
- 所需事实：["十宫主（Karm's Lord）是否有力"]
- 条件关系：{"operator": "NOT", "operands": [{"fact_key": "十宫主（Karm's Lord）是否有力"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断失业、破产或阻碍出现的年份。", "原文本句没有给出力量的判准，不得自行发明力量算法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否有力。
- 缺失即停字段：["十宫主（Karm's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v3`｜PDF [38]｜“If Karm’s Lord is devoid of strength, the native will face obstructions in his work.”


## 四路查书计划

### 支持路

- If Karm’s Lord is devoid of strength, the native will face obstructions in his work
- 十宫主 无力 工作 阻碍

### 反例或取消路

- If Karm’s Lord is strong and in exaltation, or in its own Rāśi/Navāńś, the native will derive extreme paternal happiness
- If Karm’s Lord is with a benefic, or be in an auspicious Bhava, one will always gain through royal patronage and in business
- 十宫主有力 王室恩宠 生意得利

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava
- If Karm’s Lord is in Randhr Bhava, the native will be devoid of acts, long-lived and intent on blaming others

### 判断方法路

- Effects of Karm’s Lord in Various Bhavas
- 判断事业阻碍要先看十宫主的力量

## 上游问题

- 无

## 停止条件

- 缺少十宫主力量事实时停止。
- 力量判准由排盘窗口定义，未给出取值时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
