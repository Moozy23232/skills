# Progress File Protocol

Use this protocol only for persistent project or module learning. Do not create `.codojo/` files for one-off source explanations.

## Directory Layout

Store learning state under the target repository:

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
            └── 001-topic-slug.md
```

`project-map.md` is shared across scopes. Each module or subsystem gets its own scope directory so a user can learn multiple parts of a large codebase without mixing progress.

## Scope IDs

Create stable, lowercase, hyphen-case scope IDs:

- Use the module or feature name when clear: `pipeline-parallel`, `tensor-parallel`, `optimizer`, `api-routing`.
- Prefix with a package or subsystem if needed: `megatron-pipeline-parallel`, `server-auth`, `ui-state-management`.
- Avoid spaces, slashes, uppercase letters, and punctuation.

Record the active scope in `.codojo/active-scope.md`:

```markdown
# Active Learning Scope

- Scope ID: pipeline-parallel
- Title: Pipeline Parallelism
- Status: In progress
- Last updated: 2026-07-08
- Scope directory: `.codojo/scopes/pipeline-parallel/`
```

## project-map.md

Use this for repository-level orientation:

```markdown
# Project Map

## Project Shape

- Language:
- Frameworks:
- Entry points:
- Build/test commands:
- Important configs:

## Major Areas

| Area | Key files | Why it matters |
|---|---|---|
| <area> | `<path>`, `<path>` | <role> |

## Suggested Study Scopes

| Scope ID | Title | Key files | Recommended for |
|---|---|---|---|
```

Update `project-map.md` when new repository evidence changes the map, not after every lesson.

## assessment.md

Use this for scope-specific user background and goals:

```markdown
# Assessment: <Scope Title>

## Scope

- Scope ID:
- Boundary:
- Out of scope:

## User Goals

- Goal:
- Time budget:
- Preferred depth:
- Desired outcome:

## Background

| Topic | User level | Notes |
|---|---|---|

## Assumptions

- <assumption if assessment was skipped or incomplete>
```

## task.md

Use this for the scoped study plan:

```markdown
# Learning Plan: <Scope Title>

## Scope

- Boundary:
- Out of scope:
- Main entry points:

## Knowledge Points

| ID | Topic | Type | Files | Goal | Practice |
|---|---|---|---|---|---|
| 0.1 | Scope Overview | theory | `<path>` | Understand boundaries, responsibilities, and structure | None |
```

The first row must be `0.1 Scope Overview`.

## schedule.md

Use simple status words so the file stays portable:

```markdown
# Learning Schedule: <Scope Title>

Overall progress: 0/N

| ID | Topic | Status | Theory | Practice | Last updated |
|---|---|---|---|---|---|
| 0.1 | Scope Overview | Not started | Not started | N/A | - |

## Log

<!-- Append concise progress notes here. -->
```

Allowed statuses:

- `Not started`
- `In progress`
- `Done`
- `Skipped`
- `Blocked`
- `N/A`

When a lesson starts, mark the topic `In progress`. When the user completes or skips the point, update status and append a log entry.

## readings/

Use `readings/` for durable deep-read notes that are useful later. Do not save every explanation automatically.

Create a reading note when:

- The user asks to save it.
- A lesson includes a complex call path.
- The explanation will be reused by later lessons.

Format:

```markdown
# Deep Reading: <Topic>

## Target

- Scope:
- Entry point:
- Main files:

## Reading Order

## Control/Data Flow

## Important Branches

## Tensors Or Data Structures

## Open Questions
```

## notebook.md

Use `notebook.md` only when the user asks to remember something or when a lesson summary is important enough to preserve.

Append concise notes under headings. Do not copy entire chat responses.

## modification-plan.md

Create this only after the user chooses guided modification:

```markdown
# Modification Plan: <Scope Title>

## Goal

## Tasks

| ID | Task | Files | Status | Validation |
|---|---|---|---|---|

## Change Log
```

Do not edit source files just because this file exists. Source edits still require explicit user confirmation.

## Resume Rules

When the user says "continue learning":

1. Read `.codojo/active-scope.md`.
2. Read that scope's `schedule.md` and `task.md`.
3. Continue the first `In progress` item; otherwise continue the first `Not started` item.
4. If no active scope exists, read `project-map.md` and ask which scope to continue.

If files conflict, explain the conflict and ask for a decision. Do not silently overwrite user-edited learning files.
