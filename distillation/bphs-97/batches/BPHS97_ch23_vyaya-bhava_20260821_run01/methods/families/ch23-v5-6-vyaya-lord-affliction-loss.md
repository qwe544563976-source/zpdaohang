---
method: ch23-v5-6-vyaya-lord-affliction-loss
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 妻子之乐缺失与开支之困：十二宫主落六宫、八宫，或落敌方／落陷的九分盘星座，或九分盘中落八宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我和配偶之间为什么不快乐
- 我为什么总为开销发愁

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘十二宫主（Vyaya's Lord）是哪颗行星

## 按情况检查的事实

- 十二宫主（Vyaya's Lord）是否落六宫（Ari）
- 十二宫主（Vyaya's Lord）是否落八宫（Randhr）
- 十二宫主（Vyaya's Lord）是否落敌方行星主管的九分盘（Navamsa D9）星座
- 十二宫主（Vyaya's Lord）是否落自己落陷的九分盘（Navamsa D9）星座
- 十二宫主（Vyaya's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）

## 依赖方法

- 无

## 执行步骤

### ch23-v5-6-vyaya-lord-affliction-loss.step-001

- 动作：先取本盘十二宫主（Vyaya's Lord）是哪颗行星，再核对它是否落六宫（Ari）或八宫（Randhr），是否落敌方行星主管的九分盘（Navamsa D9）星座、自己落陷的九分盘星座，或在九分盘中落八宫（Randhr）。
- 适用范围：仅限本命盘十二宫（Vyaya Bhava）主题；原文断语写作 devoid of happiness from wife，是以有妻的命主立说，女命是否适用原文未说明；原文未给时间限定。
- 原文最小意思：十二宫主（Vyaya's Lord）落六宫（Ari）或八宫（Randhr），或落敌方行星主管的九分盘（Navamsa D9）星座，或落自己落陷的九分盘（Navamsa D9）星座，或在九分盘（Navamsa D9）中落八宫（Randhr）时，命主没有来自妻子的幸福，为开支所困，并失去一般的幸福。
- 本步骤产出事实：["十二宫主受损时的配偶之乐与开支判定"]
- 所需事实：["本盘十二宫主（Vyaya's Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, {"operator": "OR", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否落六宫（Ari）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落八宫（Randhr）"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落敌方行星主管的九分盘（Navamsa D9）星座"}, {"fact_key": "十二宫主（Vyaya's Lord）是否落自己落陷的九分盘（Navamsa D9）星座"}, {"fact_key": "十二宫主（Vyaya's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否落六宫（Ari）"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否落六宫（Ari）"}, "selection_group": "ch23-v5-6-vyaya-lord-affliction-loss.step-001:vyaya-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否落六宫（Ari）。"}, {"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否落八宫（Randhr）"}, "selection_group": "ch23-v5-6-vyaya-lord-affliction-loss.step-001:vyaya-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否落八宫（Randhr）。"}, {"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否落敌方行星主管的九分盘（Navamsa D9）星座"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否落敌方行星主管的九分盘（Navamsa D9）星座"}, "selection_group": "ch23-v5-6-vyaya-lord-affliction-loss.step-001:vyaya-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否落敌方行星主管的九分盘（Navamsa D9）星座。"}, {"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）是否落自己落陷的九分盘（Navamsa D9）星座"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）是否落自己落陷的九分盘（Navamsa D9）星座"}, "selection_group": "ch23-v5-6-vyaya-lord-affliction-loss.step-001:vyaya-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）是否落自己落陷的九分盘（Navamsa D9）星座。"}, {"when": {"fact_key": "本盘十二宫主（Vyaya's Lord）是哪颗行星"}, "required_fact_keys": ["十二宫主（Vyaya's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）"], "branch_condition_logic": {"fact_key": "十二宫主（Vyaya's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）"}, "selection_group": "ch23-v5-6-vyaya-lord-affliction-loss.step-001:vyaya-lord-affliction", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫主（Vyaya's Lord）在九分盘（Navamsa D9）中是否落八宫（Randhr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「没有来自妻子的幸福」升级为离婚、丧偶或无法结婚。", "不得据此推断开支的金额或发生年份。", "不得把五个择一条件改写成必须同时成立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘十二宫主（Vyaya's Lord）是哪颗行星。
- 缺失即停字段：["本盘十二宫主（Vyaya's Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch23:v5-6`｜PDF [40]｜“And, if Vyaya’s Lord is in Ari, or Randhr Bhava, or be in enemy’s Navāńś, in debilitation Navāńś, or in Randhr Bhava in Navāńś, one will be devoid of happiness from wife, be troubled by expenses and deprived of general happiness.”


## 四路查书计划

### 支持路

- And, if Vyaya’s Lord is in Ari, or Randhr Bhava, or be in enemy’s Navāńś, in debilitation Navāńś, or in Randhr Bhava in Navāńś
- 十二宫主 落六宫 落八宫 敌宫九分盘 妻子之乐 开支之困

### 反例或取消路

- If Vyaya’s Lord is in Randhr Bhava, the native will always gain, will speak affably, will enjoy a medium span of life and be endowed with all good qualities.
- If Vyaya’s Lord is in Ari Bhava, the native will incur enmity with his own men, be given to anger, be sinful, miserable and will go to others’ wives.
- There will be expenses on good accounts, if Vyaya’s Lord is with a benefic, or in his own Bhava, or exalted

### 适用边界路

- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.
- The Grahas ruling such Rāśis are its friends, apart from the Lord of its exaltation Rāśi. Lords other than these are its enemies.
- For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula
- Now be kind enough to throw light on Stri Jatak (female horoscopy)

### 判断方法路

- Effects of Vyaya’s Lord in Various Bhavas
- 十二宫主落凶宫时该怎么判断

## 上游问题

- 无

## 停止条件

- 缺少本盘十二宫主是哪颗行星的事实时停止。
- 五个择一条件的事实全部缺失时停止。
- 九分盘（Navamsa D9）未起盘时，三个九分盘分支停止。
- 行星敌友关系未确定时，敌方九分盘星座分支停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
