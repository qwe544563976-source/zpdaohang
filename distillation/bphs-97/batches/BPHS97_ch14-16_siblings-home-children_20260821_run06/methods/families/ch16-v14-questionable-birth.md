---
method: ch16-v14-questionable-birth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 子女出身可疑：五宫主落动星座、土星落五宫、罗睺与月亮同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我孩子的出身会不会有争议
- 我的子女宫有没有出身方面的隐患

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫主是否落动星座
- 土星是否落五宫
- 罗睺是否与月亮同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch16-v14-questionable-birth.step-001

- 动作：核对五宫主所落星座性质、土星是否落五宫、罗睺是否与月亮同宫，判断所生子女的出身是否可疑。
- 适用范围：仅限本命五宫子女出身主题；原文未给上升、时间或大运限定。
- 原文最小意思：五宫主落动星座、土星落五宫、罗睺与月亮同宫时，所生子女出身可疑。
- 本步骤产出事实：["子女出身可疑判定"]
- 所需事实：["五宫主是否落动星座", "土星是否落五宫", "罗睺是否与月亮同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫主是否落动星座"}, {"fact_key": "土星是否落五宫"}, {"fact_key": "罗睺是否与月亮同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断子女数量、性别或出生时间。", "不得把子女出身可疑扩大成对父母品行的断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否落动星座、土星是否落五宫、罗睺是否与月亮同宫。
- 缺失即停字段：["五宫主是否落动星座", "土星是否落五宫", "罗睺是否与月亮同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v14`｜PDF [31]｜“If Putr’s Lord is in a Movable Rāśi, while Shani is in Putr, as Rahu is with Chandra, the child (so born) is of questionable birth.”


## 四路查书计划

### 支持路

- 五宫主落动星座 土星落五宫 罗睺月亮同宫 出身可疑

### 反例或取消路

- 五宫受吉星 子女出身可疑被取消

### 适用边界路

- 子女出身可疑断语的适用边界

### 判断方法路

- 判断子女出身要检查哪些因素

## 上游问题

- 无

## 停止条件

- 缺少五宫主所落星座性质事实时停止。
- 缺少土星落宫事实时停止。
- 缺少罗睺与月亮同宫关系事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
