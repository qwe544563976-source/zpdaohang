export const meta = {
  name: 'bphs97-independent-semantic-audit',
  description: 'BPHS97 批次独立语义审计：分片全审后合成 independent-semantic-audit/v3 报告',
  phases: [
    { title: '分片审计', detail: '未参与生成的审计员逐步骤只找问题，抄 step_hash，逐词确认高风险词' },
    { title: '合成报告', detail: '把分片判定机械拼成一份 v3 报告并落盘' },
  ],
}

const REPO = '/home/user/zpdaohang'
const TARGET = args?.target || `${REPO}/distillation/bphs-97/batches/BPHS97_ch14-16_siblings-home-children_20260820_run01`
const SHARDS = args?.shards || 4

const AUDIT_RULES = `
你是**独立语义审计员**，没有参与本批任何方法的生成。你的唯一职责是找问题。

## 只准做三件事
1. 勾选已登记的错误家族（读 ${REPO}/book-to-judgment-navigation/references/generation-rules.md）；
2. 判断"这一步有没有原文支持不了的私货"；
3. 附栏报疑似新错误家族——最多 2 条，必须带原文与复现路径。

## 机器已经查过的，严禁重查（重查即越权）
格式、字段完整性、逐字引文是否为 exact_text 子串、PDF 页码、分支通电仿真、占位事实、
空话复读、状态跳级、步骤内容指纹的算法正确性。这些验证器已经拦过了。

## 逐条核查（这才是你的活）
- \`minimum_supported_claim\` 是否只表达逐字短引**直接支持**的最小意思？有没有加进原文没有的推论？
- 条件是否漏了原文写明的前提？（例：原文要求"且受吉星相照"，方法只写了占据关系）
- OR 是否保留为可选分支？未选中的分支缺事实时，会不会误停已经成立的分支？
- 取消、缓解、补救、反例、相位方向有没有写反？
- "even if"（即使）有没有被改写成必须满足的 "if"？
- such / this / the said / these two 等指代，前置条件是否保住了？
- 有没有把案例、译注、单条结论升级成通用规则？
- 数值、年龄、行星名、宫位名、分盘名是否与原文一致？（这是重点，见下）

## 高风险词逐词确认（戴三道手铐）
生成报告里每个步骤有一张 \`high_risk_terms\` 差异表，列出该步骤命中的专名／数值／单位／时间词
及其映射（mapped_quote → mapped_claim）。你必须：
1. 对表上**每一个词**给出单选：\`accept\`（映射正确）或 \`reject\`（映射错了，例如把 Shukr 写成金星以外的东西、
   把 32nd year 映成别的年份、把 six 写成别的数）；
2. **只准针对表上列出的词做确认，严禁在表外自己找映射的茬**；
3. 一轮封顶：确认过就不再翻案。
任何一个词被 reject，该步骤的 verdict 必须是 REJECT。

## 判定
每个步骤只给 \`PASS\` 或 \`REJECT\`，并且必须**原样抄录该步骤在 method-recipes.json 里的 step_hash**。
- REJECT 必须写：异议家族、原文证据（原子编号＋逐字短引）、出问题的配方字段、影响范围。
- PASS 只能表示"本轮未找到问题"，不得表述成"已经证明正确"。

## 你的输入
- 方法配方（唯一机器真相）：${TARGET}/references/navigation/method-recipes.json
- 生成报告（含 high_risk_terms 差异表与 audit_step_ids）：${TARGET}/validation/build-methods-report.json
- 冻结原文原子（比对逐字原文用，只读，禁止修改）：${REPO}/distillation/_local/evidence_atoms.jsonl
- 已登记错误家族：${REPO}/book-to-judgment-navigation/references/generation-rules.md

## 你负责的步骤
只审下面这一片步骤编号，别的步骤不要碰：
SHARD_STEP_IDS

## 交付
返回 JSON：{"entries":[{"step_id":"...","verdict":"PASS|REJECT","step_hash":"<原样抄录>",
"high_risk_confirmations":{"<词>":"accept|reject"},"finding":"REJECT 时写清异议家族/原文证据/字段/影响；PASS 时写本轮未找到问题"}],
"suspected_new_families":["最多 2 条，带原文与复现路径；没有就空数组"],
"unchecked_scope":["你没能检查的范围，如实写"]}
entries 必须与分给你的步骤一一对应，不多不少。
`

phase('分片审计')

const ENTRY_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['entries', 'suspected_new_families', 'unchecked_scope'],
  properties: {
    entries: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
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

const stepIds = args.step_ids
if (!Array.isArray(stepIds) || !stepIds.length) {
  throw new Error('必须通过 args.step_ids 传入机器指定的应审步骤名单')
}

const shards = []
const size = Math.ceil(stepIds.length / SHARDS)
for (let i = 0; i < stepIds.length; i += size) shards.push(stepIds.slice(i, i + size))

log(`应审步骤 ${stepIds.length} 个，分 ${shards.length} 片全审`)

const shardResults = await parallel(shards.map((shard, index) => () =>
  agent(
    AUDIT_RULES.replace('SHARD_STEP_IDS', shard.map(id => `- ${id}`).join('\n')),
    { label: `audit:shard-${index + 1}`, phase: '分片审计', schema: ENTRY_SCHEMA }
  )
))

phase('合成报告')

const alive = shardResults.filter(Boolean)
const entries = alive.flatMap(r => r.entries || [])
const families = alive.flatMap(r => r.suspected_new_families || [])
const unchecked = alive.flatMap(r => r.unchecked_scope || [])
const rejected = entries.filter(e => e.verdict === 'REJECT').map(e => e.step_id)

log(`分片回收 ${entries.length}/${stepIds.length} 个判定，其中 REJECT ${rejected.length} 个`)

return {
  shards: shards.length,
  expected_steps: stepIds.length,
  returned_steps: entries.length,
  rejected_step_ids: rejected,
  entries,
  suspected_new_families: families,
  unchecked_scope: unchecked,
}
