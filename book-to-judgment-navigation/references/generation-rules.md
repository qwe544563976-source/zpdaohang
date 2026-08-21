# 判断方法生成规则登记簿

本文件只登记已经有真实失败证据的错误，以及防止它再次进入方法配方的共享代码和回归测试。共享生成程序和验证器当前冻结；代码审计发现的新洞，只有拿出真实批次证明它已经错误放行或错误拦截，才允许解冻修改。没有这种证据的项目只登记到“本门不查什么”，不修、不停产。能由字符串或结构确定判断的错误，新增异议必须在 24 小时内补齐“代码拦截＋正例测试＋反例测试”；开放语义错误必须登记真实标本、独立审计要求和未自动化的边界，不能用脆弱正则假装已经闭环。

## 唯一正式入口

```text
AI 按 references/method-extraction.schema.json 输出结构化 JSON
→ scripts/build_methods.py 强校验并装配 method-recipes.json（本技能内，v2 升级后唯一入口）
→ validate_delivery.py --require-v2 运行结构检查、分支通电、空话检查、步骤指纹和高风险词差异表复核
→ 正确／错误／空白三类检查
→ 按生成报告中的 audit_step_ids 独立语义审查（v3 凭证：逐步骤绑 step_hash ＋ 高风险词单选确认）
```

## v2 升级新增的机器拦截（拆网定案 2026-08-20）

- **步骤级哈希（Q1）**：每个 step 由生成器写入 `step_hash` 内容指纹；验证器重算比对，手改即失败。审计凭证逐步骤绑定 `step_hash`，改第 7 步只让第 7 步凭证失效；重产批次中指纹未变步骤的 PASS 凭证保持有效。已并入的旧方法由 `scripts/backfill_step_hash.py` 一次性回填。
- **放行公式（Q13）**：机器检查 Exit 0 ＋ 审计确认无私货 ＝ 该步放行。机器全过不等于直接放行；审计保留否决权，但作用域锁死单步。
- **一轮封顶（Q13b）＋按方法并入（Q16）**：被审计打回的步骤只重写 1 次；仍有争议即进 `quarantined_candidate` 隔离。任一步骤被隔离，整个方法不并入；同批其他健康方法照常并入。
- **方案 C 高风险词（Q15/Q21）**：生成器只强制映射四类高风险词（专名／数值／单位／时间词，词表在 `scripts/shared_constants.py`）；未映射即拒绝装配。差异表写入生成报告与配方 generation 块；审计员按清单逐词单选 accept/reject，清单外严禁找茬。
- **留插座（Q17）**：`spine_slot_hint` 现在一律 null；PVR 未正式加工前禁止填值。

### 真实原文驱动的词表与覆盖修正（2026-08-20，BPHS97 第 14~16 章开工时发现）

拿正式书包的真实 `exact_text` 试跑方案 C 时，实测出两个会直接放行错误的缺口，已修并留正反回归
（`test_build_methods.py::RealBphsTermCoverageTests`，样本全部取自 ch14~16 原文）：

| 缺口 | 真实样本 | 后果 | 修法 |
|---|---|---|---|
| 基数词不算数值 | `three mothers, or two fathers`（ch16 v10）、`six Grahas`（ch16 v11）、`Nine will be the number of sons`（ch16 v24-32） | 检出 0 个高风险词，子女／兄弟数量写错也能通过装配 | 新增 `HIGH_RISK_CARDINAL_WORDS`（two~twelve） |
| 译本短形式未收录 | `Putr’s Lord`、`with Shukr`、`Lagn’s Lord`、`Should Mandi be in Lagna`、`in own Navāńś` | 行星／宫位／分盘写错也能通过装配 | 专名表补 `putr`、`shukr`、`lagn`、`mandi`、`gulika` 与分盘名 `navamsa/navans/dwadasamsa/drekkana/decanate` |
| 覆盖判断用子串 | 词 `10` 被 `100 sons` 判为已覆盖；词 `one` 被 `money` 判为已覆盖 | 数值写错的步骤被误判为已映射 | `high_risk_term_covered` 改为按词边界匹配 |

故意不收 `one`：Santhanam 译本里 `one` 绝大多数是代词（`one will beget a child`），强制映射只产生
噪音；真正的 `one child only`（ch16 v5、v6）其结果词本来就必须进 results 映射。若将来出现 `one`
被写错的真实批次证据，再按错误家族纪律加入。

### 机器保证"有映射"，审计保证"映射对"——分工的真实样本

第一批出现一个只能靠人审的错误：ch16 v13 原文 `or is in her Decanate`，抽取把 `Decanate`
译成了"十分盘"。`Decanate`（西方 decan，星座的三分之一）对应 **Drekkana，D3 三分盘**；
十分盘是 Dasamsa（D10）。**写错分盘等于换一张盘**，结论全废。

