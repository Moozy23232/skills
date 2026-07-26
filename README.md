<div align="center">

# Skills

Reusable skills for research and code learning with AI coding tools.

[简体中文](README_zh.md)

</div>

## Available Skills

Choose a skill below, click its name for the full guide, and invoke it in a compatible AI coding tool.

### [`codebase-learning-coach`](.docs/codebase-learning-coach.md)

Learn an unfamiliar codebase at the project, module, or source level. It can map a repository, trace real call paths and data flow, explain implementation details, and keep a long-running learning plan.

### [`idea-to-paper`](.docs/idea-to-paper.md)

Turn a research direction, tentative idea, or existing project into reproducible experiments and an evidence-backed paper. It can investigate nearby work, test feasibility, plan experiments, resume research state, and connect paper claims to actual results.

## Getting Started

Install only the skill you need. Replace `<skill-name>` with the directory name of any skill listed below.

### Codex

Ask Codex to install the skill directly from its directory:

```text
$skill-installer install https://github.com/Moozy23232/skills/tree/main/<skill-name>
```

The skill is available from the next turn. If it does not appear, restart Codex.

### Other Compatible AI Coding Tools

The [skills CLI](https://github.com/vercel-labs/skills) can install the same directory for Codex, Claude Code, Cursor, and other compatible tools:

```bash
npx skills add https://github.com/Moozy23232/skills/tree/main/<skill-name> -g
```

The installer asks which AI coding tool to target. `-g` makes the skill available across projects; omit it to install into the current project.
