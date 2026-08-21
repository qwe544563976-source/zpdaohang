---
method: ch14-v14-adverse-grahas
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三宫的凶星：Surya 毁兄姐、Shani 毁弟妹、Mangal 两者皆毁

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的哥哥姐姐会不会有事
- 我的弟弟妹妹保得住吗

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- Surya 是否落三宫
- Shani 是否落三宫
- Mangal 是否落三宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch14-v14-adverse-grahas.step-001

- 动作：核对 Surya 是否落三宫。
- 适用范围：仅限本命盘三宫先出生兄姐的存亡主题；原文未给毁灭的年龄或年份。
- 原文最小意思：Surya 落三宫，会毁灭先出生的兄姐。
- 本步骤产出事实：["Surya 落三宫毁灭兄姐判定"]
- 所需事实：["Surya 是否落三宫"]
- 条件关系：{"fact_key": "Surya 是否落三宫"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把先出生兄姐的结论套用到后出生的弟妹。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Surya 是否落三宫。
- 缺失即停字段：["Surya 是否落三宫"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v14`｜PDF [29]｜“Surya in Sahaj Bhava will destroy the preborn.”

### ch14-v14-adverse-grahas.step-002

- 动作：核对 Shani 是否落三宫。
- 适用范围：仅限本命盘三宫后出生弟妹的存亡主题；原文未给毁灭的年龄或年份。
- 原文最小意思：Shani 落三宫，后出生的弟妹会被毁灭。
- 本步骤产出事实：["Shani 落三宫毁灭弟妹判定"]
- 所需事实：["Shani 是否落三宫"]
- 条件关系：{"fact_key": "Shani 是否落三宫"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把后出生弟妹的结论套用到先出生的兄姐。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Shani 是否落三宫。
- 缺失即停字段：["Shani 是否落三宫"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v14`｜PDF [29]｜“The afterborn will be destroyed, if Shani is found in Sahaj Bhava.”

### ch14-v14-adverse-grahas.step-003

- 动作：核对 Mangal 是否同样落三宫。
- 适用范围：仅限本命盘三宫兄弟姐妹存亡主题；本句以“In the same situation”承接前两句的落三宫情形，原文未给年龄或年份。
- 原文最小意思：Mangal 在同样落三宫的情况下，会毁灭先出生与后出生的兄弟姐妹。
- 本步骤产出事实：["Mangal 落三宫毁灭先后出生兄弟姐妹判定"]
- 所需事实：["Mangal 是否落三宫"]
- 条件关系：{"fact_key": "Mangal 是否落三宫"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断毁灭的先后次序、人数或发生时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Mangal 是否落三宫。
- 缺失即停字段：["Mangal 是否落三宫"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v14`｜PDF [29]｜“In the same situation Mangal will destroy both the preborn and later-born.”


## 四路查书计划

### 支持路

- 太阳落三宫 毁兄姐 土星落三宫 毁弟妹 火星两者皆毁

### 反例或取消路

- 三宫吉星同宫 兄弟姐妹得保全

### 适用边界路

- 三宫凶星判断的适用边界

### 判断方法路

- 判断三宫凶星对兄弟姐妹影响的步骤

## 上游问题

- 无

## 停止条件

- 缺少 Surya、Shani、Mangal 的落宫事实时停止。
- 无法确定三宫（Sahaj Bhava）所在星座时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
