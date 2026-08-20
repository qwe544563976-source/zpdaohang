---
method: ch16-v13-daughters-chandra
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 生女儿：五宫主与月亮同宫或落月亮的十分盘

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会生儿子还是女儿
- 我是不是会有女儿

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫主是哪颗行星

## 按情况检查的事实

- 五宫主是否与月亮（Chandra）同宫
- 五宫主是否落在月亮主管的十分盘（Decanate）

## 依赖方法

- 无

## 执行步骤

### ch16-v13-daughters-chandra.step-001

- 动作：先定出五宫主是哪颗行星，再核对它是否与月亮同宫，或是否落在月亮的十分盘中。
- 适用范围：仅限本命盘子女性别主题；原文只说会生女儿，未给女儿人数或出生年份。
- 原文最小意思：五宫主与月亮（Chandra）同宫、或落在月亮的十分盘（Decanate）中时，此人生女儿。
- 本步骤产出事实：["五宫主属月得女判定"]
- 所需事实：["本盘五宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "五宫主是否与月亮（Chandra）同宫"}, {"fact_key": "五宫主是否落在月亮主管的十分盘（Decanate）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否与月亮（Chandra）同宫"], "branch_condition_logic": {"fact_key": "五宫主是否与月亮（Chandra）同宫"}, "selection_group": "ch16-v13-daughters-chandra.step-001:chandra-link", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否与月亮（Chandra）同宫。"}, {"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否落在月亮主管的十分盘（Decanate）"], "branch_condition_logic": {"fact_key": "五宫主是否落在月亮主管的十分盘（Decanate）"}, "selection_group": "ch16-v13-daughters-chandra.step-001:chandra-link", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落在月亮主管的十分盘（Decanate）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断女儿的人数或出生年份。", "不得把生女儿改写成不会有儿子。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫主是哪颗行星。
- 缺失即停字段：["本盘五宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v13`｜PDF [31]｜“If Putr’s Lord is with Chandra, or is in her Decanate, the native will beget daughters; so say Jyotishis.”


## 四路查书计划

### 支持路

- Putr’s Lord with Chandra or in her Decanate beget daughters
- 五宫主与月亮同宫 月亮十分盘 生女儿

### 反例或取消路

- Putr’s Lord with Surya sons
- 五宫主与太阳相关 生子 反例

### 适用边界路

- Decanate of Chandra definition scope daughters rule
- 月亮十分盘条件的界定与边界

### 判断方法路

- how to find the Decanate of Putr’s Lord
- 怎样查五宫主所在的十分盘

## 上游问题

- 无

## 停止条件

- 缺少五宫主行星身份事实时停止。
- 缺少五宫主与月亮的同宫或十分盘事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