机器在这条上做对了它该做的：`decanate` 在高风险词表里，方案 C 强制它进 `claim_terms` 映射，
差异表如实列出了 `decanate → 或落在月亮的十分盘（Decanate）`。但机器只能验证"这个词被映射了"，
验证不了"映射的中文对不对"——那需要懂 D3 与 D10 的区别。这正是 Q21 让审计员对差异表
逐词单选 accept/reject 的意义：机器把该看的词端到审计员面前，审计员只需判对错，不用自己找茬。

### 基座事实（base fact）：纯析取偈的正式写法

第一批四个抽取组**各自独立**报告了同一堵墙：schema 要求每步至少有一个 `always` 事实进
`condition_logic`，但古典断语里大量存在纯析取型偈——"五宫主落六宫、八宫或十二宫 → 无子嗣"，
语义上没有任何 AND 前提，只有一个选择组。四组各自发明了同样的变通，74 步里有 11 步（15%）
用到，全书折算约 600 步。既然是系统性的，就不该让每批自己摸索，正式定名如下。

**基座事实**：这一步在对分支求值之前必须先取得的排盘输入。

```text
✅ 正确：本盘五宫主是哪颗行星 / 本盘五宫主落在哪一宫 / 本盘第五宫落在哪个星座
❌ 错误：五宫主是否落二宫、五宫或九宫之一（把析取压进了事实名）
```

写法要求：
- `availability = always`、`role = context`；
- 必须是排盘能**直接取值**的原子事实，不能是"把多个可能性合并后的是否判断"；
- 只用于"没有它就无法对分支求值"的真实前置依赖，不得用来凑数；
- 分支条件仍然逐个写进 `alternative_groups`，一个都不许省。

语义上它站得住：不知道五宫主是谁，就无法查它落在哪一宫；取不到它就该停判，
停判输出会明确说"缺：本盘五宫主是哪颗行星"，用户看得懂。**析取藏进事实名**则由
生成器直接拦截（见上一节），因为那会让排盘系统在取值时替我们做了判断。

同批另有一个反向样本：同一条 v13 的 `with Chandra, or is in her Decanate` 是条件侧的或，
`EXPLICIT_OR_PATTERN` 的 `\bor\s*,?\s*(?:if|when|should|in|at|from)\b` 抓不到 `or is in`，
但抽取按语义正确拆成了 `alternative_groups` 两个分支。正则漏抓不等于可以不拆——
语义上是"或"就必须拆分支，不要指望闸门替你判断。

`tmp/` 中旧的 `build_*.py`、`rebuild_*.py`、批次合并脚本和“修订 N”产物只作历史记录。新批次不得调用它们，也不得在旧方法配方上继续补丁。

## 已登记错误家族

### 未定指代在护栏字段被暗中绑定（2026-08-21，BPHS97 第 17~18 章第一轮审计发现）

原文本身没有指明的指代，方法不得靠 `forbidden_extensions` 的措辞把它坐实。
这是"代词或承接关系丢失"家族的**反向形态**：那一类是原文有指代、方法丢了；
这一类是原文本就未定、方法私自定死。

真实样本：`ch18:v31` 原文「while **the natal Lord** is in Yuvati in Navamsa」，
全书 2024 条原子里 "natal Lord" 仅此一处，别处无任何界定。方法写：

    forbidden_extensions: "不得把 the natal Lord 直接当成上升主之外的别的宫主，原文没有指明。"

禁止的是"非上升主"的一切读法，**净效果等于把它锁死为上升主**——原文没给的对象绑定，
被塞进了本该是护栏的字段。同一步骤的 `applicability_scope` 还写着"未指明它是哪一宫之主"，
两个字段互相打架，下游照哪一条走都能说自己合规。

处理：
- 原文未定的指代，`applicability_scope`、`stop_conditions`、`forbidden_extensions` 三处口径必须一致，
  一律写成"未确定即停判"，不得有任何一处给出实际绑定；
- 事实名保留原文词（`the natal Lord`），让排盘窗口映射不上而停，这就是停判机制本身；
- 要绑定，必须补一条本批范围内的独立证据，不能靠护栏措辞。

机器查不了这一条（两个自然语言字段是否互相矛盾），属审计职责；
但抽取规则里已写死"护栏不得做隐性绑定"，审计按此判。

### 装配丢字段（2026-08-21，同一轮审计发现）

抽取端写对了、装配端漏抄，交付件里就没有。`assemble_step()` 是另起新字典逐字段抄写的，
加字段必须同时改它，否则闸门全绿而信息已经丢了——闸门校验的是抽取输入，不是装配输出。

