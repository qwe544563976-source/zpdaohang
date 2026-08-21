---
method: ch18-v19-21-two-wives
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 两位妻子：七宫主落陷或落凶星星座并与凶星同宫，同时七宫或九分盘第七宫属中性行星

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我会不会有两位妻子
- 七宫主落陷又逢中性行星主七宫会怎样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘七宫主是哪颗行星

## 按情况检查的事实

- 七宫主（Yuvati's Lord）是否落陷
- 七宫主（Yuvati's Lord）是否落凶星主管的星座
- 七宫主（Yuvati's Lord）是否与凶星同宫
- 七宫主（Yuvati's Lord）是否为中性行星（eunuch planet）
- 九分盘（Navamsa D9）第七宫（Yuvati）的星座主星是否为中性行星（eunuch planet）

## 依赖方法

- 无

## 执行步骤

### ch18-v19-21-two-wives.step-001

- 动作：取出七宫主身份，先核对它是落陷还是落凶星星座并与凶星同宫，再核对七宫或九分盘第七宫是否归中性行星所有。
- 适用范围：仅限本命盘七宫（Yuvati）妻子数目主题；原文以「wives」立说，属男命框架；原文只说 eunuch planet，未列出哪些行星算中性行星；「the 7<sup>th</sup> Navamsa」本方法按九分盘第七宫取值，该读法存疑，须人工核对原书后才可改写；「while…」一句在原文里同时管住前面两支。
- 原文最小意思：七宫主落陷、或落凶星主管的星座并与凶星同宫，同时七宫或九分盘第七宫属于中性行星时，会有两位妻子。
- 本步骤产出事实：["两位妻子判定"]
- 所需事实：["本盘七宫主是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘七宫主是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落陷"}, {"operator": "AND", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落凶星主管的星座"}, {"fact_key": "七宫主（Yuvati's Lord）是否与凶星同宫"}]}]}, {"operator": "OR", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否为中性行星（eunuch planet）"}, {"fact_key": "九分盘（Navamsa D9）第七宫（Yuvati）的星座主星是否为中性行星（eunuch planet）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘七宫主是哪颗行星"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落陷"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否落陷"}, "selection_group": "ch18-v19-21-two-wives.step-001:lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落陷。"}, {"when": {"fact_key": "本盘七宫主是哪颗行星"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否落凶星主管的星座", "七宫主（Yuvati's Lord）是否与凶星同宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "七宫主（Yuvati's Lord）是否落凶星主管的星座"}, {"fact_key": "七宫主（Yuvati's Lord）是否与凶星同宫"}]}, "selection_group": "ch18-v19-21-two-wives.step-001:lord-state", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否落凶星主管的星座、七宫主（Yuvati's Lord）是否与凶星同宫。"}, {"when": {"fact_key": "本盘七宫主是哪颗行星"}, "required_fact_keys": ["七宫主（Yuvati's Lord）是否为中性行星（eunuch planet）"], "branch_condition_logic": {"fact_key": "七宫主（Yuvati's Lord）是否为中性行星（eunuch planet）"}, "selection_group": "ch18-v19-21-two-wives.step-001:eunuch-owner", "stop_condition": "选中该分支后，缺少以下事实即停止：七宫主（Yuvati's Lord）是否为中性行星（eunuch planet）。"}, {"when": {"fact_key": "本盘七宫主是哪颗行星"}, "required_fact_keys": ["九分盘（Navamsa D9）第七宫（Yuvati）的星座主星是否为中性行星（eunuch planet）"], "branch_condition_logic": {"fact_key": "九分盘（Navamsa D9）第七宫（Yuvati）的星座主星是否为中性行星（eunuch planet）"}, "selection_group": "ch18-v19-21-two-wives.step-001:eunuch-owner", "stop_condition": "选中该分支后，缺少以下事实即停止：九分盘（Navamsa D9）第七宫（Yuvati）的星座主星是否为中性行星（eunuch planet）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断婚期、离异或妻子存殁。", "不得自行指定哪些行星算中性行星（eunuch planet）。", "不得把两位妻子扩大成多妻的通则。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘七宫主是哪颗行星。
- 缺失即停字段：["本盘七宫主是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v19-21`｜PDF [34]｜“One will have two wives, if Yuvati Lord is in fall, or in a malefic Rashialong with a malefic, while Yuvati Bhava, or the 7<sup>th</sup> Navamsa belong to a eunuch planet.”


## 四路查书计划

### 支持路

- One will have two wives, if Yuvati Lord is in fall, or in a malefic Rashi along with a malefic
- 七宫主落陷 凶星星座 中性行星 两位妻子

### 反例或取消路

- If Yuvati Lord is in his own Rāśi, or in exaltation, one will derive full happiness through his wife (and marriage)
- The native will beget a spouse endowed with (the seven principal) virtues 7th Lord is exalted

### 适用边界路

- Conversely, if Yuvati Lord is in fall, or is combust, or is in an enemy’s Rāśi, one will acquire sick wives and many wives
- If Yuvati Lord is in a Rashi of Shani, or of Shukra and be drishtied by a benefic, there will be many wives
- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Gender of the Grahas. Budh and Shani are neuters. Chandra and Shukra are females
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- PLURALITY OF WIVES eunuch planet 7th Navamsa judgment
- 判断妻子数目要看七宫主的尊贵状态与七宫归属

## 上游问题

- 无

## 停止条件

- 缺少七宫主身份事实时停止。
- 落陷与「落凶星星座并与凶星同宫」两个分支事实都缺时停止。
- 七宫与九分盘第七宫的中性行星归属事实都缺时停止（中性行星名单待排盘窗口定义）。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
