---
method: ch03-v61-64-upagraha-positions
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 非发光副曜（UpaGrahas）的位置推算：Dhoom、Vyatipat、Parivesh、Chap 与 UpaKetu

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- Dhoom Vyatipat Parivesh 怎么算
- 我盘里的影曜落在哪里

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘太阳（Surya）的黄经是多少

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v61-64-upagraha-positions.step-001

- 动作：在给定时刻给太阳黄经加上 4 个星座 13 度 20 分，得 Dhoom 的位置。
- 适用范围：第3章非发光副曜条；这些是推算法，本步不给盘上吉凶断语。
- 原文最小意思：在给定时刻把 4 个星座 13 度（degrees）20 分加到太阳（Surya）的黄经上，得到全然不吉的 Dhoom 的准确位置。
- 本步骤产出事实：["Dhoom 位置判定"]
- 所需事实：["本盘太阳（Surya）的黄经是多少"]
- 条件关系：{"fact_key": "本盘太阳（Surya）的黄经是多少"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出 Dhoom 落某宫的具体断语——本步只给位置。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘太阳（Surya）的黄经是多少。
- 缺失即停字段：["本盘太阳（Surya）的黄经是多少"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v61-64`｜PDF [12, 13]｜“Add 4 Rāśis 13 degrees and 20 minutes of arc to Surya’s longitude at a given moment to get the exact position of the all inauspicious Dhoom.”

### ch03-v61-64-upagraha-positions.step-002

- 动作：用 12 个星座减去 Dhoom，得 Vyatipat 的位置。
- 适用范围：第3章非发光副曜条；这些是推算法，本步不给盘上吉凶断语。
- 原文最小意思：用 12 个星座减去 Dhoom，得到 Vyatipat，Vyatipat 同样不吉。
- 本步骤产出事实：["Vyatipat 位置判定"]
- 所需事实：["Dhoom 位置判定"]
- 条件关系：{"fact_key": "Dhoom 位置判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出 Vyatipat 落某宫的具体断语——本步只给位置。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Dhoom 位置判定。
- 缺失即停字段：["Dhoom 位置判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v61-64`｜PDF [12, 13]｜“Reduce Dhoom from 12 Rāśis to arrive at Vyatipat. Vyatipat is also inauspicious.”

### ch03-v61-64-upagraha-positions.step-003

- 动作：给 Vyatipat 加六个星座，得 Parivesh 的位置。
- 适用范围：第3章非发光副曜条；这些是推算法，本步不给盘上吉凶断语。
- 原文最小意思：把六（six）个星座加到 Vyatipat 上，得知 Parivesh 的位置，他极为不吉。
- 本步骤产出事实：["Parivesh 位置判定"]
- 所需事实：["Vyatipat 位置判定"]
- 条件关系：{"fact_key": "Vyatipat 位置判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出 Parivesh 落某宫的具体断语——本步只给位置。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Vyatipat 位置判定。
- 缺失即停字段：["Vyatipat 位置判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v61-64`｜PDF [12, 13]｜“Add six Rāśis to Vyatipat to know the position of Parivesh. He is extremely inauspicious.”

### ch03-v61-64-upagraha-positions.step-004

- 动作：用 12 个星座减去 Parivesh，得 Chap 的位置。
- 适用范围：第3章非发光副曜条；这些是推算法，本步不给盘上吉凶断语。
- 原文最小意思：用 12 个星座减去 Parivesh，得到 Chap（Indra Dhanus）的位置，他同样不吉。
- 本步骤产出事实：["Chap 位置判定"]
- 所需事实：["Parivesh 位置判定"]
- 条件关系：{"fact_key": "Parivesh 位置判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出 Chap 落某宫的具体断语——本步只给位置。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Parivesh 位置判定。
- 缺失即停字段：["Parivesh 位置判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v61-64`｜PDF [12, 13]｜“Deduct Parivesh from 12 Rāśis to arrive at the position of Chap (Indra Dhanus), who is also inauspicious.”

### ch03-v61-64-upagraha-positions.step-005

- 动作：给 Chap 加 16 度 40 分得 UpaKetu，再加一个星座回到太阳黄经以自校。
- 适用范围：第3章非发光副曜条；这些是推算法，本步不给盘上吉凶断语。
- 原文最小意思：把 16 度（degrees）40 分加到 Chap 上，得到 Ketu（UpaKetu），他是凶曜；再给 UpaKetu 加一个星座，就回到太阳（Surya）本来的黄经。
- 本步骤产出事实：["UpaKetu 位置判定"]
- 所需事实：["Chap 位置判定"]
- 条件关系：{"fact_key": "Chap 位置判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这里的 Ketu（UpaKetu）与九曜中的 Ketu 混为一谈——原文在此专称 UpaKetu。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Chap 位置判定。
- 缺失即停字段：["Chap 位置判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v61-64`｜PDF [12, 13]｜“Add 16 degrees 40 minutes to Chap, which will give Ketu (UpaKetu), who is a malefic. By adding a Rashito UpaKetu, you get the original longitude of Surya.”

### ch03-v61-64-upagraha-positions.step-006

- 动作：把这五个推算出来的天体一并判为无光的凶曜。
- 适用范围：第3章非发光副曜条；本句是对上述五者的总述。
- 原文最小意思：这些是无光的曜，本性为凶，能致损害。
- 本步骤产出事实：["非发光副曜凶性判定"]
- 所需事实：["Dhoom 位置判定", "Vyatipat 位置判定", "Parivesh 位置判定", "Chap 位置判定", "UpaKetu 位置判定"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "Dhoom 位置判定"}, {"fact_key": "Vyatipat 位置判定"}, {"fact_key": "Parivesh 位置判定"}, {"fact_key": "Chap 位置判定"}, {"fact_key": "UpaKetu 位置判定"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这五者并入九曜名单——原文另称它们为 UpaGrahas。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：Dhoom 位置判定、Vyatipat 位置判定、Parivesh 位置判定、Chap 位置判定、UpaKetu 位置判定。
- 缺失即停字段：["Dhoom 位置判定", "Vyatipat 位置判定", "Parivesh 位置判定", "Chap 位置判定", "UpaKetu 位置判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v61-64`｜PDF [12, 13]｜“These are the Grahas, devoid of splendour, which are malefics by nature and cause affliction.”


## 四路查书计划

### 支持路

- Add 4 Rāśis 13 degrees and 20 minutes of arc to Surya’s longitude at a given moment to get the exact position of the all inauspicious Dhoom
- Reduce Dhoom from 12 Rāśis to arrive at Vyatipat. Vyatipat is also inauspicious
- 非发光副曜 Dhoom Vyatipat Parivesh Chap UpaKetu 推算

### 反例或取消路

- 无

### 适用边界路

- From Surya to Shani no one is exalted in the above-mentioned exaltation Rāśis, nor debilitated in the above-mentioned debilitation Rāśis
- 影曜的尊贵表出自转述，且不适用于七曜

### 判断方法路

- If one of these afflicts Surya, the native’s dynasty will decline
- Effects of Vyatipat in Various Bhavas (up to Sloka 25)
- 算出影曜位置之后怎么断

## 上游问题

- 无

## 停止条件

- 缺少本盘太阳黄经时停止。
- 上一环位置没算出来时，后续各环停止。
- 本条只给位置与凶性，不给逐宫断语，要断落宫效应必须另找原文。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
