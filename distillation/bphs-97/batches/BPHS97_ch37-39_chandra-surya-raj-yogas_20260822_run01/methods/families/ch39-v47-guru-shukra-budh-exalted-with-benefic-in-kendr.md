---
method: ch39-v47-guru-shukra-budh-exalted-with-benefic-in-kendr
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 木星、金星或水星之一入旺且角宫有吉星：成为国王或与国王相当

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 只有一颗吉星入旺够不够
- 角宫里有吉星有多重要

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 角宫（Kendras）内是否有吉星

## 按情况检查的事实

- 木星（Guru）是否入旺
- 金星（Shukra）是否入旺
- 水星（Budh）是否入旺

## 依赖方法

- 无

## 执行步骤

### ch39-v47-guru-shukra-budh-exalted-with-benefic-in-kendr.step-001

- 动作：取本盘吉星名册，核对木星、金星、水星之中是否有一颗入旺，同时角宫内是否有吉星。
- 适用范围：仅限本命盘；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：木星（Guru）、金星（Shukra）与水星（Budh）之中有一颗入旺，同时角宫（Kendr）内有一颗吉星时，命主会成为国王，或与国王相当。
- 本步骤产出事实：["三吉星之一入旺配角宫吉星的贵格判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "角宫（Kendras）内是否有吉星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "角宫（Kendras）内是否有吉星"}]}, {"operator": "OR", "operands": [{"fact_key": "木星（Guru）是否入旺"}, {"fact_key": "金星（Shukra）是否入旺"}, {"fact_key": "水星（Budh）是否入旺"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "角宫（Kendras）内是否有吉星"}]}, "required_fact_keys": ["木星（Guru）是否入旺"], "branch_condition_logic": {"fact_key": "木星（Guru）是否入旺"}, "selection_group": "ch39-v47-guru-shukra-budh-exalted-with-benefic-in-kendr.step-001:which-graha-exalted", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否入旺。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "角宫（Kendras）内是否有吉星"}]}, "required_fact_keys": ["金星（Shukra）是否入旺"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否入旺"}, "selection_group": "ch39-v47-guru-shukra-budh-exalted-with-benefic-in-kendr.step-001:which-graha-exalted", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否入旺。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "角宫（Kendras）内是否有吉星"}]}, "required_fact_keys": ["水星（Budh）是否入旺"], "branch_condition_logic": {"fact_key": "水星（Budh）是否入旺"}, "selection_group": "ch39-v47-guru-shukra-budh-exalted-with-benefic-in-kendr.step-001:which-graha-exalted", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只列木星、金星、水星三颗，不得把别的行星入旺也算进来。", "不得据此推断登位时间或具体权位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、角宫（Kendras）内是否有吉星。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "角宫（Kendras）内是否有吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v47`｜PDF [84]｜“Even, if one among Guru, Shukra and Budh is in exaltation, while a benefic is in a Kendr, the native will become a king, or be equal to him.”


## 四路查书计划

### 支持路

- Even, if one among Guru, Shukra and Budh is in exaltation, while a benefic is in a Kendr, the native will become a king, or be equal to him
- 木星金星水星入旺 角宫吉星 国王

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained
- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn

## 上游问题

- 无

## 停止条件

- 缺少本盘吉星名册事实时停止。
- 缺少角宫吉星占据事实时停止。
- 三颗行星的入旺事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
