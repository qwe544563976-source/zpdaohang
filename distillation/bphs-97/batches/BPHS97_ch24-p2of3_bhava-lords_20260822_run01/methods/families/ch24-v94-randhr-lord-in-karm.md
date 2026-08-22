---
method: ch24-v94-randhr-lord-in-karm
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 八宫主落十宫：父亲方面没有福分、搬弄是非、生计无着

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我和父亲之间的福分怎么样
- 我为什么一直找不到稳定生计

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫主（Randhr's Lord）是否落十宫（Karm）

## 按情况检查的事实

- 原文未指明相照对象的吉星相照（benefic Drishti）是否存在

## 依赖方法

- 无

## 执行步骤

### ch24-v94-randhr-lord-in-karm.step-001

- 动作：核对八宫主（Randhr's Lord）是否落十宫（Karm Bhava），据此判断本人在父亲、言语与生计方面的处境；同偈另给了吉星相照的缓解句，作为例外关系一并登记。
- 适用范围：仅限本命盘八宫主落十宫（Karm Bhava）一条；原文随后写「若过程中有来自吉星的相照，这些恶果就不会成熟」，但未指明该相照的对象是八宫主还是十宫，该缓解条件未确定即停判；本段原文自标「Effects of Randhr’s Lord in Various Bhavas (up to Sloka 96)」；原文未给时间限定。
- 原文最小意思：八宫主（Randhr's Lord）落十宫（Karm Bhava）时，本人在父亲方面没有福分，搬弄是非，且生计无着。
- 本步骤产出事实：["八宫主落十宫的父亲福分与生计判定"]
- 所需事实：["八宫主（Randhr's Lord）是否落十宫（Karm）"]
- 条件关系：{"fact_key": "八宫主（Randhr's Lord）是否落十宫（Karm）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[{"type": "mitigation", "evidence_atom_ids": ["bphs-97:santhanam:ch24:v94"], "condition_logic": {"fact_key": "原文未指明相照对象的吉星相照（benefic Drishti）是否存在"}}]
- 禁止扩大：["不得把「吉星相照」默认绑定到八宫主一方或十宫一方——原文未指明相照对象。", "不得把「没有福分」写成父亲去世或父子断绝等原文没有的情节。", "不得据此推断失业的时间、行业或收入。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否落十宫（Karm）。
- 缺失即停字段：["八宫主（Randhr's Lord）是否落十宫（Karm）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v94`｜PDF [47]｜“If Randhr’s Lord is in Karm Bhava, the native will be devoid of paternal bliss, be a talebearer and be bereft of livelihood. If there is a Drishti in the process from a benefic, then these evils will not mature.”


## 四路查书计划

### 支持路

- If Randhr’s Lord is in Karm Bhava, the native will be devoid of paternal bliss, be a talebearer
- 八宫主落十宫 父亲无福 生计无着

### 反例或取消路

- If there is a Drishti in the process from a benefic, then these evils will not mature
- If Karm’s Lord is strong and in exaltation, or in its own Rāśi/Navāńś, the native will derive extreme paternal happiness, will enjoy fame and will perform good deeds

### 适用边界路

- Indications of Randhr Bhava. Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead and things, that have happened and are to happen
- Indications of Karm Bhava. Royalty (authority), place, profession (livelihood), honour, father, living in foreign lands and debts are to be understood from Karm Bhava
- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics

### 判断方法路

- Effects of Randhr’s Lord in Various Bhavas
- Effects of Karm’s Lord in Various Bhavas

## 上游问题

- 无

## 停止条件

- 缺少八宫主是否落十宫的事实时停止。
- 原文未指明吉星相照的对象是八宫主还是十宫，该缓解事实未确定即停止。
- 吉星名册未确定时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
