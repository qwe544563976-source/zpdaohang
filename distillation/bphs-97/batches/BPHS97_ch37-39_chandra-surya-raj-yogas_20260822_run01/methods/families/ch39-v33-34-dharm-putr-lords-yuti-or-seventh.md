---
method: ch39-v33-34-dharm-putr-lords-yuti-or-seventh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 九宫主与五宫主同宫或互处第7宫：王族出身者成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我出身普通 这个组合还算吗
- 九宫主五宫主同宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘九宫主（Dharm's Lord）是哪颗行星
- 本盘五宫主（Putr's Lord）是哪颗行星

## 按情况检查的事实

- 九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否同宫
- 九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否互处第7宫

## 依赖方法

- 无

## 执行步骤

### ch39-v33-34-dharm-putr-lords-yuti-or-seventh.step-001

- 动作：先认出九宫主与五宫主，再核对两者是同宫，还是彼此互处第7宫。
- 适用范围：仅限本命盘；原文这一句的断语主语限定为 one born of royal scion（王族出身者），不适用于一般出身；原文没有时间限定。
- 原文最小意思：九宫主（Dharm's Lord）与五宫主（Putr's Lord）在任一宫同宫，或彼此互处第7宫时，王族出身者会成为国王。
- 本步骤产出事实：["九五宫主同宫或对冲的成王判定"]
- 所需事实：["本盘九宫主（Dharm's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否同宫"}, {"fact_key": "九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否互处第7宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, "required_fact_keys": ["九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否同宫"], "branch_condition_logic": {"fact_key": "九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否同宫"}, "selection_group": "ch39-v33-34-dharm-putr-lords-yuti-or-seventh.step-001:yuti-or-seventh", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, "required_fact_keys": ["九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否互处第7宫"], "branch_condition_logic": {"fact_key": "九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否互处第7宫"}, "selection_group": "ch39-v33-34-dharm-putr-lords-yuti-or-seventh.step-001:yuti-or-seventh", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否互处第7宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得去掉 one born of royal scion 这一出身限定。", "不得据此推断登位时间或权位大小。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘九宫主（Dharm's Lord）是哪颗行星、本盘五宫主（Putr's Lord）是哪颗行星。
- 缺失即停字段：["本盘九宫主（Dharm's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v33-34`｜PDF [84]｜“Dharm’s Lord is akin to a minister and more especially Putr’s Lord.”
  - `bphs-97:santhanam:ch39:v33-34`｜PDF [84]｜“Even, if these two are yuti in any Bhava, or, if they happen to be placed in mutually 7<sup>th</sup> places, one born of royal scion will become a king.”


## 四路查书计划

### 支持路

- Even, if these two are yuti in any Bhava, or, if they happen to be placed in mutually 7<sup>th</sup> places, one born of royal scion will become a king
- 九宫主五宫主同宫 互处第七宫 王族出身

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- Should Putr’s and Dharm’s Lords be, respectively, found in Ari and Vyaya Bhava and receive a Drishti from Marak Grahas, the native will be penniless

### 适用边界路

- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained
- Putr and Dharm Bhava are known by the name Kon (or trine)

### 判断方法路

- Dharm’s Lord and Putr’s Lord are capable of bestowing wealth
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- 九宫主或五宫主的身份事实缺失时停止。
- 同宫与互处第7宫两项事实全部缺失时停止。
- 命主是否为王族出身未确定时，本条断语停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
