# Idea to Paper 使用说明

[English](idea-to-paper.md)

`idea-to-paper` 用来把经验型科研想法逐步变成可审计、有证据支撑的项目和论文。它尤其适合跨多个 session 的长期科研：从文献、实验一直追踪到论文中的每个 claim。

## 什么时候使用

适合这些场景：

- 从一个研究方向中寻找候选 idea；
- 检查新颖性、相似工作碰撞和可行性；
- 把模糊想法变成可证伪的研究方案；
- 初始化或恢复长期科研仓库；
- 设计 spike、smoke、pilot、formal 和 robustness 实验；
- 根据证据做 go/no-go 决策；
- 从真实项目产物出发写论文或审稿。

不要把它用于普通作文润色、单篇论文总结，或与科研生命周期无关的日常编码。

## 快速开始

```text
Use $idea-to-paper to 调研这个方向，找出最接近的工作，并给出 GO、PIVOT、HOLD 或 NO-GO 建议。
```

```text
Use $idea-to-paper to 把这个初步假设变成可证伪方案，设计 smoke、pilot 和 formal 实验闸门。
```

```text
Use $idea-to-paper to 恢复这个科研仓库的真实状态，并告诉我下一个证据闸门。
```

```text
Use $idea-to-paper to 根据这些实验产物建立 claim-evidence matrix，并按 P0/P1/P2 审查论文。
```

## 工作流

1. **发现 idea**：建立术语地图和文献簇。
2. **碰撞与可行性检查**：精读最近邻工作，给出有范围说明的闸门决策。
3. **可执行方案**：明确假设、证伪条件、指标、阈值、资源和风险。
4. **持久化项目状态**：每类事实只有一个权威文档，原始证据只追加、不悄悄改写。
5. **分级实验**：从工程链路验证逐步推进到冻结协议后的正式科学证据。
6. **构建论文**：先建立 claim-evidence 对照，再写作并进行独立审查。
7. **可选理论提升**：只形式化确实可推导的性质，诚实标注 conjecture。

## 持久化工作区

可以用下面的命令无覆盖地初始化研究状态：

```bash
python3 /path/to/idea-to-paper/scripts/init_research_workspace.py /path/to/project --title "Project Title" --dry-run
python3 /path/to/idea-to-paper/scripts/init_research_workspace.py /path/to/project --title "Project Title"
```

必须显式传入项目路径。先检查 dry-run；脚本会拒绝解析到项目外的路径，只在 `docs/research/` 下创建缺失文件，并保留所有已有内容。

## 可选 `grill-me` 交接

这个 skill 可以独立运行。在研究方案澄清阶段或 formal protocol 冻结前的一次限定追问中，可以在使用者显式调用或同意后，把尚未解决的决策直接交给原版 `grill-me`。

- 只有确实需要这次深度追问时，才检查当前运行时是否报告 `grill-me` 已安装或可调用；如果运行时清单无法确定，只检查标准安装目标是否存在，不打开其中内容。
- 对已经安装但不允许隐式调用的 `grill-me`，只提供可直接执行的显式调用，不提示重装。
- 如果没有，skill 会先说明 Grill 是可选项，再询问一次是否安装官方原版；拒绝后立即使用完整的内置追问流程。
- 使用者明确同意后，才把安装交给环境认可的 skill installer：只从 `mattpocock/skills` 安装缺失的官方 `grill-me` 及其所需 `grilling` 组件；目标已存在时中止，下载文件保持原样。
- 新安装的 skill 通常在下一轮可用；等待刷新期间仍可继续内置追问。
- handoff 只包含当前方案、固定约束、已解决和待解决决策以及退出条件。
- prompt 把 `grill-me` 限定为一次问一个问题并返回决策；不得写文件、安装、实现、运行实验、评估证据或推进研究阶段。
- 返回的决策仍由 `idea-to-paper` 对照证据核验，项目状态与阶段推进也只归 `idea-to-paper` 管理。
- 不把 Grill 的内部流程复制进 `idea-to-paper`，也不直接依赖 Grill 内部使用的 skill。
- 已安装 skill、全局配置、环境、同级仓库和项目无关文件一律只读。
- 可用性检查不校验、不计算哈希、不制作指纹，也不读取 Grill 的文件内容。
- 绝不修补、替换、更新、修复、重装或覆盖已有 skill。
- Grill 不替代文献证据、实验评估或论文审稿。

`idea-to-paper` 的所有写操作必须位于明确选中的研究项目内。初始化前要显式传入项目根目录，并先检查 dry-run。

## 证据底线

- 单个搜索入口没找到，不等于 idea 新颖。
- smoke run 只证明链路能跑，不证明科研 claim。
- formal 对比必须使用冻结协议和不可变 run manifest。
- 失败实验和负结果也必须保留。
- 论文中每个公开 claim 都必须对应来源或实验产物。
- 公式和定理必须来自已声明的假设，不能为了“显得高级”而制造。
