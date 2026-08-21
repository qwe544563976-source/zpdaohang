---
method: ch21-v16-bereft-of-acts
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 没有作为：土星与落陷行星同落十宫、九分盘十宫又被凶星占据

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会一事无成
- 土星落十宫对我的事业意味着什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 土星（Shani）是否落十宫（Karm）
- 土星（Shani）是否与另一颗落陷行星同落十宫（Karm）
- 十宫（Karm）在九分盘（Navamsa D9）中是否被凶星占据

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v16-bereft-of-acts.step-001

- 动作：核对本盘十宫（Karm）内是否土星（Shani）与落陷行星同处，并核对九分盘（Navamsa D9）的十宫是否被凶星占据。
- 适用范围：仅限本命盘十宫（Karm）作为主题；原文三个条件同时成立才下断语，其中第三条明写在九分盘（Navāńś Kundali）上；原文未给时间限定，也未给凶星判准，凶星名册按本书自身的定义取。
- 原文最小意思：土星落十宫、十宫内另有落陷行星、且九分盘十宫被凶星占据时，命主没有作为。
- 本步骤产出事实：["土星与落陷星同落十宫没有作为判定"]
- 所需事实：["土星（Shani）是否落十宫（Karm）", "土星（Shani）是否与另一颗落陷行星同落十宫（Karm）", "十宫（Karm）在九分盘（Navamsa D9）中是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星（Shani）是否落十宫（Karm）"}, {"fact_key": "土星（Shani）是否与另一颗落陷行星同落十宫（Karm）"}, {"fact_key": "十宫（Karm）在九分盘（Navamsa D9）中是否被凶星占据"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断失业时间、职业种类或寿命。", "不得只凭本命盘十宫的两个条件成立、而不核九分盘（Navamsa D9）就下断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星（Shani）是否落十宫（Karm）、土星（Shani）是否与另一颗落陷行星同落十宫（Karm）、十宫（Karm）在九分盘（Navamsa D9）中是否被凶星占据。
- 缺失即停字段：["土星（Shani）是否落十宫（Karm）", "土星（Shani）是否与另一颗落陷行星同落十宫（Karm）", "十宫（Karm）在九分盘（Navamsa D9）中是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v16`｜PDF [39]｜“If Shani is in Karm Bhava along with a debilitated Grah, while Karm Bhava in the Navāńś Kundali is occupied by a malefic, the native will be bereft of acts.”


## 四路查书计划

### 支持路

- If Shani is in Karm Bhava along with a debilitated Grah, while Karm Bhava in the Navāńś Kundali is occupied by a malefic, the native will be bereft of acts
- 土星落十宫 落陷行星同宫 九分盘十宫 凶星占据 没有作为

### 反例或取消路

- If the Karm’s Lord is exalted in an angle, or a trine and is yuti with Guru, or receives a Drishti from Guru, one will be endowed with deeds
- If Karm’s Lord is strong and in exaltation, or in its own Rāśi/Navāńś, the native will derive extreme paternal happiness, will enjoy fame and will perform good deeds

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava

### 判断方法路

- Prosperity, or Annihilation of a Bhava. Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic
- 判断十宫（Karm）作为时应否核对九分盘（Navamsa D9）的同一宫

## 上游问题

- 无

## 停止条件

- 缺少土星落宫事实时停止。
- 缺少「土星是否与另一颗落陷行星同落十宫」的事实时停止。
- 缺少九分盘（Navamsa D9）十宫占据者事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
