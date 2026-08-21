---
method: ch21-v8-10-karm-lord-in-meen-with-guru
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 衣物装饰与幸福：十宫主有力、落双鱼座并与木星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有好衣服好首饰
- 十宫主落双鱼座与木星同宫有什么效果

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否有力
- 十宫主（Karm's Lord）是否落双鱼座（Meen）
- 十宫主（Karm's Lord）是否与木星（Guru）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v8-10-karm-lord-in-meen-with-guru.step-001

- 动作：核对十宫主（Karm's Lord）是否有力、是否落双鱼座（Meen），并核对它是否与木星（Guru）同宫。
- 适用范围：仅限三项条件同时成立这一种配置；「有力」的判准原文本句未给；原文未给时间限定。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：十宫主有力、落双鱼座并与木星同宫时，命主必定得到衣物、装饰品与幸福。
- 本步骤产出事实：["十宫主落双鱼座与木星同宫的衣物装饰判定"]
- 所需事实：["十宫主（Karm's Lord）是否有力", "十宫主（Karm's Lord）是否落双鱼座（Meen）", "十宫主（Karm's Lord）是否与木星（Guru）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否有力"}, {"fact_key": "十宫主（Karm's Lord）是否落双鱼座（Meen）"}, {"fact_key": "十宫主（Karm's Lord）是否与木星（Guru）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断财物数量、价格或取得时间。", "不得把双鱼座（Meen）换成木星主管的另一个星座。", "原文本句没有给出「有力」的判准，不得自行发明力量算法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否有力、十宫主（Karm's Lord）是否落双鱼座（Meen）、十宫主（Karm's Lord）是否与木星（Guru）同宫。
- 缺失即停字段：["十宫主（Karm's Lord）是否有力", "十宫主（Karm's Lord）是否落双鱼座（Meen）", "十宫主（Karm's Lord）是否与木星（Guru）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v8-10`｜PDF [38]｜“Should Karm’s Lord in strength be in Meen along Guru, the native will doubtless obtain robes, ornaments and happiness.”


## 四路查书计划

### 支持路

- Should Karm’s Lord in strength be in Meen along Guru, the native will doubtless obtain robes, ornaments and happiness
- 十宫主 有力 落双鱼座 与木星同宫 衣物 装饰品

### 反例或取消路

- If Karm’s Lord is devoid of strength, the native will face obstructions in his work
- If Karm’s Lord is in Vyaya Bhava, the native will spend through royal abodes, will have fear from enemies
- 十宫主无力 工作受阻

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava

### 判断方法路

- Effects of Karm’s Lord in Various Bhavas
- 判断十宫主落双鱼座并与木星同宫要查什么

## 上游问题

- 无

## 停止条件

- 缺少十宫主力量事实时停止。
- 力量判准由排盘窗口定义，未给出取值时停止。
- 缺少十宫主落双鱼座或与木星同宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
