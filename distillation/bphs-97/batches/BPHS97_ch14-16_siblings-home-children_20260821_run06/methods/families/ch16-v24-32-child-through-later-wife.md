---
method: ch16-v24-32-child-through-later-wife
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 子嗣出自后妻：五宫有凶星或土星落木星起第5宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的孩子会是第几任配偶生的
- 我第一段婚姻会不会没有孩子

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星

## 按情况检查的事实

- 五宫是否有凶星在内
- 土星是否落于木星起第5宫

## 依赖方法

- 无

## 执行步骤

### ch16-v24-32-child-through-later-wife.step-001

- 动作：先取得本盘凶星名单，再核对五宫内是否有凶星、或土星是否落木星起第5宫，判断子嗣是否只能出自第二或第三位妻子。
- 适用范围：仅限本命五宫子嗣来源主题；原文只讲第二或第三位妻子，未给时间或上升限定。
- 原文最小意思：五宫中有凶星，或土星落木星起第5宫时，此人只能通过第二或第三位妻子得到子嗣。
- 本步骤产出事实：["子嗣出自第二或第三位妻子判定"]
- 所需事实：["本盘中哪些行星被判为凶星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"operator": "OR", "operands": [{"fact_key": "五宫是否有凶星在内"}, {"fact_key": "土星是否落于木星起第5宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些行星被判为凶星"}, "required_fact_keys": ["五宫是否有凶星在内"], "branch_condition_logic": {"fact_key": "五宫是否有凶星在内"}, "selection_group": "ch16-v24-32-child-through-later-wife.step-001:either-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫是否有凶星在内。"}, {"when": {"fact_key": "本盘中哪些行星被判为凶星"}, "required_fact_keys": ["土星是否落于木星起第5宫"], "branch_condition_logic": {"fact_key": "土星是否落于木星起第5宫"}, "selection_group": "ch16-v24-32-child-through-later-wife.step-001:either-condition", "stop_condition": "选中该分支后，缺少以下事实即停止：土星是否落于木星起第5宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断离婚、再婚的时间或原因。", "不得把第二或第三位妻子扩大成更多次婚姻。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星。
- 缺失即停字段：["本盘中哪些行星被判为凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v24-32`｜PDF [31, 32]｜“If Putr Bhava has a malefic in it, or, if Shani is in the 5<sup>th</sup> from Guru, the native will beget offspring only through his second, or third wife.”


## 四路查书计划

### 支持路

- offspring only through his second or third wife malefic in Putr Bhava
- 五宫有凶星 土星在木星第5宫 后妻得子

### 反例或取消路

- 五宫有吉星 第一位妻子得子

### 适用边界路

- 子嗣出自后妻断语的适用边界

### 判断方法路

- 判断子嗣来自哪位配偶要看什么

## 上游问题

- 无

## 停止条件

- 缺少五宫内凶星事实时停止。
- 缺少土星相对木星位置事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
