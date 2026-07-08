# Codebase Learning Coach Usage

[简体中文](codebase-learning-coach_zh.md)

`codebase-learning-coach` helps you learn existing codebases at three levels: project orientation, module study, and deep source reading.

## When To Use

Use this skill when you want to:

- Build a map of an unfamiliar repository.
- Learn one module, subsystem, feature area, or execution path.
- Deeply explain a source file, function, class, config flow, training/inference path, or kernel.
- Continue a saved learning plan.
- Plan a guided code change after understanding the relevant code.

Do not use it as a generic implementation or debugging skill unless code understanding or guided learning is the main goal.

## Quick Start

Invoke the skill explicitly in Codex:

```text
Use $codebase-learning-coach to map this repository and suggest learning scopes.
```

For large repositories, start with a project map:

```text
Use $codebase-learning-coach to help me learn this project. First map the major modules and suggest a good learning scope.
```

For a specific module:

```text
Use $codebase-learning-coach to help me learn Megatron's pipeline parallelism module.
```

For a narrow implementation path:

```text
Use $codebase-learning-coach to trace how this function is called and explain the key branches and tensor shapes.
```

## Learning Modes

### Project Orientation

Use this when the repository is unfamiliar or too large to learn directly.

The skill will:

1. Inspect the repository structure, configs, tests, examples, and entry points.
2. Identify major modules or subsystems.
3. Suggest practical study scopes.
4. Recommend a first scope based on your goal.

This mode should stay high level. It should not create a huge whole-project curriculum for large projects.

### Module Study

Use this when you want to learn a bounded part of a project.

The skill will:

1. Define the module boundary and what is out of scope.
2. Build a module map with key files, entry points, configs, tests, and data/control flow.
3. Create a scoped learning plan.
4. Teach one knowledge point at a time.
5. Use deep source reading inside lessons when runtime behavior matters.

If persistent learning is active, progress is stored under:

```text
.codojo/scopes/<scope-id>/
```

### Deep Source Reading

Use this for one-off explanations of specific code.

The skill will:

1. Define the reading target.
2. Build a call path or implementation map.
3. Explain the execution order with file and line references.
4. Track key data structures, tensor shapes, branches, formulas, and examples when relevant.

This mode does not create `.codojo/` progress files.

## Persistent Progress

Persistent learning uses `.codojo/` in the target repository:

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

Use this only when you want to continue learning across sessions. For one-off source explanations, ask for deep source reading instead.

## Useful Prompts

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

## Safety Notes

- The skill should not edit source code during project orientation or deep reading.
- Guided modifications require an explicit plan and user confirmation before source edits.
- `.codojo/` files are learning state, not application source files.
- For large projects, prefer module study over a whole-project learning plan.
