export const meta = {
  name: 'bphs97-batch-audit',
  description: 'BPHS97 批次三视角审核：逐字对照原文的正确性、能否当路标的实用性、有无漏规则的完整性',
  phases: [
    { title: '对照原文审计', detail: '分片逐步骤打开原子 exact_text 比对，只找问题' },
    { title: '实用性与完整性', detail: '这批能不能真当 RAG 路标用；对照 41 条原文查漏和拆分是否恰当' },
  ],
}

const REPO = '/home/user/zpdaohang'
const TARGET = args?.target
const ATOMS = `${REPO}/distillation/_local/evidence_atoms.jsonl`
const BATCH = args?.batch || ''
// 第一批的分组落在 _local/groups；批量起用 _local/batches/<批次>/groups
const GROUPS = BATCH ? `${REPO}/distillation/_local/batches/${BATCH}/groups`
                     : `${REPO}/distillation/_local/groups`

if (!TARGET) throw new Error('必须通过 args.target 传入批次目录')
const stepIds = args?.step_ids
if (!Array.isArray(stepIds) || !stepIds.length) throw new Error('必须通过 args.step_ids 传入应审步骤名单')

const COMMON = `
你没有参与本批任何方法的生成。你的职责只有一个：找问题。不要修改任何文件。

## 机器已经查过的，严禁重查（重查即越权）
JSON 格式、字段完整性、逐字短引是否为 exact_text 子串、PDF 页码是否一致、
分支通电仿真、占位事实黑名单、空话复读、状态跳级、步骤指纹算法。
验证器已经全部拦过了，你重查是浪费。

## 你要查的是机器查不了的：语义
关键动作：**打开原文，逐字对照**。
- 冻结原文原子（只读，禁止修改）：${ATOMS}
  每行一条 JSON，用 evidence_atom_id 定位，读它的 exact_text 全文。
- 方法配方（唯一机器真相）：${TARGET}/references/navigation/method-recipes.json
- 生成报告（含 high_risk_terms 差异表）：${TARGET}/validation/build-methods-report.json
- 已登记错误家族：${REPO}/book-to-judgment-navigation/references/generation-rules.md
`

const CORRECTNESS = `${COMMON}
# 你的角色：对照原文的正确性审计员

对分给你的每一个步骤，按这个顺序做：
1. 从 method-recipes.json 找到该步骤，记下它引用的 evidence_atom_id；
2. 去 evidence_atoms.jsonl 把那条原子的 **exact_text 全文**读出来（不是只读短引）；
3. 把原文和步骤逐项对照，回答下面每一条：

- **有没有多说**：\`minimum_supported_claim\` 里的每一个意思，原文都真的说了吗？
  有没有加进原文没有的推论、程度、时间、对象？（这是最常见的私货）
- **有没有漏说**：原文写明的前提条件，条件树里都有吗？
  例：原文要求"且受吉星相照"，方法只写了占据关系 → 漏前提，REJECT。
- **条件结构对不对**：原文的"或"拆成分支了吗？分支之间会不会互相误停？
  原文的"即使…仍然"（even if）有没有被写成必须满足的 if？
- **取消/缓解/补救有没有写反**：原文说"某某可化解"，方法有没有把它当成风险条件？
- **指代有没有丢**：such / this / the said / these two / 前一偈的条件，还在不在？
- **范围有没有被放大**：单条断语被写成通则了吗？\`applicability_scope\` 诚实吗？
- **数值和专名**：年龄、年数、人数、行星名、宫位名、分盘名与原文完全一致吗？
  （重点核对 high_risk_terms 差异表里的每一个词）

## 高风险词逐词确认（三道手铐）
生成报告里每个步骤有一张差异表。对表上**每一个词**给单选 accept 或 reject。
只准针对表上列出的词确认，**严禁在表外自己找映射的茬**。一轮封顶，确认过不翻案。
任何一词 reject，该步骤 verdict 必须 REJECT。

## 判定
每步只给 PASS 或 REJECT，并**原样抄录该步骤的 step_hash**。
REJECT 必须写：异议家族、原文逐字证据、出问题的字段、影响范围。
PASS 只表示"本轮未找到问题"，不得写成"已证明正确"。

## 你负责的步骤（只审这些）
SHARD_STEP_IDS

## 交付
返回 JSON：{"entries":[{"step_id","verdict","step_hash","high_risk_confirmations":{词:accept|reject},"finding"}],
"suspected_new_families":[最多2条,带原文与复现路径],"unchecked_scope":[如实写没查的范围]}
entries 与分给你的步骤一一对应，不多不少。
`

