---
method: ch14-v4-cobirth-gender
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三宫的阴阳属性：兄弟姐妹的性别

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会有弟弟还是妹妹
- 我兄弟姐妹是男是女
- 我下面会不会有妹妹

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 三宫主是哪颗行星
- 三宫涉及的行星与星座是否阴阳混合

## 按情况检查的事实

- 三宫主是否为阴性行星
- 三宫是否被阴性行星占据
- 三宫主是否为阳性行星
- 三宫是否被阳性行星占据
- 三宫所在星座是否为阳性星座

## 依赖方法

- 无

## 执行步骤

### ch14-v4-cobirth-gender.step-001

- 动作：核对三宫主是否为阴性行星，或三宫是否被阴性行星占据。
- 适用范围：仅限本命盘三宫兄弟姐妹性别主题；原文只说晚生的妹妹，未给数目与时间。
- 原文最小意思：三宫主是阴性行星，或三宫被阴性行星占据，会有比自己晚生的妹妹。
- 本步骤产出事实：["三宫阴性主晚生妹妹判定"]
- 所需事实：["三宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "三宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "三宫主是否为阴性行星"}, {"fact_key": "三宫是否被阴性行星占据"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫主是否为阴性行星"], "branch_condition_logic": {"fact_key": "三宫主是否为阴性行星"}, "selection_group": "ch14-v4-cobirth-gender.step-001:female-source", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主是否为阴性行星。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫是否被阴性行星占据"], "branch_condition_logic": {"fact_key": "三宫是否被阴性行星占据"}, "selection_group": "ch14-v4-cobirth-gender.step-001:female-source", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫是否被阴性行星占据。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断妹妹的数目、出生年份或存亡。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：三宫主是哪颗行星。
- 缺失即停字段：["三宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v4-4.5`｜PDF [28]｜“If Sahaj’s Lord is a female Grah, or, if Sahaj Bhava be occupied by female Grahas, one will have sisters, born after him.”

### ch14-v4-cobirth-gender.step-002

- 动作：先取得三宫主是哪颗行星，再核对阳性一侧的三种指示：三宫主为阳性行星、三宫被阳性行星占据、三宫所在星座为阳性星座。
- 适用范围：仅限本章三宫兄弟姐妹性别主题；本句以“Similarly”承接上一句的阴性判法，原文未给数目与时间。原文以 Similarly 承接上一句的析取框架，阳性一侧与阴性一侧地位相同：三种指示各自主有弟弟，不需要同时成立。
- 原文最小意思：三宫的阳性行星与阳性星座主有弟弟。
- 本步骤产出事实：["三宫阳性主有弟弟判定"]
- 所需事实：["三宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "三宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "三宫主是否为阳性行星"}, {"fact_key": "三宫是否被阳性行星占据"}, {"fact_key": "三宫所在星座是否为阳性星座"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫主是否为阳性行星"], "branch_condition_logic": {"fact_key": "三宫主是否为阳性行星"}, "selection_group": "ch14-v4-cobirth-gender.step-002:male-source", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫主是否为阳性行星。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫是否被阳性行星占据"], "branch_condition_logic": {"fact_key": "三宫是否被阳性行星占据"}, "selection_group": "ch14-v4-cobirth-gender.step-002:male-source", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫是否被阳性行星占据。"}, {"when": {"fact_key": "三宫主是哪颗行星"}, "required_fact_keys": ["三宫所在星座是否为阳性星座"], "branch_condition_logic": {"fact_key": "三宫所在星座是否为阳性星座"}, "selection_group": "ch14-v4-cobirth-gender.step-002:male-source", "stop_condition": "选中该分支后，缺少以下事实即停止：三宫所在星座是否为阳性星座。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断弟弟的数目、出生年份或存亡。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：三宫主是哪颗行星。
- 缺失即停字段：["三宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v4-4.5`｜PDF [28]｜“Similarly male Grahas and male Rāśis denote younger brothers.”

### ch14-v4-cobirth-gender.step-003

- 动作：核对三宫涉及的行星与星座是否为阴阳混合。
- 适用范围：仅限本章三宫兄弟姐妹性别主题；本句以“it”承接上文的阴阳判法，原文未给数目与时间。
- 原文最小意思：三宫涉及的行星与星座为阴阳混合时，会得到两性兼有的兄弟姐妹。
- 本步骤产出事实：["三宫阴阳混合主两性兄弟姐妹判定"]
- 所需事实：["三宫涉及的行星与星座是否阴阳混合"]
- 条件关系：{"fact_key": "三宫涉及的行星与星座是否阴阳混合"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断两性兄弟姐妹各自的数目或先后次序。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：三宫涉及的行星与星座是否阴阳混合。
- 缺失即停字段：["三宫涉及的行星与星座是否阴阳混合"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v4-4.5`｜PDF [28]｜“Should it be of mixed nature, co-born of both sexes will be obtained.”


## 四路查书计划

### 支持路

- Sahaj Lord female Grah sisters born after him male Rasis younger brothers
- 三宫主阴性行星 妹妹 阳性星座 弟弟

### 反例或取消路

- Surya Sahaj Bhava destroy preborn Shani destroy afterborn
- 三宫凶星 兄弟姐妹被毁

### 适用边界路

- female and male co-born strength and weakness assessment
- 兄弟姐妹性别判断的适用边界

### 判断方法路

- how to determine gender of co-born from Sahaj Bhava
- 判断兄弟姐妹性别的步骤

## 上游问题

- 无

## 停止条件

- 缺少三宫主行星身份事实时停止。
- 缺少三宫内行星与三宫星座的阴阳属性事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
