---
method: ch03-v57-58-compound-relationship
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 合成关系：自然关系与临时关系合成极友、友、均等、敌、极敌

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 两颗行星最终算友还是敌
- 自然关系和临时关系冲突时怎么办

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘该两行星的自然关系（natural relationship）是友、敌还是中立
- 本盘该两行星的临时关系（temporary relationship）是友还是敌

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v57-58-compound-relationship.step-001

- 动作：两方面都为友时，判为极友。
- 适用范围：第3章合成关系条；本条只合成关系，未给各档关系的吉凶结果。
- 原文最小意思：若两颗行星（two Grahas）在自然与临时两方面都为友，它们成为极友（extremely friendly）。
- 本步骤产出事实：["两行星极友判定"]
- 所需事实：["本盘该两行星的自然关系（natural relationship）是友、敌还是中立", "本盘该两行星的临时关系（temporary relationship）是友还是敌"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘该两行星的自然关系（natural relationship）是友、敌还是中立"}, {"fact_key": "本盘该两行星的临时关系（temporary relationship）是友还是敌"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出极友带来什么吉果——本条只合成关系。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘该两行星的自然关系（natural relationship）是友、敌还是中立、本盘该两行星的临时关系（temporary relationship）是友还是敌。
- 缺失即停字段：["本盘该两行星的自然关系（natural relationship）是友、敌还是中立", "本盘该两行星的临时关系（temporary relationship）是友还是敌"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v57-58`｜PDF [12]｜“Should two Grahas be naturally and temporarily friendly, they become extremely friendly.”

### ch03-v57-58-compound-relationship.step-002

- 动作：一方面为友、另一方面为中立时，判为友。
- 适用范围：第3章合成关系条；原文没有指明「一方面」指自然还是临时，不得替它指定。
- 原文最小意思：一方面为友、另一方面为中立，两者为友。
- 本步骤产出事实：["两行星合成为友判定"]
- 所需事实：["本盘该两行星的自然关系（natural relationship）是友、敌还是中立", "本盘该两行星的临时关系（temporary relationship）是友还是敌"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘该两行星的自然关系（natural relationship）是友、敌还是中立"}, {"fact_key": "本盘该两行星的临时关系（temporary relationship）是友还是敌"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文指定「一方面」是自然关系还是临时关系。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘该两行星的自然关系（natural relationship）是友、敌还是中立、本盘该两行星的临时关系（temporary relationship）是友还是敌。
- 缺失即停字段：["本盘该两行星的自然关系（natural relationship）是友、敌还是中立", "本盘该两行星的临时关系（temporary relationship）是友还是敌"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v57-58`｜PDF [12]｜“Friendship on one count and neutrality on another count make them friendly.”

### ch03-v57-58-compound-relationship.step-003

- 动作：一方面为敌、另一方面为亲合时，判为均等。
- 适用范围：第3章合成关系条；原文没有指明「一方面」指自然还是临时，不得替它指定。
- 原文最小意思：一方面为敌、另一方面为亲合，转为均等（equality）。
- 本步骤产出事实：["两行星合成为均等判定"]
- 所需事实：["本盘该两行星的自然关系（natural relationship）是友、敌还是中立", "本盘该两行星的临时关系（temporary relationship）是友还是敌"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘该两行星的自然关系（natural relationship）是友、敌还是中立"}, {"fact_key": "本盘该两行星的临时关系（temporary relationship）是友还是敌"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文指定「一方面」是自然关系还是临时关系。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘该两行星的自然关系（natural relationship）是友、敌还是中立、本盘该两行星的临时关系（temporary relationship）是友还是敌。
- 缺失即停字段：["本盘该两行星的自然关系（natural relationship）是友、敌还是中立", "本盘该两行星的临时关系（temporary relationship）是友还是敌"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v57-58`｜PDF [12]｜“Enmity on one count combined with affinity on the other turns into equality.”

### ch03-v57-58-compound-relationship.step-004

- 动作：敌与中立相合时，判为敌。
- 适用范围：第3章合成关系条；原文没有指明哪一方面为敌、哪一方面为中立，不得替它指定。
- 原文最小意思：敌与中立相合，只成为敌。
- 本步骤产出事实：["两行星合成为敌判定"]
- 所需事实：["本盘该两行星的自然关系（natural relationship）是友、敌还是中立", "本盘该两行星的临时关系（temporary relationship）是友还是敌"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘该两行星的自然关系（natural relationship）是友、敌还是中立"}, {"fact_key": "本盘该两行星的临时关系（temporary relationship）是友还是敌"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文指定哪一方面为敌、哪一方面为中立。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘该两行星的自然关系（natural relationship）是友、敌还是中立、本盘该两行星的临时关系（temporary relationship）是友还是敌。
- 缺失即停字段：["本盘该两行星的自然关系（natural relationship）是友、敌还是中立", "本盘该两行星的临时关系（temporary relationship）是友还是敌"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v57-58`｜PDF [12]｜“Enmity and neutralship cause only enmity.”

### ch03-v57-58-compound-relationship.step-005

- 动作：两方面都为敌时判为极敌，并据这些合成关系去断盘。
- 适用范围：第3章合成关系条；末句是作者对占星者的操作交代，不是另一条盘上条件。
- 原文最小意思：若两方面都为敌，得极敌（extreme enmity）；占星者应据这些合成关系来断盘。
- 本步骤产出事实：["两行星极敌判定"]
- 所需事实：["本盘该两行星的自然关系（natural relationship）是友、敌还是中立", "本盘该两行星的临时关系（temporary relationship）是友还是敌"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "本盘该两行星的自然关系（natural relationship）是友、敌还是中立"}, {"fact_key": "本盘该两行星的临时关系（temporary relationship）是友还是敌"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据本条推出极敌带来什么凶果——本条只合成关系。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘该两行星的自然关系（natural relationship）是友、敌还是中立、本盘该两行星的临时关系（temporary relationship）是友还是敌。
- 缺失即停字段：["本盘该两行星的自然关系（natural relationship）是友、敌还是中立", "本盘该两行星的临时关系（temporary relationship）是友还是敌"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v57-58`｜PDF [12]｜“Should there be enmity in both manners, extreme enmity is obtained. The Jyotishi should consider these and declare horoscopic effects accordingly.”


## 四路查书计划

### 支持路

- Should two Grahas be naturally and temporarily friendly, they become extremely friendly
- Enmity on one count combined with affinity on the other turns into equality
- 合成关系 极友 均等 极敌

### 反例或取消路

- 无

### 适用边界路

- (This applies to a given Janm Kundali)
- 合成关系里的临时一侧只对出生盘成立

### 判断方法路

- 60, 45, 30, 22, 15, 8, 4, 2 and 0 are the Subhankas (Subha Griha Pankthis, benefic points), due to a Grah’s placement, respectively, in exaltation, Mooltrikon, own, great friend’s, friend’s, neutral, enemy’s, great enemy’s and debilitation Rāśi
- 极友 极敌 怎么折成分值

## 上游问题

- 无

## 停止条件

- 缺少该两行星的自然关系时停止。
- 缺少该两行星的临时关系时停止。
- 原文没有指明「一方面」对应自然还是临时，遇到需要区分的情形即停判。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
