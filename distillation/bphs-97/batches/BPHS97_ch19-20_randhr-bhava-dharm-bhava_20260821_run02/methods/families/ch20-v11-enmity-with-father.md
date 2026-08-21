---
method: ch20-v11-enmity-with-father
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 父子互相为敌且父亲性情卑劣：上升主落九宫并与六宫主同宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我和父亲会不会不和
- 上升主落九宫又与六宫主同宫说明什么

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 上升主（Lagn's Lord）是否落九宫（Dharm）
- 上升主（Lagn's Lord）是否与六宫主（Ari's Lord）同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch20-v11-enmity-with-father.step-001

- 动作：核对上升主（Lagn's Lord）是否落九宫（Dharm），并核对它是否与六宫主（Ari's Lord）同宫。
- 适用范围：仅限本命盘九宫（Dharm）父亲主题；原文第二句以「Further」承接同偈前句，共用同一组条件；原文未给时间或上升限定。
- 原文最小意思：上升主（Lagn's Lord）落九宫（Dharm）、且与六宫主（Ari's Lord）同宫时，父亲与命主之间互相为敌，命主的父亲性情卑劣。
- 本步骤产出事实：["上升主落九宫会六宫主主父子为敌且父性情卑劣判定"]
- 所需事实：["上升主（Lagn's Lord）是否落九宫（Dharm）", "上升主（Lagn's Lord）是否与六宫主（Ari's Lord）同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "上升主（Lagn's Lord）是否落九宫（Dharm）"}, {"fact_key": "上升主（Lagn's Lord）是否与六宫主（Ari's Lord）同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断父亲的寿命或财产纠纷。", "不得把「互相为敌」加重成断绝关系或诉讼。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：上升主（Lagn's Lord）是否落九宫（Dharm）、上升主（Lagn's Lord）是否与六宫主（Ari's Lord）同宫。
- 缺失即停字段：["上升主（Lagn's Lord）是否落九宫（Dharm）", "上升主（Lagn's Lord）是否与六宫主（Ari's Lord）同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch20:v11`｜PDF [37]｜“There will be mutual enmity between the father and the native, if Lagn’s Lord is in Dharm Bhava, but with the Lord of Ari. Further, the native’s father will be of contemptible disposition.”


## 四路查书计划

### 支持路

- There will be mutual enmity between the father and the native, if Lagn’s Lord is in Dharm Bhava, but with the Lord of Ari.
- 上升主落九宫 与六宫主同宫 父子为敌 父亲性情卑劣

### 反例或取消路

- Should Surya be in deep exaltation, as Dharm’s Lord is in Labh Bhava, the native will be virtuous, dear to the king and devoted to father
- If Karm’s Lord is in Dhan Bhava, the native will be wealthy, virtuous, honoured by the king, charitable and will enjoy happiness from father and others

### 适用边界路

- Surya is the indicator of father for all beings, while the mother is indicated by Chandra
- Indications of Dharm Bhava. Fortunes, wife’s brother, religion, brother’s wife, visits to shrines etc. be known from Dharm Bhava

### 判断方法路

- Dharm Bhava and the 9<sup>th</sup> from Surya deal with one’s father
- 判断父子关系要看上升主（Lagn's Lord）与六宫主（Ari's Lord）的哪些配置

## 上游问题

- 无

## 停止条件

- 缺少上升主（Lagn's Lord）落宫事实时停止。
- 缺少上升主与六宫主是否同宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
