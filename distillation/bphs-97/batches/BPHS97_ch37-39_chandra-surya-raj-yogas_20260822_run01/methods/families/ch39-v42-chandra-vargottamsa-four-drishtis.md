---
method: ch39-v42-chandra-vargottamsa-four-drishtis
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 月亮有力且为 Vargottāńś 并受四颗以上行星相照：成为国王

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 月亮受很多行星相照说明什么
- 我有没有登顶的组合

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 相照月亮（Chandra）的行星有几颗
- 月亮（Chandra）是否有力（endowed with strength）
- 月亮（Chandra）是否为 Vargottāńś
- 相照月亮（Chandra）的行星是否不少于四颗

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch39-v42-chandra-vargottamsa-four-drishtis.step-001

- 动作：核对月亮（Chandra）是否有力、是否为 Vargottāńś，并数相照它的行星是否不少于四颗。
- 适用范围：仅限本命盘；原文说月亮须 endowed with strength，但未给出力量的判准；原文没有时间限定。
- 原文最小意思：月亮（Chandra）有力、为 Vargottāńś，并受四颗或更多行星相照时，命主会成为国王。
- 本步骤产出事实：["月亮 Vargottāńś 受多照的贵格判定"]
- 所需事实：["相照月亮（Chandra）的行星有几颗", "月亮（Chandra）是否有力（endowed with strength）", "月亮（Chandra）是否为 Vargottāńś", "相照月亮（Chandra）的行星是否不少于四颗"]
- 条件关系：{"operator": "AND", "operands": [{"fact_key": "相照月亮（Chandra）的行星有几颗"}, {"fact_key": "月亮（Chandra）是否有力（endowed with strength）"}, {"fact_key": "月亮（Chandra）是否为 Vargottāńś"}, {"fact_key": "相照月亮（Chandra）的行星是否不少于四颗"}]}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["原文未给出 endowed with strength 的判准，不得自行指定力量门槛。", "原文没有限定相照的行星是吉是凶，不得自行加上吉星限定。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：相照月亮（Chandra）的行星有几颗、月亮（Chandra）是否有力（endowed with strength）、月亮（Chandra）是否为 Vargottāńś、相照月亮（Chandra）的行星是否不少于四颗。
- 缺失即停字段：["相照月亮（Chandra）的行星有几颗", "月亮（Chandra）是否有力（endowed with strength）", "月亮（Chandra）是否为 Vargottāńś", "相照月亮（Chandra）的行星是否不少于四颗"]
- 原文证据：
  - `bphs-97:santhanam:ch39:v42`｜PDF [84]｜“Should Chandra, endowed with strength, be Vargottāńś and receives a Drishti from four, or more Grahas, the native will become a king.”


## 四路查书计划

### 支持路

- Should Chandra, endowed with strength, be Vargottāńś and receives a Drishti from four, or more Grahas, the native will become a king
- 月亮有力 Vargottāńś 四颗行星相照 国王

### 反例或取消路

- One born in Kema Drum Yog will be very much reproached, will be bereft of intelligence, learning, reduced to penury and perils
- The divisions of a combust Grah, defeated Grah, weak Grah and a Grah in bad Avasthas, like Sayan, be all ignored to be auspicious, for these destroy the good Yogas

### 适用边界路

- Shad Bal consists of the following: Sthan Bal (positional), Dig Bal (directional), Kaal Bal (Temporal)
- This happens, when Lagn in the RashiKundali and the Navāńś Lagn are in the same Rāśi
- In the Dasha Varg scheme the designations commence from Parijata etc., such as 2 good Vargas - Parijatha, 3 Uttama, 4 Gopur, 5 Simhasan

### 判断方法路

- Raj Yogas are to be known from the Karakāńś Lagn and the natal Lagn
- The 2<sup>nd</sup> , 3<sup>rd</sup> etc. up to 12<sup>th</sup> from Chandra and Surya will deal with the same subject, as they do, when reckoned from Lagn

## 上游问题

- 无

## 停止条件

- 原文未给出月亮有力的判准，力量未确定即停判。
- 缺少月亮 Vargottāńś 事实时停止。
- 缺少相照月亮的行星计数事实时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
