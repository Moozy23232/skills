# Persistent Research State Protocol

Use this protocol when a research project spans sessions or agents.

## Canonical Roles

Default to `docs/research/` unless the repository already has equivalent authoritative files.

```text
docs/research/
├── README.md                    # authoritative map and five-minute status
├── overview.md                  # stable problem, claim, scope, and roadmap
├── CONTEXT.md                   # constraints and resolved/open decisions
├── plans/live-plan.md           # only the currently executable plan
├── literature/evidence-ledger.md
├── notes/log.md                 # append-only dated observations
├── experiments/
│   ├── index.md
│   ├── protocols/               # frozen protocol versions
│   └── runs/                    # immutable run manifests
├── paper/claim-evidence.md
└── archive/                     # superseded plans and snapshots
```

Map these roles onto existing project files instead of duplicating them.

## Ownership Rules

- Keep `README.md` short: current phase, last verified event, strongest result, blocker, and next gate.
- Keep `overview.md` stable: research question, motivation, proposed mechanism, claim boundary, non-goals, and roadmap.
- Record each material choice in `CONTEXT.md` with date, decision, rationale, evidence, owner, and superseded decision.
- Keep only live tasks in `plans/live-plan.md`; move completed or abandoned plans to `archive/`.
- Append observations to `notes/log.md`; do not rewrite history to match later understanding.
- Freeze protocol files before formal runs. Create a new version for any post-freeze change.
- Keep each run manifest immutable after finalization. Add a correction note rather than silently altering it.
- Use `paper/claim-evidence.md` as the only authoritative mapping from paper claims to evidence.

Never store the same fact as independently editable prose in several files. Link to the owning document.

## Session Recovery

At session start:

1. Read the map, overview, context, live plan, experiment index, claim-evidence matrix, and newest manifests.
2. Inspect actual repository status, recent commits, configs, logs, and artifacts.
3. Compare prose status with evidence.
4. Report:
   - stable research question;
   - current phase and gate;
   - last verified event;
   - strongest positive and negative evidence;
   - unresolved decisions and blockers;
   - next smallest action.
5. Resolve contradictions before changing code or running experiments.

If no authoritative state is discoverable, reconstruct a snapshot from evidence and mark uncertain fields rather than guessing.

## Update Transaction

After meaningful work:

1. Save raw artifacts and finalize the run manifest.
2. Append observations and failures to the log.
3. Update the experiment index.
4. Update decisions only when evidence changes them.
5. Update the claim-evidence matrix.
6. Advance or revise the live plan.
7. Refresh the five-minute status last.
8. Archive superseded documents with links to their replacements.

Keep updates small enough that the Git diff reveals what changed and why.

## Status Vocabulary

Use explicit states:

- `draft`: editable and not yet relied upon;
- `active`: currently authoritative;
- `frozen`: inputs fixed for a named experiment;
- `completed`: exit criteria met;
- `failed`: exit criteria not met, with evidence retained;
- `superseded`: replaced, with successor linked;
- `blocked`: a named dependency prevents progress.

Do not use vague labels such as “mostly done” without measurable exit criteria.
