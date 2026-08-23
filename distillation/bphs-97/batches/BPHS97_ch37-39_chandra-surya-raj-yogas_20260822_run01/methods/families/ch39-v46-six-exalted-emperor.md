---
method: ch39-v46-six-exalted-emperor
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 六颗行星入旺：成为帝王并享王家仪仗

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 入旺的行星特别多说明什么
- 最高一档的贵格是什么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘入旺的行星有几颗
- 本盘入旺的行星是否有六颗

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v46-six-exalted-emperor.step-001

- 动作：数本盘入旺的行星是否达到六颗。
- 适用范围：仅限本命盘；原文没有时间限定。
- 原文最小意思：有六颗行星入旺时，命主会成为帝王，并享有各种王家仪仗。
- 本步骤产出事实：["六颗行星入旺的帝王判定"]
- 所需事实：["本盘入旺的行星有几颗", "本盘入旺的行星是否有六颗"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘入旺的行星有几颗"}, {"fact_key": "本盘入旺的行星是否有六颗"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文这一条只写六颗，不得把四颗、五颗一档的结果搬到这里，也不得反向套用。", "不得据此推断疆域、朝代或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘入旺的行星有几颗、本盘入旺的行星是否有六颗。
- 缺失即停字段：["本盘入旺的行星有几颗", "本盘入旺的行星是否有六颗"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v46`｜PDF [84]｜“If six Grahas are exalted, the native will become emperor and will enjoy various kinds of royal paraphernalia.”


## 四路查书计划

### 支持路

- If six Grahas are exalted, the native will become emperor and will enjoy various kinds of royal paraphernalia
- 六颗行星入旺 帝王 王家仪仗

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- In Simh the first 20 degrees are Surya’s Mooltrikon, while the rest is his own Bhava

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少本盘入旺行星计数事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
