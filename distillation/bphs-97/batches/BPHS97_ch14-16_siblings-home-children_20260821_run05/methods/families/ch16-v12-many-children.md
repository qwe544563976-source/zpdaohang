---
method: ch16-v12-many-children
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 子女众多：五宫主有力且五宫受有力的水星木星金星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会有几个孩子
- 我是不是子女缘旺

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫主是否有力量
- 第五宫（Putr）是否受有力的水星（Budh）、木星（Guru）与金星（Shukr）相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch16-v12-many-children.step-001

- 动作：核对五宫主是否有力，并核对第五宫是否同时受有力的水星、木星与金星相照。
- 适用范围：仅限本命盘子女人数主题；原文只说众多，未给具体数字、性别或出生年份。
- 原文最小意思：五宫主有力、且五宫（Putr）受有力的水星（Budh）、木星（Guru）与金星（Shukr）相照时，子女众多。
- 本步骤产出事实：["五宫得力受吉相照多子判定"]
- 所需事实：["五宫主是否有力量", "第五宫（Putr）是否受有力的水星（Budh）、木星（Guru）与金星（Shukr）相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫主是否有力量"}, {"fact_key": "第五宫（Putr）是否受有力的水星（Budh）、木星（Guru）与金星（Shukr）相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把“众多”换算成具体子女人数。", "不得据此推断子女的性别或出生时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否有力量、第五宫（Putr）是否受有力的水星（Budh）、木星（Guru）与金星（Shukr）相照。
- 缺失即停字段：["五宫主是否有力量", "第五宫（Putr）是否受有力的水星（Budh）、木星（Guru）与金星（Shukr）相照"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v12`｜PDF [31]｜“There will be many children, if Putr’s Lord is strong, while Putr is drishtied by strong Budh, Guru and Shukr.”


## 四路查书计划

### 支持路

- Putr’s Lord strong Putr drishtied by strong Budh Guru Shukr many children
- 五宫主有力 五宫受水星木星金星相照 子女众多

### 反例或取消路

- Putr’s Lord in fall no children
- 五宫主落陷 无子 反例

### 适用边界路

- many children rule scope strength requirement
- 多子断语对力量条件的要求与边界

### 判断方法路

- how to check drishti of Budh Guru Shukr on Putr Bhava
- 怎样查水星木星金星对五宫的相照

## 上游问题

- 无

## 停止条件

- 缺少五宫主力量事实时停止。
- 缺少水星木星金星对第五宫相照的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
