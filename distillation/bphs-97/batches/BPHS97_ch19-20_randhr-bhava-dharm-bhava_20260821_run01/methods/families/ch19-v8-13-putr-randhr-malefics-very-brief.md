---
method: ch19-v8-13-putr-randhr-malefics-very-brief
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 寿数极短：五宫、八宫与八宫主都与凶星会合

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 五宫八宫都有凶星寿命会怎样
- 八宫主与凶星同宫严不严重

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫（Putr）是否被凶星占据
- 八宫（Randhr）是否被凶星占据
- 八宫主（Randhr's Lord）是否与凶星同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch19-v8-13-putr-randhr-malefics-very-brief.step-001

- 动作：核对五宫（Putr）、八宫（Randhr）与八宫主（Randhr's Lord）是否都与凶星会合。
- 适用范围：仅限本命盘寿命主题；原文只说寿数极短，未给具体年岁或时间。
- 原文最小意思：五宫、八宫与八宫主都与凶星会合时，寿数极短。
- 本步骤产出事实：["五宫八宫及八宫主皆会凶星的极短寿判定"]
- 所需事实：["五宫（Putr）是否被凶星占据", "八宫（Randhr）是否被凶星占据", "八宫主（Randhr's Lord）是否与凶星同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "五宫（Putr）是否被凶星占据"}, {"fact_key": "八宫（Randhr）是否被凶星占据"}, {"fact_key": "八宫主（Randhr's Lord）是否与凶星同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「寿数极短」折算成具体年岁。", "不得只凭三项中的一两项成立就下断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫（Putr）是否被凶星占据、八宫（Randhr）是否被凶星占据、八宫主（Randhr's Lord）是否与凶星同宫。
- 缺失即停字段：["五宫（Putr）是否被凶星占据", "八宫（Randhr）是否被凶星占据", "八宫主（Randhr's Lord）是否与凶星同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch19:v8-13`｜PDF [36]｜“If Putr and Randhr Bhava and Randhr’s Lord are all conjunct malefics, the life span will be very brief.”


## 四路查书计划

### 支持路

- If Putr and Randhr Bhava and Randhr’s Lord are all conjunct malefics, the life span will be very brief
- 五宫 八宫 八宫主 皆与凶星 寿数极短

### 反例或取消路

- If the Lords of Putr, Randhr and Tanu Bhava are in own Navāńśas, own Rāśis, or in friendly Rāśis, the native will enjoy a long span of life
- a single, but strong Guru in Lagn will ward off all the evils

### 适用边界路

- Evils, causing premature end, exist up to the 24th year of one’s age. As such, no definite calculation of life span should be made till such year of age
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu … are malefics, while the rest are benefics
- The life-span in Bal Risht is 8 years, in Yog Risht 20 years, in short, medium and long lives, respectively, 32, 64 and 120 years

### 判断方法路

- Other Clues to Longevity This is based on the positions of Lagn’s Lord, Randhr’s Lord, Shani, Chandra, natal Lagn and Hora Lagn
- The strength and weakness of the Grahas concerned be estimated in deciding longevity
- 多宫同时会凶星怎么判寿命

## 上游问题

- 无

## 停止条件

- 缺少五宫、八宫或八宫主的凶星事实时停止。
- 凶星名册未定时停止（判准见第3章 v11）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
