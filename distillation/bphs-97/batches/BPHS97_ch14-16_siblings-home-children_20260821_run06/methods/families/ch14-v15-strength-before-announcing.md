---
method: ch14-v15-strength-before-announcing
workflow_status: pilot_candidate
source_status: repeated_support
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 先估量强弱再宣布兄弟姐妹结果

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 兄弟姐妹的结论怎么下才靠谱
- 看兄弟姐妹还要看什么才敢下结论

## 来源与事实接入

- 来源状态：`repeated_support`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 三宫相关行星与瑜伽组合的强弱

## 按情况检查的事实

- 无

## 依赖方法

- 无

## 执行步骤

### ch14-v15-strength-before-announcing.step-001

- 动作：在宣布兄弟姐妹相关结果之前，先估量相关行星与瑜伽组合的强弱。
- 适用范围：仅限本章三宫兄弟姐妹结果的宣布程序；原文只说先估强弱再宣布，未给强弱的计算方法与时间。
- 原文最小意思：要先估量相关者的强弱，也要先估量这些瑜伽的强弱，然后才宣布这些结果，即宣布兄弟姐妹相关的结果。
- 本步骤产出事实：["兄弟姐妹结果宣布前的强弱评估判定"]
- 所需事实：["三宫相关行星与瑜伽组合的强弱"]
- 条件关系：{"fact_key": "三宫相关行星与瑜伽组合的强弱"}
- 按分支必查事实：[]
- 例外、取消或缓解：[]
- 禁止扩大：["不得据此自行发明强弱的计算办法或打分标准。", "不得把本条的宣布程序当成兄弟姐妹有无的独立断语。"]
- 来源状态：`repeated_support`
- 停止条件：缺少以下固定事实即停止：三宫相关行星与瑜伽组合的强弱。
- 缺失即停字段：["三宫相关行星与瑜伽组合的强弱"]
- 原文证据：
  - `bphs-97:santhanam:ch14:v4-4.5`｜PDF [28]｜“These effects be declared after assessing the strength and weakness of the concerned.”
  - `bphs-97:santhanam:ch14:v15`｜PDF [29]｜“After estimating the strength and weakness of such Yogas, the effects, related to brothers and sisters, be announced.”


## 四路查书计划

### 支持路

- After estimating the strength and weakness of such Yogas effects related to brothers and sisters be announced
- 先估量强弱 再宣布兄弟姐妹结果

### 反例或取消路

- 不看强弱直接断兄弟姐妹的反例

### 适用边界路

- 强弱估量在兄弟姐妹判断中的适用边界

### 判断方法路

- 宣布兄弟姐妹结论前的强弱估量步骤

## 上游问题

- 无

## 停止条件

- 缺少三宫相关行星与瑜伽组合的强弱事实时停止。
- 强弱未估量前不得宣布兄弟姐妹结论。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
