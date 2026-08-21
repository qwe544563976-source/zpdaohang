---
method: ch21-v12-guru-meen-shukr-learned-wealthy
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 有学问且富有：木星落双鱼座与金星同宫，上升主有力且月亮入旺

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有学问又有钱
- 木星落双鱼座跟金星同宫是什么效果

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否落双鱼座（Meen）
- 木星（Guru）是否与金星（Shukra）同宫
- 上升主（Lagn's Lord）是否有力
- 月亮（Chandra）是否入旺

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v12-guru-meen-shukr-learned-wealthy.step-001

- 动作：核对木星（Guru）是否落双鱼座（Meen）并与金星（Shukra）同宫，同时核对上升主是否有力、月亮（Chandra）是否入旺。
- 适用范围：仅限四项条件同时成立这一种配置；「有力」的判准原文本句未给；原文未给时间限定。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：木星落双鱼座并与金星同宫，同时上升主有力、月亮入旺时，命主会有学问且富有。
- 本步骤产出事实：["木星落双鱼座与金星同宫的学问财富判定"]
- 所需事实：["木星（Guru）是否落双鱼座（Meen）", "木星（Guru）是否与金星（Shukra）同宫", "上升主（Lagn's Lord）是否有力", "月亮（Chandra）是否入旺"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落双鱼座（Meen）"}, {"fact_key": "木星（Guru）是否与金星（Shukra）同宫"}, {"fact_key": "上升主（Lagn's Lord）是否有力"}, {"fact_key": "月亮（Chandra）是否入旺"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断学历、职业或财富数额。", "不得把四项条件拆成任取其一。", "原文本句没有给出「有力」的判准，不得自行发明力量算法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落双鱼座（Meen）、木星（Guru）是否与金星（Shukra）同宫、上升主（Lagn's Lord）是否有力、月亮（Chandra）是否入旺。
- 缺失即停字段：["木星（Guru）是否落双鱼座（Meen）", "木星（Guru）是否与金星（Shukra）同宫", "上升主（Lagn's Lord）是否有力", "月亮（Chandra）是否入旺"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v12`｜PDF [38]｜“One will be learned and wealthy, if Guru is in Meen along with Shukr, while Lagn’s Lord is strong and Chandra is in exaltation.”


## 四路查书计划

### 支持路

- One will be learned and wealthy, if Guru is in Meen along with Shukr, while Lagn’s Lord is strong and Chandra is in exaltation
- 木星落双鱼座 与金星同宫 上升主有力 月亮入旺 有学问 富有

### 反例或取消路

- Please tell me such Yogas, causing utter poverty
- If Karm’s Lord is devoid of strength, the native will face obstructions in his work
- 导致贫穷的组合

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula
- I now tell you of special combinations, giving wealth. One born to these Yogas will surely become wealthy

### 判断方法路

- Effects of Karm’s Lord in Various Bhavas
- 判断学问与财富要核对哪些行星

## 上游问题

- 无

## 停止条件

- 缺少木星落双鱼座或与金星同宫的事实时停止。
- 缺少上升主力量事实时停止，力量判准由排盘窗口定义。
- 缺少月亮入旺的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
