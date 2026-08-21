---
method: ch21-v14-exalted-karm-lord-deeds
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 富于作为：十宫主入旺落角宫或三角宫、并与木星同宫或受木星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子做事有没有成就
- 十宫主入旺又逢木星对我意味着什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否入旺

## 按情况检查的事实

- 十宫主（Karm's Lord）是否落角宫
- 十宫主（Karm's Lord）是否落三角宫
- 十宫主（Karm's Lord）是否与木星（Guru）同宫
- 十宫主（Karm's Lord）是否被木星（Guru）相照

## 依赖方法

- 无

## 执行步骤

### ch21-v14-exalted-karm-lord-deeds.step-001

- 动作：先核对十宫主（Karm's Lord）是否入旺，再核对它落角宫还是三角宫，以及它与木星（Guru）是同宫还是受其相照。
- 适用范围：仅限本命盘十宫（Karm）作为主题；原文里入旺与落角宫或三角宫是同一句里的合取，与木星的两种关系另成一组备选；原文未给时间限定。
- 原文最小意思：十宫主入旺并落角宫或三角宫、且与木星同宫或受木星相照时，命主富于作为。
- 本步骤产出事实：["十宫主入旺逢木星富于作为判定"]
- 所需事实：["十宫主（Karm's Lord）是否入旺"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否入旺"}, {"operator": "OR", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落角宫"}, {"fact_key": "十宫主（Karm's Lord）是否落三角宫"}]}, {"operator": "OR", "operands": [{"fact_key": "十宫主（Karm's Lord）是否与木星（Guru）同宫"}, {"fact_key": "十宫主（Karm's Lord）是否被木星（Guru）相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "十宫主（Karm's Lord）是否入旺"}, "required_fact_keys": ["十宫主（Karm's Lord）是否落角宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否落角宫"}, "selection_group": "ch21-v14-exalted-karm-lord-deeds.step-001:exalted-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否落角宫。"}, {"when": {"fact_key": "十宫主（Karm's Lord）是否入旺"}, "required_fact_keys": ["十宫主（Karm's Lord）是否落三角宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否落三角宫"}, "selection_group": "ch21-v14-exalted-karm-lord-deeds.step-001:exalted-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否落三角宫。"}, {"when": {"fact_key": "十宫主（Karm's Lord）是否入旺"}, "required_fact_keys": ["十宫主（Karm's Lord）是否与木星（Guru）同宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否与木星（Guru）同宫"}, "selection_group": "ch21-v14-exalted-karm-lord-deeds.step-001:guru-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否与木星（Guru）同宫。"}, {"when": {"fact_key": "十宫主（Karm's Lord）是否入旺"}, "required_fact_keys": ["十宫主（Karm's Lord）是否被木星（Guru）相照"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否被木星（Guru）相照"}, "selection_group": "ch21-v14-exalted-karm-lord-deeds.step-001:guru-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否被木星（Guru）相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断职业种类、地位高低或应期。", "不得把入旺与落角宫或三角宫拆开，只凭其中一项成立就下断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否入旺。
- 缺失即停字段：["十宫主（Karm's Lord）是否入旺"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v14`｜PDF [39]｜“If the Karm’s Lord is exalted in an angle, or a trine and is yuti with Guru, or receives a Drishti from Guru, one will be endowed with deeds.”


## 四路查书计划

### 支持路

- If the Karm’s Lord is exalted in an angle, or a trine and is yuti with Guru, or receives a Drishti from Guru, one will be endowed with deeds
- 十宫主入旺 角宫 三角宫 与木星同宫 木星相照 富于作为

### 反例或取消路

- If Shani is in Karm Bhava along with a debilitated Grah, while Karm Bhava in the Navāńś Kundali is occupied by a malefic, the native will be bereft of acts
- If Karm’s Lord is devoid of strength, the native will face obstructions in his work

### 适用边界路

- Kendras, Konas etc. defined. O Maitreya, listen to other matters, which I am explaining. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava

### 判断方法路

- If Karm’s Lord is strong and in exaltation, or in its own Rāśi/Navāńś, the native will derive extreme paternal happiness, will enjoy fame and will perform good deeds
- 判断十宫（Karm）作为应检查十宫主的哪些状态

## 上游问题

- 无

## 停止条件

- 缺少十宫主入旺事实时停止。
- 落角宫、落三角宫两个分支事实都缺时停止。
- 与木星同宫、受木星相照两个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
