---
method: ch39-v39-guru-own-rasi-in-dharm
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 木星居与九宫重合的本星座并与金星或五宫主同宫：获得王者地位

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 木星在九宫有多好
- 我有没有靠福德得位的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘五宫主（Putr's Lord）是哪颗行星
- 木星（Guru）是否落九宫（Dharm）
- 木星（Guru）是否落自己主管的星座（own Rāśi）

## 按情况检查的事实

- 木星（Guru）是否与金星（Shukra）同宫
- 木星（Guru）是否与五宫主（Putr's Lord）同宫

## 依赖方法

- 无

## 执行步骤

### ch39-v39-guru-own-rasi-in-dharm.step-001

- 动作：核对木星（Guru）是否落在与九宫重合的、自己主管的星座里，再核对它是否与金星或五宫主同宫。
- 适用范围：仅限本命盘；原文没有时间限定。
- 原文最小意思：木星（Guru）落在与九宫（Dharm Bhava）重合的自己主管的星座（own Rashi），并与金星（Shukr）或五宫主（Putr's Lord）同宫时，命主会获得王者地位。
- 本步骤产出事实：["木星居九宫本星座的王者地位判定"]
- 所需事实：["本盘五宫主（Putr's Lord）是哪颗行星", "木星（Guru）是否落九宫（Dharm）", "木星（Guru）是否落自己主管的星座（own Rāśi）"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "木星（Guru）是否落九宫（Dharm）"}, {"fact_key": "木星（Guru）是否落自己主管的星座（own Rāśi）"}]}, {"operator": "OR", "operands": [{"fact_key": "木星（Guru）是否与金星（Shukra）同宫"}, {"fact_key": "木星（Guru）是否与五宫主（Putr's Lord）同宫"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "木星（Guru）是否落九宫（Dharm）"}, {"fact_key": "木星（Guru）是否落自己主管的星座（own Rāśi）"}]}, "required_fact_keys": ["木星（Guru）是否与金星（Shukra）同宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否与金星（Shukra）同宫"}, "selection_group": "ch39-v39-guru-own-rasi-in-dharm.step-001:yuti-with", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否与金星（Shukra）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘五宫主（Putr's Lord）是哪颗行星"}, {"fact_key": "木星（Guru）是否落九宫（Dharm）"}, {"fact_key": "木星（Guru）是否落自己主管的星座（own Rāśi）"}]}, "required_fact_keys": ["木星（Guru）是否与五宫主（Putr's Lord）同宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否与五宫主（Putr's Lord）同宫"}, "selection_group": "ch39-v39-guru-own-rasi-in-dharm.step-001:yuti-with", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否与五宫主（Putr's Lord）同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["own Rāśi 是木星自己主管的星座，不得读成落本宫；原文还要求这个星座与九宫重合。", "不得据此推断得位时间或权位大小。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘五宫主（Putr's Lord）是哪颗行星、木星（Guru）是否落九宫（Dharm）、木星（Guru）是否落自己主管的星座（own Rāśi）。
- 缺失即停字段：["本盘五宫主（Putr's Lord）是哪颗行星", "木星（Guru）是否落九宫（Dharm）", "木星（Guru）是否落自己主管的星座（own Rāśi）"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v39`｜PDF [84]｜“Should Guru be in his own Rashiidentical with Dharm Bhava and yuti with either Shukr, or Putr’s Lord, the native will obtain royal status.”


## 四路查书计划

### 支持路

- Should Guru be in his own Rashiidentical with Dharm Bhava and yuti with either Shukr, or Putr’s Lord, the native will obtain royal status
- 木星在九宫本星座 与金星同宫 王者地位

### 反例或取消路

- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas
- Should Putr’s and Dharm’s Lords be, respectively, found in Ari and Vyaya Bhava and receive a Drishti from Marak Grahas, the native will be penniless

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Putr and Dharm Bhava are known by the name Kon (or trine)

### 判断方法路

- Should Guru be in Putr Bhava identical with his own Rāśi, as Budh is in Labh Bhava, the native will be very affluent
- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained

## 上游问题

- 无

## 停止条件

- 缺少木星落九宫或落本星座的事实时停止。
- 与金星、与五宫主两项同宫事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
