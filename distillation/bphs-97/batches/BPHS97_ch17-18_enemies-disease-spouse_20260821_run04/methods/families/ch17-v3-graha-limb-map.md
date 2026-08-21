---
method: ch17-v3-graha-limb-map
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 亲属受累部位对照：具此主管关系并落六宫或八宫的行星各主一处肢体

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我父亲身上哪个部位容易出问题
- 亲属的伤病在身体哪个部位

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

- 所论亲属的指示星（Karak）是否为太阳（Surya）
- 所论亲属对应宫位的宫主是否为太阳（Surya）
- 太阳（Surya）是否落六宫（Ari）
- 太阳（Surya）是否落八宫（Randhr）
- 所论亲属的指示星（Karak）是否为月亮（Chandra）
- 所论亲属对应宫位的宫主是否为月亮（Chandra）
- 月亮（Chandra）是否落六宫（Ari）
- 月亮（Chandra）是否落八宫（Randhr）
- 所论亲属的指示星（Karak）是否为火星（Mangal）
- 所论亲属对应宫位的宫主是否为火星（Mangal）
- 火星（Mangal）是否落六宫（Ari）
- 火星（Mangal）是否落八宫（Randhr）
- 所论亲属的指示星（Karak）是否为水星（Budh）
- 所论亲属对应宫位的宫主是否为水星（Budh）
- 水星（Budh）是否落六宫（Ari）
- 水星（Budh）是否落八宫（Randhr）
- 所论亲属的指示星（Karak）是否为木星（Guru）
- 所论亲属对应宫位的宫主是否为木星（Guru）
- 木星（Guru）是否落六宫（Ari）
- 木星（Guru）是否落八宫（Randhr）
- 所论亲属的指示星（Karak）是否为金星（Shukra）
- 所论亲属对应宫位的宫主是否为金星（Shukra）
- 金星（Shukra）是否落六宫（Ari）
- 金星（Shukra）是否落八宫（Randhr）
- 所论亲属的指示星（Karak）是否为土星（Shani）
- 所论亲属对应宫位的宫主是否为土星（Shani）
- 土星（Shani）是否落六宫（Ari）
- 土星（Shani）是否落八宫（Randhr）
- 所论亲属的指示星（Karak）是否为罗睺（Rahu）
- 所论亲属对应宫位的宫主是否为罗睺（Rahu）
- 罗睺（Rahu）是否落六宫（Ari）
- 罗睺（Rahu）是否落八宫（Randhr）
- 所论亲属的指示星（Karak）是否为计都（Ketu）
- 所论亲属对应宫位的宫主是否为计都（Ketu）
- 计都（Ketu）是否落六宫（Ari）
- 计都（Ketu）是否落八宫（Randhr）

## 依赖方法

- ch17-v3-relative-ulcers

## 执行步骤

### ch17-v3-graha-limb-map.step-001

