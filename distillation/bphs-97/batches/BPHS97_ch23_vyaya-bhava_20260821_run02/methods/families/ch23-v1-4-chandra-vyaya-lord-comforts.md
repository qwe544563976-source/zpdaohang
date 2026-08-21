---
method: ch23-v1-4-chandra-vyaya-lord-comforts
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 房屋床铺与享乐：月亮为十二宫主，且入旺、落本宫本九分盘，或落十一宫、九宫、五宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我住的地方好不好
- 我这辈子享不享受得到好东西

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 十二宫主（Vyaya's Lord）是否为月亮（Chandra）

## 按情况检查的事实

- 月亮（Chandra）是否入旺
- 月亮（Chandra）是否落本星座（own Rāśi）
- 月亮（Chandra）是否落在自己主管的九分盘（Navamsa D9）星座
- 月亮（Chandra）是否落十一宫（Labh）
- 月亮（Chandra）是否落九宫（Dharm）
- 月亮（Chandra）是否落五宫（Putr）
- 月亮（Chandra）在九分盘（Navamsa D9）中是否落十一宫（Labh）
- 月亮（Chandra）在九分盘（Navamsa D9）中是否落九宫（Dharm）
- 月亮（Chandra）在九分盘（Navamsa D9）中是否落五宫（Putr）

## 依赖方法

- 无

## 执行步骤

### ch23-v1-4-chandra-vyaya-lord-comforts.step-001

