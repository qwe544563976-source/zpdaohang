---
method: ch03-v11-budh-joins-a-malefic
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 水星（Budh）与凶星同宫时转为凶星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 水星什么时候变成凶星
- 我盘里的水星算吉星还是凶星

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 水星（Budh）是否与凶星同宫

## 按情况检查的事实

- 无

## 依赖方法

- ch03-v11-benefics-and-malefics

## 执行步骤

### ch03-v11-budh-joins-a-malefic.step-001

- 动作：核对水星（Budh）是否与凶星同宫；同宫则判为凶星。
- 适用范围：第3章自然吉凶归类中对水星（Budh）的专门规定；原文未按上升、大运或昼夜限定。
- 原文最小意思：水星（Budh）若与凶星同宫，即为凶星。
- 本步骤产出事实：["水星（Budh）吉凶身份判定"]
- 所需事实：["水星（Budh）是否与凶星同宫"]
- 条件关系：{"fact_key": "水星（Budh）是否与凶星同宫"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『joins a malefic』扩大成受凶星相照（Drishti）或被凶星夹——原文只说与凶星会合同宫。", "不得反推出水星（Budh）与吉星同宫即为吉星——原文此处只写了与凶星同宫这一侧。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：水星（Budh）是否与凶星同宫。
- 缺失即停字段：["水星（Budh）是否与凶星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v11`｜PDF [9]｜“Budh, however, is a malefic, if he joins a malefic.”


## 四路查书计划

### 支持路

- Budh, however, is a malefic, if he joins a malefic
- 水星 Budh 与凶星同宫 转为凶星

### 反例或取消路

- Budh is neutral (a benefic, when associated with a benefic and a malefic, when related to a malefic)
- If waning Chandra and Budh are together, both are benefics

### 适用边界路

- Grahas and Simh Lagn Budh, Shukra and Shani are malefics 按上升定的水星吉凶
- As regards Budh, we have clear instructions from Maharishi Parashar, that he becomes a malefic, if he joins a malefic

### 判断方法路

- If Budh is associated with a malefic, there will be during his Dasha punishment by Government
- Budh be associated with a malefic, or malefics in Ari, in Randhr, or in Vyaya 水星与凶星相关的断语

## 上游问题

- 无

## 停止条件

- 缺少「水星（Budh）是否与凶星同宫」时停止。
- 凶星名册未定时停止：凶星由 ch03:v11 的自然吉凶星名册方法给出。
- 原文只说『joins』（会合同宫），若排盘对会合的取值范围不确定则停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
