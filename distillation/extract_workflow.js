export const meta = {
  name: 'bphs97-extract',
  description: 'BPHS97 抽取：一批一个 agent，读完本批全部原文写成方法卡并自验通过',
  phases: [
    { title: '抽取', detail: '一批一个 agent；反复跑 check_fragment.py 直到通过' },
  ],
}

// 一批一个 agent。原先按分组派（一批 2~5 个），加上装配 agent 与 6 个审计 agent，
// 一批要 9~12 个 agent，实测第 21~23 章 18 个 agent 烧掉 212 万 token 只做了 39 条原文。
// 装配是跑脚本，主窗口自己 Bash 跑就行，不该占一个 agent。
const REPO = '/home/user/zpdaohang'
const BATCHES = args?.batches
if (!Array.isArray(BATCHES) || !BATCHES.length) {
  throw new Error('必须通过 args.batches 传入：[{label, groups, topic}]')
}

const RULES = `
你是判断方法蒸馏窗口的抽取员。任务：把 BPHS 97 章版（R. Santhanam 英译）的正式原文原子，
抽成严格符合 schema 的"判断方法"结构化 JSON，将来给 RAG（查原文系统）当路标。

## 开工必读（两份都要完整读，规则以它们为准）
1. ${REPO}/distillation/抽取规则_批量版.md
2. ${REPO}/distillation/事实键命名规范.md

## 标准样例（已通过生成器强校验，照这个形状写）
${REPO}/distillation/EXAMPLE_METHOD.json

## 字段合同
${REPO}/book-to-judgment-navigation/references/method-extraction.schema.json

## 绝对禁止
- 禁止修改、复述、改写任何原文；exact_text 是冻结内容
- 禁止编造原文里没有的条件、结果、数值、时间或行星
- 禁止把一条原文的结论扩大成通则
- 禁止占位事实（source_*、choice_*、"原文事实已取得"等）
- **禁止比照别处补出原文没有的分支**（第 1 批栽过：原文阴阳两侧本来就不对称，
  有人以为"不对称是遗漏"补了个宫主分支，被审计判为"多说"）
- **禁止靠护栏措辞给原文未定的指代做隐性绑定**（第 2 批栽过：原文只写 the natal Lord，
  方法写"不得当成上升主之外的别的宫主"，净效果等于锁死成上升主）
- **禁止替原文定义它没写的东西**（第 4 批栽过："In a contrary situation" 原文没说
  什么算相反情形，方法把它接成前句条件的逻辑否定，等于替原文定死）
- **own Rāśi 是本星座（行星自己主管的星座），不是"本宫"**；本书里"宫"对应 Bhava。
  写成"本宫"就换了一张查询——七宫主落自己主管的星座 ≠ 七宫主落七宫。

## 你的输入：本批全部原文
目录 ${REPO}/distillation/_local/batches/BATCH_LABEL/groups/
先 ls 看有哪几组，逐个读完所有 *.json——那是本批全部原文，一条都不能漏。

## 交付方式（必须自验通过才算完成）
1. 把 methods 数组（纯数组，不要外层对象）按组写到
   ${REPO}/distillation/_local/batches/BATCH_LABEL/fragments/<组名>.json
   已存在的组文件说明上一轮已抽完，跳过它，只补没有的组。
2. 每写完一组就自验，直到 passed 为 true：
   cd ${REPO} && PYTHONUTF8=1 python3 distillation/check_fragment.py <该组文件>
   报错就按提示改再跑。常见报错都是硬约束没满足。
   **分支仿真报错**（"无法构造所有分支都不满足的事实"）的意思是：这个选择组里的分支
   互相穷尽了，机器造不出一个都不命中的盘。通常是把"必然二选一"的枚举（如顺行/逆行）
   写成了条件分支——改成基座事实（"本盘该运的推进方向是哪一个"）再由分支判断。
3. 通过后自己复核：本批每条原子都被引用了吗？语义上的"或"都拆成分支了吗？
   长偈拆够步骤了吗？有没有把原文没有的话写进最小意思？
   跨偈承接（本偈没写落宫、前提来自上一偈）写进 context_reference／context_bindings 了吗？
   ——这两个字段会随步骤进交付件，绑错或该绑没绑，审计会打回。
4. **没有判断规则的原文**（纯过渡句、章节引言、收尾告诫、纯知识罗列）不要硬做成方法，
   写进 ${REPO}/distillation/_local/batches/BATCH_LABEL/knowledge_only.json：
   {"atoms":[{"evidence_atom_id":"…","reason":"…","semantic_class":"foundational_knowledge","disposition":"knowledge_only"}]}
   不要去改全局的 KNOWLEDGE_ONLY_ATOMS.json。
5. 返回 JSON：{"batch","groups_written","methods","steps","atoms_covered","knowledge_only","notes"}
   notes 写拆分依据、争议点、没把握的地方——审计会重点看这些。

## 本批
批次：BATCH_LABEL
主题（章名以原子自带 chapter_title 为准，本行仅供定位）：BATCH_TOPIC
方法编号用 "ch<章号>-v<偈号>-<英文短标签>" 全小写连字符，全批唯一。
`

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['batch', 'groups_written', 'methods', 'steps', 'atoms_covered', 'knowledge_only', 'notes'],
  properties: {
    batch: { type: 'string' },
    groups_written: { type: 'array', items: { type: 'string' } },
    methods: { type: 'integer' }, steps: { type: 'integer' },
    atoms_covered: { type: 'integer' }, knowledge_only: { type: 'integer' },
    notes: { type: 'string' },
  },
}

phase('抽取')
log(`抽取 ${BATCHES.length} 批，一批一个 agent：${BATCHES.map(b => b.label).join('、')}`)

const results = await parallel(BATCHES.map(batch => () =>
  agent(
    RULES.replace(/BATCH_LABEL/g, batch.label).replace(/BATCH_TOPIC/g, batch.topic || '')
      + (batch.note ? `\n## 本批修理说明（先读，带着问题去改）\n${batch.note}\n` : ''),
    { label: `抽取:${batch.label}`, phase: '抽取', schema: SCHEMA }
  )
))

return { batches: results.filter(Boolean) }
