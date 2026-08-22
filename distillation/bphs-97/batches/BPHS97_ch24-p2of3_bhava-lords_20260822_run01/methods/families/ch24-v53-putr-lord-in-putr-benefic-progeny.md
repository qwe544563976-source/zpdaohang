---
method: ch24-v53-putr-lord-in-putr-benefic-progeny
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 五宫主落五宫且与吉星关联：会有子女

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子有没有子女
- 我求子这件事有没有指望

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 五宫主（Putr's Lord）是否落五宫（Putr）
- 五宫主（Putr's Lord）是否与吉星发生关联（related）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v53-putr-lord-in-putr-benefic-progeny.step-001

- 动作：先确定本盘吉星名册，再核对五宫主（Putr's Lord）是否落五宫（Putr Bhava）、是否与吉星发生关联，据此判断有无子女。
- 适用范围：仅限本命盘五宫主落五宫（Putr Bhava）且与吉星关联一条；原文只说 related to a benefic，未在本偈界定「关联」是同宫、相照还是别的形式，未确定即停判；原文未给时间限定。
- 原文最小意思：五宫主（Putr's Lord）落五宫（Putr Bhava）、并与吉星发生关联（related to a benefic）时，本人会有子女。
- 本步骤产出事实：["五宫主落五宫与吉星关联的子女判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "五宫主（Putr's Lord）是否落五宫（Putr）", "五宫主（Putr's Lord）是否与吉星发生关联（related）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "五宫主（Putr's Lord）是否落五宫（Putr）"}, {"fact_key": "五宫主（Putr's Lord）是否与吉星发生关联（related）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「与吉星发生关联」自行坐实为同宫、相照或任何一种具体关系——原文未在本偈界定。", "不得据此推断子女人数、性别或得子年份。", "不得把本条与同偈凶星关联一条合并下断。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、五宫主（Putr's Lord）是否落五宫（Putr）、五宫主（Putr's Lord）是否与吉星发生关联（related）。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "五宫主（Putr's Lord）是否落五宫（Putr）", "五宫主（Putr's Lord）是否与吉星发生关联（related）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v53`｜PDF [44]｜“If Putr’s Lord is in Putr Bhava, the native will have progeny, if related to a benefic”


## 四路查书计划

### 支持路

- If Putr’s Lord is in Putr Bhava, the native will have progeny, if related to a benefic
- 五宫主落五宫 与吉星关联 会有子女

### 反例或取消路

- If Putr’s Lord is in Ari, Randhr, or Vyaya Bhava, or be in an inimical Rāśi, or be in fall, or in Putr itself, the native will beget issues with difficulty
- One’s own sons will be his enemies, if Putr Lord is in Ari, while Ari Lord is with Guru

### 适用边界路

- Indications of Putr Bhava. The learned should deduce from Putr Bhava amulets, sacred spells, learning, knowledge, sons, royalty (or authority), fall of position etc.
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Effects of Putr’s Lord in Various Bhavas
- Effects of Putr Bhava

## 上游问题

- 无

## 停止条件

- 缺少五宫主是否落五宫的事实时停止。
- 原文未界定「与吉星发生关联」的形式，该事实未确定即停止。
- 吉星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
