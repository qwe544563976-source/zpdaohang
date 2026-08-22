---
method: ch03-v11-benefics-and-malefics
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 自然吉凶星名册：六凶（含减光月）与其余为吉

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 哪些行星算凶星、哪些算吉星
- 月亮什么时候算凶星

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中的九曜（Grahas）分别是哪些行星
- 月亮（Chandra）是否为减光月（decreasing Chandra）

## 按情况检查的事实

- 无

## 依赖方法

- ch03-v10-names-of-the-nine-grahas

## 执行步骤

### ch03-v11-benefics-and-malefics.step-001

- 动作：把太阳（Surya）、土星（Shani）、火星（Mangal）、罗睺（Rahu）、计都（Ketu）判为凶星。
- 适用范围：第3章对九曜（『Among these』承接前条列出的九曜名单）的自然吉凶归类；原文此处未按上升、大运或昼夜限定。
- 原文最小意思：太阳（Surya）、土星（Shani）、火星（Mangal）、罗睺（Rahu）与计都（Ketu）为凶星。
- 本步骤产出事实：["固定凶星名册判定"]
- 所需事实：["本盘中的九曜（Grahas）分别是哪些行星"]
- 条件关系：{"fact_key": "本盘中的九曜（Grahas）分别是哪些行星"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把本条的自然凶星身份当成按上升定的功能凶星——原文此处没有按上升限定。", "不得据凶星身份直接推出任何具体的吉凶事件或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中的九曜（Grahas）分别是哪些行星。
- 缺失即停字段：["本盘中的九曜（Grahas）分别是哪些行星"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v11`｜PDF [9]｜“Among these, Surya, Shani, Mangal”
  - `bphs-97:santhanam:ch03:v11`｜PDF [9]｜“Rahu and Ketu”
  - `bphs-97:santhanam:ch03:v11`｜PDF [9]｜“are malefics”

### ch03-v11-benefics-and-malefics.step-002

- 动作：核对月亮（Chandra）是否为减光月；是减光月则判为凶星。
- 适用范围：第3章自然吉凶归类中对月亮（Chandra）的限定；原文只说 decreasing（减光），未给盈亏门槛或度数界线。
- 原文最小意思：减光的月亮（decreasing Chandra）为凶星。
- 本步骤产出事实：["减光月（Chandra）凶星身份判定"]
- 所需事实：["月亮（Chandra）是否为减光月（decreasing Chandra）"]
- 条件关系：{"fact_key": "月亮（Chandra）是否为减光月（decreasing Chandra）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替『decreasing』（减光）选定某一种盈亏门槛、度数界线或与太阳的距角范围——原文此处未给界定。", "不得反推出增光的月亮（Chandra）一定为吉星，本步只写了减光这一侧。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否为减光月（decreasing Chandra）。
- 缺失即停字段：["月亮（Chandra）是否为减光月（decreasing Chandra）"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v11`｜PDF [9]｜“decreasing Chandra”
  - `bphs-97:santhanam:ch03:v11`｜PDF [9]｜“are malefics”

### ch03-v11-benefics-and-malefics.step-003

- 动作：把上列凶星之外的其余行星判为吉星。
- 适用范围：第3章自然吉凶归类的另一侧；『the rest』指的是前条列出的九曜中未被列为凶星者，原文未按上升限定。
- 原文最小意思：其余的行星为吉星。
- 本步骤产出事实：["吉星名册判定"]
- 所需事实：["固定凶星名册判定", "减光月（Chandra）凶星身份判定"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "固定凶星名册判定"}, {"fact_key": "减光月（Chandra）凶星身份判定"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『其余』扩大到九曜以外的任何天体——『these』指的是前条列出的九曜。", "不得据吉星身份直接推出任何具体的吉凶事件或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：固定凶星名册判定、减光月（Chandra）凶星身份判定。
- 缺失即停字段：["固定凶星名册判定", "减光月（Chandra）凶星身份判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v11`｜PDF [9]｜“while the rest are benefics”


## 四路查书计划

### 支持路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu are malefics, while the rest are benefics
- Benefics and Malefics 凶星 吉星 减光月 Chandra Rahu Ketu

### 反例或取消路

- Natural Benefics and Malefics Guru and Shukra are benefics, while Chandra is mediocre in benefice and Budh is neutral
- Malefics are Surya, Shani and Mangal 第34章 另一份自然吉凶名册

### 适用边界路

- Grahas and Kark Lagn Shukra and Budh are malefics 按上升定的功能吉凶
- Paksh Bal Deduct from Chandra’s longitude that of Surya 月亮盈亏与力量

### 判断方法路

- decreasing Chandra is in Tanu Bhava, while malefics capture Randhr Bhava and a Kendra 减光月在断语里怎么用
- No benefic shall be yuti with the said malefics 吉星凶星在断语中的用法

## 上游问题

- 无

## 停止条件

- 缺少「月亮（Chandra）是否为减光月（decreasing Chandra）」时，吉星名册停判。
- 『decreasing』（减光）本条未给界定门槛，取值不确定即停判，不得自行选定盈亏算法。
- 本条只给自然吉凶，未按上升给功能吉凶；要按上升定吉凶须另找原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
