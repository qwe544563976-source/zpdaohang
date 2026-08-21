---
method: ch14-v9-twelve-cobirth-count
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 三宫主落角宫、Mangal 在三角宫入旺并与 Guru 同宫：兄弟姐妹共12人

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我一共有多少个兄弟姐妹
- 我的兄弟姐妹里谁活不长

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 三宫主是否落角宫
- Mangal 是否在三角宫入旺
- Mangal 是否与 Guru 同宫

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch14-v9-twelve-cobirth-count.step-001

- 动作：核对三宫主是否落角宫、指示星 Mangal 是否在三角宫入旺并与 Guru 同宫，得出兄弟姐妹总数。
- 适用范围：仅限本命盘三宫兄弟姐妹总数主题；原文只给这一组条件下的总数，未给出生时间。
- 原文最小意思：三宫主落角宫、指示星 Mangal 在三角宫入旺并与 Guru 同宫时，兄弟姐妹总数为12人。
- 本步骤产出事实：["兄弟姐妹总数为12人的判定"]
- 所需事实：["三宫主是否落角宫", "Mangal 是否在三角宫入旺", "Mangal 是否与 Guru 同宫"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "三宫主是否落角宫"}, {"fact_key": "Mangal 是否在三角宫入旺"}, {"fact_key": "Mangal 是否与 Guru 同宫"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把12这个总数改成其他数目，也不得据此推断兄弟姐妹的性别。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：三宫主是否落角宫、Mangal 是否在三角宫入旺、Mangal 是否与 Guru 同宫。
- 缺失即停字段：["三宫主是否落角宫", "Mangal 是否在三角宫入旺", "Mangal 是否与 Guru 同宫"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v7-11`｜PDF [29]｜“If Sahaj’s Lord is in an angle, while the significator (Mangal) is exalted in a trine and be yuti with Guru, 12 will be the number of total co-born.”

### ch14-v9-twelve-cobirth-count.step-002

- 动作：在总数为12人的判定成立时，核对其中哪几位短寿、有几位长寿。
- 适用范围：仅限上一步得出的这12位兄弟姐妹；本条以“Out of these”“the said twelve”承接上一句，原文未给寿命的年龄或年份。
- 原文最小意思：在总数为12人的兄弟姐妹中，其中两位兄姐，以及排行第3、第7、第9、第12的弟妹寿命短，另有六位在这十二人中长寿。
- 本步骤产出事实：["十二位兄弟姐妹中的短寿与长寿分布判定"]
- 所需事实：["兄弟姐妹总数为12人的判定"]
- 条件关系：{"fact_key": "兄弟姐妹总数为12人的判定"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得把短寿名单套用到总数不是12人的盘。", "不得据此推断具体去世年龄或死亡年份。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：兄弟姐妹总数为12人的判定。
- 缺失即停字段：["兄弟姐妹总数为12人的判定"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v7-11`｜PDF [29]｜“12 will be the number of total co-born. Out of these two elders and the 3<sup>rd</sup> , the 7<sup>th</sup> , the 9<sup>th</sup> and the 12<sup>th</sup> of the younger co-born will be shortlived, while six of the said twelve will be longlived.”


## 四路查书计划

### 支持路

- 三宫主落角宫 火星三角宫入旺 与木星同宫 兄弟姐妹12人

### 反例或取消路

- There will be 1 co-born Vyaya Lord joins Mangal and Guru
- 只有一位兄弟姐妹 十二宫主与火星木星同宫

### 适用边界路

- 十二位兄弟姐妹寿命判断的适用边界

### 判断方法路

- 判断兄弟姐妹总数与寿命分布的步骤

## 上游问题

- 无

## 停止条件

- 缺少三宫主落角宫事实时停止。
- 缺少 Mangal 入旺与同宫事实时停止。
- 未先得出总数为12人的判定时，不进入寿命分布步骤。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
