---
method: ch12-v1-2-benefic-in-lagna-angles-trines-health-remedy
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 健康的有力补救：上升的角宫或三角宫内有吉星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的健康有没有靠山
- 四宫七宫十宫五宫九宫有吉星代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星

## 按情况检查的事实

- 四宫（Bandhu）是否被吉星占据
- 七宫（Yuvati）是否被吉星占据
- 十宫（Karm）是否被吉星占据
- 五宫（Putr）是否被吉星占据
- 九宫（Dharm）是否被吉星占据

## 依赖方法

- 无

## 执行步骤

### ch12-v1-2-benefic-in-lagna-angles-trines-health-remedy.step-001

- 动作：逐一核对上升的角宫（四宫、七宫、十宫）与上升的三角宫（五宫、九宫）里有没有吉星。
- 适用范围：仅限本命盘与健康有关的事项；原文本句自列了角宫与三角宫的具体宫位，不再另作推广。
- 原文最小意思：上升的角宫（四宫 Bandhu、七宫 Yuvati、十宫）或上升的三角宫（五宫 Putr、九宫 Dharm）中有吉星时，对一切与健康有关的事都是有力的补救。
- 本步骤产出事实：["上升角宫三角宫吉星的健康补救判定"]
- 所需事实：["本盘中哪些行星被判为吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"operator": "OR", "operands": [{"fact_key": "四宫（Bandhu）是否被吉星占据"}, {"fact_key": "七宫（Yuvati）是否被吉星占据"}, {"fact_key": "十宫（Karm）是否被吉星占据"}, {"fact_key": "五宫（Putr）是否被吉星占据"}, {"fact_key": "九宫（Dharm）是否被吉星占据"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["四宫（Bandhu）是否被吉星占据"], "branch_condition_logic": {"fact_key": "四宫（Bandhu）是否被吉星占据"}, "selection_group": "ch12-v1-2-benefic-in-lagna-angles-trines-health-remedy.step-001:benefic-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：四宫（Bandhu）是否被吉星占据。"}, {"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["七宫（Yuvati）是否被吉星占据"], "branch_condition_logic": {"fact_key": "七宫（Yuvati）是否被吉星占据"}, "selection_group": "ch12-v1-2-benefic-in-lagna-angles-trines-health-remedy.step-001:benefic-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫（Yuvati）是否被吉星占据。"}, {"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["十宫（Karm）是否被吉星占据"], "branch_condition_logic": {"fact_key": "十宫（Karm）是否被吉星占据"}, "selection_group": "ch12-v1-2-benefic-in-lagna-angles-trines-health-remedy.step-001:benefic-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫（Karm）是否被吉星占据。"}, {"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["五宫（Putr）是否被吉星占据"], "branch_condition_logic": {"fact_key": "五宫（Putr）是否被吉星占据"}, "selection_group": "ch12-v1-2-benefic-in-lagna-angles-trines-health-remedy.step-001:benefic-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：五宫（Putr）是否被吉星占据。"}, {"when": {"fact_key": "本盘中哪些行星被判为吉星"}, "required_fact_keys": ["九宫（Dharm）是否被吉星占据"], "branch_condition_logic": {"fact_key": "九宫（Dharm）是否被吉星占据"}, "selection_group": "ch12-v1-2-benefic-in-lagna-angles-trines-health-remedy.step-001:benefic-bhava", "stop_condition": "选中该分支后，缺少以下事实即停止：九宫（Dharm）是否被吉星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 remedy for all, related to health 扩成对财富、寿命或子女的补救。", "不得据此断出补救生效的时间或程度。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星。
- 缺失即停字段：["本盘中哪些行星被判为吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v1-2`｜PDF [26]｜“Lagn’s angles (i.e. Bandhu, Yuvati, or the 10<sup>th</sup> ), or its trine (Putr, Dharm), containing a benefic, is a powerful remedy for all, related to health.”


## 四路查书计划

### 支持路

- Lagn’s angles (i.e. Bandhu, Yuvati, or the 10th), or its trine (Putr, Dharm), containing a benefic, is a powerful remedy for all, related to health
- 上升角宫三角宫有吉星 健康的有力补救

### 反例或取消路

- There will not be bodily health, if Lagna, or Chandra be drishtied by, or yuti with a malefic, being devoid of a benefics Drishti
- Malefics, occupying Tanu and Yuvati Bhava, while Chandra is yuti with a malefic with no relief from a benefic, will also cause premature death

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine). Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava

### 判断方法路

- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- Effects of Tanu Bhava
- 判断健康的补救要看四宫七宫十宫五宫九宫有没有吉星

## 上游问题

- 无

## 停止条件

- 缺少吉星名册事实时停止。
- 五个宫位分支事实全缺时停止。
- 吉星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
