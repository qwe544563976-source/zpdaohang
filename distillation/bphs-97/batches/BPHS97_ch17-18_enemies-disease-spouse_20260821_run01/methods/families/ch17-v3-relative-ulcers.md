---
method: ch17-v3-relative-ulcers
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 亲属的溃疡瘀伤：亲属指示星或其宫主与六宫主同宫、落六宫或落八宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲身上会不会有疮或伤
- 家里长辈的健康外伤怎么看

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 所论亲属的指示星（Karak）是哪颗行星
- 所论亲属对应宫位的宫主是哪颗行星

## 按情况检查的事实

- 所论亲属的指示星（Karak）是否与六宫主（Ari's Lord）同宫
- 所论亲属的指示星（Karak）是否落六宫（Ari）
- 所论亲属的指示星（Karak）是否落八宫（Randhr）
- 所论亲属对应宫位的宫主是否与六宫主（Ari's Lord）同宫
- 所论亲属对应宫位的宫主是否落六宫（Ari）
- 所论亲属对应宫位的宫主是否落八宫（Randhr）

## 依赖方法

- 无

## 执行步骤

### ch17-v3-relative-ulcers.step-001

- 动作：核对所论亲属的指示星（Karak）或该亲属宫位的宫主与六宫（Ari）、八宫（Randhr）及六宫主的关系。
- 适用范围：原文以亲属（举父亲为例）立说，未限定是哪一位亲属，也未给时间限定；指示星的判定原文未给判准。
- 原文最小意思：亲属的指示星或该亲属宫位的宫主与六宫主同宫、落六宫或落八宫时，指示该亲属（如父亲）有溃疡或瘀伤。
- 本步骤产出事实：["亲属溃疡瘀伤判定"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "所论亲属的指示星（Karak）是否与六宫主（Ari's Lord）同宫"}, {"fact_key": "所论亲属的指示星（Karak）是否落六宫（Ari）"}, {"fact_key": "所论亲属的指示星（Karak）是否落八宫（Randhr）"}, {"fact_key": "所论亲属对应宫位的宫主是否与六宫主（Ari's Lord）同宫"}, {"fact_key": "所论亲属对应宫位的宫主是否落六宫（Ari）"}, {"fact_key": "所论亲属对应宫位的宫主是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否与六宫主（Ari's Lord）同宫"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否与六宫主（Ari's Lord）同宫"}, "selection_group": "ch17-v3-relative-ulcers.step-001:kin-graha-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否与六宫主（Ari's Lord）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否落六宫（Ari）"}, "selection_group": "ch17-v3-relative-ulcers.step-001:kin-graha-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否落八宫（Randhr）"}, "selection_group": "ch17-v3-relative-ulcers.step-001:kin-graha-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否落八宫（Randhr）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否与六宫主（Ari's Lord）同宫"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否与六宫主（Ari's Lord）同宫"}, "selection_group": "ch17-v3-relative-ulcers.step-001:kin-graha-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否与六宫主（Ari's Lord）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否落六宫（Ari）"}, "selection_group": "ch17-v3-relative-ulcers.step-001:kin-graha-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否落八宫（Randhr）"}, "selection_group": "ch17-v3-relative-ulcers.step-001:kin-graha-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断该亲属的寿命、死因或事发年份。", "不得把结论从所论的那位亲属扩大到全部亲属。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应宫位的宫主是哪颗行星。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“The Karak of a relative, or the Lord of such a Bhava, joining Ari’s Lord, or being in Ari, or Randhr Bhava, indicates ulcers/bruises to such a relative, like father.”


## 四路查书计划

### 支持路

- The Karak of a relative, or the Lord of such a Bhava, joining Ari’s Lord ulcers to such a relative
- 亲属指示星 落六宫 八宫 溃疡

### 反例或取消路

- The limb, related to a benefic, will have a mark So say the Jyotishis
- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed

### 适用边界路

- Constant Karakatwas the stronger among Surya and Shukra indicates the father
- The 9th from Surya denotes father, the 4th from Chandra mother

### 判断方法路

- Bhavas Related these constant significances are derivable from the Bhavas
- 如何为每位亲属选定指示星与宫位

## 上游问题

- 无

## 停止条件

- 缺少所论亲属的指示星身份事实时停止。
- 缺少所论亲属宫位宫主身份事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
