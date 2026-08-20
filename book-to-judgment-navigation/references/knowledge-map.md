# 流水线第 2 步 · 已验收证据知识地图（Accepted Evidence Knowledge Map）

> v2 升级版说明：本文即原 `book-to-skill` SKILL.md 的 "Mode 5. Accepted Evidence Knowledge Map"，按拆网定案 Q19 整段搬入本技能，作为固定工作链第 2 步。它只读冻结原文原子，不需要 book-to-skill 的提取器；`book-to-skill` 已恢复原厂，不再承担本职责。除下列两处外内容与原文一致：出处标注改为本技能；唯一生成入口路径从 `cangjie-skill/scripts/build_methods.py` 改为本技能 `scripts/build_methods.py`。

**触发：** 收到 `accepted-package.json（已验收书包凭证）`，或收到 `artifact_scope` 为 `PILOT_TEMP` 的试验夹具工作单，进入判断导航流水线的知识地图阶段。

**路由规则：** 本步不运行 book-to-skill 的普通转换流程（Steps 0–10、Update/Fold-in）。本节说明就是本步的完整工作流。

**项目协调闸：** 在 `C:/Users/aa/Documents/ChatGPT/洗书` 项目内运行时，先读 `JUDGMENT_PIPELINE_STATUS.json（判断导航当前状态总账）` 和 `JUDGMENT_WRITE_OWNERSHIP.json（文件写入所有权表）`。当前范围被冻结、或本窗口不是登记的责任窗口时，保持只读并向主窗口报告；不得把状态或所有权复制进其他文档。

正式运行前，从工作单取得当前 `accepted_package_path`，并在建图前立即调用 `tools.register_accepted_package.run_authoritative_validation` 只读检查这一份书包。退出码非 0 即停止本书，即使旧状态文件写着"已登记"。不得用全书目 `--check` 的结果让另一本失败的书连坐本书。上游验证器必须已证明每一页都做过表格等保留结构的视觉检查；本步永不打开 PDF 重做或绕过该证明。

**输入闸：**

- 正式运行只接受 `accepted-package.json`；拒绝裸 `evidence_atoms.jsonl` 路径。
- 试验运行只接受 `artifact_scope = PILOT_TEMP` 的工作单，外加禁止发布、迁移和生产执行的 `PILOT_STATUS.json`。
- 从被接受的输入解析冻结原文原子路径；不接受后续提示替换输入。

**动作：** 不运行文档提取。不读 `book.md`、`pages.jsonl`、PDF、OCR 输出或其他来源来修补原子。只读锁定原子文件中允许范围内的记录，围绕它们建立导航元数据。

原子必备字段：

```text
evidence_atom_id
chapter_number
chapter_title
heading_path
content_role
exact_text
pdf_pages
citation
```

工作单必须写明允许的章节或原子范围。范围外内容只允许为过滤记录而查看；其 `exact_text` 不得用于任何综合。

只产出一层知识地图，不产出第二份原文库：

```text
references/knowledge/
├── chapter-map.json
├── topic-map.json
└── glossary.json
```

每个地图条目必须用 `evidence_atom_id` 或 `evidence_atom_ids` 定位来源，可以同时保留 `pdf_pages`、`citation`、`heading_path`、`content_role`。摘要、主题标签和术语解释只是导航辅助，永远不是证据。

硬边界：

- 永不合并、拆分、改写、修复或重新编号原文原子。
- 上游字段缺失时永不制造替代原子。
- 发现问题时把受影响的 `evidence_atom_id`、影响、阻塞阶段、状态和受影响方法写入 `UPSTREAM_ISSUES.json`，报告而不是修源。
- 唯一来源锚点是 `evidence_atom_id` 或 `evidence_atom_ids`；退役来源字段不得出现。
- 保留每条原子的 `content_role`。导言、译注、案例、举例和编辑材料可以作为辅助位置入图，但永不升级为通用判断方法证据。
- `pilot_only = true` 时，把该标志复制进每个生成的机器文件，强制 `publishable = false`，禁止迁移进正式运行。
- 知识地图只是"书内位置"的机器真相；不得把方法步骤或执行许可复制进去。
- `chapter-map.json` 必须恰好包含范围内每个 `evidence_atom_id` 一次。只比总数不够：校验必须比对精确编号集合，拒绝遗漏、重复和越界编号。
- 知识地图覆盖只证明每条原子有位置，不证明每条原子都做过判断方法审查；那是 Cangjie 阶段的独立全书审查，不得从主题或章节覆盖推断。

建图完成后，在同一锁定运行上下文内交给下一步（判断方法蒸馏）。正式运行继续引用已验收书包；试验运行继续引用同一 `PILOT_TEMP` 夹具。本步不决定任何命盘、案例或现实问题该怎样判断。

v2 判断批次的交接止于知识地图和已分类的原文范围。Cangjie 阶段的结构化 JSON 必须经唯一正式入口 `scripts/build_methods.py` 装配；本步和任何批次本地脚本都不得写 `method-recipes.json`。

知识地图阶段不得被误当成方法审查。Cangjie 生成方法前，下游总账必须单独对范围内每条原子记录实际语义角色和处理去向。完整章节地图只证明每条原子有位置，不证明没有漏掉判断方法。身份混杂、上下文缺失或原文不完整必须保持对下游阻塞可见，不得被摘要悄悄抹平。
