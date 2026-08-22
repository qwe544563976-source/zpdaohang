---
method: ch09-v24-benefics-drishti-chandra-good-to-mother
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 吉星相照月亮：给母亲带来好处

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 吉星照月亮对母亲有什么好处
- 母亲的吉象怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 月亮（Chandra）是否受吉星相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch09-v24-benefics-drishti-chandra-good-to-mother.step-001

- 动作：核对月亮是否受吉星相照，判断母亲的吉象。
- 适用范围：仅限本命盘对母亲的判断；原文这一句只说带来好处，不给好处的具体内容。
- 原文最小意思：吉星相照月亮（Chandra）时，会给母亲带来好处。
- 本步骤产出事实：["月亮受吉照的母亲吉象判定"]
- 所需事实：["月亮（Chandra）是否受吉星相照"]
- 条件关系：{"fact_key": "月亮（Chandra）是否受吉星相照"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把『好处』补成原文没写的具体内容（寿命、财富或健康）。", "不得据本句断定前一句的凶象一定被抵消——原文没有这样说。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）是否受吉星相照。
- 缺失即停字段：["月亮（Chandra）是否受吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch09:v24`｜PDF [23]｜“Benefics, giving a Drishti to Chandra, will bring good to the mother.”


## 四路查书计划

### 支持路

- Benefics, giving a Drishti to Chandra, will bring good to the mother.
- 吉星相照月亮 母亲 吉

### 反例或取消路

- The mother of the native will incur evils (will die soon), if Chandra at birth receives a Drishti from three malefics

### 适用边界路

- Evils to Mother (up to Sloka 33)
- The stronger among Surya and Shukra indicates the father, while the stronger among Chandra and Mangal indicates the mother.
- Evils, causing premature end, exist up to the 24<sup>th</sup> year of one’s age. As such, no definite calculation of life span should be made till such year of age.

### 判断方法路

- Evils at Birth
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Those are the evils (due to a native). I now narrate the antidotes for such evils as well, which will be helpful to assess the extent of inauspiciousness.
- 母亲用哪颗星看

## 上游问题

- 无

## 停止条件

- 缺少月亮所受相照事实时停止。
- 吉星与凶星的名册未定时停止（判准见第 3 章 Benefics and Malefics）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
