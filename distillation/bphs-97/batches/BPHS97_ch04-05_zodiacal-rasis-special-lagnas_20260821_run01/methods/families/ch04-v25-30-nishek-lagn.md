---
method: ch04-v25-30-nishek-lagn
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 受胎上升（Nishek Lagn）推算：土星与曼迪的角距加上升宫与九宫宫始之差

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我大概是什么时候受胎的
- 我在母胎里的处境好不好
- 能不能从受胎盘看父母的寿命和生死

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘上升（Lagn）是否已知
- 土星（Shani）的黄经是多少度
- 曼迪（Mandi）的黄经是多少度
- 本盘上升宫（Lagn Bhava）宫始点与九宫（Dharm）宫始点的差是多少度
- 本盘上升主（Lagn's Lord）是否落在不可见半（自上升宫始点至下降宫始点）

## 按情况检查的事实

- 月亮（Chandra）在其所落星座内已行进多少度

## 依赖方法

- 无

## 执行步骤

### ch04-v25-30-nishek-lagn.step-001

- 动作：确认本命上升（Lagn）已知，然后取土星（Shani）与曼迪（Mandi，即 Gulik）两点的角距，作为求受胎上升的第一个量。
- 适用范围：仅限已知本命上升（Lagn）的盘；原文把这一步列为求受胎上升（Nishek Lagna）的起手步骤，未给曼迪的取法与角距的取向。
- 原文最小意思：本盘上升（Lagn）已知时，起受胎上升（Nishek Lagna）的第一步是取土星（Shani）与曼迪（Mandi）之间的角距。
- 本步骤产出事实：["土星与曼迪的角距值"]
- 所需事实：["本盘上升（Lagn）是否已知", "土星（Shani）的黄经是多少度", "曼迪（Mandi）的黄经是多少度"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘上升（Lagn）是否已知"}, {"fact_key": "土星（Shani）的黄经是多少度"}, {"fact_key": "曼迪（Mandi）的黄经是多少度"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只说取土星与曼迪的角距，没有规定按哪个方向量取，方向未确定即停判，不得自定顺逆再当成原文授权。", "不得把这一步的角距挪用到原文未提的其他推算上。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘上升（Lagn）是否已知、土星（Shani）的黄经是多少度、曼迪（Mandi）的黄经是多少度。
- 缺失即停字段：["本盘上升（Lagn）是否已知", "土星（Shani）的黄经是多少度", "曼迪（Mandi）的黄经是多少度"]
- 原文证据：
  - `bphs-97:santhanam:ch04:v25-30`｜PDF [15, 16]｜“now is a step explained to arrive at the Nishek Lagna, when the natal Lagn is known”
  - `bphs-97:santhanam:ch04:v25-30`｜PDF [15, 16]｜“Note the angular distance between Shani and Mandi (Gulik).”

### ch04-v25-30-nishek-lagn.step-002

- 动作：把第 1 步得到的土星与曼迪角距（原文『Add this』所指），加到上升宫（Lagn Bhava）宫始点与九宫（Dharm）宫始点之差上，把所得结果读作受胎与出生之间已过的月、日等。
- 适用范围：仅限受胎上升推算链条的第二步；原文只说结果以星座、度数等表示，未给星座度数换算成月日的具体折算率。
- 原文最小意思：把土星与曼迪的角距加到上升宫（Lagn Bhava）宫始点与九宫（Dharm）宫始点之差上，所得的星座与度数等结果，代表受胎与出生之间已过的月、日等。
- 本步骤产出事实：["受胎与出生之间已过的月日数"]
- 所需事实：["土星与曼迪的角距值", "本盘上升宫（Lagn Bhava）宫始点与九宫（Dharm）宫始点的差是多少度"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星与曼迪的角距值"}, {"fact_key": "本盘上升宫（Lagn Bhava）宫始点与九宫（Dharm）宫始点的差是多少度"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这个月日数当成受胎的具体钟点。", "原文没有给星座、度数折成月、日的换算率，换算率未确定即停判。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星与曼迪的角距值、本盘上升宫（Lagn Bhava）宫始点与九宫（Dharm）宫始点的差是多少度。
- 缺失即停字段：["土星与曼迪的角距值", "本盘上升宫（Lagn Bhava）宫始点与九宫（Dharm）宫始点的差是多少度"]
- 原文证据：
  - `bphs-97:santhanam:ch04:v25-30`｜PDF [15, 16]｜“Add this to the difference between the Lagn Bhava (Madhya, or cusp) and the 9<sup>th</sup> Bhava (cusp). The resultant product in Rāśis, degrees etc. will represent the months, days etc., that elapsed between Nishek and birth.”

### ch04-v25-30-nishek-lagn.step-003

- 动作：检查出生时上升主（Lagn's Lord）是否落在不可见半（自上升宫始点至下降宫始点）；落在其中时，把月亮（Chandra）在其所落星座内已行进的度数加到第 2 步所得的结果上。
- 适用范围：只在出生时上升主落不可见半时才加这一项；原文以本命出生时刻立说，未说其他时刻是否照办。
- 原文最小意思：出生时上升主（Lagn Lord）落在不可见半（自上升宫始点至下降宫始点）时，把月亮（Chandra）在其所落星座（Rāśi）内已行进的度数加到上述结果上。
- 本步骤产出事实：["加入月亮行度后的受胎间隔"]
- 所需事实：["受胎与出生之间已过的月日数", "本盘上升主（Lagn's Lord）是否落在不可见半（自上升宫始点至下降宫始点）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "受胎与出生之间已过的月日数"}, {"fact_key": "本盘上升主（Lagn's Lord）是否落在不可见半（自上升宫始点至下降宫始点）"}]}
- 按分支必查事实：[{"when": {"fact_key": "本盘上升主（Lagn's Lord）是否落在不可见半（自上升宫始点至下降宫始点）"}, "required_fact_keys": ["月亮（Chandra）在其所落星座内已行进多少度"], "stop_condition": "命中该条件分支后，缺少以下事实即停止：月亮（Chandra）在其所落星座内已行进多少度。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只在上升主落不可见半时加月亮行度，不得反过来在其他情形下减去或另加数值。", "不得把不可见半改读成原文没写的其他半球划法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：受胎与出生之间已过的月日数、本盘上升主（Lagn's Lord）是否落在不可见半（自上升宫始点至下降宫始点）。
- 缺失即停字段：["受胎与出生之间已过的月日数", "本盘上升主（Lagn's Lord）是否落在不可见半（自上升宫始点至下降宫始点）"]
- 原文证据：
  - `bphs-97:santhanam:ch04:v25-30`｜PDF [15, 16]｜“At birth, if Lagn Lord is in the invisible half (i.e. from Lagn cusp to descendental cusp), add the degrees etc., Chandra moved in the particular Rāśi, occupied by her, to the above-mentioned product.”

### ch04-v25-30-nishek-lagn.step-004

- 动作：用前面算出的受胎与出生间隔（第 3 步成立时用加过月亮行度的值），从出生时刻回推定出受胎时的上升（Lagn at Nishek），再据以推测命主在母胎中所经历的吉与凶。
- 适用范围：原文用『can be guessed』（可以推测）措辞，是推测性结论，强度不等同确断；且未给母胎吉凶的具体判准。
- 原文最小意思：受胎时的上升（Lagn at Nishek）被推算出来后，可推测命主在母胎中所经历的吉与凶。
- 本步骤产出事实：["受胎上升（Nishek Lagn）", "胎中吉凶的推测"]
- 所需事实：["受胎与出生之间已过的月日数", "本盘上升（Lagn）是否已知"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "受胎与出生之间已过的月日数"}, {"fact_key": "本盘上升（Lagn）是否已知"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只说可推测母胎中的吉与凶，没有给判准，不得自造母胎吉凶的判断表。", "不得把母胎吉凶扩大成出生后的运势结论。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：受胎与出生之间已过的月日数、本盘上升（Lagn）是否已知。
- 缺失即停字段：["受胎与出生之间已过的月日数", "本盘上升（Lagn）是否已知"]
- 原文证据：
  - `bphs-97:santhanam:ch04:v25-30`｜PDF [15, 16]｜“Then Lagn at Nishek can be worked out and the good and bad, experienced by the native in the womb, can be guessed.”

### ch04-v25-30-nishek-lagn.step-005

- 动作：在已定出受胎上升（Nishek Lagn）之后，借助受胎上升的效果推测父母的寿命、死亡等事。
- 适用范围：原文用『One can also guess』措辞，属推测性用法；原文只举父母的寿命、死亡等，未列其余项目，也未给具体判准。
- 原文最小意思：借助受胎上升（Nishek Lagn）的效果，还可以推测父母的寿命、死亡等事。
- 本步骤产出事实：["父母寿命与死亡等效果的推测"]
- 所需事实：["受胎上升（Nishek Lagn）"]
- 条件关系：{"fact_key": "受胎上升（Nishek Lagn）"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此断出父母去世的具体年份或死因，原文只说可以推测寿命、死亡等事。", "不得把受胎上升的效果推及父母以外的亲属。", "原文没有给『受胎上升的效果』如何取，取法未确定即停判。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：受胎上升（Nishek Lagn）。
- 缺失即停字段：["受胎上升（Nishek Lagn）"]
- 原文证据：
  - `bphs-97:santhanam:ch04:v25-30`｜PDF [15, 16]｜“One can also guess with the help of Nishek Lagn effects, like longevity, death etc. of the parents.”


## 四路查书计划

### 支持路

- Note the angular distance between Shani and Mandi (Gulik). Add this to the difference between the Lagn Bhava (Madhya, or cusp) and the 9th Bhava (cusp)
- The resultant product in Rāśis, degrees etc. will represent the months, days etc., that elapsed between Nishek and birth
- add the degrees etc., Chandra moved in the particular Rāśi, occupied by her, to the above-mentioned product
- 受胎上升 土星 曼迪 角距 上升宫始 九宫宫始

### 反例或取消路

- Combinations for Father’s Death. The father of the native would have passed away prior to the native’s birth
- 父母的死亡 另有专门组合 不经受胎上升

### 适用边界路

- These durations differently apply to different places (commensurate with variable day and night durations)
- The natal Lagn is to be calculated according to birth place, while Bhava Lagna, Hora Lagn etc. are common to all places
- Grahas placed in the visible half of the zodiac will give explicit results, while the ones in the invisible half will confer secret results

### 判断方法路

- Calculations of Gulik etc. The portions of Surya etc. up to Shani denote the periods of Gulik and others
- Gulik’s Position. The degree, ascending at the time of start of Gulik’s portion (as above), will be the longitude of Gulik at a given place
- now is a step explained to arrive at the Nishek Lagna, when the natal Lagn is known
- 怎么起受胎盘 Nishek

## 上游问题

- 无

## 停止条件

- 本命上升（Lagn）未知时停止——原文以『when the natal Lagn is known』为前提。
- 缺少土星（Shani）位置或曼迪（Mandi）位置时停止。
- 缺少上升宫（Lagn Bhava）宫始点与九宫（Dharm）宫始点之差时停止。
- 原文未规定角距的取向，取向未确定即停判。
- 上升主是否落不可见半未确定时，第 3 步的加值停判。
- 原文未给母胎吉凶与父母寿命、死亡的具体判准，判准未确定即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
