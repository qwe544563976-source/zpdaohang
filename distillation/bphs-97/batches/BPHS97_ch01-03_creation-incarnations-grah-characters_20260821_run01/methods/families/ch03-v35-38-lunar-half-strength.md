---
method: ch03-v35-38-lunar-half-strength
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 明暗半月强弱：暗半月凶星有力、明半月吉星得力

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我出生在暗半月 盘里凶星是不是更有力
- 明半月出生对吉星强弱有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘出生时的月相属暗半月（dark half）还是明半月（bright half）
- 本盘中哪些行星被判为凶星
- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v35-38-lunar-half-strength.step-001

- 动作：核对本盘出生时的月相与凶星名册，判断凶星是否处于有力时段。
- 适用范围：第3章诸曜强弱条；吉凶星的名册由本书第3章另条界定，本偈不重复。
- 原文最小意思：在暗半月（dark half）凶星有力。
- 本步骤产出事实：["暗半月凶星有力判定"]
- 所需事实：["本盘出生时的月相属暗半月（dark half）还是明半月（bright half）", "本盘中哪些行星被判为凶星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘出生时的月相属暗半月（dark half）还是明半月（bright half）"}, {"fact_key": "本盘中哪些行星被判为凶星"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条把「凶星有力」读成凶果一定发生。", "不得据本条推出暗半月里吉星如何——本句只说凶星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生时的月相属暗半月（dark half）还是明半月（bright half）、本盘中哪些行星被判为凶星。
- 缺失即停字段：["本盘出生时的月相属暗半月（dark half）还是明半月（bright half）", "本盘中哪些行星被判为凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v35-38`｜PDF [11]｜“During the dark half malefics are strong.”

### ch03-v35-38-lunar-half-strength.step-002

- 动作：核对本盘出生时的月相与吉星名册，判断吉星是否处于得力时段。
- 适用范围：第3章诸曜强弱条；吉凶星的名册由本书第3章另条界定，本偈不重复。
- 原文最小意思：在该月的明半月（bright half）吉星得力。
- 本步骤产出事实：["明半月吉星得力判定"]
- 所需事实：["本盘出生时的月相属暗半月（dark half）还是明半月（bright half）", "本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘出生时的月相属暗半月（dark half）还是明半月（bright half）"}, {"fact_key": "本盘中哪些行星被判为吉星"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条把「吉星得力」读成吉果一定发生。", "不得据本条推出明半月里凶星如何——本句只说吉星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生时的月相属暗半月（dark half）还是明半月（bright half）、本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘出生时的月相属暗半月（dark half）还是明半月（bright half）", "本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v35-38`｜PDF [11]｜“Benefics acquire strength in the bright half of the month.”


## 四路查书计划

### 支持路

- During the dark half malefics are strong. Benefics acquire strength in the bright half of the month
- 明半月 暗半月 吉星凶星强弱

### 反例或取消路

- 无

### 适用边界路

- All evils are destroyed, if a benefic drishties Lagn of one born during the night in the bright half
- 明暗半月与昼夜合看的另一条原文

### 判断方法路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu
- Kaal Bal comprises of the following subdivisions: Nathonnata Bal (diurnal and nocturnal), Paksh Bal (fortnight)
- 本书怎么界定吉星与凶星

## 上游问题

- 无

## 停止条件

- 缺少本盘出生月相（明半月还是暗半月）的事实时停止。
- 缺少本盘吉星或凶星名册时停止。
- 本条只说强弱，没有给吉凶结果，要下断语必须另找原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
