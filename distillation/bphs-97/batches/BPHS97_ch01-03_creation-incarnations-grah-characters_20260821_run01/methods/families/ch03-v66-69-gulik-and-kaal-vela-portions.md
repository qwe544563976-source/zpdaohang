---
method: ch03-v66-69-gulik-and-kaal-vela-portions
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# Gulik 等五 Kaal Vela 的时段推算：昼夜各八等分

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Gulik 的时段怎么算
- Kaal Mrityu Yamaghantak Ardhaprahar 分别是谁的时段

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘出生当日的白昼时长是多少
- 本盘出生当夜的夜间时长是多少
- 本盘出生当日的星期主（week day Lord）是哪颗行星
- 本盘中各八等分时段分别由哪颗行星所辖
- 本盘出生地点在哪里

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v66-69-gulik-and-kaal-vela-portions.step-001

- 动作：把白昼时长八等分，第八分留作无主，其余七分自星期主起依次分配给七曜。
- 适用范围：第3章 Gulik 等推算条；本步只分配时段，不给盘上吉凶断语。
- 原文最小意思：把白昼（day）时长分成八（eight）等分，第八分（eighth）无主，其余七（seven）分自星期主起依次分配给七曜。
- 本步骤产出事实：["白昼八等分的曜主分配判定"]
- 所需事实：["本盘出生当日的白昼时长是多少", "本盘出生当日的星期主（week day Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘出生当日的白昼时长是多少"}, {"fact_key": "本盘出生当日的星期主（week day Lord）是哪颗行星"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本步推出各分时段的吉凶——本步只做分配。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生当日的白昼时长是多少、本盘出生当日的星期主（week day Lord）是哪颗行星。
- 缺失即停字段：["本盘出生当日的白昼时长是多少", "本盘出生当日的星期主（week day Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v66-69`｜PDF [13]｜“Divide the day duration (of any week day) into eight equal parts. The eighth portion is Lord-less. The seven portions are distributed to the seven Grahas commencing from the Lord of the week day.”

### ch03-v66-69-gulik-and-kaal-vela-portions.step-002

- 动作：在白昼的八等分中取土星所辖的那一分，判为 Gulik 之分。
- 适用范围：第3章 Gulik 等推算条；本步承前一步的白昼分配结果。
- 原文最小意思：由土星（Shani）所辖的那一分，即是 Gulik 之分。
- 本步骤产出事实：["白昼 Gulik 之分判定"]
- 所需事实：["白昼八等分的曜主分配判定"]
- 条件关系：{"fact_key": "白昼八等分的曜主分配判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本步推出 Gulik 的黄经——那由下一偈给出。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：白昼八等分的曜主分配判定。
- 缺失即停字段：["白昼八等分的曜主分配判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v66-69`｜PDF [13]｜“Whichever portion is ruled by Shani, will be the portion of Gulik.”

### ch03-v66-69-gulik-and-kaal-vela-portions.step-003

- 动作：把夜间时长八等分，自第 5 个星期主起依次分配，第八分无主，土星之分即 Gulik。
- 适用范围：第3章 Gulik 等推算条；本步只分配时段，不给盘上吉凶断语。
- 原文最小意思：同样把夜间时长分成八（eight）等分，自第 5 个星期主起依次分配；第八分（eighth）同样无主，土星（Shani）之分即 Gulik。
- 本步骤产出事实：["夜间八等分的曜主分配与 Gulik 判定"]
- 所需事实：["本盘出生当夜的夜间时长是多少", "本盘出生当日的星期主（week day Lord）是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘出生当夜的夜间时长是多少"}, {"fact_key": "本盘出生当日的星期主（week day Lord）是哪颗行星"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把「第 5 个星期主」改成别的起点——原文只给这一个起算法。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生当夜的夜间时长是多少、本盘出生当日的星期主（week day Lord）是哪颗行星。
- 缺失即停字段：["本盘出生当夜的夜间时长是多少", "本盘出生当日的星期主（week day Lord）是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v66-69`｜PDF [13]｜“Similarly make the night duration into eight equal parts and distribute these, commencing from the Lord of the 5<sup>th</sup> (by) week. Here again, the eighth portion is Lord-less, while Shani’s portion is Gulik.”

### ch03-v66-69-gulik-and-kaal-vela-portions.step-004

- 动作：按各分时段的所辖行星，取出其余四个 Kaal Vela 的名目。
- 适用范围：第3章 Gulik 等推算条；本句紧接昼夜两段分配之后，未分别声明只适用于其中一段。
- 原文最小意思：太阳（Surya）之分为 Kaal，火星（Mangal）之分为 Mrityu，木星（Guru）之分为 Yamaghantak，水星（Budh）之分为 Ardhaprahar。
- 本步骤产出事实：["四个 Kaal Vela 名目的曜主对应判定"]
- 所需事实：["本盘中各八等分时段分别由哪颗行星所辖"]
- 条件关系：{"fact_key": "本盘中各八等分时段分别由哪颗行星所辖"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得给月亮（Chandra）与金星（Shukr）之分补上名目——本句没有给。", "不得据本句推出这些时段的吉凶断语。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘中各八等分时段分别由哪颗行星所辖。
- 缺失即停字段：["本盘中各八等分时段分别由哪颗行星所辖"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v66-69`｜PDF [13]｜“Surya’s portion is Kaal, Mangal’s portion is Mrityu, Guru’s portion is Yamaghantak and Budh’s portion is Ardhaprahar.”

### ch03-v66-69-gulik-and-kaal-vela-portions.step-005

- 动作：按出生地点核对这些时段的实际长度，不套用固定值。
- 适用范围：第3章 Gulik 等推算条；本句是对上述时段算法的适用限制。
- 原文最小意思：这些时段随地点不同而不同，因昼夜（day and night）时长各地有别。
- 本步骤产出事实：["时段随地点变化判定"]
- 所需事实：["本盘出生地点在哪里"]
- 条件关系：{"fact_key": "本盘出生地点在哪里"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得用一地的时段长度套到另一地——原文明说各地不同。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘出生地点在哪里。
- 缺失即停字段：["本盘出生地点在哪里"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v66-69`｜PDF [13]｜“These durations differently apply to different places (commensurate with variable day and night durations).”


## 四路查书计划

### 支持路

- Divide the day duration (of any week day) into eight equal parts. The eighth portion is Lord-less
- Whichever portion is ruled by Shani, will be the portion of Gulik
- Surya’s portion is Kaal, Mangal’s portion is Mrityu, Guru’s portion is Yamaghantak and Budh’s portion is Ardhaprahar
- Gulik 时段 八等分 五 Kaal Vela

### 反例或取消路

- 无

### 适用边界路

- These durations differently apply to different places (commensurate with variable day and night durations)
- Ardhaprahar, Yamaghantak, Mrityu, Kaal and Gulik are the 5 Kaal Velas, suggested by Maharishi Parashar
- 时段算法随地点变化 译注另有交代

### 判断方法路

- The degree, ascending at the time of start of Gulik’s portion (as above), will be the longitude of Gulik at a given place
- Effects of Gulik in Various Bhavas (up to Sloka 73)
- 算出 Gulik 时段之后怎么取黄经与断效应

## 上游问题

- 无

## 停止条件

- 缺少白昼或夜间时长时，对应那一步停止。
- 缺少出生当日星期主时停止。
- 本条只给时段划分，不给吉凶断语，要断效应必须另找原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
