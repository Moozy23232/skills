# Idea to Paper Usage

[简体中文](idea-to-paper_zh.md)

`idea-to-paper` turns an empirical research idea into a staged, evidence-backed project and paper. It is designed for work that may span many sessions and must remain auditable from literature through experiments to written claims.

## When to Use

Use it to:

- discover candidate ideas from a research area;
- check novelty, collisions, and feasibility;
- convert a vague idea into a falsifiable research plan;
- initialize or resume a long-running research repository;
- design spike, smoke, pilot, formal, and robustness experiments;
- make go/no-go decisions from evidence;
- draft or review a paper from real project artifacts.

Do not use it for generic essay polishing, a one-off paper summary, or ordinary coding with no research lifecycle.

## Quick Start

```text
Use $idea-to-paper to survey this research direction, find the closest collisions, and recommend GO, PIVOT, HOLD, or NO-GO.
```

```text
Use $idea-to-paper to turn this tentative hypothesis into a falsifiable plan with smoke, pilot, and formal experiment gates.
```

```text
Use $idea-to-paper to recover the current state of this research repository and tell me the next evidence gate.
```

```text
Use $idea-to-paper to build a claim-evidence matrix from these experiment artifacts and review the paper for P0/P1/P2 issues.
```

## Workflow

1. **Idea discovery**: map terminology and literature clusters.
2. **Collision and feasibility**: inspect the nearest work and make a scoped gate decision.
3. **Executable specification**: clarify assumptions, falsifiers, metrics, thresholds, resources, and risks.
4. **Persistent state**: keep one authoritative document for each fact and preserve append-only evidence.
5. **Experiment ladder**: advance from engineering validation to frozen-protocol scientific evidence.
6. **Paper construction**: map claims to evidence before drafting and run independent review passes.
7. **Optional theory**: formalize only derivable properties and label conjectures honestly.

## Persistent Workspace

To initialize non-destructive research state:

```bash
python3 /path/to/idea-to-paper/scripts/init_research_workspace.py /path/to/project --title "Project Title" --dry-run
python3 /path/to/idea-to-paper/scripts/init_research_workspace.py /path/to/project --title "Project Title"
```

The explicit project path is required. Inspect the dry-run first; the script rejects resolved paths outside that project, creates missing files under `docs/research/`, and preserves all existing files.

## Optional `grill-me` Handoff

The skill is standalone. During research specification or one bounded pre-freeze pass, it can hand the unresolved decisions directly to the original `grill-me` when the user explicitly invokes or accepts it.

- Only when that interview is materially useful, the skill checks whether the runtime reports `grill-me` as installed or callable. If runtime inventory is inconclusive, it checks only whether the exact standard install destination exists and does not open its contents.
- An installed but non-implicit `grill-me` receives a ready-to-run explicit invocation; it is never offered for reinstallation.
- If it is absent, the skill says that Grill is optional and asks once whether to install the official original. Declining immediately returns to the complete built-in clarification loop.
- Explicit approval delegates installation to the approved skill installer. It installs only missing official `grill-me` and required `grilling` components from `mattpocock/skills`, aborts on existing destinations, and leaves downloaded files unchanged.
- A newly installed skill is normally available on the next turn; the built-in loop can continue while waiting.
- The handoff contains only the current proposal, fixed constraints, resolved and open decisions, and exit criteria.
- The prompt restricts `grill-me` to asking one question at a time and returning decisions. It must not write files, install anything, implement, run experiments, evaluate evidence, or advance the research phase.
- `idea-to-paper` verifies the returned decisions and remains the sole owner of project state and phase transitions.
- No Grill workflow is copied into `idea-to-paper`, and it does not depend directly on Grill's internal skills.
- Existing skills, global configuration, environments, sibling repositories, and unrelated project files remain read-only.
- The availability check does not validate, hash, fingerprint, or inspect Grill's file contents.
- It never patches, replaces, updates, repairs, reinstalls, or overwrites an existing skill.
- Grill never substitutes for literature evidence, experiment evaluation, or paper review.

All writes made by `idea-to-paper` stay inside the explicitly selected research project. Run the workspace initializer with an explicit project root and inspect its dry-run before applying changes.

## Evidence Guardrails

- Absence from one search is not proof of novelty.
- A smoke run proves plumbing, not a scientific claim.
- A formal comparison uses a frozen protocol and an immutable run manifest.
- Failed and negative experiments remain part of the evidence.
- Every visible paper claim maps to a source or experiment artifact.
- Equations and theorems must follow from declared assumptions, not presentation pressure.
