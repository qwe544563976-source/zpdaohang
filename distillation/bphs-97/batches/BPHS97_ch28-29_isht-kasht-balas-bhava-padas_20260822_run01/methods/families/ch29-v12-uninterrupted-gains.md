---
method: ch29-v12-uninterrupted-gains
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 上升 Pad 起第 12 宫不受相照而第 11 宫受相照：得益不中断

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的收入会不会断
- 进项稳不稳

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升 Pad（Lagn Pad）起第 12 宫是否被行星（Grah）相照
- 上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch29-v12-uninterrupted-gains.step-001

- 动作：核对上升 Pad（Lagn Pad）起第 12 宫是否不受相照，同时其起第 11 宫是否受行星相照。
- 适用范围：本条以上升 Pad（Lagn Pad）为起算点；原文没有给时间范围或适用人群限定。
- 原文最小意思：上升 Pad（Lagn Pad）起第 12 宫不受相照，而上升 Pad（Lagn Pad）起第 11 宫受行星相照时，得益不会中断。
- 本步骤产出事实：["上升 Pad 得益是否连续的判定"]
- 所需事实：["上升 Pad（Lagn Pad）起第 12 宫是否被行星（Grah）相照", "上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）相照"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "上升 Pad（Lagn Pad）起第 12 宫是否被行星（Grah）相照"}]}, {"fact_key": "上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断收入数额或持续年数。", "第 12 宫只要受任何行星相照，本条即不成立，不得只排除凶星相照。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升 Pad（Lagn Pad）起第 12 宫是否被行星（Grah）相照、上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）相照。
- 缺失即停字段：["上升 Pad（Lagn Pad）起第 12 宫是否被行星（Grah）相照", "上升 Pad（Lagn Pad）起第 11 宫是否被行星（Grah）相照"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v12`｜PDF [62]｜“O excellent of the Brahmins, if the 12<sup>th</sup> from Lagn Pad does not receive a Drishti, as the 11<sup>th</sup> from Lagn Pad receives a Drishti from a Grah, then the gains will be uninterrupted.”


## 四路查书计划

### 支持路

- if the 12<sup>th</sup> from Lagn Pad does not receive a Drishti, as the 11<sup>th</sup> from Lagn Pad receives a Drishti from a Grah, then the gains will be uninterrupted
- 上升 Pad 起第 12 宫不受照 得益不中断

### 反例或取消路

- If the 12<sup>th</sup> from Lagn Pad receives a Drishti from, or is yuti with both benefics and malefics, there will be abundant earnings, but plenty of expenses.
- 上升 Pad 起第 12 宫受吉凶相照时的破财条

### 适用边界路

- In all these cases, the 12<sup>th</sup> from Pad should simultaneously be free from malefic association.
- 得益诸条都要求第 12 宫不与凶星关联

### 判断方法路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 上升 Pad 怎么求

## 上游问题

- 无

## 停止条件

- 缺少上升 Pad 起第 11、12 宫的相照事实时停止。
- 缺少本盘上升 Pad（Lagn Pad）落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