- 动作：核对太阳（Surya）是否兼具所论亲属的主管关系并落六宫或八宫，据以定受累部位。
- 适用范围：承接同偈前句「亲属指示星或其宫位宫主落六宫、八宫」的安排；原文未给时间限定，也未说该部位一定发病。
- 原文最小意思：太阳具有该亲属的主管关系并落在该宫时，指示头部受到该种影响。
- 本步骤产出事实：["亲属受累部位判定（太阳）"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "所论亲属的指示星（Karak）是否为太阳（Surya）"}, {"fact_key": "所论亲属对应宫位的宫主是否为太阳（Surya）"}]}, {"operator": "OR", "operands": [{"fact_key": "太阳（Surya）是否落六宫（Ari）"}, {"fact_key": "太阳（Surya）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否为太阳（Surya）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否为太阳（Surya）"}, "selection_group": "ch17-v3-graha-limb-map.step-001:surya-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否为太阳（Surya）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否为太阳（Surya）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否为太阳（Surya）"}, "selection_group": "ch17-v3-graha-limb-map.step-001:surya-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否为太阳（Surya）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["太阳（Surya）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否落六宫（Ari）"}, "selection_group": "ch17-v3-graha-limb-map.step-001:surya-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["太阳（Surya）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "太阳（Surya）是否落八宫（Randhr）"}, "selection_group": "ch17-v3-graha-limb-map.step-001:surya-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：太阳（Surya）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此把太阳与该部位的对应扩大到没有此种主管关系的情形。", "不得据此推断病症名称、轻重或发生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应宫位的宫主是哪颗行星。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“Surya with such lordship and in such a Bhava denotes such affectation of head”

### ch17-v3-graha-limb-map.step-002

- 动作：核对月亮（Chandra）是否兼具所论亲属的主管关系并落六宫或八宫，据以定受累部位。
- 适用范围：承接同偈前句「亲属指示星或其宫位宫主落六宫、八宫」的安排；原文未给时间限定，也未说该部位一定发病。
- 原文最小意思：月亮具有该亲属的主管关系并落在该宫时，指示面部受到该种影响。
- 本步骤产出事实：["亲属受累部位判定（月亮）"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "所论亲属的指示星（Karak）是否为月亮（Chandra）"}, {"fact_key": "所论亲属对应宫位的宫主是否为月亮（Chandra）"}]}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否落六宫（Ari）"}, {"fact_key": "月亮（Chandra）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否为月亮（Chandra）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否为月亮（Chandra）"}, "selection_group": "ch17-v3-graha-limb-map.step-002:chandra-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否为月亮（Chandra）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否为月亮（Chandra）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否为月亮（Chandra）"}, "selection_group": "ch17-v3-graha-limb-map.step-002:chandra-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否为月亮（Chandra）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["月亮（Chandra）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落六宫（Ari）"}, "selection_group": "ch17-v3-graha-limb-map.step-002:chandra-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["月亮（Chandra）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落八宫（Randhr）"}, "selection_group": "ch17-v3-graha-limb-map.step-002:chandra-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此把月亮与该部位的对应扩大到没有此种主管关系的情形。", "不得据此推断病症名称、轻重或发生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应宫位的宫主是哪颗行星。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“with such lordship and in such a Bhava denotes such affectation”
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“Chandra of the face”

### ch17-v3-graha-limb-map.step-003

- 动作：核对火星（Mangal）是否兼具所论亲属的主管关系并落六宫或八宫，据以定受累部位。
- 适用范围：承接同偈前句「亲属指示星或其宫位宫主落六宫、八宫」的安排；原文未给时间限定，也未说该部位一定发病。
- 原文最小意思：火星具有该亲属的主管关系并落在该宫时，指示颈部受到该种影响。
- 本步骤产出事实：["亲属受累部位判定（火星）"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "所论亲属的指示星（Karak）是否为火星（Mangal）"}, {"fact_key": "所论亲属对应宫位的宫主是否为火星（Mangal）"}]}, {"operator": "OR", "operands": [{"fact_key": "火星（Mangal）是否落六宫（Ari）"}, {"fact_key": "火星（Mangal）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否为火星（Mangal）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否为火星（Mangal）"}, "selection_group": "ch17-v3-graha-limb-map.step-003:mangal-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否为火星（Mangal）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否为火星（Mangal）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否为火星（Mangal）"}, "selection_group": "ch17-v3-graha-limb-map.step-003:mangal-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否为火星（Mangal）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["火星（Mangal）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否落六宫（Ari）"}, "selection_group": "ch17-v3-graha-limb-map.step-003:mangal-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["火星（Mangal）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否落八宫（Randhr）"}, "selection_group": "ch17-v3-graha-limb-map.step-003:mangal-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此把火星与该部位的对应扩大到没有此种主管关系的情形。", "不得据此推断病症名称、轻重或发生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应宫位的宫主是哪颗行星。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“with such lordship and in such a Bhava denotes such affectation”
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“Mangal of the neck”

### ch17-v3-graha-limb-map.step-004

- 动作：核对水星（Budh）是否兼具所论亲属的主管关系并落六宫或八宫，据以定受累部位。
- 适用范围：承接同偈前句「亲属指示星或其宫位宫主落六宫、八宫」的安排；原文未给时间限定，也未说该部位一定发病。
- 原文最小意思：水星具有该亲属的主管关系并落在该宫时，指示脐部受到该种影响。
- 本步骤产出事实：["亲属受累部位判定（水星）"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "所论亲属的指示星（Karak）是否为水星（Budh）"}, {"fact_key": "所论亲属对应宫位的宫主是否为水星（Budh）"}]}, {"operator": "OR", "operands": [{"fact_key": "水星（Budh）是否落六宫（Ari）"}, {"fact_key": "水星（Budh）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否为水星（Budh）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否为水星（Budh）"}, "selection_group": "ch17-v3-graha-limb-map.step-004:budh-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否为水星（Budh）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否为水星（Budh）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否为水星（Budh）"}, "selection_group": "ch17-v3-graha-limb-map.step-004:budh-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否为水星（Budh）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["水星（Budh）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "水星（Budh）是否落六宫（Ari）"}, "selection_group": "ch17-v3-graha-limb-map.step-004:budh-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["水星（Budh）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "水星（Budh）是否落八宫（Randhr）"}, "selection_group": "ch17-v3-graha-limb-map.step-004:budh-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此把水星与该部位的对应扩大到没有此种主管关系的情形。", "不得据此推断病症名称、轻重或发生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应宫位的宫主是哪颗行星。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“with such lordship and in such a Bhava denotes such affectation”
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“Budh of the navel”

