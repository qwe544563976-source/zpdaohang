---
method: ch21-v5-karm-labh-malefics-bad-deeds
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 只做坏事并玷污自己的人：十宫与十一宫同时被凶星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我为什么老是做出格的事
- 十宫十一宫都是凶星会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫（Karm）是否被凶星占据
- 十一宫（Labh）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v5-karm-labh-malefics-bad-deeds.step-001

- 动作：核对十宫（Karm）与十一宫（Labh）是否都被凶星占据。
- 适用范围：仅限两宫同时被凶星占据这一种配置；原文没有给凶星的数量、也没有给时间限定，凶星名册须另查原文定义。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：十宫与十一宫同时被凶星占据时，命主只会做坏事，并会玷污自己的人。
- 本步骤产出事实：["十宫十一宫凶星占据的坏事判定"]
- 所需事实：["十宫（Karm）是否被凶星占据", "十一宫（Labh）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫（Karm）是否被凶星占据"}, {"fact_key": "十一宫（Labh）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断犯罪、坐牢等原文没有写的具体事件。", "不得把两宫同时被占据放宽成任一宫被占据。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫（Karm）是否被凶星占据、十一宫（Labh）是否被凶星占据。
- 缺失即停字段：["十宫（Karm）是否被凶星占据", "十一宫（Labh）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v5`｜PDF [38]｜“Should Karm and Labh Bhava be both occupied by malefics, the native will indulge only in bad deeds and will defile his own men.”


## 四路查书计划

### 支持路

- Should Karm and Labh Bhava be both occupied by malefics, the native will indulge only in bad deeds and will defile his own men
- 十宫 十一宫 都被凶星占据 坏事

### 反例或取消路

- If malefics are surrounded by benefics, while angles, or trines are themselves beneficoccupied, evils disappear soon
- If Karm’s Lord is with a benefic, or be in an auspicious Bhava, one will always gain through royal patronage and in business
- 凶星被吉星包围 恶果消失

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Sahaj, Ari, Karm and Labh are Upachayas
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava

### 判断方法路

- Prosperity, or Annihilation of a Bhava. Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic
- 判断某一宫被凶星占据的效果要查什么

## 上游问题

- 无

## 停止条件

- 缺少十宫被凶星占据的事实时停止。
- 缺少十一宫被凶星占据的事实时停止。
- 凶星名册未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
