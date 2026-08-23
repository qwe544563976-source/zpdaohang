---
method: ch41-v16-grahas-yuti-with-dharm-putr-lords-give-wealth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 给财之曜：与九宫主或五宫主同宫的行星，在各自大运期间给出财富

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 除了宫主还有哪些星管我的财
- 我哪一段大运会有进项

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘九宫主（Dharm's Lord）是哪颗行星
- 本盘五宫主（Putr's Lord）是哪颗行星

## 按情况检查的事实

- 该行星（Grah）是否与九宫主（Dharm's Lord）同宫
- 该行星（Grah）是否与五宫主（Putr's Lord）同宫

## 依赖方法

- 无

## 执行步骤

### ch41-v16-grahas-yuti-with-dharm-putr-lords-give-wealth.step-001

- 动作：认出与九宫主同宫、或与五宫主同宫的行星，把它们同样记为有给财能力的行星，其给财落在各自的大运期间。
- 适用范围：仅限本命盘与九宫主、五宫主同宫的行星；原文写作 and/or，即与其中一位同宫已足，两位都同宫也成立；「these Grahas」承指本偈上文所说的这几颗行星；原文没有给出财富数额，也没有给出大运之外的时间限定。
- 原文最小意思：与九宫主（Dharm's Lord）同宫的行星、与五宫主（Putr's Lord）同宫的行星，同样有能力给予财富，这些行星必定在其自己的大运期间给出财富。
- 本步骤产出事实：["与九宫主五宫主同宫行星的给财资格判定"]
- 所需事实：["本盘九宫主（Dharm's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "该行星（Grah）是否与九宫主（Dharm's Lord）同宫"}, {"fact_key": "该行星（Grah）是否与五宫主（Putr's Lord）同宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, "required_fact_keys": ["该行星（Grah）是否与九宫主（Dharm's Lord）同宫"], "branch_condition_logic": {"fact_key": "该行星（Grah）是否与九宫主（Dharm's Lord）同宫"}, "selection_group": "ch41-v16-grahas-yuti-with-dharm-putr-lords-give-wealth.step-001:yuti-with-which-lord", "stop_condition": "选中该分支后，缺少以下事实即停止：该行星（Grah）是否与九宫主（Dharm's Lord）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}]}, "required_fact_keys": ["该行星（Grah）是否与五宫主（Putr's Lord）同宫"], "branch_condition_logic": {"fact_key": "该行星（Grah）是否与五宫主（Putr's Lord）同宫"}, "selection_group": "ch41-v16-grahas-yuti-with-dharm-putr-lords-give-wealth.step-001:yuti-with-which-lord", "stop_condition": "选中该分支后，缺少以下事实即停止：该行星（Grah）是否与五宫主（Putr's Lord）同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写同宫（yuti），不得把相照、互换一并算作同一条件。", "不得据此推断财富数额、来源或大运内的具体时点。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘九宫主（Dharm's Lord）是哪颗行星、本盘五宫主（Putr's Lord）是哪颗行星。
- 缺失即停字段：["本盘九宫主（Dharm's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch41:v16`｜PDF [86, 87]｜“Similarly Grahas, yuti with Dharm’s Lord and/or Putr’s Lord are capable of bestowing wealth”
  - `bphs-97:santhanam:ch41:v16`｜PDF [86, 87]｜“There is no doubt, that these Grahas will give wealth during their Dasha periods.”


## 四路查书计划

### 支持路

- Similarly Grahas, yuti with Dharm’s Lord and/or Putr’s Lord are capable of bestowing wealth
- 与九宫主五宫主同宫的行星 大运给财

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava

### 适用边界路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- Combinations for Wealth
- Other Qualified Grahas. Dharm’s Lord and Putr’s Lord are capable of bestowing wealth

## 上游问题

- 无

## 停止条件

- 九宫主或五宫主的身份事实缺失时停止。
- 同宫关系事实缺失时停止。
- 大运次第未取到时，给财时段无法定位，只保留给财资格的结论。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
