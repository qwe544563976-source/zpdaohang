---
method: ch16-v9-adopted-issues-shani-budh
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 养子女：五宫由土星或水星主管，并被土星与曼迪占据或相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会领养孩子
- 我的孩子是不是不是亲生的

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘第五宫落在哪个星座

## 按情况检查的事实

- 第五宫是否由土星（Shani）主管
- 第五宫是否由水星（Budh）主管
- 第五宫是否被土星与曼迪（Mandi）占据
- 第五宫是否被土星与曼迪（Mandi）相照

## 依赖方法

- 无

## 执行步骤

### ch16-v9-adopted-issues-shani-budh.step-001

- 动作：先定出第五宫落在哪个星座与由谁主管，再核对土星与曼迪是占据还是相照第五宫。
- 适用范围：仅限本命盘领养子女主题；原文只给这一组主管与占据相照条件，未给领养时间或人数。
- 原文最小意思：五宫由土星（Shani）或水星（Budh）主管，并且被土星与曼迪（Mandi）占据或相照时，会有养子女。
- 本步骤产出事实：["五宫土星水星主管得养子女判定"]
- 所需事实：["本盘第五宫落在哪个星座"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘第五宫落在哪个星座"}, {"operator": "OR", "operands": [{"fact_key": "第五宫是否由土星（Shani）主管"}, {"fact_key": "第五宫是否由水星（Budh）主管"}]}, {"operator": "OR", "operands": [{"fact_key": "第五宫是否被土星与曼迪（Mandi）占据"}, {"fact_key": "第五宫是否被土星与曼迪（Mandi）相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘第五宫落在哪个星座"}, "required_fact_keys": ["第五宫是否由土星（Shani）主管"], "branch_condition_logic": {"fact_key": "第五宫是否由土星（Shani）主管"}, "selection_group": "ch16-v9-adopted-issues-shani-budh.step-001:owner", "stop_condition": "选中该分支后，缺少以下事实即停止：第五宫是否由土星（Shani）主管。"}, {"when": {"fact_key": "本盘第五宫落在哪个星座"}, "required_fact_keys": ["第五宫是否由水星（Budh）主管"], "branch_condition_logic": {"fact_key": "第五宫是否由水星（Budh）主管"}, "selection_group": "ch16-v9-adopted-issues-shani-budh.step-001:owner", "stop_condition": "选中该分支后，缺少以下事实即停止：第五宫是否由水星（Budh）主管。"}, {"when": {"fact_key": "本盘第五宫落在哪个星座"}, "required_fact_keys": ["第五宫是否被土星与曼迪（Mandi）占据"], "branch_condition_logic": {"fact_key": "第五宫是否被土星与曼迪（Mandi）占据"}, "selection_group": "ch16-v9-adopted-issues-shani-budh.step-001:contact", "stop_condition": "选中该分支后，缺少以下事实即停止：第五宫是否被土星与曼迪（Mandi）占据。"}, {"when": {"fact_key": "本盘第五宫落在哪个星座"}, "required_fact_keys": ["第五宫是否被土星与曼迪（Mandi）相照"], "branch_condition_logic": {"fact_key": "第五宫是否被土星与曼迪（Mandi）相照"}, "selection_group": "ch16-v9-adopted-issues-shani-budh.step-001:contact", "stop_condition": "选中该分支后，缺少以下事实即停止：第五宫是否被土星与曼迪（Mandi）相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断领养的时间、人数或性别。", "不得把养子女改写成亲生子女的吉凶。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘第五宫落在哪个星座。
- 缺失即停字段：["本盘第五宫落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch16:v9`｜PDF [30]｜“Should Putr Bhava be owned by Shani, or Budh and be occupied, or drishtied by Shani and Mandi, one will have adopted issues.”


## 四路查书计划

### 支持路

- Putr Bhava owned by Shani Budh drishtied by Shani and Mandi adopted issues
- 五宫由土星或水星主管 土星曼迪占据相照 养子女

### 反例或取消路

- Putr Bhava strong Guru own children
- 五宫得木星力量 亲生子女 反例

### 适用边界路

- adopted issues rule scope Mandi drishti
- 养子女断语的适用边界与曼迪相照

### 判断方法路

- how to find the lord and occupants of Putr Bhava
- 怎样确定五宫宫主与五宫内的行星

## 上游问题

- 无

## 停止条件

- 缺少第五宫星座与宫主事实时停止。
- 缺少土星与曼迪对第五宫的占据或相照事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
