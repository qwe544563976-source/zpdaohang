---
method: ch29-v20-guru-expenses-taxes-and-self
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 木星落上升 Pad 起第 12 宫且受他星相照：开销用于赋税与本人

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我的钱会花在税上吗
- 开销主要花在哪

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 木星（Guru）是否落上升 Pad（Lagn Pad）起第 12 宫
- 木星（Guru）是否被其他行星（Grah）相照

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch29-v20-guru-expenses-taxes-and-self.step-001

- 动作：核对木星（Guru）是否落上升 Pad（Lagn Pad）起第 12 宫，并是否受其他行星相照。
- 适用范围：本条以上升 Pad（Lagn Pad）为起算点；原文只写 receiving a Drishti from others，没有指明相照者的吉凶身份。
- 原文最小意思：木星（Guru）落上升 Pad（Lagn Pad）起第 12 宫，并受其他行星相照时，开销用于赋税与本人自身。
- 本步骤产出事实：["木星在上升 Pad 起第 12 宫的开销来由判定"]
- 所需事实：["木星（Guru）是否落上升 Pad（Lagn Pad）起第 12 宫", "木星（Guru）是否被其他行星（Grah）相照"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "木星（Guru）是否落上升 Pad（Lagn Pad）起第 12 宫"}, {"fact_key": "木星（Guru）是否被其他行星（Grah）相照"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断税种、金额或年份。", "原文未指明相照者的吉凶身份，不得只按吉星相照成立本条。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：木星（Guru）是否落上升 Pad（Lagn Pad）起第 12 宫、木星（Guru）是否被其他行星（Grah）相照。
- 缺失即停字段：["木星（Guru）是否落上升 Pad（Lagn Pad）起第 12 宫", "木星（Guru）是否被其他行星（Grah）相照"]
- 原文证据：
  - `bphs-97:santhanam:ch29:v20`｜PDF [63]｜“O Brahmin, if Guru is in the 12<sup>th</sup> from Lagn Pad, receiving a Drishti from others, the expenses will be through taxes and on the person himself.”


## 四路查书计划

### 支持路

- O Brahmin, if Guru is in the 12<sup>th</sup> from Lagn Pad, receiving a Drishti from others, the expenses will be through taxes and on the person himself.
- 木星落上升 Pad 起第 12 宫 开销用于赋税

### 反例或取消路

- 无

### 适用边界路

- The same Bhava, or the 7<sup>th</sup> from it does not become its Pad.
- 上升 Pad 取宫本身的例外

### 判断方法路

- The Pad of Lagn will correspond to the Rāśi, arrived at by counting so many Rāśis from Lagn’s Lord, as he is away from Tanu Bhava
- 上升 Pad 怎么求

## 上游问题

- 无

## 停止条件

- 缺少木星相对上升 Pad 起第 12 宫的落宫事实时停止。
- 缺少木星是否受其他行星相照的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
