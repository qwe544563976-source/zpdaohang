---
method: ch40-v1-karm-lord-amatya-karak-court-chief
workflow_status: pilot_candidate
source_status: single_explicit_source
fact_binding_status: unmapped
executable_in_pilot: false
pilot_only: false
publishable: false
---

# 王廷之长：十宫主与 Amatya Karak 或其星座主同宫、受其相照

> 本文件由 `method-recipes.json` 自动生成。机器配方是唯一真相；禁止手改本文件改变状态、事实或执行许可。

## 适用问题

- 我在官场里能不能做到高位
- 我有没有近王之贵

## 来源与事实接入

- 来源状态：`single_explicit_source`
- 事实接入状态：`unmapped`
- 当前状态：`pilot_candidate`
- 允许执行：`false`
- 允许发布：`false`

## 必查事实

- 本盘十宫主（Karm's Lord）是哪颗行星
- 本盘的 Amatya Karak 是哪颗行星

## 按情况检查的事实

- 十宫主（Karm's Lord）是否与 Amatya Karak 的星座主（dispositor）同宫
- 十宫主（Karm's Lord）是否被 Amatya Karak 的星座主（dispositor）相照
- 十宫主（Karm's Lord）是否与 Amatya Karak 同宫
- 十宫主（Karm's Lord）是否被 Amatya Karak 相照

## 依赖方法

- 无

## 执行步骤

### ch40-v1-karm-lord-amatya-karak-court-chief.step-001

- 动作：先认出十宫主（Karm's Lord）与 Amatya Karak，再核对十宫主与 Amatya Karak 的星座主、以及与 Amatya Karak 本身的同宫与相照关系，据此判断是否为王廷之长。
- 适用范围：仅限本命盘十宫主与 Amatya Karak 一线；Amatya Karak 的取法本偈未给，须另按本书第 32 章按黄经次序定 Char Karak 的规则取得；原文未给时间限定，也未给上升限定。
- 原文最小意思：十宫主（Karm's Lord）与 Amatya Karak 的星座主同宫、或受其相照，或十宫主与 Amatya Karak 本身同宫、或受其相照时，命主将成为王廷之长。
- 本步骤产出事实：["十宫主与 Amatya Karak 关联的王廷之长判定"]
- 所需事实：["本盘十宫主（Karm's Lord）是哪颗行星", "本盘的 Amatya Karak 是哪颗行星"]
- 条件关系：{"operator": "AND", "operands": [{"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘的 Amatya Karak 是哪颗行星"}]}, {"operator": "OR", "operands": [{"fact_key": "十宫主（Karm's Lord）是否与 Amatya Karak 的星座主（dispositor）同宫"}, {"fact_key": "十宫主（Karm's Lord）是否被 Amatya Karak 的星座主（dispositor）相照"}, {"fact_key": "十宫主（Karm's Lord）是否与 Amatya Karak 同宫"}, {"fact_key": "十宫主（Karm's Lord）是否被 Amatya Karak 相照"}]}]}
- 按分支必查事实：[{"when": {"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘的 Amatya Karak 是哪颗行星"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否与 Amatya Karak 的星座主（dispositor）同宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否与 Amatya Karak 的星座主（dispositor）同宫"}, "selection_group": "ch40-v1-karm-lord-amatya-karak-court-chief.step-001:karm-lord-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否与 Amatya Karak 的星座主（dispositor）同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘的 Amatya Karak 是哪颗行星"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否被 Amatya Karak 的星座主（dispositor）相照"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否被 Amatya Karak 的星座主（dispositor）相照"}, "selection_group": "ch40-v1-karm-lord-amatya-karak-court-chief.step-001:karm-lord-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否被 Amatya Karak 的星座主（dispositor）相照。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘的 Amatya Karak 是哪颗行星"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否与 Amatya Karak 同宫"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否与 Amatya Karak 同宫"}, "selection_group": "ch40-v1-karm-lord-amatya-karak-court-chief.step-001:karm-lord-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否与 Amatya Karak 同宫。"}, {"when": {"operator": "AND", "operands": [{"fact_key": "本盘十宫主（Karm's Lord）是哪颗行星"}, {"fact_key": "本盘的 Amatya Karak 是哪颗行星"}]}, "required_fact_keys": ["十宫主（Karm's Lord）是否被 Amatya Karak 相照"], "branch_condition_logic": {"fact_key": "十宫主（Karm's Lord）是否被 Amatya Karak 相照"}, "selection_group": "ch40-v1-karm-lord-amatya-karak-court-chief.step-001:karm-lord-relation", "stop_condition": "选中该分支后，缺少以下事实即停止：十宫主（Karm's Lord）是否被 Amatya Karak 相照。"}]
- 例外、取消或缓解：[]
- 禁止扩大：["原文只写与 Amatya Karak 及其星座主的同宫与相照两种关系，不得扩大到互换、主管一类别的关系。", "不得据此推断具体官职、任职时间或收入。"]
- 来源状态：`single_explicit_source`
- 停止条件：缺少以下固定事实即停止：本盘十宫主（Karm's Lord）是哪颗行星、本盘的 Amatya Karak 是哪颗行星。
- 缺失即停字段：["本盘十宫主（Karm's Lord）是哪颗行星", "本盘的 Amatya Karak 是哪颗行星"]
- 原文证据：
  - `bphs-97:santhanam:ch40:v1`｜PDF [85]｜“If Karm’s Lord is yuti with, or receives a Drishti from the dispositor of Amatya Karak, or even, if Karm’s Lord is yuti with, or receives a Drishti from Amatya Karak himself, the native will be a chief in the king’s court.”


## 四路查书计划

### 支持路

- If Karm’s Lord is yuti with, or receives a Drishti from the dispositor of Amatya Karak
- 十宫主 与 Amatya Karak 同宫或相照 王廷之长

### 反例或取消路

- If the Atma Karak is adverse, other Karakas cannot give their benefic effects

### 适用边界路

- The Grah next to Atma Karak in terms of longitude is called Amatya Karak
- Amatya Karak 的取法在本书哪里界定

### 判断方法路

- Yogas For Royal Association
- If Karm and Labh Bhava are devoid of malefic occupation and devoid of Drishti from a malefic

## 上游问题

- 无

## 停止条件

- 十宫主身份事实缺失时停止。
- Amatya Karak 身份事实缺失时停止。
- 四种关联事实全部缺失时停止。

## 固定边界

- 本文件只展示机器配方，不是原文证据。
- 原文必须在运行时由原文证据检索系统重新取回。
- 事实未接通、上游问题仍阻塞、独立核验缺失或执行许可为 false 时，禁止形成结论。
- 试验产物禁止迁移编号、手改转正或正式发布。
