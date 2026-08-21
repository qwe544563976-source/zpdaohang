---
method: ch12-v5-7-budh-guru-shukra-royal-fortunes
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 享王者富贵：水木金落从上升起算的四七十宫，或与月亮同落一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有大富贵
- 水星木星金星落四宫七宫十宫代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘一宫（Lagn）落在哪个星座

## 按情况检查的事实

- 水星（Budh）是否落四宫（Bandhu）
- 水星（Budh）是否落七宫（Yuvati）
- 水星（Budh）是否落十宫（Karm）
- 木星（Guru）是否落四宫（Bandhu）
- 木星（Guru）是否落七宫（Yuvati）
- 木星（Guru）是否落十宫（Karm）
- 金星（Shukra）是否落四宫（Bandhu）
- 金星（Shukra）是否落七宫（Yuvati）
- 金星（Shukra）是否落十宫（Karm）
- 水星（Budh）是否落一宫（Tanu）
- 木星（Guru）是否落一宫（Tanu）
- 金星（Shukra）是否落一宫（Tanu）
- 月亮（Chandra）是否落一宫（Tanu）

## 依赖方法

- 无

## 执行步骤

### ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001

- 动作：逐一核对水星、木星、金星是否落在从上升起算的四宫、七宫、十宫，或是否与月亮同落一宫。
- 适用范围：仅限本命盘一宫（Tanu Bhava）富贵主题；原文本句自列了四宫、七宫、十宫这三个宫位。
- 原文最小意思：水星（Budh）、木星（Guru）或金星（Shukra）落从上升起算的四宫、七宫或十宫，或与月亮（Chandra）一同落一宫（Lagna）时，命主会享有王者般的富贵。
- 本步骤产出事实：["水木金落四七十宫或与月亮同宫的富贵判定"]
- 所需事实：["本盘一宫（Lagn）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘一宫（Lagn）落在哪个星座"}, {"operator": "OR", "operands": [{"fact_key": "水星（Budh）是否落四宫（Bandhu）"}, {"fact_key": "水星（Budh）是否落七宫（Yuvati）"}, {"fact_key": "水星（Budh）是否落十宫（Karm）"}, {"fact_key": "木星（Guru）是否落四宫（Bandhu）"}, {"fact_key": "木星（Guru）是否落七宫（Yuvati）"}, {"fact_key": "木星（Guru）是否落十宫（Karm）"}, {"fact_key": "金星（Shukra）是否落四宫（Bandhu）"}, {"fact_key": "金星（Shukra）是否落七宫（Yuvati）"}, {"fact_key": "金星（Shukra）是否落十宫（Karm）"}, {"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["水星（Budh）是否落四宫（Bandhu）"], "branch_condition_logic": {"fact_key": "水星（Budh）是否落四宫（Bandhu）"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落四宫（Bandhu）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["水星（Budh）是否落七宫（Yuvati）"], "branch_condition_logic": {"fact_key": "水星（Budh）是否落七宫（Yuvati）"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落七宫（Yuvati）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["水星（Budh）是否落十宫（Karm）"], "branch_condition_logic": {"fact_key": "水星（Budh）是否落十宫（Karm）"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落十宫（Karm）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["木星（Guru）是否落四宫（Bandhu）"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落四宫（Bandhu）"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落四宫（Bandhu）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["木星（Guru）是否落七宫（Yuvati）"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落七宫（Yuvati）"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落七宫（Yuvati）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["木星（Guru）是否落十宫（Karm）"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落十宫（Karm）"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落十宫（Karm）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落四宫（Bandhu）"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落四宫（Bandhu）"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落四宫（Bandhu）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落七宫（Yuvati）"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落七宫（Yuvati）"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落七宫（Yuvati）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落十宫（Karm）"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落十宫（Karm）"}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落十宫（Karm）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["水星（Budh）是否落一宫（Tanu）", "月亮（Chandra）是否落一宫（Tanu）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "水星（Budh）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落一宫（Tanu）、月亮（Chandra）是否落一宫（Tanu）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["木星（Guru）是否落一宫（Tanu）", "月亮（Chandra）是否落一宫（Tanu）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落一宫（Tanu）、月亮（Chandra）是否落一宫（Tanu）。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落一宫（Tanu）", "月亮（Chandra）是否落一宫（Tanu）"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落一宫（Tanu）"}, {"fact_key": "月亮（Chandra）是否落一宫（Tanu）"}]}, "selection_group": "ch12-v5-7-budh-guru-shukra-royal-fortunes.step-001:royal-fortune-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落一宫（Tanu）、月亮（Chandra）是否落一宫（Tanu）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 royal fortunes 读成一定登上王位，原文只说享有王者般的富贵。", "不得据此推断富贵到来的年份或大运。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘一宫（Lagn）落在哪个星座。
- 缺失即停字段：["本盘一宫（Lagn）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v5-7`｜PDF [26, 27]｜“If Budh, Guru, or Shukra be in 4<sup>th</sup> , 7<sup>th</sup> , or 10<sup>th</sup> from Lagna, or be in the company of Chandra in Lagna, the native will enjoy royal fortunes.”


## 四路查书计划

### 支持路

- If Budh, Guru, or Shukra be in 4th, 7th, or 10th from Lagna, or be in the company of Chandra in Lagna, the native will enjoy royal fortunes
- 水星木星金星落四宫七宫十宫 或与月亮同落一宫 王者富贵

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- Now I tell you some Yogas for poverty along with conditions of their nullifications

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The Kendras are known, as Vishnu Sthanas (Bhavas of Lord Vishnu), while the Konas are called Lakshmi Sthanas

### 判断方法路

- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- Effects of Tanu Bhava
- 判断富贵要看水木金落哪几宫

## 上游问题

- 无

## 停止条件

- 缺少上升星座事实时停止。
- 十二个分支事实全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
