---
method: ch36-v3-4-gaj-kesari-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Gaj Kesari Yog：木星落上升或月亮起的角宫，与吉星同宫或受吉星相照，且不落陷、不燃烧、不在敌方星座

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我这辈子有没有名望和财富
- 我命里木星的组合好不好

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否落陷
- 木星（Guru）是否燃烧
- 木星（Guru）是否落敌方行星主管的星座

## 按情况检查的事实

- 木星（Guru）是否落从上升宫（Lagna）起算的角宫
- 木星（Guru）是否落从月亮（Chandra）起算的角宫
- 木星（Guru）是否与吉星同宫
- 木星（Guru）是否被吉星相照

## 依赖方法

- 无

## 执行步骤

### ch36-v3-4-gaj-kesari-yog.step-001

- 动作：先核对木星（Guru）是否避开了落陷、燃烧与敌方星座，再核对它是否落上升宫（Lagna）起或月亮（Chandra）起的角宫，并与吉星同宫或受吉星相照，判定 Gaj Kesari Yog 是否成立。
- 适用范围：仅限本命盘 Gaj Kesari Yog 的成立判定；原文本句未给出吉星的判准，也没有时间限定。
- 原文最小意思：木星（Guru）落上升宫（Lagna）起的角宫，或落月亮（Chandra）起的角宫，并与吉星同宫或受吉星相照，同时避开落陷、燃烧与敌方星座（inimical Rāśi），则 Gaj Kesari Yog 成立。
- 本步骤产出事实：["Gaj Kesari Yog 成立判定"]
- 所需事实：["木星（Guru）是否落陷", "木星（Guru）是否燃烧", "木星（Guru）是否落敌方行星主管的星座"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否落陷"}]}, {"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否燃烧"}]}, {"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否落敌方行星主管的星座"}]}]}, {"operator": "OR", "operands": [{"fact_key": "木星（Guru）是否落从上升宫（Lagna）起算的角宫"}, {"fact_key": "木星（Guru）是否落从月亮（Chandra）起算的角宫"}]}, {"operator": "OR", "operands": [{"fact_key": "木星（Guru）是否与吉星同宫"}, {"fact_key": "木星（Guru）是否被吉星相照"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否落陷"}]}, {"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否燃烧"}]}, {"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否落敌方行星主管的星座"}]}]}, "required_fact_keys": ["木星（Guru）是否落从上升宫（Lagna）起算的角宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落从上升宫（Lagna）起算的角宫"}, "selection_group": "ch36-v3-4-gaj-kesari-yog.step-001:kendra-reference", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落从上升宫（Lagna）起算的角宫。"}, {"when": {"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否落陷"}]}, {"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否燃烧"}]}, {"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否落敌方行星主管的星座"}]}]}, "required_fact_keys": ["木星（Guru）是否落从月亮（Chandra）起算的角宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否落从月亮（Chandra）起算的角宫"}, "selection_group": "ch36-v3-4-gaj-kesari-yog.step-001:kendra-reference", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否落从月亮（Chandra）起算的角宫。"}, {"when": {"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否落陷"}]}, {"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否燃烧"}]}, {"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否落敌方行星主管的星座"}]}]}, "required_fact_keys": ["木星（Guru）是否与吉星同宫"], "branch_condition_logic": {"fact_key": "木星（Guru）是否与吉星同宫"}, "selection_group": "ch36-v3-4-gaj-kesari-yog.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否与吉星同宫。"}, {"when": {"operator": "AND", "operands": [{"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否落陷"}]}, {"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否燃烧"}]}, {"operator": "NOT", "operands": [{"fact_key": "木星（Guru）是否落敌方行星主管的星座"}]}]}, "required_fact_keys": ["木星（Guru）是否被吉星相照"], "branch_condition_logic": {"fact_key": "木星（Guru）是否被吉星相照"}, "selection_group": "ch36-v3-4-gaj-kesari-yog.step-001:benefic-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：木星（Guru）是否被吉星相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断具体官职、财富数额或应期。", "原文本句把角宫的起算点限定为上升宫（Lagna）与月亮（Chandra）两处，不得改从别的行星或宫位起算。", "原文本句未给出吉星判准，不得自行指定哪几颗行星算吉星。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落陷、木星（Guru）是否燃烧、木星（Guru）是否落敌方行星主管的星座。
- 缺失即停字段：["木星（Guru）是否落陷", "木星（Guru）是否燃烧", "木星（Guru）是否落敌方行星主管的星座"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v3-4`｜PDF [79]｜“Should Guru be in a Kendr from Lagna, or from Chandra and be yuti with, or receiving a Drishti from benefic, avoiding at the same time debilitation, combustion and inimical Rāśi, Gaj Kesari Yog is caused.”

### ch36-v3-4-gaj-kesari-yog.step-002

- 动作：在 Gaj Kesari Yog 成立时读取命主的光彩、财富与才智断语。
- 适用范围：仅限已判定 Gaj Kesari Yog 成立的本命盘；原文未给时间限定。
- 原文最小意思：生于 Gaj Kesari Yog 者光彩照人、富有、聪慧、具备许多值得称道的德行，并会取悦国王。
- 本步骤产出事实：["Gaj Kesari Yog 效果断语"]
- 所需事实：["Gaj Kesari Yog 成立判定"]
- 条件关系：{"fact_key": "Gaj Kesari Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「取悦国王」推广成一定得到官职、封赏或某个具体职位。", "不得据此推断寿命、婚姻或子女。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Gaj Kesari Yog 成立判定。
- 缺失即停字段：["Gaj Kesari Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v3-4`｜PDF [79]｜“One born in Gaj Kesari Yog will be splendourous, wealthy, intelligent, endowed with many laudable virtues and will please the king.”


## 四路查书计划

### 支持路

- Should Guru be in a Kendr from Lagna, or from Chandra and be yuti with, or receiving a Drishti from benefic
- One born in Gaj Kesari Yog will be splendourous, wealthy, intelligent, endowed with many laudable virtues and will please the king
- 木星落角宫 与吉星同宫 Gaj Kesari Yog

### 反例或取消路

- Excluding Surya, should there be no Grah with Chandra, or in the 2nd and/or 12th from Chandra, or in a Kendr from Lagna, Kema Drum Yog is formed
- If Guru is in his debilitation Rāśi, combust, associated with malefics, or in Ari, or Randhr
- 木星落陷 燃烧 恶果

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu
- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula

### 判断方法路

- Evaluation of the Drishtis of the Grahas. Deduct the longitude of the Grah (or Bhava), that receives a Drishti, from that of the Grah, which gives the Drishti
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少木星落陷、燃烧或敌方星座任一项事实时停止。
- 木星在上升宫起与月亮起两种角宫的落宫事实都缺失时停止。
- 木星与吉星同宫、被吉星相照两项事实都缺失时停止。
- 原文本句未给出吉星判准，吉星名册未取得时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