真实样本：`context_bindings`／`context_reference`／`time_scope` 三个字段，
抽取端 34/34/94 步写得正确，交付件 `method-recipes.json` 里 grep 计数为 0，
第 1 批第 2 批都是如此。后果是 `ch18:v8-9½`「Mangal denotes a female with attractive breasts.」
这类承前偈的步骤，落七宫的前提来自 `ch18:v7-8½`，绑定一丢，
只读交付件的下游看到的就是一个凭空多出来的落宫条件。

处理：交付件字段集变更后，必须 grep 交付件本身确认字段真的在，不能只看抽取端通过。

## 本门不查什么

以下情况不再触发共享闸门改动：只有代码审计推演、没有真实批次因它错误放行或错误拦截；只是假设有人伪造运行回执、伪造最小凭证或故意利用空文件绕过，而现有真实批次没有因此出错。此类项目只保留审计记录，不改变共享程序、不增加测试、不停止生产。

已确认有真实失败证据并继续保留的四项：失败批次必须进入失败终态、合入必须要么全部成功要么全部回滚、备份目录不能进入正式检查、派生人读文件必须随合入回滚。

## 本轮必须持续拦截的三个错误家族（2026-08-19）

这三类不是假设题，而是已经在真实批次中出现过；以后每个新批次都按下面的处理：

- 占位事实冒充真实条件：`source_*`、`choice_*`、`原文事实已取得`、`或者分支 A/B`、`条件已成立` 等都不是排盘事实。`build_methods.py` 的 `PLACEHOLDER_FACT_PATTERNS` 负责在生成器自检时直接拒绝；验证器再做一次拦截。证据：[其他专题后半批次的独立审查报告](C:/Users/aa/Documents/ChatGPT/洗书/tmp/BPHS97_其他专题后半原文_20260819_run01/validation/independent-semantic-audit.json)。
- 逐字短引被截成句尾碎片：像只剩半个句尾的引文不能进入方法步骤；必须回到正式原文补齐完整条件—结果，再由生成器逐字核对。证据：[定位和计算基础批次的独立审查报告](C:/Users/aa/Documents/ChatGPT/洗书/tmp/BPHS97_定位和计算基础其余原文_20260819_run02/validation/independent-semantic-audit.json)。
- 多条独立规则挤进一个步骤：一个步骤只做一次明确检查；如果同一原文包含多组独立条件、结果或反制，必须拆成多个步骤并分别绑定证据。证据：[十二宫和宫主结果批次的独立审查报告](C:/Users/aa/Documents/ChatGPT/洗书/tmp/BPHS97_十二宫和宫主结果_原文批次002_20260819_run02/validation/independent-semantic-audit.json)。

本轮第9章收拢批次还留下一个具体反例：`v7-11` 步骤文字写了“Vyaya 中任意一颗行星”，但条件树没有接入实际占据事实；以后遇到“文字说检查、条件树没接线”也按真实语义错误拒绝。证据：[第9章 v3～v17 收拢批次审查报告](C:/Users/aa/Documents/ChatGPT/洗书/tmp/BPHS97_第09章出生不利条件_20260819_run06/validation/independent-semantic-audit.json)。