- 动作：先确认十二宫（Vyaya）的宫主是不是月亮（Chandra），再核对月亮是否入旺、是否落本星座（own Rāśi）或自己主管的九分盘（Navamsa D9）星座，以及是否在本盘或九分盘中落十一宫（Labh）、九宫（Dharm）、五宫（Putr）。
- 适用范围：仅限本命盘十二宫（Vyaya Bhava）主题下、且十二宫主恰为月亮（Chandra）的命盘；原文对本盘与九分盘并列写作 in Rāśi/Navāńś，两张盘各自成立即可；原文未给时间限定。后半句「The said native」承接同偈前句所指的同一命主，逐字短引已把前句一并纳入。
- 原文最小意思：月亮（Chandra）是十二宫（Vyaya）的宫主，并且入旺，或落本星座（own Rāśi）或落自己主管的九分盘（Navamsa D9）星座，或在本盘或九分盘（Navamsa D9）中落十一宫（Labh）、九宫（Dharm）或五宫（Putr）时，会拥有美好的房屋与床铺，并享有上等的香品与享乐；该命主会穿戴华贵的衣饰、有学问、有尊贵地位。
- 本步骤产出事实：["月亮为十二宫主时的居所与享乐判定"]
- 所需事实：["十二宫主（Vyaya's Lord）是否为月亮（Chandra）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "十二宫主（Vyaya's Lord）是否为月亮（Chandra）"}, {"operator": "OR", "operands": [{"fact_key": "月亮（Chandra）是否入旺"}, {"fact_key": "月亮（Chandra）是否落本星座（own Rāśi）"}, {"fact_key": "月亮（Chandra）是否落在自己主管的九分盘（Navamsa D9）星座"}, {"fact_key": "月亮（Chandra）是否落十一宫（Labh）"}, {"fact_key": "月亮（Chandra）是否落九宫（Dharm）"}, {"fact_key": "月亮（Chandra）是否落五宫（Putr）"}, {"fact_key": "月亮（Chandra）在九分盘（Navamsa D9）中是否落十一宫（Labh）"}, {"fact_key": "月亮（Chandra）在九分盘（Navamsa D9）中是否落九宫（Dharm）"}, {"fact_key": "月亮（Chandra）在九分盘（Navamsa D9）中是否落五宫（Putr）"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "十二宫主（Vyaya's Lord）是否为月亮（Chandra）"}, "required_fact_keys": ["月亮（Chandra）是否入旺"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否入旺"}, "selection_group": "ch23-v1-4-chandra-vyaya-lord-comforts.step-001:chandra-dignity-or-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否入旺。"}, {"when": {"fact_key": "十二宫主（Vyaya's Lord）是否为月亮（Chandra）"}, "required_fact_keys": ["月亮（Chandra）是否落本星座（own Rāśi）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落本星座（own Rāśi）"}, "selection_group": "ch23-v1-4-chandra-vyaya-lord-comforts.step-001:chandra-dignity-or-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落本星座（own Rāśi）。"}, {"when": {"fact_key": "十二宫主（Vyaya's Lord）是否为月亮（Chandra）"}, "required_fact_keys": ["月亮（Chandra）是否落在自己主管的九分盘（Navamsa D9）星座"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落在自己主管的九分盘（Navamsa D9）星座"}, "selection_group": "ch23-v1-4-chandra-vyaya-lord-comforts.step-001:chandra-dignity-or-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落在自己主管的九分盘（Navamsa D9）星座。"}, {"when": {"fact_key": "十二宫主（Vyaya's Lord）是否为月亮（Chandra）"}, "required_fact_keys": ["月亮（Chandra）是否落十一宫（Labh）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落十一宫（Labh）"}, "selection_group": "ch23-v1-4-chandra-vyaya-lord-comforts.step-001:chandra-dignity-or-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落十一宫（Labh）。"}, {"when": {"fact_key": "十二宫主（Vyaya's Lord）是否为月亮（Chandra）"}, "required_fact_keys": ["月亮（Chandra）是否落九宫（Dharm）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落九宫（Dharm）"}, "selection_group": "ch23-v1-4-chandra-vyaya-lord-comforts.step-001:chandra-dignity-or-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落九宫（Dharm）。"}, {"when": {"fact_key": "十二宫主（Vyaya's Lord）是否为月亮（Chandra）"}, "required_fact_keys": ["月亮（Chandra）是否落五宫（Putr）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）是否落五宫（Putr）"}, "selection_group": "ch23-v1-4-chandra-vyaya-lord-comforts.step-001:chandra-dignity-or-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）是否落五宫（Putr）。"}, {"when": {"fact_key": "十二宫主（Vyaya's Lord）是否为月亮（Chandra）"}, "required_fact_keys": ["月亮（Chandra）在九分盘（Navamsa D9）中是否落十一宫（Labh）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）在九分盘（Navamsa D9）中是否落十一宫（Labh）"}, "selection_group": "ch23-v1-4-chandra-vyaya-lord-comforts.step-001:chandra-dignity-or-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）在九分盘（Navamsa D9）中是否落十一宫（Labh）。"}, {"when": {"fact_key": "十二宫主（Vyaya's Lord）是否为月亮（Chandra）"}, "required_fact_keys": ["月亮（Chandra）在九分盘（Navamsa D9）中是否落九宫（Dharm）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）在九分盘（Navamsa D9）中是否落九宫（Dharm）"}, "selection_group": "ch23-v1-4-chandra-vyaya-lord-comforts.step-001:chandra-dignity-or-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）在九分盘（Navamsa D9）中是否落九宫（Dharm）。"}, {"when": {"fact_key": "十二宫主（Vyaya's Lord）是否为月亮（Chandra）"}, "required_fact_keys": ["月亮（Chandra）在九分盘（Navamsa D9）中是否落五宫（Putr）"], "branch_condition_logic": {"fact_key": "月亮（Chandra）在九分盘（Navamsa D9）中是否落五宫（Putr）"}, "selection_group": "ch23-v1-4-chandra-vyaya-lord-comforts.step-001:chandra-dignity-or-placement", "stop_condition": "选中该分支后，缺少以下事实即停止：月亮（Chandra）在九分盘（Navamsa D9）中是否落五宫（Putr）。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这条月亮的规则改挂到别的行星身上；原文限定十二宫主恰为月亮（Chandra）。", "不得据此推断房产数量、价值或购置时间。", "不得把并列的择一条件改写成必须同时成立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：十二宫主（Vyaya's Lord）是否为月亮（Chandra）。
- 缺失即停字段：["十二宫主（Vyaya's Lord）是否为月亮（Chandra）"]
- 原文证据：
  - `bphs-97:santhanam:ch23:v1-4`｜PDF [40]｜“One will own beautiful houses and beds and be endowed with superior scented articles and pleasures, if Chandra happens to be Vyaya’s Lord and be exalted, or be in its own Rashiand/or Navāńś, or in Labh/Dharm/Putr Bhava in Rāśi/Navāńś. The said native will live with rich clothes and ornaments, be learned and Lordly.”


## 四路查书计划

### 支持路

- One will own beautiful houses and beds and be endowed with superior scented articles and pleasures, if Chandra happens to be Vyaya’s Lord
- 月亮 十二宫主 入旺 本宫 九分盘 房屋 床铺 香品

### 反例或取消路

- If Vyaya’s Lord is in Vyaya Bhava, the native will only face heavy expenditure, will not have physical felicity, be irritable and spiteful.
- if Chandra is weak, or is associated with malefics, or, if Chandra is in Ari, Randhr, or Vyaya
- And, if Vyaya’s Lord is in Ari, or Randhr Bhava, or be in enemy’s Navāńś, in debilitation Navāńś, or in Randhr Bhava in Navāńś, one will be devoid of happiness from wife

### 适用边界路

- Indications of Vyaya Bhava. From Vyaya Bhava, one can know about expenses, history of enemies, one’s own death etc.
- For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula
- The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)

### 判断方法路

- Effects of Vyaya’s Lord in Various Bhavas
- 十二宫主是月亮时怎么判断居所与享乐

## 上游问题

- 无

## 停止条件

- 缺少十二宫主是否为月亮（Chandra）的事实时停止。
- 月亮的入旺、本宫、本九分盘星座与三宫位落宫事实全部缺失时停止。
- 九分盘（Navamsa D9）未起盘时，九分盘相关分支停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
