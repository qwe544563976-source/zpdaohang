---
method: ch15-v10-14-conveyance-benefic-malefic
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 车乘的吉凶与安全：吉星或凶星与四宫及其宫主的关系

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我开车安不安全
- 我的车会不会出事故或损失

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 是否有吉星与四宫（Bandhu Bhava）及其宫主发生关系
- 是否有凶星与四宫（Bandhu Bhava）及其宫主发生关系
- 命盘中哪些行星为吉星
- 命盘中哪些行星为凶星

## 按情况检查的事实

- 是否有吉星落四宫（Bandhu）
- 是否有吉星相照四宫（Bandhu）
- 是否有吉星与四宫主（Lord of Bandhu）同处
- 是否有吉星相照四宫主（Lord of Bandhu Bhava）
- 是否有凶星落四宫（Bandhu）
- 是否有凶星相照四宫（Bandhu）
- 是否有凶星与四宫主（Lord of Bandhu）同处
- 是否有凶星相照四宫主（Lord of Bandhu Bhava）

## 依赖方法

- 无

## 执行步骤

### ch15-v10-14-conveyance-benefic-malefic.step-001

- 动作：核对是否有吉星与四宫及其宫主发生关系，判断车乘方面的吉利效果。
- 适用范围：仅限吉星与四宫及其宫主发生关系时的车乘效果；原文未给时间限定。
- 原文最小意思：吉星与四宫（Bandhu Bhava）及其宫主发生关系时，会带来关于车乘的吉利效果。
- 本步骤产出事实：["四宫吉星带来的车乘吉利判定"]
- 所需事实：["是否有吉星与四宫（Bandhu Bhava）及其宫主发生关系"]
- 条件关系：{"fact_key": "是否有吉星与四宫（Bandhu Bhava）及其宫主发生关系"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把车乘方面的吉利效果扩展到住房、母亲等其他四宫事项。", "不得据此推断得车年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：是否有吉星与四宫（Bandhu Bhava）及其宫主发生关系。
- 缺失即停字段：["是否有吉星与四宫（Bandhu Bhava）及其宫主发生关系"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v10-14`｜PDF [30]｜“A benefic, related to Bandhu Bhava (and to its Lord), will bring with him auspicious effects (regarding conveyances), while a malefic will produce only malefic effects (in respect of conveyances).”

### ch15-v10-14-conveyance-benefic-malefic.step-002

- 动作：另行核对是否有凶星与四宫及其宫主发生关系，判断车乘方面的凶恶效果。
- 适用范围：仅限凶星与四宫及其宫主发生关系时的车乘效果；原文未给时间限定。
- 原文最小意思：凶星与四宫（Bandhu Bhava）及其宫主发生关系时，只会产生关于车乘的凶恶效果。
- 本步骤产出事实：["四宫凶星带来的车乘凶恶判定"]
- 所需事实：["是否有凶星与四宫（Bandhu Bhava）及其宫主发生关系"]
- 条件关系：{"fact_key": "是否有凶星与四宫（Bandhu Bhava）及其宫主发生关系"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把车乘方面的凶恶效果扩展到住房、母亲等其他四宫事项。", "不得据此推断事故的具体时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：是否有凶星与四宫（Bandhu Bhava）及其宫主发生关系。
- 缺失即停字段：["是否有凶星与四宫（Bandhu Bhava）及其宫主发生关系"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v10-14`｜PDF [30]｜“A benefic, related to Bandhu Bhava (and to its Lord), will bring with him auspicious effects (regarding conveyances), while a malefic will produce only malefic effects (in respect of conveyances).”

### ch15-v10-14-conveyance-benefic-malefic.step-003

- 动作：逐一核对吉星是否落四宫、相照四宫、与四宫主同处、或相照四宫主，判断车乘之乐与是否免于事故。
- 适用范围：仅限原文列出的吉星与四宫或四宫主的四种关系及其车乘结果；原文未给时间限定。
- 原文最小意思：吉星落四宫（Bandhu）、相照四宫、与四宫主同处、或相照四宫主时，命主在车乘上快乐，并免于事故与危险。
- 本步骤产出事实：["车乘之乐与免于事故判定"]
- 所需事实：["命盘中哪些行星为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "命盘中哪些行星为吉星"}, {"operator": "OR", "operands": [{"fact_key": "是否有吉星落四宫（Bandhu）"}, {"fact_key": "是否有吉星相照四宫（Bandhu）"}, {"fact_key": "是否有吉星与四宫主（Lord of Bandhu）同处"}, {"fact_key": "是否有吉星相照四宫主（Lord of Bandhu Bhava）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "命盘中哪些行星为吉星"}, "required_fact_keys": ["是否有吉星落四宫（Bandhu）"], "branch_condition_logic": {"fact_key": "是否有吉星落四宫（Bandhu）"}, "selection_group": "ch15-v10-14-conveyance-benefic-malefic.step-003:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有吉星落四宫（Bandhu）。"}, {"when": {"fact_key": "命盘中哪些行星为吉星"}, "required_fact_keys": ["是否有吉星相照四宫（Bandhu）"], "branch_condition_logic": {"fact_key": "是否有吉星相照四宫（Bandhu）"}, "selection_group": "ch15-v10-14-conveyance-benefic-malefic.step-003:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有吉星相照四宫（Bandhu）。"}, {"when": {"fact_key": "命盘中哪些行星为吉星"}, "required_fact_keys": ["是否有吉星与四宫主（Lord of Bandhu）同处"], "branch_condition_logic": {"fact_key": "是否有吉星与四宫主（Lord of Bandhu）同处"}, "selection_group": "ch15-v10-14-conveyance-benefic-malefic.step-003:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有吉星与四宫主（Lord of Bandhu）同处。"}, {"when": {"fact_key": "命盘中哪些行星为吉星"}, "required_fact_keys": ["是否有吉星相照四宫主（Lord of Bandhu Bhava）"], "branch_condition_logic": {"fact_key": "是否有吉星相照四宫主（Lord of Bandhu Bhava）"}, "selection_group": "ch15-v10-14-conveyance-benefic-malefic.step-003:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有吉星相照四宫主（Lord of Bandhu Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把免于事故扩展成终生绝对安全。", "不得把这四种关系以外的关系也算作成立条件。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：命盘中哪些行星为吉星。
- 缺失即停字段：["命盘中哪些行星为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v10-14`｜PDF [30]｜“Should a benefic be in Bandhu, drishti Bandhu, or in yuti with the Lord of Bandhu, or a Drishti on the Lord of Bandhu Bhava, then the native will be happy with conveyances and be free from accidents and dangers.”

### ch15-v10-14-conveyance-benefic-malefic.step-004

- 动作：核对是否有凶星取代前一句所说的吉星，占据同样四种关系之一，判断车辆损失与严重事故。
- 适用范围：仅限凶星取代前句吉星时的车辆损失与事故结果；原文未给时间限定。
- 原文最小意思：凶星取代前述吉星时，会造成车辆方面的损失，并使人遭遇严重事故。
- 本步骤产出事实：["车辆损失与严重事故判定"]
- 所需事实：["命盘中哪些行星为凶星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "命盘中哪些行星为凶星"}, {"operator": "OR", "operands": [{"fact_key": "是否有凶星落四宫（Bandhu）"}, {"fact_key": "是否有凶星相照四宫（Bandhu）"}, {"fact_key": "是否有凶星与四宫主（Lord of Bandhu）同处"}, {"fact_key": "是否有凶星相照四宫主（Lord of Bandhu Bhava）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "命盘中哪些行星为凶星"}, "required_fact_keys": ["是否有凶星落四宫（Bandhu）"], "branch_condition_logic": {"fact_key": "是否有凶星落四宫（Bandhu）"}, "selection_group": "ch15-v10-14-conveyance-benefic-malefic.step-004:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有凶星落四宫（Bandhu）。"}, {"when": {"fact_key": "命盘中哪些行星为凶星"}, "required_fact_keys": ["是否有凶星相照四宫（Bandhu）"], "branch_condition_logic": {"fact_key": "是否有凶星相照四宫（Bandhu）"}, "selection_group": "ch15-v10-14-conveyance-benefic-malefic.step-004:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有凶星相照四宫（Bandhu）。"}, {"when": {"fact_key": "命盘中哪些行星为凶星"}, "required_fact_keys": ["是否有凶星与四宫主（Lord of Bandhu）同处"], "branch_condition_logic": {"fact_key": "是否有凶星与四宫主（Lord of Bandhu）同处"}, "selection_group": "ch15-v10-14-conveyance-benefic-malefic.step-004:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有凶星与四宫主（Lord of Bandhu）同处。"}, {"when": {"fact_key": "命盘中哪些行星为凶星"}, "required_fact_keys": ["是否有凶星相照四宫主（Lord of Bandhu Bhava）"], "branch_condition_logic": {"fact_key": "是否有凶星相照四宫主（Lord of Bandhu Bhava）"}, "selection_group": "ch15-v10-14-conveyance-benefic-malefic.step-004:malefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：是否有凶星相照四宫主（Lord of Bandhu Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断事故年份、伤情程度或车辆价值。", "the said benefic 只指同一段前一句列出的四种吉星关系，不得另行扩充。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：命盘中哪些行星为凶星。
- 缺失即停字段：["命盘中哪些行星为凶星"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v10-14`｜PDF [30]｜“A malefic, replacing the said benefic, will cause losses, concerning vehicles and reduce one to severe accidents.”


## 四路查书计划

### 支持路

- benefic in Bandhu drishti yuti Lord of Bandhu happy with conveyances free from accidents
- 吉星落四宫 相照四宫主 车乘平安

### 反例或取消路

- malefic replacing benefic losses concerning vehicles severe accidents
- 凶星取代吉星 车辆损失 严重事故

### 适用边界路

- which relations count as related to Bandhu Bhava and its Lord
- 与四宫及其宫主发生关系的适用边界

### 判断方法路

- how to judge vehicle safety and losses in BPHS
- 判断车乘安全与损失要查什么

## 上游问题

- 无

## 停止条件

- 无法确定哪些行星为吉星或凶星时停止。
- 缺少吉星或凶星与四宫及四宫主关系的事实时停止。
- 只知道行星吉凶但不知其与四宫的具体关系时不得下结论。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