const USEFULNESS = `${COMMON}
# 你的角色：实用性审计员——这批东西能不能真当 RAG 路标用？

老板的目标是："让 RAG 拿着这些方法当导航路标"。你要回答的是：拿到了，真的能用吗？

逐个方法检查：
1. **user_intents 是不是真人会问的话**？"我会有几个孩子"是真人话；
   "五宫主落宫效果判定"不是。有没有该有的问法没写？
2. **四路查询词能不能真检索到东西**？support/counter/boundary/method 四路：
   - 是不是只是把标题复述了一遍？
   - 反例路是不是真的在找反例，还是又一条支持路？
   - 边界路有没有指向真实的边界主题？
3. **required_facts 是不是排盘能算出来的**？例如"四宫是否被四宫主占据"可以算；
   "命主是否命好"算不出来。写不出来的事实等于这个方法永远停判。
4. **停判条件有没有用**？缺什么、怎么说，用户能看懂吗？
5. **方法粒度合不合适**？一个方法管太多事（用户问一句要跑十步）还是切太碎
   （同一条原文被切成互相依赖却没声明依赖的碎片）？
6. **主题路由会不会串台**？例如问"住房"却路由到"五宫子女"的方法。
   注意 ch15 v3 原文本身讲的是 Putr（五宫）主，出现在第 15 章里——
   这种原文自带的错位，方法有没有如实标注，还是硬归到四宫主题？

## 交付
返回 JSON：{"verdict":"USABLE|NEEDS_WORK","summary":"一句话结论",
"blocking_gaps":[真的会让 RAG 用不了的问题，每条写清方法编号和理由],
"improvements":[能用但该改进的，按重要性排序],
"good_examples":[做得对的例子，给后续批次当样板]}
`

const COMPLETENESS = `${COMMON}
# 你的角色：完整性审计员——对照原文查漏

本批的原文分组目录：${GROUPS}／（逐个读完目录下所有 *.json，那是本批全部原文）。
`ls ${GROUPS}` 先看有哪几组。

逐条原文过一遍，回答：
1. **有没有规则被漏掉**？一条原文里如果有 3 组独立的"条件→结果"，方法是不是只做了 2 组？
   长偈（一条原子含多个偈号、正文特别长的）尤其要数清楚。
   把你数出来的规则条数和方法实际做出的步骤数对照，不一致就说清差在哪。
2. **拆分是否恰当**？该拆的没拆（多条独立规则挤在一步）、不该拆的拆了
   （一条完整的条件-结果被切成两半，各自不成立）？
3. **有没有原文根本没有判断规则却被做成了方法**？
   例如纯过渡句"三宫已讲完，现在听四宫"。这类应该标 knowledge_only 而不是做成方法。
   （生成器现在支持 source_records 的 disposition 字段声明非方法去向）
4. **版本注记有没有保住**？原文写 "(some texts read, as ...)" 这类版本异文，
   方法有没有如实保留，还是擅自选了一个？
5. **本批每一条原子逐条给去向**：做成方法 / 应标 knowledge_only / 有规则但漏做。

## 交付
返回 JSON：{"verdict":"COMPLETE|GAPS_FOUND","summary":"一句话结论",
"missing_rules":[漏掉的规则，写清原子编号、原文片段、漏了什么],
"wrong_splitting":[拆分不当的，写清方法编号和理由],
"should_be_knowledge_only":[没有判断规则却被做成方法的原子编号与方法编号],
"atom_coverage":[{"evidence_atom_id":"...","rules_in_text":<你数出的规则条数>,"steps_made":<实际步骤数>,"note":"..."}]}
`

phase('对照原文审计')

