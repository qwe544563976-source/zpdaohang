---
method: ch36-v23-24-kurm-yog
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Kurm Yog：吉星以本宫、入旺或友好星座占据五宫六宫七宫，凶星以本宫或入旺落三宫十一宫一宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我有没有做领袖的命
- 我这辈子的地位与名声怎么样

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 五宫（Putr）是否被吉星占据
- 六宫（Ari）是否被吉星占据
- 七宫（Yuvati）是否被吉星占据
- 三宫（Sahaj）是否被凶星占据
- 十一宫（Labh）是否被凶星占据
- 一宫（Tanu）是否被凶星占据

## 按情况检查的事实

- 占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否落本宫
- 占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否入旺
- 占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否落友好星座（friendly Rāśi）
- 落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）的凶星是否落本宫
- 落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）的凶星是否入旺

## 依赖方法

- 无

## 执行步骤

### ch36-v23-24-kurm-yog.step-001

- 动作：先核对五宫（Putr）、六宫（Ari）、七宫（Yuvati）内是否有吉星、三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）内是否有凶星，再分别核对这些吉星与凶星的尊贵状态。
- 适用范围：仅限本命盘 Kurm Yog 的成立与效果；原文对吉星一侧给出本宫、入旺、友好星座三选一，对凶星一侧只给出本宫、入旺两选一，两侧原文本来就不对称，不得互相补齐。原文未给时间限定。
- 原文最小意思：五宫（Putr）、六宫（Ari）、七宫（Yuvati）被吉星占据，且这些吉星落本宫、入旺或落友好星座（friendly Rāśi），同时凶星落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu），且这些凶星落本宫或入旺时，成立 Kurm Yog，命主会成为国王、勇敢、有德、有名、乐于助人、快乐，并会成为众人的领袖。
- 本步骤产出事实：["Kurm Yog 成立判定"]
- 所需事实：["五宫（Putr）是否被吉星占据", "六宫（Ari）是否被吉星占据", "七宫（Yuvati）是否被吉星占据", "三宫（Sahaj）是否被凶星占据", "十一宫（Labh）是否被凶星占据", "一宫（Tanu）是否被凶星占据"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "五宫（Putr）是否被吉星占据"}, {"fact_key": "六宫（Ari）是否被吉星占据"}, {"fact_key": "七宫（Yuvati）是否被吉星占据"}, {"fact_key": "三宫（Sahaj）是否被凶星占据"}, {"fact_key": "十一宫（Labh）是否被凶星占据"}, {"fact_key": "一宫（Tanu）是否被凶星占据"}]}, {"operator": "OR", "operands": [{"fact_key": "占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否落本宫"}, {"fact_key": "占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否入旺"}, {"fact_key": "占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否落友好星座（friendly Rāśi）"}]}, {"operator": "OR", "operands": [{"fact_key": "落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）的凶星是否落本宫"}, {"fact_key": "落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）的凶星是否入旺"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "五宫（Putr）是否被吉星占据"}, {"fact_key": "六宫（Ari）是否被吉星占据"}, {"fact_key": "七宫（Yuvati）是否被吉星占据"}, {"fact_key": "三宫（Sahaj）是否被凶星占据"}, {"fact_key": "十一宫（Labh）是否被凶星占据"}, {"fact_key": "一宫（Tanu）是否被凶星占据"}]}, "required_fact_keys": ["占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否落本宫"], "branch_condition_logic": {"fact_key": "占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否落本宫"}, "selection_group": "ch36-v23-24-kurm-yog.step-001:benefic-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否落本宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "五宫（Putr）是否被吉星占据"}, {"fact_key": "六宫（Ari）是否被吉星占据"}, {"fact_key": "七宫（Yuvati）是否被吉星占据"}, {"fact_key": "三宫（Sahaj）是否被凶星占据"}, {"fact_key": "十一宫（Labh）是否被凶星占据"}, {"fact_key": "一宫（Tanu）是否被凶星占据"}]}, "required_fact_keys": ["占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否入旺"], "branch_condition_logic": {"fact_key": "占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否入旺"}, "selection_group": "ch36-v23-24-kurm-yog.step-001:benefic-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否入旺。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "五宫（Putr）是否被吉星占据"}, {"fact_key": "六宫（Ari）是否被吉星占据"}, {"fact_key": "七宫（Yuvati）是否被吉星占据"}, {"fact_key": "三宫（Sahaj）是否被凶星占据"}, {"fact_key": "十一宫（Labh）是否被凶星占据"}, {"fact_key": "一宫（Tanu）是否被凶星占据"}]}, "required_fact_keys": ["占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否落友好星座（friendly Rāśi）"], "branch_condition_logic": {"fact_key": "占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否落友好星座（friendly Rāśi）"}, "selection_group": "ch36-v23-24-kurm-yog.step-001:benefic-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：占据五宫（Putr）、六宫（Ari）、七宫（Yuvati）的吉星是否落友好星座（friendly Rāśi）。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "五宫（Putr）是否被吉星占据"}, {"fact_key": "六宫（Ari）是否被吉星占据"}, {"fact_key": "七宫（Yuvati）是否被吉星占据"}, {"fact_key": "三宫（Sahaj）是否被凶星占据"}, {"fact_key": "十一宫（Labh）是否被凶星占据"}, {"fact_key": "一宫（Tanu）是否被凶星占据"}]}, "required_fact_keys": ["落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）的凶星是否落本宫"], "branch_condition_logic": {"fact_key": "落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）的凶星是否落本宫"}, "selection_group": "ch36-v23-24-kurm-yog.step-001:malefic-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）的凶星是否落本宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "五宫（Putr）是否被吉星占据"}, {"fact_key": "六宫（Ari）是否被吉星占据"}, {"fact_key": "七宫（Yuvati）是否被吉星占据"}, {"fact_key": "三宫（Sahaj）是否被凶星占据"}, {"fact_key": "十一宫（Labh）是否被凶星占据"}, {"fact_key": "一宫（Tanu）是否被凶星占据"}]}, "required_fact_keys": ["落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）的凶星是否入旺"], "branch_condition_logic": {"fact_key": "落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）的凶星是否入旺"}, "selection_group": "ch36-v23-24-kurm-yog.step-001:malefic-dignity", "stop_condition": "选中该分支后，缺少以下事实即停止：落三宫（Sahaj）、十一宫（Labh）、一宫（Tanu）的凶星是否入旺。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断王位的具体形式、任期或领导的人数。", "凶星一侧原文只写了本宫与入旺两种尊贵，不得比照吉星一侧补出友好星座分支。", "不得把吉星与凶星的落宫互换使用。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：五宫（Putr）是否被吉星占据、六宫（Ari）是否被吉星占据、七宫（Yuvati）是否被吉星占据、三宫（Sahaj）是否被凶星占据、十一宫（Labh）是否被凶星占据、一宫（Tanu）是否被凶星占据。
- 缺失即停字段：["五宫（Putr）是否被吉星占据", "六宫（Ari）是否被吉星占据", "七宫（Yuvati）是否被吉星占据", "三宫（Sahaj）是否被凶星占据", "十一宫（Labh）是否被凶星占据", "一宫（Tanu）是否被凶星占据"]
- 原文证据：
  - `bphs-97:santhanam:ch36:v23-24`｜PDF [80]｜“If Putr, Ari and Yuvati Bhava are occupied by benefic Grahas identical with own Bhava, or exaltation, or friendly Rāśi, while malefics are in Sahaj, Labh and Tanu Bhava, in own Bhava, or in exaltation, Kurm Yog is formed. The results of Kurm Yog are: the native will be a king. be courageous, virtuous, famous, helpful, happy. He will be a leader of men.”


