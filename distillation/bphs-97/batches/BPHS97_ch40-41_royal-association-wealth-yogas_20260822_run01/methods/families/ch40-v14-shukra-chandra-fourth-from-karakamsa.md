---
method: ch40-v14-shukra-chandra-fourth-from-karakamsa
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 得王家徽记：金星与月亮同落 Karakāńś 起第 4 位

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有那种体面的名分
- 我身上会不会带官家的标记

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Karakāńś 落在哪个星座
- 金星（Shukra）是否落 Karakāńś 起第 4 宫
- 月亮（Chandra）是否落 Karakāńś 起第 4 宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch40-v14-shukra-chandra-fourth-from-karakamsa.step-001

- 动作：先取 Karakāńś，再核对金星（Shukra）与月亮（Chandra）是否都落在 Karakāńś 起第 4 位。
- 适用范围：仅限本命盘以 Karakāńś Lagna 起算的第 4 位；Karakāńś 的取法本偈未给，须另按本书第 33 章「Karakāńś 是 Atma Karak 所落的九分盘（Navāńś）」取得；原文未给时间限定。
- 原文最小意思：金星（Shukra）与月亮（Chandra）同落 Karakāńś Lagna 起第 4 位时，命主将得王家徽记。
- 本步骤产出事实：["金星月亮同居 Karakāńś 第四位的王家徽记判定"]
- 所需事实：["本盘的 Karakāńś 落在哪个星座", "金星（Shukra）是否落 Karakāńś 起第 4 宫", "月亮（Chandra）是否落 Karakāńś 起第 4 宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘的 Karakāńś 落在哪个星座"}, {"fact_key": "金星（Shukra）是否落 Karakāńś 起第 4 宫"}, {"fact_key": "月亮（Chandra）是否落 Karakāńś 起第 4 宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文要求两颗行星同落第 4 位，不得只有其中一颗就下断。", "不得据此推断徽记的形式、授予者或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Karakāńś 落在哪个星座、金星（Shukra）是否落 Karakāńś 起第 4 宫、月亮（Chandra）是否落 Karakāńś 起第 4 宫。
- 缺失即停字段：["本盘的 Karakāńś 落在哪个星座", "金星（Shukra）是否落 Karakāńś 起第 4 宫", "月亮（Chandra）是否落 Karakāńś 起第 4 宫"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v14`｜PDF [85]｜“If Shukra and Chandra are in the 4<sup>th</sup> from Karakāńś Lagna, the native will be endowed with royal insignia.”


## 四路查书计划

### 支持路

- If Shukra and Chandra are in the 4<sup>th</sup> from Karakāńś Lagna, the native will be endowed with royal insignia
- 金星月亮落 Karakāńś 第四位 王家徽记

### 反例或取消路

- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- Karakāńś is the Navāńś, occupied by the Atma Karak Grah

### 判断方法路

- Yogas For Royal Association
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- Karakāńś 未按本书第 33 章的界定取到时停止。
- 金星或月亮的落位事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
