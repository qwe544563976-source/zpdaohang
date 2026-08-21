---
method: ch21-v2-karm-lord-paternal-happiness
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父亲方面的幸福与名声：十宫主有力，且入旺、落本星座或落本九分盘星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我和父亲的缘分好不好
- 我这辈子有没有名声

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否有力

## 按情况检查的事实

- 十宫主（Karm's Lord）是否入旺
- 十宫主（Karm's Lord）是否落本星座（own Rāśi）
- 十宫主（Karm's Lord）是否落在自己主管的九分盘（Navamsa D9）星座

## 依赖方法

- 无

## 执行步骤

### ch21-v2-karm-lord-paternal-happiness.step-001

- 动作：先核对十宫主（Karm's Lord）是否有力，再核对它是否入旺、落本宫或落自己主管的九分盘（Navamsa D9）星座。
- 适用范围：仅限本命盘十宫（Karm Bhava）主题下的父亲幸福、名声与善行；原文把「有力」与入旺／本星座／本九分盘并列在同一个条件里，「有力」的判准原文本句未给；原文未给时间限定。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：十宫主有力，并且入旺、落本星座或落本九分盘（Navamsa D9）星座时，命主会得到极大的父亲方面的幸福、享有名声，并做出善行。
- 本步骤产出事实：["十宫主力量与尊贵状态的父亲幸福名声判定"]
- 所需事实：["十宫主（Karm's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否有力"}, {"operator": "OR", "operands": [{"fact_key": "十宫主（Karm's Lord）是否入旺"}, {"fact_key": "十宫主（Karm's Lord）是否落本星座（own Rāśi）"}, {"fact_key": "十宫主（Karm's Lord）是否落在自己主管的九分盘（Navamsa D9）星座"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "十宫主（Karm's Lord）是否有力"}, "required_fact_keys": ["十宫主（Karm's Lord）是否入旺"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否入旺"}, "selection_group": "ch21-v2-karm-lord-paternal-happiness.step-001:karm-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否入旺。"}, {"when": {"fact_key": "十宫主（Karm's Lord）是否有力"}, "required_fact_keys": ["十宫主（Karm's Lord）是否落本星座（own Rāśi）"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否落本星座（own Rāśi）"}, "selection_group": "ch21-v2-karm-lord-paternal-happiness.step-001:karm-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否落本星座（own Rāśi）。"}, {"when": {"fact_key": "十宫主（Karm's Lord）是否有力"}, "required_fact_keys": ["十宫主（Karm's Lord）是否落在自己主管的九分盘（Navamsa D9）星座"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否落在自己主管的九分盘（Navamsa D9）星座"}, "selection_group": "ch21-v2-karm-lord-paternal-happiness.step-001:karm-lord-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否落在自己主管的九分盘（Navamsa D9）星座。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的寿命、职业或具体事件。", "不得把这条十宫主的规则改挂到九宫主或太阳（Surya）身上。", "原文本句没有给出「有力」的判准，不得自行发明力量算法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否有力。
- 缺失即停字段：["十宫主（Karm's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v2`｜PDF [38]｜“If Karm’s Lord is strong and in exaltation, or in its own Rāśi/Navāńś, the native will derive extreme paternal happiness, will enjoy fame and will perform good deeds.”


## 四路查书计划

### 支持路

- If Karm’s Lord is strong and in exaltation, or in its own Rāśi/Navāńś, the native will derive extreme paternal happiness
- 十宫主 有力 入旺 本宫 九分盘 父亲的幸福 名声

### 反例或取消路

- If Karm’s Lord is devoid of strength, the native will face obstructions in his work
- If Karm’s Lord is in Ari Bhava, the native will be bereft of paternal bliss
- 十宫主无力 工作受阻 失去父亲之乐

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava
- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula

### 判断方法路

- Effects of Karm’s Lord in Various Bhavas
- 判断十宫（Karm Bhava）时要核对宫主的力量与尊贵状态

## 上游问题

- 无

## 停止条件

- 缺少十宫主力量事实时停止。
- 力量判准由排盘窗口定义，未给出取值时停止。
- 缺少十宫主入旺、本星座与本九分盘星座三项事实中被命中的那一项时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
