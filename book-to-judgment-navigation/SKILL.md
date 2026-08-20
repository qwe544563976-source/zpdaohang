---
name: book-to-judgment-navigation
description: "一条流水线把 accepted-package.json 正式书包（或明确隔离的试点夹具）加工成判断导航：知识地图 → 原文分类盘点 → 唯一入口 scripts/build_methods.py 生成逐步骤带原文证据和 step_hash 的方法配方 → 组装四路查书计划与停止条件 → 机械验收、三对照、v3 独立审计后按方法并入总账。v2 升级版：知识地图与方法蒸馏已内置本技能，不再调用 book-to-skill 或 cangjie-skill。不负责 OCR、切卡、修复原文原子、修改 RAG 或发布未经独立核验的方法。"
---

# 必读卡（v2 升级版 · 开工只读这一张）

其余详规都是备查字典，只在报错或本卡指路表点名时翻。发现本卡漏了规矩，只准在指路表加一行链接，严禁把长篇细则贴回本卡。

## 岗位定位（管住所有越权）

```text
第 1 层【流程脊梁】= PVR          ← 未加工，留空；spine_slot_hint 一律 null
第 2 层【规则零件】= BPHS 97 ＋ UK ＋ 300C   ← BPHS 正在做
第 3 层【时间判断】= K.N. Rao     ← 未加工，留空
```

**铁律**：PVR 未正式加工前，完整看盘顺序不可用；K.N. Rao 未正式加工前，完整时间判断不可用。跨章拼接 BPHS 没写过的整盘顺序＝越权；单章内作者明写的检查清单＝合规零件，逐字锚定，不标 synthesized_candidate。

## 开工三查

1. 读项目状态总账 `JUDGMENT_PIPELINE_STATUS.json` 和写入所有权表 `JUDGMENT_WRITE_OWNERSHIP.json`；范围冻结或本窗口非责任窗口 → 只读并报告。
2. 用 `tools.register_accepted_package.run_authoritative_validation` 只读检查当前工作单绑定的这一份书包；退出码非 0 → 停止本书证据工作。另一册失败不连坐本书。
3. 读目标目录 `WORK_ORDER.json`、`PIPELINE_STATE.md`；试验任务加读 `PILOT_STATUS.json`。

## 一条流水线（每批照此跑）

```text
1 锁定只读输入（正式=accepted-package；试验=PILOT_TEMP 夹具）
2 建知识地图（本技能内做，见指路表；只答"书里有什么在哪里"）
3 原文分类盘点（每条原文记类型＋去向；分类未清零不得批量生成）
4 AI 按 references/method-extraction.schema.json 出结构化 JSON
  → 唯一入口 scripts/build_methods.py 装配 method-recipes.json
5 组装导航：方法配方＝唯一方法真相；query-recipes＝唯一主题真相
6 scripts/validate_delivery.py --render-derived 生成人读派生文件
7 scripts/validate_delivery.py <目录> --require-v2 机械验收
8 反假绿三对照：正常过、错误挂、空白挂，留真实运行凭证
9 scripts/advance_batch_state.py 送独立审计（v3 凭证）
10 审计通过 → scripts/merge_method_batch.py 单批并入，数字必须闭合
```

批次状态单向：未开工→生成中→机检仿真→审计中→已并入；失败进 rejected 终态，旧目录只留证据，重产必须新建目录。

## v2 三件套（切断死循环）

- **步骤级哈希**：每步带 `step_hash` 内容指纹；审计凭证逐步骤绑定。改第 7 步只废第 7 步的凭证，重产批次里指纹未变步骤的 PASS 原样搬入。已并入旧方法先跑一次 `scripts/backfill_step_hash.py`。
- **放行公式**：机器 Exit 0 ＋ 审计确认无私货 ＝ 该步放行。审计只准：勾已登记错误家族、判私货、附栏报疑似新家族（≤2 条、带证据、不阻塞）。机器查过的严禁重查。
- **一轮封顶**：审计打回的步骤只重写 1 次；仍有争议 → 该步进 quarantined_candidate 隔离。任一步骤被隔离，整个方法不并入；同批健康方法照常并入。

**方案 C**：四类高风险词（专名／数值／单位／时间词）必须进 claim_terms 映射，生成器直接拒绝未映射；差异表进生成报告，审计按清单逐词单选 accept/reject，清单外禁止找茬。

## 铁纪律（违者即废批）

- 不读 book.md、pages.jsonl、PDF 补证据；不切卡、不改原文原子的字、编号、页码和引用。
- 原文锚点只用 evidence_atom_id；work_id、parent_id、card_id、source_atom_ids、filters.work_ids 是退役词。
- 每步证据三件套齐全（原子编号＋逐字短引＋页码）；只有正文身份（verse/prose/table）能给通用步骤背书。
- 生成窗口绝不自审；人工填对照结论、只凭报告字段的"通过"一律无效。
- JH8／RAG 缺字段只阻止执行不阻止生产；缺口不得写成已满足。
- 原子级 P0 只隔离真实引用者；包级 P0 整本书停。P1/P2 记账不断线。
- 上游问题只登记 `UPSTREAM_ISSUES.json` 并报告，不修源、不标已解决。

## 批次与审计节奏

一批＝一个专题或直接依赖组，40～120 个审查步骤。大运流年、多星同聚、复杂瑜伽、新书型首批：永远全审。只有简单落宫章节连续 3 批零新错误家族才许抽审（机器摇号 20%），每 3 批仍有 1 批全审。跑通判据：连续 3 批零新病根＋100% 一轮通关＋总账数字闭合 → 才开并行线。

## 指路表（报错才翻）

| 要查什么 | 翻哪里 |
|---|---|
| 全部合同细则（工作单/书包/状态/验收/多书） | references/contracts.md |
| v1 完整操作手册（批量提效/断点续跑细节） | references/full-manual.md |
| 知识地图第 2 步怎么做 | references/knowledge-map.md |
| 生成规则、已登记错误家族、审查换挡 | references/generation-rules.md |
| 独立审计怎么写 v3 凭证 | references/terra-audit-prompt.md |
| 抽取 JSON 字段 | references/method-extraction.schema.json ＋ templates/ |
| JH8 排盘事实接入与停判 | references/full-manual.md 的"JH8 排盘事实接入"节 |
| 回填 635 条 step_hash | scripts/backfill_step_hash.py 文件头说明 |
| 本轮拆网定案原文（22 条 Q 号） | 仓库根《拆网定案_v2升级_20260820》 |
