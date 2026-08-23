---
method: ch40-v2-karm-labh-free-of-malefics-court-chief
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 王廷之长：十宫与十一宫无凶星占据相照，十一宫受其宫主相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能不能进到有权势的圈子里
- 我的事业格局到什么层次

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为凶星
- 十宫（Karm）是否被凶星占据
- 十一宫（Labh）是否被凶星占据
- 十宫（Karm）是否被凶星相照
- 十一宫（Labh）是否被凶星相照
- 十一宫（Labh）是否被十一宫主（Labh's Lord）相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch40-v2-karm-labh-free-of-malefics-court-chief.step-001

- 动作：先取凶星名册，核对十宫（Karm）与十一宫（Labh）有没有凶星占据或凶星相照，再看十一宫是否受其自己的宫主相照。
- 适用范围：仅限本命盘十宫与十一宫的凶星配置；原文本偈未给凶星判准，须另按本书第 3 章的吉凶星名册取得；原文未给时间限定。
- 原文最小意思：十宫（Karm）与十一宫（Labh）都没有凶星占据、也不受凶星相照，同时十一宫受其自己的宫主相照时，命主将成为王廷之长。
- 本步骤产出事实：["十宫十一宫清净并受宫主相照的王廷之长判定"]
- 所需事实：["本盘中哪些行星被判为凶星", "十宫（Karm）是否被凶星占据", "十一宫（Labh）是否被凶星占据", "十宫（Karm）是否被凶星相照", "十一宫（Labh）是否被凶星相照", "十一宫（Labh）是否被十一宫主（Labh's Lord）相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为凶星"}, {"operator": "NOT", "operands": [{"fact_key": "十宫（Karm）是否被凶星占据"}]}, {"operator": "NOT", "operands": [{"fact_key": "十一宫（Labh）是否被凶星占据"}]}, {"operator": "NOT", "operands": [{"fact_key": "十宫（Karm）是否被凶星相照"}]}, {"operator": "NOT", "operands": [{"fact_key": "十一宫（Labh）是否被凶星相照"}]}, {"fact_key": "十一宫（Labh）是否被十一宫主（Labh's Lord）相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文要求两宫都无凶星占据且都不受凶星相照，不得只核对其中一宫就下断。", "不得据此推断具体官职、收入数额或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为凶星、十宫（Karm）是否被凶星占据、十一宫（Labh）是否被凶星占据、十宫（Karm）是否被凶星相照、十一宫（Labh）是否被凶星相照、十一宫（Labh）是否被十一宫主（Labh's Lord）相照。
- 缺失即停字段：["本盘中哪些行星被判为凶星", "十宫（Karm）是否被凶星占据", "十一宫（Labh）是否被凶星占据", "十宫（Karm）是否被凶星相照", "十一宫（Labh）是否被凶星相照", "十一宫（Labh）是否被十一宫主（Labh's Lord）相照"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v2`｜PDF [85]｜“If Karm and Labh Bhava are devoid of malefic occupation and devoid of Drishti from a malefic, while Labh Bhava receives a Drishti from its own Lord, the native will be a chief in the king’s court.”


## 四路查书计划

### 支持路

- If Karm and Labh Bhava are devoid of malefic occupation and devoid of Drishti from a malefic
- 十宫十一宫无凶星 十一宫主相照 王廷之长

### 反例或取消路

- One will be penniless, if the Lord of Dhan Bhava is in an evil Bhava

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- Yogas For Royal Association
- One will gain through royal association, if Labh Bhava is occupied by its own Lord and is devoid of a Drishti from a malefic

## 上游问题

- 无

## 停止条件

- 凶星名册未定时停止：须先按 BPHS 自己的吉凶星定义取名册。
- 缺少十宫或十一宫的凶星占据、相照事实时停止。
- 缺少十一宫是否受其宫主相照的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
