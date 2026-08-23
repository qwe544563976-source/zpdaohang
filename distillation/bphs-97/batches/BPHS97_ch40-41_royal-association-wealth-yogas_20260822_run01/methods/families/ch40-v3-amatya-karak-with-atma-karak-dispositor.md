---
method: ch40-v3-amatya-karak-with-atma-karak-dispositor
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 大智并为王之大臣：Amatya Karak 与 Atma Karak 的星座主同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的头脑与见识怎么样
- 我有没有辅佐掌权者的命

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的 Amatya Karak 是哪颗行星
- 本盘的 Atma Karak 是哪颗行星
- Amatya Karak 是否与 Atma Karak 的星座主（dispositor）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch40-v3-amatya-karak-with-atma-karak-dispositor.step-001

- 动作：先认出 Amatya Karak 与 Atma Karak，再取 Atma Karak 所落星座的星座主，核对它是否与 Amatya Karak 同宫。
- 适用范围：仅限本命盘两个 Char Karak 一线；原文本偈附有英译者括注（‘Karakendr’ is interpreted here, as the dispositor of Atma Karak），此处「Atma Karak 的星座主」这一读法出自英译者，结论强度不能与 Parashara 自断等同；原文未给时间限定。
- 原文最小意思：Amatya Karak 与 Atma Karak 的星座主同宫时，命主将具大智慧，并成为王之大臣。
- 本步骤产出事实：["Amatya Karak 与 Atma Karak 星座主同宫的智慧与大臣判定"]
- 所需事实：["本盘的 Amatya Karak 是哪颗行星", "本盘的 Atma Karak 是哪颗行星", "Amatya Karak 是否与 Atma Karak 的星座主（dispositor）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘的 Amatya Karak 是哪颗行星"}, {"fact_key": "本盘的 Atma Karak 是哪颗行星"}, {"fact_key": "Amatya Karak 是否与 Atma Karak 的星座主（dispositor）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写同宫（be together），不得把它扩大成相照或互换。", "不得据此推断学历、职衔或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的 Amatya Karak 是哪颗行星、本盘的 Atma Karak 是哪颗行星、Amatya Karak 是否与 Atma Karak 的星座主（dispositor）同宫。
- 缺失即停字段：["本盘的 Amatya Karak 是哪颗行星", "本盘的 Atma Karak 是哪颗行星", "Amatya Karak 是否与 Atma Karak 的星座主（dispositor）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v3`｜PDF [85]｜“Should Amatya Karak and the dispositor of Atma Karak be together, the native will be endowed with great intelligence and will be a king’s minister.”


## 四路查书计划

### 支持路

- Should Amatya Karak and the dispositor of Atma Karak be together, the native will be endowed with great intelligence
- Amatya Karak 与 Atma Karak 星座主同宫 大智 大臣

### 反例或取消路

- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- The Grah next to Atma Karak in terms of longitude is called Amatya Karak
- Out of these Karakas, Atma Karak is the most important and has a prime say on the native

### 判断方法路

- Yogas For Royal Association
- If Atma Karak is strong and is with a benefic, or Amatya Karak is in its own Bhava, or in exaltation

## 上游问题

- 无

## 停止条件

- Amatya Karak 或 Atma Karak 的身份事实缺失时停止。
- Atma Karak 所落星座的星座主未取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