### ch17-v3-graha-limb-map.step-005

- 动作：核对木星（Guru）是否兼具所论亲属的主管关系并落六宫或八宫，据以定受累部位。
- 适用范围：承接同偈前句「亲属指示星或其宫位宫主落六宫、八宫」的安排；原文未给时间限定，也未说该部位一定发病。
- 原文最小意思：木星具有该亲属的主管关系并落在该宫时，指示鼻部受到该种影响。
- 本步骤产出事实：["亲属受累部位判定（木星）"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "所论亲属的指示星（Karak）是否为木星（Guru）"}, {"fact_key": "所论亲属对应宫位的宫主是否为木星（Guru）"}]}, {"operator": "OR", "operands": [{"fact_key": "木星（Guru）是否落六宫（Ari）"}, {"fact_key": "木星（Guru）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否为木星（Guru）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否为木星（Guru）"}, "selection_group": "ch17-v3-graha-limb-map.step-005:guru-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否为木星（Guru）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否为木星（Guru）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否为木星（Guru）"}, "selection_group": "ch17-v3-graha-limb-map.step-005:guru-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否为木星（Guru）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["木星（Guru）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落六宫（Ari）"}, "selection_group": "ch17-v3-graha-limb-map.step-005:guru-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["木星（Guru）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落八宫（Randhr）"}, "selection_group": "ch17-v3-graha-limb-map.step-005:guru-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此把木星与该部位的对应扩大到没有此种主管关系的情形。", "不得据此推断病症名称、轻重或发生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应宫位的宫主是哪颗行星。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“with such lordship and in such a Bhava denotes such affectation”
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“Guru of the nose”

### ch17-v3-graha-limb-map.step-006

- 动作：核对金星（Shukra）是否兼具所论亲属的主管关系并落六宫或八宫，据以定受累部位。
- 适用范围：承接同偈前句「亲属指示星或其宫位宫主落六宫、八宫」的安排；原文未给时间限定，也未说该部位一定发病。
- 原文最小意思：金星具有该亲属的主管关系并落在该宫时，指示眼部受到该种影响。
- 本步骤产出事实：["亲属受累部位判定（金星）"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "所论亲属的指示星（Karak）是否为金星（Shukra）"}, {"fact_key": "所论亲属对应宫位的宫主是否为金星（Shukra）"}]}, {"operator": "OR", "operands": [{"fact_key": "金星（Shukra）是否落六宫（Ari）"}, {"fact_key": "金星（Shukra）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否为金星（Shukra）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否为金星（Shukra）"}, "selection_group": "ch17-v3-graha-limb-map.step-006:shukra-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否为金星（Shukra）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否为金星（Shukra）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否为金星（Shukra）"}, "selection_group": "ch17-v3-graha-limb-map.step-006:shukra-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否为金星（Shukra）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["金星（Shukra）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落六宫（Ari）"}, "selection_group": "ch17-v3-graha-limb-map.step-006:shukra-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["金星（Shukra）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落八宫（Randhr）"}, "selection_group": "ch17-v3-graha-limb-map.step-006:shukra-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此把金星与该部位的对应扩大到没有此种主管关系的情形。", "不得据此推断病症名称、轻重或发生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应宫位的宫主是哪颗行星。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“with such lordship and in such a Bhava denotes such affectation”
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“Shukra of the eyes”

### ch17-v3-graha-limb-map.step-007

- 动作：核对土星（Shani）是否兼具所论亲属的主管关系并落六宫或八宫，据以定受累部位。
- 适用范围：承接同偈前句「亲属指示星或其宫位宫主落六宫、八宫」的安排；原文未给时间限定，也未说该部位一定发病。
- 原文最小意思：土星具有该亲属的主管关系并落在该宫时，指示足部受到该种影响。
- 本步骤产出事实：["亲属受累部位判定（土星）"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "所论亲属的指示星（Karak）是否为土星（Shani）"}, {"fact_key": "所论亲属对应宫位的宫主是否为土星（Shani）"}]}, {"operator": "OR", "operands": [{"fact_key": "土星（Shani）是否落六宫（Ari）"}, {"fact_key": "土星（Shani）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否为土星（Shani）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否为土星（Shani）"}, "selection_group": "ch17-v3-graha-limb-map.step-007:shani-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否为土星（Shani）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否为土星（Shani）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否为土星（Shani）"}, "selection_group": "ch17-v3-graha-limb-map.step-007:shani-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否为土星（Shani）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["土星（Shani）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "土星（Shani）是否落六宫（Ari）"}, "selection_group": "ch17-v3-graha-limb-map.step-007:shani-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：土星（Shani）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["土星（Shani）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "土星（Shani）是否落八宫（Randhr）"}, "selection_group": "ch17-v3-graha-limb-map.step-007:shani-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：土星（Shani）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此把土星与该部位的对应扩大到没有此种主管关系的情形。", "不得据此推断病症名称、轻重或发生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应宫位的宫主是哪颗行星。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“with such lordship and in such a Bhava denotes such affectation”
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“Shani of the feet”

