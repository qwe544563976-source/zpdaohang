---
method: ch16-v8-issues-with-difficulty
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 得子艰难：五宫主落凶宫、敌星座、落陷或落回五宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我生孩子会不会很难
- 我要不要做好难有孩子的准备

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫主是哪颗行星

## 按情况检查的事实

- 五宫主是否落在第六宫（Ari Bhava）
- 五宫主是否落在第八宫（Randhr Bhava）
- 五宫主是否落在第十二宫（Vyaya Bhava）
- 五宫主是否落在敌星座
- 五宫主是否处于落陷状态
- 五宫主是否落在第五宫本宫

## 依赖方法

- 无

## 执行步骤

### ch16-v8-issues-with-difficulty.step-001

- 动作：先定出五宫主是哪颗行星，再逐一核对它是否落第六、第八、第十二宫、敌星座、落陷或落回第五宫。
- 适用范围：仅限本命盘得子难易主题；原文只列这六种落点，未给子女人数、性别或时间。
- 原文最小意思：五宫主落六宫、八宫、十二宫，或落敌星座，或落陷，或落五宫本宫时，得子艰难。
- 本步骤产出事实：["五宫主落点不利得子艰难判定"]
- 所需事实：["本盘五宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘五宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "五宫主是否落在第六宫（Ari Bhava）"}, {"fact_key": "五宫主是否落在第八宫（Randhr Bhava）"}, {"fact_key": "五宫主是否落在第十二宫（Vyaya Bhava）"}, {"fact_key": "五宫主是否落在敌星座"}, {"fact_key": "五宫主是否处于落陷状态"}, {"fact_key": "五宫主是否落在第五宫本宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否落在第六宫（Ari Bhava）"], "branch_condition_logic": {"fact_key": "五宫主是否落在第六宫（Ari Bhava）"}, "selection_group": "ch16-v8-issues-with-difficulty.step-001:unfavourable-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落在第六宫（Ari Bhava）。"}, {"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否落在第八宫（Randhr Bhava）"], "branch_condition_logic": {"fact_key": "五宫主是否落在第八宫（Randhr Bhava）"}, "selection_group": "ch16-v8-issues-with-difficulty.step-001:unfavourable-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落在第八宫（Randhr Bhava）。"}, {"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否落在第十二宫（Vyaya Bhava）"], "branch_condition_logic": {"fact_key": "五宫主是否落在第十二宫（Vyaya Bhava）"}, "selection_group": "ch16-v8-issues-with-difficulty.step-001:unfavourable-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落在第十二宫（Vyaya Bhava）。"}, {"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否落在敌星座"], "branch_condition_logic": {"fact_key": "五宫主是否落在敌星座"}, "selection_group": "ch16-v8-issues-with-difficulty.step-001:unfavourable-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落在敌星座。"}, {"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否处于落陷状态"], "branch_condition_logic": {"fact_key": "五宫主是否处于落陷状态"}, "selection_group": "ch16-v8-issues-with-difficulty.step-001:unfavourable-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否处于落陷状态。"}, {"when": {"fact_key": "本盘五宫主是哪颗行星"}, "required_fact_keys": ["五宫主是否落在第五宫本宫"], "branch_condition_logic": {"fact_key": "五宫主是否落在第五宫本宫"}, "selection_group": "ch16-v8-issues-with-difficulty.step-001:unfavourable-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫主是否落在第五宫本宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把“艰难”升级成无子或子女夭折。", "不得据此推断得子的年龄或年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫主是哪颗行星。
- 缺失即停字段：["本盘五宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v8`｜PDF [30]｜“If Putr’s Lord is in Ari, Randhr, or Vyaya Bhava, or be in an inimical Rāśi, or be in fall, or in Putr itself, the native will beget issues with difficulty.”


## 四路查书计划

### 支持路

- Putr’s Lord inimical Rāśi in fall beget issues with difficulty
- 五宫主落敌星座 落陷 得子艰难

### 反例或取消路

- Putr’s Lord in own Rāśi angle trine happiness through children
- 五宫主落吉位 子女顺利 反例

### 适用边界路

- difficulty in begetting issues rule boundary
- 得子艰难断语的适用边界

### 判断方法路

- how to evaluate Putr’s Lord dignity and house
- 怎样评估五宫主的落宫与庙陷友敌

## 上游问题

- 无

## 停止条件

- 缺少五宫主行星身份事实时停止。
- 缺少五宫主落宫或庙陷友敌事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
