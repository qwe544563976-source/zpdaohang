---
method: ch13-v12-dhan-lord-dusthana-eye-disease
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 眼病或眼部畸形：二宫主落六宫、八宫或十二宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的眼睛会不会有毛病
- 二宫主落六八十二宫对眼睛有什么影响

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘二宫主（Dhan's Lord）落在哪一宫

## 按情况检查的事实

- 二宫主（Dhan's Lord）是否落六宫（Ari）
- 二宫主（Dhan's Lord）是否落八宫（Randhr）
- 二宫主（Dhan's Lord）是否落十二宫（Vyaya）

## 依赖方法

- 无

## 执行步骤

### ch13-v12-dhan-lord-dusthana-eye-disease.step-001

- 动作：取本偈前句所说的那颗行星（二宫主）的落宫，核对它是否落六宫、八宫或十二宫。
- 适用范围：仅限本命盘二宫（Dhan Bhava）眼睛主题；原文 the said Grah 承接本偈前句的 Dhan Lord（二宫主），已绑定该原子。
- 原文最小意思：上一句所说的二宫主落六宫（Ari）、八宫（Randhr）或十二宫（Vyaya）之一时，命主眼睛有病或畸形。
- 本步骤产出事实：["二宫主落六八十二宫的眼病判定"]
- 所需事实：["本盘二宫主（Dhan's Lord）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "二宫主（Dhan's Lord）是否落六宫（Ari）"}, {"fact_key": "二宫主（Dhan's Lord）是否落八宫（Randhr）"}, {"fact_key": "二宫主（Dhan's Lord）是否落十二宫（Vyaya）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落六宫（Ari）"}, "selection_group": "ch13-v12-dhan-lord-dusthana-eye-disease.step-001:dhan-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落六宫（Ari）。"}, {"when": {"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落八宫（Randhr）"}, "selection_group": "ch13-v12-dhan-lord-dusthana-eye-disease.step-001:dhan-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落八宫（Randhr）。"}, {"when": {"fact_key": "本盘二宫主（Dhan's Lord）落在哪一宫"}, "required_fact_keys": ["二宫主（Dhan's Lord）是否落十二宫（Vyaya）"], "branch_condition_logic": {"fact_key": "二宫主（Dhan's Lord）是否落十二宫（Vyaya）"}, "selection_group": "ch13-v12-dhan-lord-dusthana-eye-disease.step-001:dhan-lord-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：二宫主（Dhan's Lord）是否落十二宫（Vyaya）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 the said Grah 当成二宫主以外的行星。", "不得据此推断眼病的种类、程度或发病时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘二宫主（Dhan's Lord）落在哪一宫。
- 缺失即停字段：["本盘二宫主（Dhan's Lord）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v12`｜PDF [28]｜“Should the said Grah be in Ari, Randhr, or Vyaya Bhava, there will be disease, or deformity of eyes.”


## 四路查书计划

### 支持路

- Should the said Grah be in Ari, Randhr, or Vyaya Bhava, there will be disease, or deformity of eyes
- 二宫主落六宫八宫十二宫 眼病 眼部畸形

### 反例或取消路

- If Dhan Lord is endowed with strength, the native will possess beautiful eyes
- One born in Vapi Yog will be capable of accumulating wealth, be endowed with lasting wealth and happiness and sons, be free from eye afflictions
- If Dhum is in Lagna, the native will be valiant, endowed with beautiful eyes

### 适用边界路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- Note the Grahas, that are ruling the Rāśis, occupied by the Lords of Ari, Randhr and Vyaya Bhava. If the said dispositors are in such evil Bhavas in turn and are associated with, or receive a Drishti from malefics, the native will be miserable and indigent
- Head, eyes, ears, nose, temple, chin and face is the order of limbs, denoted (by the various Bhavas), when the first decanate of a Rashiascends

### 判断方法路

- The limb, related to a malefic by occupation, will have ulcers, or scars
- Surya with such lordship and in such a Bhava denotes such affectation of head, Chandra of the face, Mangal of the neck, Budh of the navel, Guru of the nose, Shukra of the eyes
- 判断眼睛问题要看二宫主落在哪一宫

## 上游问题

- 无

## 停止条件

- 缺少二宫主落宫事实时停止。
- 六宫、八宫、十二宫三个分支事实全缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
