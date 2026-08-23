---
method: ch40-v12-labh-occupied-by-own-lord-royal-gain
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 因与王家往还而得利：十一宫被其宫主占据不受凶照，Atma Karak 偕吉星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的进项能不能靠关系打开
- 我能不能从上面得到实惠

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星
- 本盘中哪些行星被判为吉星
- 十一宫（Labh）是否被十一宫主（Labh's Lord）占据
- 十一宫（Labh）是否被凶星相照
- Atma Karak 是否与吉星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch40-v12-labh-occupied-by-own-lord-royal-gain.step-001

- 动作：核对十一宫（Labh）是否被它自己的宫主占据、是否不受凶星相照，同时看 Atma Karak 是否与吉星同宫。
- 适用范围：仅限本命盘十一宫与 Atma Karak 一线；原文本偈未给吉凶星判准，须另按本书第 3 章的吉凶星名册取得；原文未给时间限定。
- 原文最小意思：十一宫（Labh）被其自己的宫主占据、并且不受凶星相照，同时 Atma Karak 与吉星同宫时，命主将因与王家往还而得利。
- 本步骤产出事实：["十一宫自主星占据的王家得利判定"]
- 所需事实：["本盘中哪些行星被判为凶星", "本盘中哪些行星被判为吉星", "十一宫（Labh）是否被十一宫主（Labh's Lord）占据", "十一宫（Labh）是否被凶星相照", "Atma Karak 是否与吉星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "十一宫（Labh）是否被十一宫主（Labh's Lord）占据"}, {"operator": "NOT", "operands": [{"fact_key": "十一宫（Labh）是否被凶星相照"}]}, {"fact_key": "Atma Karak 是否与吉星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文的三项条件同时成立才下断，不得只凭十一宫一项。", "不得据此推断得利数额、来源或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星、本盘中哪些行星被判为吉星、十一宫（Labh）是否被十一宫主（Labh's Lord）占据、十一宫（Labh）是否被凶星相照、Atma Karak 是否与吉星同宫。
- 缺失即停字段：["本盘中哪些行星被判为凶星", "本盘中哪些行星被判为吉星", "十一宫（Labh）是否被十一宫主（Labh's Lord）占据", "十一宫（Labh）是否被凶星相照", "Atma Karak 是否与吉星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v12`｜PDF [85]｜“One will gain through royal association, if Labh Bhava is occupied by its own Lord and is devoid of a Drishti from a malefic. The Atma Karak should at the same time be yuti with a benefic.”


## 四路查书计划

### 支持路

- One will gain through royal association, if Labh Bhava is occupied by its own Lord and is devoid of a Drishti from a malefic
- 十一宫被本宫主占据 不受凶照 Atma Karak 偕吉星 王家得利

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The Grah next to Atma Karak in terms of longitude is called Amatya Karak

### 判断方法路

- Yogas For Royal Association
- If Karm and Labh Bhava are devoid of malefic occupation and devoid of Drishti from a malefic

## 上游问题

- 无

## 停止条件

- 吉凶星名册未定时停止：须先按 BPHS 自己的吉凶星定义取名册。
- 十一宫的占据与相照事实缺失时停止。
- Atma Karak 是否与吉星同宫的事实缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
