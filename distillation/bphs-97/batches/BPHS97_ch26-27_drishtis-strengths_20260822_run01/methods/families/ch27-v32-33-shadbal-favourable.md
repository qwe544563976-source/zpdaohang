---
method: ch27-v32-33-shadbal-favourable
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 六力达标：行星有力则对命主显吉

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我盘里这颗行星够不够有力
- 行星有力对我是好事吗

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 所考察行星（Grah）的六力（Shad Bal）总值是多少 Virupas

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch27-v32-33-shadbal-favourable.step-001

- 动作：取所考察行星的六力（Shad Bal）总值，与原文列出的所需 Shad Bal Pinda 比较，判定它是否达到有力的门槛。
- 适用范围：仅限本章 Shad Bal 体系内的强弱判定；原文只写「Surya etc.」，没有把七个数值逐颗对应到行星，本步不替它指定对应次序。
- 原文最小意思：六力（Shad Bal）Pinda 达到 390、360、300、420、390、330、300 Virupas 时，Surya 等行星才视为有力。
- 本步骤产出事实：["所考察行星（Grah）的六力（Shad Bal）达标判定"]
- 所需事实：["所考察行星（Grah）的六力（Shad Bal）总值是多少 Virupas"]
- 条件关系：{"fact_key": "所考察行星（Grah）的六力（Shad Bal）总值是多少 Virupas"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["本步只判定有力与否，不得据此直接给出任何吉凶事项。", "原文只写 Surya etc.，不得自行指定七个所需数值与各行星的逐一对应次序。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所考察行星（Grah）的六力（Shad Bal）总值是多少 Virupas。
- 缺失即停字段：["所考察行星（Grah）的六力（Shad Bal）总值是多少 Virupas"]
- 原文证据：
  - `bphs-97:santhanam:ch27:v32-33`｜PDF [60]｜“390, 360, 300, 420, 390, 330 and 300 Virupas are the Shad Bal Pindas, needed for Surya etc. to be considered strong.”

### ch27-v32-33-shadbal-favourable.step-002

- 动作：把所考察行星的六力（Shad Bal）总值与同偈前句给出的所需数值比较，判定是否属于极有力。
- 适用范围：「上述数值」承接同偈前句给出的所需 Shad Bal Pinda；原文没有说明超出多少才算超出，也没有说明本句的 very strong 与同偈末句 Shani 的 extreme strength 是否同一状态。
- 原文最小意思：六力（Shad Bal）超过上述所需数值时，该行星（Grah）视为极有力。
- 本步骤产出事实：["所考察行星（Grah）的六力（Shad Bal）极有力判定"]
- 所需事实：["所考察行星（Grah）的六力（Shad Bal）总值是多少 Virupas"]
- 条件关系：{"fact_key": "所考察行星（Grah）的六力（Shad Bal）总值是多少 Virupas"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文未说明「very strong」与同偈末句 Shani 的「extreme strength」是否同一状态，两者不得互相代入。", "本步只做强度分级，不得据此给出任何吉凶事项。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所考察行星（Grah）的六力（Shad Bal）总值是多少 Virupas。
- 缺失即停字段：["所考察行星（Grah）的六力（Shad Bal）总值是多少 Virupas"]
- 原文证据：
  - `bphs-97:santhanam:ch27:v32-33`｜PDF [60]｜“If the strength exceeds the above-mentioned values, the Grah is deemed to be very strong.”

### ch27-v32-33-shadbal-favourable.step-003

- 动作：在该行星已判定达到所需六力（Shad Bal）时，按原文断它凭力量对命主显出有利。
- 适用范围：原文只说凭其力量对命主显出有利，没有指明显在哪一宫、哪一时段或哪一件事上。
- 原文最小意思：行星（Grah）具备所需的六力（Shad Bal）时，会凭其力量对命主（native）显出有利。
- 本步骤产出事实：["所考察行星（Grah）对命主显吉判定"]
- 所需事实：["所考察行星（Grah）的六力（Shad Bal）达标判定"]
- 条件关系：{"fact_key": "所考察行星（Grah）的六力（Shad Bal）达标判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断具体的应验事项、时间或程度。", "不得把这一条反推成六力不足即对命主不利。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：所考察行星（Grah）的六力（Shad Bal）达标判定。
- 缺失即停字段：["所考察行星（Grah）的六力（Shad Bal）达标判定"]
- 原文证据：
  - `bphs-97:santhanam:ch27:v32-33`｜PDF [60]｜“If a Grah has the required Shad Bal, it will prove favourable to the native by virtue of its strength.”


## 四路查书计划

### 支持路

- If a Grah has the required Shad Bal, it will prove favourable to the native by virtue of its strength
- 390, 360, 300, 420, 390, 330 and 300 Virupas are the Shad Bal Pindas
- 六力达标 行星对命主显吉

### 反例或取消路

- However, Shani’s extreme strength will give long life as well as miseries
- 力量强反而带来苦难的说法

### 适用边界路

- Evaluation Of Strengths
- 六力判强的适用范围：只算 Surya 到 Shani 七曜

### 判断方法路

- thus the various sources of strengths be gathered together and effects declared
- 怎样把各类力量汇总起来算六力

## 上游问题

- 无

## 停止条件

- 缺少所考察行星（Grah）的六力（Shad Bal）总值时停止。
- 无法确定所考察行星对应原文所列哪一个所需 Shad Bal Pinda 数值时停止。
- 所考察对象不是原文所说的 Surya 至 Shani 七曜时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
