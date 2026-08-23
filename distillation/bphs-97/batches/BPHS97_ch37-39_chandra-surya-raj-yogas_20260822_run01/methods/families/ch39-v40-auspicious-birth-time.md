---
method: ch39-v40-auspicious-birth-time
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 生于正午或午夜起的两个半 Ghati 吉时：成为国王或与国王相当

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我出生的时辰好不好
- 正午前后出生有什么讲究

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘的出生时刻是什么时间

## 按情况检查的事实

- 出生时刻是否落在正午（mid-day）起的两个半 Ghati 之内
- 出生时刻是否落在午夜（mid-night）起的两个半 Ghati 之内

## 依赖方法

- 无

## 执行步骤

### ch39-v40-auspicious-birth-time.step-001

- 动作：取出生时刻，核对它是否落在正午起或午夜起的两个半 Ghati 之内。
- 适用范围：仅限本命盘出生时刻的判断；原文没有给出这段吉时的起讫换算细节。
- 原文最小意思：从正午起，或从午夜起的两个半 Ghati（Two and a half Ghatis）是吉时；生在这样的吉时会使人成为国王，或与国王相当。
- 本步骤产出事实：["出生吉时的贵格判定"]
- 所需事实：["本盘的出生时刻是什么时间"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘的出生时刻是什么时间"}, {"operator": "OR", "operands": [{"fact_key": "出生时刻是否落在正午（mid-day）起的两个半 Ghati 之内"}, {"fact_key": "出生时刻是否落在午夜（mid-night）起的两个半 Ghati 之内"}]}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘的出生时刻是什么时间"}, "required_fact_keys": ["出生时刻是否落在正午（mid-day）起的两个半 Ghati 之内"], "branch_condition_logic": {"fact_key": "出生时刻是否落在正午（mid-day）起的两个半 Ghati 之内"}, "selection_group": "ch39-v40-auspicious-birth-time.step-001:which-window", "stop_condition": "选中该分支后，缺少以下事实即停止：出生时刻是否落在正午（mid-day）起的两个半 Ghati 之内。"}, {"when": {"fact_key": "本盘的出生时刻是什么时间"}, "required_fact_keys": ["出生时刻是否落在午夜（mid-night）起的两个半 Ghati 之内"], "branch_condition_logic": {"fact_key": "出生时刻是否落在午夜（mid-night）起的两个半 Ghati 之内"}, "selection_group": "ch39-v40-auspicious-birth-time.step-001:which-window", "stop_condition": "选中该分支后，缺少以下事实即停止：出生时刻是否落在午夜（mid-night）起的两个半 Ghati 之内。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写正午与午夜两个起点，不得把日出、日落等别的时点也算进来。", "不得把两个半 Ghati 换算成原文没有给出的别的时长单位结论。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘的出生时刻是什么时间。
- 缺失即停字段：["本盘的出生时刻是什么时间"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v40`｜PDF [84]｜“Two and a half Ghatis from mid-day, or from mid-night is auspicious time. A birth during such an auspicious time will cause one to be a king, or equal to him.”


## 四路查书计划

### 支持路

- Two and a half Ghatis from mid-day, or from mid-night is auspicious time. A birth during such an auspicious time will cause one to be a king, or equal to him
- 正午午夜起两个半 Ghati 吉时 国王

### 反例或取消路

- If Lagn’s Lord along with a malefic is in Ari, Randhr, or Vyaya Bhava, while Dhan’s Lord is in an enemy’s Rāśi, or in debilitation, even a native of royal scion will become penniless
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- This Lagn changes along with every Ghati (24 minutes) from the sunrise
- I explain below again some special Lagnas, viz. Bhava Lagna, Hora Lagn and Ghati Lagn

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The Yogas, mentioned above (up to Sloka 16) should be delineated after knowing favourable, or unfavourable dispositions of the participant Grahas and their strength and weakness

## 上游问题

- 无

## 停止条件

- 缺少出生时刻事实时停止。
- 正午与午夜两个时段的判定事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
