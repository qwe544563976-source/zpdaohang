---
method: ch21-v19-21-fame-karm-lord-in-dharm
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 得享名声：十宫主落九宫、上升主落十宫、月亮落五宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会声名远播
- 十宫主落九宫对我意味着什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十宫主（Karm's Lord）是否落九宫（Dharm）
- 上升主（Lagn's Lord）是否落十宫（Karm）
- 月亮（Chandra）是否落五宫（Putr）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch21-v19-21-fame-karm-lord-in-dharm.step-001

- 动作：核对十宫主（Karm's Lord）是否落九宫（Dharm）、上升主（Lagn's Lord）是否落十宫（Karm）、月亮（Chandra）是否落五宫（Putr）。
- 适用范围：仅限本命盘十宫（Karm）名声主题；本条是同偈三组名声组合中的第三组，三个条件同时成立才下断语；原文未给时间限定。
- 原文最小意思：十宫主落九宫、上升主落十宫、月亮落五宫时，命主会有名声。
- 本步骤产出事实：["十宫主落九宫得名声判定"]
- 所需事实：["十宫主（Karm's Lord）是否落九宫（Dharm）", "上升主（Lagn's Lord）是否落十宫（Karm）", "月亮（Chandra）是否落五宫（Putr）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十宫主（Karm's Lord）是否落九宫（Dharm）"}, {"fact_key": "上升主（Lagn's Lord）是否落十宫（Karm）"}, {"fact_key": "月亮（Chandra）是否落五宫（Putr）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断名声的领域、大小或应期。", "不得把三个落宫条件中的任何一个单独当成有名声的判据。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十宫主（Karm's Lord）是否落九宫（Dharm）、上升主（Lagn's Lord）是否落十宫（Karm）、月亮（Chandra）是否落五宫（Putr）。
- 缺失即停字段：["十宫主（Karm's Lord）是否落九宫（Dharm）", "上升主（Lagn's Lord）是否落十宫（Karm）", "月亮（Chandra）是否落五宫（Putr）"]
- 原文证据：
  - `bphs-97:santhanam:ch21:v19-21`｜PDF [39]｜“Fame will come to the native, if Karm’s Lord is in Dharm Bhava, as Lagn’s Lord is in Karm Bhava and Chandra is in Putr Bhava.”


## 四路查书计划

### 支持路

- Fame will come to the native, if Karm’s Lord is in Dharm Bhava, as Lagn’s Lord is in Karm Bhava and Chandra is in Putr Bhava
- 十宫主落九宫 上升主落十宫 月亮落五宫 名声

### 反例或取消路

- If Shani is in Karm Bhava along with a debilitated Grah, while Karm Bhava in the Navāńś Kundali is occupied by a malefic, the native will be bereft of acts
- Should Rahu, Surya, Shani and Mangal be in Labh Bhava, the native will incur cessation of his duties

### 适用边界路

- If Karm’s Lord is in Dharm Bhava, one born of royal scion will become a king, whereas an ordinary native will be equal to a king
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava

### 判断方法路

- Prosperity, or Annihilation of a Bhava. Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic
- 判断名声应检查十宫主落在哪一宫

## 上游问题

- 无

## 停止条件

- 缺少十宫主落宫事实时停止。
- 缺少上升主落宫事实时停止。
- 缺少月亮落宫事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
