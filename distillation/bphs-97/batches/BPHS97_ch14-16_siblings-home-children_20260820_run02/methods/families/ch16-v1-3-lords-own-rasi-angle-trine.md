---
method: ch16-v1-3-lords-own-rasi-angle-trine
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 子女幸福：上升主与五宫主同落本宫星座、角宫或三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我和孩子的缘分好不好
- 我这辈子能不能因为孩子过得幸福

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主与五宫主分别是哪颗行星

## 按情况检查的事实

- 上升主与五宫主是否都落在各自主管的星座
- 上升主与五宫主是否都落在角宫
- 上升主与五宫主是否都落在三角宫

## 依赖方法

- 无

## 执行步骤

### ch16-v1-3-lords-own-rasi-angle-trine.step-001

- 动作：先定出上升主与五宫主分别是哪颗行星，再核对两者是否同落各自主管星座、同落角宫或同落三角宫。
- 适用范围：仅限本命盘五宫子女幸福主题；原文只给这三种落点，未给上升星座、性别或时间限定。
- 原文最小意思：上升主与五宫主同落各自本宫星座、或同落角宫、或同落三角宫时，因子女而享有充分幸福。
- 本步骤产出事实：["上升主与五宫主吉位得子女幸福判定"]
- 所需事实：["本盘上升主与五宫主分别是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升主与五宫主分别是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "上升主与五宫主是否都落在各自主管的星座"}, {"fact_key": "上升主与五宫主是否都落在角宫"}, {"fact_key": "上升主与五宫主是否都落在三角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升主与五宫主分别是哪颗行星"}, "required_fact_keys": ["上升主与五宫主是否都落在各自主管的星座"], "branch_condition_logic": {"fact_key": "上升主与五宫主是否都落在各自主管的星座"}, "selection_group": "ch16-v1-3-lords-own-rasi-angle-trine.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主与五宫主是否都落在各自主管的星座。"}, {"when": {"fact_key": "本盘上升主与五宫主分别是哪颗行星"}, "required_fact_keys": ["上升主与五宫主是否都落在角宫"], "branch_condition_logic": {"fact_key": "上升主与五宫主是否都落在角宫"}, "selection_group": "ch16-v1-3-lords-own-rasi-angle-trine.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主与五宫主是否都落在角宫。"}, {"when": {"fact_key": "本盘上升主与五宫主分别是哪颗行星"}, "required_fact_keys": ["上升主与五宫主是否都落在三角宫"], "branch_condition_logic": {"fact_key": "上升主与五宫主是否都落在三角宫"}, "selection_group": "ch16-v1-3-lords-own-rasi-angle-trine.step-001:placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主与五宫主是否都落在三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断子女人数、性别或出生年份。", "不得把这条幸福断语扩大成其他宫位的吉凶。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主与五宫主分别是哪颗行星。
- 缺失即停字段：["本盘上升主与五宫主分别是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v1-3`｜PDF [30]｜“If the Lords of Lagn and Putr are in their own Rāśis, or in an angle, or in a trine, one will enjoy thorough happiness through his children.”


## 四路查书计划

### 支持路

- Lords of Lagn and Putr in their own Rāśis happiness through children
- 上升主 五宫主 落本宫星座 角宫 三角宫 子女幸福

### 反例或取消路

- Putr’s Lord in Ari Randhr Vyaya no offspring
- 五宫主落六八十二宫 无子

### 适用边界路

- Putr Bhava happiness scope of children effects
- 五宫子女幸福断语的适用边界

### 判断方法路

- how to judge Putr Bhava effects for children
- 判断五宫子女要先查哪些事实

## 上游问题

- 无

## 停止条件

- 缺少上升主或五宫主的行星身份事实时停止。
- 缺少两主落宫与落座事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
