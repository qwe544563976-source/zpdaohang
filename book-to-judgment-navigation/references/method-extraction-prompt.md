# 判断方法结构化抽取提示词

你只负责 Stage A：读取工作单允许范围内的正式原文原子，输出一个 JSON 对象。禁止输出 Markdown、解释、代码围栏或 JSON 之外的文字。

输出必须通过同目录的 `method-extraction.schema.json`：

1. 每一步分别写条件树、最小意思、时间范围、取消／缓解关系、让步条件和前文承接。
2. OR 只能写进 `alternative_groups`；主 `condition_logic` 禁止出现 OR。
3. `claim_terms` 必须同时给出条件词和结果词，每个词分别保存“逐字短引中的词”和“最小意思中的中文对应词”。
4. 补救事实必须标为 `remedy_condition`，只能进入 `exception_relations`，不能进入风险成立条件。
5. “即使……也……”中的有利条件写进 `concession_conditions`，不能写成必须满足的前提。
6. 原文含 such、this、the above、fully 等承接时，设置 `context_reference=true`并绑定实际前置原文编号。
7. 不读取 PDF、book.md 或 pages.jsonl，不补写、合并、拆分或修改原文。
8. 找不到直接原文支持的字段就不要生成该步骤；不要用占星常识补齐。

输出后必须交给：

```text
python scripts/build_methods.py \
  --extraction <AI抽取.json> \
  --accepted-package <正式accepted-package.json> \
  --output <新目录>/references/navigation/method-recipes.json
```

任何 Schema 错误或语义结构错误都由程序直接终止，不允许人工绕过后继续装配。
