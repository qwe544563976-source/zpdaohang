---
method: ch03-v59-60-inauspicious-effect-reverse
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 凶效方向：凶效与上述吉效比例恰好相反

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 落陷的行星凶效是不是更强
- 凶效怎么按尊贵状态折算

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘该行星（Grah）落在哪个星座

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch03-v59-60-inauspicious-effect-reverse.step-001

- 动作：把上述吉效比例的方向反过来看凶效，不再另立比例。
- 适用范围：第3章吉效比例条末句；原文只说与上述所陈相反，没有逐档给出凶效的比例。
- 原文最小意思：就上述所陈而言，凶效恰好相反。
- 本步骤产出事实：["凶效方向相反判定"]
- 所需事实：["本盘该行星（Grah）落在哪个星座"]
- 条件关系：{"fact_key": "本盘该行星（Grah）落在哪个星座"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得替原文定义「相反」的逐档折算——原文只说与上述所陈相反，没有给凶效的比例数字。", "不得据本条推出凶效在哪一档最大或最小。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘该行星（Grah）落在哪个星座。
- 缺失即停字段：["本盘该行星（Grah）落在哪个星座"]
- 原文证据：
  - `bphs-97:santhanam:ch03:v59-60`｜PDF [12]｜“Inauspicious effects are quite reverse with reference to what is stated.”


## 四路查书计划

### 支持路

- Inauspicious effects are quite reverse with reference to what is stated
- 凶效与吉效比例相反

### 反例或取消路

- 无

### 适用边界路

- If Subhanka is deducted from 60, Asubhanka (Asubh Pankthi, inauspicious points) will emerge
- 另一处用 60 减吉分得凶分

### 判断方法路

- A Grah in exaltation gives fully good effects, while in Mooltrikon it is bereft of its auspicious effects by one fourth
- 要先拿到吉效各档才能反过来看凶效

## 上游问题

- 无

## 停止条件

- 原文没有界定「相反」如何逐档折算，需要具体凶效比例时停判。
- 缺少该行星所落星座与尊贵状态时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
