---
method: ch24-v117-karm-lord-in-dharm-royal-scion
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 十宫主落九宫且出身王族：成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能不能坐上最高的位子
- 出身王族的人这个格局会怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否落九宫（Dharm）
- 本人是否出身王族（royal scion）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v117-karm-lord-in-dharm-royal-scion.step-001

- 动作：核对十宫主（Karm's Lord）是否落九宫（Dharm Bhava），并核对本人是否出身王族，据此判断能否成为国王。
- 适用范围：仅限本命盘十宫主（Karm's Lord）落九宫（Dharm Bhava）、且本人出身王族这一半；同偈另一半（普通出身者与国王相当）另立方法 ch24-v117-karm-lord-in-dharm-ordinary；原文没有界定什么算「出身王族」，该判准未确定即停判；原文未给时间限定。
- 原文最小意思：十宫主（Karm's Lord）落九宫（Dharm Bhava）且本人出身王族时，会成为国王。
- 本步骤产出事实：["十宫主落九宫且出身王族的权位判定"]
- 所需事实：["十宫主（Karm's Lord）是否落九宫（Dharm）", "本人是否出身王族（royal scion）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落九宫（Dharm）"}, {"fact_key": "本人是否出身王族（royal scion）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文定义什么算「出身王族」；该项未确定即停判。", "不得把这一半的结论套到普通出身的人身上——原文对那一半另有断语。", "不得把「成为国王」直接换算成今天的某个具体职务。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否落九宫（Dharm）、本人是否出身王族（royal scion）。
- 缺失即停字段：["十宫主（Karm's Lord）是否落九宫（Dharm）", "本人是否出身王族（royal scion）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v117`｜PDF [48]｜“If Karm’s Lord is in Dharm Bhava, one born of royal scion will become a king, whereas an ordinary native will be equal to a king.”


## 四路查书计划

### 支持路

- If Karm’s Lord is in Dharm Bhava, one born of royal scion will become a king, whereas an ordinary native will be equal to a king.
- 十宫主落九宫 出身王族 成为国王

### 反例或取消路

- In the case of a Grah, owning two Bhavas, the results are to be deducted based on its two lordships. If contrary results are thus indicated, the results will be nullified
- 宫主效果被抵消或按力量打折的原文

### 适用边界路

- The Grah will yield full, half, or a quarter of the effects according to its strength being full, medium and negligible, respectively
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava.
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava.
- 出身王族与普通出身的分别在原文里怎么界定

### 判断方法路

- Effects of Karm’s Lord in Various Bhavas
- Effects of Dharm’s Lord in Various Bhavas
- 判断宫主落宫效果应查本章哪一段

## 上游问题

- 无

## 停止条件

- 缺少十宫主是否落九宫的事实时停止。
- 原文未界定「出身王族」，该项未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
