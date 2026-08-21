---
method: ch36-v15-16-bhairi-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Bhairi Yog：九宫主有力，且十二宫、一宫、二宫、七宫都被占据，或金星木星与上升主都落角宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有富贵成名的组合
- 我这辈子财富、妻子和子女怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 九宫主（Dharm's Lord）是否有力

## 按情况检查的事实

- 十二宫（Vyaya）是否被行星占据
- 上升宫（Tanu Bhava）是否被行星占据
- 二宫（Dhan）是否被行星占据
- 七宫（Yuvati）是否被行星占据
- 金星（Shukra）是否落角宫
- 木星（Guru）是否落角宫
- 上升主（Lagn's Lord）是否落角宫

## 依赖方法

- 无

## 执行步骤

### ch36-v15-16-bhairi-yog.step-001

- 动作：先核对九宫主（Dharm's Lord）是否有力，再核对十二宫（Vyaya）、上升宫（Tanu Bhava）、二宫（Dhan）与七宫（Yuvati）是否都被行星占据，或金星（Shukr）、木星（Guru）与上升主（Lagn's Lord）是否都落角宫，判定 Bhairi Yog 是否成立。
- 适用范围：仅限本命盘 Bhairi Yog 的成立判定；原文本句未给出「有力」的判准，也没有时间限定。
- 原文最小意思：九宫主（Dharm's Lord）有力，且十二宫（Vyaya）、上升宫（Tanu Bhava）、二宫（Dhan）与七宫（Yuvati）都被行星占据，或金星（Shukr）、木星（Guru）与上升主（Lagn's Lord）都落角宫，则 Bhairi Yog 成立。
- 本步骤产出事实：["Bhairi Yog 成立判定"]
- 所需事实：["九宫主（Dharm's Lord）是否有力"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "九宫主（Dharm's Lord）是否有力"}, {"operator": "OR", "operands": [{"operator": "AND", "operands": [{"fact_key": "十二宫（Vyaya）是否被行星占据"}, {"fact_key": "上升宫（Tanu Bhava）是否被行星占据"}, {"fact_key": "二宫（Dhan）是否被行星占据"}, {"fact_key": "七宫（Yuvati）是否被行星占据"}]}, {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落角宫"}, {"fact_key": "木星（Guru）是否落角宫"}, {"fact_key": "上升主（Lagn's Lord）是否落角宫"}]}]}]}
- 按分支必查事实：[{"when": {"fact_key": "九宫主（Dharm's Lord）是否有力"}, "required_fact_keys": ["十二宫（Vyaya）是否被行星占据", "上升宫（Tanu Bhava）是否被行星占据", "二宫（Dhan）是否被行星占据", "七宫（Yuvati）是否被行星占据"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "十二宫（Vyaya）是否被行星占据"}, {"fact_key": "上升宫（Tanu Bhava）是否被行星占据"}, {"fact_key": "二宫（Dhan）是否被行星占据"}, {"fact_key": "七宫（Yuvati）是否被行星占据"}]}, "selection_group": "ch36-v15-16-bhairi-yog.step-001:bhairi-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：十二宫（Vyaya）是否被行星占据、上升宫（Tanu Bhava）是否被行星占据、二宫（Dhan）是否被行星占据、七宫（Yuvati）是否被行星占据。"}, {"when": {"fact_key": "九宫主（Dharm's Lord）是否有力"}, "required_fact_keys": ["金星（Shukra）是否落角宫", "木星（Guru）是否落角宫", "上升主（Lagn's Lord）是否落角宫"], "branch_condition_logic": {"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落角宫"}, {"fact_key": "木星（Guru）是否落角宫"}, {"fact_key": "上升主（Lagn's Lord）是否落角宫"}]}, "selection_group": "ch36-v15-16-bhairi-yog.step-001:bhairi-formation", "stop_condition": "选中该分支后，缺少以下事实即停止：金星（Shukra）是否落角宫、木星（Guru）是否落角宫、上升主（Lagn's Lord）是否落角宫。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文本句没有给出「有力」的判准，不得自行发明力量算法。", "原文第一种成立方式只说四宫被占据，没有区分吉凶星，不得自行加上吉星或凶星的限定。", "第二种成立方式原文要求三颗都落角宫，不得放宽成其中一两颗。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：九宫主（Dharm's Lord）是否有力。
- 缺失即停字段：["九宫主（Dharm's Lord）是否有力"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v15-16`｜PDF [79]｜“If Vyaya, Tanu, Dhan and Yuvati Bhava are occupied, as Dharm’s Lord is strong, the native obtains Bhairi Yog.”
  - `bphs-97:santhanam:ch36:v15-16`｜PDF [79]｜“Again another kind of Bhairi Yog is formed, if Shukr, Guru and Lagn’s Lord are in a Kendr, while Dharm’s Lord is strong.”

### ch36-v15-16-bhairi-yog.step-002

- 动作：在 Bhairi Yog 成立时读取财富、家室、地位与名声的断语。
- 适用范围：仅限已判定 Bhairi Yog 成立的本命盘；原文以 wife and sons、He 立说（男命框架），未给时间限定。
- 原文最小意思：Bhairi Yog 的结果是：命主会有财富、妻子与儿子；他会成为国王、有名声、有德行，并具备良好的举止、幸福与享乐。
- 本步骤产出事实：["Bhairi Yog 效果断语"]
- 所需事实：["Bhairi Yog 成立判定"]
- 条件关系：{"fact_key": "Bhairi Yog 成立判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文未给妻子与子女的数目，不得据此推断有几个儿子。", "不得把「成为国王」改写成某个具体官职或现代职位。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Bhairi Yog 成立判定。
- 缺失即停字段：["Bhairi Yog 成立判定"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v15-16`｜PDF [79]｜“The results of Bhairi Yog are: the native will be endowed with wealth, wife and sons. He will be a king, be famous, virtuous and endowed with good behaviour, happiness and pleasures.”


## 四路查书计划

### 支持路

- If Vyaya, Tanu, Dhan and Yuvati Bhava are occupied, as Dharm’s Lord is strong, the native obtains Bhairi Yog
- Again another kind of Bhairi Yog is formed, if Shukr, Guru and Lagn’s Lord are in a Kendr
- 九宫主有力 金星木星上升主落角宫 Bhairi Yog

### 反例或取消路

- If Lagn’s Lord is yuti with the Lord of Ari, Randhr, or Vyaya Bhava, or with Shani and, if Lagn’s Lord is devoid of a Drishti from a benefic, the native will be penniless
- If inauspicious Bhavas are occupied by benefics, while auspicious Bhavas are occupied by malefics, the native will be indigent
- If the Lords of a Kendr, or a Kon own simultaneously an evil Bhava, he does not cause a Raj Yog by mere relations stipulated

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- Kendras, Konas etc. defined. The Kendras are specially known, as Lagn (the ascendent), Bandhu Bhava, Yuvati Bhava (the descendant) and Karm Bhava (mid-heaven)
- Benefics, owning Kendras, will not give benefic effects, while malefics, owning Kendras, will not remain inauspicious

### 判断方法路

- Indications of Dharm Bhava
- Thus the auspicious and inauspicious effects, derivable through the Grahas, due to their lordship, according to the rising Rāśi, have to be estimated

## 上游问题

- 无

## 停止条件

- 缺少九宫主力量事实时停止。
- 「有力」的判准由排盘窗口定义，未给出取值时停止。
- 四宫被占据与三星落角宫两组事实都缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
