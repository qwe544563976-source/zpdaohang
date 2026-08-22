---
method: ch03-v59-60-auspicious-effect-ratio
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 吉效比例：入旺、Mooltrikon、own Bhava、友座、均等者座、落陷或敌座各给多少吉效

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 这颗行星能给出多少吉效
- 入旺和落本座给的吉效差多少

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 该行星（Grah）是否入旺
- 该行星（Grah）是否落其 Mooltrikon
- 该行星（Grah）是否落原文所称的 own Bhava
- 该行星（Grah）是否落友星的星座（friendly Rāśi）
- 该行星（Grah）是否落均等者的星座（equal’s Rāśi）
- 本盘该行星（Grah）落在哪个星座

## 按情况检查的事实

- 该行星（Grah）是否落陷
- 该行星（Grah）是否落敌星的营地（enemy’s camp）

## 依赖方法

- 无

## 执行步骤

### ch03-v59-60-auspicious-effect-ratio.step-001

- 动作：查该行星是否入旺，据以定其吉效比例。
- 适用范围：第3章吉效比例条；本条只折算吉效，凶效另由本偈末句处理。
- 原文最小意思：行星（Grah）入旺时，给出完全的吉效。
- 本步骤产出事实：["入旺吉效比例判定"]
- 所需事实：["该行星（Grah）是否入旺"]
- 条件关系：{"fact_key": "该行星（Grah）是否入旺"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「完全的吉效」读成具体分值——本偈只给比例关系。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：该行星（Grah）是否入旺。
- 缺失即停字段：["该行星（Grah）是否入旺"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v59-60`｜PDF [12]｜“A Grah in exaltation gives fully good effects”

### ch03-v59-60-auspicious-effect-ratio.step-002

- 动作：查该行星是否落其 Mooltrikon，据以定其吉效比例。
- 适用范围：第3章吉效比例条；本条只折算吉效，凶效另由本偈末句处理。
- 原文最小意思：落其 Mooltrikon 时，吉效减去四分之一（one fourth）。
- 本步骤产出事实：["Mooltrikon 吉效比例判定"]
- 所需事实：["该行星（Grah）是否落其 Mooltrikon"]
- 条件关系：{"fact_key": "该行星（Grah）是否落其 Mooltrikon"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「减去四分之一」换算成本偈没有给的分值。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：该行星（Grah）是否落其 Mooltrikon。
- 缺失即停字段：["该行星（Grah）是否落其 Mooltrikon"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v59-60`｜PDF [12]｜“while in Mooltrikon it is bereft of its auspicious effects by one fourth”

### ch03-v59-60-auspicious-effect-ratio.step-003

- 动作：查该行星是否落原文所称的 own Bhava，据以定其吉效比例。
- 适用范围：第3章吉效比例条；原文此处用语为 own Bhava，本偈没有界定它与星座（Rāśi）、宫（Bhava）的对应，故照原文保留。
- 原文最小意思：落其 own Bhava 时，吉效减半。
- 本步骤产出事实：["own Bhava 吉效比例判定"]
- 所需事实：["该行星（Grah）是否落原文所称的 own Bhava"]
- 条件关系：{"fact_key": "该行星（Grah）是否落原文所称的 own Bhava"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 own Bhava 读成宫位落点——原文在这一列里与入旺、Mooltrikon、友座并列。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：该行星（Grah）是否落原文所称的 own Bhava。
- 缺失即停字段：["该行星（Grah）是否落原文所称的 own Bhava"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v59-60`｜PDF [12]｜“It is half beneficial in its own Bhava.”

### ch03-v59-60-auspicious-effect-ratio.step-004

- 动作：查该行星是否落友星的星座，据以定其吉效比例。
- 适用范围：第3章吉效比例条；友星由本书自然关系与合成关系条另行界定。
- 原文最小意思：落友星的星座（friendly Rāśi）时，吉效为四分之一（one fourth）。
- 本步骤产出事实：["友座吉效比例判定"]
- 所需事实：["该行星（Grah）是否落友星的星座（friendly Rāśi）"]
- 条件关系：{"fact_key": "该行星（Grah）是否落友星的星座（friendly Rāśi）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条自行判定谁是友星——友星另由自然关系与合成关系条界定。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：该行星（Grah）是否落友星的星座（friendly Rāśi）。
- 缺失即停字段：["该行星（Grah）是否落友星的星座（friendly Rāśi）"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v59-60`｜PDF [12]｜“Its beneficence is one fourth in a friendly Rāśi.”

### ch03-v59-60-auspicious-effect-ratio.step-005

- 动作：查该行星是否落均等者的星座，据以定其吉效比例。
- 适用范围：第3章吉效比例条；均等者由本书自然关系与合成关系条另行界定。
- 原文最小意思：落均等者的星座（equal’s Rāśi）时，只有八分之一（one eighth）的吉性可用。
- 本步骤产出事实：["均等者座吉效比例判定"]
- 所需事实：["该行星（Grah）是否落均等者的星座（equal’s Rāśi）"]
- 条件关系：{"fact_key": "该行星（Grah）是否落均等者的星座（equal’s Rāśi）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条自行判定谁是均等者——它另由自然关系与合成关系条界定。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：该行星（Grah）是否落均等者的星座（equal’s Rāśi）。
- 缺失即停字段：["该行星（Grah）是否落均等者的星座（equal’s Rāśi）"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v59-60`｜PDF [12]｜“In an equal’s Rashione eighth of auspicious disposition is useful.”

### ch03-v59-60-auspicious-effect-ratio.step-006

- 动作：查该行星是落陷还是落敌星的营地，据以判定吉效为零。
- 适用范围：第3章吉效比例条；本条只折算吉效，凶效另由本偈末句处理。
- 原文最小意思：落陷，或落敌星的营地（enemy’s camp），吉效为零。
- 本步骤产出事实：["落陷与敌座吉效为零判定"]
- 所需事实：["本盘该行星（Grah）落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘该行星（Grah）落在哪个星座"}, {"operator": "OR", "operands": [{"fact_key": "该行星（Grah）是否落陷"}, {"fact_key": "该行星（Grah）是否落敌星的营地（enemy’s camp）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘该行星（Grah）落在哪个星座"}, "required_fact_keys": ["该行星（Grah）是否落陷"], "branch_condition_logic": {"fact_key": "该行星（Grah）是否落陷"}, "selection_group": "ch03-v59-60-auspicious-effect-ratio.step-006:nil-good-effect-source", "stop_condition": "选中该分支后，缺少以下事实即停止：该行星（Grah）是否落陷。"}, {"when": {"fact_key": "本盘该行星（Grah）落在哪个星座"}, "required_fact_keys": ["该行星（Grah）是否落敌星的营地（enemy’s camp）"], "branch_condition_logic": {"fact_key": "该行星（Grah）是否落敌星的营地（enemy’s camp）"}, "selection_group": "ch03-v59-60-auspicious-effect-ratio.step-006:nil-good-effect-source", "stop_condition": "选中该分支后，缺少以下事实即停止：该行星（Grah）是否落敌星的营地（enemy’s camp）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「吉效为零」读成一定出凶果——本句只说吉效。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘该行星（Grah）落在哪个星座。
- 缺失即停字段：["本盘该行星（Grah）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v59-60`｜PDF [12]｜“The good effects are nil in debilitation, or enemy’s camp.”


## 四路查书计划

### 支持路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Its beneficence is one fourth in a friendly Rāśi. In an equal’s Rashione eighth of auspicious disposition is useful
- 吉效比例 入旺 Mooltrikon 友座 落陷

### 反例或取消路

- Inauspicious effects are quite reverse with reference to what is stated
- 同一偈末句给的凶效方向相反

### 适用边界路

- 60, 45, 30, 22, 15, 8, 4, 2 and 0 are the Subhankas (Subha Griha Pankthis, benefic points), due to a Grah’s placement, respectively, in exaltation, Mooltrikon, own, great friend’s, friend’s, neutral, enemy’s, great enemy’s and debilitation Rāśi
- 另一处把尊贵分成九档并给分值

### 判断方法路

- In this case Surya, being exalted, or in a friendly Rāśi, is not a malefic. He is a malefic, if in debilitation, or in an enemy’s Rāśi
- The Grahas ruling such Rāśis are its friends, apart from the Lord of its exaltation Rāśi
- 尊贵状态怎么落到具体断语上 友星与均等者怎么定

## 上游问题

- 无

## 停止条件

- 缺少该行星尊贵状态的事实时，对应那一步停止。
- 原文没有界定 own Bhava 与星座、宫的对应，需要把它映射成排盘取值时停判。
- 本条只给吉效比例，没有给具体分值，要量化必须另查原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
