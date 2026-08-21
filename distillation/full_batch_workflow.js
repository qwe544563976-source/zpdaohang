export const meta = {
  name: 'bphs97-full-batch',
  description: 'BPHS97 整批端到端：并行抽取→装配机检→第一轮三视角审核；多批流水线重叠推进',
  phases: [
    { title: '抽取', detail: '每组一个 agent，各自跑 check_fragment.py 自验至通过' },
    { title: '装配', detail: '合并片段跑唯一生成器与 --require-v2，顺带切审计分片包' },
    { title: '审核', detail: '分片逐字对照原文 + 实用性 + 完整性' },
  ],
}

// 用 pipeline 而不是 parallel：第 N 批在审核时第 N+1 批已经在抽取，
// 不设批间栅栏。整本书 69 批，栅栏的空转代价是实打实的。
const REPO = '/home/user/zpdaohang'
const BATCHES = args?.batches
if (!Array.isArray(BATCHES) || !BATCHES.length) {
  throw new Error('必须通过 args.batches 传入批次数组：[{label, batch_id, groups, topic}]')
}
const SHARDS = args?.shards || 5

const EXTRACT_RULES = `
你是判断方法蒸馏窗口的抽取员。任务：把 BPHS 97 章版（R. Santhanam 英译）的正式原文原子，
抽成严格符合 schema 的"判断方法"结构化 JSON，将来给 RAG（查原文系统）当路标。

## 开工必读（两份都要完整读，规则以它们为准）
1. ${REPO}/distillation/抽取规则_批量版.md ——硬约束、四路查询正反教材、软约束
2. ${REPO}/distillation/事实键命名规范.md ——事实键三条铁律、句式模板、译名红线

## 标准样例（已通过生成器强校验，照这个形状写）
${REPO}/distillation/EXAMPLE_METHOD.json

## 字段合同
${REPO}/book-to-judgment-navigation/references/method-extraction.schema.json

## 绝对禁止
- 禁止修改、复述、改写任何原文；exact_text 是冻结内容
- 禁止编造原文里没有的条件、结果、数值、时间或行星
- 禁止把一条原文的结论扩大成通则
- 禁止占位事实（source_*、choice_*、"原文事实已取得"等）
- **禁止比照别处补出原文没有的分支**——第 1 批就栽在这上面：
  原文阴性侧写 Lord＋occupied、阳性侧只写 Grahas＋Rāśis，两侧本来就不对称，
  有人以为"不对称是遗漏"补了个宫主分支，被审计判为"多说"。原文写什么就是什么。
- **禁止靠护栏措辞给原文未定的指代做隐性绑定**——第 2 批栽在这上面：
  原文只写 the natal Lord、全书无界定，方法写"不得当成上升主之外的别的宫主"，
  净效果等于锁死成上升主。未定就三处一致地停判。

## 你的输入
本组原文（含 exact_text、pdf_pages、context_before/after、prev/next 编号）：GROUP_FILE

## 交付方式（必须自验通过才算完成）
1. 把 methods 数组（纯数组，不要外层对象）写到 OUT_FILE
2. 反复自验直到 passed 为 true：
   cd ${REPO} && PYTHONUTF8=1 python3 distillation/check_fragment.py OUT_FILE
   报错就按提示改再跑。常见报错都是硬约束没满足。
3. 通过后自己复核：本组每条原子都被引用了吗？语义上的"或"都拆成分支了吗？
   长偈拆够步骤了吗？有没有把原文没有的话写进最小意思？
   跨偈承接（本偈没写落宫、前提来自上一偈）有没有写进 context_reference／context_bindings？
   ——这两个字段会随步骤进交付件，绑错或该绑没绑，审计会 REJECT。
4. **没有判断规则的原文**（纯过渡句、章节引言、收尾告诫）不要硬做成方法，
   写进 KNOWLEDGE_ONLY_FILE：
   {"atoms":[{"evidence_atom_id":"…","reason":"…","semantic_class":"foundational_knowledge","disposition":"knowledge_only"}]}
   **不要去改全局的 KNOWLEDGE_ONLY_ATOMS.json**——几个组并行会抢同一个文件。
5. 返回 JSON：{"group","out_file","methods","steps","atoms_covered","notes"}
   notes 写你的拆分依据、遇到的争议、没把握的地方——审计会重点看这些。
`