| 异议家族 | 真实标本 | 共享代码拦截 | 正例测试 | 反例测试 |
|---|---|---|---|---|
| OR 被压成 AND，或跨分支借用前置条件 | 第 37、42、74、75 章被驳回配方；`validation/or-multi-match-independent-review-20260819.md` 的交叉假放行；`validation/or-multi-match-independent-recheck-20260819.md` 的三分支误拒绝 | `build_methods.py` 强制 OR 写入 `alternative_groups` 并装配为 `selection_group + branch_condition_logic`；运行时要求同一分支的 `when` 与分支条件同时成立；验证器检查仅 A、仅 B、A+B、全不成立、交叉无人命中和三分支中其他分支真实命中 | `test_or_positive_is_assembled_as_selection_group`、`test_selection_group_allows_both_branches_active`、`test_accepts_selection_group_with_overlapping_branches`、`test_accepts_three_branch_cross_when_third_branch_is_active` | `test_or_negative_rejects_raw_or_in_main_logic`、`test_selection_group_crossed_when_and_logic_stops`、`test_selection_group_crossed_combination_is_checked`、`test_rejects_three_branch_when_no_branch_is_active` |
| 最小意思是空话 | 第 52～60 章 272 步空模板 | 生成器核对条件词和结果词的“原文词／中文主张词”配对；生成器和验证器共同拦截空话及三次以上原句复读 | `test_minimum_claim_positive_has_condition_and_result_pairs` | `test_minimum_claim_negative_rejects_empty_template`、`test_rejects_minimum_claim_repeated_three_times` |
| 阶段事实错挂 | 第 57～60 章开始／中段／末段异议 | `time_scope.kind=phase` 时，阶段事实必须进入对应条件树并标成 `phase_condition` | `test_phase_positive_requires_exact_phase_fact` | `test_phase_negative_rejects_unwired_phase_fact` |
| 补救混入风险条件 | 第 57～60 章念诵、捐赠等补救异议 | `remedy_condition` 禁止进入主风险条件；只能进入取消或缓解关系 | `test_remedy_positive_is_kept_in_mitigation_relation` | `test_remedy_negative_rejects_remedy_as_risk_condition` |
| even if 被写成 if | 第 57 章 step-007 | 让步条件只能写入 `concession_conditions`，不得进入主风险条件和选择分支 | `test_even_if_positive_is_separate_from_risk_gate` | `test_even_if_negative_rejects_concession_as_required_gate` |
| 代词或承接关系丢失 | 前句给条件、后句用 such／this／fully 承接的异议 | `context_reference=true` 时必须绑定本批范围内的前置原文编号 | `test_context_positive_binds_previous_atom` | `test_context_negative_rejects_missing_binding` |
| 占位事实冒充真实条件 | `tmp/BPHS97_其他专题前半其余原文_20260819_run01/validation/independent-semantic-audit.json`、`tmp/BPHS97_其他专题后半原文_20260819_run01/validation/independent-semantic-audit.json`（`source_*`、`choice_*`、`原文事实已取得`） | `build_methods.py` 和 `validate_delivery.py` 共用占位事实黑名单；命中即拒绝进入机器配方 | `test_placeholder_source_fact_is_rejected`、`test_placeholder_chinese_fact_is_rejected` | `test_generator_derives_query_scan_and_mechanical_state`（真实事实键通过） |
| 句尾碎片短引 | `tmp/BPHS97_定位和计算基础其余原文_20260819_run02/validation/independent-semantic-audit.json`（如 `fer positional displacement`、`Gangetic belt, shrines etc.`） | 先由抽取段恢复完整条件—结果边界；独立审计在高风险批次逐步骤检查，当前不加无法可靠判断句界的正则 | 真实审计条目作为回归样本，重产批次必须全审 | 完整短引正例由 `exact_text` 逐字验收；碎片反例由审计退回并保留 |
| 多条独立规则挤进一个步骤 | `tmp/BPHS97_十二宫和宫主结果_原文批次002_20260819_run02/validation/independent-semantic-audit.json`（第 21 章 step-016） | 抽取段按“一步只做一次明确检查”拆分；语义边界由独立审计确认，当前不以关键词猜规则数量 | 拆分后的真实批次作为正例；原合并步骤作为反例留档 | 机器只验结构和证据绑定，不能替代语义拆分判断 |

代码级回归位置：

- `cangjie-skill/scripts/test_build_methods.py`
- `book-to-judgment-navigation/scripts/test_validate_delivery.py`

## 审查换挡

- 大运流年、多星同聚、复杂瑜伽：永远 `full`，逐步全审。
- 生产节奏和审计密度分开：机器检查通过且没有真实依赖的下一批可以连续生产；当前审计仍保持 `full`，不因生产连续就降低审计密度。
- 只有结构单一的落宫章节，在连续三个批次没有出现新的错误家族后才允许 `sample`；这三个批次必须完成独立审计全审。一次性内容失误只退回本批，不重置计数。
- 高速状态每三个批次仍有一个批次全审。
- 抽审步骤由 `build_methods.py` 用 `batch_id` 作固定随机种子抽取 20%，写入 `audit_step_ids`；人工智能和程序员不能改名单。
- 抽审发现任何新异议时，当前批次和相邻批次恢复全审；这项回退由批次状态记录执行，不改方法正文。
- 共享生成程序或验证器一旦因新的可复现 P0 解冻，清洁批次数归零；独立审计必须在一次报告中提交完整组合矩阵：两分支、三分支、跨分支借条件、完整原文与短引，以及 `A or B`、`Either … or`、`or if/when/in`。矩阵缺一格就不能把修复记为完成。

## 案例书

- 规则书只允许 `generalization_scope=general_rule`。
- 案例书可以使用 `single_case_only`，但这种方法不得进入通用执行主路。
- 单个案例的结果不得升级成全书通则。案例书首次出现新的真实错误类别时，登记新规则和正反测试，不把“发现新书型”本身算作流程失败。

## 批次状态和老板审批

批次只能按以下顺序前进：

```text
未开工 → 生成中 → 机检仿真 → 审计中 → 已并入
```

没有机器检查记录不能进入审计，没有独立审计记录不能并入。日常批次不要求老板逐批签字；老板只审批首次进入抽审、BPHS 全书完成和系统正式发布三个里程碑。

## 不属于本地生成器的异常

`build_methods.py` 是纯本地程序，不联网，不添加 503、网络超时或接口重试。实际外部调用入口出现已复现的瞬时错误后，只在那个入口增加有限次数重试和机器日志；不能把未知的“五类异常”提前做成全局重试系统。
