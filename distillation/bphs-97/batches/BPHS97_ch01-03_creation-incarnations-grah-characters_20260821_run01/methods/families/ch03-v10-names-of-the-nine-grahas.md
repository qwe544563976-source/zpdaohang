---
method: ch03-v10-names-of-the-nine-grahas
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 九曜名单（Names of Grahas）

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 本书说的九曜到底是哪九颗
- 罗睺、计都算不算行星

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中的九曜（Grahas）分别是哪些行星

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v10-names-of-the-nine-grahas.step-001

- 动作：取本书所论的九曜名单，作为后续吉凶归类与所主人事的对象。
- 适用范围：第3章给出的九曜名单；本条只给名称与次序，未给吉凶、强弱或所主人事。
- 原文最小意思：九曜（nine Grahas）依次为太阳（Surya）、月亮（Chandra）、火星（Mangal）、水星（Budh）、木星（Guru）、金星（Shukr）、土星（Shani）、罗睺（Rahu）、计都（Ketu）。
- 本步骤产出事实：["九曜名单判定"]
- 所需事实：["本盘中的九曜（Grahas）分别是哪些行星"]
- 条件关系：{"fact_key": "本盘中的九曜（Grahas）分别是哪些行星"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出九曜的吉凶、强弱或所主人事——本条只给名称与次序。", "不得把本名单扩充到 Mandi、Gulik 等本条未列的天体。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中的九曜（Grahas）分别是哪些行星。
- 缺失即停字段：["本盘中的九曜（Grahas）分别是哪些行星"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v10`｜PDF [9]｜“The names of the nine Grahas, respectively, are Surya, Chandra, Mangal, Budh, Guru, Shukr, Shani, Rahu and Ketu.”


## 四路查书计划

### 支持路

- The names of the nine Grahas, respectively, are Surya, Chandra, Mangal, Budh, Guru, Shukr, Shani, Rahu and Ketu
- Names of Grahas 九曜 名单 次序

### 反例或取消路

- I now detail below Atma Karak etc., obtainable from among the 7 Grahas, viz. Surya to Shani
- Gulik’s Position The degree, ascending at the time of start of Gulik’s portion 名单之外的影曜

### 适用边界路

- Those are called ‘Grahas’, that move through the Nakshatraas (or stellar mansions) in the zodiac
- Rahu and Ketu (the ascending and the descending nodes of Chandra) 交点算不算行星

### 判断方法路

- Grah governances Surya is the soul of all 拿到九曜名单之后怎么用

## 上游问题

- 无

## 停止条件

- 缺少本盘九曜（Grahas）名单时停止。
- 本条只给名称与次序，没有任何吉凶结果；要下断语必须另找原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