const EXTRACT_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['group', 'out_file', 'methods', 'steps', 'atoms_covered', 'notes'],
  properties: {
    group: { type: 'string' }, out_file: { type: 'string' },
    methods: { type: 'integer' }, steps: { type: 'integer' },
    atoms_covered: { type: 'integer' }, notes: { type: 'string' },
  },
}

const ASSEMBLE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['passed', 'batch_id', 'target', 'methods', 'steps', 'step_ids', 'errors', 'notes'],
  properties: {
    passed: { type: 'boolean' },
    batch_id: { type: 'string' }, target: { type: 'string' },
    methods: { type: 'integer' }, steps: { type: 'integer' },
    step_ids: { type: 'array', items: { type: 'string' } },
    errors: { type: 'array', items: { type: 'string' } },
    notes: { type: 'string' },
  },
}

const AUDIT_COMMON = `
你没有参与本批任何方法的生成。你的职责只有一个：找问题。不要修改任何文件。

## 机器已经查过的，严禁重查（重查即越权）
JSON 格式、字段完整性、逐字短引是否为 exact_text 子串、PDF 页码是否一致、
分支通电仿真、占位事实黑名单、空话复读、状态跳级、步骤指纹算法、批内译名漂移。
验证器已经全部拦过了，你重查是浪费。

## 你要查的是机器查不了的：语义。关键动作：**打开原文，逐字对照**。
- 已登记错误家族：${REPO}/book-to-judgment-navigation/references/generation-rules.md
- 冻结原文原子（唯一真相，只读）：${REPO}/distillation/_local/evidence_atoms.jsonl
`

