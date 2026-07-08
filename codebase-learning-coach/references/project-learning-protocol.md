# Project And Module Learning Protocol

Use this protocol when the user wants to learn a repository, a module, a subsystem, or a feature area rather than receive a one-off source explanation.

## Scope Model

Always define the study scope before planning.

| Scope | When to use | Output |
|---|---|---|
| Project Orientation | User asks to learn a repository, especially a large one, without naming a subsystem | Project map plus suggested module scopes |
| Module Study | User names a module, subsystem, feature area, package, or execution path | Scoped assessment, plan, schedule, and lessons |
| Deep Source Reading | User asks about a specific file, class, function, call path, kernel, or config flow | Source-grounded explanation; no progress files |

For large repositories, do not generate a whole-project curriculum immediately. Produce a project map and suggest modules first. Examples of module scopes include training loop, inference path, distributed topology, pipeline parallelism, tensor parallel layers, optimizer, data loading, checkpointing, plugin system, storage layer, API layer, and CLI/config flow.

## S0: Scope Discovery

Build a quick repository map before choosing the study path.

Check:

- Top-level directories and package boundaries.
- Build and dependency files.
- CLI, server, script, notebook, or training entry points.
- Tests, examples, docs, configs, and sample runs.
- Frameworks, runtime services, external dependencies, and generated files.

For project orientation, output:

1. **Project Shape**: language, framework, entry points, major directories, tests/examples/configs.
2. **Suggested Study Scopes**: 5-10 scopes, each with key files and why it matters.
3. **Recommended First Scope**: one good starting point based on the user's likely goal.

Ask the user to choose a scope only when the choice is genuinely needed. If the user already named a module or feature, proceed with module study.

## S1: Scope-Specific Assessment

For persistent study, assess only what matters for the selected scope. Keep this lightweight:

- Ask 3-7 questions for a module.
- Ask 5-10 questions for a small whole-project study.
- Do not ask broad unrelated questions.
- Include the user's goal, time budget, preferred depth, and desired outcome.

Record the result in `.codojo/scopes/<scope-id>/assessment.md` when using persistent progress. If the user wants to skip assessment, write a short "assumptions" section instead and continue.

## S2: Learning Plan

Generate a scoped plan. The first knowledge point must always be an overview:

```text
0.1 Scope Overview: boundaries, responsibilities, and why this code is structured this way
```

Then order topics by dependency:

- Conceptual prerequisites before runtime paths.
- Entry points before internals.
- Data structures before algorithms that mutate them.
- Config flags before branches they control.
- Common path before specialized backends or distributed variants.

For each knowledge point include:

- ID and title.
- Type: theory, deep reading, practice, or mixed.
- Learning goal.
- Real files to read.
- Deep-reading target, if a call path or tensor/data flow matters.
- Optional practice task, if safe and useful.
- Verification command or check, when practice is included.

Keep module plans to 6-18 knowledge points. Whole-project plans should usually be avoided for large repositories; if unavoidable, keep them high-level and route into module scopes.

## S3: Guided Teaching

Teach one knowledge point at a time.

For each point:

1. State where it sits in the scope.
2. Explain why it exists.
3. Explain the core idea.
4. Ground it in real files and line references.
5. Invoke deep source reading for important call paths, config branches, tensor shapes, formulas, or runtime dispatch.
6. Offer a small practice task only if it is safe and aligned with the user's goal.
7. Update progress if persistent learning is active.

Do not silently advance after a major lesson. Ask whether to continue, go deeper, practice, or pause.

## Deep Reading Inside Lessons

Use the deep-reading checklist inside module study whenever a lesson depends on actual implementation behavior. This includes:

- Runtime entry to core implementation.
- Config-driven branches.
- Distributed or backend-specific behavior.
- Tensor or data structure transformations.
- Loss, reward, sampling, scheduling, serialization, or persistence logic.
- Failure boundaries and tests.

The lesson should not merely summarize the code. It should show how control/data moves through the scoped path and what conditions change that path.

## S4: Guided Modification

Use this only when the user explicitly wants to modify code after learning.

Before editing source files:

1. Propose the change.
2. List affected files and behavior.
3. Explain validation steps.
4. Wait for explicit confirmation such as "start", "execute", "make the change", or an equivalent clear instruction.

Keep modifications small and tied to the learned scope. Update `.codojo/scopes/<scope-id>/modification-plan.md` when persistent learning is active.

## Output Tone

- Prefer concise, source-grounded teaching over broad lectures.
- Use the user's language.
- Be clear about uncertainty and unverified branches.
- For large projects, keep orienting maps compact and push detail into the selected scope.
