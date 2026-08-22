---
method: ch08-v4-5-graha-in-drishtied-rashi-also-receives
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 落在受照星座里的行星，同时也受该相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 受相照的星座里的行星算不算被照到
- 行星什么时候算受到星座相照

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 待判行星（Grah）所落星座（Rāśi）是否受到某个相照（Drishti）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch08-v4-5-graha-in-drishtied-rashi-also-receives.step-001

- 动作：核对待判行星所落星座是否正在受某个相照，若是则该行星同时也受这一相照。
- 适用范围：仅限第 8 章星座相照体系；本句只说相照及于其中的行星，不给吉凶断语。
- 原文最小意思：落在受相照星座（Rāśi）里的行星（Grah），同时也受到该相照（Drishti）。
- 本步骤产出事实：["待判行星（Grah）是否同时受到该星座所受的相照（Drishti）"]
- 所需事实：["待判行星（Grah）所落星座（Rāśi）是否受到某个相照（Drishti）"]
- 条件关系：{"fact_key": "待判行星（Grah）所落星座（Rāśi）是否受到某个相照（Drishti）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本句判断这一相照是吉是凶——本句只说相照及于其中的行星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：待判行星（Grah）所落星座（Rāśi）是否受到某个相照（Drishti）。
- 缺失即停字段：["待判行星（Grah）所落星座（Rāśi）是否受到某个相照（Drishti）"]
- 原文证据：
  - `bphs-97:santhanam:ch08:v4-5`｜PDF [22]｜“Simultaneously a Grah in the Rāśi, that receives a Drishti, is also subjected to the Drishti concerned.”


## 四路查书计划

### 支持路

- Simultaneously a Grah in the Rāśi, that receives a Drishti, is also subjected to the Drishti concerned
- 受照星座内的行星 同时受照

### 反例或取消路

- 无

### 适用边界路

- O Brahmin, I have earlier stated Drishtis, based on Rāśis. The other kind is between Grahas, which I detail below.
- 行星自身的相照另有一套

### 判断方法路

- Drishtis of the Rāśis
- Dristhis of the Grahas
- 星座相照怎么落到行星身上

## 上游问题

- 无

## 停止条件

- 未指明要判哪一颗行星（Grah）时停止。
- 缺少该行星所落星座（Rāśi）是否受相照的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
