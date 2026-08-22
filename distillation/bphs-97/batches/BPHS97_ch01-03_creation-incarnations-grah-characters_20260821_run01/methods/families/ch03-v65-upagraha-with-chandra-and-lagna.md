---
method: ch03-v65-upagraha-with-chandra-and-lagna
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 副曜与月亮或上升相合：分别毁其寿元与智慧

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 影曜跟月亮同度会怎么样
- 影曜落在上升上会怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些点与非发光副曜（UpaGrahas）相合

## 按情况检查的事实

- 月亮（Chandra）是否与非发光副曜相合
- 上升（Lagna）是否与非发光副曜相合

## 依赖方法

- 无

## 执行步骤

### ch03-v65-upagraha-with-chandra-and-lagna.step-001

- 动作：核对月亮与上升是否与上一偈的非发光副曜相合，按原文的对应次序取其结果。
- 适用范围：第3章副曜效应条；「这些」承上一偈的非发光副曜名单。本条以 So declared Lord Brahma, the Lotus-Born 转述立说；原文没有给「相合」的判准。
- 原文最小意思：月亮（Chandra）与上升（Lagna）依原文次序与这些副曜之一相合时，将分别毁其寿元与智慧。
- 本步骤产出事实：["副曜与月亮或上升相合的损害判定"]
- 所需事实：["本盘中哪些点与非发光副曜（UpaGrahas）相合"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些点与非发光副曜（UpaGrahas）相合"}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否与非发光副曜相合"}, {"fact_key": "上升（Lagna）是否与非发光副曜相合"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些点与非发光副曜（UpaGrahas）相合"}, "required_fact_keys": ["月亮（Chandra）是否与非发光副曜相合"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否与非发光副曜相合"}, "selection_group": "ch03-v65-upagraha-with-chandra-and-lagna.step-001:afflicted-point", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否与非发光副曜相合。"}, {"when": {"fact_key": "本盘中哪些点与非发光副曜（UpaGrahas）相合"}, "required_fact_keys": ["上升（Lagna）是否与非发光副曜相合"], "branch_condition_logic": {"fact_key": "上升（Lagna）是否与非发光副曜相合"}, "selection_group": "ch03-v65-upagraha-with-chandra-and-lagna.step-001:afflicted-point", "stop_condition": "选中该分支后，缺少以下事实即停止：上升（Lagna）是否与非发光副曜相合。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出寿元或智慧受损的时间、程度。", "不得自行给「相合」补上同宫、相照等判准——原文没有给。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些点与非发光副曜（UpaGrahas）相合。
- 缺失即停字段：["本盘中哪些点与非发光副曜（UpaGrahas）相合"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v65`｜PDF [13]｜“while Chandra and Lagna, respectively, associated with one of these, will destroy the longevity and wisdom.”


## 四路查书计划

### 支持路

- while Chandra and Lagna, respectively, associated with one of these, will destroy the longevity and wisdom
- 副曜与月亮相合 寿元 副曜与上升相合 智慧

### 反例或取消路

- 无

### 适用边界路

- So declared Lord Brahma, the Lotus-Born
- 本条是转述立说

### 判断方法路

- These are the Grahas, devoid of splendour, which are malefics by nature and cause affliction
- 先算出非发光副曜的位置才能看是否相合

## 上游问题

- 无

## 停止条件

- 缺少月亮或上升是否与非发光副曜相合的事实时，对应分支停止。
- 原文没有界定「相合」的判准，判准未定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
