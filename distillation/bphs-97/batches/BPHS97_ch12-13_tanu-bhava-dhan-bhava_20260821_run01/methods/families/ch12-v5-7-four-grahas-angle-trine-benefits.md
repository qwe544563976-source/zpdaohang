---
method: ch12-v5-7-four-grahas-angle-trine-benefits
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 长寿富有聪明受王喜爱：上升主或水木金落角宫、三角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子的基本格局怎么样
- 水星木星金星落角宫三角宫代表什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘一宫（Lagn）落在哪个星座

## 按情况检查的事实

- 上升主（Lagn's Lord）是否落角宫
- 上升主（Lagn's Lord）是否落三角宫
- 水星（Budh）是否落角宫
- 水星（Budh）是否落三角宫
- 木星（Guru）是否落角宫
- 木星（Guru）是否落三角宫
- 金星（Shukra）是否落角宫
- 金星（Shukra）是否落三角宫

## 依赖方法

- 无

## 执行步骤

### ch12-v5-7-four-grahas-angle-trine-benefits.step-001

- 动作：逐一核对上升主、水星、木星、金星是否落在角宫或三角宫。
- 适用范围：仅限本命盘一宫（Tanu Bhava）整体利益主题（原文小标题 Other Benefits）；原文把四颗星并列，没有说需要几颗同时成立。
- 原文最小意思：上升主（Lagn Lord）、水星（Budh）、木星（Guru）或金星（Shukra）落角宫或落三角宫时，命主长寿、富有、聪明，并受国王喜爱。
- 本步骤产出事实：["四星落角宫三角宫的综合利益判定"]
- 所需事实：["本盘一宫（Lagn）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘一宫（Lagn）落在哪个星座"}, {"operator": "OR", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落角宫"}, {"fact_key": "上升主（Lagn's Lord）是否落三角宫"}, {"fact_key": "水星（Budh）是否落角宫"}, {"fact_key": "水星（Budh）是否落三角宫"}, {"fact_key": "木星（Guru）是否落角宫"}, {"fact_key": "木星（Guru）是否落三角宫"}, {"fact_key": "金星（Shukra）是否落角宫"}, {"fact_key": "金星（Shukra）是否落三角宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落角宫"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落角宫"}, "selection_group": "ch12-v5-7-four-grahas-angle-trine-benefits.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落角宫。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["上升主（Lagn's Lord）是否落三角宫"], "branch_condition_logic": {"fact_key": "上升主（Lagn's Lord）是否落三角宫"}, "selection_group": "ch12-v5-7-four-grahas-angle-trine-benefits.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：上升主（Lagn's Lord）是否落三角宫。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["水星（Budh）是否落角宫"], "branch_condition_logic": {"fact_key": "水星（Budh）是否落角宫"}, "selection_group": "ch12-v5-7-four-grahas-angle-trine-benefits.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落角宫。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["水星（Budh）是否落三角宫"], "branch_condition_logic": {"fact_key": "水星（Budh）是否落三角宫"}, "selection_group": "ch12-v5-7-four-grahas-angle-trine-benefits.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：水星（Budh）是否落三角宫。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["木星（Guru）是否落角宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落角宫"}, "selection_group": "ch12-v5-7-four-grahas-angle-trine-benefits.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落角宫。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["木星（Guru）是否落三角宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落三角宫"}, "selection_group": "ch12-v5-7-four-grahas-angle-trine-benefits.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落三角宫。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落角宫"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落角宫"}, "selection_group": "ch12-v5-7-four-grahas-angle-trine-benefits.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落角宫。"}, {"when": {"fact_key": "本盘一宫（Lagn）落在哪个星座"}, "required_fact_keys": ["金星（Shukra）是否落三角宫"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落三角宫"}, "selection_group": "ch12-v5-7-four-grahas-angle-trine-benefits.step-001:graha-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落三角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 long lived 换算成具体年数，原文没有给寿数。", "不得据此推断财富数额或官职级别。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘一宫（Lagn）落在哪个星座。
- 缺失即停字段：["本盘一宫（Lagn）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch12:v5-7`｜PDF [26, 27]｜“If Lagn Lord, Budh, Guru, or Shukra be in an angle, or in a trine, the native will be long lived, wealthy, intelligent and liked by the king.”


## 四路查书计划

### 支持路

- If Lagn Lord, Budh, Guru, or Shukra be in an angle, or in a trine, the native will be long lived, wealthy, intelligent and liked by the king
- 上升主水星木星金星落角宫三角宫 长寿富有聪明

### 反例或取消路

- Should Lagn Lord be yuti with a malefic, or be in Randhr, 6th, or 12th, physical felicity will diminish
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless

### 适用边界路

- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Putr and Dharm Bhava are known by the name Kon (or trine). Evil Bhavas, or Dusthan Bhavas are Ari, Randhr and Vyaya Bhava
- The Kendras are known, as Vishnu Sthanas (Bhavas of Lord Vishnu), while the Konas are called Lakshmi Sthanas

### 判断方法路

- Kindly detail methods of ascertaining the life-span of human beings
- Indications of Tanu Bhava. Maharishi Parashar replies. Physique, appearance, intellect (or the organ of intelligence, i.e. brain), complexion of the body, vigour, weakness, happiness, grief and innate nature are all to be guessed through the ascending Rāśi
- 判断整体格局要看四颗星落不落角宫三角宫

## 上游问题

- 无

## 停止条件

- 缺少上升星座事实时停止。
- 八个分支事实全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
