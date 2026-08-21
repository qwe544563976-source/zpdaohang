---
method: ch36-v18-shrinath-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Shrinath Yog：七宫主落十宫，十宫主入旺并与九宫主同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有极贵重的组合
- 我的事业宫组合好不好

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 七宫主（Yuvati's Lord）是否落十宫（Karm）
- 十宫主（Karm's Lord）是否入旺
- 十宫主（Karm's Lord）是否与九宫主（Dharm's Lord）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch36-v18-shrinath-yog.step-001

- 动作：核对七宫主（Yuvati's Lord）是否落十宫（Karm），以及十宫主（Karm's Lord）是否入旺并与九宫主（Dharm's Lord）同宫，判定 Shrinath Yog 是否成立。
- 适用范围：仅限本命盘 Shrinath Yog 的成立判定；原文三项条件同时成立才算，未给时间限定。
- 原文最小意思：七宫主（Yuvati's Lord）落十宫（Karm），十宫主（Karm's Lord）入旺并与九宫主（Dharm's Lord）同宫，则 Shrinath Yog 成立。
- 本步骤产出事实：["Shrinath Yog 成立判定"]
- 所需事实：["七宫主（Yuvati's Lord）是否落十宫（Karm）", "十宫主（Karm's Lord）是否入旺", "十宫主（Karm's Lord）是否与九宫主（Dharm's Lord）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落十宫（Karm）"}, {"fact_key": "十宫主（Karm's Lord）是否入旺"}, {"fact_key": "十宫主（Karm's Lord）是否与九宫主（Dharm's Lord）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文三项条件是并列必需，不得只满足其中一两项就判成立。", "原文写十宫主入旺，不得放宽成落本星座或落本宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：七宫主（Yuvati's Lord）是否落十宫（Karm）、十宫主（Karm's Lord）是否入旺、十宫主（Karm's Lord）是否与九宫主（Dharm's Lord）同宫。
- 缺失即停字段：["七宫主（Yuvati's Lord）是否落十宫（Karm）", "十宫主（Karm's Lord）是否入旺", "十宫主（Karm's Lord）是否与九宫主（Dharm's Lord）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v18`｜PDF [80]｜“If Yuvati’s Lord is in Karm Bhava, while Karm’s Lord is exalted and yuti with Dharm’s Lord, Shrinath Yog takes place.”

### ch36-v18-shrinath-yog.step-002

- 动作：在 Shrinath Yog 成立时读取地位的断语。
- 适用范围：仅限已判定 Shrinath Yog 成立的本命盘；原文以 Lord Devendra（众神之神）作比，未给具体人事内容与时间限定。
- 原文最小意思：有 Shrinath Yog 的命主会与 Lord Devendra（god of gods，众神之神）相等。
- 本步骤产出事实：["Shrinath Yog 效果断语"]
- 所需事实：["Shrinath Yog 成立判定"]
- 条件关系：{"fact_key": "Shrinath Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只作神格比拟，不得据此推断具体官职、财富数额、寿命或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Shrinath Yog 成立判定。
- 缺失即停字段：["Shrinath Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v18`｜PDF [80]｜“The native with Shrinath Yog will be equal to Lord Devendra (god of gods).”


## 四路查书计划

### 支持路

- If Yuvati’s Lord is in Karm Bhava, while Karm’s Lord is exalted and yuti with Dharm’s Lord, Shrinath Yog takes place
- The native with Shrinath Yog will be equal to Lord Devendra
- 七宫主落十宫 十宫主入旺 九宫主同宫 Shrinath Yog

### 反例或取消路

- Note the Grahas, that are ruling the Rāśis, occupied by the Lords of Ari, Randhr and Vyaya Bhava
- If inauspicious Bhavas are occupied by benefics, while auspicious Bhavas are occupied by malefics, the native will be indigent
- If the Lords of a Kendr, or a Kon own simultaneously an evil Bhava, he does not cause a Raj Yog by mere relations stipulated

### 适用边界路

- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula
- Benefics, owning Kendras, will not give benefic effects, while malefics, owning Kendras, will not remain inauspicious
- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少七宫主落十宫、十宫主入旺、十宫主与九宫主同宫三项中任一项事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
