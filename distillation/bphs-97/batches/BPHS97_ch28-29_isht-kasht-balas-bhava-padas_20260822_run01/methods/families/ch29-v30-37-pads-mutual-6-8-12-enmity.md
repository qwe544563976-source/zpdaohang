---
method: ch29-v30-37-pads-mutual-6-8-12-enmity
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升 Pad 与 Dar Pad 互为第 6、8、12 宫：必生敌意

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我们会不会闹翻
- 夫妻会不会互相敌视

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升 Pad（Lagn Pad）落在哪一宫
- 本盘 Dar Pad（Kalatr Pad）落在哪一宫

## 按情况检查的事实

- 上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 6 宫
- 上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 8 宫
- 上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 12 宫

## 依赖方法

- 无

## 执行步骤

### ch29-v30-37-pads-mutual-6-8-12-enmity.step-001

- 动作：先定出上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）各落哪一宫，再看两者是否互为第 6、8 或 12 宫。
- 适用范围：原文的「these」承同偈前句的上升 Pad 与 Dar Pad 两者；本条断的是两者之间的敌意。
- 原文最小意思：上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）互为第 6 宫、第 8 宫、或第 12 宫时，两者之间必生敌意。
- 本步骤产出事实：["两 Pad 互为 6、8、12 宫的敌意判定"]
- 所需事实：["本盘上升 Pad（Lagn Pad）落在哪一宫", "本盘 Dar Pad（Kalatr Pad）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}]}, {"operator": "OR", "operands": [{"fact_key": "上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 6 宫"}, {"fact_key": "上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 8 宫"}, {"fact_key": "上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 12 宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}]}, "required_fact_keys": ["上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 6 宫"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 6 宫"}, "selection_group": "ch29-v30-37-pads-mutual-6-8-12-enmity.step-001:mutual-position", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 6 宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}]}, "required_fact_keys": ["上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 8 宫"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 8 宫"}, "selection_group": "ch29-v30-37-pads-mutual-6-8-12-enmity.step-001:mutual-position", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 8 宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升 Pad（Lagn Pad）落在哪一宫"}, {"fact_key": "本盘 Dar Pad（Kalatr Pad）落在哪一宫"}]}, "required_fact_keys": ["上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 12 宫"], "branch_condition_logic": {"fact_key": "上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 12 宫"}, "selection_group": "ch29-v30-37-pads-mutual-6-8-12-enmity.step-001:mutual-position", "stop_condition": "选中该分支后，缺少以下事实即停止：上升 Pad（Lagn Pad）与 Dar Pad（Kalatr Pad）是否互为第 12 宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断离异、诉讼或时间。", "原文只说必生敌意，不得加重成关系破裂。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升 Pad（Lagn Pad）落在哪一宫、本盘 Dar Pad（Kalatr Pad）落在哪一宫。
- 缺失即停字段：["本盘上升 Pad（Lagn Pad）落在哪一宫", "本盘 Dar Pad（Kalatr Pad）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v30-37`｜PDF [63]｜“If Lagn Pad and Dar Pad are mutually in Kendras, or Konas, there will be amity between the couple.”
  - `bphs-97:santhanam:ch29:v30-37`｜PDF [63]｜“If these be in mutually 6<sup>th</sup> /8<sup>th</sup> /12<sup>th</sup> , doubtlessly mutual enmity will crop up.”


## 四路查书计划

### 支持路

- If these be in mutually 6<sup>th</sup> /8<sup>th</sup> /12<sup>th</sup> , doubtlessly mutual enmity will crop up.
- 上升 Pad 与 Dar Pad 互为 6、8、12 宫 敌意

### 反例或取消路

- If Lagn Pad and Dar Pad are mutually in Kendras, or Konas, there will be amity between the couple.
- 两 Pad 互为角宫三角宫时的和睦条

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- Dar (Kalatr) of Yuvati
- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- Dar Pad 是哪一个 Pad

## 上游问题

- 无

## 停止条件

- 缺少上升 Pad 或 Dar Pad 落宫事实时停止。
- 缺少两者相互位次的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
