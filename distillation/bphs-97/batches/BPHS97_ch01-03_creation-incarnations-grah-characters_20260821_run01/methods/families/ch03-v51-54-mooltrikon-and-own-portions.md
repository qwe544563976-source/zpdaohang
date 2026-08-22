---
method: ch03-v51-54-mooltrikon-and-own-portions
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 附加尊贵：七曜各自的 Mooltrikon 段与 own Bhava 段

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我盘里这颗行星落在 Mooltrikon 还是别的段
- 各行星的 Mooltrikon 是哪几度

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 太阳（Surya）落在狮子座（Simh）内的第几度
- 月亮（Chandra）落在金牛座（Vrishabh）内的第几度
- 火星（Mangal）落在白羊座（Mesh）内的第几度
- 水星（Budh）落在处女座（Kanya）内的第几度
- 木星（Guru）落在射手座（Dhanu）内的第几度
- 金星（Shukra）落在天秤座（Tula）内的第几度
- 土星（Shani）落在水瓶座（Kumbh）内的第几度

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v51-54-mooltrikon-and-own-portions.step-001

- 动作：取太阳在狮子座内的度数，判断它落在 Mooltrikon 段还是 own Bhava 段。
- 适用范围：第3章附加尊贵条；原文此处用语为 own Bhava，本偈没有界定它与星座（Rāśi）、宫（Bhava）的对应，故照原文保留。
- 原文最小意思：狮子座（Simh）的前（first）20 度（degrees）是太阳（Surya）的 Mooltrikon，其余部分是他的 own Bhava。
- 本步骤产出事实：["太阳在狮子座的分段尊贵判定"]
- 所需事实：["太阳（Surya）落在狮子座（Simh）内的第几度"]
- 条件关系：{"fact_key": "太阳（Surya）落在狮子座（Simh）内的第几度"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 own Bhava 读成宫位落点——本偈只在星座度数范围内说话。", "不得据本条推出落在各段时吉效如何折算。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：太阳（Surya）落在狮子座（Simh）内的第几度。
- 缺失即停字段：["太阳（Surya）落在狮子座（Simh）内的第几度"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v51-54`｜PDF [12]｜“In Simh the first 20 degrees are Surya’s Mooltrikon, while the rest is his own Bhava.”

### ch03-v51-54-mooltrikon-and-own-portions.step-002

- 动作：取月亮在金牛座内的度数，判断它落在入旺段之后的 Mooltrikon 段。
- 适用范围：第3章附加尊贵条；本句只说入旺段之后的部分，未说金牛座内还有别的分段。
- 原文最小意思：金牛座（Vrishabh）中入旺段的前（first）3 度（degrees）之后，对月亮（Chandra）而言其余部分是她的 Mooltrikon。
- 本步骤产出事实：["月亮在金牛座的分段尊贵判定"]
- 所需事实：["月亮（Chandra）落在金牛座（Vrishabh）内的第几度"]
- 条件关系：{"fact_key": "月亮（Chandra）落在金牛座（Vrishabh）内的第几度"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出月亮在金牛座另有 own Bhava 段——本句没有说。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：月亮（Chandra）落在金牛座（Vrishabh）内的第几度。
- 缺失即停字段：["月亮（Chandra）落在金牛座（Vrishabh）内的第几度"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v51-54`｜PDF [12]｜“After the first 3 degrees of exaltation portion in Vrishabh, for Chandra, the rest is her Mooltrikon.”

### ch03-v51-54-mooltrikon-and-own-portions.step-003

- 动作：取火星在白羊座内的度数，判断它落在 Mooltrikon 段还是 own Bhava 段。
- 适用范围：第3章附加尊贵条；原文此处用语为 own Bhava，本偈没有界定它与星座（Rāśi）、宫（Bhava）的对应，故照原文保留。
- 原文最小意思：火星（Mangal）在白羊座（Mesh）的前（first）12 度（degrees）为 Mooltrikon，其余部分只是他的 own Bhava。
- 本步骤产出事实：["火星在白羊座的分段尊贵判定"]
- 所需事实：["火星（Mangal）落在白羊座（Mesh）内的第几度"]
- 条件关系：{"fact_key": "火星（Mangal）落在白羊座（Mesh）内的第几度"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 own Bhava 读成宫位落点——本偈只在星座度数范围内说话。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：火星（Mangal）落在白羊座（Mesh）内的第几度。
- 缺失即停字段：["火星（Mangal）落在白羊座（Mesh）内的第几度"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v51-54`｜PDF [12]｜“Mangal has the first 12 degrees in Mesh, as Mooltrikon with the rest therein becoming simply his own Bhava.”

### ch03-v51-54-mooltrikon-and-own-portions.step-004

- 动作：取水星在处女座内的度数，判断它落在入旺区、Mooltrikon 段还是 own Bhava 段。
- 适用范围：第3章附加尊贵条；原文此处用语为 own Bhava，本偈没有界定它与星座（Rāśi）、宫（Bhava）的对应，故照原文保留。
- 原文最小意思：对水星（Budh）而言，处女座（Kanya）的前（first）15 度（degrees）为入旺区，接下来的 5 度为 Mooltrikon，最后 10 度为 own Bhava。
- 本步骤产出事实：["水星在处女座的分段尊贵判定"]
- 所需事实：["水星（Budh）落在处女座（Kanya）内的第几度"]
- 条件关系：{"fact_key": "水星（Budh）落在处女座（Kanya）内的第几度"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 own Bhava 读成宫位落点——本偈只在星座度数范围内说话。", "不得据本条推出水星深度入旺的度数——那由另一偈给出。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：水星（Budh）落在处女座（Kanya）内的第几度。
- 缺失即停字段：["水星（Budh）落在处女座（Kanya）内的第几度"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v51-54`｜PDF [12]｜“For Budh, in Kanya the first 15 degrees are exaltation zone, the next 5 degrees Mooltrikon and the last 10 degrees are own Bhava.”

### ch03-v51-54-mooltrikon-and-own-portions.step-005

- 动作：取木星在射手座内的度数，判断它落在 Mooltrikon 段还是 own Bhava 段。
- 适用范围：第3章附加尊贵条；原文此处用语为 own Bhava，本偈没有界定它与星座（Rāśi）、宫（Bhava）的对应，故照原文保留。
- 原文最小意思：射手座（Dhanu）的前（first）三分之一（one third）是木星（Guru）的 Mooltrikon，其余部分是他的 own Bhava。
- 本步骤产出事实：["木星在射手座的分段尊贵判定"]
- 所需事实：["木星（Guru）落在射手座（Dhanu）内的第几度"]
- 条件关系：{"fact_key": "木星（Guru）落在射手座（Dhanu）内的第几度"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 own Bhava 读成宫位落点——本偈只在星座度数范围内说话。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）落在射手座（Dhanu）内的第几度。
- 缺失即停字段：["木星（Guru）落在射手座（Dhanu）内的第几度"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v51-54`｜PDF [12]｜“The first one third of Dhanu is the Mooltrikon of Guru, while the remaining part thereof is his own Bhava.”

### ch03-v51-54-mooltrikon-and-own-portions.step-006

- 动作：取金星在天秤座内的度数，判断它落在前半的 Mooltrikon 还是后半的 own Bhava。
- 适用范围：第3章附加尊贵条；原文此处用语为 own Bhava，本偈没有界定它与星座（Rāśi）、宫（Bhava）的对应，故照原文保留。
- 原文最小意思：金星（Shukra）把天秤座（Tula）分成两半（two halves），前一半（first）为 Mooltrikon，后一半（second）为 own Bhava。
- 本步骤产出事实：["金星在天秤座的分段尊贵判定"]
- 所需事实：["金星（Shukra）落在天秤座（Tula）内的第几度"]
- 条件关系：{"fact_key": "金星（Shukra）落在天秤座（Tula）内的第几度"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把 own Bhava 读成宫位落点——本偈只在星座度数范围内说话。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：金星（Shukra）落在天秤座（Tula）内的第几度。
- 缺失即停字段：["金星（Shukra）落在天秤座（Tula）内的第几度"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v51-54`｜PDF [12]｜“Shukra divides Tula into two halves keeping the first, as Mooltrikon and the second, as own Bhava.”

### ch03-v51-54-mooltrikon-and-own-portions.step-007

- 动作：取土星在水瓶座内的度数，按太阳在狮子座的同一分法判断它的分段尊贵。
- 适用范围：第3章附加尊贵条；本句以太阳在狮子座的分法为准，分段界线承本方法第一步。
- 原文最小意思：土星（Shani）在水瓶座（Kumbh）的分段安排相同，与太阳（Surya）在狮子座（Simh）的安排一样。
- 本步骤产出事实：["土星在水瓶座的分段尊贵判定"]
- 所需事实：["土星（Shani）落在水瓶座（Kumbh）内的第几度", "太阳在狮子座的分段尊贵判定"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "土星（Shani）落在水瓶座（Kumbh）内的第几度"}, {"fact_key": "太阳在狮子座的分段尊贵判定"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把这条同分法推广到土星主管的另一个星座——本句只说水瓶座（Kumbh）。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：土星（Shani）落在水瓶座（Kumbh）内的第几度、太阳在狮子座的分段尊贵判定。
- 缺失即停字段：["土星（Shani）落在水瓶座（Kumbh）内的第几度", "太阳在狮子座的分段尊贵判定"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v51-54`｜PDF [12]｜“Shani’s arrangements are same in Kumbh, as Surya has in Simh.”


## 四路查书计划

### 支持路

- In Simh the first 20 degrees are Surya’s Mooltrikon, while the rest is his own Bhava
- For Budh, in Kanya the first 15 degrees are exaltation zone, the next 5 degrees Mooltrikon and the last 10 degrees are own Bhava
- Shukra divides Tula into two halves keeping the first, as Mooltrikon and the second, as own Bhava
- 各曜的 Mooltrikon 度数段

### 反例或取消路

- 无

### 适用边界路

- Note the Rāśis, which are the 2<sup>nd</sup> , 4<sup>th</sup> , 5<sup>th</sup> , 8<sup>th</sup> , 9<sup>th</sup> and 12<sup>th</sup> from the Mooltrikon of a Grah
- Mooltrikon 还被用来定自然友敌

### 判断方法路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- 落在 Mooltrikon 段之后吉效怎么折算

## 上游问题

- 无

## 停止条件

- 缺少该行星在对应星座内度数的事实时，该步停止。
- 原文没有界定 own Bhava 与星座、宫的对应，需要把它映射成排盘取值时停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
