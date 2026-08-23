---
method: ch40-v9-moon-dispositor-as-atma-karak-in-tanu
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 高龄之年成为王之大臣：月亮星座主即 Atma Karak 并偕吉星落一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的运是不是要到晚年才起来
- 我什么时候能坐到高位

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘中哪些行星被判为吉星
- 本盘月亮（Chandra）所落星座的星座主（dispositor）是哪颗行星
- 月亮（Chandra）所落星座的星座主（dispositor）是否即 Atma Karak
- 月亮（Chandra）所落星座的星座主（dispositor）是否落一宫（Tanu Bhava）
- 月亮（Chandra）所落星座的星座主（dispositor）是否与吉星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch40-v9-moon-dispositor-as-atma-karak-in-tanu.step-001

- 动作：先取月亮所落星座的星座主，核对它是不是本盘的 Atma Karak，再看这颗行星是否与吉星同宫落在一宫（Tanu Bhava）。
- 适用范围：仅限本命盘月亮星座主兼 Atma Karak 一线；原文本偈未给吉星判准，须另按本书第 3 章的吉凶星名册取得；原文以「at his advanced age」限定应期，未给具体年岁。
- 原文最小意思：月亮（Chandra）所落星座的星座主即是 Atma Karak，且这颗行星与吉星同宫落在一宫（Tanu Bhava）时，命主将在其高龄之年成为王之大臣。
- 本步骤产出事实：["月亮星座主兼 Atma Karak 落一宫的晚年大臣判定"]
- 所需事实：["本盘中哪些行星被判为吉星", "本盘月亮（Chandra）所落星座的星座主（dispositor）是哪颗行星", "月亮（Chandra）所落星座的星座主（dispositor）是否即 Atma Karak", "月亮（Chandra）所落星座的星座主（dispositor）是否落一宫（Tanu Bhava）", "月亮（Chandra）所落星座的星座主（dispositor）是否与吉星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘中哪些行星被判为吉星"}, {"fact_key": "本盘月亮（Chandra）所落星座的星座主（dispositor）是哪颗行星"}, {"fact_key": "月亮（Chandra）所落星座的星座主（dispositor）是否即 Atma Karak"}, {"fact_key": "月亮（Chandra）所落星座的星座主（dispositor）是否落一宫（Tanu Bhava）"}, {"fact_key": "月亮（Chandra）所落星座的星座主（dispositor）是否与吉星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只说 at his advanced age，不得据此推出具体年岁或大运。", "不得把三项条件拆开单用，原文要求同时成立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中哪些行星被判为吉星、本盘月亮（Chandra）所落星座的星座主（dispositor）是哪颗行星、月亮（Chandra）所落星座的星座主（dispositor）是否即 Atma Karak、月亮（Chandra）所落星座的星座主（dispositor）是否落一宫（Tanu Bhava）、月亮（Chandra）所落星座的星座主（dispositor）是否与吉星同宫。
- 缺失即停字段：["本盘中哪些行星被判为吉星", "本盘月亮（Chandra）所落星座的星座主（dispositor）是哪颗行星", "月亮（Chandra）所落星座的星座主（dispositor）是否即 Atma Karak", "月亮（Chandra）所落星座的星座主（dispositor）是否落一宫（Tanu Bhava）", "月亮（Chandra）所落星座的星座主（dispositor）是否与吉星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v9`｜PDF [85]｜“If the Lord of the Rāśi, where Chandra is placed becomes Atma Karak and, if this Lord is placed in Tanu Bhava along with a benefic, the native will become a king’s minister at his advanced age.”


## 四路查书计划

### 支持路

- If the Lord of the Rāśi, where Chandra is placed becomes Atma Karak and, if this Lord is placed in Tanu Bhava along with a benefic
- 月亮星座主为 Atma Karak 落一宫 与吉星同宫 晚年大臣

### 反例或取消路

- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The Grah next to Atma Karak in terms of longitude is called Amatya Karak

### 判断方法路

- Yogas For Royal Association
- There is no doubt in one’s becoming a king’s minister and famous, if Atma Karak is in Tanu, or Putr, or Dharm Bhava

## 上游问题

- 无

## 停止条件

- 月亮所落星座的星座主未取到时停止。
- 该行星是否即 Atma Karak 的事实缺失时停止。
- 吉星名册未定时停止：须先按 BPHS 自己的吉凶星定义取名册。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
