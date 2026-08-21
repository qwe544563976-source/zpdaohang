---
method: ch19-v4-7-longevity-strength-estimate
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 定寿命前先估量相关行星的强弱

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 定寿命之前要先看什么
- 寿命瑜伽是不是只有书里列的这几条

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 与寿命有关的行星（Grahas）的强弱如何

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch19-v4-7-longevity-strength-estimate.step-001

- 动作：在下寿命结论前，先估量与寿命有关的行星（Grahas）的强弱。
- 适用范围：承接同偈前面列出的各条寿命瑜伽（「Like these」）；原文只说要估量强弱，没有给出强弱的判准，本方法不自拟算法。
- 原文最小意思：在判定寿命时要估量相关行星的强弱；原文另说这类寿命瑜伽还有许多。
- 本步骤产出事实：["寿命判断的强弱前置检查判定"]
- 所需事实：["与寿命有关的行星（Grahas）的强弱如何"]
- 条件关系：{"fact_key": "与寿命有关的行星（Grahas）的强弱如何"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得自行发明强弱的判准；原文本句没给算法。", "不得据「还有许多瑜伽」把本书未写出的组合当作原文已给的规则。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：与寿命有关的行星（Grahas）的强弱如何。
- 缺失即停字段：["与寿命有关的行星（Grahas）的强弱如何"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v4-7`｜PDF [36]｜“Like these, there are many other Yogas, dealing with the issue of longevity. The strength and weakness of the Grahas concerned be estimated in deciding longevity.”


## 四路查书计划

### 支持路

- Like these, there are many other Yogas, dealing with the issue of longevity. The strength and weakness of the Grahas concerned be estimated in deciding longevity
- 定寿命 估量行星强弱

### 反例或取消路

- Knowing that longevity is difficult even for gods. Many exponents have laid down various methods of longevity calculations
- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- According to which of the three, Lagna, Surya, or Chandra is stronger than the other two, Ańśayu, Pindayu, or Nisargayu should be, respectively, chosen
- The life-span in Bal Risht is 8 years, in Yog Risht 20 years, in short, medium and long lives, respectively, 32, 64 and 120 years

### 判断方法路

- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- for the benefit of mankind I narrate methods of ascertaining longevity
- 行星强弱怎么算 六力

## 上游问题

- 无

## 停止条件

- 缺少行星强弱事实时停止（该判准待排盘窗口定义，见第27章 Shad Bal）。
- 本方法只作前置检查，不得单独输出寿命长短结论。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
