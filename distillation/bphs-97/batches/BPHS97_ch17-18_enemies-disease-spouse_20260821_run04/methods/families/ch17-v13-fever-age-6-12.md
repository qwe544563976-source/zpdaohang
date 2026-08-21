---
method: ch17-v13-fever-age-6-12
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第6岁与第12岁的重热病：火星落六宫、六宫主落八宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我小时候会不会发高烧
- 六岁十二岁前后健康怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 火星（Mangal）是否落六宫（Ari）
- 六宫主（Ari's Lord）是否落八宫（Randhr）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch17-v13-fever-age-6-12.step-001

- 动作：核对火星落六宫、六宫主落八宫，判断第6岁与第12岁的结果。
- 适用范围：仅限本命盘发热主题；「(severe)」为译本括注，原文未再说明病程与轻重。
- 原文最小意思：火星落六宫、六宫主落八宫时，第6岁与第12岁会患（重）热病。
- 本步骤产出事实：["六宫火星与八宫六宫主的热病判定"]
- 所需事实：["火星（Mangal）是否落六宫（Ari）", "六宫主（Ari's Lord）是否落八宫（Randhr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "火星（Mangal）是否落六宫（Ari）"}, {"fact_key": "六宫主（Ari's Lord）是否落八宫（Randhr）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把本条的年龄推广到其他年份。", "不得据此推断致死与否或治疗方式。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：火星（Mangal）是否落六宫（Ari）、六宫主（Ari's Lord）是否落八宫（Randhr）。
- 缺失即停字段：["火星（Mangal）是否落六宫（Ari）", "六宫主（Ari's Lord）是否落八宫（Randhr）"]
- 原文证据：
  - `bphs-97:santhanam:ch17:v13-19.5`｜PDF [32, 33]｜“One will suffer from (severe) fever at the age of 6 and at the age of 12, if Mangal is in Ari, while Ari Lord is in Randhr.”


## 四路查书计划

### 支持路

- One will suffer from (severe) fever at the age of 6 and at the age of 12, if Mangal is in Ari, while Ari Lord is in Randhr.
- 火星落六宫、六宫主落八宫 第6岁与第12岁会患（重）热病

### 反例或取消路

- Should one among Budh, Guru and Shukra be in an angle from Lagna, all evils are destroyed
- Lagn Lord is singly capable of counteracting all evils, if he is strongly placed in an angle

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age
- 第6岁与第12岁 与 Vimshottari 大运定时的关系

### 判断方法路

- 判断第6岁与第12岁的凶事应检查哪些宫主与落宫

## 上游问题

- 无

## 停止条件

- 缺少火星（Mangal）是否落六宫（Ari）事实时停止。
- 缺少六宫主（Ari's Lord）是否落八宫（Randhr）事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
