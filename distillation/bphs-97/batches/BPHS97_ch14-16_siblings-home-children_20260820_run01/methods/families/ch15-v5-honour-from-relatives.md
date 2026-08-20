---
method: ch15-v5-honour-from-relatives
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 受亲属尊敬：水星落上升且四宫主为吉星并受吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我在亲戚里有没有地位
- 我和亲属关系好不好

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 水星（Budh）是否落上升（Lagna）
- 四宫主（Bandhu’s Lord）本身是否为吉星
- 四宫主（Bandhu’s Lord）是否受另一颗吉星相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch15-v5-honour-from-relatives.step-001

- 动作：同时核对水星是否落上升、四宫主是否为吉星、以及四宫主是否受另一吉星相照。
- 适用范围：仅限本命盘中亲属尊敬这一结果；原文未给时间限定。
- 原文最小意思：水星（Budh）落上升（Lagna）、四宫主（Bandhu’s Lord）本身是吉星、并受另一吉星相照时，命主将受亲属尊敬。
- 本步骤产出事实：["受亲属尊敬判定"]
- 所需事实：["水星（Budh）是否落上升（Lagna）", "四宫主（Bandhu’s Lord）本身是否为吉星", "四宫主（Bandhu’s Lord）是否受另一颗吉星相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落上升（Lagna）"}, {"fact_key": "四宫主（Bandhu’s Lord）本身是否为吉星"}, {"fact_key": "四宫主（Bandhu’s Lord）是否受另一颗吉星相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断亲属人数、亲属身份或来往时间。", "三个条件缺一不可，不得只凭其中一条下结论。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：水星（Budh）是否落上升（Lagna）、四宫主（Bandhu’s Lord）本身是否为吉星、四宫主（Bandhu’s Lord）是否受另一颗吉星相照。
- 缺失即停字段：["水星（Budh）是否落上升（Lagna）", "四宫主（Bandhu’s Lord）本身是否为吉星", "四宫主（Bandhu’s Lord）是否受另一颗吉星相照"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v5`｜PDF [29]｜“Should Budh be in Lagna, while Bandhu’s Lord, being a benefic, is drishtied by another benefic, the native will be honoured by his relatives.”


## 四路查书计划

### 支持路

- Budh in Lagna Bandhu’s Lord benefic drishti honoured by relatives
- 水星落上升 四宫主吉星 受亲属尊敬

### 反例或取消路

- Bandhu’s Lord malefic quarrels with relatives
- 四宫主为凶星 与亲属不和

### 适用边界路

- which relatives are meant by Bandhu Bhava
- 亲属尊敬这一断语的适用边界

### 判断方法路

- how to judge relations with relatives in BPHS
- 判断亲属关系要查哪些条件

## 上游问题

- 无

## 停止条件

- 缺少水星落宫事实时停止。
- 缺少四宫主吉凶属性或相位事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
