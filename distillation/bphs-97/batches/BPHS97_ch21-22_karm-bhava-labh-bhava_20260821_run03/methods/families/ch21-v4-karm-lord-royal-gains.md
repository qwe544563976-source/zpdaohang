---
method: ch21-v4-karm-lord-royal-gains
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 王室恩宠与生意得利：十宫主与吉星同宫或落吉宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我能不能靠贵人或上级得利
- 我做生意赚不赚钱

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘十宫主（Karm's Lord）是哪颗行星

## 按情况检查的事实

- 十宫主（Karm's Lord）是否与吉星同宫
- 十宫主（Karm's Lord）是否落在吉宫（auspicious Bhava）

## 依赖方法

- 无

## 执行步骤

### ch21-v4-karm-lord-royal-gains.step-001

- 动作：先定出十宫主（Karm's Lord）是哪颗行星，再核对它是否与吉星同宫，或是否落在吉宫。
- 适用范围：仅限本命盘十宫（Karm Bhava）主题下的王室恩宠与生意得利；原文本句未界定哪些宫属于吉宫，也未给时间限定。本章效果原文自述以 Brahma、Garga 等人之言转述（同章 v1）。
- 原文最小意思：十宫主与吉星同宫，或落在吉宫时，命主总能通过王室恩宠和生意获利。
- 本步骤产出事实：["十宫主吉星同宫或落吉宫的王室与生意获利判定"]
- 所需事实：["本盘十宫主（Karm's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "十宫主（Karm's Lord）是否与吉星同宫"}, {"fact_key": "十宫主（Karm's Lord）是否落在吉宫（auspicious Bhava）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, "required_fact_keys": ["十宫主（Karm's Lord）是否与吉星同宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否与吉星同宫"}, "selection_group": "ch21-v4-karm-lord-royal-gains.step-001:karm-lord-association", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否与吉星同宫。"}, {"when": {"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, "required_fact_keys": ["十宫主（Karm's Lord）是否落在吉宫（auspicious Bhava）"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否落在吉宫（auspicious Bhava）"}, "selection_group": "ch21-v4-karm-lord-royal-gains.step-001:karm-lord-association", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否落在吉宫（auspicious Bhava）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断获利的金额、行业或时间。", "不得自行规定哪些宫算吉宫，界定须来自原文另有出处的段落。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘十宫主（Karm's Lord）是哪颗行星。
- 缺失即停字段：["本盘十宫主（Karm's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v4`｜PDF [38]｜“If Karm’s Lord is with a benefic, or be in an auspicious Bhava, one will always gain through royal patronage and in business.”


## 四路查书计划

### 支持路

- If Karm’s Lord is with a benefic, or be in an auspicious Bhava, one will always gain through royal patronage and in business
- 十宫主 与吉星同宫 吉宫 王室恩宠 生意获利

### 反例或取消路

- In a contrary situation, only opposite results will come to pass
- Should Karm and Labh Bhava be both occupied by malefics, the native will indulge only in bad deeds
- 十宫与十一宫被凶星占据 只做坏事

### 适用边界路

- Kendras and Konas (Putr and Dharm) are auspicious Bhavas, the association with which turns even evil into auspiciousness
- Ari, Randhr and Vyaya are Trikas, Dusthan, or malefic Bhavas
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Effects of Karm’s Lord in Various Bhavas
- 判断十宫主所落宫位的吉凶要查什么

## 上游问题

- 无

## 停止条件

- 无法确定十宫主是哪颗行星时停止。
- 缺少十宫主与吉星同宫或落吉宫的事实时停止。
- 吉星名册未取得时停止。
- 吉宫的界定未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
