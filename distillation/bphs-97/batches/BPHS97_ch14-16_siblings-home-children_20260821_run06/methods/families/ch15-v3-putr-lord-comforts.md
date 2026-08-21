---
method: ch15-v3-putr-lord-comforts
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 土地车乘房屋与乐器之乐：五宫主落本宫、本分盘或入旺

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有房有车
- 我这辈子物质享受怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫主（Putr’s Lord）是哪一颗行星

## 按情况检查的事实

- 五宫主（Putr’s Lord）是否落在自己的宫
- 五宫主（Putr’s Lord）是否落在自己的 Navāńś
- 五宫主（Putr’s Lord）是否入旺

## 依赖方法

- 无

## 执行步骤

### ch15-v3-putr-lord-comforts.step-001

- 动作：先定出五宫主（Putr’s Lord）是哪一颗行星，再核对它是否落本宫、落本 Navāńś 或入旺。
- 适用范围：仅限原文列出的五宫主三种状态与土地车乘房屋乐器之乐；原文未给时间限定。
- 原文最小意思：五宫主（Putr’s Lord）落自己的宫、落自己的 Navāńś、或入旺时，命主享有土地、车乘、房屋等以及乐器方面的舒适。
- 本步骤产出事实：["五宫主带来的土地车乘房屋乐器舒适判定"]
- 所需事实：["五宫主（Putr’s Lord）是哪一颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫主（Putr’s Lord）是哪一颗行星"}, {"operator": "OR", "operands": [{"fact_key": "五宫主（Putr’s Lord）是否落在自己的宫"}, {"fact_key": "五宫主（Putr’s Lord）是否落在自己的 Navāńś"}, {"fact_key": "五宫主（Putr’s Lord）是否入旺"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "五宫主（Putr’s Lord）是哪一颗行星"}, "required_fact_keys": ["五宫主（Putr’s Lord）是否落在自己的宫"], "branch_condition_logic": {"fact_key": "五宫主（Putr’s Lord）是否落在自己的宫"}, "selection_group": "ch15-v3-putr-lord-comforts.step-001:putr-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主（Putr’s Lord）是否落在自己的宫。"}, {"when": {"fact_key": "五宫主（Putr’s Lord）是哪一颗行星"}, "required_fact_keys": ["五宫主（Putr’s Lord）是否落在自己的 Navāńś"], "branch_condition_logic": {"fact_key": "五宫主（Putr’s Lord）是否落在自己的 Navāńś"}, "selection_group": "ch15-v3-putr-lord-comforts.step-001:putr-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主（Putr’s Lord）是否落在自己的 Navāńś。"}, {"when": {"fact_key": "五宫主（Putr’s Lord）是哪一颗行星"}, "required_fact_keys": ["五宫主（Putr’s Lord）是否入旺"], "branch_condition_logic": {"fact_key": "五宫主（Putr’s Lord）是否入旺"}, "selection_group": "ch15-v3-putr-lord-comforts.step-001:putr-lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主（Putr’s Lord）是否入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断房产或车辆的数量、价格与取得时间。", "不得把这条五宫主的规则改挂到四宫主身上。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主（Putr’s Lord）是哪一颗行星。
- 缺失即停字段：["五宫主（Putr’s Lord）是哪一颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v3`｜PDF [29]｜“Should Putr’s Lord be in his own Bhava, or in own Navāńś, or in exaltation, the native will be endowed with comforts, related to lands, conveyances, houses etc. and musical instruments.”


## 四路查书计划

### 支持路

- 五宫主 入本宫 入旺 土地 车乘 房屋 乐器

### 反例或取消路

- 五宫主落陷 失去土地车乘

### 适用边界路

- 五宫主规则的适用边界

### 判断方法路

- 判断土地车乘房屋之乐要查什么

## 上游问题

- 无

## 停止条件

- 无法确定五宫主是哪一颗行星时停止。
- 缺少五宫主的落宫、Navāńś 或旺弱事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
