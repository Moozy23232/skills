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
python3 /path/to/idea-to-paper/scripts/init_research_workspace.py /path/to/project --title "Project Title"
```

The script creates missing files under `docs/research/` and preserves all existing files.

## Evidence Guardrails

- Absence from one search is not proof of novelty.
- A smoke run proves plumbing, not a scientific claim.
- A formal comparison uses a frozen protocol and an immutable run manifest.
- Failed and negative experiments remain part of the evidence.
- Every visible paper claim maps to a source or experiment artifact.
- Equations and theorems must follow from declared assumptions, not presentation pressure.