## 四路查书计划

### 支持路

- Kurm Yog. If Putr, Ari and Yuvati Bhava are occupied by benefic Grahas identical with own Bhava
- Kurm Yog 吉星五宫六宫七宫 凶星三宫十一宫一宫 国王 领袖

### 反例或取消路

- The native will be penniless, if Lagn’s Lord is in Vyaya Bhava, while Vyaya’s Lord is in Lagn along with the Lord of a Marak
- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- The Bhava, which is not drishtied by its Lord, or, whose Lord is with a malefic Grah, or with one of the Lords of evil and such other Bhavas

### 适用边界路

- Benefics and Malefics. Among these, Surya, Shani, Mangal, decreasing Chandra, Rahu and Ketu (the ascending and the descending nodes of Chandra) are malefics, while the rest are benefics
- Exaltation and Debilitation. For the seven Grahas, from Surya on, the exaltation Rāśis are, respectively, Mesh, Vrishabh, Makar, Kanya, Kark, Meen and Tula
- The Grahas ruling such Rāśis are its friends, apart from the Lord of its exaltation Rāśi. Lords other than these are its enemies

### 判断方法路

- Ratio of Effects. A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- Prosperity, or Annihilation of a Bhava. Predict prosperity of the Bhava, which is yuti with, or drishtied by a benefic

## 上游问题

- 无

## 停止条件

- 缺少五宫、六宫、七宫吉星占据事实或三宫、十一宫、一宫凶星占据事实时停止。
- 命中吉星尊贵分支后，缺少该分支对应的本宫、入旺或友好星座事实时停止。
- 命中凶星尊贵分支后，缺少该分支对应的本宫或入旺事实时停止。
- 吉星与凶星名册未按本书 ch03:v11 取到时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
