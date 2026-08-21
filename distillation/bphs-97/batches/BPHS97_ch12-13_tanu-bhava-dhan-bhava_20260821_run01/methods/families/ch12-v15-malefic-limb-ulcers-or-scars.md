---
method: ch12-v15-malefic-limb-ulcers-or-scars
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 肢体有溃疡或疤痕：该肢体对应的宫被凶星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身上的疤是怎么来的
- 凶星占的宫对应哪个部位会有伤

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘一宫（Lagn）所在星座的三分盘（Drekkana D3）给出的宫位肢体对应是哪一组
- 该肢体所对应的宫（Bhava）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- ch12-v12-14-first-decanate-limb-order
- ch12-v12-14-second-decanate-limb-order
- ch12-v12-14-third-decanate-limb-order

## 执行步骤

### ch12-v15-malefic-limb-ulcers-or-scars.step-001

- 动作：先按上升三分盘取出宫位与肢体的对应，再核对该肢体所对应的宫是否被凶星占据。
- 适用范围：仅限本命盘肢体伤痕主题；本句的 The limb 承接第12章 v12-14 给出的宫位肢体对应表；结句 So say the Jyotishis 表明这是占星家们的转述，结论强度不与作者自断等同。
- 原文最小意思：被凶星以占据方式关联到的那个肢体，会有溃疡或疤痕；这是占星家们的说法。
- 本步骤产出事实：["凶星占据宫位对应肢体的伤痕判定"]
- 所需事实：["本盘一宫（Lagn）所在星座的三分盘（Drekkana D3）给出的宫位肢体对应是哪一组", "该肢体所对应的宫（Bhava）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘一宫（Lagn）所在星座的三分盘（Drekkana D3）给出的宫位肢体对应是哪一组"}, {"fact_key": "该肢体所对应的宫（Bhava）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把占据以外的关联方式（相照、主管）也算作本句的凶星关联，原文这半句写的是 by occupation。", "不得据此断出伤痕出现的时间，那是括注引述 Saravali 的另一条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘一宫（Lagn）所在星座的三分盘（Drekkana D3）给出的宫位肢体对应是哪一组、该肢体所对应的宫（Bhava）是否被凶星占据。
- 缺失即停字段：["本盘一宫（Lagn）所在星座的三分盘（Drekkana D3）给出的宫位肢体对应是哪一组", "该肢体所对应的宫（Bhava）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v15`｜PDF [27]｜“The limb, related to a malefic by occupation, will have ulcers, or scars”
  - `bphs-97:santhanam:ch12:v15`｜PDF [27]｜“So say the Jyotishis”


## 四路查书计划

### 支持路

- The limb, related to a malefic by occupation, will have ulcers, or scars
- 凶星占据的宫对应肢体 溃疡疤痕

### 反例或取消路

- while the one, related to a benefic, will have a mark (like moles etc)

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- One third of a Rashiis called Dreshkan. These are totally 36, counted from Mesh, repeating thrice at the rate of 12 per round
- Effects of Moles, Marks, Signs etc. for Men and Women

### 判断方法路

- Now I will describe to you the effects of moles, marks, spots and signs, found on the body of women and men
- O Brahmin, following are the effects, produced by Ari Bhava, relating to diseases, ulcers etc. Listen to this attentively
- 判断肢体伤痕要先取上升三分盘的宫位肢体对应

## 上游问题

- 无

## 停止条件

- 缺少上升三分盘宫位肢体对应表时停止（对应表见第12章 v12-14）。
- 缺少该宫是否被凶星占据的事实时停止。
- 凶星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
