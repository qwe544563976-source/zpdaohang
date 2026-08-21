---
method: ch16-v24-32-successive-loss-of-children
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 长寿而子女相继去世：五宫凶星、木土同落五宫、上升主落二宫、五宫主与火星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的孩子会不会养不活
- 我子女缘为什么这么坎坷

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫是否被凶星占据
- 木星是否与土星同落五宫
- 上升主是否落二宫
- 五宫主是否与火星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch16-v24-32-successive-loss-of-children.step-001

- 动作：核对五宫凶星占据、木星与土星是否同落五宫、上升主是否落二宫、五宫主是否与火星同宫，判断本人寿命与子女存殁。
- 适用范围：仅限本命五宫子女存殁与本人寿长主题；原文未给年龄、时间或上升限定。
- 原文最小意思：五宫被凶星占据、木星与土星同落五宫、上升主落二宫、五宫主与火星同宫时，此人长寿，但子女一个接一个出生后去世。
- 本步骤产出事实：["长寿而子女相继去世判定"]
- 所需事实：["五宫是否被凶星占据", "木星是否与土星同落五宫", "上升主是否落二宫", "五宫主是否与火星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫是否被凶星占据"}, {"fact_key": "木星是否与土星同落五宫"}, {"fact_key": "上升主是否落二宫"}, {"fact_key": "五宫主是否与火星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断子女去世的年龄、数量或原因。", "不得把长寿写成具体寿数。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫是否被凶星占据、木星是否与土星同落五宫、上升主是否落二宫、五宫主是否与火星同宫。
- 缺失即停字段：["五宫是否被凶星占据", "木星是否与土星同落五宫", "上升主是否落二宫", "五宫主是否与火星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v24-32`｜PDF [31, 32]｜“Should Putr be occupied by a malefic, while Guru is yuti with Shani in Putr Bhava, as Lagn’s Lord is in Dhan Bhava and Putr’s Lord is yuti with Mangal, one will live long, but lose his children one after the other, as they are born.”


## 四路查书计划

### 支持路

- Guru yuti with Shani in Putr Bhava lose his children one after the other
- 五宫凶星 木星土星同落五宫 火星与五宫主 子女相继去世

### 反例或取消路

- 五宫得吉星保护 子女得以存活

### 适用边界路

- 长寿而子女去世断语的适用边界

### 判断方法路

- 判断子女能否存活要看哪些组合

## 上游问题

- 无

## 停止条件

- 缺少五宫占据者事实时停止。
- 缺少木星与土星落宫事实时停止。
- 缺少上升主与五宫主的落宫和同宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
