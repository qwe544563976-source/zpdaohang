---
method: ch22-v10-labh-sahaj-lords-interchange-coborn-wealth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 通过同胞得财并有上好饰物：十一宫主落三宫、三宫主落十一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能不能靠兄弟姐妹得财
- 三宫主与十一宫主互换是什么效果

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十一宫主（Labh's Lord）是否落三宫（Sahaj）
- 三宫主（Sahaj's Lord）是否落十一宫（Labh）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch22-v10-labh-sahaj-lords-interchange-coborn-wealth.step-001

- 动作：核对十一宫主（Labh's Lord）是否落三宫（Sahaj），同时核对三宫主（Sahaj's Lord）是否落十一宫（Labh）。
- 适用范围：仅限本命盘十一宫（Labh）收获主题；两宫主须互换落宫，缺一不成立；原文未给数额与应期。
- 原文最小意思：十一宫主落三宫、三宫主落十一宫时，本人通过同胞得财，并拥有上好的饰物。
- 本步骤产出事实：["十一宫主三宫主互换同胞得财判定"]
- 所需事实：["十一宫主（Labh's Lord）是否落三宫（Sahaj）", "三宫主（Sahaj's Lord）是否落十一宫（Labh）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十一宫主（Labh's Lord）是否落三宫（Sahaj）"}, {"fact_key": "三宫主（Sahaj's Lord）是否落十一宫（Labh）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断同胞的人数、性别或他们各自的境况。", "不得只凭单向落宫就下断：原文要求两宫主互换。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十一宫主（Labh's Lord）是否落三宫（Sahaj）、三宫主（Sahaj's Lord）是否落十一宫（Labh）。
- 缺失即停字段：["十一宫主（Labh's Lord）是否落三宫（Sahaj）", "三宫主（Sahaj's Lord）是否落十一宫（Labh）"]
- 原文证据：
  - `bphs-97:santhanam:ch22:v10`｜PDF [40]｜“If Labh’s Lord is in Sahaj Bhava, as Sahaj’s Lord is in Labh Bhava, one will gain wealth through co-borns and will be endowed with excellent ornaments.”


## 四路查书计划

### 支持路

- If Labh’s Lord is in Sahaj Bhava, as Sahaj’s Lord is in Labh Bhava, one will gain wealth through co-borns and will be endowed with excellent ornaments
- 十一宫主落三宫（Sahaj） 三宫主落十一宫（Labh） 同胞 得财 饰物

### 反例或取消路

- If Randhr’s Lord is in Sahaj Bhava, the native will be devoid of fraternal happiness, be indolent and devoid of servants and strength
- There will be no gains in spite of numerous efforts, if Labh’s Lord is in fall, in combustion, or be in Ari, Randhr, or Vyaya Bhava with a malefic

### 适用边界路

- Indications of Sahaj Bhava. From Sahaj Bhava know of the following: valour, servants (attending etc.), brothers, sisters etc., initiatory instructions (Upadesh), journey and parent’s death
- Indications of Labh Bhava. All articles, son’s wife, income, prosperity, quadrupeds etc. are to be understood from Labh Bhava

### 判断方法路

- If Labh’s Lord is in Sahaj Bhava, the native will be skilful in all jobs, wealthy, endowed with fraternal bliss and may sometimes incur gout pains
- If Sahaj’s Lord is in Sahaj Bhava, the native will be endowed with happiness through co-born and will have wealth and sons, be cheerful and extremely happy

## 上游问题

- 无

## 停止条件

- 缺少十一宫主落三宫事实时停止。
- 缺少三宫主落十一宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
