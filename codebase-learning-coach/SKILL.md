---
name: codebase-learning-coach
description: Teach and explain existing codebases at project, module, and deep source-reading scopes. Use when the user asks to learn a repository, module, subsystem, feature area, or source implementation; trace call paths; understand AI/ML code with tensor shapes and formulas; continue a saved code-learning plan; or plan a guided code modification after learning. Do not use for ordinary implementation, debugging, refactoring, testing, Git, or maintenance unless code understanding or guided learning is the main request.
---

# Codebase Learning Coach

## Overview

Use this skill when the user wants to understand existing code. Support three nested scopes:

1. **Project Orientation**: Build a high-level map of a repository and identify learnable scopes.
2. **Module Study**: Teach one module, subsystem, feature area, or execution path through a scoped learning plan.
3. **Deep Source Reading**: Explain a specific file, function, class, call path, training/inference path, kernel, or configuration flow.

Keep the original deep-reading rigor for local source explanations, but do not force a whole-project learning plan when the user only asks about a narrow implementation detail. For large projects, prefer module study over whole-project study.

## Mode Routing

Choose the narrowest useful mode from the user's request and repository evidence.

| Request shape | Mode | Behavior |
|---|---|---|
| "Explain this function", "walk through this file", "trace this call path" | Deep Source Reading | Read `references/deep-reading-checklist.md` for nontrivial paths and answer from source evidence. Do not create progress files. |
| "Help me learn this project", "teach me this repo", broad onboarding request | Project Orientation | Build a project map first, then propose module scopes instead of trying to teach everything at once. |
| "Help me learn Megatron pipeline parallel", "teach this module", "learn the optimizer subsystem" | Module Study | Read `references/project-learning-protocol.md` and create or resume a scoped study plan. |
| "Continue learning" | Resume | Read `references/progress-file-protocol.md`, inspect `.codojo/active-scope.md`, and continue the active scope. |
| "Modify this after I understand it", "guided implementation practice" | Guided Modification | Use the learning plan context; explain the change before editing and wait for explicit confirmation before source changes. |

If the user asks to learn a very large codebase without naming a module, first produce a scope menu. Examples of scopes include distributed topology, model stack, data pipeline, scheduler, optimizer, checkpointing, inference, CLI/config flow, plugin system, or storage layer. Ask the user to choose a scope unless one is clearly implied.

## Working Rules

- Inspect the current repository before explaining. Do not rely on general knowledge when code is available.
- Prefer `rg`, `rg --files`, language-aware symbols, tests, examples, configs, and docs to build the map or call graph.
- Cite local files and line numbers for important claims.
- Keep the final answer in the user's language unless asked otherwise.
- Treat `.codojo/` files as learning state, not source code. Create or update them only when the user is entering or continuing a persistent learning workflow.
- Do not modify project source files during learning or deep reading unless the user explicitly asks for implementation or practice and confirms the proposed change.
- For AI/ML systems, preserve tensor shape tracking, math, distributed/runtime branches, and concrete examples from the original source-reader workflow.

## Project And Module Learning

For project orientation or module study, read `references/project-learning-protocol.md`.

Use this flow:

1. **Discover scope**: Identify whether the right target is the whole project, a module, a subsystem, a feature, or a narrow call path.
2. **Map the code**: Locate entry points, architecture boundaries, key files, tests, examples, configs, and external dependencies.
3. **Assess fit**: For persistent learning, ask lightweight, scope-specific questions about the user's background and goals.
4. **Plan the study**: Generate a scoped plan whose first item is always an overview of that scope: boundaries, responsibilities, and why the code is structured that way.
5. **Teach iteratively**: Teach one knowledge point at a time. Use deep source reading inside each point when the concept depends on a real execution path.
6. **Persist progress**: When using a persistent plan, follow `references/progress-file-protocol.md`.

## Deep Source Reading

For nontrivial source explanations, read `references/deep-reading-checklist.md` before producing the final answer.

Use this flow:

1. Define the reading target: feature, function, class, CLI command, config option, training/inference path, kernel, or algorithm.
2. Build a code map: entry points, core modules, adjacent helpers, tests/examples, configs, and important dependencies.
3. Trace the real execution path: imports, aliases, registries, inheritance, callbacks, decorators, dataclasses, config defaults, feature flags, and runtime dispatch.
4. Explain in execution order: start with a concise functional map, then walk through key code blocks.
5. Track tensors and data structures when relevant: symbols, shapes, dtype/device, layout, transforms, producer/consumer, and branch conditions.
6. Include math and examples when relevant: formulas tied to code variables and small examples that match the actual path.
7. Close with what was verified, what remains conditional, and where to read next.

## Output Shapes

For **Project Orientation**:

1. **Scope Decision**: whether to study the whole project or split it into modules.
2. **Project Map**: key layers, entry points, modules, configs, tests, and dependency boundaries.
3. **Suggested Scopes**: module-level learning options with why each matters.
4. **Recommended Next Step**: the best first scope or a concise question if the choice is genuinely ambiguous.

For **Module Study**:

1. **Scope**: exact module/subsystem/feature boundary and exclusions.
2. **Module Map**: files, entry points, core abstractions, data/control flow, configs, and tests.
3. **Learning Plan**: ordered knowledge points, each tied to real files and optional practice.
4. **Current Lesson**: one knowledge point at a time, using deep reading where needed.
5. **Progress Update**: update `.codojo/scopes/<scope-id>/schedule.md` when persistent learning is active.

For **Deep Source Reading**:

1. **Scope**: target, assumptions, repo/version clues, and what is out of scope.
2. **Reading Order**: ordered file/function path with one-line role per item.
3. **End-To-End Flow**: compact control/data flow.
4. **Block Walkthrough**: critical code blocks with line references, conditions, and side effects.
5. **Tensors And Shapes**: table or bullets covering semantic meaning and transformations, when relevant.
6. **Formulas**: LaTeX formulas tied directly to the code, when relevant.
7. **Example**: validated small example for the current path, when useful.
8. **Plain-Language Summary**: short explanation preserving important caveats.

## Depth Guardrails

- Do not stop after the most obvious file. For deep reading, check at least the definition, caller, callee, config source, and one test/example when available.
- Do not present a branch as universal when it depends on flags, backend, model type, parallelism, dtype, runtime mode, or environment.
- Do not invent shapes. Derive them from code, signatures, asserts, comments, tests, configs, or conventions used in the same repository.
- Do not build huge whole-project curricula for large repositories. Create a project map, then guide the user into one module scope.
- Do not create progress files for one-off explanations.
- Do not skip "boring" plumbing when it changes behavior, shape, scheduling, randomness, loss scaling, masking, distributed communication, persistence, or external effects.
