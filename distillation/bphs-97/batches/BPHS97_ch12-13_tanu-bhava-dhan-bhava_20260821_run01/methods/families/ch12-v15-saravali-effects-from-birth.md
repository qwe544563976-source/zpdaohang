---
method: ch12-v15-saravali-effects-from-birth
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 记号自出生起就有：所涉行星落本星座或本九分盘

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我身上的痕迹是天生的还是后来的
- 行星落本星座会怎样影响记号出现的时间

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 与该肢体关联的行星是哪一颗

## 按情况检查的事实

- 与该肢体关联的行星是否落本星座（own Rāśi）
- 与该肢体关联的行星是否落本九分盘（own Navāńś）

## 依赖方法

- ch12-v15-malefic-limb-ulcers-or-scars
- ch12-v15-benefic-limb-mark

## 执行步骤

### ch12-v15-saravali-effects-from-birth.step-001

- 动作：核对与该肢体关联的那颗行星是否落在自己主管的星座，或落在自己的九分盘。
- 适用范围：此句是英译者在括注中转引 Saravali 第4章第6颂的说法，不是 BPHS 作者自断，结论强度不与作者自断等同；承接第12章 v15 前句的凶星与吉星关联。
- 原文最小意思：英译者括注转引 Saravali 第4章第6颂：凶星或吉星落自己主管的星座（own Rāśi）或落自己的九分盘（Navāńś）时，这些效果从出生起就有。
- 本步骤产出事实：["肢体记号自出生起显现的判定"]
- 所需事实：["与该肢体关联的行星是哪一颗"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "与该肢体关联的行星是哪一颗"}, {"operator": "OR", "operands": [{"fact_key": "与该肢体关联的行星是否落本星座（own Rāśi）"}, {"fact_key": "与该肢体关联的行星是否落本九分盘（own Navāńś）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "与该肢体关联的行星是哪一颗"}, "required_fact_keys": ["与该肢体关联的行星是否落本星座（own Rāśi）"], "branch_condition_logic": {"fact_key": "与该肢体关联的行星是否落本星座（own Rāśi）"}, "selection_group": "ch12-v15-saravali-effects-from-birth.step-001:own-varga", "stop_condition": "选中该分支后，缺少以下事实即停止：与该肢体关联的行星是否落本星座（own Rāśi）。"}, {"when": {"fact_key": "与该肢体关联的行星是哪一颗"}, "required_fact_keys": ["与该肢体关联的行星是否落本九分盘（own Navāńś）"], "branch_condition_logic": {"fact_key": "与该肢体关联的行星是否落本九分盘（own Navāńś）"}, "selection_group": "ch12-v15-saravali-effects-from-birth.step-001:own-varga", "stop_condition": "选中该分支后，缺少以下事实即停止：与该肢体关联的行星是否落本九分盘（own Navāńś）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这条转引的 Saravali 说法当成 BPHS 作者自断。", "不得把 own Rāśi 读成本宫，它指行星自己主管的星座。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：与该肢体关联的行星是哪一颗。
- 缺失即停字段：["与该肢体关联的行星是哪一颗"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v15`｜PDF [27]｜“Also see Sloka 6, Ch. 4 of Saravali, which states, that a malefic, or a benefic, if be in own Rāśi, or Navāńś, the effects will be right from birth.”


## 四路查书计划

### 支持路

- that a malefic, or a benefic, if be in own Rāśi, or Navāńś, the effects will be right from birth
- 行星落本星座或本九分盘 记号自出生起就有

### 反例或取消路

- In other cases it will be in the course of one’s life, that these effects will come to pass

### 适用边界路

- Effects of Moles, Marks, Signs etc. for Men and Women
- The Navāńś calculation are for a Movable Rashifrom there itself, for a Fixed Rashifrom the 9th thereof and for a Dual Rashifrom the 5th thereof
- The Sixteen Divisions of a Rāśi

### 判断方法路

- Now I will describe to you the effects of moles, marks, spots and signs, found on the body of women and men
- One third of a Rashiis called Dreshkan. These are totally 36, counted from Mesh, repeating thrice at the rate of 12 per round
- 判断记号出现的时间要看所涉行星落不落本星座本九分盘

## 上游问题

- 无

## 停止条件

- 缺少与该肢体关联的行星身份事实时停止。
- 本星座与本九分盘两个分支事实全缺时停止。
- 此条出自转引 Saravali，需要与 BPHS 自断区分时须回查原书。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