### ch17-v3-graha-limb-map.step-008

- 动作：核对罗睺（Rahu）是否兼具所论亲属的主管关系并落六宫或八宫，据以定受累部位。
- 适用范围：承接同偈前句「亲属指示星或其宫位宫主落六宫、八宫」的安排；原文未给时间限定，也未说该部位一定发病。
- 原文最小意思：罗睺（与计都同列）具有该亲属的主管关系并落在该宫时，指示腹部受到该种影响。
- 本步骤产出事实：["亲属受累部位判定（罗睺）"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "所论亲属的指示星（Karak）是否为罗睺（Rahu）"}, {"fact_key": "所论亲属对应宫位的宫主是否为罗睺（Rahu）"}]}, {"operator": "OR", "operands": [{"fact_key": "罗睺（Rahu）是否落六宫（Ari）"}, {"fact_key": "罗睺（Rahu）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否为罗睺（Rahu）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否为罗睺（Rahu）"}, "selection_group": "ch17-v3-graha-limb-map.step-008:rahu-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否为罗睺（Rahu）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否为罗睺（Rahu）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否为罗睺（Rahu）"}, "selection_group": "ch17-v3-graha-limb-map.step-008:rahu-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否为罗睺（Rahu）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["罗睺（Rahu）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "罗睺（Rahu）是否落六宫（Ari）"}, "selection_group": "ch17-v3-graha-limb-map.step-008:rahu-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：罗睺（Rahu）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["罗睺（Rahu）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "罗睺（Rahu）是否落八宫（Randhr）"}, "selection_group": "ch17-v3-graha-limb-map.step-008:rahu-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：罗睺（Rahu）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此把罗睺与该部位的对应扩大到没有此种主管关系的情形。", "不得据此推断病症名称、轻重或发生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应宫位的宫主是哪颗行星。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“with such lordship and in such a Bhava denotes such affectation”
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“the Rahu and Ketu of the abdomen”