const ENTRY_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['entries', 'suspected_new_families', 'unchecked_scope'],
  properties: {
    entries: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['step_id', 'verdict', 'step_hash', 'high_risk_confirmations', 'finding'],
        properties: {
          step_id: { type: 'string' },
          verdict: { enum: ['PASS', 'REJECT'] },
          step_hash: { type: 'string' },
          high_risk_confirmations: { type: 'object', additionalProperties: { enum: ['accept', 'reject'] } },
          finding: { type: 'string' },
        },
      },
    },
    suspected_new_families: { type: 'array', items: { type: 'string' }, maxItems: 2 },
    unchecked_scope: { type: 'array', items: { type: 'string' } },
  },
}

// 第二轮只确认修复：实用性与完整性在第一轮已全批扫过，重跑纯属浪费。
// 实测第一轮 725k tokens、第二轮 709k——步骤从 73 降到 15，token 却几乎没降，
// 就是因为这两个视角每次都全批重看。
const ROUND = args?.round || 1
const SHARDS = args?.shards || 4
const shards = []
const size = Math.ceil(stepIds.length / SHARDS)
for (let i = 0; i < stepIds.length; i += size) shards.push(stepIds.slice(i, i + size))
log(`应审步骤 ${stepIds.length} 个，分 ${shards.length} 片逐字对照原文全审`)

const correctness = await parallel(shards.map((shard, index) => () =>
  agent(CORRECTNESS.replace('SHARD_STEP_IDS', shard.map(id => `- ${id}`).join('\n')),
    { label: `对照原文:${index + 1}/${shards.length}`, phase: '对照原文审计', schema: ENTRY_SCHEMA })
))

const skipWholeBatchLenses = ROUND > 1
if (!skipWholeBatchLenses) phase('实用性与完整性')

const [usefulness, completeness] = skipWholeBatchLenses ? [null, null] : await parallel([
  () => agent(USEFULNESS, {
    label: '实用性:能否当路标', phase: '实用性与完整性',
    schema: {
      type: 'object', additionalProperties: false,
      required: ['verdict', 'summary', 'blocking_gaps', 'improvements', 'good_examples'],
      properties: {
        verdict: { enum: ['USABLE', 'NEEDS_WORK'] },
        summary: { type: 'string' },
        blocking_gaps: { type: 'array', items: { type: 'string' } },
        improvements: { type: 'array', items: { type: 'string' } },
        good_examples: { type: 'array', items: { type: 'string' } },
      },
    },
  }),
  () => agent(COMPLETENESS, {
    label: '完整性:对照原文查漏', phase: '实用性与完整性',
    schema: {
      type: 'object', additionalProperties: false,
      required: ['verdict', 'summary', 'missing_rules', 'wrong_splitting', 'should_be_knowledge_only', 'atom_coverage'],
      properties: {
        verdict: { enum: ['COMPLETE', 'GAPS_FOUND'] },
        summary: { type: 'string' },
        missing_rules: { type: 'array', items: { type: 'string' } },
        wrong_splitting: { type: 'array', items: { type: 'string' } },
        should_be_knowledge_only: { type: 'array', items: { type: 'string' } },
        atom_coverage: { type: 'array', items: { type: 'object' } },
      },
    },
  }),
])

const alive = correctness.filter(Boolean)
const entries = alive.flatMap(r => r.entries || [])
const rejected = entries.filter(e => e.verdict === 'REJECT')

log(`对照原文：回收 ${entries.length}/${stepIds.length} 个判定，REJECT ${rejected.length} 个`)
if (skipWholeBatchLenses) {
  log('第二轮：跳过实用性与完整性全批复核（第一轮已扫过），只确认修复')
} else {
  log(`实用性：${usefulness?.verdict} ｜ 完整性：${completeness?.verdict}`)
}

return {
  expected_steps: stepIds.length,
  returned_steps: entries.length,
  rejected: rejected.map(e => ({ step_id: e.step_id, finding: e.finding })),
  entries,
  suspected_new_families: alive.flatMap(r => r.suspected_new_families || []),
  unchecked_scope: alive.flatMap(r => r.unchecked_scope || []),
  usefulness,
  completeness,
}
