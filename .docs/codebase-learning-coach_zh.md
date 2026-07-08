# Codebase Learning Coach 使用说明

[English](codebase-learning-coach.md)

`codebase-learning-coach` 用来帮助你按三个层次学习已有代码库：项目全景、模块学习、源码深读。

## 什么时候使用

适合这些场景：

- 想快速建立陌生仓库的整体地图。
- 想学习某个模块、子系统、功能域或执行路径。
- 想深入解释某个文件、函数、类、配置流、训练/推理路径或 kernel。
- 想继续之前保存的学习计划。
- 想在理解相关代码后，再做一个有引导的小改动。

不要把它当成通用实现、调试或重构 skill；除非当前任务的核心是理解代码或带学习目标的改动。

## 快速开始

在 Codex 里显式调用：

```text
Use $codebase-learning-coach to map this repository and suggest learning scopes.
```

大型项目建议先做项目地图：

```text
Use $codebase-learning-coach to help me learn this project. First map the major modules and suggest a good learning scope.
```

学习指定模块：

```text
Use $codebase-learning-coach to help me learn Megatron's pipeline parallelism module.
```

深读具体实现路径：

```text
Use $codebase-learning-coach to trace how this function is called and explain the key branches and tensor shapes.
```

## 学习模式

### 项目全景

适合在仓库陌生，或者项目太大、不适合直接整体学习时使用。

skill 会：

1. 扫描仓库结构、配置、测试、示例和入口。
2. 识别主要模块或子系统。
3. 推荐可学习的模块 scope。
4. 根据你的目标推荐第一个学习 scope。

这个模式应该保持高层视角。对于大型项目，不应该直接生成巨大的全项目学习计划。

### 模块学习

适合学习一个边界清晰的项目局部。

skill 会：

1. 定义模块边界和不包含的内容。
2. 建立模块地图，包括关键文件、入口、配置、测试和数据/控制流。
3. 生成限定 scope 的学习计划。
4. 一次讲一个知识点。
5. 在涉及真实运行逻辑时，把源码深读嵌入到课程里。

如果开启持久化学习，进度会保存在：

```text
.codojo/scopes/<scope-id>/
```

### 源码深读

适合一次性解释某段具体代码。

skill 会：

1. 明确阅读目标。
2. 建立调用链或实现路径地图。
3. 按执行顺序解释，并引用文件和行号。
4. 在相关时追踪关键数据结构、tensor shape、分支、公式和例子。

这个模式不会创建 `.codojo/` 进度文件。

## 持久化进度

持久化学习会在目标仓库中使用 `.codojo/`：

```text
.codojo/
├── project-map.md
├── active-scope.md
└── scopes/
    └── <scope-id>/
        ├── assessment.md
        ├── task.md
        ├── schedule.md
        ├── notebook.md
        ├── modification-plan.md
        └── readings/
```

只有在你希望跨 session 继续学习时才使用它。如果只是一次性解释源码，直接要求源码深读即可。

## 常用提示词

```text
Use $codebase-learning-coach to map this repository and suggest 5-10 module learning scopes.
```

```text
Use $codebase-learning-coach to create a module study plan for the optimizer subsystem.
```

```text
Use $codebase-learning-coach to continue my active learning scope from .codojo.
```

```text
Use $codebase-learning-coach to deep-read the training step implementation and track tensor shapes.
```

```text
Use $codebase-learning-coach to help me plan a small guided modification after I understand this module.
```

## 安全约定

- 项目全景和源码深读阶段不应该修改源码。
- 引导式改动必须先给出方案，并等用户明确确认后才能改源码。
- `.codojo/` 文件是学习状态，不是应用源码。
- 大型项目优先做模块学习，不要直接生成全项目学习计划。
