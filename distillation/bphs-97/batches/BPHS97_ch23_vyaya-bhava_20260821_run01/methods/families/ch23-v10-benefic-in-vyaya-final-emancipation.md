---
method: ch23-v10-benefic-in-vyaya-final-emancipation
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 获得最终解脱：十二宫内有吉星，且十二宫主入旺、与吉星同宫或被吉星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子有没有解脱的可能
- 我的灵性道路怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十二宫（Vyaya）是否被吉星占据

## 按情况检查的事实

- 十二宫主（Vyaya's Lord）是否入旺
- 十二宫主（Vyaya's Lord）是否与吉星同宫
- 十二宫主（Vyaya's Lord）是否被吉星相照

## 依赖方法

- 无

## 执行步骤

### ch23-v10-benefic-in-vyaya-final-emancipation.step-001

- 动作：先核对十二宫（Vyaya）内是否有吉星，再核对十二宫主是否入旺、是否与吉星同宫、是否被吉星相照。
- 适用范围：仅限本命盘十二宫（Vyaya Bhava）主题；原文把十二宫内有吉星作为共同前提，后三项为并列择一；原文未给时间限定。
- 原文最小意思：十二宫（Vyaya）内有吉星，并且十二宫主入旺，或与吉星同宫，或被吉星相照时，命主会获得最终的解脱。
- 本步骤产出事实：["十二宫吉星与宫主状态的解脱判定"]
- 所需事实：["十二宫（Vyaya）是否被吉星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十二宫（Vyaya）是否被吉星占据"}, {"operator": "OR", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否入旺"}, {"fact_key": "十二宫主（Vyaya's Lord）是否与吉星同宫"}, {"fact_key": "十二宫主（Vyaya's Lord）是否被吉星相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "十二宫（Vyaya）是否被吉星占据"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否入旺"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否入旺"}, "selection_group": "ch23-v10-benefic-in-vyaya-final-emancipation.step-001:vyaya-lord-benefic-support", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否入旺。"}, {"when": {"fact_key": "十二宫（Vyaya）是否被吉星占据"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否与吉星同宫"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否与吉星同宫"}, "selection_group": "ch23-v10-benefic-in-vyaya-final-emancipation.step-001:vyaya-lord-benefic-support", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否与吉星同宫。"}, {"when": {"fact_key": "十二宫（Vyaya）是否被吉星占据"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否被吉星相照"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否被吉星相照"}, "selection_group": "ch23-v10-benefic-in-vyaya-final-emancipation.step-001:vyaya-lord-benefic-support", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否被吉星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得省掉十二宫内有吉星这个共同前提，只凭宫主状态下判断。", "不得据此推断出家、修行方式或解脱的时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十二宫（Vyaya）是否被吉星占据。
- 缺失即停字段：["十二宫（Vyaya）是否被吉星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch23:v10`｜PDF [40]｜“If there is a benefic in Vyaya, while its Lord is exalted, or is yuti with, or receives a Drishti from a benefic, one will attain final emancipation.”


## 四路查书计划

### 支持路

- If there is a benefic in Vyaya, while its Lord is exalted, or is yuti with, or receives a Drishti from a benefic, one will attain final emancipation.
- 十二宫 吉星 宫主入旺 最终解脱

### 反例或取消路

- If Rahu is in Vyaya along with Mangal, Shani and Surya, the native will go to hell.
- Guru heaven, Chandra, or Shukra the world of Manes, Mangal and/or Surya earth (rebirth), Budh and/or Shani hell
- Benefics in both Vyaya and Dhan Bhava cause Subh Yog. Malefics in both Vyaya and Dhan Bhava cause Asubh Yog.

### 适用边界路

- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula

### 判断方法路

- Effects of Vyaya’s Lord in Various Bhavas
- 十二宫怎么判断解脱与死后去向

## 上游问题

- 无

## 停止条件

- 缺少十二宫是否被吉星占据的事实时停止。
- 宫主入旺、合吉星、被吉星相照三项事实全部缺失时停止。
- 吉星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
