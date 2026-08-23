---
method: ch39-v37-bandhu-or-karm-lord-joins-putr-or-dharm-lord
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 四宫主或十宫主与五宫主或九宫主同宫：得到王国

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 角宫主和三角宫主碰头说明什么
- 我有没有得大位的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘四宫主（Bandhu's Lord）是哪颗行星
- 本盘十宫主（Karm's Lord）是哪颗行星
- 本盘五宫主（Putr's Lord）是哪颗行星
- 本盘九宫主（Dharm's Lord）是哪颗行星

## 按情况检查的事实

- 四宫主（Bandhu's Lord）是否与五宫主（Putr's Lord）同宫
- 四宫主（Bandhu's Lord）是否与九宫主（Dharm's Lord）同宫
- 十宫主（Karm's Lord）是否与五宫主（Putr's Lord）同宫
- 十宫主（Karm's Lord）是否与九宫主（Dharm's Lord）同宫

## 依赖方法

- 无

## 执行步骤

### ch39-v37-bandhu-or-karm-lord-joins-putr-or-dharm-lord.step-001

- 动作：先认出四宫主、十宫主、五宫主与九宫主，再核对四种同宫组合中是否有一种成立。
- 适用范围：仅限本命盘；原文没有时间限定。
- 原文最小意思：四宫主（Bandhu's Lord）或十宫主（Karm's Lord）与五宫主（Putr's Lord）或九宫主（Dharm's Lord）同宫时，命主会得到王国。
- 本步骤产出事实：["四十宫主与五九宫主同宫的得国判定"]
- 所需事实：["本盘四宫主（Bandhu's Lord）是哪颗行星", "本盘十宫主（Karm's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星", "本盘九宫主（Dharm's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "四宫主（Bandhu's Lord）是否与五宫主（Putr's Lord）同宫"}, {"fact_key": "四宫主（Bandhu's Lord）是否与九宫主（Dharm's Lord）同宫"}, {"fact_key": "十宫主（Karm's Lord）是否与五宫主（Putr's Lord）同宫"}, {"fact_key": "十宫主（Karm's Lord）是否与九宫主（Dharm's Lord）同宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}]}, "required_fact_keys": ["四宫主（Bandhu's Lord）是否与五宫主（Putr's Lord）同宫"], "branch_condition_logic": {"fact_key": "四宫主（Bandhu's Lord）是否与五宫主（Putr's Lord）同宫"}, "selection_group": "ch39-v37-bandhu-or-karm-lord-joins-putr-or-dharm-lord.step-001:which-pair", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫主（Bandhu's Lord）是否与五宫主（Putr's Lord）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}]}, "required_fact_keys": ["四宫主（Bandhu's Lord）是否与九宫主（Dharm's Lord）同宫"], "branch_condition_logic": {"fact_key": "四宫主（Bandhu's Lord）是否与九宫主（Dharm's Lord）同宫"}, "selection_group": "ch39-v37-bandhu-or-karm-lord-joins-putr-or-dharm-lord.step-001:which-pair", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫主（Bandhu's Lord）是否与九宫主（Dharm's Lord）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否与五宫主（Putr's Lord）同宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否与五宫主（Putr's Lord）同宫"}, "selection_group": "ch39-v37-bandhu-or-karm-lord-joins-putr-or-dharm-lord.step-001:which-pair", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否与五宫主（Putr's Lord）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘四宫主（Bandhu's Lord）是哪颗行星"}, {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "本盘九宫主（Dharm's Lord）是哪颗行星"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否与九宫主（Dharm's Lord）同宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否与九宫主（Dharm's Lord）同宫"}, "selection_group": "ch39-v37-bandhu-or-karm-lord-joins-putr-or-dharm-lord.step-001:which-pair", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否与九宫主（Dharm's Lord）同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写同宫（join），不得把相照也算作成立条件。", "不得据此推断得位时间或权位大小。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘四宫主（Bandhu's Lord）是哪颗行星、本盘十宫主（Karm's Lord）是哪颗行星、本盘五宫主（Putr's Lord）是哪颗行星、本盘九宫主（Dharm's Lord）是哪颗行星。
- 缺失即停字段：["本盘四宫主（Bandhu's Lord）是哪颗行星", "本盘十宫主（Karm's Lord）是哪颗行星", "本盘五宫主（Putr's Lord）是哪颗行星", "本盘九宫主（Dharm's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v37`｜PDF [84]｜“Should the Lord of Bandhu, or of Karm Bhava join either the Putr’s Lord, or Dharm’s Lord, the native will obtain a kingdom.”


## 四路查书计划

### 支持路

- Should the Lord of Bandhu, or of Karm Bhava join either the Putr’s Lord, or Dharm’s Lord, the native will obtain a kingdom
- 四宫主十宫主与五宫主九宫主同宫 得国

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- Should Putr’s and Dharm’s Lords be, respectively, found in Ari and Vyaya Bhava and receive a Drishti from Marak Grahas, the native will be penniless

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine)

### 判断方法路

- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- 四个宫主的身份事实缺任一项时停止。
- 四种同宫组合的事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
