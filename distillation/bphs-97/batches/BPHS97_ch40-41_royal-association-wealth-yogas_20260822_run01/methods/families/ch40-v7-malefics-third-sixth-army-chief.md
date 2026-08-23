---
method: ch40-v7-malefics-third-sixth-army-chief
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 成为军队统帅：凶星落 Atma Karak 或 Arudh Lagna 起第 3 与第 6 位，或落三宫与六宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我适不适合带兵这类硬派差事
- 我会不会走武职这条路

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星

## 按情况检查的事实

- Atma Karak 起第 3 宫内是否有凶星
- Atma Karak 起第 6 宫内是否有凶星
- Arudh Lagn 起第 3 宫内是否有凶星
- Arudh Lagn 起第 6 宫内是否有凶星
- 三宫（Sahaj）是否被凶星占据
- 六宫（Ari）是否被凶星占据

## 依赖方法

- 无

## 执行步骤

### ch40-v7-malefics-third-sixth-army-chief.step-001

- 动作：先取凶星名册，再分别从 Atma Karak、Arudh Lagna 起算第 3 位与第 6 位，或直接看本命三宫（Sahaj）与六宫（Ari），核对这两处是否都有凶星。
- 适用范围：仅限本命盘的凶星分布；原文本偈未给凶星判准，须另按本书第 3 章的吉凶星名册取得；Arudh Lagna 的算法本偈未给，须另按本书 Arudh 一章取得；原文未给时间限定。
- 原文最小意思：凶星落在 Atma Karak 起第 3 位与第 6 位，或落在 Arudh Lagna 起第 3 位与第 6 位，或落在三宫（Sahaj）与六宫（Ari）时，命主将成为军队统帅。
- 本步骤产出事实：["凶星居第三第六位的军队统帅判定"]
- 所需事实：["本盘中哪些行星被判为凶星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "Atma Karak 起第 3 宫内是否有凶星"}, {"fact_key": "Atma Karak 起第 6 宫内是否有凶星"}]}, {"operator": "AND", "operands": [{"fact_key": "Arudh Lagn 起第 3 宫内是否有凶星"}, {"fact_key": "Arudh Lagn 起第 6 宫内是否有凶星"}]}, {"operator": "AND", "operands": [{"fact_key": "三宫（Sahaj）是否被凶星占据"}, {"fact_key": "六宫（Ari）是否被凶星占据"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些行星被判为凶星"}, "required_fact_keys": ["Atma Karak 起第 3 宫内是否有凶星", "Atma Karak 起第 6 宫内是否有凶星"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Atma Karak 起第 3 宫内是否有凶星"}, {"fact_key": "Atma Karak 起第 6 宫内是否有凶星"}]}, "selection_group": "ch40-v7-malefics-third-sixth-army-chief.step-001:reckoned-from", "stop_condition": "选中该分支后，缺少以下事实即停止：Atma Karak 起第 3 宫内是否有凶星、Atma Karak 起第 6 宫内是否有凶星。"}, {"when": {"fact_key": "本盘中哪些行星被判为凶星"}, "required_fact_keys": ["Arudh Lagn 起第 3 宫内是否有凶星", "Arudh Lagn 起第 6 宫内是否有凶星"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "Arudh Lagn 起第 3 宫内是否有凶星"}, {"fact_key": "Arudh Lagn 起第 6 宫内是否有凶星"}]}, "selection_group": "ch40-v7-malefics-third-sixth-army-chief.step-001:reckoned-from", "stop_condition": "选中该分支后，缺少以下事实即停止：Arudh Lagn 起第 3 宫内是否有凶星、Arudh Lagn 起第 6 宫内是否有凶星。"}, {"when": {"fact_key": "本盘中哪些行星被判为凶星"}, "required_fact_keys": ["三宫（Sahaj）是否被凶星占据", "六宫（Ari）是否被凶星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "三宫（Sahaj）是否被凶星占据"}, {"fact_key": "六宫（Ari）是否被凶星占据"}]}, "selection_group": "ch40-v7-malefics-third-sixth-army-chief.step-001:reckoned-from", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫（Sahaj）是否被凶星占据、六宫（Ari）是否被凶星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文在每条起算法下都同时要求第 3 位与第 6 位有凶星，不得只满足一处就下断。", "不得据此推断兵种、军衔或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星。
- 缺失即停字段：["本盘中哪些行星被判为凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v7`｜PDF [85]｜“Should malefics be in the 3<sup>rd</sup> and the 6<sup>th</sup> from Atma Karak, or from Arudh Lagna, or in Sahaj and Ari Bhava, one will become Army chief.”


## 四路查书计划

### 支持路

- Should malefics be in the 3<sup>rd</sup> and the 6<sup>th</sup> from Atma Karak, or from Arudh Lagna, or in Sahaj and Ari Bhava, one will become Army chief
- 凶星在 Atma Karak 或 Arudh Lagna 起第三第六 军队统帅

### 反例或取消路

- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Karakāńś is the Navāńś, occupied by the Atma Karak Grah

### 判断方法路

- Yogas For Royal Association
- If malefics be in Karakāńś, Arudh Lagn and the 2<sup>nd</sup> and 8<sup>th</sup> from these places

## 上游问题

- 无

## 停止条件

- 凶星名册未定时停止：须先按 BPHS 自己的吉凶星定义取名册。
- 三条起算法的位置事实全部缺失时停止。
- Arudh Lagna 未按本书 Arudh 一章算出时，该分支停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
