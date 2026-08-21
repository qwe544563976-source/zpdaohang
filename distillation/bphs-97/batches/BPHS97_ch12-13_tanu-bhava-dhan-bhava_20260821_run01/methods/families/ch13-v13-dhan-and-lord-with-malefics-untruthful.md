---
method: ch13-v13-dhan-and-lord-with-malefics-untruthful
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 搬弄是非说谎并患风病：二宫内有凶星且二宫主与凶星同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我说话是不是容易惹麻烦
- 二宫和二宫主受凶星影响会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 二宫（Dhan）是否被凶星占据
- 二宫主（Dhan's Lord）是否与凶星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch13-v13-dhan-and-lord-with-malefics-untruthful.step-001

- 动作：核对二宫（Dhan Bhava）内是否有凶星，并核对二宫主是否与凶星同宫。
- 适用范围：仅限本命盘二宫（Dhan Bhava）主题；原文要求二宫与二宫主两侧同时与凶星相处，未给时间限定。
- 原文最小意思：二宫（Dhan Bhava）内有凶星、二宫主也与凶星同宫时，命主搬弄是非、说谎，并受风病（windy diseases）之苦。
- 本步骤产出事实：["二宫与二宫主受凶星的言语与风病判定"]
- 所需事实：["二宫（Dhan）是否被凶星占据", "二宫主（Dhan's Lord）是否与凶星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "二宫（Dhan）是否被凶星占据"}, {"fact_key": "二宫主（Dhan's Lord）是否与凶星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得只凭二宫有凶星、或只凭二宫主与凶星同宫其中一侧就下断语。", "不得据此推断风病的具体病名或发病时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：二宫（Dhan）是否被凶星占据、二宫主（Dhan's Lord）是否与凶星同宫。
- 缺失即停字段：["二宫（Dhan）是否被凶星占据", "二宫主（Dhan's Lord）是否与凶星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch13:v13`｜PDF [28]｜“If Dhan Bhava and its Lord are yuti with malefics, the native will be a talebearer, will speak untruth and will be afflicted by windy diseases.”


## 四路查书计划

### 支持路

- If Dhan Bhava and its Lord are yuti with malefics, the native will be a talebearer, will speak untruth and will be afflicted by windy diseases
- 二宫有凶星 二宫主与凶星同宫 搬弄是非 说谎 风病

### 反例或取消路

- If Dhan’s Lord is in own Rāśi, or is exalted, the native will look after his people, will help others and also will become famous
- A benefic in Dhan will give wealth, while a malefic instead will destroy wealth
- If Karm’s Lord is in Sahaj Bhava, the native will enjoy happiness from brothers and servants, be valorous, virtuous, eloquent and truthful

### 适用边界路

- Indications of Dhan Bhava. Wealth, grains (food etc.), family, death, enemies, metals, precious stones etc. are to be understood through Dhan Bhava
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- if Vyaya and Dhan Bhava are occupied by malefics and devoid of a Drishti from a benefic, or of Yuti with a benefic, the native will be shortlived

### 判断方法路

- Similarly Shukra will cause diseases through females, Shani windy diseases, Rahu danger through low-caste-men and Ketu navel diseases
- If the Lord of Dhan is in Dhan, or is in an angle, or in trine, he will promote one’s wealth (or monetary state)
- 判断言语与风病要看二宫和二宫主与凶星的关系

## 上游问题

- 无

## 停止条件

- 缺少二宫是否被凶星占据的事实时停止。
- 缺少二宫主是否与凶星同宫的事实时停止。
- 凶星名册未定时停止（吉凶判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
