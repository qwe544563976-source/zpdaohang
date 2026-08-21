---
method: ch13-v11-high-varga-effortless-wealth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 不劳而获的财富：二宫主与吉星同宫且处于高等级分盘

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我家里的钱是不是来得轻松
- 二宫主在高等级分盘里代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫主（Dhan's Lord）是否与吉星同宫

## 按情况检查的事实

- 二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Paravatāńś 等级
- 二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Devalokāńś 等级
- 二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Brahmalokāńś 等级
- 二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Sakravahanāńś 等级
- 二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Sridhamāńś 等级

## 依赖方法

- 无

## 执行步骤

### ch13-v11-high-varga-effortless-wealth.step-001

- 动作：先核对二宫主是否与吉星同宫，再核对它在 Dash Varg 分盘方案中是否达到 Paravatāńś 一类高等级。
- 适用范围：仅限本命盘二宫（Dhan Bhava）财富主题；括号内 Paravatāńś、Devalokāńś、Brahmalokāńś、Sakravahanāńś、Sridhamāńś 名单出自英译者 Santhanam 的注文（“Paravatāńśdau” of the text denotes…），其结论强度不与作者自断等同。
- 原文最小意思：二宫主（Dhan’s Lord）与吉星同宫，并处于 Paravatāńś 这类良好分盘等级时，命主家中不费力气就得到各种财富；英译者注把这类等级列为 Dash Varg 分盘方案中的 Paravatāńś、Devalokāńś、Brahmalokāńś、Sakravahanāńś、Sridhamāńś。
- 本步骤产出事实：["二宫主高等级分盘的不劳而获判定"]
- 所需事实：["二宫主（Dhan's Lord）是否与吉星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否与吉星同宫"}, {"operator": "OR", "operands": [{"fact_key": "二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Paravatāńś 等级"}, {"fact_key": "二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Devalokāńś 等级"}, {"fact_key": "二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Brahmalokāńś 等级"}, {"fact_key": "二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Sakravahanāńś 等级"}, {"fact_key": "二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Sridhamāńś 等级"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "二宫主（Dhan's Lord）是否与吉星同宫"}, "required_fact_keys": ["二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Paravatāńś 等级"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Paravatāńś 等级"}, "selection_group": "ch13-v11-high-varga-effortless-wealth.step-001:dash-varg-grade", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Paravatāńś 等级。"}, {"when": {"fact_key": "二宫主（Dhan's Lord）是否与吉星同宫"}, "required_fact_keys": ["二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Devalokāńś 等级"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Devalokāńś 等级"}, "selection_group": "ch13-v11-high-varga-effortless-wealth.step-001:dash-varg-grade", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Devalokāńś 等级。"}, {"when": {"fact_key": "二宫主（Dhan's Lord）是否与吉星同宫"}, "required_fact_keys": ["二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Brahmalokāńś 等级"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Brahmalokāńś 等级"}, "selection_group": "ch13-v11-high-varga-effortless-wealth.step-001:dash-varg-grade", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Brahmalokāńś 等级。"}, {"when": {"fact_key": "二宫主（Dhan's Lord）是否与吉星同宫"}, "required_fact_keys": ["二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Sakravahanāńś 等级"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Sakravahanāńś 等级"}, "selection_group": "ch13-v11-high-varga-effortless-wealth.step-001:dash-varg-grade", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Sakravahanāńś 等级。"}, {"when": {"fact_key": "二宫主（Dhan's Lord）是否与吉星同宫"}, "required_fact_keys": ["二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Sridhamāńś 等级"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Sridhamāńś 等级"}, "selection_group": "ch13-v11-high-varga-effortless-wealth.step-001:dash-varg-grade", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）在 Dash Varg 分盘方案中是否达到 Sridhamāńś 等级。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把英译者注列出的 Varga 名单当成作者自断的独立断语。", "不得据此推断财富数额或得财时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫主（Dhan's Lord）是否与吉星同宫。
- 缺失即停字段：["二宫主（Dhan's Lord）是否与吉星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v11`｜PDF [28]｜“If Dhan’s Lord is yuti with a benefic and is in a good division, like Paravatāńś, there will be effortlessly all kinds of wealth in the native’s family.”
  - `bphs-97:santhanam:ch13:v11`｜PDF [28]｜“Dhan’s Lord should be in Paravatāńś, or in Devalokāńś, Brahmalokāńś, Sakravahanāńś, or Sridhamāńś in the Dash Varg scheme”


## 四路查书计划

### 支持路

- If Dhan’s Lord is yuti with a benefic and is in a good division, like Paravatāńś, there will be effortlessly all kinds of wealth in the native’s family
- 二宫主与吉星同宫 Paravatāńś 高等级 Varga 不劳而获 财富

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava, while the Lord of Labh Bhava is also so placed and Dhan Bhava is occupied by a malefic
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avast
- There will be penury right from birth and the native will have to beg even for his food

### 适用边界路

- In the Dasha Varg scheme the designations commence from Parijata etc., such as 2 good Vargas - Parijatha, 3 Uttama, 4 Gopur, 5 Simhasan, 6 Paravata, 7 Devaloka, 8 Brahmaloka, 9 Sakravahana and 10 Vargas - Shridham
- Add Dashāńś, Shodashāńś and Shashtiāńś to the said Sapt Varg Divisions to get the scheme of Dasha Varg
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics

### 判断方法路

- Lagn’s Lord in Parijatāńś will make one happy, in Vargottama will give immunity to diseases, in Gopurāńś will make one rich with wealth and grains
- If the Lord of a Kendr is in Parijatāńś, the native will be liberal, if in Uttamāńś, will be highly liberal, if in Gopurāńś, will be endowed with prowess
- 判断分盘等级要看十种分盘中有几个好 Varga

## 上游问题

- 无

## 停止条件

- 缺少二宫主与吉星同宫的事实时停止。
- 五个 Varga 等级分支事实全缺时停止。
- 吉星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
