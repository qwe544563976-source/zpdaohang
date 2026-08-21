---
method: ch16-v24-32-number-of-sons
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 儿子数量：十子、九子、八子与两种七子组合

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会有几个儿子
- 我孩子多不多
- 我能生几个孩子

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 四宫是否被凶星占据
- 六宫是否被凶星占据
- 五宫主是否深度入旺
- 五宫主是否与上升主同宫
- 木星是否与另一吉星同宫
- 木星是否深度入旺
- 罗睺是否与二宫主同宫
- 九宫是否被九宫主占据
- 五宫主是否有力
- 二宫主是否落十宫
- 土星是否落九宫
- 五宫主是否落五宫
- 五宫主是否与二宫主同宫

## 按情况检查的事实

- 木星是否落五宫
- 木星是否落九宫

## 依赖方法

- 无

## 执行步骤

### ch16-v24-32-number-of-sons.step-001

- 动作：核对四宫与六宫的凶星占据、五宫主深度入旺并与上升主同宫、木星与另一吉星同宫，判断是否主十个儿子。
- 适用范围：仅限本命五宫儿子数量主题；原文只给十个儿子这一个数量结论，未给时间或上升限定。
- 原文最小意思：四宫与六宫被凶星占据、五宫主深度入旺并与上升主同宫、木星与另一吉星同宫时，会有10个儿子。
- 本步骤产出事实：["十子判定"]
- 所需事实：["四宫是否被凶星占据", "六宫是否被凶星占据", "五宫主是否深度入旺", "五宫主是否与上升主同宫", "木星是否与另一吉星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "四宫是否被凶星占据"}, {"fact_key": "六宫是否被凶星占据"}, {"fact_key": "五宫主是否深度入旺"}, {"fact_key": "五宫主是否与上升主同宫"}, {"fact_key": "木星是否与另一吉星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把10个儿子改写成其他数量或算作子女总数。", "不得据此推断子女出生时间或性别比例。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：四宫是否被凶星占据、六宫是否被凶星占据、五宫主是否深度入旺、五宫主是否与上升主同宫、木星是否与另一吉星同宫。
- 缺失即停字段：["四宫是否被凶星占据", "六宫是否被凶星占据", "五宫主是否深度入旺", "五宫主是否与上升主同宫", "木星是否与另一吉星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v24-32`｜PDF [31, 32]｜“There will be 10 sons, if Bandhu Bhava and Ari Bhava are occupied by malefics, while Putr’s Lord is in deep exaltation, joining Lagn’s Lord, as Guru is with another benefic.”

### ch16-v24-32-number-of-sons.step-002

- 动作：核对木星是否深度入旺、罗睺是否与二宫主同宫、九宫是否被九宫主占据，判断是否主九个儿子。
- 适用范围：仅限本命五宫儿子数量主题；原文只给九个儿子这一个数量结论，未给时间或上升限定。
- 原文最小意思：木星深度入旺、罗睺与二宫主同宫、九宫被其宫主占据时，会有九个儿子。
- 本步骤产出事实：["九子判定"]
- 所需事实：["木星是否深度入旺", "罗睺是否与二宫主同宫", "九宫是否被九宫主占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "木星是否深度入旺"}, {"fact_key": "罗睺是否与二宫主同宫"}, {"fact_key": "九宫是否被九宫主占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把九个儿子改写成其他数量或算作子女总数。", "不得据此推断子女出生时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星是否深度入旺、罗睺是否与二宫主同宫、九宫是否被九宫主占据。
- 缺失即停字段：["木星是否深度入旺", "罗睺是否与二宫主同宫", "九宫是否被九宫主占据"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v24-32`｜PDF [31, 32]｜“Nine will be the number of sons, that one will beget, if Guru is in deep exaltation, as Rahu is with Dhan’s Lord and Dharm is occupied by its own Lord.”

### ch16-v24-32-number-of-sons.step-003

- 动作：核对木星是否落五宫或九宫、五宫主是否有力、二宫主是否落十宫，判断是否主八个儿子。
- 适用范围：仅限本命五宫儿子数量主题；原文只给八个儿子这一个数量结论，木星落宫只列五宫与九宫两处。
- 原文最小意思：木星落五宫或九宫、五宫主有力、二宫主落十宫时，会有八个儿子。
- 本步骤产出事实：["八子判定"]
- 所需事实：["五宫主是否有力", "二宫主是否落十宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "五宫主是否有力"}, {"fact_key": "二宫主是否落十宫"}]}, {"operator": "OR", "operands": [{"fact_key": "木星是否落五宫"}, {"fact_key": "木星是否落九宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "五宫主是否有力"}, {"fact_key": "二宫主是否落十宫"}]}, "required_fact_keys": ["木星是否落五宫"], "branch_condition_logic": {"fact_key": "木星是否落五宫"}, "selection_group": "ch16-v24-32-number-of-sons.step-003:guru-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星是否落五宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "五宫主是否有力"}, {"fact_key": "二宫主是否落十宫"}]}, "required_fact_keys": ["木星是否落九宫"], "branch_condition_logic": {"fact_key": "木星是否落九宫"}, "selection_group": "ch16-v24-32-number-of-sons.step-003:guru-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星是否落九宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把木星落五宫、九宫以外的位置也算作本条件。", "不得把八个儿子改写成其他数量或算作子女总数。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否有力、二宫主是否落十宫。
- 缺失即停字段：["五宫主是否有力", "二宫主是否落十宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v24-32`｜PDF [31, 32]｜“There will be eight sons, if Guru is in Putr, or Dharm Bhava, while Putr’s Lord is endowed with strength and Dhan’s Lord is in Karm Bhava.”

### ch16-v24-32-number-of-sons.step-004

- 动作：核对土星是否落九宫、五宫主是否落五宫本宫，判断是否主七个儿子并两次生双胞胎。
- 适用范围：仅限本命五宫儿子数量主题；原文只给七个儿子并两次双生这一个结论，未给时间限定。
- 原文最小意思：土星落九宫、五宫主落五宫本宫时，会有7个儿子，其中两次生双胞胎。
- 本步骤产出事实：["七子双生判定"]
- 所需事实：["土星是否落九宫", "五宫主是否落五宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星是否落九宫"}, {"fact_key": "五宫主是否落五宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把7个儿子或两次双生改写成其他数量。", "不得据此推断双胞胎出生的具体时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星是否落九宫、五宫主是否落五宫。
- 缺失即停字段：["土星是否落九宫", "五宫主是否落五宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v24-32`｜PDF [31, 32]｜“Shani in Dharm Bhava, while Putr’s Lord is in Putr itself, gives 7 sons, out of which twins will be born twice.”

### ch16-v24-32-number-of-sons.step-005

- 动作：核对五宫主是否落五宫并与二宫主同宫，判断是否主七个儿子而其中三个去世。
- 适用范围：仅限本命五宫儿子数量与存殁主题；原文只给七子三亡这一个结论，未给时间限定。
- 原文最小意思：五宫主落五宫并与二宫主同宫时，会生7个儿子，其中3个会去世。
- 本步骤产出事实：["七子三亡判定"]
- 所需事实：["五宫主是否落五宫", "五宫主是否与二宫主同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫主是否落五宫"}, {"fact_key": "五宫主是否与二宫主同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把7个儿子或去世3个改写成其他数量。", "不得据此推断去世发生的年龄或原因。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否落五宫、五宫主是否与二宫主同宫。
- 缺失即停字段：["五宫主是否落五宫", "五宫主是否与二宫主同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v24-32`｜PDF [31, 32]｜“If Putr’s Lord is in Putr in Yuti with Dhan’s Lord, there will be birth of 7 sons, out of which 3 will pass away.”


## 四路查书计划

### 支持路

- There will be 10 sons Bandhu Ari occupied by malefics deep exaltation
- Nine will be the number of sons Guru deep exaltation Rahu Dhan’s Lord
- 五宫主落五宫 与二宫主同宫 七子三亡

### 反例或取消路

- Only one son is denoted malefic in Putr Bhava
- 五宫有凶星 子女数量减少

### 适用边界路

- number of sons rules scope Putr Bhava BPHS
- 儿子数量断语的适用边界

### 判断方法路

- how to count number of children from Putr Bhava
- 判断子女数量要检查哪些行星组合

## 上游问题

- 无

## 停止条件

- 缺少四宫、六宫凶星占据事实时停止。
- 缺少五宫主庙旺、力量与同宫关系事实时停止。
- 缺少木星与土星落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
