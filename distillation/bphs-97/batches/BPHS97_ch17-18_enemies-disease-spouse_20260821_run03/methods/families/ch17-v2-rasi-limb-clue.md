---
method: ch17-v2-rasi-limb-clue
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 受累肢体的线索：成为六宫的那个星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身上的疮或伤会出现在哪个部位
- 六宫怎么看受影响的身体部位

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘六宫（Ari Bhava）落在哪个星座

## 按情况检查的事实

- 无

## 依赖方法

- ch17-v2-ari-lord-ulcers

## 执行步骤

### ch17-v2-rasi-limb-clue.step-001

- 动作：取成为六宫（Ari Bhava）的星座，据以得知受累的肢体。
- 适用范围：仅限承接同偈前句的溃疡瘀伤结论；原文只说由星座得知肢体，未给具体星座与肢体的对照表。
- 原文最小意思：成为六宫的星座，可据以得知所涉肢体。
- 本步骤产出事实：["六宫星座对应受累肢体判定"]
- 所需事实：["本盘六宫（Ari Bhava）落在哪个星座"]
- 条件关系：{"fact_key": "本盘六宫（Ari Bhava）落在哪个星座"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得在本条内自行补出星座与肢体的对照表。", "不得据此推断病症种类或发生时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘六宫（Ari Bhava）落在哪个星座。
- 缺失即停字段：["本盘六宫（Ari Bhava）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v2`｜PDF [32]｜“The Rāśi, becoming Ari Bhava, will lead to the knowledge of the concerned limb.”


## 四路查书计划

### 支持路

- The Rāśi, becoming Ari Bhava, will lead to the knowledge of the concerned limb
- 六宫星座 受累肢体

### 反例或取消路

- The limb, related to a benefic, will have a mark (like moles etc)
- 吉星所属部位只是痣记不是溃疡

### 适用边界路

- Limbs of Kaal Purush 12 Rāśis head face arms heart stomach
- Decanates and Bodily Limbs head eyes ears nose temple chin
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- clues to know of ulcers, identity marks etc. on one’s person
- 如何由星座与分盘定身体部位

## 上游问题

- 无

## 停止条件

- 缺少六宫所在星座事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
