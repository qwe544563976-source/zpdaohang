export const meta = {
  name: 'bphs97-batch-extraction',
  description: 'BPHS97 单批并行抽取：按批量版规则产出 schema 合规方法候选并各自自验通过',
  phases: [
    { title: '抽取', detail: '分组并行抽取，每组跑 check_fragment.py 自验至通过' },
  ],
}

const REPO = '/home/user/zpdaohang'
const BATCH = args?.batch
if (!BATCH) throw new Error('必须通过 args.batch 传入批次标签，例如 ch17-18')
const GROUPS = args?.groups
if (!Array.isArray(GROUPS) || !GROUPS.length) throw new Error('必须通过 args.groups 传入分组名单')
const TOPIC = args?.topic || ''

const RULES = `
你是判断方法蒸馏窗口的抽取员。任务：把 BPHS 97 章版（R. Santhanam 英译）的正式原文原子，
抽成严格符合 schema 的"判断方法"结构化 JSON，将来给 RAG（查原文系统）当路标。

## 开工必读（两份都要完整读，规则以它们为准）
1. ${REPO}/distillation/抽取规则_批量版.md ——硬约束、四路查询正反教材、软约束（条数会增补，以文件为准）
2. ${REPO}/distillation/事实键命名规范.md ——事实键三条铁律、16 个句式模板、译名红线

## 标准样例（已通过生成器强校验，照这个形状写）
${REPO}/distillation/EXAMPLE_METHOD.json

## 字段合同
${REPO}/book-to-judgment-navigation/references/method-extraction.schema.json

## 绝对禁止
- 禁止修改、复述、改写任何原文；exact_text 是冻结内容
- 禁止编造原文里没有的条件、结果、数值、时间或行星
- 禁止把一条原文的结论扩大成通则
- 禁止占位事实（source_*、choice_*、"原文事实已取得"等）
- **禁止比照别处补出原文没有的分支**——第一批就栽在这上面：
  原文阴性侧写 Lord＋occupied、阳性侧只写 Grahas＋Rāśis，两侧本来就不对称，
  有人以为"不对称是遗漏"补了个宫主分支，被审计判为"多说"。原文写什么就是什么。

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
   ——这两个字段现在会随步骤进交付件，绑错或该绑没绑，审计会 REJECT。
4. **没有判断规则的原文**（纯过渡句、章节引言、收尾告诫）不要硬做成方法，
   写进 ${REPO}/distillation/_local/batches/${BATCH}/knowledge_only.json：
   {"atoms":[{"evidence_atom_id":"…","reason":"…","semantic_class":"foundational_knowledge","disposition":"knowledge_only"}]}
   **不要去改全局的 KNOWLEDGE_ONLY_ATOMS.json**——几个组并行会抢同一个文件。
5. 返回 JSON：{"group","out_file","methods","steps","atoms_covered","notes"}
   notes 写你的拆分依据、遇到的争议、没把握的地方——审计会重点看这些。
`

phase('抽取')

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['group', 'out_file', 'methods', 'steps', 'atoms_covered', 'notes'],
  properties: {
    group: { type: 'string' }, out_file: { type: 'string' },
    methods: { type: 'integer' }, steps: { type: 'integer' },
    atoms_covered: { type: 'integer' }, notes: { type: 'string' },
  },
}

log(`批次 ${BATCH}：${GROUPS.length} 组并行抽取`)

const results = await parallel(GROUPS.map(g => () =>
  agent(
    RULES
      .replace(/GROUP_FILE/g, `${REPO}/distillation/_local/batches/${BATCH}/groups/${g}.json`)
      .replace(/OUT_FILE/g, `${REPO}/distillation/_local/batches/${BATCH}/fragments/${g}.json`)
      + `\n\n## 本批主题\n${TOPIC}\n批次：${BATCH}　组名：${g}\n`
      + `方法编号用 "ch<章号>-v<偈号>-<英文短标签>" 全小写连字符，全批唯一。\n`,
    { label: `extract:${BATCH}/${g}`, phase: '抽取', schema: SCHEMA }
  )
))

return { batch: BATCH, results: results.filter(Boolean) }
