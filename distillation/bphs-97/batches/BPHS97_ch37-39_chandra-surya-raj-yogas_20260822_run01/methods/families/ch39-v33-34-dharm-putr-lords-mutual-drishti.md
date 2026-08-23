---
method: ch39-v33-34-dharm-putr-lords-mutual-drishti
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 九宫主与五宫主互相相照：获得王国

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 九宫主和五宫主的关系有多重要
- 我有没有得大位的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘九宫主（Dharm's Lord）是哪颗行星
- 本盘五宫主（Putr's Lord）是哪颗行星
- 九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否互相相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v33-34-dharm-putr-lords-mutual-drishti.step-001

- 动作：先认出九宫主与五宫主，再核对两者是否互相相照。
- 适用范围：仅限本命盘；原文先说九宫主如大臣、五宫主尤甚，本步只取其互照一条；原文没有时间限定。
- 原文最小意思：九宫主（Dharm's Lord）与五宫主（Putr's Lord）互相相照时，命主会获得王国。
- 本步骤产出事实：["九五宫主互照的得国判定"]
- 所需事实：["本盘九宫主（Dharm's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星", "九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否互相相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否互相相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文此句没有出身限定，不得把下一句的 royal scion 限定搬到这里。", "不得据此推断得位时间或权位大小。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘九宫主（Dharm's Lord）是哪颗行星、本盘五宫主（Putr's Lord）是哪颗行星、九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否互相相照。
- 缺失即停字段：["本盘九宫主（Dharm's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星", "九宫主（Dharm's Lord）与五宫主（Putr's Lord）是否互相相照"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v33-34`｜PDF [84]｜“Dharm’s Lord is akin to a minister and more especially Putr’s Lord. If these two Grahas mutually give a Drishti, the native will obtain a kingdom.”


## 四路查书计划

### 支持路

- Dharm’s Lord is akin to a minister and more especially Putr’s Lord. If these two Grahas mutually give a Drishti, the native will obtain a kingdom
- 九宫主五宫主互相相照 获得王国

### 反例或取消路

- Should Putr’s and Dharm’s Lords be, respectively, found in Ari and Vyaya Bhava and receive a Drishti from Marak Grahas, the native will be penniless
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

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
- 缺少两者互照的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
