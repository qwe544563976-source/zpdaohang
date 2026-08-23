---
method: ch40-v13-karm-lagn-lords-exchange-royal-association
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 与王有大关联：十宫主与上升主互换星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的事业跟当权者会不会绑在一起
- 我这辈子能攀到多高的关系

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）是哪颗行星
- 本盘十宫主（Karm's Lord）是哪颗行星
- 上升主（Lagn's Lord）与十宫主（Karm's Lord）是否互换星座（Rāśi）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch40-v13-karm-lagn-lords-exchange-royal-association.step-001

- 动作：先认出上升主与十宫主，再核对两者是否互换所落星座。
- 适用范围：仅限本命盘上升主与十宫主的星座互换一项；原文未给时间限定，也未给上升限定。
- 原文最小意思：十宫主（Karm's Lord）与上升主（Lagn's Lord）互换星座时，命主将与王有大关联。
- 本步骤产出事实：["上升主与十宫主互换星座的王家关联判定"]
- 所需事实：["本盘上升主（Lagn's Lord）是哪颗行星", "本盘十宫主（Karm's Lord）是哪颗行星", "上升主（Lagn's Lord）与十宫主（Karm's Lord）是否互换星座（Rāśi）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）与十宫主（Karm's Lord）是否互换星座（Rāśi）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文写的是两主互换星座，不得把单向落入对方星座当成互换。", "不得据此推断关联的形式、职位或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）是哪颗行星、本盘十宫主（Karm's Lord）是哪颗行星、上升主（Lagn's Lord）与十宫主（Karm's Lord）是否互换星座（Rāśi）。
- 缺失即停字段：["本盘上升主（Lagn's Lord）是哪颗行星", "本盘十宫主（Karm's Lord）是哪颗行星", "上升主（Lagn's Lord）与十宫主（Karm's Lord）是否互换星座（Rāśi）"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v13`｜PDF [85]｜“An exchange of Rāśis between Karm’s Lord and Lagn’s Lord will make the native associated with the king in a great manner.”


## 四路查书计划

### 支持路

- An exchange of Rāśis between Karm’s Lord and Lagn’s Lord will make the native associated with the king in a great manner
- 十宫主与上升主互换星座 与王有大关联

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Other related effects be guessed by you based on the relationship of the Lords of Lagn and of Karm Bhava

### 判断方法路

- Yogas For Royal Association
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 上升主或十宫主的身份事实缺失时停止。
- 两主是否互换星座的事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
