<div align="center">

# Skills

面向科研与源码学习、可在不同 AI 编程工具中复用的 skills。

[English](README.md)

</div>

## 可用 Skills

选择下面的 skill，点击名称查看完整说明，然后在支持 skill 的 AI 编程工具中调用。

### [`codebase-learning-coach`](.docs/codebase-learning-coach_zh.md)

从项目、模块或具体源码三个层次学习陌生代码库。它可以梳理仓库结构、追踪真实调用链和数据流、解释实现细节，并持续记录长期学习进度。

### [`idea-to-paper`](.docs/idea-to-paper_zh.md)

把研究方向、初步想法或已有项目推进成可复现实验和有证据支撑的论文。它可以调研相近工作、检查可行性、规划实验、恢复长期研究状态，并让论文结论与真实结果保持对应。

## 快速开始

只安装你需要的 skill。将 `<skill-name>` 替换为下方任意 skill 的目录名。

### 在 Codex 中安装

让 Codex 直接从对应目录安装：

```text
$skill-installer install https://github.com/Moozy23232/skills/tree/main/<skill-name>
```

安装后的 skill 会从下一轮对话开始可用；如果没有出现，重启 Codex。

### 在其他兼容的 AI 编程工具中安装

可以使用 [skills CLI](https://github.com/vercel-labs/skills)，把同一个目录安装到 Codex、Claude Code、Cursor 等兼容工具：

```bash
npx skills add https://github.com/Moozy23232/skills/tree/main/<skill-name> -g
```

安装程序会询问目标 AI 编程工具。`-g` 表示在所有项目中可用；去掉它则只安装到当前项目。
