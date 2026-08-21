---
method: ch17-v28-fear-from-dogs
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 怕狗：上升主与六宫主互换宫位，第10年与第19年

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会被狗吓到或被狗咬
- 我哪一年容易有动物方面的惊险

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否与六宫主（Ari's Lord）互换宫位

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v28-fear-from-dogs.step-001

- 动作：核对上升主（Lagn's Lord）与六宫主（Ari's Lord）是否互换宫位，判断怕狗之事。
- 适用范围：仅限本命盘六宫（Ari）灾厄主题；原文只把结果系在第10年与第19年，未给其他年份。
- 原文最小意思：上升主与六宫主互换宫位时，第10年与第19年会有来自狗的恐惧。
- 本步骤产出事实：["上升主与六宫主互换主怕狗判定"]
- 所需事实：["上升主（Lagn's Lord）是否与六宫主（Ari's Lord）互换宫位"]
- 条件关系：{"fact_key": "上升主（Lagn's Lord）是否与六宫主（Ari's Lord）互换宫位"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断被咬伤的程度、部位或其他动物的灾厄。", "不得把第10年与第19年之外的年份也算进本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否与六宫主（Ari's Lord）互换宫位。
- 缺失即停字段：["上升主（Lagn's Lord）是否与六宫主（Ari's Lord）互换宫位"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v28`｜PDF [33]｜“There will be fear from dogs during the 10<sup>th</sup> and 19<sup>th</sup> year, if the Lagna Lord and the 6<sup>th</sup> Lord are in exchange.”


## 四路查书计划

### 支持路

- 上升主与六宫主互换宫位 怕狗 第10年 第19年

### 反例或取消路

- 无

### 适用边界路

- 无

### 判断方法路

- 判断六宫（Ari）灾厄应检查什么

## 上游问题

- 无

## 停止条件

- 缺少上升主与六宫主是否互换宫位的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
