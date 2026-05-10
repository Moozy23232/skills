# skills

个人 Codex skills 仓库，用来存放和迭代我自己的工作流技能。

每个 skill 使用独立目录，目录名采用 lowercase hyphen-case，例如：

```text
ai-source-code-reader/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── deep-reading-checklist.md
```

## Skills

### ai-source-code-reader

源码阅读辅助 skill，面向 AI/ML 相关代码库，例如 Megatron-LM、vLLM、VeRL、Ms-Swift、TinyZero、Search-R1 等。

它的目标是避免只看表层调用或凭印象解释代码，要求按真实调用链阅读源码，并在讲解中覆盖：

- 功能级阅读顺序和调用路径
- 关键代码逐段或逐行解释
- 配置、后端、分布式、精度、性能相关分支
- 张量含义、shape、dtype/device 和 shape 变化
- 代码对应的数学公式
- 与当前代码路径一致的具体例子
- 最后的通俗总结和未验证条件说明

默认调用方式：

```text
Use $ai-source-code-reader 来按真实调用链解释这段 AI 源码，并说明张量 shape、公式和贴合代码的例子。
```

## Adding A Skill

新增 skill 时保持以下约定：

1. 目录名使用小写英文和连字符。
2. 必须包含 `SKILL.md`，并在 frontmatter 中写清楚 `name` 和 `description`。
3. 如果有较长的流程、清单或领域知识，放到 `references/`，只在 `SKILL.md` 中保留核心工作流和入口说明。
4. 如果需要 UI 展示信息，放到 `agents/openai.yaml`。
5. 提交前运行基础校验：

```bash
python3 /home/lzhih/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>
```
