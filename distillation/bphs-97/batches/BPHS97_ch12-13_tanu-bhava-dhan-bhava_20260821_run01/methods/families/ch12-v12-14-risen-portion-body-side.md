---
method: ch12-v12-14-risen-portion-body-side
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 身体左右侧：已升起的部分主左侧，未升起的部分主右侧

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 身体左边右边怎么分
- 上升已升起的度数代表哪一侧

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘一宫（Lagn）在所在星座中已升起的度数是多少

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch12-v12-14-risen-portion-body-side.step-001

- 动作：取上升在所在星座中已升起的度数，据此分出身体的左右两侧。
- 适用范围：仅限本命盘身体左右侧的划分；括号内关于未升起一半的说明在原文中以括注形式出现，保留其括注身份。
- 原文最小意思：上升星座中已经升起的部分代表身体左侧，尚未升起的那一半（不可见的一半）代表身体右侧。
- 本步骤产出事实：["上升已升起部分的身体左右侧划分"]
- 所需事实：["本盘一宫（Lagn）在所在星座中已升起的度数是多少"]
- 条件关系：{"fact_key": "本盘一宫（Lagn）在所在星座中已升起的度数是多少"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此断出左右侧的吉凶，本偈只给左右侧的归属。", "不得把这条左右划分套到男女之别上，原文本句没有区分性别。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘一宫（Lagn）在所在星座中已升起的度数是多少。
- 缺失即停字段：["本盘一宫（Lagn）在所在星座中已升起的度数是多少"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v12-14`｜PDF [27]｜“The portion already risen indicates left side of the body (while the one yet to rise, i.e. the invisible half, denotes the right side of the body).”


## 四路查书计划

### 支持路

- The portion already risen indicates left side of the body (while the one yet to rise, i.e. the invisible half, denotes the right side of the body)
- 上升已升起部分主左侧 未升起部分主右侧

### 反例或取消路

- A mole, spot, or figure, formed by hair on the left side of a woman and right side of a man is auspicious

### 适用边界路

- One third of a Rashiis called Dreshkan. These are totally 36, counted from Mesh, repeating thrice at the rate of 12 per round
- Dreshkan Bal. Male, female and hermaphrodite Grahas, respectively, get a quarter Rupa according to placements in the first, second and third decanates

### 判断方法路

- Now I will describe to you the effects of moles, marks, spots and signs, found on the body of women and men
- Effects of Moles, Marks, Signs etc. for Men and Women
- 判断身体左右侧要看上升升起了多少

## 上游问题

- 无

## 停止条件

- 缺少上升已升起度数的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
