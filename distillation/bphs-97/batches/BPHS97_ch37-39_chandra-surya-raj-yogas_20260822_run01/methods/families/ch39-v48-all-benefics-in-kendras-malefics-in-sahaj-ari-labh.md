---
method: ch39-v48-all-benefics-in-kendras-malefics-in-sahaj-ari-labh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 吉星全落角宫、凶星居三宫六宫十一宫：出身寒微也登王位

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 吉星凶星各就各位有多大力量
- 出身一般能不能翻身

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 本盘中哪些行星被判为凶星
- 本盘所有吉星是否都落角宫（Kendras）
- 三宫（Sahaj）是否被凶星占据
- 六宫（Ari）是否被凶星占据
- 十一宫（Labh）是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v48-all-benefics-in-kendras-malefics-in-sahaj-ari-labh.step-001

- 动作：取吉星与凶星名册，核对所有吉星是否都落角宫，凶星是否落三宫、六宫与十一宫。
- 适用范围：仅限本命盘；原文本句未给出吉凶星的判准，也没有时间限定。
- 原文最小意思：所有吉星都落角宫（Kendras），同时凶星落三宫（Sahaj）、六宫（Ari）与十一宫（Labh Bhava）时，命主即使出身寒微也会登上王位。
- 本步骤产出事实：["吉星全居角宫凶星居三六十一宫的登位判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "本盘中哪些行星被判为凶星", "本盘所有吉星是否都落角宫（Kendras）", "三宫（Sahaj）是否被凶星占据", "六宫（Ari）是否被凶星占据", "十一宫（Labh）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "本盘中哪些行星被判为凶星"}, {"fact_key": "本盘所有吉星是否都落角宫（Kendras）"}, {"fact_key": "三宫（Sahaj）是否被凶星占据"}, {"fact_key": "六宫（Ari）是否被凶星占据"}, {"fact_key": "十一宫（Labh）是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文要求所有吉星都落角宫，不得放宽成部分吉星落角宫。", "不得据此推断登位时间或具体权位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、本盘中哪些行星被判为凶星、本盘所有吉星是否都落角宫（Kendras）、三宫（Sahaj）是否被凶星占据、六宫（Ari）是否被凶星占据、十一宫（Labh）是否被凶星占据。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "本盘中哪些行星被判为凶星", "本盘所有吉星是否都落角宫（Kendras）", "三宫（Sahaj）是否被凶星占据", "六宫（Ari）是否被凶星占据", "十一宫（Labh）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v48`｜PDF [84]｜“If all benefics are relegated to Kendras, while malefics are in Sahaj, Ari and Labh Bhava, the native, though may be of mean descent, will ascend the throne.”


## 四路查书计划

### 支持路

- If all benefics are relegated to Kendras, while malefics are in Sahaj, Ari and Labh Bhava, the native, though may be of mean descent, will ascend the throne
- 吉星全落角宫 凶星三宫六宫十一宫 登王位

### 反例或取消路

- If inauspicious Bhavas are occupied by benefics, while auspicious Bhavas are occupied by malefics, the native will be indigent and will be distressed even in the matter of food
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Sahaj, Ari, Karm and Labh Bhava are Upachaya Bhavas
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少吉星或凶星名册事实时停止。
- 四项占据事实缺任一项时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
