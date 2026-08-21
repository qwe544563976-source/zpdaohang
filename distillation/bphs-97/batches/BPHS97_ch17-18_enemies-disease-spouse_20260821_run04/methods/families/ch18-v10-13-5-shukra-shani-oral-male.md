---
method: ch18-v10-13-5-shukra-shani-oral-male
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 「亲吻」男性私处：金星与土星的同类关系（承上句「so related」）

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 金星和土星有关系时性生活是什么样
- 我的房事偏好会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘金星（Shukra）落在哪一宫

## 按情况检查的事实

- 金星（Shukra）是否落土星（Shani）主管的九分盘（Navamsa D9）星座
- 金星（Shukra）是否落土星（Shani）主管的星座
- 金星（Shukra）是否被土星（Shani）相照
- 金星（Shukra）是否与土星（Shani）同宫

## 依赖方法

- 无

## 执行步骤

### ch18-v10-13-5-shukra-shani-oral-male.step-001

- 动作：取出金星（Shukra）的位置，按上句所列的同类关系核对它与土星（Shani）的关系。
- 适用范围：仅限本命盘性事主题；本章以男命立说；「so related」承接同偈上句列出的四种关系（九分盘星座、本盘星座、相照、同宫）；原文未给强弱或时间。
- 原文最小意思：金星与土星发生上句所列的同类关系（落其主管的九分盘（Navamsa D9）星座、落其主管的星座、受其相照、与其同宫）时，命主会「亲吻」男性的私处。
- 本步骤产出事实：["金星土星相关主亲吻男性私处判定"]
- 所需事实：["本盘金星（Shukra）落在哪一宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘金星（Shukra）落在哪一宫"}, {"operator": "OR", "operands": [{"fact_key": "金星（Shukra）是否落土星（Shani）主管的九分盘（Navamsa D9）星座"}, {"fact_key": "金星（Shukra）是否落土星（Shani）主管的星座"}, {"fact_key": "金星（Shukra）是否被土星（Shani）相照"}, {"fact_key": "金星（Shukra）是否与土星（Shani）同宫"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘金星（Shukra）落在哪一宫"}, "required_fact_keys": ["金星（Shukra）是否落土星（Shani）主管的九分盘（Navamsa D9）星座"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落土星（Shani）主管的九分盘（Navamsa D9）星座"}, "selection_group": "ch18-v10-13-5-shukra-shani-oral-male.step-001:shukra-shani-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落土星（Shani）主管的九分盘（Navamsa D9）星座。"}, {"when": {"fact_key": "本盘金星（Shukra）落在哪一宫"}, "required_fact_keys": ["金星（Shukra）是否落土星（Shani）主管的星座"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否落土星（Shani）主管的星座"}, "selection_group": "ch18-v10-13-5-shukra-shani-oral-male.step-001:shukra-shani-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落土星（Shani）主管的星座。"}, {"when": {"fact_key": "本盘金星（Shukra）落在哪一宫"}, "required_fact_keys": ["金星（Shukra）是否被土星（Shani）相照"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否被土星（Shani）相照"}, "selection_group": "ch18-v10-13-5-shukra-shani-oral-male.step-001:shukra-shani-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否被土星（Shani）相照。"}, {"when": {"fact_key": "本盘金星（Shukra）落在哪一宫"}, "required_fact_keys": ["金星（Shukra）是否与土星（Shani）同宫"], "branch_condition_logic": {"fact_key": "金星（Shukra）是否与土星（Shani）同宫"}, "selection_group": "ch18-v10-13-5-shukra-shani-oral-male.step-001:shukra-shani-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否与土星（Shani）同宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["「so related」只能取上句列出的那四种关系，不得再添别的关系。", "不得据此推断婚姻、配偶身份或时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘金星（Shukra）落在哪一宫。
- 缺失即停字段：["本盘金星（Shukra）落在哪一宫"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v10-13.5`｜PDF [34]｜“If Shukra is so related to Shani, the native will “kiss” the private parts of the male.”


## 四路查书计划

### 支持路

- If Shukra is so related to Shani, the native will “kiss” the private parts of the male
- 金星 土星 九分盘 星座 相照 同宫 私处

### 反例或取消路

- Should Shukra be in a Navamsa of Mangal, or in a Rasi of Mangal, or receive a Drishti from, or be yuti with Mangal
- The native will beget a spouse endowed with (the seven principal) virtues

### 适用边界路

- If Shukra is in Randhr, while his dispositor is in a Rashiof Shani, death of wife
- Shani indicates sick and weak spouse
- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)

### 判断方法路

- 判断金星与土星的关系应检查什么

## 上游问题

- 无

## 停止条件

- 缺少金星位置事实时停止。
- 九分盘星座、本盘星座、相照、同宫四个分支事实都缺时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
