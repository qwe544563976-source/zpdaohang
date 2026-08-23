---
method: ch39-v21-benefics-in-kendras-raj-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 吉星落角宫：同样成立贵格

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 吉星落四正宫有多重要
- 我盘里的吉星位置好不好

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 角宫（Kendras）内是否有吉星

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v21-benefics-in-kendras-raj-yog.step-001

- 动作：取本盘吉星名册，核对角宫（Kendras）内是否有吉星。
- 适用范围：仅限本命盘 Raj Yog 的成立判定；原文的 Similar is the case 承同偈前句十宫主相照上升一条的结论（a Raj Yog is formed）；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：吉星落角宫（Kendras）时，同样成立 Raj Yog。
- 本步骤产出事实：["吉星落角宫的贵格判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "角宫（Kendras）内是否有吉星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "角宫（Kendras）内是否有吉星"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只说吉星落角宫，不得补上十宫主或相照等原文此句没有的条件。", "不得据此推断职位、财富或应期。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、角宫（Kendras）内是否有吉星。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "角宫（Kendras）内是否有吉星"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v21`｜PDF [83]｜“Similar is the case, if benefics are in Kendras.”
  - `bphs-97:santhanam:ch39:v21`｜PDF [83]｜“a Raj Yog is formed”


## 四路查书计划

### 支持路

- Similar is the case, if benefics are in Kendras
- 吉星落角宫 贵格成立

### 反例或取消路

- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas
- If inauspicious Bhavas are occupied by benefics, while auspicious Bhavas are occupied by malefics, the native will be indigent and will be distressed even in the matter of food

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Budh, however, is a malefic, if he joins a malefic

### 判断方法路

- If the Lord of a Kendr establishes a relationship with the Lord of a Kon, a Raj Yog is obtained
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少本盘吉星名册事实时停止。
- 缺少角宫吉星占据事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
