---
method: ch10-v7-mangal-with-guru-auspicious-for-mother
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 对母亲与本人皆吉：火星与木星同宫或被木星相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 火星木星的关系对母亲有什么影响
- 我母亲的处境怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘火星（Mangal）落在哪一宫
- 本盘木星（Guru）落在哪一宫

## 按情况检查的事实

- 火星（Mangal）是否与木星（Guru）同宫
- 火星（Mangal）是否被木星（Guru）相照

## 依赖方法

- 无

## 执行步骤

### ch10-v7-mangal-with-guru-auspicious-for-mother.step-001

- 动作：核对火星（Mangal）是否与木星（Guru）同宫，或是否被木星（Guru）相照。
- 适用范围：仅限第 10 章消解凶恶（Antidotes for Evils）主题；原文没有指明火星落在哪一宫，也没有指明这是承接哪一条凶象，未确定即停判；原文未给时间限定。
- 原文最小意思：火星（Mangal）与木星（Guru）同宫，或被木星（Guru）相照时，对母亲与本人都将是吉利的。
- 本步骤产出事实：["火星与木星相涉对母亲与本人的吉利判定"]
- 所需事实：["本盘火星（Mangal）落在哪一宫", "本盘木星（Guru）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘火星（Mangal）落在哪一宫"}, {"fact_key": "本盘木星（Guru）落在哪一宫"}]}, {"operator": "OR", "operands": [{"fact_key": "火星（Mangal）是否与木星（Guru）同宫"}, {"fact_key": "火星（Mangal）是否被木星（Guru）相照"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘火星（Mangal）落在哪一宫"}, {"fact_key": "本盘木星（Guru）落在哪一宫"}]}, "required_fact_keys": ["火星（Mangal）是否与木星（Guru）同宫"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否与木星（Guru）同宫"}, "selection_group": "ch10-v7-mangal-with-guru-auspicious-for-mother.step-001:mangal-guru-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否与木星（Guru）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘火星（Mangal）落在哪一宫"}, {"fact_key": "本盘木星（Guru）落在哪一宫"}]}, "required_fact_keys": ["火星（Mangal）是否被木星（Guru）相照"], "branch_condition_logic": {"fact_key": "火星（Mangal）是否被木星（Guru）相照"}, "selection_group": "ch10-v7-mangal-with-guru-auspicious-for-mother.step-001:mangal-guru-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：火星（Mangal）是否被木星（Guru）相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文补出火星应落哪一宫——原文这一句没有写。", "不得据此推断对母亲吉利的具体事项（寿命、健康、财物等）。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘火星（Mangal）落在哪一宫、本盘木星（Guru）落在哪一宫。
- 缺失即停字段：["本盘火星（Mangal）落在哪一宫", "本盘木星（Guru）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch10:v7`｜PDF [25]｜“It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru.”


## 四路查书计划

### 支持路

- It will prove auspicious for the mother as well as the native, if Mangal joins, or is drishtied by Guru
- 火星与木星同宫或被木星相照 对母亲与本人吉利

### 反例或取消路

- The mother of the native will incur evils (will die soon), if Chandra at birth receives a Drishti from three malefics
- Malefics in Ari and Vyaya Bhava will bring evils to mother

### 适用边界路

- Indications of Bandhu Bhava. Conveyances, relatives, mother, happiness, treasure, lands and buildings are to be consulted through Bandhu Bhava
- 母亲之事从哪一宫看

### 判断方法路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- Benefics, giving a Drishti to Chandra, will bring good to the mother
- 怎样判断母亲的吉凶

## 上游问题

- 无

## 停止条件

- 缺少火星或木星落宫事实时停止。
- 原文没有指明火星应落哪一宫，若要按某一宫限定使用，本方法停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
