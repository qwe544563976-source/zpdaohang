---
method: ch37-v2-4-contrary-situation
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 相反情形下木星或金星相照月亮：财富很少甚至没有

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 木星或金星照月亮就一定好吗
- 为什么我盘里有吉星照月亮却没钱

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘是否属于原文所说的 In a contrary situation（原文未界定该情形）

## 按情况检查的事实

- 月亮（Chandra）是否被木星（Guru）相照
- 月亮（Chandra）是否被金星（Shukra）相照

## 依赖方法

- 无

## 执行步骤

### ch37-v2-4-contrary-situation.step-001

- 动作：先确认本盘是否属于原文所说的相反情形（In a contrary situation），再核对木星（Guru）或金星（Shukra）对月亮（Chandra）的相照，读取财富断语。
- 适用范围：原文只写 In a contrary situation，全句未界定什么算相反情形；该情形未确定即停判。
- 原文最小意思：在原文所说的相反情形（In a contrary situation）下，木星（Guru）或金星（Shukra）相照月亮（Chandra），会使人只有很少财富，甚至没有财富。
- 本步骤产出事实：["相反情形下的月亮受照财富断语"]
- 所需事实：["本盘是否属于原文所说的 In a contrary situation（原文未界定该情形）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘是否属于原文所说的 In a contrary situation（原文未界定该情形）"}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否被木星（Guru）相照"}, {"fact_key": "月亮（Chandra）是否被金星（Shukra）相照"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘是否属于原文所说的 In a contrary situation（原文未界定该情形）"}, "required_fact_keys": ["月亮（Chandra）是否被木星（Guru）相照"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否被木星（Guru）相照"}, "selection_group": "ch37-v2-4-contrary-situation.step-001:drishti-source", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否被木星（Guru）相照。"}, {"when": {"fact_key": "本盘是否属于原文所说的 In a contrary situation（原文未界定该情形）"}, "required_fact_keys": ["月亮（Chandra）是否被金星（Shukra）相照"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否被金星（Shukra）相照"}, "selection_group": "ch37-v2-4-contrary-situation.step-001:drishti-source", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否被金星（Shukra）相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文界定 In a contrary situation 的所指，尤其不得把它接成前两句条件的逻辑否定。", "不得据此推断具体财富数额或贫富发生的时间。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘是否属于原文所说的 In a contrary situation（原文未界定该情形）。
- 缺失即停字段：["本盘是否属于原文所说的 In a contrary situation（原文未界定该情形）"]
- 原文证据：
  - `bphs-97:santhanam:ch37:v2-4`｜PDF [81]｜“In a contrary situation, the Drishti from Guru, or from Shukra on Chandra will make one go with little wealth, or even without that.”


## 四路查书计划

### 支持路

- In a contrary situation, the Drishti from Guru, or from Shukra on Chandra will make one go with little wealth, or even without that
- 相反情形 木星金星照月亮 财富很少

### 反例或取消路

- In the case of a day birth, if Chandra, placed in its own Navāńś, or in a friendly Navāńś, receives a Drishti from Guru, one will be endowed with wealth and happiness
- One born at night time will enjoy similar effects, if Chandra is in its own Navāńś, or in a friendly Navāńś, receiving a Drishti from Shukr

### 适用边界路

- Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas
- 原文未界定相反情形 停判

### 判断方法路

- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness
- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn

## 上游问题

- 无

## 停止条件

- 原文未界定 In a contrary situation 的所指，该情形未确定即停判。
- 缺少月亮受木星或金星相照的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
