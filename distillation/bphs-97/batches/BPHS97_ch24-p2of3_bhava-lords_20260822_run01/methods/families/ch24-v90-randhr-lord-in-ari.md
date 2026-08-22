---
method: ch24-v90-randhr-lord-in-ari
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 八宫主落六宫：胜过敌人、受疾病困扰、童年遭遇蛇与水的危险

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我和对手较量能不能占上风
- 我小时候为什么老出险情

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 八宫主（Randhr's Lord）是否落六宫（Ari）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch24-v90-randhr-lord-in-ari.step-001

- 动作：核对八宫主（Randhr's Lord）是否落六宫（Ari Bhava），据此判断本人与敌人的胜负、疾病困扰与童年的险情。
- 适用范围：仅限本命盘八宫主（Randhr's Lord）落六宫（Ari Bhava）一条；原文只把蛇与水的危险限定在童年（during childhood），其余断语未给时间限定；本段原文自标「Effects of Randhr’s Lord in Various Bhavas (up to Sloka 96)」；原文未给病名与危险的具体年份。
- 原文最小意思：八宫主（Randhr's Lord）落六宫（Ari Bhava）时，本人胜过自己的敌人，受疾病困扰，并在童年遭遇来自蛇与水的危险。
- 本步骤产出事实：["八宫主落六宫的敌我胜负与童年险情判定"]
- 所需事实：["八宫主（Randhr's Lord）是否落六宫（Ari）"]
- 条件关系：{"fact_key": "八宫主（Randhr's Lord）是否落六宫（Ari）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把童年的蛇与水之险扩大到成年之后——原文限定在童年。", "不得据此推断具体病名、病程或危险的年份。", "不得把本条套用到八宫主落其他宫位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：八宫主（Randhr's Lord）是否落六宫（Ari）。
- 缺失即停字段：["八宫主（Randhr's Lord）是否落六宫（Ari）"]
- 原文证据：
  - `bphs-97:santhanam:ch24:v90`｜PDF [46]｜“If Randhr’s Lord is in Ari Bhava, the native will win over his enemies, be afflicted by diseases and during childhood will incur danger through snakes and water.”


## 四路查书计划

### 支持路

- If Randhr’s Lord is in Ari Bhava, the native will win over his enemies, be afflicted by diseases
- 八宫主落六宫 胜过敌人 疾病 童年 蛇与水

### 反例或取消路

- If Dhum is in Ari Bhava, the native will be strong, will conquer his enemies, be very brilliant, famous and free from diseases

### 适用边界路

- Indications of Randhr Bhava. Randhr Bhava indicates longevity, battle, enemies, forts, wealth of the dead and things, that have happened and are to happen
- Indications of Ari Bhava. Maternal uncle, doubts about death, enemies, ulcers, stepmother etc. are to be estimated from Ari Bhava

### 判断方法路

- Effects of Randhr’s Lord in Various Bhavas
- Effects of Ari Bhava

## 上游问题

- 无

## 停止条件

- 缺少八宫主是否落六宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
