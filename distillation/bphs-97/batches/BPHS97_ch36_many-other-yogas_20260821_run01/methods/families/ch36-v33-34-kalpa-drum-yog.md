---
method: ch36-v33-34-kalpa-drum-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Kalpa Drum Yog：上升主及其三层星座主全落角宫三角宫或全入旺

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子的财富和地位怎么样
- 我有没有掌权的命

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升主（Lagn's Lord）是哪颗行星
- 上升主（Lagn's Lord）的星座主（dispositor，原文记为 a）是哪颗行星
- 原文记为 a 的行星的星座主（dispositor，原文记为 b）是哪颗行星
- 原文记为 b 的行星在九分盘（Navamsa D9）中的星座主是哪颗行星

## 按情况检查的事实

- 这四颗行星是否都落在从上升（Lagna）起算的角宫（Kendras）与三角宫（Konas）内
- 这四颗行星是否都入旺

## 依赖方法

- 无

## 执行步骤

### ch36-v33-34-kalpa-drum-yog.step-001

- 动作：先按原文顺序取出四颗行星：上升主（Lagn's Lord）、上升主的星座主 a、行星 a 的星座主 b、行星 b 的九分盘（Navamsa D9）星座主；再核对这四颗是全落角宫三角宫还是全部入旺。
- 适用范围：仅限本命盘 Kalpa Drum Yog 的成立与效果；原文只对最后一层用九分盘（Navāńś）取星座主，前三层都在本盘取，不得混用。原文未给上升限定，也未给时间限定。
- 原文最小意思：上升主（Lagn's Lord）、上升主的星座主 a、行星 a 的星座主 b、行星 b 的九分盘（Navamsa D9）星座主这四颗行星，全部落在从上升（Lagna）起算的角宫（Kendras）与三角宫（Konas）内，或者全部入旺时，成立 Kalpa Drum Yog，命主会拥有各种财富、成为国王、虔诚、强壮、好战、慈悲。
- 本步骤产出事实：["Kalpa Drum Yog 成立判定"]
- 所需事实：["本盘上升主（Lagn's Lord）是哪颗行星", "上升主（Lagn's Lord）的星座主（dispositor，原文记为 a）是哪颗行星", "原文记为 a 的行星的星座主（dispositor，原文记为 b）是哪颗行星", "原文记为 b 的行星在九分盘（Navamsa D9）中的星座主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）的星座主（dispositor，原文记为 a）是哪颗行星"}, {"fact_key": "原文记为 a 的行星的星座主（dispositor，原文记为 b）是哪颗行星"}, {"fact_key": "原文记为 b 的行星在九分盘（Navamsa D9）中的星座主是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "这四颗行星是否都落在从上升（Lagna）起算的角宫（Kendras）与三角宫（Konas）内"}, {"fact_key": "这四颗行星是否都入旺"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）的星座主（dispositor，原文记为 a）是哪颗行星"}, {"fact_key": "原文记为 a 的行星的星座主（dispositor，原文记为 b）是哪颗行星"}, {"fact_key": "原文记为 b 的行星在九分盘（Navamsa D9）中的星座主是哪颗行星"}]}, "required_fact_keys": ["这四颗行星是否都落在从上升（Lagna）起算的角宫（Kendras）与三角宫（Konas）内"], "branch_condition_logic": {"fact_key": "这四颗行星是否都落在从上升（Lagna）起算的角宫（Kendras）与三角宫（Konas）内"}, "selection_group": "ch36-v33-34-kalpa-drum-yog.step-001:kalpa-drum-disposition", "stop_condition": "选中该分支后，缺少以下事实即停止：这四颗行星是否都落在从上升（Lagna）起算的角宫（Kendras）与三角宫（Konas）内。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘上升主（Lagn's Lord）是哪颗行星"}, {"fact_key": "上升主（Lagn's Lord）的星座主（dispositor，原文记为 a）是哪颗行星"}, {"fact_key": "原文记为 a 的行星的星座主（dispositor，原文记为 b）是哪颗行星"}, {"fact_key": "原文记为 b 的行星在九分盘（Navamsa D9）中的星座主是哪颗行星"}]}, "required_fact_keys": ["这四颗行星是否都入旺"], "branch_condition_logic": {"fact_key": "这四颗行星是否都入旺"}, "selection_group": "ch36-v33-34-kalpa-drum-yog.step-001:kalpa-drum-disposition", "stop_condition": "选中该分支后，缺少以下事实即停止：这四颗行星是否都入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把四颗行星减为三颗或把链条延长到第五层。", "只有第四颗用九分盘（Navamsa D9）取星座主，不得把九分盘用到前三颗上。", "不得据此推断战争、财富的具体形式或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升主（Lagn's Lord）是哪颗行星、上升主（Lagn's Lord）的星座主（dispositor，原文记为 a）是哪颗行星、原文记为 a 的行星的星座主（dispositor，原文记为 b）是哪颗行星、原文记为 b 的行星在九分盘（Navamsa D9）中的星座主是哪颗行星。
- 缺失即停字段：["本盘上升主（Lagn's Lord）是哪颗行星", "上升主（Lagn's Lord）的星座主（dispositor，原文记为 a）是哪颗行星", "原文记为 a 的行星的星座主（dispositor，原文记为 b）是哪颗行星", "原文记为 b 的行星在九分盘（Navamsa D9）中的星座主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v33-34`｜PDF [80]｜“Note the following four Grahas: Lagn’s Lord , the dispositor of Lagn’s Lord (a), the dispositor of the Grah “a” (b), the Navāńś dispositor of the Grah “b”. If all these are disposed in Kendras and in Konas from Lagna, or are exalted, Kalpa Drum Yog exists. One with Kalpa Drum Yog will be endowed with all kinds of wealth, be a king, pious, strong, fond of war and merciful.”


## 四路查书计划

### 支持路

- Kalpa Drum Yog. Note the following four Grahas: Lagn’s Lord , the dispositor of Lagn’s Lord
- Kalpa Drum Yog 上升主 星座主 九分盘星座主 角宫三角宫 入旺

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine)
- Navāńś. The Navāńś calculation are for a Movable Rashifrom there itself, for a Fixed Rashifrom the 9<sup>th</sup> thereof
- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula

### 判断方法路

- If four, or five Grahas occupy their exaltation Rāśis, or Mooltrikon Rāśis, even a person of base birth will become king
- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour

## 上游问题

- 无

## 停止条件

- 缺少四颗行星中任一颗的身份事实时停止。
- 命中落宫分支后，缺少四颗行星全落角宫三角宫的事实时停止。
- 命中入旺分支后，缺少四颗行星全部入旺的事实时停止。
- 九分盘（Navamsa D9）星座主的取值口径未按本书 ch06 取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
