---
method: ch35-v9-11-hal-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Hal Yog：所有行星都落在二六十宫、三七十一宫或四八十二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我盘上行星是不是都在同一组三宫里
- 我命里有没有 Hal Yog

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘所有行星（Grahas）分别落在哪一宫（Bhava）

## 按情况检查的事实

- 本盘所有行星（Grahas）是否都落在二宫（Dhan）、六宫（Ari）与十宫（Karm Bhava）内
- 本盘所有行星（Grahas）是否都落在三宫（Sahaj）、七宫（Yuvati）与十一宫（Labh Bhava）内
- 本盘所有行星（Grahas）是否都落在四宫（Bandhu）、八宫（Randhr）与十二宫（Vyaya Bhava）内

## 依赖方法

- 无

## 执行步骤

### ch35-v9-11-hal-yog.step-001

- 动作：核对本盘行星（Grahas）的分布，判定 Hal Yog 是否成立。
- 适用范围：仅限本命盘 Hal Yog 的成立判定；原文只给盘面分布条件，没有时间、上升或男女限定。
- 原文最小意思：本盘所有行星（Grahas）都落在二宫（Dhan）、六宫（Ari）与十宫（Karm Bhava）内，或都落在三宫（Sahaj）、七宫（Yuvati）与十一宫（Labh Bhava）内，或都落在四宫（Bandhu）、八宫（Randhr）与十二宫（Vyaya Bhava）内时，构成 Hal Yog。
- 本步骤产出事实：["Hal Yog 成立判定"]
- 所需事实：["本盘所有行星（Grahas）分别落在哪一宫（Bhava）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘所有行星（Grahas）分别落在哪一宫（Bhava）"}, {"operator": "OR", "operands": [{"fact_key": "本盘所有行星（Grahas）是否都落在二宫（Dhan）、六宫（Ari）与十宫（Karm Bhava）内"}, {"fact_key": "本盘所有行星（Grahas）是否都落在三宫（Sahaj）、七宫（Yuvati）与十一宫（Labh Bhava）内"}, {"fact_key": "本盘所有行星（Grahas）是否都落在四宫（Bandhu）、八宫（Randhr）与十二宫（Vyaya Bhava）内"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘所有行星（Grahas）分别落在哪一宫（Bhava）"}, "required_fact_keys": ["本盘所有行星（Grahas）是否都落在二宫（Dhan）、六宫（Ari）与十宫（Karm Bhava）内"], "branch_condition_logic": {"fact_key": "本盘所有行星（Grahas）是否都落在二宫（Dhan）、六宫（Ari）与十宫（Karm Bhava）内"}, "selection_group": "ch35-v9-11-hal-yog.step-001:hal-triads", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘所有行星（Grahas）是否都落在二宫（Dhan）、六宫（Ari）与十宫（Karm Bhava）内。"}, {"when": {"fact_key": "本盘所有行星（Grahas）分别落在哪一宫（Bhava）"}, "required_fact_keys": ["本盘所有行星（Grahas）是否都落在三宫（Sahaj）、七宫（Yuvati）与十一宫（Labh Bhava）内"], "branch_condition_logic": {"fact_key": "本盘所有行星（Grahas）是否都落在三宫（Sahaj）、七宫（Yuvati）与十一宫（Labh Bhava）内"}, "selection_group": "ch35-v9-11-hal-yog.step-001:hal-triads", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘所有行星（Grahas）是否都落在三宫（Sahaj）、七宫（Yuvati）与十一宫（Labh Bhava）内。"}, {"when": {"fact_key": "本盘所有行星（Grahas）分别落在哪一宫（Bhava）"}, "required_fact_keys": ["本盘所有行星（Grahas）是否都落在四宫（Bandhu）、八宫（Randhr）与十二宫（Vyaya Bhava）内"], "branch_condition_logic": {"fact_key": "本盘所有行星（Grahas）是否都落在四宫（Bandhu）、八宫（Randhr）与十二宫（Vyaya Bhava）内"}, "selection_group": "ch35-v9-11-hal-yog.step-001:hal-triads", "stop_condition": "选中该分支后，缺少以下事实即停止：本盘所有行星（Grahas）是否都落在四宫（Bandhu）、八宫（Randhr）与十二宫（Vyaya Bhava）内。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["三组宫位是原文并列的三种成立方式，不得互相拼接成新的组合。", "不得把「所有行星」放宽成「多数行星」。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘所有行星（Grahas）分别落在哪一宫（Bhava）。
- 缺失即停字段：["本盘所有行星（Grahas）分别落在哪一宫（Bhava）"]
- 原文证据：
  - `bphs-97:santhanam:ch35:v9-11`｜PDF [76]｜“while all Grahas in Dhan, Ari and Karm Bhava, or in Sahaj, Yuvati and Labh Bhava, or in Bandhu, Randhr and Vyaya Bhava cause Hal Yog”


## 四路查书计划

### 支持路

- while all Grahas in Dhan, Ari and Karm Bhava, or in Sahaj, Yuvati and Labh Bhava, or in Bandhu, Randhr and Vyaya Bhava cause Hal Yog
- Hal Yog 的成立条件

### 反例或取消路

- 无

### 适用边界路

- O excellent of the Brahmins, explained below are 32 Nabhash Yogas, which have a total of 1800 different varieties.
- These consist of 3 Asraya Yogas, 2 Dala Yogas, 20 Akriti Yogas and 7 Sankhya Yogas.
- Nabhash 瑜伽全章的总数与分类边界

### 判断方法路

- Names of Nabhash Yogas. The 3 Asraya Yogas are Rajju, Musala and Nala Yogas.
- Effects of Nabhash Yogas (up to Sloka 50).
- 怎么按 Nabhash 瑜伽的分类去查一张盘

## 上游问题

- 无

## 停止条件

- 缺少判定 Hal Yog 所需的行星分布事实时停止。
- 行星分布事实取不到确定值时停止，不得凭部分行星推定 Hal Yog 成立。
- 三组宫位的占据事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
