---
method: ch18-v27-marriage-year-18
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 第18年成婚：金星落月亮起第七宫、土星落金星起第七宫

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我大概几岁结婚
- 金星落月亮起第七宫主什么婚期

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 金星（Shukra）是否落月亮（Chandra）起第七宫（Yuvati）
- 土星（Shani）是否落金星（Shukra）起第七宫（Yuvati）

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch18-v27-marriage-year-18.step-001

- 动作：核对金星是否落在从月亮起算的第七宫，再核对土星是否落在从金星起算的第七宫。
- 适用范围：仅限本命盘七宫（Yuvati）婚期主题；两处第七宫都是从行星起算而非从上升起算；原文本偈用中性的 marriage，未限男女。
- 原文最小意思：金星落月亮起第七宫、且土星落金星起第七宫时，婚姻发生在第18年。
- 本步骤产出事实：["第18年成婚判定"]
- 所需事实：["金星（Shukra）是否落月亮（Chandra）起第七宫（Yuvati）", "土星（Shani）是否落金星（Shukra）起第七宫（Yuvati）"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "金星（Shukra）是否落月亮（Chandra）起第七宫（Yuvati）"}, {"fact_key": "土星（Shani）是否落金星（Shukra）起第七宫（Yuvati）"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此推断配偶身份或婚姻质量。", "不得把从行星起算的第七宫改成从上升起算的七宫。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：金星（Shukra）是否落月亮（Chandra）起第七宫（Yuvati）、土星（Shani）是否落金星（Shukra）起第七宫（Yuvati）。
- 缺失即停字段：["金星（Shukra）是否落月亮（Chandra）起第七宫（Yuvati）", "土星（Shani）是否落金星（Shukra）起第七宫（Yuvati）"]
- 原文证据：
  - `bphs-97:santhanam:ch18:v27`｜PDF [35]｜“Should Shukra be in Yuvati from Chandra, while Shani is in Yuvati from Shukr, marriage will be in the 18<sup>th</sup> year.”


## 四路查书计划

### 支持路

- Should Shukra be in Yuvati from Chandra, while Shani is in Yuvati from Shukr, marriage will be in the 18th year
- 金星落月亮起第七宫 土星落金星起第七宫 第18年 成婚

### 反例或取消路

- The native will marry at 12, or l9, if Shukra is in an angle from the Lagna, while Shani is in Yuvati counted from Shukr
- Marriage will be in the 15th year, if Dhan Lord is in Labh, while Lagn Lord is in Karm

### 适用边界路

- TIME OF MARRIAGE (upto Sloka 34)
- THREE MARRIAGES Should Chandra be in Yuvati from Shukr, while Budh is in Yuvati from Chandra

### 判断方法路

- 判断婚期要看从月亮与从金星起算的第七宫

## 上游问题

- 无

## 停止条件

- 缺少金星相对月亮落宫的事实时停止。
- 缺少土星相对金星落宫的事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
