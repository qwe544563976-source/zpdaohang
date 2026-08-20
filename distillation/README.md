# BPHS 97 正式蒸馏工作区

把仓库里的正式书包加工成判断导航方法配方，给 RAG（查原文系统）当路标。
所有规则以 `book-to-judgment-navigation/SKILL.md`（必读卡）为准，本文只讲这个工作区怎么跑。

## 三个脚本

| 脚本 | 做什么 | 什么时候跑 |
|---|---|---|
| `setup_workspace.py` | 解 `2024/BPHS97_2024_formal_package.zip` 到 `_local/`（不入库），做蒸馏窗口独立复算，生成本地重定位包 `accepted-package.local.json` | 每次换机器、换容器后先跑一次 |
| `check_fragment.py` | 把一组抽取片段包成完整 extraction，跑唯一入口 `build_methods.py --check-only` 自验 | 抽取窗口每写完一组就跑，直到 `passed=true` |
| `make_batch.py` | 合并全部片段 → 装配机器配方 → 生成知识地图与工作单 → 渲染人读派生文件 → `--require-v2` 机械验收 | 全部片段自验通过后跑一次 |

```bash
python distillation/setup_workspace.py                       # 开工闸门
python distillation/check_fragment.py <片段.json>            # 抽取自验（反复）
python distillation/make_batch.py                            # 合成批次并机械验收
```

## 为什么要"本地重定位包"

书包凭证里的 `evidence_atoms.path` 是切卡窗口本机的 `F:\切卡实验\...`，在别的机器上不存在。
`setup_workspace.py` 复制一份 `accepted-package.local.json`，**只改这一个路径字段**，
其余（`package_id`、`content_sha256`、`upstream_gates`、`created_at_utc` 等）逐字不动，
并把原路径、新路径和"两边内容哈希相同"的证明写进 `_local/PACKAGE_RELOCATION.json`。

内容摘要不变是关键：装配器和验证器都会重算 `evidence_atoms.jsonl` 的 sha256 并与凭证比对，
一个字节都改不了。所以重定位只搬位置，改不了原文。

## `_local/` 里有什么（都不入库）

```text
_local/
├── evidence_atoms.jsonl          2024 条冻结原文原子（zip 解出，只读）
├── accepted-package.local.json   本地重定位包
├── PACKAGE_RELOCATION.json       重定位留痕与独立复算结果
├── groups/                       按批次切好的分组原文（抽取窗口的输入）
└── fragments/                    各组抽取片段（自验通过后由 make_batch 合并）
```

库内真相是 `2024/BPHS97_2024_formal_package.zip` 本身；`_local/` 是它的派生物，随时可重建。

## 批次产物在哪

`bphs-97/batches/<批次编号>/`。机器真相只有两份：
`references/navigation/method-recipes.json`（方法）和 `query-recipes.json`（主题）；
人读文件全部由验证器 `--render-derived` 生成，手改即判失败。

## 这一批做完之后

批次目录做到"机器验收通过"为止。接下来两步不在本环境做：

1. **独立语义审计**：由未参与生成的窗口按 `references/terra-audit-prompt.md` 出
   `independent-semantic-audit/v3` 报告（逐步骤绑 `step_hash`、高风险词逐词单选）。
2. **并入全书总账**：用 `merge_method_batch.py` 并入用户本机那份含已并入方法的全书总账
   （总账不在本仓库，所以合并只能在用户本机做）。