### ch17-v3-graha-limb-map.step-009

- 动作：核对计都（Ketu）是否兼具所论亲属的主管关系并落六宫或八宫，据以定受累部位。
- 适用范围：承接同偈前句「亲属指示星或其宫位宫主落六宫、八宫」的安排；原文未给时间限定，也未说该部位一定发病。
- 原文最小意思：计都（与罗睺同列）具有该亲属的主管关系并落在该宫时，指示腹部受到该种影响。
- 本步骤产出事实：["亲属受累部位判定（计都）"]
- 所需事实：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "所论亲属的指示星（Karak）是否为计都（Ketu）"}, {"fact_key": "所论亲属对应宫位的宫主是否为计都（Ketu）"}]}, {"operator": "OR", "operands": [{"fact_key": "计都（Ketu）是否落六宫（Ari）"}, {"fact_key": "计都（Ketu）是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属的指示星（Karak）是否为计都（Ketu）"], "branch_condition_logic": {"fact_key": "所论亲属的指示星（Karak）是否为计都（Ketu）"}, "selection_group": "ch17-v3-graha-limb-map.step-009:ketu-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属的指示星（Karak）是否为计都（Ketu）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["所论亲属对应宫位的宫主是否为计都（Ketu）"], "branch_condition_logic": {"fact_key": "所论亲属对应宫位的宫主是否为计都（Ketu）"}, "selection_group": "ch17-v3-graha-limb-map.step-009:ketu-lordship", "stop_condition": "选中该分支后，缺少以下事实即停止：所论亲属对应宫位的宫主是否为计都（Ketu）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["计都（Ketu）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "计都（Ketu）是否落六宫（Ari）"}, "selection_group": "ch17-v3-graha-limb-map.step-009:ketu-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：计都（Ketu）是否落六宫（Ari）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "所论亲属的指示星（Karak）是哪颗行星"}, {"fact_key": "所论亲属对应宫位的宫主是哪颗行星"}]}, "required_fact_keys": ["计都（Ketu）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "计都（Ketu）是否落八宫（Randhr）"}, "selection_group": "ch17-v3-graha-limb-map.step-009:ketu-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：计都（Ketu）是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此把计都与该部位的对应扩大到没有此种主管关系的情形。", "不得据此推断病症名称、轻重或发生年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所论亲属的指示星（Karak）是哪颗行星、所论亲属对应宫位的宫主是哪颗行星。
- 缺失即停字段：["所论亲属的指示星（Karak）是哪颗行星", "所论亲属对应宫位的宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“with such lordship and in such a Bhava denotes such affectation”
  - `bphs-97:santhanam:ch17:v3-5`｜PDF [32]｜“the Rahu and Ketu of the abdomen”


## 四路查书计划

### 支持路

- Surya with such lordship and in such a Bhava denotes such affectation of head, Chandra of the face
- 太阳主头 月亮主面 火星主颈 水星主脐 受累部位

### 反例或取消路

- The limb, related to a benefic, will have a mark (like moles etc)
- 吉星所属部位只留印记

### 适用边界路

- Limbs of Kaal Purush head, face, arms, heart, stomach, hip
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- 判断亲属受累部位应先定哪颗指示星

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
