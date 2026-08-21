---
method: ch16-v1-3-lords-yuti-bhava-quality
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 得子早晚与缺陷：五宫主与上升主同宫所落宫位的吉凶

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我什么时候能有孩子
- 我在孩子这件事上会不会出岔子

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫主是否与上升主同宫
- 五宫主与上升主同宫之处是否为吉宫
- 五宫主与上升主同宫之处是否为凶宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch16-v1-3-lords-yuti-bhava-quality.step-001

- 动作：核对五宫主是否与上升主同宫，并确认该同宫之处是否为吉宫。
- 适用范围：仅限本命盘五宫子女主题；原文只说吉宫同宫，未给具体年龄、年份或子女人数。
- 原文最小意思：五宫主与上升主在吉宫同宫时，能较早得到子女，并因子女获得幸福。
- 本步骤产出事实：["两主吉宫同宫早得子判定"]
- 所需事实：["五宫主是否与上升主同宫", "五宫主与上升主同宫之处是否为吉宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫主是否与上升主同宫"}, {"fact_key": "五宫主与上升主同宫之处是否为吉宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把“较早”写成具体年龄或年份。", "不得据此推断子女人数或性别。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否与上升主同宫、五宫主与上升主同宫之处是否为吉宫。
- 缺失即停字段：["五宫主是否与上升主同宫", "五宫主与上升主同宫之处是否为吉宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v1-3`｜PDF [30]｜“The Yuti of Putr’s Lord with Lagn’s Lord in a good Bhava will ensure early obtainment of children apart from happiness through them.”

### ch16-v1-3-lords-yuti-bhava-quality.step-002

- 动作：在同一组两主同宫的前提下，核对该同宫之处是否为凶宫。
- 适用范围：仅限本命盘五宫子女主题；原文只说凶宫同宫会成为缺陷，未说明缺陷的具体形式。
- 原文最小意思：五宫主与上升主在凶宫同宫时，在子女方面会有缺陷。
- 本步骤产出事实：["两主凶宫同宫子女缺陷判定"]
- 所需事实：["五宫主是否与上升主同宫", "五宫主与上升主同宫之处是否为凶宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫主是否与上升主同宫"}, {"fact_key": "五宫主与上升主同宫之处是否为凶宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把原文的“缺陷”坐实成无子、去世或疾病。", "不得据此推断缺陷出现的时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否与上升主同宫、五宫主与上升主同宫之处是否为凶宫。
- 缺失即停字段：["五宫主是否与上升主同宫", "五宫主与上升主同宫之处是否为凶宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v1-3`｜PDF [30]｜“The Yuti of Putr’s Lord with Lagn’s Lord in a good Bhava will ensure early obtainment of children apart from happiness through them. If they join in an evil Bhava, they will prove a defect in this respect.”


## 四路查书计划

### 支持路

- 五宫主 上升主 同宫 吉宫 早得子

### 反例或取消路

- 两主落凶宫同宫 子女有缺陷

### 适用边界路

- 吉宫与凶宫在这条同宫规则中的界定

### 判断方法路

- 怎样判断五宫主与上升主同宫

## 上游问题

- 无

## 停止条件

- 缺少两主是否同宫的事实时停止。
- 缺少同宫之处吉凶属性的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
