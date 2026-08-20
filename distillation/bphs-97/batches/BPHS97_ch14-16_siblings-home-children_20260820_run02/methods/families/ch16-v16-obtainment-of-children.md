---
method: ch16-v16-obtainment-of-children
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 得子有望：五宫主入庙、落二五九宫或与木星同宫相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子会不会有孩子
- 我能不能顺利得子

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫主是否入庙旺
- 本盘五宫主落在哪一宫
- 本盘五宫主是哪颗行星

## 按情况检查的事实

- 五宫主是否落二宫
- 五宫主是否落五宫
- 五宫主是否落九宫
- 五宫主是否与木星同宫
- 五宫主是否被木星相照

## 依赖方法

- 无

## 执行步骤

### ch16-v16-obtainment-of-children.step-001

- 动作：核对五宫主是否入庙旺，判断是否有子女可得。
- 适用范围：仅限本命五宫得子有无主题；原文未给数量、时间或上升限定。
- 原文最小意思：五宫主入庙旺时，会有子女可得。
- 本步骤产出事实：["五宫主入庙得子判定"]
- 所需事实：["五宫主是否入庙旺"]
- 条件关系：{"fact_key": "五宫主是否入庙旺"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断子女数量、性别或得子年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫主是否入庙旺。
- 缺失即停字段：["五宫主是否入庙旺"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v16`｜PDF [31]｜“If Putr’s Lord is exalted”
  - `bphs-97:santhanam:ch16:v16`｜PDF [31]｜“obtainment of children will be there”

### ch16-v16-obtainment-of-children.step-002

- 动作：先取得五宫主所落宫位，再核对是否落二宫、五宫或九宫，判断是否有子女可得。
- 适用范围：仅限本命五宫得子有无主题；原文只列二宫、五宫、九宫三处落宫，未给数量或时间限定。
- 原文最小意思：五宫主落二宫、五宫或九宫之一时，会有子女可得。
- 本步骤产出事实：["五宫主吉宫得子判定"]
- 所需事实：["本盘五宫主落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫主落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "五宫主是否落二宫"}, {"fact_key": "五宫主是否落五宫"}, {"fact_key": "五宫主是否落九宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘五宫主落在哪一宫"}, "required_fact_keys": ["五宫主是否落二宫"], "branch_condition_logic": {"fact_key": "五宫主是否落二宫"}, "selection_group": "ch16-v16-obtainment-of-children.step-002:lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落二宫。"}, {"when": {"fact_key": "本盘五宫主落在哪一宫"}, "required_fact_keys": ["五宫主是否落五宫"], "branch_condition_logic": {"fact_key": "五宫主是否落五宫"}, "selection_group": "ch16-v16-obtainment-of-children.step-002:lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落五宫。"}, {"when": {"fact_key": "本盘五宫主落在哪一宫"}, "required_fact_keys": ["五宫主是否落九宫"], "branch_condition_logic": {"fact_key": "五宫主是否落九宫"}, "selection_group": "ch16-v16-obtainment-of-children.step-002:lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落九宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把二宫、五宫、九宫以外的落宫也算作本条件。", "不得据此推断子女数量或得子年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫主落在哪一宫。
- 缺失即停字段：["本盘五宫主落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v16`｜PDF [31]｜“be in Dhan, Putr, or Dharm Bhava”
  - `bphs-97:santhanam:ch16:v16`｜PDF [31]｜“obtainment of children will be there”

### ch16-v16-obtainment-of-children.step-003

- 动作：先取得五宫主是哪颗行星，再核对它与木星的同宫或相照关系，判断是否有子女可得。
- 适用范围：仅限本命五宫得子有无主题；原文只讲与木星的同宫或相照关系，未给数量或时间限定。
- 原文最小意思：五宫主与木星同宫或被木星相照时，会有子女可得。
- 本步骤产出事实：["五宫主木星关联得子判定"]
- 所需事实：["本盘五宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "五宫主是否与木星同宫"}, {"fact_key": "五宫主是否被木星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否与木星同宫"], "branch_condition_logic": {"fact_key": "五宫主是否与木星同宫"}, "selection_group": "ch16-v16-obtainment-of-children.step-003:guru-link", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否与木星同宫。"}, {"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否被木星相照"], "branch_condition_logic": {"fact_key": "五宫主是否被木星相照"}, "selection_group": "ch16-v16-obtainment-of-children.step-003:guru-link", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否被木星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把木星以外行星的同宫或相照算作本条件。", "不得据此推断子女数量或得子年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫主是哪颗行星。
- 缺失即停字段：["本盘五宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v16`｜PDF [31]｜“be yuti with, or drishtied by Guru”
  - `bphs-97:santhanam:ch16:v16`｜PDF [31]｜“obtainment of children will be there”


## 四路查书计划

### 支持路

- Putr’s Lord exalted or in Dhan Putr Dharm Bhava obtainment of children
- 五宫主入庙 落二宫五宫九宫 与木星同宫相照 得子

### 反例或取消路

- Putr’s Lord in fall or with malefics denial of children
- 五宫主落陷 与凶星同宫 无子

### 适用边界路

- obtainment of children rule applicability Putr Bhava
- 得子有无判断的适用边界

### 判断方法路

- how to judge whether one will have children BPHS
- 判断有没有孩子应检查五宫主什么状态

## 上游问题

- 无

## 停止条件

- 缺少五宫主庙旺陷落状态事实时停止。
- 缺少五宫主落宫事实时停止。
- 缺少五宫主与木星同宫或相照事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
