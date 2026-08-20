---
method: ch15-v6-v7-mother-condition
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 母亲长寿与幸福：四宫吉星占据、四宫主入旺、母星有力与角宫组合

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我妈妈身体好不好
- 我妈妈这辈子过得幸不幸福

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 四宫（Bandhu Bhava）是否被吉星占据
- 四宫主是否落入其入旺星座
- 母亲的指示星是否有力
- 四宫主（Bandhu’s Lord）是否落角宫
- 金星（Shukra）是否落角宫
- 水星（Budh）是否入旺

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch15-v6-v7-mother-condition.step-001

- 动作：核对四宫是否被吉星占据、四宫主是否落入旺星座、母亲指示星是否有力，判断母亲寿命。
- 适用范围：仅限母亲寿命长短这一结果；原文未给具体年数或时间限定。
- 原文最小意思：四宫（Bandhu Bhava）被吉星占据、四宫主落其入旺星座（exaltation Rāśi）、且母亲的指示星有力时，命主的母亲长寿。
- 本步骤产出事实：["母亲长寿判定"]
- 所需事实：["四宫（Bandhu Bhava）是否被吉星占据", "四宫主是否落入其入旺星座", "母亲的指示星是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "四宫（Bandhu Bhava）是否被吉星占据"}, {"fact_key": "四宫主是否落入其入旺星座"}, {"fact_key": "母亲的指示星是否有力"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推算母亲的具体寿数或去世时间。", "不得把长寿结论扩展成母亲健康无病。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：四宫（Bandhu Bhava）是否被吉星占据、四宫主是否落入其入旺星座、母亲的指示星是否有力。
- 缺失即停字段：["四宫（Bandhu Bhava）是否被吉星占据", "四宫主是否落入其入旺星座", "母亲的指示星是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v6`｜PDF [29]｜“If Bandhu Bhava is occupied by a benefic, while its Lord is in his exaltation Rāśi, as the indicator of mother is endowed with strength, the native will have a long-living mother.”

### ch15-v6-v7-mother-condition.step-002

- 动作：另行核对四宫主是否落角宫、金星是否也落角宫、水星是否入旺，判断母亲是否幸福。
- 适用范围：仅限母亲是否幸福这一结果；原文未给时间限定。
- 原文最小意思：四宫主（Bandhu’s Lord）落角宫、金星（Shukra）也落角宫、水星（Budh）入旺时，命主的母亲会幸福。
- 本步骤产出事实：["母亲幸福判定"]
- 所需事实：["四宫主（Bandhu’s Lord）是否落角宫", "金星（Shukra）是否落角宫", "水星（Budh）是否入旺"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "四宫主（Bandhu’s Lord）是否落角宫"}, {"fact_key": "金星（Shukra）是否落角宫"}, {"fact_key": "水星（Budh）是否入旺"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把母亲幸福扩展成母亲长寿或母亲富有。", "三个条件缺一不可，不得只凭其中一条下结论。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：四宫主（Bandhu’s Lord）是否落角宫、金星（Shukra）是否落角宫、水星（Budh）是否入旺。
- 缺失即停字段：["四宫主（Bandhu’s Lord）是否落角宫", "金星（Shukra）是否落角宫", "水星（Budh）是否入旺"]
- 原文证据：
  - `bphs-97:santhanam:ch15:v7`｜PDF [29]｜“The native’s mother will be happy, if Bandhu’s Lord is in an angle, while Shukra is also in an angle, as Budh is exalted.”


## 四路查书计划

### 支持路

- Bandhu Bhava benefic exaltation indicator of mother long-living mother
- 四宫主入旺 母亲长寿 母亲幸福

### 反例或取消路

- Bandhu Bhava afflicted early loss of mother
- 四宫受克 母亲早亡

### 适用边界路

- who is the indicator of mother in this rule
- 母亲寿命与幸福断语的适用边界

### 判断方法路

- how to judge mother from fourth house BPHS
- 判断母亲状况要查哪些条件

## 上游问题

- 无

## 停止条件

- 缺少四宫占据者或四宫主旺弱事实时停止。
- 缺少母亲指示星强弱事实时停止。
- 缺少金星与水星的落宫和旺弱事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
