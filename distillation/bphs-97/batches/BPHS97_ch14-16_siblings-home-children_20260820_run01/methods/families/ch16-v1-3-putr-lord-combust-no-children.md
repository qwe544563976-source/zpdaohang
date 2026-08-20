---
method: ch16-v1-3-putr-lord-combust-no-children
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 无子女：五宫主燃烧、或与凶星同宫且力弱

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会没有孩子
- 我的孩子会不会养不住

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫主是哪颗行星

## 按情况检查的事实

- 五宫主是否处于燃烧（combust）状态
- 五宫主是否与凶星同宫并且力量微弱
- 是否偶然获得了子女

## 依赖方法

- 无

## 执行步骤

### ch16-v1-3-putr-lord-combust-no-children.step-001

- 动作：先定出五宫主是哪颗行星，再核对它是否燃烧，或是否与凶星同宫且力弱。
- 适用范围：仅限本命盘五宫子女有无与存活主题；原文只给燃烧与凶星致弱两种情形，未给时间或补救限定。
- 原文最小意思：五宫主燃烧、或与凶星同宫且力弱时，没有子女；即使偶然得到子女，子女也会很快离世。
- 本步骤产出事实：["五宫主受克无子女判定"]
- 所需事实：["本盘五宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "五宫主是否处于燃烧（combust）状态"}, {"fact_key": "五宫主是否与凶星同宫并且力量微弱"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否处于燃烧（combust）状态"], "branch_condition_logic": {"fact_key": "五宫主是否处于燃烧（combust）状态"}, "selection_group": "ch16-v1-3-putr-lord-combust-no-children.step-001:affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否处于燃烧（combust）状态。"}, {"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否与凶星同宫并且力量微弱"], "branch_condition_logic": {"fact_key": "五宫主是否与凶星同宫并且力量微弱"}, "selection_group": "ch16-v1-3-putr-lord-combust-no-children.step-001:affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否与凶星同宫并且力量微弱。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断子女离世的具体年龄或年份。", "不得把原文的让步句改写成必定得子。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫主是哪颗行星。
- 缺失即停字段：["本盘五宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v1-3`｜PDF [30]｜“Should the Lord of Putr be combust, or be with malefics and be weak, there will be no children; even, if per chance issues are obtained, they will only quit the world soon.”


## 四路查书计划

### 支持路

- Lord of Putr combust with malefics weak no children
- 五宫主燃烧 与凶星同宫 力弱 无子女

### 反例或取消路

- Putr’s Lord strong benefic drishti children survive
- 五宫主有力 得子 反例

### 适用边界路

- combust Putr Lord rule scope children survival
- 燃烧致无子断语的边界

### 判断方法路

- how to judge combustion and malefic association of Putr’s Lord
- 怎样查五宫主的燃烧与凶星同宫

## 上游问题

- 无

## 停止条件

- 缺少五宫主行星身份事实时停止。
- 缺少五宫主燃烧或凶星同宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
