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
python3 /path/to/idea-to-paper/scripts/init_research_workspace.py /path/to/project --title "Project Title"
```

脚本只会在 `docs/research/` 下创建缺失文件，不会覆盖已有内容。

## 证据底线

- 单个搜索入口没找到，不等于 idea 新颖。
- smoke run 只证明链路能跑，不证明科研 claim。
- formal 对比必须使用冻结协议和不可变 run manifest。
- 失败实验和负结果也必须保留。
- 论文中每个公开 claim 都必须对应来源或实验产物。
- 公式和定理必须来自已声明的假设，不能为了“显得高级”而制造。