const CORRECTNESS = `${AUDIT_COMMON}
# 你的角色：对照原文的正确性审计员

## 你的分片包（该看的东西已预切好，直接读这一个文件）
BUNDLE_PATH
里面有：分给你的每一步的完整配方、所属方法的意图与查询词、
该步引用的**每一条原子的 exact_text 全文**（逐字复制，未摘要未截断）、该步的高风险词差异表。
包里记了冻结文件的 sha256，你随时可以回冻结文件核对。

对每个步骤：读原子 exact_text 全文（不是只读短引），逐项对照回答：
- **有没有多说**：\`minimum_supported_claim\` 里每个意思，原文都真说了吗？加了推论/程度/时间/对象没有？
- **有没有漏说**：原文写明的前提，条件树里都有吗？（例："且受吉星相照"漏了就 REJECT）
- **条件结构对不对**：原文的"或"拆成分支了吗？"即使…仍然"被写成必须满足的 if 了吗？
  注意 "or in X"（承接同一个 if）与 "or, if X"（独立条件句）的差别，它决定 while 从句管几支。
- **取消/缓解/补救写反没有**：原文说"可化解"，方法当成风险条件了吗？
- **指代丢没丢**：such / this / the said / 前一偈的条件，还在不在？
- **承接绑对没有**：本偈没写的前提若来自别的偈，\`context_bindings\` 指向的原子对不对？该绑没绑？
- **时间限定对不对**：\`time_scope.label\` 与原文一致吗？原文没有时间限定的应为 kind=none。
- **范围放大没有**：单条断语被写成通则了吗？\`applicability_scope\` 诚实吗？
- **护栏有没有做隐性绑定**：原文未定的指代（例 the natal Lord），
  \`forbidden_extensions\` 是不是用"不得当成 X 之外的别的…"把它锁死成 X 了？那是原文没给的授权。
- **数值和专名**：年龄、年数、人数、行星名、宫位名、分盘名与原文完全一致吗？

## 高风险词逐词确认（三道手铐）
分片包里每步有一张差异表。对表上**每一个词**给单选 accept 或 reject。
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

const USEFULNESS_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['verdict', 'summary', 'blocking_gaps', 'improvements', 'good_examples'],
  properties: {
    verdict: { enum: ['USABLE', 'NEEDS_WORK'] },
    summary: { type: 'string' },
    blocking_gaps: { type: 'array', items: { type: 'string' } },
    improvements: { type: 'array', items: { type: 'string' } },
    good_examples: { type: 'array', items: { type: 'string' } },
  },
}

const COMPLETENESS_SCHEMA = {
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
}

log(`整本书批量：本次 ${BATCHES.length} 批流水线推进 —— ${BATCHES.map(b => b.label).join('、')}`)

const results = await pipeline(
  BATCHES,

  // 阶段一：本批各组并行抽取
  (batch) => parallel(batch.groups.map(g => () =>
    agent(
      EXTRACT_RULES
        .replace(/GROUP_FILE/g, `${REPO}/distillation/_local/batches/${batch.label}/groups/${g}.json`)
        .replace(/OUT_FILE/g, `${REPO}/distillation/_local/batches/${batch.label}/fragments/${g}.json`)
        .replace(/KNOWLEDGE_ONLY_FILE/g, `${REPO}/distillation/_local/batches/${batch.label}/knowledge_only.json`)
        + `\n\n## 本批主题（章名以原子自带 chapter_title 为准，本行仅供定位）\n${batch.topic || ''}\n`
        + `批次：${batch.label}　组名：${g}\n`
        + `方法编号用 "ch<章号>-v<偈号>-<英文短标签>" 全小写连字符，全批唯一。\n`,
      { label: `抽取:${batch.label}/${g}`, phase: '抽取', schema: EXTRACT_SCHEMA }
    )
  )),

  // 阶段二：装配 + 机检（一个 agent 跑脚本，不做判断）
  (extracted, batch) => agent(
    `你只做一件事：把已抽取的片段装配成正式批次并跑机器验收。不要修改任何片段内容。

cd ${REPO} && PYTHONUTF8=1 python3 distillation/make_batch.py \\
  --batch-id ${batch.batch_id} \\
  --target distillation/bphs-97/batches/${batch.batch_id} \\
  --scope distillation/_local/batches/${batch.label}/scope.json \\
  --fragments distillation/_local/batches/${batch.label}/fragments

它会打印一份 JSON 报告。要求：
- validate.passed 必须为 true、validate.errors 必须为空。若失败，把 errors 原样带回，
  **不要自己改片段去凑通过**——那是抽取和审计的职责，你只报告。
- 报告里的 term_drift.passed 若为 false，把漂移术语写进 notes。
- 跑完后取出全部步骤编号：
  python3 -c "import json;d=json.load(open('distillation/bphs-97/batches/${batch.batch_id}/references/navigation/method-recipes.json'));print(json.dumps([s['step_id'] for m in d['methods'] for s in m['steps']]))"

返回 JSON：{"passed","batch_id","target","methods","steps","step_ids","errors","notes"}
target 写绝对路径 ${REPO}/distillation/bphs-97/batches/${batch.batch_id}`,
    { label: `装配:${batch.label}`, phase: '装配', schema: ASSEMBLE_SCHEMA }
  ),

  // 阶段三：三视角审核（分片包已由 make_batch 切好）
  (built, batch) => {
    if (!built || !built.passed || !built.step_ids?.length) {
      return { batch: batch.label, built, audit: null, note: '装配未通过，跳过审核' }
    }
    const ids = built.step_ids
    const size = Math.ceil(ids.length / SHARDS)
    const shards = []
    for (let i = 0; i < ids.length; i += size) shards.push(ids.slice(i, i + size))

    const correctness = parallel(shards.map((shard, index) => () =>
      agent(
        CORRECTNESS
          .replace('SHARD_STEP_IDS', shard.map(id => `- ${id}`).join('\n'))
          .replace('BUNDLE_PATH', `${built.target}/validation/audit-bundles/shard-${index + 1}.json`),
        { label: `对照原文:${batch.label}/${index + 1}`, phase: '审核', schema: ENTRY_SCHEMA }
      )
    ))

    const usefulness = agent(`${AUDIT_COMMON}
# 你的角色：实用性审计员——这批能不能真当 RAG 路标用？

方法配方：${built.target}/references/navigation/method-recipes.json
主题与四路查询：${built.target}/references/navigation/query-recipes.json

逐个方法检查：
1. **user_intents 是不是真人会问的话**？"我会有几个孩子"是真人话；"五宫主落宫效果判定"不是。
2. **四路查询词能不能真检索到东西**？support/counter/boundary/method：
   是不是只把标题复述了一遍？反例路是真找反例还是又一条支持路？边界路指向真实边界主题吗？
   同一族方法的反例路是不是塌成同几句通用消灾语（问什么都取回同一批文档）？
3. **required_facts 是不是排盘能算出来的**？算不出来的事实等于这个方法永远停判。
   若方法依赖"吉星/凶星/有力/中性行星"这类判准，四路词里有没有一条能查到 BPHS 自己的定义？
   （现成的：吉凶星 ch03:v11、六力 ch27:v0.1、中性行星 ch03:v19、女命 ch80:v1）
4. **停判条件有没有用**？缺什么、怎么说，用户看得懂吗？
5. **方法粒度合不合适**？管太多事，还是切太碎（互相依赖却没声明依赖）？
6. **主题路由会不会串台**？特别注意原文自带的错位：某章里的偈讲的其实是别的宫。
   方法如实标注了，还是硬归到本章主题？
7. **男命口径的方法有没有给女命留改道线索**？（断语主语是妻/配偶的才需要；纯时间条不需要）

## 交付
返回 JSON：{"verdict":"USABLE|NEEDS_WORK","summary":"一句话结论",
"blocking_gaps":[真的会让 RAG 用不了的问题，每条写清方法编号和理由],
"improvements":[能用但该改进的，按重要性排序],"good_examples":[做得对的例子，给后续批次当样板]}`,
      { label: `实用性:${batch.label}`, phase: '审核', schema: USEFULNESS_SCHEMA })

    const completeness = agent(`${AUDIT_COMMON}
# 你的角色：完整性审计员——对照原文查漏

本批原文分组目录：${REPO}/distillation/_local/batches/${batch.label}/groups
先 ls 这个目录看有哪几组，然后逐个读完目录下所有 *.json——那是本批全部原文。
方法配方：${built.target}/references/navigation/method-recipes.json
本批已标 knowledge_only 的原子：${REPO}/distillation/_local/batches/${batch.label}/knowledge_only.json（可能不存在）

逐条原文过一遍，回答：
1. **有没有规则被漏掉**？一条原文里若有 3 组独立的"条件→结果"，方法是不是只做了 2 组？
   长偈（含多个偈号、正文特别长的）尤其要数清楚。把你数出的规则条数与实际步骤数对照。
2. **拆分是否恰当**？该拆的没拆（多条独立规则挤在一步）、不该拆的拆了（一条完整条件-结果被切成两半）？
   同一批里对同类句式（例：两个交点共用一个结果）有没有前后用了相反口径？
3. **有没有原文根本没有判断规则却被做成了方法**？纯过渡句应标 knowledge_only。
4. **版本注记有没有保住**？"(some texts read, as ...)" 这类版本异文，方法如实保留还是擅自选了一个？
5. **有没有原文异常该回上游登记**？排印讹字、偈号区间重叠、正文缺失等。
6. **本批每一条原子逐条给去向**：做成方法 / 应标 knowledge_only / 有规则但漏做。

## 交付
返回 JSON：{"verdict":"COMPLETE|GAPS_FOUND","summary":"一句话结论",
"missing_rules":[漏掉的规则，写清原子编号、原文片段、漏了什么],
"wrong_splitting":[拆分不当的，写清方法编号和理由],
"should_be_knowledge_only":[没有判断规则却被做成方法的原子编号与方法编号],
"atom_coverage":[{"evidence_atom_id","rules_in_text","steps_made","note"}]}`,
      { label: `完整性:${batch.label}`, phase: '审核', schema: COMPLETENESS_SCHEMA })

    return Promise.all([correctness, usefulness, completeness]).then(([shardResults, use, comp]) => {
      const alive = shardResults.filter(Boolean)
      const entries = alive.flatMap(r => r.entries || [])
      const rejected = entries.filter(e => e.verdict === 'REJECT')
      log(`${batch.label}：${built.methods} 方法 ${built.steps} 步 ｜ 回收 ${entries.length}/${ids.length} 判定，REJECT ${rejected.length} ｜ 实用性 ${use?.verdict} 完整性 ${comp?.verdict}`)
      return {
        batch: batch.label,
        batch_id: built.batch_id,
        target: built.target,
        methods: built.methods,
        steps: built.steps,
        expected_steps: ids.length,
        returned_steps: entries.length,
        rejected: rejected.map(e => ({ step_id: e.step_id, finding: e.finding })),
        entries,
        suspected_new_families: alive.flatMap(r => r.suspected_new_families || []),
        usefulness: use,
        completeness: comp,
      }
    })
  }
)

return { batches: results.filter(Boolean) }
